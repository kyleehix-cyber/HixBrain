# HixBrain — Account Intelligence for Sellers

**Goal:** Type in a company and get back, in about 90 seconds, a cited brief that tells you who they are, what they care about right now, who decides, and how to position what you sell. You should walk into a first call already knowing what a good rep would otherwise learn in three calls.

---

## 1. What the brief answers

Each section answers one question a salesperson needs answered before a call. Each claim is cited and dated.

| # | Section | The question it answers | Primary sources |
|---|---------|-------------------------|-----------------|
| 1 | **Snapshot** | Who are they? | Website, enrichment API, Crunchbase/PitchBook |
| 2 | **Strategy & priorities** | What is leadership trying to accomplish this year? | 10-K/10-Q, earnings call transcripts, shareholder letters, CEO interviews and posts |
| 3 | **Financial health & budget signals** | Do they have money, and where is it going? | SEC EDGAR, funding rounds, layoffs, M&A |
| 4 | **Trigger events (last 90 days)** | Why would they buy *now*? | News, press releases, exec changes, funding, earnings |
| 5 | **Hiring signals** | Which teams are growing, and what pain do the job posts admit to? | Greenhouse / Lever / Ashby / Workday career boards |
| 6 | **Tech stack & current vendors** | What are they using today, and what would I displace or integrate with? | BuiltWith/Wappalyzer, job posts, case studies, G2 |
| 7 | **Org & buying committee** | Who is the economic buyer, champion, blocker, and end user? | Enrichment API (Apollo / PDL / ZoomInfo), company site, press |
| 8 | **People profiles** | For each person I'm meeting: background, tenure, what they've said publicly, and how to open the conversation | Enrichment API, podcasts/talks, posts, prior emails/meetings |
| 9 | **Competitive landscape** | Who are their competitors, and who are *my* competitors in the account? | Web search, G2, earnings calls |
| 10 | **Pain hypotheses → my solution** | Where does what I sell map to what they care about? | Synthesis of 2–9 + your product profile |
| 11 | **Talk track** | Opening line, 3 value angles, relevant customer proof points | Synthesis + your case-study library |
| 12 | **Discovery questions** | What I still need to learn, ranked by deal impact | Gaps found in 1–10 |
| 13 | **Likely objections** | What they'll push back on, and how to respond | Synthesis + your objection playbook |
| 14 | **Relationship history** | Have we talked before? What was said? | Gmail, Calendar, Wispr Flow meeting notes, CRM |
| 15 | **Next best actions** | Who to contact, which channel, and with what message | Synthesis |

The **one-page TL;DR** at the top is the part you read in the elevator: 5 bullets, the #1 pain hypothesis, the person to win, and the one question to ask.

---

## 2. How it stays fast: parallel research agents

```
                         ┌──────────────────────────┐
  "acme.com"  ─────────▶ │  Resolver                │  domain → legal name, ticker,
  (+ meeting attendees)  │  (entity resolution)     │  CIK, HQ, LinkedIn URL, aliases
                         └────────────┬─────────────┘
                                      │ fan out (all in parallel)
       ┌──────────┬──────────┬────────┼─────────┬───────────┬──────────────┐
       ▼          ▼          ▼        ▼         ▼           ▼              ▼
   Financials   News &    Hiring   Tech     People &    Competitors   Relationship
   (EDGAR,      triggers  (career  stack    org chart   & market      history
   earnings)    (news,    boards)  (Built-  (enrich-    (web, G2)     (Gmail, Cal,
                 PR)                With)   ment API)                  Wispr, CRM)
       └──────────┴──────────┴────────┬─────────┴───────────┴──────────────┘
                                      ▼
                         ┌──────────────────────────┐
                         │  Evidence store          │  every fact = {claim, source URL,
                         │  (normalized, cached)    │  date, confidence}
                         └────────────┬─────────────┘
                                      ▼
                         ┌──────────────────────────┐
                         │  Sales strategist        │  + YOUR product profile,
                         │  (synthesis model)       │    ICP, case studies, objections
                         └────────────┬─────────────┘
                                      ▼
                     Brief (HTML / Markdown / PDF) + JSON → CRM
```

**Speed levers**
- **Parallel collectors.** The run takes as long as the slowest collector, not the sum of all of them. Target: under 90 seconds end to end.
- **Small models for extraction, a large model for strategy.** `claude-haiku-4-5` reads filings, job posts, and articles and pulls out structured facts. `claude-opus-5-5` does only the final sales synthesis.
- **Cache by company with TTLs.** Firmographics: 30 days. Filings: until the next filing. News and jobs: 24 hours. A second rep researching the same account pays almost nothing.
- **Two depths.** `quick` (about 30 seconds: snapshot, triggers, people, talk track) and `deep` (everything, including earnings-call analysis).

---

## 3. Making it trustworthy (the part most tools get wrong)

