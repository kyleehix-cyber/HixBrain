# Southern Company — Deepgram Account Brief

Generated 2026-10-05 · Depth: quick · Fit score: **69/100 (active prospect)** · Legend: [n] = sourced fact · *🧠* = hypothesis, verify · **Unknown** = not found

> Facts come from web-search results, some from excerpts only (the company site, SEC, and job boards were blocked for direct fetch). Open the source before quoting a number to Southern Company.

## TL;DR
- **Who:** Atlanta utility holding company (NYSE: SO) serving ~9M electric and gas customers through Georgia Power, Alabama Power, Mississippi Power, and Southern Company Gas, with ~28,000 employees [1].
- **Why now:** A new EVP & Chief Information Technology Officer (Hans Brown, Jul 2025) has a mandate for "data and analytics, AI, and innovation" [3], and the customer team is already building gen-AI on a customer lakehouse [7].
- **Pain:** *🧠* Storm and billing peaks overwhelm the phone channel. Public posts describe 20–30+ minute holds and looping voice menus at Georgia Power [12].
- **Motion:** **Co-sell via Five9.** SouthStar Energy (Southern Company Gas) runs Five9 for IVR, ACD, and "AI-driven tools" [9]. Land the speech layer there, then carry the proof to the gas utilities and Georgia Power.
- **Win — key stakeholder:** **Kerry Hogan, VP Customer Experience, Southern Company Gas** [5]. She owns customer care, billing, collections, and digital experience design for 4.4M customers and leads the multi-year Digital Transformation Strategy. Exec sponsor for expansion: **Latanza Adjei** (Georgia Power CCO) [4]. Technical approver: **Hans Brown** [3].
- **Ask:** "Your gen-AI work is giving you a 360° view of the customer. What happens to the millions of calls that still go through a menu?"

## 1. Account Snapshot
| | |
|---|---|
| Company | Electric + gas utility holding co. · Atlanta, GA · NYSE: SO · founded 1945 [19] |
| Scale | 4.59M retail electric customers (GA Power 2.83M, AL Power 1.56M, MS Power 0.19M) + ~4.4M gas customers; ~28,000 employees [1][5] |
| Strategy | CITO role created to drive "technology, data and analytics, AI, and innovation to meet customers' changing needs" (Jul 2025) [3] |
| Financial signal | Q2 2026 adjusted EPS $1.13 vs. $0.92; retail sales +2.3% YTD, the strongest in ~20 years, driven by data centers [2] |
| Relationship | No business contact with southernco.com found in Gmail or Calendar |

## 2. Why Now
| When | Trigger | So what for Deepgram |
|---|---|---|
| Nov 5, 2026 | Q3 earnings call [18] | Listen for cost-to-serve and AI language to quote back |
| 2026 | Helene cost recovery ($800M storm costs) deferred into 2026 under a base-rate freeze through 2028 [14][15] | Bill questions plus flat base rates → pressure to lower cost to serve |
| Jul 2025 | Hans Brown (ex-BNY) named EVP & CITO [3] | New technical decision-maker, now ~15 months in and setting the AI roadmap |
| Mar 2025 | DTECH talk: gen-AI, RAG, LLMs, and "AI agent deployment" on a customer lakehouse [7][8] | Text and data AI exists. Voice is the missing channel |

## 3. Contact Center & Stack
| Layer | Vendor (evidence) | Class → implication |
|---|---|---|
| CCaaS / omnichannel | **Five9** at SouthStar Energy (IVR, ACD, chat, text, AI tools) [9] | **Partner** → co-sell. Unknown whether Five9 extends to the gas utilities or Georgia Power |
| Contact center QA / WFM | NICE SmartCenter as the standard across centers ⚠️ (old article) [11] | **Either** → if still NICE, find which speech engine runs under analytics |
| Speech engine / IVR | **Unknown**. Public posts describe a multi-level voice menu [12] | Discovery Q1. *🧠* DTMF or directed-speech IVR |
| AI / data platform | Databricks and Azure AI named in AI Engineer posts [17]; CGI as data partner [7] | *🧠* Azure Speech is a likely default → bake-off |
| CRM / billing | **Unknown** | Integrate through the voice agent's tool calls |

**Ops & hiring:** Southern Company Gas runs care centers in Riverdale, GA and Virginia Beach, VA (~200 employees under one manager) for Atlanta Gas Light, Chattanooga Gas, and Virginia Natural Gas [10], plus a Mississippi Power center in Gulfport, MS [13]. Georgia Power and Alabama Power center locations and headcount are **Unknown**.

