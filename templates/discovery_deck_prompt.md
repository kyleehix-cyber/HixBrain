# Discovery Deck Prompt — {Company} (for Claude Design)

<!--
HOW TO FILL THIS (Claude): build from the account brief + seller_profile.yaml + the
customer's own website. The deck is CUSTOMER-FACING:
  - NO internal content: no fit score, "displacement", "motion", competitor framing,
    review-site complaints, or 🧠 labels. Say "our hypotheses — please correct us" instead.
  - Never criticize the customer's vendors, service levels, or people.
  - Prefer facts from the customer's own site and Deepgram's site; put every source in
    the speaker notes. Mark anything you couldn't verify with [verify ...].
  - Unknowns become [placeholders] or questions on the slide, never guesses.
  - If a Deepgram partner (Five9, Amazon Connect, Twilio, Genesys, ...) is in the account,
    show it by name in the slide 6 diagram. Otherwise show "[platform — TBD]".
  - Pick 1–2 case studies from seller_profile.yaml that match the industry or pain.
Save as briefs/<slug>-<date>-discovery-deck-prompt.md. Remove this comment.
-->

> **How to use:** copy everything below the line into Claude Design. If Claude Design has a Deepgram design system or brand kit, select it first. Fill in the `[brackets]`. Open each source before presenting.

---

Create an **8-slide, 16:9 discovery-meeting deck** from **Deepgram** to **{Company}**. The presenter is **{Seller}, Deepgram**. This is a first discovery meeting with {audience}. It should feel like a **conversation starter, not a pitch**: short, confident, and full of questions.

## Design direction
- Use the Deepgram brand: a dark, near-black background with a bright Deepgram-green accent and clean sans-serif type. If a Deepgram design system is available, use it instead.
- Keep text to **6 bullets or fewer per slide and about 12 words or fewer per bullet**. Use one visual idea per slide.
- Put a placeholder box labeled "{Company} logo" on the title slide. Don't recreate either company's logo.
- Add **speaker notes to every slide** with talking points and sources.
- Use only the facts given here. **Do not invent metrics, customer names, logos, or quotes.**
- Tone: respectful of {Company}'s existing investments. Never criticize their vendors or service.

## Slide-by-slide content

### Slide 1 — Title
"{Company} × Deepgram: Discovery Conversation" · subtitle tied to their top goal · `[Meeting date]` · presenter · `[attendees]`

### Slide 2 — Agenda
Six items with times for a 45-minute meeting: what we know (5) · challenges and goals (15) · intro to Deepgram (5) · fit in your stack (8) · scoping and timeline (7) · next steps (5). Goal line: "understand your priorities and agree whether a next step makes sense."

### Slide 3 — What we know about {Company}
4 stat tiles (from their website and filings: history, scale, customers/members, contact-center scale), plus 3 bullets (mission in their words, a current initiative to compliment, a leadership priority quote). Close with "What did we miss or get wrong?"

### Slide 4 — Current Challenges & Business Goals
Two columns: "What we think we heard" (3–5 industry-level challenges) and "Business goals" (3–4, tied to their stated priorities). Banner: "Our hypotheses — please correct us." Footer question. Speaker notes: the top 3 discovery questions.

### Slide 5 — Intro to Deepgram
Positioning line · 4 stat tiles from deepgram.com · 3 product cards (Nova, Aura, Voice Agent API) · trust strip (SOC 2 Type II, HIPAA BAA, PCI DSS, GDPR, cloud/VPC/self-hosted). Re-check stats on deepgram.com each time; they change.

### Slide 6 — Where Deepgram fits into {Company}'s stack
Left-to-right diagram: calls in → their telephony/CCaaS (named, or TBD) → Deepgram (voice agent / speech layer for the relevant use case) → warm handoff → their agents and tools. Show their CRM and their deployment boundary (VPC). Three callouts: complements existing investments · works with their platforms · data stays theirs. Matching case study in the notes.

### Slide 7 — Project Scoping & Timeline Discussion
Three phases: Proof (bake-off on their audio, 2–3 wks) → Pilot (2–3 intents, 8–10 wks) → Scale. Plus a "Questions to scope together" box (first intents, success metrics, security path, owners). Avoid the customer's peak season.

### Slide 8 — Next Steps, Proposed Timeline & Action Items
Dated timeline (Week 1 audio + NDA/BAA → bake-off → readout → pilot kickoff) and an action table (Action · Owner · Target date) with owners on both sides. Close: "Does this plan work for you?" plus contact details.
