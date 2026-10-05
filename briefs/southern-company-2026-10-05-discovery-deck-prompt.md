# Discovery Deck Prompt — Southern Company (for Claude Design)

> **How to use:** copy everything below the line into Claude Design. If Claude Design has a Deepgram design system or brand kit, select it first. Fill in the `[brackets]` before or after generating. Facts come from southerncompany.com, SEC filings, deepgram.com, and the press sources listed in the speaker notes. Open each source before presenting.

---

Create an **8-slide, 16:9 discovery-meeting deck** from **Deepgram** to **Southern Company**. The presenter is **Kyle Hix, Deepgram**. This is a first discovery meeting with Southern Company Gas customer-experience leaders (care centers, digital experience) and Southern Company technology partners. The deck should feel like a **conversation starter, not a pitch**: short, confident, and full of questions. It should show we did our homework and leave room for Southern Company to correct us.

## Design direction
- Use the Deepgram brand: a dark, near-black background with a bright Deepgram-green accent and clean sans-serif type. If a Deepgram design system is available, use it instead of these notes.
- Use a clean, modern enterprise-tech style. Keep text to **6 bullets or fewer per slide and about 12 words or fewer per bullet**. Use one visual idea per slide (a stat row, a simple diagram, a timeline).
- Put a placeholder box labeled "Southern Company logo" on the title slide. **Don't recreate either company's logo.**
- Add **speaker notes to every slide** with talking points and the sources listed below.
- Use only the facts given here. **Do not invent metrics, customer names, logos, or quotes.** Where a fact is unknown, show it as a question or a `[placeholder]`.
- Tone: respectful of Southern Company's existing investments. Never criticize Five9, NICE, Microsoft, their current vendors, or their service levels.

## Slide-by-slide content

### Slide 1 — Title
- Title: **"Southern Company × Deepgram: Discovery Conversation"**
- Subtitle: "Bringing your AI investments to the voice channel"
- Footer: `[Meeting date]` · Kyle Hix, Deepgram · `[Southern Company attendees]`
- Visual: subtle sound-wave motif, with logo placeholders for Southern Company and Deepgram.

### Slide 2 — Agenda
Six numbered items with suggested times for a 45-minute meeting:
1. What we know about Southern Company (5 min)
2. Your challenges and goals: we want to hear from you (15 min)
3. A quick intro to Deepgram (5 min)
4. Where Deepgram could fit in your stack (8 min)
5. Project scoping and timeline (7 min)
6. Next steps (5 min)

Below the list, add a small line: "Our goal today: understand your priorities and agree whether a next step makes sense."

### Slide 3 — What we know about Southern Company
Visual: a row of 4 stat tiles, then 3 short bullets.
- Stat tiles:
  - **Since 1945**: powering the Southeast `[verify wording on southerncompany.com/about-us/history]`
  - **~9M customers** across electric and gas utilities
  - **4.4M+ gas customers** served by Southern Company Gas utilities
  - **~28,000 employees**
- Bullets:
  - Strongest retail-sales growth in about two decades (Q2 2026), led by economic development across the Southeast
  - Already investing in AI for customers: a customer lakehouse with gen-AI, RAG, and AI agents (DISTRIBUTECH 2025)
  - Leadership priority: a new Chief Information Technology Officer role focused on "data and analytics, AI, and innovation to meet customers' changing needs"
- Small closing line: "What did we miss or get wrong?"
- Speaker notes: Sources are Southern Company 10-K FY2025 (customers, employees); Q2 2026 earnings release (Jul 30, 2026); Southern Company press release naming Hans Brown EVP & CITO (Jul 21, 2025); DISTRIBUTECH 2025 session "Can generative AI transform customer engagement? Southern Company paves the way"; Kerry Hogan bio (4.4M gas customers). Present the lakehouse work as admiration for a visible AI win, not as a gap.

### Slide 4 — Current Challenges & Business Goals
Two columns titled **"What we think we heard"** (left) and **"Business goals"** (right), and a clear banner: **"Our hypotheses — please correct us."**
- Challenges, phrased as industry-level and non-judgmental:
  - Storms and heating season create sudden call spikes no staffing plan fully covers
  - Many calls are routine: outage status, billing, payment arrangements, start/stop service
  - Callers speak account numbers and addresses that are hard for speech systems to capture
  - Customers are watching bills closely, so every interaction carries more weight
  - Adopting AI responsibly with regulators, union workforces, and customer data protections