## 4. Buying Committee
| Person | Background | Likely role |
|---|---|---|
| **Kerry Hogan** — VP Customer Experience, Southern Company Gas [5] | At the company since 2006. Owns care, billing, collections, energy assistance, and digital experience design. Leads the multi-year Digital Transformation Strategy | **Champion / economic buyer for the land.** Best first meeting |
| **Latanza Adjei** — SVP & Chief Customer Officer, Georgia Power [4] | Joined 1994 (Georgia Tech IE). Previously VP Sales & Marketing and VP Corporate Services. Owns physical and digital channels | Exec sponsor for the largest expansion (2.8M customers) |
| **Hans Brown** — EVP & Chief Information Technology Officer [3] | Ex-BNY CIO and Global Head of Enterprise Innovation. Started Jul 31, 2025 | Technical approver, vendor and AI strategy |
| **Jesse Killings** — SVP Customer Operations, Southern Company Gas [6] | Owns customer experience, resource management, and safety training | Kerry Hogan's line leader. Needs to sign off |
| **Alexia Borden** — SVP Customer & Community Engagement, Alabama Power [16] | Oversees Customer Operations and six business divisions | Later expansion sponsor (1.56M customers) |

## 5. Pain → Deepgram Fit
| Signal | *🧠* Pain | Deepgram answer + proof |
|---|---|---|
| Storm seasons; Helene was the most destructive storm in the utility's history [14] | Outage and restoration calls spike past staffing | Voice agent handles outage status and ETR calls at any volume. Covers peaks without overtime |
| Hold and menu complaints [12] | Callers can't get through menus and escape to agents | Nova accuracy on account numbers, addresses, and Southern accents. Five9 healthcare deployment **doubled authentication rates** |
| Gen-AI and lakehouse program [7] | AI investment so far covers text and data, not the phone | Voice Agent API with their own LLM and RAG, plugged into the lakehouse |
| Five9 at SouthStar [9] | Five9 IVA speech accuracy limits containment | Deepgram already powers STT inside Five9 IVA Studio. Upgrade, not a replacement |
| Regulated customer data and union workforces | Change and data-handling risk | VPC or on-prem deployment. Frame as helping agents with peaks, not reducing headcount |

**ROI sketch:** Calls per year are **Unknown**. Assume 9M customers × ~1 call/yr = 9M calls (assumed). Conservative: 9M × 30% automatable × 50% containment × ($4 − $1.50) ≈ **$3.4M/yr**. Midpoint: 9M × 40% × 60% × ($6 − $1) ≈ **$10.8M/yr**. All inputs are playbook defaults except customer count [1].

## 6. Talk Track & Objections
- **Opener:** "You've built a 360° customer view and are deploying gen-AI agents on it. The phone is still where most of your customers show up on the worst day, during a storm. We'd like to see if a voice agent on your Five9 platform can take those calls."
- **Angles:** *Kerry Hogan:* containment and authentication by intent, peak coverage, energy-assistance and payment calls. *Hans Brown:* bring-your-own LLM, Azure or VPC deployment, one speech layer across opcos. *Latanza Adjei:* outage-season experience for 2.8M customers.
- **Proof:** Five9 healthcare deployment (2× authentication) and Abby Connect (100,000+ calls/month).

| Objection | Response |
|---|---|
| "Five9 / our vendor already has AI" | Good. Deepgram runs inside Five9 IVA Studio, so this upgrades the speech layer you already own |
| "We're on Azure / Microsoft" | Bake-off on your recorded calls: accuracy on account numbers and addresses, latency, cost per hour. Deepgram can run in your VPC |
| "Regulators and unions" | Agents get the complex calls; the AI takes outage status and payment arrangements. Audio stays in your environment |
| "Rates are frozen; no budget" | Cost takeout under a rate freeze. Often lands in the existing Five9 line |

## 7. Discovery Questions
1. "Which IVR and speech engine handle Georgia Power, Alabama Power, and the gas utilities' calls today? Is Five9 used beyond SouthStar?"
2. "How many calls a year do the care centers take, and what share is outage, billing, payment arrangement, or start/stop service?"
3. "What happened to call volume and service level during Helene, and what's the plan for the next major storm?"
4. "Your lakehouse team is deploying AI agents. Is voice on that roadmap, and who owns it: IT under Hans Brown or customer experience?"
5. "What would a pilot need to prove for regulators, the union, and your security team?"