1. **Cite every claim.** If a fact has no source it doesn't go in the brief. Each bullet links to its source and shows its date.
2. **Say "Unknown" instead of guessing.** Gaps become discovery questions. They are never filled with plausible-sounding filler.
3. **Label facts and hypotheses differently.** "They hired 14 data engineers in Q3" is a fact. "They are likely struggling with pipeline reliability" is a hypothesis. They look different in the brief.
4. **Flag stale data.** Anything older than 12 months is flagged.
5. **Check entity resolution.** "Mercury" the bank is not "Mercury" the insurer. The resolver confirms domain, ticker, and HQ before fanning out.

---

## 4. The secret weapon: your own context

Generic company research is a commodity. What makes this tool *yours* is a **seller profile** you fill out once:

```yaml
# seller_profile.yaml
product: "..."                # what you sell, in one line
value_props: [...]            # the 3–5 outcomes you deliver
icp:                          # who buys
  industries: [...]
  company_size: "..."
  buyer_titles: [...]         # economic buyer, champion, users
pains_we_solve: [...]         # mapped to observable signals (e.g. "hiring SDRs" → pipeline pain)
competitors: [...]            # so it can spot them in the account
case_studies: [...]           # customer, industry, outcome, metric
objections: {...}             # objection → best response
```

With this profile, every brief answers "why should *this* account buy *my* thing" instead of just "here is a company."

You already have **Gmail, Google Calendar, Google Drive, and Wispr Flow** connected. That allows two features that generic tools can't offer:
- **Auto-brief before every external meeting.** Scan the calendar for meetings with outside domains and deliver a brief 30 minutes before each one, with profiles of the actual attendees.
- **Relationship memory.** "You last emailed Jane on Aug 12; she said budget opens in Q4. In the June call, their VP mentioned Snowflake costs."

---

## 5. Interfaces (build in this order)

1. **CLI:** `hixbrain brief acme.com --depth quick --attendees jane@acme.com`, which outputs Markdown and HTML. This is the fastest way to start getting value.
2. **Meeting-triggered briefs:** a scheduled job reads the calendar, generates briefs, and emails or pushes them to you.
3. **Account watchlist:** daily monitoring of target accounts that alerts you only on real trigger events (funding, exec hire, layoffs, earnings guidance changes, relevant job posts).
4. **Web app / CRM push:** a shareable brief page, and section JSON written to Salesforce/HubSpot account notes.

---

## 6. Tech choices (proposed)

| Concern | Choice | Why |
|---|---|---|
| Language | Python 3.12 | Best ecosystem for scraping and parsing (EDGAR, HTML, PDFs) |
| LLM | Claude API: Opus 5.5 for synthesis, Haiku 4.5 for extraction | Quality where it matters, speed and cost everywhere else |
| Web research | Claude's server-side web search and fetch tools | No separate search vendor needed at first |
| Free data | SEC EDGAR API, public ATS job-board JSON, company sites, GDELT news | $0 to get to MVP |
| Paid data (optional) | Apollo or People Data Labs (people/org), BuiltWith (tech), Crunchbase (funding) | Add only once the free version proves value |
| Storage / cache | SQLite to start, Postgres later | Simple |
| Concurrency | `asyncio` collectors | Parallel fan-out |
| Output | Jinja2 → Markdown/HTML, WeasyPrint → PDF | Readable on phone and desktop |

**Cost estimate:** about $0.10–$0.50 per deep brief in LLM spend at current pricing, plus any paid data APIs.

**Compliance:** use official APIs or licensed enrichment vendors for people data. Do not scrape LinkedIn directly, because that violates its ToS. Store personal data minimally, and support deletion (GDPR/CCPA).

---

## 7. Proposed repo layout

```
hixbrain/
  cli.py                 # entry point
  resolver.py            # domain → canonical entity
  collectors/
    edgar.py  news.py  jobs.py  techstack.py
    people.py  competitors.py  relationship.py
  evidence.py            # Fact model + cache
  synthesize.py          # strategist prompt + seller profile
  render/                # templates for md/html/pdf
  watch.py               # watchlist + trigger alerts (phase 3)
seller_profile.yaml
tests/
```

---

## 8. Roadmap

| Phase | Scope | Outcome |
|---|---|---|
| **MVP (week 1)** | CLI, resolver, web search + EDGAR + jobs collectors, synthesis, Markdown brief | Usable briefs for any public company or startup |
| **2** | Seller profile, attendee profiles, Gmail/Calendar/Wispr relationship history | Briefs specific to *your* deal |
| **3** | Auto-brief before meetings, account watchlist with trigger alerts | The tool comes to you |
| **4** | Paid enrichment, CRM push, web UI, team sharing | Ready for a team |

---

## 9. Open questions for Kyle

1. **What do you sell, and to whom?** (product, typical buyer title, deal size, industry). This shapes the synthesis prompts and which signals matter most.
2. **Mostly public companies, private companies, or both?** Public companies get rich EDGAR and earnings-call data. Private companies lean on hiring, news, and enrichment.
3. **Which CRM, if any?** (Salesforce, HubSpot, none)
4. **Budget for data vendors?** The MVP is free apart from LLM costs. Accurate people and org-chart data is where paid APIs help most.
5. **Where do you want briefs to show up?** Terminal, email, phone, or a web page.
