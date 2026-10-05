"""Render one or more brief Markdown files into a single print-ready PDF.

Usage:
    python3 -m hixbrain.render_pdf briefs/acme-prep.md briefs/acme.md \
        --out briefs/acme.pdf --title "Acme — Internal Pre-Meeting Prep" [--internal]

Each input file starts on a new page. Uses headless Chromium for layout
(set HIXBRAIN_CHROME to override the browser path). Requires: pip install markdown
"""

import argparse
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

import markdown

# Emoji don't render reliably in headless Chromium without an emoji font, so
# swap the brief's markers for styled text badges.
BADGES = [
    ("🧠 Hypothesis:", '<span class="badge hyp">Hypothesis</span>'),
    ("🧠", '<span class="badge hyp">Hypothesis</span>'),
    ("⚠️", '<span class="badge stale">Stale</span>'),
    ("⚙️", ""),
    ("🔥🔥🔥", '<span class="heat">High</span>'),
    ("🔥🔥", '<span class="heat">Med</span>'),
    ("🔥", '<span class="heat">Low</span>'),
]

CSS = """
@page { size: Letter; margin: 0.6in 0.6in 0.7in; }
* { box-sizing: border-box; }
body { font-family: "Liberation Sans", "DejaVu Sans", Arial, sans-serif; font-size: 9.5pt;
       line-height: 1.38; color: #1a1d21; margin: 0; }
.banner { background: #13151a; color: #fff; padding: 10px 14px; border-radius: 4px; margin-bottom: 14px;
          display: flex; justify-content: space-between; align-items: center; font-size: 8.5pt; }
.banner b { color: #13ef93; letter-spacing: .08em; }
h1 { font-size: 19pt; margin: 0 0 4px; line-height: 1.2; }
h2 { font-size: 12.5pt; margin: 18px 0 6px; padding-bottom: 3px; border-bottom: 2px solid #13ef93;
     break-after: avoid; }
h3 { font-size: 10.5pt; margin: 12px 0 4px; break-after: avoid; }
p { margin: 4px 0 8px; }
ul, ol { margin: 4px 0 8px; padding-left: 20px; }
li { margin: 2px 0; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 8.6pt; break-inside: auto; }
tr { break-inside: avoid; }
thead:not(:has(th:not(:empty))) { display: none; }  /* "| | |" key-value tables */
th { background: #eef1f4; text-align: left; font-weight: 700; }
th, td { border: 1px solid #d5dae0; padding: 4px 6px; vertical-align: top; }
blockquote { margin: 6px 0 10px; padding: 6px 10px; background: #f5f7f9; border-left: 3px solid #9aa4ae;
             color: #3d444c; font-size: 8.6pt; }
blockquote p { margin: 2px 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.3pt; background: #f1f3f5; padding: 0 3px;
       border-radius: 2px; }
pre { background: #f1f3f5; padding: 6px 8px; white-space: pre-wrap; }
a { color: #0b63c5; text-decoration: none; word-break: break-all; }
.badge { display: inline-block; font-size: 7pt; font-weight: 700; text-transform: uppercase; letter-spacing: .04em;
         padding: 0 4px; border-radius: 3px; vertical-align: 1px; }
.badge.hyp { background: #efe6ff; color: #5b2bb5; }
.badge.stale { background: #fff1d6; color: #8a5a00; }
.heat { font-weight: 700; color: #b4361e; }
.doc { break-before: page; }
.doc:first-of-type { break-before: auto; }
.checkbox { font-family: "DejaVu Sans", sans-serif; }
"""


def find_chrome():
    env = os.environ.get("HIXBRAIN_CHROME")
    if env:
        return env
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    mac = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(mac):
        return mac
    hits = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    if hits:
        return hits[-1]
    sys.exit("No Chrome/Chromium found. Set HIXBRAIN_CHROME to the browser binary.")


