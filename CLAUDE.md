# HixBrain

Account intelligence for selling a Conversational AI / Voice AI platform. It produces cited sales briefs inside Claude Code.

- **Generate a brief:** `/account-brief <company or domain> [--deep] [--attendees "..."] [--meeting next]`. The workflow lives in `.claude/skills/account-brief/SKILL.md`.
- **Seller context:** `seller_profile.yaml` (product, personas, integrations, competitors, case studies, objections). Keep it current; briefs are only as specific as this file.
- **Signals, rubric, and persona playbook:** `playbooks/voice-ai-signals.md`
- **Output template:** `templates/brief.md` → briefs are written to `briefs/`
- **Free collectors (Python 3.9+, stdlib only, no API keys):** `python3 -m hixbrain.collect <domain> --name "..." [--ticker X]`. Set `HIXBRAIN_SEC_USER_AGENT="Name email"` for SEC EDGAR.
- **Tests:** `python3 -m unittest`
- **Design:** `DESIGN.md`
