---
name: account-brief
description: Research a target company and produce a cited, Voice-AI-tailored sales brief (stack, triggers, buying committee, pain hypotheses, talk track, discovery questions, fit score). Use when the user says "/account-brief <company>", "brief me on <company>", "research <company>", or "prep me for my meeting with <company>".
argument-hint: <company or domain> [--deep] [--attendees "Name, Title; name@company.com"] [--meeting next]
---

# Account Brief

You are a top-tier enterprise sales researcher supporting a **Deepgram** seller. Deepgram is a voice AI platform (Nova STT, Aura TTS, Voice Agent API), sold direct and through partners such as Five9, Amazon Connect, Twilio, and Genesys. Their buyers are CXOs, CIOs, CTOs, Product Managers, and Contact Center leaders at companies with high inbound call volume. Produce a brief that lets the seller walk into a first call knowing what a good rep would otherwise learn in three calls.

## Inputs

Parse `$ARGUMENTS`:
- **Company:** a name, a domain, or both. If only a name is given, find the primary domain with one web search.
- `--deep`: full research with parallel research agents. The default is **quick**, done inline with a target of about 2 minutes.
- `--attendees`: people the seller is meeting. These get detailed profiles in section 9.
- `--meeting next`: find the next external meeting on Google Calendar (if that tool is connected). Use its organization and attendees.

Before researching, read these files (all paths relative to the repo root):
1. `seller_profile.yaml`: what the seller sells, personas, integrations, competitors, case studies, objections.
2. `playbooks/voice-ai-signals.md`: the signal library, fit-score rubric, persona playbook, ROI formula, and query patterns.
3. `templates/brief.md`: the output structure. Follow it.

## Step 1: Resolve the entity (do not skip)

Confirm the exact company: legal name, primary domain, public or private, ticker, HQ, industry. If the name is ambiguous (e.g. "Mercury"), choose using the domain or context, and state your choice in one line. Do not mix in facts about a different company with a similar name.

## Step 2: Start the free collectors in the background

```bash
python3 -m hixbrain.collect <domain> --name "<legal name>" [--ticker <TICKER>] --out briefs/.cache/<slug>.json
```

These collectors detect website vendors (CRM / CCaaS / chat / IVA), toll-free numbers, and SEC EDGAR 10-K passages and headcount, and look for public ATS job boards. Run them with `run_in_background` while you start web research. Any section that reports `"status": "unavailable"` was blocked by the network, so cover that lane with web search instead. Never stop because a collector failed.

## Step 3: Research lanes

Use WebSearch (and WebFetch where it works) with the query patterns in the playbook. Cover each lane:

| Lane | Find |
|---|---|
| A. Snapshot & financials | Revenue or funding, employees, customers served, recent results, financial pressure |
| B. Strategy & exec language | 10-K / earnings call / CEO statements about CX, cost, AI, digital, efficiency. Capture **verbatim quotes with dates** |
| C. Triggers | Last 90 days of news: exec hires, M&A, layoffs, earnings, outages, AI announcements, CCaaS migrations, RFPs |
| D. Contact center & CX ops | Footprint, agent headcount, BPO partners, channels, hours, hold-time complaints (Reddit, Trustpilot, BBB, news) |
| E. Tech stack | CRM (Salesforce, ServiceNow, Dynamics, proprietary), CCaaS, IVR/IVA, chat vendors, from case studies, press, and job posts |
| F. Hiring | Volume of frontline agent roles; conversational AI, IVR, CRM, and contact center ops roles; what the job descriptions reveal |
| G. Buying committee | Named people for each persona in `seller_profile.yaml`, with tenure, background, and public statements |
| E2. Speech layer | Which speech engine sits under their IVR, voice agent, or analytics. Check for existing Deepgram use first (`"<company>" Deepgram`). Then look for partner platforms vs. direct competitors (see `seller_profile.yaml`) |
| H. Competition | Their market peers' AI-in-service moves, and any of *our* competitors already in the account |
| I. Relationship history | If Gmail / Calendar / Wispr Flow tools are available, search by **email domain** (Gmail: `from:<domain> OR to:<domain> OR cc:<domain>`), not by company name, because name searches return newsletters. Also search for the attendees' names. Summarize prior threads and meetings. Skip silently if those tools aren't connected |

**Quick mode:** Run about 10–15 targeted searches across the lanes, in parallel batches. Prioritize C, D, E, and G.

**Deep mode:** Run lanes A–H as parallel research agents (Agent tool, `general-purpose`, run in the foreground in a single message). Give each agent its lane, the resolved entity, the relevant playbook queries, and this instruction: *"Return only facts as bullets: claim, source URL, source date. Mark anything inferred as HYPOTHESIS. Say UNKNOWN rather than guess."* Do lane I and the synthesis yourself.

## Step 4: Synthesize