- Goals, tied to Southern Company's stated priorities:
  - Use technology, data, and AI "to meet customers' changing needs"
  - Faster answers and less waiting, especially on the worst-weather days
  - Free care-center teams for complex, high-value conversations
  - Extend the customer-data and gen-AI foundation to the phone
- Footer question: **"Which of these matter most for 2027, and what's missing?"**
- Speaker notes: This is the most important slide. Spend most of the meeting here. Ask: Which IVR and speech engine handle calls today, and is Five9 used beyond SouthStar? How many calls a year, and what share are routine? Is voice on the AI-agent roadmap, and who owns it: IT or customer experience?

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
- Speaker notes: Sources are deepgram.com (company milestones, data-security page, and the Series C press release). Keep this slide to 3 minutes.

### Slide 6 — Where we see Deepgram fitting into Southern Company's stack
Visual: a simple left-to-right architecture diagram.
**Customer calls in** → **Five9 contact center platform** `[verify which business units run Five9]` → **Deepgram Voice Agent** (resolves routine intents: outage status, bill and balance, payment arrangements, start/stop service) → if a person is needed, a **warm handoff with full context** → **Care-center representatives**.
Underneath the diagram, show a **"Customer lakehouse / customer & billing systems `[name TBD]`"** box connected to the voice agent ("look up accounts, outages, and balances"), and draw a **"Runs in Southern Company's cloud / VPC"** boundary around the Deepgram components.
- Three callouts:
  - **Complements your gen-AI program:** the same customer data and LLMs, now available by phone
  - **Works with your platforms:** Deepgram powers speech inside Five9 IVA Studio and integrates with Amazon Connect, Twilio, and Genesys
  - **Your data stays yours:** VPC or self-hosted deployment
- Footer question: "What sits in front of your representatives today, and which speech engine powers your IVR?"
- Speaker notes: The diagram is a starting point to redraw with them. Five9 appears in a SouthStar Energy role description; confirm its scope across the gas utilities and electric companies. Partner integrations are listed on deepgram.com/partners. Proof point: a major healthcare provider using Five9's IVA doubled caller authentication rates after switching to Deepgram, which was 2–4x more accurate on alphanumeric inputs (deepgram.com/customers/five9). Scale proof: Abby Connect handles 100,000+ calls a month with a Deepgram-powered AI receptionist (deepgram.com/learn/case-study/abby-connect).

### Slide 7 — Project Scoping & Timeline Discussion
Visual: a three-phase horizontal roadmap, plus a small "Questions to scope together" box.
- **Phase 0: Proof (2–3 weeks).** Accuracy bake-off on ~500 real recorded calls (account numbers, addresses, regional accents), measuring accuracy, latency, and cost per hour, run in Southern Company's environment.
- **Phase 1: Pilot (8–10 weeks).** One voice agent on 2–3 high-volume routine intents for one utility, with warm handoff to representatives and success metrics agreed up front.
- **Phase 2: Scale.** Expand intents and utilities, and be storm-ready before the next hurricane season.
- Questions to scope together:
  - Which utility and intents first?
  - What success metrics matter: containment, authentication rate, service level, cost per call?
  - Security, regulatory, and labor-relations review path?
  - Who are the owners on each side?
- Speaker notes: Phase durations are proposals to discuss, not commitments. Time the pilot around winter heating season and hurricane season so it doesn't compete with peak operations — a spring 2027 pilot can be in production before the June hurricane season.

### Slide 8 — Next Steps, Proposed Timeline & Action Items
Visual: a dated timeline across the top, with an action-item table below it (columns: Action · Owner · Target date).
- Timeline (proposed):
  - **Week 1** (`[date]`): share sample call audio and intent list; mutual NDA
  - **Weeks 2–4** (`[dates]`): accuracy bake-off
  - **Week 5** (`[date]`): results readout with customer-experience and technology teams
  - **`[Spring 2027]`**: pilot kickoff, after the winter peak and before hurricane season
- Action items:
  - Send recap and bake-off plan · Deepgram (Kyle Hix) · within 2 business days
  - Identify sample calls and top intents · Southern Company `[owner]` · `[date]`
  - Security / data review kickoff · Southern Company `[owner]` + Deepgram · `[date]`
  - Loop in the Five9 account team · Deepgram · `[date]`
  - Book the results-readout meeting · Deepgram · `[date]`
- Closing line: **"Does this plan work for you?"** with Kyle Hix's contact details: `[email]` · `[phone]`
- Speaker notes: Confirm owners and dates live in the meeting, and replace the placeholders before sending the deck afterward.