def normalize_lists(text):
    """Make GitHub-style lists parse under Python-Markdown: 2-space nested
    bullets -> 4 spaces, and a blank line before a list that directly follows
    a paragraph line."""
    out, prev = [], ""
    for line in text.splitlines():
        m = re.match(r"^( {2,3})([-*+]|\d+\.) ", line)
        if m:
            line = "    " + line[len(m.group(1)):]
        is_item = re.match(r"^([-*+]|\d+\.) ", line)
        prev_is_item = re.match(r"^\s*([-*+]|\d+\.) ", prev)
        if is_item and prev.strip() and not prev_is_item and not prev.startswith(("|", ">", "#")):
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out)


def md_to_html(text):
    text = normalize_lists(text)
    for emoji, repl in BADGES:
        text = text.replace(emoji, repl)
    text = text.replace("☐", '<span class="checkbox">☐</span>')
    # Bare URLs -> links (the markdown lib only links <...> and [..](..)).
    text = re.sub(r"(?<![(<\"'])(https?://[^\s)<>|]+)", r"<\1>", text)
    return markdown.markdown(text, extensions=["tables", "sane_lists"])


def build_html(paths, title, internal):
    docs = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            docs.append(f'<section class="doc">{md_to_html(f.read())}</section>')
    banner = ""
    if internal:
        banner = ('<div class="banner"><span><b>INTERNAL — DEEPGRAM ONLY</b> · Do not forward to the customer</span>'
                  f"<span>{html.escape(title)}</span></div>")
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f"<style>{CSS}</style></head><body>{banner}{''.join(docs)}</body></html>")


# Google Docs' HTML import ignores most <style> rules, so this variant uses
# inline styles and text-only markers (emoji outside the BMP get mangled).
GDOC_BADGES = [
    ('<span class="badge hyp">Hypothesis</span>', '<b style="color:#5b2bb5">[Hypothesis]</b>'),
    ('<span class="badge stale">Stale</span>', '<b style="color:#8a5a00">[Stale]</b>'),
    ('<span class="heat">', '<span style="color:#b4361e;font-weight:bold">'),
    ('<span class="checkbox">☐</span>', "☐"),
]


def build_gdoc_html(paths, internal=False):
    parts = []
    if internal:
        parts.append('<p style="background:#13151a;color:#13ef93;font-weight:bold;padding:6px">'
                     "INTERNAL — DEEPGRAM ONLY · Do not forward to the customer</p>")
    for i, p in enumerate(paths):
        with open(p, encoding="utf-8") as f:
            body = md_to_html(f.read())
        for a, b in GDOC_BADGES:
            body = body.replace(a, b)
        # Key-value tables ("| | |") have an empty header row; Docs would show it.
        body = re.sub(r"<thead>\s*<tr>\s*(<th></th>\s*)+</tr>\s*</thead>\s*", "", body)
        body = body.replace("<table>", '<table border="1" cellpadding="4" style="border-collapse:collapse">')
        if i:
            body = '<hr style="page-break-before:always">' + body
        parts.append(body)
    return '<html><head><meta charset="utf-8"></head><body>' + "".join(parts) + "</body></html>"


def render(paths, out, title, internal=False):
    doc = build_html(paths, title, internal)
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "brief.html")
        with open(src, "w", encoding="utf-8") as f:
            f.write(doc)
        cmd = [find_chrome(), "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
               f"--print-to-pdf={os.path.abspath(out)}", f"file://{src}"]
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("inputs", nargs="+")
    p.add_argument("--out", required=True)
    p.add_argument("--title", default="Account Brief")
    p.add_argument("--internal", action="store_true", help="add an INTERNAL / do-not-forward banner")
    p.add_argument("--gdoc-html", action="store_true",
                   help="write Google-Docs-friendly HTML (for Drive upload) instead of a PDF")
    a = p.parse_args(argv)
    if a.gdoc_html:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(build_gdoc_html(a.inputs, a.internal))
    else:
        render(a.inputs, a.out, a.title, a.internal)
    print(a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
