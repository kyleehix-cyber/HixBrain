# Humana — Internal Pre-Meeting Prep

**Account owner:** Kyle Hix · **Prepared:** Oct 5, 2026 · **Fit score:** 77/100 (active prospect) · **Full brief:** next pages

> **Purpose of this meeting:** agree on how we enter Humana, who we contact first, and what each of us owns. Medicare Annual Enrollment opens **Oct 15**, so the outreach window is now.

## The account in 60 seconds
- **Scale:** 20,000+ member advocates handle up to **~80M member calls a year**. One of the largest inbound voice operations in U.S. healthcare.
- **Incumbent:** **Google Cloud** (Vertex AI / Gemini) powers *Agent Assist*, a copilot for human advocates, rolling out across member service centers through 2026. Humana claims $100M+ in savings over a few years.
- **Gap:** No public evidence of AI that resolves calls on its own. Routine calls still reach a person. Reviews cite 30–45-minute holds.
- **Mandate:** On the Q2 call, the CEO said Humana wants to be "simpler, leaner and faster" and to lead with "automation and AI with best-performing vendors."
- **Timing:** Enrollment peak (Oct 15 – Dec 7) plus ~600K members getting plan-exit letters. A new CTO (Apr 2026) and CDO (Jul 2025) are both in their first year.

## Decisions we need today
| # | Decision | Options | Kyle's recommendation |
|---|---|---|---|
| 1 | **Lead motion** | (a) Direct: Voice Agent API for self-service, bake-off vs. Google speech · (b) Co-sell through their CCaaS partner | **(a) now**, switch to (b) if discovery shows Five9 / Amazon Connect / Twilio / Genesys |
| 2 | **First door** | CDO Damian Warren (digital and self-service) · CTO Bobby Mukundan (technical) · both | **Both in parallel.** Warren on the business case, Mukundan on the bake-off |
| 3 | **Bake-off offer** | Size, scope, and data handling | ~500 real member calls; accuracy on member IDs, drug names, senior voices; latency; cost per hour; run in their VPC |
| 4 | **Timing** | Before Oct 15 vs. after the enrollment peak (Dec 7) | **Before Oct 15** for the first touch, framed as "for your January / next enrollment period." Expect meetings to land in December or January |
| 5 | **Exec involvement** | Deepgram exec to CTO-level outreach? | Yes. Peer note to Mukundan (ex-CVS CIO, ex-JPMorgan CTO) |

## Who does what (assign owners)
| Workstream | Owner | Due |
|---|---|---|
| Outreach to Damian Warren (CDO) + business-case email | Kyle Hix | Before Oct 15 |
| Technical note + bake-off proposal for Bobby Mukundan (CTO) | Sales Engineer: ______ | Before Oct 15 |
| Ask Five9 / AWS / Twilio / Genesys partner teams whether Humana is their customer | Partner manager: ______ | This week |
| Check our own CRM and console for existing humana.com sign-ups, usage, or past opportunities | ______ | This week |
| Healthcare security pack (HIPAA BAA, VPC / on-prem, PHI handling) ready for procurement | ______ | Before first meeting |
| Exec-to-exec note to CTO | Exec sponsor: ______ | After partner check |
| Find the VP / Director of Member Services (contact center leader) | Kyle Hix / BDR: ______ | This week |

## What we still don't know (and how we'll find out)
| Unknown | Why it matters | How to find out |
|---|---|---|
| CCaaS / telephony platform | Decides direct vs. co-sell | Partner teams; job posts; ask in discovery |
| Speech engine under the IVR | Displacement target (Google? Nuance?) | Discovery Q4; SE network |
| BPO vendors for member calls | Savings case and timing of contract renewals | Discovery Q7; 10-K |
| Contact center leader's name | Champion with the most enrollment-season pain | Web search; LinkedIn via network |
| Any existing Deepgram footprint | Expansion vs. new logo | Internal CRM and console check |

## Risks to discuss
- **Google is entrenched.** It shipped a visible win and claims $100M+ in savings, and may bundle Gemini virtual agents next. *Counter:* compete on measured accuracy, latency, and cost on their audio. Bring your own LLM, so they can keep Gemini as the brain.
- **Peak-season freeze.** Operations and IT may not take meetings from Oct 15 to Dec 7. *Counter:* aim the first touch at the 2027 roadmap and land meetings in December or January.
- **Vendor consolidation.** Humana is reducing vendors. *Counter:* position as replacing IVR speech and BPO spend, or deliver through a partner they already pay.
- **Compliance.** CMS marketing rules, HIPAA, and a senior population. *Counter:* VPC / on-prem deployment; start with low-risk informational intents.
- **Evidence quality.** Several facts in the brief come from search-result excerpts. Verify the linked sources before quoting them to Humana.

## Proposed first customer meeting (30 min)
1. **Intros and purpose** (3 min)
2. **Their priorities:** 2027 self-service roadmap, enrollment-season results (7 min)
3. **Discovery:** top routine intents; speech engine under the IVR; authentication failure rate (10 min)
4. **Proof:** Five9 healthcare result (authentication rates doubled) plus a short live voice-agent demo (6 min)
5. **Next step:** agree on bake-off scope and a data-handling path (4 min)

## Asks of the team
- Bring any Humana or health-plan relationships you have (former colleagues, partner contacts).
- SE: confirm we can run the bake-off in a Humana VPC and how long it takes to stand up.
- Marketing: do we have a payer / health-plan reference we can name?
