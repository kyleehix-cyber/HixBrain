# HixBrain

Account intelligence for selling **Deepgram** (Voice AI platform: Nova STT, Aura TTS, Voice Agent API). It produces cited sales briefs inside Claude Code.

- **Generate a brief:** `/account-brief <company or domain> [--deep] [--attendees "..."] [--meeting next]`. The workflow lives in `.claude/skills/account-brief/SKILL.md`.
- **Seller context:** `seller_profile.yaml` (product, personas, integrations, competitors, case studies, objections). Keep it current; briefs are only as specific as this file.
- **Signals, rubric, and persona playbook:** `playbooks/voice-ai-signals.md`
- **Output template:** `templates/brief.md` → briefs are written to `briefs/`. **Briefs are 5 pages max** (target 3–4), enforced with `render_pdf --max-pages 5`.
- **Free collectors (Python 3.9+, stdlib only, no API keys):** `python3 -m hixbrain.collect <domain> --name "..." [--ticker X]`. Set `HIXBRAIN_SEC_USER_AGENT="Name email"` for SEC EDGAR.
- **PDF (customer-safe or `--internal` prep):** `python3 -m hixbrain.render_pdf <md files...> --out x.pdf --title "..." [--internal]`. Needs `pip install markdown` and Chrome/Chromium (`HIXBRAIN_CHROME` to override).
- **Google Drive:** every brief gets a Drive folder `<Account> - Account Brief - <YYYY-MM-DD>` containing the brief (and any internal prep) as Google Docs, uploaded as HTML from `render_pdf --gdoc-html`.
- **Tests:** `python3 -m unittest`
- **Design:** `DESIGN.md`