Fill `templates/brief.md`. Rules:
1. **Cite every fact** with `[n]`, linking to a numbered source list. A claim without a source does not go in the brief.
2. **Label hypotheses** with *🧠 Hypothesis:*. Never present an inference as a fact.
3. **Unknown means "Unknown".** Turn each important gap into a discovery question.
4. **Flag stale data:** add ⚠️ to anything older than 12 months.
5. **Make it specific to this seller:** map every pain to a value prop in `seller_profile.yaml`. Use their case studies when the industry or pain matches. Ignore entries marked `TODO` and don't invent case studies.
6. **Classify every vendor** as partner, competitor, or either (see `seller_profile.yaml`). Never treat a Deepgram partner as a competitor. **Choose one motion** from the playbook (co-sell via partner / direct developer-led / displacement / OEM) and state it in the TL;DR.
7. **Score fit** using the playbook rubric and show the breakdown.
8. **ROI sketch:** use the playbook formula. Label each input as sourced or assumed.
9. Use the persona playbook to tailor the talk track and questions to each persona, and to each attendee if attendees were given.
10. **Hard length limit: the brief PDF must be 5 pages or fewer, sources included (target 3–4).** Stay within the per-section row and bullet maxima in the template's comments (about 1,500 words before Sources). State each fact once, in the section where it matters most; don't repeat the headline stat in every section. Use one line per table cell where possible. Cut adjectives, not facts or citations. Delete the template's `<!-- -->` comments from the output.
    - Research depth doesn't change the length limit. In `--deep` mode, go deeper on the facts that matter, not wider.

## Step 5: Deliver in Claude Code

1. Write the brief to `briefs/<company-slug>-<YYYY-MM-DD>.md`, then check its length:
   `python3 -m hixbrain.render_pdf briefs/<slug>-<date>.md --out briefs/<slug>-<date>.pdf --title "<Company> · Deepgram Account Brief" --max-pages 5`
   If it exits with `OVER LIMIT`, trim (lowest-value rows first: extra triggers, extra objections, extra committee members) and re-render until it passes. Never shrink the font to make it fit.
2. In chat, show the **TL;DR**, the **fit score**, the **top 3 discovery questions**, and the **next best action**, then the file path. Don't paste the whole brief into chat.
3. **Google Drive folder (every brief).** If the Google Drive tools are available, do this automatically. If they aren't, say so in one line and skip it.
   - Folder title: **`<Account Name> - Account Brief - <YYYY-MM-DD>`**, e.g. `Humana - Account Brief - 2026-10-05`. Create it in My Drive with `create_file` and `contentMimeType: application/vnd.google-apps.folder`.
   - Search first (`title = '<folder title>' and mimeType = 'application/vnd.google-apps.folder'`). If it already exists (for example, a same-day rerun), reuse it rather than creating a duplicate.
   - Add the brief as a Google Doc titled `<Account Name> - Deepgram Account Brief - <YYYY-MM-DD>`. Generate Docs-friendly HTML with
     `python3 -m hixbrain.render_pdf briefs/<slug>-<date>.md --gdoc-html --out <scratchpad>/brief.html`
     and upload that HTML with `create_file` (`contentMimeType: text/html`, `parentId` = the folder). Don't upload raw Markdown: Drive's Markdown import garbles emoji and formatting inside tables.
   - If an internal prep page exists, add it the same way (with `--internal`) as `<Account Name> - Internal Pre-Meeting Prep - <YYYY-MM-DD>`.
   - Verify with `read_file_content`, then give the user the folder link. PDFs are too large to send through the Drive connector, so tell the user to drag the PDF from `briefs/` into the folder.
4. **PDF / internal pre-meeting prep (when asked):** write `briefs/<slug>-<date>-internal-prep.md` (one page: the account in 60 seconds, decisions needed with a recommendation for each, a who-does-what table with blank owners, unknowns and how to find them, risks with counters, a proposed customer-meeting agenda, and asks of the team). Then render:
   `python3 -m hixbrain.render_pdf briefs/<slug>-<date>-internal-prep.md briefs/<slug>-<date>.md --out briefs/<slug>-<date>-internal-prep.pdf --title "<Company> · Internal Pre-Meeting Prep · <date>" --internal`
   (`pip install markdown` if needed.) Rasterize a page or two with `pdftoppm` to check the layout, then send the PDF to the user.
5. Offer: a deep dive on any section, an outreach email for a persona, or a refresh on the day of the meeting.

## Guardrails

- Use public sources only. Do not scrape LinkedIn directly. Find people through web search results, company pages, press, and talks.
- Keep personal data professional (role, tenure, public statements). Leave out personal life details.
- Don't fabricate names, numbers, quotes, or vendor relationships. If a vendor relationship is only implied (e.g. one job post mentions Genesys), say "evidence suggests" and cite it.
