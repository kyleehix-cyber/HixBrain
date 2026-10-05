# PolyAI — Internal Pre-Meeting Prep

**Account owner:** TBD (see Decision 1) · **Prepared by:** Kyle Hix · **Prepared:** Oct 5, 2026 · **Fit score:** 63/100 (active prospect, OEM expansion) · **Full brief:** next pages

> **Purpose of this meeting:** decide whether and how Deepgram expands at PolyAI, who leads, and how we handle Kyle's recent employment there.

## The account in 60 seconds
- **What they are:** an enterprise voice-agent vendor (Marriott, Caesars, PG&E, UniCredit, FedEx). $200M+ raised, Series D Dec 2025, NVIDIA's NVentures is an investor.
- **Already a Deepgram account (per their docs):** Deepgram is one of **seven ASR providers** PolyAI routes calls to by language, with automatic fallback. Google, AWS, OpenAI Whisper, and NVIDIA are the others.
- **They are bringing speech in-house:** Owl ASR (built on NVIDIA Riva) and **Dialog-RSN-1** (Jul 30, 2026), an audio-native model that absorbs ASR. **It is English only.**
- **Opening:** the non-English and fallback minutes across 75 languages, plus **TTS**. Their list has seven TTS vendors (ElevenLabs, Cartesia, Rime, and others) and **no Aura**.
- **New people:** Paul Asoyan (VP Strategic Alliances, ex-Google) and Helen Greul (SVP Eng) both joined in May 2026.

## Decisions we need today
| # | Decision | Options | Recommendation |
|---|---|---|---|
| 1 | **Who leads the account** | Kyle · existing Deepgram owner / partnerships team · joint | **Existing owner or partnerships leads; Kyle advises on public information only** until legal clears it |
| 2 | **Motion** | OEM expansion · co-sell into shared CCaaS accounts · both | **OEM expansion first** (ASR share + Aura); co-sell as phase 2 |
| 3 | **Bake-off scope** | Non-English ASR · TTS (Aura) · both | **Both:** their 3–5 highest-volume non-English languages, plus an Aura latency / cost test |
| 4 | **Commercial stance** | Volume pricing aimed at self-serve margins? | Decide internally after pulling current usage |
| 5 | **Position vs. RSN-1** | Compete in English · complement | **Complement.** Don't fight Owl or RSN-1 in English |

## Who does what (assign owners)
| Workstream | Owner | Due |
|---|---|---|
| Find the current Deepgram owner of PolyAI; pull usage (minutes, languages, Nova vs. Aura, trend) | ______ | This week |
| Legal / manager review of Kyle's PolyAI separation agreement (confidentiality, non-solicit) | Kyle Hix + Legal: ______ | Before any outreach |
| Outreach to Paul Asoyan (VP Strategic Alliances) | Account owner: ______ | After the two items above |
| Bake-off plan: non-English ASR on their audio + Aura TTS test | Sales Engineer: ______ | Before first meeting |
| Map shared Five9 / Genesys / Amazon Connect / Twilio accounts | Partner manager: ______ | Two weeks |
| Check whether NVIDIA-related terms limit vendor choice (from public information only) | ______ | Discovery |

## What we still don't know (and how we'll find out)
| Unknown | Why it matters | How to find out |
|---|---|---|
| Deepgram's current share of PolyAI ASR minutes | Sets the size and baseline of the opportunity | Internal usage data |
| Which languages route to which provider | Defines the bake-off targets | Discovery Q1–Q2 |
| RSN-1 roadmap beyond English | Decides how long the opening lasts | Discovery Q3; watch PolyAI's blog |
| Speech ML lead's name | The technical evaluator | Public posts and talks; ask Asoyan |
| How NVIDIA's investment affects speech vendor choice | Possible hidden blocker | Discovery Q7 |

## Risks to discuss
- **Conflict of interest.** Kyle left PolyAI in Sep 2026. *Counter:* legal review; use public information only; another rep or partnerships leads the account.
- **In-house speech shrinks third-party ASR.** RSN-1 may expand to more languages. *Counter:* also win TTS (Aura), which RSN-1 leaves open by design, and lock in multilingual volume now.
- **NVIDIA alignment.** Investor plus Riva base. *Counter:* position Deepgram as managed multilingual coverage they don't have to train, routed by measured accuracy.
- **Price pressure** from a vendor that buys infrastructure. *Counter:* commit to volume tiers; show the full cost (fallback, vendor sprawl), not just the per-minute rate.
- **Evidence quality.** Poly.ai and Deepgram pages were blocked during research; key facts (the provider list in particular) come from search excerpts. Verify before quoting.

## Proposed first customer meeting (30 min, with Alliances + Engineering)
1. **Intros and purpose** (3 min)
2. **Their roadmap:** RSN-1 languages, self-serve growth, channel goals (7 min)
3. **Discovery:** ASR routing per language, TTS choice, where speech fails (10 min)
4. **Proof:** Nova multilingual / alphanumeric results; live Aura latency demo (6 min)
5. **Next step:** agree on bake-off languages and an audio-sharing path (4 min)

## Asks of the team
- Partnerships: is PolyAI a known partner or OEM account? Who owns it?
- SE: can we run a non-English bake-off on telephony audio within two weeks?
- Marketing: an Aura reference in voice agents, and any named multilingual Nova proof point.
