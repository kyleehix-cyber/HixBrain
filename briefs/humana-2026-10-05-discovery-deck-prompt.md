# Discovery Deck Prompt — Humana (for Claude Design)

> **How to use:** copy everything below the line into Claude Design. If Claude Design has a Deepgram design system or brand kit, select it first. Fill in the `[brackets]` before or after generating. Facts come from humana.com, deepgram.com, and the press sources listed in the speaker notes. Open each source before presenting.

---

Create an **8-slide, 16:9 discovery-meeting deck** from **Deepgram** to **Humana**. The presenter is **Kyle Hix, Deepgram**. This is a first discovery meeting with Humana's digital, technology, and member-services leaders. The deck should feel like a **conversation starter, not a pitch**: short, confident, and full of questions. It should show we did our homework and leave room for Humana to correct us.

## Design direction
- Use the Deepgram brand: a dark, near-black background with a bright Deepgram-green accent and clean sans-serif type. If a Deepgram design system is available, use it instead of these notes.
- Use a clean, modern enterprise-tech style. Keep text to **6 bullets or fewer per slide and about 12 words or fewer per bullet**. Use one visual idea per slide (a stat row, a simple diagram, a timeline).
- Put a placeholder box labeled "Humana logo" on the title slide. **Don't recreate either company's logo.**
- Add **speaker notes to every slide** with talking points and the sources listed below.
- Use only the facts given here. **Do not invent metrics, customer names, logos, or quotes.** Where a fact is unknown, show it as a question or a `[placeholder]`.
- Tone: respectful of Humana's existing investments. Never criticize Google, their current vendors, or their service levels.

## Slide-by-slide content

### Slide 1 — Title
- Title: **"Humana × Deepgram: Discovery Conversation"**
- Subtitle: "Exploring voice AI for member self-service"
- Footer: `[Meeting date]` · Kyle Hix, Deepgram · `[Humana attendees]`
- Visual: subtle sound-wave motif, with logo placeholders for Humana and Deepgram.

### Slide 2 — Agenda
Six numbered items with suggested times for a 45-minute meeting:
1. What we know about Humana (5 min)
2. Your challenges and goals: we want to hear from you (15 min)
3. A quick intro to Deepgram (5 min)
4. Where Deepgram could fit in your stack (8 min)
5. Project scoping and timeline (7 min)
6. Next steps (5 min)

Below the list, add a small line: "Our goal today: understand your priorities and agree whether a next step makes sense."

### Slide 3 — What we know about Humana
Visual: a row of 4 stat tiles, then 3 short bullets.
- Stat tiles:
  - **Since 1961**: helping people achieve their best health
  - **~8M members** across Humana programs `[verify the current figure on humana.com/about]`
  - **350 CenterWell Primary Care clinics** in 15 states
  - **20,000+ member advocates** handling up to **~80M member calls a year**
- Bullets:
  - Mission: personalized care "from people who care," built on listening to members
  - Already investing in AI for members: **Agent Assist**, built with Google Cloud, is rolling out to member service centers, with $100M+ in expected savings
  - Leadership priority: "simpler, leaner and faster" and "automation and AI with best-performing vendors" (Q2 2026 earnings call)
- Small closing line: "What did we miss or get wrong?"
- Speaker notes: Sources are humana.com/about; Humana Newsroom and Healthcare Dive (Agent Assist); TechInformed (20,000+ advocates, ~80M calls); Q2 2026 earnings call transcript (Motley Fool). Present the Agent Assist reference as admiration for a visible AI win, not as a gap.

### Slide 4 — Current Challenges & Business Goals
Two columns titled **"What we think we heard"** (left) and **"Business goals"** (right), and a clear banner: **"Our hypotheses — please correct us."**
- Challenges, phrased as industry-level and non-judgmental:
  - Medicare Annual Enrollment (Oct 15 – Dec 7) creates the biggest call spike of the year
  - Plan changes for 2027 drive high volumes of repetitive "what happens to my plan?" calls
  - Many routine calls (ID cards, claim status, pharmacy, provider lookup) still need an advocate
  - Members, often seniors, speak member IDs, drug names, and dates that are hard for speech systems to capture
  - Balancing AI adoption with HIPAA, CMS rules, and a trusted member experience
- Goals, tied to Humana's stated priorities:
  - Lower cost to serve while improving member experience ("simpler, leaner, faster")
  - Faster answers and less waiting for members
  - Free advocates for complex, high-value conversations
  - Scale proven AI wins (like Agent Assist) responsibly
