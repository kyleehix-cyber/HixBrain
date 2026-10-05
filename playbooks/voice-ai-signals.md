# Voice AI Sales Signals & Persona Playbook (Deepgram)

Reference for the `/account-brief` workflow. It covers what to look for, what each finding means for a Conversational / Voice AI deal, and how to talk to each buyer.

## 1. Signal library

| Signal | Where to find it | What it means | Weight |
|---|---|---|---|
| Large frontline agent workforce (hundreds of "customer service rep", "call center", "member services", "patient access", "reservations" jobs) | Job boards, Indeed/LinkedIn job search via web search, 10-K headcount | High inbound volume and labor cost, which is the core ROI case | 🔥🔥🔥 |
| Toll-free numbers on many pages, separate lines per line of business, "24/7" support | Contact/support pages | Volume and complexity; after-hours coverage gap | 🔥🔥 |
| Complaints about hold times, "can't reach a human", long waits | Reddit, Trustpilot, BBB, app-store reviews, news, X | Pain is public, so the CX exec feels it | 🔥🔥🔥 |
| 10-K / earnings call mentions "cost to serve", "self-service", "digital", "AI", "efficiency", "contact center" | EDGAR, earnings transcripts | Board-level priority; quote the CEO/CFO back to them | 🔥🔥🔥 |
| Recent CCaaS migration (to Genesys Cloud, NICE CXone, Amazon Connect, Five9) or an RFP for one | Press releases, vendor case studies, job posts ("Genesys Cloud engineer") | Timing window: AI usually comes next, and the platform is modern enough to integrate | 🔥🔥🔥 |
| Legacy on-prem Avaya / Cisco / Nuance IVR | Job posts, case studies | Modernization pressure; Nuance and Avaya transitions create an opening | 🔥🔥 |
| Hiring conversational AI / IVR / NLU / "AI agent" roles | Job boards | Active initiative (an evaluation or build is underway). Find out whether they are building or buying | 🔥🔥🔥 |
| Hiring Salesforce Service Cloud / ServiceNow CSM admins or architects | Job boards | CRM-centric service org; integration path is clear | 🔥 |
| Uses a BPO (Teleperformance, Concentrix, TTEC, Alorica, Foundever, TaskUs) | 10-K "service providers", news, Glassdoor | Large variable labor spend that AI can take out; contract renewals are timing events | 🔥🔥 |
| New CXO / CCO / CIO / CDO hired in the last 12 months | News, press releases, LinkedIn via web search | New leaders buy in their first 6–12 months | 🔥🔥🔥 |
| Seasonal spikes (open enrollment, storms, tax season, holiday travel, billing cycles) | Industry knowledge, news | Elastic capacity story with a specific deadline | 🔥🔥 |
| Cost-cutting, layoffs, or margin pressure | Earnings, news | Cost-takeout framing wins; avoid "headcount replacement" wording with the contact center manager | 🔥🔥 |
| M&A (systems and contact centers to consolidate) | 8-K, news | Integration chaos; unify the front door with AI | 🔥🔥 |
| Already announced an AI assistant / chatbot | News, website | Expansion or displacement. Find what it doesn't cover (usually voice, or complex intents) | 🔥 (qualify) |
| Regulated (HIPAA, PCI, TCPA, state insurance rules) | Industry | Lead with security and compliance; expect a longer cycle | info |
| **Deepgram partner platform in use** (Five9, Amazon Connect, Twilio, Genesys, Vonage, AudioCodes, Cognigy, Kore.ai, OneReach, Replicant) | Job posts, case studies, press, website scripts | **Partner route.** Upgrade the speech layer inside the platform they already own, and bring in the partner's account team for co-selling | 🔥🔥🔥 |
| Building voice features in-house (hiring voice / ASR / "voice agent" engineers, LLM platform team, Twilio developers) | Job boards, engineering blog, GitHub | **Ideal Voice Agent API buyer.** They need a real-time speech layer. "Build" is the opening, not a lost deal | 🔥🔥🔥 |
| Hyperscaler speech in use (Google STT/CCAI, AWS Transcribe/Lex, Azure Speech/Nuance) | Press, case studies, job posts | **Displacement.** Offer a bake-off on their own audio: accuracy, latency, cost per hour | 🔥🔥 |
| Accuracy pain: failed authentication, "didn't understand me", accents, noisy audio (drive-thru, field, mobile), alphanumeric IDs | Reviews, Reddit, IVR complaints | Deepgram's core differentiator. Use the Five9 healthcare authentication story | 🔥🔥🔥 |
| On-prem or VPC requirement (banks, government, healthcare) | Industry, security pages, RFPs | Deepgram deploys in VPC or on-prem, which many cloud-only competitors can't | 🔥🔥 |
| QSR / drive-thru / phone ordering | Industry | Proven Deepgram vertical with labor and ticket-size results | 🔥🔥🔥 |
| Software company with a voice product (CCaaS, conversation intelligence, voice-agent startup) | Website, product pages | **OEM / embed opportunity.** Deepgram becomes their speech engine. Different motion from an enterprise deal | 🔥🔥 |