## 8. Next Best Actions
1. **Five9 account team** (partner channel): confirm Five9 scope across Southern Company Gas and ask for a warm intro to Kerry Hogan.
2. **Kerry Hogan** (email after the intro): one paragraph on storm-season call coverage and the Five9 2× authentication proof; propose a 30-minute discovery call.
3. **Hans Brown** (LinkedIn or executive event): a note on the voice gap in the gen-AI program and a VPC bake-off offer.
4. Q3 earnings (Nov 5): capture any AI or cost-to-serve quote for the follow-up.

**Fit score:** Volume 27/30 · Pain 15/25 · Timing 13/20 · Stack 11/15 · Access 3/10 · Competitor adj −0 = **69/100**

## Sources
1. SEC — Southern Company Form 10-K FY2025 (Feb 2026) — [sec.gov](https://www.sec.gov/Archives/edgar/data/92122/000009212226000006/so-20251231.htm)
2. Southern Company — Second-quarter 2026 earnings (Jul 30, 2026) — [southerncompany.mediaroom.com](https://southerncompany.mediaroom.com/2026-07-30-Southern-Company-reports-second-quarter-2026-earnings)
3. Southern Company — Hans Brown named EVP & CITO (Jul 21, 2025) — [southerncompany.mediaroom.com](https://southerncompany.mediaroom.com/2025-07-21-Southern-Company-names-Hans-Brown-Executive-Vice-President-Chief-Information-Technology-Officer)
4. Georgia Power — Latanza Adjei leadership bio (undated) — [georgiapower.com](https://www.georgiapower.com/content/dam/georgia-power/pdfs/about/leadership/bio-latanza-adjei.pdf)
5. ACI Worldwide — Kerry Hogan speaker bio (undated) — [events.aciworldwide.com](https://events.aciworldwide.com/paymentsunleashed/speaker/1891874/kerry-hogan)
6. Southern Company Gas — Jesse Killings leadership page (undated) — [southerncompanygas.com](https://www.southerncompanygas.com/who-we-are/leadership/jesse-killings.html)
7. DISTRIBUTECH — "Can generative AI transform customer engagement? Southern Company paves the way" (Mar 25, 2025) — [distributech.com](https://www.distributech.com/2025-technical-conference-sessions/can-generative-ai-transform-customer-engagement-southern-company-paves-the-way)
8. CGI — How Southern Company turned governed data into enterprise AI value (podcast, undated) — [cgi.com](https://www.cgi.com/en/podcast/energy-utilities/how-southern-company-turned-governed-data-enterprise-ai-value)
9. Job post — SouthStar Energy omnichannel (Five9) role (undated, search excerpt) — [abilitylinks.org](https://abilitylinks.org/jobs/407192689/apply)
10. Job post — Southern Company Gas Manager, Customer Care Center (undated) — [abilitylinks.org](https://abilitylinks.org/jobs/184860454-mgr-customer-care-center)
11. Speech Technology — U.S. utility expands use of NICE SmartCenter ⚠️ (older than 12 months) — [speechtechmag.com](https://www.speechtechmag.com/Articles/News/Speech-Technology-News/U.S.-Utility-Expands-Use-of-NICE-SmartCenter-51769.aspx)
12. Aggregated blog post (low reliability) — "Why Georgia Power's customer service is a nightmare" (undated) — [flashtelecom.es](https://doapi.flashtelecom.es/post/why-georgia-powers-customer-service-is-a-nightmare-for-everyday-customers)
13. Job post — Southern Company Customer Service Representative, Gulfport MS (undated) — [blackcareernetwork.com](https://blackcareernetwork.com/job/customer-service-representative-777)
14. AP via Washington Times — Georgia Power agrees to hold rates steady; Helene costs excluded (May 19, 2025) — [washingtontimes.com](https://www.washingtontimes.com/news/2025/may/19/utility-georgia-power-agrees-hold-rates-steady-doesnt-include/)
15. WSB-TV — Georgia PSC approves base-rate freeze through 2028 (2025) — [wsbtv.com](https://www.wsbtv.com/news/local/atlanta/georgia-power-agrees-freeze-base-rates-through-2028/FQEB3ZGQ25BS7F252ESTWOYKCM/)
16. NNPA — Alabama Power announces leadership changes (undated) — [nnpa.org](https://nnpa.org/alabama-power-announces-leadership-changes)
17. Job post — Southern Company Services AI Engineer or Analyst (undated) — [abilitylinks.org](https://abilitylinks.org/jobs/503410557/apply)
18. Finviz — Southern Company Q3 2026 earnings to be released Nov 5 (Sep 25, 2026) — [finviz.com](https://finviz.com/news/395620/southern-company-third-quarter-2026-earnings-to-be-released-november-5)
19. Southern Company — History — [southerncompany.com](https://www.southerncompany.com/about-us/history.html)