- Footer question: **"Which of these matter most for 2027, and what's missing?"**
- Speaker notes: This is the most important slide. Spend most of the meeting here. Ask: What share of calls are routine? How did last enrollment season go? Who owns voice self-service: Digital, IT, or Operations?

### Slide 5 — Intro to Deepgram
Visual: one-line positioning, 4 stat tiles, then 3 product cards.
- Positioning: **"The voice AI platform enterprises build on: speech-to-text, text-to-speech, and real-time voice agents."**
- Stat tiles (from deepgram.com):
  - **200,000+ developers**
  - **1,400+ organizations**, including **400+ enterprises**
  - **50,000+ years of audio** processed
  - **$1.3B valuation** (Series C, Jan 2026)
- Product cards:
  - **Nova**: speech-to-text, built for accuracy on names, numbers, and noisy audio
  - **Aura**: natural, low-latency text-to-speech
  - **Voice Agent API**: speech-to-text, LLM, and text-to-speech in one real-time stack. Bring your own LLM.
- Trust strip: SOC 2 Type II · HIPAA (BAA available) · PCI DSS · GDPR · deploy in cloud, VPC, or self-hosted
- Speaker notes: Sources are deepgram.com (company milestones, enterprise, data-security pages, and the Series C press release). Keep this slide to 3 minutes.

### Slide 6 — Where we see Deepgram fitting into Humana's stack
Visual: a simple left-to-right architecture diagram.
**Member calls in** → **[Humana telephony / contact center platform — TBD]** → **Deepgram Voice Agent** (resolves routine intents: ID cards, claim status, pharmacy refills, plan questions) → if a human is needed, a **warm handoff with full context** → **Member advocates + Agent Assist**.
Underneath the diagram, show a **Salesforce** box connected to the voice agent ("look up and update member records") and a **"Runs in Humana's VPC"** boundary drawn around the Deepgram components.
- Three callouts:
  - **Complements Agent Assist:** we handle the calls that don't need an advocate, and advocates get full context on the ones that do
  - **Works with your platforms:** Deepgram integrates with Five9, Amazon Connect, Twilio, Genesys, and Salesforce
  - **Your data stays yours:** VPC or self-hosted deployment, HIPAA BAA
- Footer question: "What sits in front of your advocates today, and which speech engine powers your IVR?"
- Speaker notes: The diagram is a starting point to redraw with them. Deepgram partner integrations are listed on deepgram.com/partners. Healthcare proof point: a major healthcare provider using Five9's IVA doubled caller authentication rates after switching to Deepgram, which was 2–4x more accurate on alphanumeric inputs (deepgram.com/customers/five9).

### Slide 7 — Project Scoping & Timeline Discussion
Visual: a three-phase horizontal roadmap, plus a small "Questions to scope together" box.
- **Phase 0: Proof (2–3 weeks).** Accuracy bake-off on ~500 real member calls (IDs, drug names, senior voices), measuring accuracy, latency, and cost per hour, run in Humana's environment.
- **Phase 1: Pilot (8–10 weeks).** One voice agent on 2–3 high-volume routine intents, with warm handoff to advocates and success metrics agreed up front.
- **Phase 2: Scale (2027).** Expand intents and lines of business, plan capacity for the next enrollment period.
- Questions to scope together:
  - Which intents and lines of business first?
  - What success metrics matter: containment, authentication rate, CSAT, cost per call?
  - Security and compliance review path (BAA, VPC)?
  - Who are the owners on each side?
- Speaker notes: Phase durations are proposals to discuss, not commitments. Aim the pilot to start after the enrollment peak so it doesn't compete with October–December operations.

### Slide 8 — Next Steps, Proposed Timeline & Action Items
Visual: a dated timeline across the top, with an action-item table below it (columns: Action · Owner · Target date).
- Timeline (proposed):
  - **Week 1** (`[date]`): share sample call audio and intent list; mutual NDA / BAA
  - **Weeks 2–4** (`[dates]`): accuracy bake-off
  - **Week 5** (`[date]`): results readout with the technical and member-services teams
  - **January 2027**: pilot kickoff, after the enrollment peak
- Action items:
  - Send recap and bake-off plan · Deepgram (Kyle Hix) · within 2 business days
  - Identify sample calls and top intents · Humana `[owner]` · `[date]`
  - Security / BAA review kickoff · Humana `[owner]` + Deepgram · `[date]`
  - Book the results-readout meeting · Deepgram · `[date]`
- Closing line: **"Does this plan work for you?"** with Kyle Hix's contact details: `[email]` · `[phone]`
- Speaker notes: Confirm owners and dates live in the meeting, and replace the placeholders before sending the deck afterward.
