"""Free, no-API-key data collectors for an account brief.

Usage:
    python3 -m hixbrain.collect delta.com [--name "Delta Air Lines"] [--ticker DAL] [--out path.json]

Runs every collector in parallel and prints one JSON document of evidence.
Each collector degrades gracefully: if a host is blocked or down, its section
records {"status": "unavailable", "error": ...} and the brief workflow falls
back to web search for that lane.

Set HIXBRAIN_SEC_USER_AGENT to "<your name> <your email>" — SEC EDGAR
rejects requests without a contact User-Agent.
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

from . import signatures as sig

TIMEOUT = 12
BROWSER_UA = "Mozilla/5.0 (compatible; HixBrain/0.1; account research)"
SEC_UA = os.environ.get("HIXBRAIN_SEC_USER_AGENT", "HixBrain account research (set HIXBRAIN_SEC_USER_AGENT)")


def fetch(url, ua=BROWSER_UA, accept="*/*"):
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": accept})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read(4_000_000)
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.geturl(), raw.decode(charset, errors="replace")


def fetch_json(url, ua=BROWSER_UA):
    _, body = fetch(url, ua=ua, accept="application/json")
    return json.loads(body)


def strip_html(text):
    text = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", text)
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def unavailable(err):
    return {"status": "unavailable", "error": f"{type(err).__name__}: {err}"[:300]}


# --------------------------------------------------------------------------- website

SITE_PATHS = ["", "contact", "contact-us", "support", "help", "customer-service", "customer-support", "about", "about-us", "careers"]


def collect_website(domain):
    base = f"https://{domain.strip('/')}"
    pages, errors = {}, {}

    def grab(path):
        url = f"{base}/{path}"
        try:
            final, body = fetch(url)
            return path, final, body, None
        except Exception as e:  # noqa: BLE001 - every failure is just "no data"
            return path, url, None, e

    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        for path, final, body, err in pool.map(grab, SITE_PATHS):
            if body is not None:
                pages[final] = body
            else:
                errors[path or "/"] = f"{type(err).__name__}: {err}"[:160]

    if not pages:
        return {"status": "unavailable", "error": "no pages reachable", "attempts": errors}

    vendors, toll, other = {}, set(), set()
    for url, body in pages.items():
        for vendor, cat in sig.detect_vendors(body).items():
            vendors.setdefault(vendor, {"category": cat, "seen_on": []})["seen_on"].append(url)
        t, o = sig.find_phone_numbers(strip_html(body))
        toll |= t
        other |= o

    home = next(iter(pages.values()))
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", home)
    desc = re.search(r'(?is)<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)', home)
    support_text = " ".join(strip_html(b) for b in pages.values()).lower()
    return {
        "status": "ok",
        "pages_fetched": list(pages),
        "title": html.unescape(title.group(1).strip()) if title else None,
        "description": html.unescape(desc.group(1).strip()) if desc else None,
        "detected_vendors": vendors,
        "toll_free_numbers": sorted(toll),
        "other_phone_numbers": sorted(other)[:25],
        "mentions_24_7": bool(re.search(r"24/7|24 hours a day|around the clock", support_text)),
        "mentions_chat": bool(re.search(r"live chat|chat with us|virtual assistant|chat now", support_text)),
    }


# --------------------------------------------------------------------------- SEC EDGAR


def _sec_lookup(name, ticker):
    data = fetch_json("https://www.sec.gov/files/company_tickers.json", ua=SEC_UA)
    rows = list(data.values())
    if ticker:
        for r in rows:
            if r["ticker"].upper() == ticker.upper():
                return r
    if name:
        n = re.sub(r"[^a-z0-9 ]", "", name.lower())
        exact = [r for r in rows if re.sub(r"[^a-z0-9 ]", "", r["title"].lower()) == n]
        if exact:
            return exact[0]
        starts = [r for r in rows if re.sub(r"[^a-z0-9 ]", "", r["title"].lower()).startswith(n)]
        if starts:
            return starts[0]
    return None


def _keyword_passages(text, keywords, per_kw=2, width=260):
    out = {}
    low = text.lower()
    for kw in keywords:
        hits, start = [], 0
        while len(hits) < per_kw:
            i = low.find(kw, start)
            if i < 0:
                break
            a, b = max(0, i - width // 2), min(len(text), i + width // 2)
            hits.append("…" + text[a:b].strip() + "…")
            start = i + len(kw) + width
        if hits:
            out[kw] = hits
    return out


def collect_sec(name, ticker):
    try:
        row = _sec_lookup(name, ticker)
        if not row:
            return {"status": "not_found", "note": "No SEC registrant matched — likely private. Use web search for financials."}
        cik = str(row["cik_str"]).zfill(10)
        sub = fetch_json(f"https://data.sec.gov/submissions/CIK{cik}.json", ua=SEC_UA)
        recent = sub["filings"]["recent"]
        filings = [
            {"form": f, "date": d, "url": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{doc}"}
            for f, d, acc, doc in zip(recent["form"], recent["filingDate"], recent["accessionNumber"], recent["primaryDocument"])
        ]
        notable = [x for x in filings if x["form"] in ("10-K", "10-Q", "8-K", "DEF 14A", "20-F")][:15]
        annual = next((x for x in filings if x["form"] in ("10-K", "20-F")), None)
        result = {
            "status": "ok",
            "registrant": sub.get("name"),
            "cik": cik,
            "tickers": sub.get("tickers"),
            "sic_description": sub.get("sicDescription"),
            "fiscal_year_end": sub.get("fiscalYearEnd"),
            "recent_filings": notable,
        }
        if annual:
            _, body = fetch(annual["url"], ua=SEC_UA)
            text = strip_html(body)
            emp = re.search(r"(?i)(approximately|about|over|more than)?\s*([\d,]{3,})\s+(full-time\s+)?(employees|team members|associates)", text)
            result["annual_report"] = {
                "form": annual["form"],
                "date": annual["date"],
                "url": annual["url"],
                "employees_phrase": emp.group(0).strip() if emp else None,
                "keyword_passages": _keyword_passages(text, sig.FILING_KEYWORDS),
            }
        return result
    except Exception as e:  # noqa: BLE001
        return unavailable(e)


# --------------------------------------------------------------------------- job boards


def slug_candidates(domain, name):
    root = domain.lower().split(".")
    root = root[-2] if len(root) >= 2 else root[0]
    cands = [root]
    if name:
        compact = re.sub(r"[^a-z0-9]", "", name.lower())
        first = re.sub(r"[^a-z0-9]", "", name.lower().split()[0])
        cands += [compact, first]
    seen, out = set(), []
    for c in cands:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def _board_greenhouse(slug):
    data = fetch_json(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    return [{"title": j["title"], "location": (j.get("location") or {}).get("name"), "url": j.get("absolute_url")} for j in data.get("jobs", [])]


def _board_lever(slug):
    data = fetch_json(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    return [{"title": j["text"], "location": (j.get("categories") or {}).get("location"), "url": j.get("hostedUrl")} for j in data]


def _board_ashby(slug):
    data = fetch_json(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
    return [{"title": j["title"], "location": j.get("location"), "url": j.get("jobUrl")} for j in data.get("jobs", [])]


def _board_smartrecruiters(slug):
    data = fetch_json(f"https://api.smartrecruiters.com/v1/companies/{slug}/postings?limit=100")
    return [{"title": j["name"], "location": (j.get("location") or {}).get("city"), "url": f"https://jobs.smartrecruiters.com/{slug}/{j['id']}"} for j in data.get("content", [])]


BOARDS = {"greenhouse": _board_greenhouse, "lever": _board_lever, "ashby": _board_ashby, "smartrecruiters": _board_smartrecruiters}


def summarize_jobs(jobs):
    buckets = {}
    for j in jobs:
        b = sig.classify_title(j["title"] or "")
        if b:
            buckets.setdefault(b, []).append(j)
    return {
        "total_open_roles": len(jobs),
        "bucket_counts": {k: len(v) for k, v in buckets.items()},
        "examples": {k: v[:8] for k, v in buckets.items()},
        "vendors_in_titles": sig.detect_vendors(" ".join(j["title"] or "" for j in jobs)),
    }


def collect_jobs(domain, name):
    attempts = {}
    for slug in slug_candidates(domain, name):
        for board, fn in BOARDS.items():
            try:
                jobs = fn(slug)
            except urllib.error.HTTPError as e:
                attempts[f"{board}:{slug}"] = f"HTTP {e.code}"
                continue
            except Exception as e:  # noqa: BLE001 - network blocked / DNS / timeout
                attempts[f"{board}:{slug}"] = f"{type(e).__name__}: {e}"[:120]
                continue
            if jobs:
                return {"status": "ok", "board": board, "slug": slug, **summarize_jobs(jobs)}
            attempts[f"{board}:{slug}"] = "empty"
    if attempts and not any(v.startswith("HTTP") or v == "empty" for v in attempts.values()):
        return {"status": "unavailable", "error": "job board APIs unreachable from this network", "attempts": attempts}
    return {
        "status": "not_found",
        "note": "No public Greenhouse/Lever/Ashby/SmartRecruiters board found (large enterprises often use Workday/iCIMS/Taleo). Use web search: site:<careers domain> or '<company> customer service representative jobs'.",
        "attempts": attempts,
    }


# --------------------------------------------------------------------------- main


def collect(domain, name=None, ticker=None):
    domain = re.sub(r"^https?://", "", domain).strip("/").removeprefix("www.")
    started = dt.datetime.now(dt.timezone.utc)
    with cf.ThreadPoolExecutor(max_workers=3) as pool:
        futs = {
            "website": pool.submit(collect_website, f"www.{domain}"),
            "sec": pool.submit(collect_sec, name or domain.split(".")[0], ticker),
            "jobs": pool.submit(collect_jobs, domain, name),
        }
        out = {k: f.result() for k, f in futs.items()}
    if out["website"].get("status") != "ok":
        out["website"] = collect_website(domain)  # retry apex domain
    return {
        "domain": domain,
        "name": name,
        "ticker": ticker,
        "collected_at": started.isoformat(timespec="seconds"),
        "elapsed_seconds": round((dt.datetime.now(dt.timezone.utc) - started).total_seconds(), 1),
        **out,
    }


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("domain")
    p.add_argument("--name")
    p.add_argument("--ticker")
    p.add_argument("--out")
    a = p.parse_args(argv)
    result = collect(a.domain, a.name, a.ticker)
    doc = json.dumps(result, indent=2)
    if a.out:
        os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        with open(a.out, "w") as f:
            f.write(doc)
    print(doc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