## 2. Fit score rubric (0–100)

- **Inbound volume (0–30):** Agent headcount, call-heavy industry, number of support lines.
- **Pain evidence (0–25):** Public complaints, hold times, attrition, cost pressure in filings.
- **Timing / triggers (0–20):** New exec, CCaaS migration, an announced AI initiative, BPO renewal, M&A, earnings language.
- **Stack compatibility (0–15):** A Deepgram **partner** platform (Five9, Amazon Connect, Twilio, Genesys, etc.) or an in-house build team scores highest. Salesforce / ServiceNow add points. Proprietary CRM is fine (via API) but adds scope.
- **Access (0–10):** A known contact, a mutual connection, a prior conversation, a reachable persona, or a partner account team already in the account.

Classify every vendor found using `seller_profile.yaml`: **partners** (positive), **competitors** (displacement), **platforms_could_be_either** (find out which speech engine they use). Subtract 5–15 only for a *direct speech competitor* (Google, AWS Transcribe, Azure/Nuance, OpenAI, ElevenLabs, AssemblyAI, etc.) deployed in the last 18 months. Note it as a displacement or a bake-off play. A partner platform is never a deduction.

Bands: **80+** = pursue now, **60–79** = active prospect, **40–59** = nurture, **<40** = deprioritize.

## 3. Persona playbook

### Chief Experience Officer / Chief Customer Officer
- **Cares about:** NPS/CSAT, customer effort, brand, digital adoption, a consistent experience across channels.
- **KPIs:** NPS, CSAT, customer effort score, complaint volume, digital containment.
- **Open with:** Their public CX promise or a complaint trend: "Your customers are telling Reddit X; here's how [peer] fixed it."
- **Ask:** "Which customer journeys generate the most calls that shouldn't need a human?" / "How do you measure effort today?"
- **Objection to expect:** "Bots hurt CX." Answer with CSAT on AI-handled calls and an instant escape to a human.

### CIO
- **Cares about:** Vendor rationalization, security, integration risk, total cost of ownership, the AI strategy story for the board.
- **KPIs:** IT spend, uptime, delivery speed, risk.
- **Open with:** Earnings call or 10-K AI/efficiency language, and how this fits the existing Salesforce/ServiceNow and CCaaS investments without a rip-and-replace.
- **Ask:** "Where does conversational AI sit in your AI roadmap: platform vendor, build, or best of breed?" / "What's your standard for LLM governance?"
- **Objection to expect:** "Our CCaaS vendor already has AI." Answer with a containment-rate comparison and a land-alongside approach.

### CTO
- **Cares about:** Architecture, latency, scalability, data residency, LLM choice and guardrails, build vs. buy.
- **Open with:** Technical depth: real-time voice latency, barge-in, telephony (SIP/CCaaS) integration, CRM write-back, observability.
- **Ask:** "Have you prototyped voice agents in-house? What broke?" / "What are your requirements for PII/PHI redaction and model hosting?"
- **Objection to expect:** "We'll build it." Answer with the hard 80% (telephony, tuning, analytics, compliance) and time to production.

### Product Manager (digital / CX / conversational)
- **Cares about:** Shipping, iteration speed, containment by intent, analytics, a no-code/low-code designer, A/B testing.
- **KPIs:** Containment rate, intent coverage, task completion, release velocity.
- **Open with:** "What's on your self-service roadmap that's stuck behind engineering?"
- **Ask:** "Which top 10 call intents would you automate first?" / "How do you get call transcripts today?"
- **Role:** Usually the **champion**. Arm them with a business case they can take upstairs.

### Contact Center Manager / Director / VP of Operations
- **Cares about:** Service levels, hold times, abandonment, AHT, FCR, staffing, agent attrition, forecast accuracy, peak coverage.
- **KPIs:** ASA, abandonment rate, AHT, FCR, occupancy, cost per contact, attrition, QA scores.
- **Open with:** Peaks and staffing pain: "What happens to your service level on [seasonal spike]?"
- **Ask:** "What % of calls are repetitive (status, billing, password, scheduling)?" / "What's your fully loaded cost per agent hour?" / "What's agent attrition?"
- **Language:** Talk about "giving agents the hard, interesting calls" and "covering peaks". Do not talk about "replacing headcount".

### Engineering lead / ML or voice engineer (technical evaluator)
- **Cares about:** WER on *their* audio, latency (time to first word, barge-in), alphanumeric accuracy, SDKs, concurrency, deployment (VPC / on-prem), price per hour.
- **Open with:** "Want to run your hardest calls through Nova and see the transcripts side by side with what you use today?"
- **Ask:** "What speech engine sits under your IVA or voice agent today?" / "Where does it fail: names, IDs, accents, noise?" / "What's your latency budget?"
- **Role:** Runs the bake-off. Their benchmark decides the deal, so get them sample audio access early.

## 4. Motions (choose one per account)

| Situation | Motion |
|---|---|
| Uses a Deepgram partner (Five9, Amazon Connect, Twilio, Genesys, …) | **Co-sell through the partner.** Turn on or upgrade Deepgram inside their platform |
| Building their own voice agent | **Direct, developer-led.** Voice Agent API, bring your own LLM, bake-off |
| On a hyperscaler or another speech vendor | **Displacement.** Bake-off on accuracy, latency, and cost at their volume |
| End-to-end voice agent vendor (Sierra, PolyAI, Parloa, …) | Find out the vendor's speech engine. If it isn't Deepgram, consider pitching Deepgram to the vendor (OEM) as well as to the account |
| Software company with a voice product | **OEM / embed** |

## 5. ROI back-of-envelope (use in briefs when inputs exist)

```
annual_calls × automatable_share × containment_rate × (human_cost_per_call − ai_cost_per_call)
```

Defaults when unknown (always label them as assumptions):

| Input | Default |
|---|---|
| Human cost per call (US) | $4–$8 |
| Offshore BPO cost per call | $2–$4 |
| AI cost per call | $0.50–$1.50 |
| Automatable share | 30–50% |
| Containment rate | 50–70% |
| Calls per agent per year | ≈ 8,000–12,000 |

## 6. Research queries that work

- `"<company>" contact center OR "call center" OR "customer care" <current year>`
- `"<company>" Genesys OR "NICE CXone" OR Five9 OR "Amazon Connect" OR Talkdesk OR Avaya`
- `"<company>" Salesforce "Service Cloud" OR ServiceNow customer service`
- `"<company>" conversational AI OR "virtual agent" OR chatbot OR "voice assistant"`
- `"<company>" customer service hold time complaints` (and with `site:reddit.com`)
- `"<company>" "chief customer officer" OR "chief experience officer" OR "VP customer experience"`
- `"<company>" earnings call "customer service" OR "contact center" OR AI`
- `"<company>" Teleperformance OR Concentrix OR TTEC OR Alorica OR Foundever`
- `"<company>" customer service representative jobs` (headcount and locations)
- `"<company>" layoffs OR acquisition OR "new CEO" OR funding` (last 90 days)
- `"<company>" Deepgram` (existing usage, directly or through a partner; check this first)
- `"<company>" "speech recognition" OR "speech-to-text" OR "voice agent" engineer jobs`
- `"<company>" Google CCAI OR "Amazon Lex" OR Nuance OR "Azure Speech" OR ElevenLabs OR AssemblyAI`
