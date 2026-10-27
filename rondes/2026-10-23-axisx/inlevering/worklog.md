# Work log: AxisX, AI Marketing Kombat Stage 2

Team: Bjorn (human lead, all decisions). Models: Claude (Claude Code: one main session and three parallel sessions) and ChatGPT (three sessions, its extracts and research notes were fed into Claude). Time: 15:07 to 17:07 CEST, 23 October 2026.

This log is assembled from the raw session exports and our own notes. The raw material is attached unedited:
- `worklog-sessie-export.md`: main Claude session, 15:07 to 16:25, every prompt, model answer and tool call (times in UTC, add two hours).
- `worklog-parallel-cf7388bd.md`: parallel session, five research agents (deep dives 2 to 6), 15:50 to 15:57.
- `worklog-parallel-caf54828.md`: parallel session, hooks, hook selection by the simulated panel, last slide for the founder, 15:58 to 16:27.
- `worklog-parallel-39621d59.md`: parallel session, campaign name question to the panel, 16:29 (short, not used in the deck).
- `AxisX_volledige_chat_2026-10-23 (1).md`: ChatGPT session A, 15:14 to 16:44, strategy: competitors, why AxisX exists, community-led acquisition, Founding 500, extract for Claude Code.
- `AxisX_volledige_chat_en_onderzoek_2026-10-23.md`: ChatGPT session B, about 16:00 to 16:40, the five research questions, the selection quiz and landing page questions, with both research notes in full as appendices.
- `AxisX_volledige_chat_2026-10-23.md`: ChatGPT session C, 16:27 to 16:44, perimenopause symptoms for the pitch, origin of "What they'll see. What they don't see.", second handoff file.
- The three ChatGPT files are readable Markdown conversions made by ChatGPT itself (their own header says they are not byte-exact exports). They hold every visible prompt and answer, not hidden reasoning.
- Deck iterations 16:30 to 17:02 are reconstructed from the git history (16 commits in this round) and the notes in section 8.

## 1. How we worked, in six lines
1. Fixed round routine first (skill `ronde-start`): work folder, rules file distilled from the brief, AI-errors file, rejections file, tool check (Meta Ad Library, WebSearch, Loudbox).
2. Questions to the organisation went out early. A simulated panel of marketing experts (AI role-play on the public work of leading practitioners) cut 11 draft questions to 9 short practical ones.
3. Research ran in parallel: three Claude research agents (audience, paid economics, competitors and AI risk), then five deep-dive agents in a second session (economic anchor, ceiling, ad policy, quiz-to-day-7 measurement, Ad Library run lengths), and a ChatGPT session for the strategic core.
4. Every number traced to a linked source or labelled ASSUMPTION; two small Python models (`funnel_model.py`, `plan_b_model.py`) so each figure can be recomputed. When the model's numbers became unclear ("abracadabra"), Bjorn stopped the deck and asked for a plain-language explanation first.
5. The panel reviewed four times (questions, full brief, campaign plan, hooks) and changed the plan each time (section 4).
6. The human made the strategic calls (section 3); the model proposed, researched, calculated and wrote. Two things were deliberately kept away from the model: the founder's own first sentence and the 30-second pitch card.

## 2. Timeline: prompts, tools, outputs (local time)
| Time | Session | Bjorn's prompt (shortened, original wording in the exports) | What the model did | Output / commit |
|---|---|---|---|---|
| 15:07 | main | Brief PDF attached; start the round | Skill `ronde-start`; read lessons from round 1; work folder, `regels.md`, 11 draft questions | commit 15:08 |
| 15:12 | main | "Kun je de vijf vragen even langs ons panel laten gaan?" | Skill `panel-review`, review 1 on the top-5 questions | `panel-log.md` |
| 15:15 | main | "En nu samenkomen tot praktische vragen aub?" | 7-question set, then a 9-question short set | `vragen.md`, commit 15:13 |
| 15:16 | main | Full brief part 2 pasted | Rules extended (definitions, red lines, deliverables); Ad Library search "perimenopause" UK/US; first strategy concept "No two systems alike" | `regels.md`, `strategie.md`, commit 15:24 |
| 15:22 | main | "Dit is een heel goede vervolgstap!" | Three research agents started (audience and communities; paid economics; competitors and AI risk); funnel model written | `data/onderzoek-*.md`, `funnel_model.py`, commit 15:27 |
| 15:28 | main | (model proposed to build the deck now) | Rejected by Bjorn, see 15:40 | |
| 15:40 | main | "Nee we zijn hier nog lang niet aan toe ... te veel abracadabra ... laat Avinash Kaushik mij even helpen dit te verduidelijken" | Plain-language numbers (100 visitors, plan A, plan B, break-even); FX error caught; rejections file started | `data/cijfers-helder.md`, `afwijzingen.md` |
| 15:49 | main | "Active founder D7 = feedback in the first 7 days; day-14 report as second metric. Leg dit vast." | Measurement plan with the brief's KPIs as score and two steering metrics | `meetplan.md`, commit 15:50 |
| 15:50 | parallel 1 | "Kun jij wat research agents aan het werk zetten" (five deep-dive questions from the panel synthesis) | Five agents in parallel, each to its own file; model re-checked the Web2Wave 48-hour claim itself | `data/induik-2..6.md` |
| 15:53 | main | ChatGPT extract added: "lees dit uit en haal inspiratie voor verdere campagnevoering" | Campaign input: community-led acquisition, Founding 500, partner offer, weekly plan | `campagne-input.md`, commit 15:54 |
| 15:58 | parallel 2 | "Hook bouwer en taste skill ... betere hooks dan From feeling lost in your own body ... ABM op communities en community leaders" | Skills `hook-generator` and `viral-hooks`; hooks for leaders and five personas; AI error caught ("Is this perimenopause?") | `hooks.md` |
| 16:00 | main | "Panel review dit plan ... welke meetwaardes ... plus private invites vanuit de founder, geadviseerd door AI, aan kartrekkers met haar eigen verhaal" | Panel review 3 (7 members): invite codes, one steering metric, public role not health posts, founder hours | `panel-log.md`, commit 16:01 |
| 16:02 | parallel 2 | "Er is een panellid die de selectie kan maken" | Creative panel member (simulated) selects 4 member hooks, 8 openings, cuts vague hooks | `hooks.md` section 6 |
| 16:07 | main | "AVG 100% meenemen: AI analyseert en adviseert, dan data verwijderen; publieke rol, geen profilering. Neem induik 2-6 en het marktonderzoek mee, panel: solide basis? Presenteer deel 1: wat doen we met A?" | Plan A written; economic anchor corrected (RevenueCat 2.9/6.2%); panel review 4 | `plan-A.md`, commit 16:10 |
| 16:17 | main | "Ja, funnel, quiz en hooks gebruiken" + selection note pasted (select on recognition, search, fit with the method, ability to test now) | Funnel content: text and image per step | `funnel-inhoud.md`, commit 16:18 |
| 16:20 | parallel 2 | "Laatste slide aan de founder: geef jouw sterkste zin" | Model declined to write her line; slide asks her for it with three questions | `slide-laatste-founder.md` |
| 16:22 | main | "Vragen zo open mogelijk ... met AI classificeren ... testgroep met mensen bij wie we die signalen niet horen" | Four open questions, AI classification (structured output, prompt and model version logged), signal group and contrast group | `funnel-inhoud.md`, commit 16:23 |
| 16:25 | main | "Iedereen die zich aanmeldt voor de Founding Circle krijgt goedkoper toegang" | Founding price £70 instead of £100 for every applicant | commit 16:25 |
| 16:26 | main | | Plan B: three stages, honest break-even line | `plan-B.md`, commit 16:26 |
| 16:29 | parallel 3 | "Panel members: what do we call the campaign?" | Started reading the plan; not used, "The Founding 500" kept | |
| 16:30 | main | Build the deck | Deck v1 (8 slides, PDF) and first work log | commit 16:30 |
| 16:43 | main | "This isn't it" and new structure set by Bjorn | Deck v2 rebuilt around "What they'll see. What they don't see."; appendix in plain language | commit 16:49 |
| 16:51 | main | "Too dense" and storyline set by Bjorn | Deck v3: one idea per slide, closing line "We only need your story to start the story", appendix with panel validation | commits 17:00, 17:01 |
| 16:55 | new session | "Upgrade this 30 sec pitch, add facts and style so I can redo it in my own words" | Fact sheet with corrections (700 to 500, "Exis" to AxisX, AI disclosure) and style rules; example version marked not for use | `pitch-card-feiten-en-stijl.md` |
| 17:05 | new session | "Stel de worklog samen uit de volledige chats en onze eigen worklog" | This file | `worklog.md` |

## 2b. ChatGPT sessions (local time, from the three exports)
| Time | Session | Bjorn's prompt (shortened) | What ChatGPT did | Where it went in Claude |
|---|---|---|---|---|
| 15:14 | A | Brief part 1 attached: "ik wil dat je aan het einde een extract van onze gesprekken deelt"; short question on thePause, Play Health, Waves Women, Balance | Competitor overview with what makes each different | `data/onderzoek-concurrentie-ai.md` cross-check |
| 15:24 | A | Brief part 2 pasted: "meer over het probleem zelf en de bestaande community ... wat geeft AxisX bestaansrecht volgens jou?" | Problem, existing communities, where AxisX can exist (personal system, not more tracking or information), what is not convincing yet | `strategie.md` |
| 15:34 | A | "Binnen die communities met behulp van AI de juiste mensen opsporen en activeren ... Account Based Marketing maar hyper-personalized ... Founders Circle ... altijd gratis ... vriendinnen ook gratis" | Founders Circle concept, referral design, a stated precondition on privacy and cost | Core of plan A. "Free forever for all" kept only as a risk scenario |
| 15:45 | A | "Extract in md formaat voor Claude Code, waar ik de numbers game doe en een panel heb opgezet" | Strategic context file (Founding 500, community-led acquisition, decisions) | `AxisX_Founding_500_strategisch_context_extract.md`, read into Claude 15:53 |
| about 16:00 | B | The five research questions (economic anchor, ceiling, ad policy, quiz to day 7, Ad Library) | Research note with sources and an explicit split between verified benchmarks and assumptions | `AxisX_marktonderzoek_businesscase_2026-10-23.md`, read into Claude with deep dives 2 to 6 at 16:07 |
| about 16:15 | B | "Niet het vinden van mensen die helpen activeren, maar de mensen die vanuit de activatie komen kijken ... zeker 500 aanmeldingen en minstens 300 plakkers" | Selection model, landing page copy that selects, pre-screen questions, nine quiz questions, D7 definition | Selection note pasted into Claude 16:17; became the open-question funnel at 16:22 |
| 16:27 | C | "Wat zijn de meest voorkomende premenopauze symptomen? Ik moet de aandoening beter begrijpen, als man" | Symptom overview and the insight that recognition differs from reality | Symptom context line in the deck, with NHS and Flo/Mayo sources |
| 16:32 | C | "What they'll see and what they don't see is iets waar ik mee ga spelen" (front: campaign language, design, funnel; back: systematics, applied AI, success metrics; a page "what you'll see"; the known last slide) | Second handoff file with the analysis and a decision register | `AxisX_campaign_pitch_continuation_2026-10-23.md`. This became the deck structure (v2, 16:49) |
| 16:44 | A, B, C | "Kan jij deze hele chat als md aanleveren?" | The three exports in this folder | Attached to this log |

## 3. Human decisions that shaped the solution
- The strategic core is Bjorn's: AI-powered community-led acquisition (account-based marketing on communities, not on individuals) and private founder invites to community leads with her own story. The model's first concept (quiz, content from real systems, answer pages) became the funnel underneath it.
- Stop the deck, explain the numbers first (15:40). The deck was built only after plan A, the funnel and plan B were on paper.
- Steering metrics: Active founder D7 (feedback given in week 1) and the day-14 doctor report, on top of the brief's score (500 onboarded, 60% open on day 7).
- GDPR line: AI analyses public conversations at theme level, raw text deleted afterwards, leads chosen on public role, no health profiling, founder sends every message herself, no automated DMs.
- Open questions instead of a tick-box quiz; AI classifies her own words; a random contrast group without the signals so plan B learns whether retention comes from the selection or the market.
- Founding price for every applicant (£70 instead of £100) as an extra reason to apply and as the paid signal for plan B.
- Deck frame: "What they'll see. What they don't see." is Bjorn's own idea (ChatGPT session C, 16:32), with the double meaning of the woman's visible and invisible day and the campaign's visible front and invisible engine. He then reset the storyline twice (16:43, 16:51): one idea per slide.
- Last slide left blank for the founder's own sentence; pitch card written by Bjorn himself.

## 4. What the model proposed that we rejected or changed, and why
| Time | Model proposed | What we did | Why |
|---|---|---|---|
| 15:10 | 11 questions to the organisation, with explanations | 9 short practical questions | Must be answerable directly |
| 15:13 | "Selection on fit is how we hit 60% day 7", no caveat | Random contrast group of lower-fit applicants | Selection inflates retention; the investor plan would inherit a number that does not scale (panel) |
| 15:28 | Build the deck (7 slides, PDF) right after the first funnel model | Rejected; analysis and a real campaign first | Numbers were "abracadabra"; the campaign did not exist yet |
| ChatGPT | Recruit women who do not yet recognise perimenopause | Removed | The full brief rules them out for the first 500 |
| ChatGPT | Lifetime free for all founders and friends (Bjorn's own idea in that session) | Kept only as a risk scenario | Price model and cost per user unknown |
| 15:5x | Research agent: "Is this perimenopause?" as quiz hook | Removed | Same reason: the brief wants women who already recognise it |
| 15:5x | Research agent wanted a Web2Wave 422 tool error logged as an AI error | Not logged | Tool configuration issue, not a model error |
| 16:00 | Select community leads on what they post about their symptoms | Select on public role only (moderator, admin, newsletter, coach) | Health profiling of individuals (GDPR art. 9) and platform rules |
| 16:00 | Many loose metrics | Brief KPIs as score, one steering metric, stop rule per source | One decision per metric |
| 16:02 | 13+ hooks, 50 reserved places per community | 4 hooks kept, 8 openings; 10 places per community | Must land in 3 seconds, work muted, be sayable by a real woman; scarcity per community |
| 16:10 | Closed 8-question quiz | 4 open questions plus AI classification | Matches how the app works; the signals are in her own words |
| 16:20 | Model writing the founder's first line | Left blank on purpose | A model writes something smooth; the women in these communities would hear it is not hers |
| 16:29 | New campaign name from the panel | Kept "The Founding 500" | No time, and the name already carried the deck |
| 16:30 | Deck v1 | Rebuilt twice to Bjorn's structure | First too technical, then too dense |
| 16:45 | Claude Design brand pass for the deck | Dropped, restyled by hand | Time |
| 16:55 | Example pitch text in the fact sheet | Not used as written | Brief: the pitch card must be Bjorn's own words; a model version is penalised |

## 5. AI errors we caught
| Time | AI said or did | Should have been | Caught by |
|---|---|---|---|
| 15:13 | "Selection on fit is how we hit 60% day-7 retention" as a lever without caveat | Selection hits 60% but makes the 500 unrepresentative; contrast group needed | Simulated panel |
| 15:28 | Compared cost per onboarding in dollars ($7-20) with a break-even in pounds (£8.50-25.50) | Convert first with a sourced FX rate (1.32, currency-converter.org.uk) | Plain-language review |
| 15:28 | Proposed building the deck before the campaign existed | Analysis and campaign first | Bjorn |
| 16:00 | Research agent advised "Is this perimenopause?" as hook | Out of scope: the brief excludes women who do not recognise it yet | Claude, hooks check |
| 16:10 | "1, 2 or 3 in 10 onboarded women will pay" without source | Public anchor 2.1-6.2% download-to-paid (RevenueCat 2026); a woman is worth $2-7 in year 1, not $11-34. This turned plan B into an honest test instead of a growth plan | Deep dive 2 |
| 16:3x | A shell command hung on an empty `cat` and created a stray empty file | Stopped, file removed | Claude itself |
| 16:55 | Bjorn's pitch draft said "700 women" and "Exis"; the fact sheet flagged both | 500 onboarded, 300 on day 7; AxisX | Fact check against the brief |

## 6. Tools, skills and agents
- Claude Code skills: `ronde-start`, `panel-review` (4 reviews), `hook-generator` and `viral-hooks` (parallel session), measurement-plan logic from `meetplan`. The `taste-skill` was found and not used (it covers landing-page design).
- Research agents: 3 in the main session (15:22) and 5 in parallel session 1 (15:50), each writing to its own file, each under the rule "a number counts only if you checked it on a public page, with the link".
- Meta Ad Library (MCP `ads_library_search`, 3 searches plus the deep-dive agent): about 28k US ads on "perimenopause app", 5,247 active UK ads on "perimenopause"; named-woman and named-doctor advertorial pages; anna app as the only direct app advertiser; Flo and BioID run lengths.
- Web2Wave MCP: creative trends (run lengths 200-435 days for Flo and BioID), documentation check of the 48-hour identify window.
- WebSearch and WebFetch via agents: RevenueCat, Adapty, StatCounter, ONS, US Census, Eurostat, superads, influee/Triple Whale, Meta and Google policy pages, Apple TestFlight documentation, NICE NG23, NHS.
- Python (standard library only): `funnel_model.py`, `plan_b_model.py`; `scripts/sessie_naar_md.py` to export the sessions to this log.
- ChatGPT (three sessions, section 2b): competitor overview, brand reason to exist, the community-led acquisition idea shaped with Bjorn, a market research note on the same five questions the Claude agents ran, selection quiz research, symptom background for a male presenter, and two handoff files. Its research note and the Claude deep dives were read side by side before plan A; where they differed the linked public source decided.
- Loudbox demo: checked at 15:08, not used (workspace held other data).
- Git: 16 commits between 15:08 and 17:01, so every version of the plan and the deck is recoverable.

## 7. Files behind the deck
`regels.md` · `vragen.md` · `strategie.md` · `campagne-input.md` · `meetplan.md` · `plan-A.md` · `plan-B.md` · `funnel-inhoud.md` · `hooks.md` · `slide-laatste-founder.md` · `pitch-card-feiten-en-stijl.md` · `panel-log.md` · `panel-pitches.md` · `ai-fouten.md` · `afwijzingen.md` · `data/` (research tables, deep dives 2 to 6, models and outputs) · ChatGPT handoff files in the project root: `AxisX_Founding_500_strategisch_context_extract.md`, `AxisX_marktonderzoek_businesscase_2026-10-23.md`, `AxisX_campaign_pitch_continuation_2026-10-23.md` · the three ChatGPT chat exports in this folder

## 8. Deck iterations (16:30 to 17:55)
- **v1 (16:30).** Eight slides straight from plan A and plan B. Bjorn: "this isn't it". Too technical, the woman was missing.
- **v2 (16:49).** Bjorn set the structure: open on "What they'll see. What they don't see." (the woman's visible day and the effort behind it; the campaign's front and the engine underneath). Plan A, plan B and success metrics split into what they see, what they don't see, what you will see per phase. All technical detail moved to a plain-language appendix. A Claude Design brand pass was considered and dropped for time; restyled by hand (warm paper, plum and terracotta, serif headlines, the member "system card" as the recurring asset).
- **v3, final (17:00).** Bjorn: too dense. Storyline reset to one idea per slide: how we reach the Founding 500, what they experience as a funnel (front and engine), what the funnel teaches for plan B, how A builds B, the money, and the closing line "We only need your story to start the story." Eight slides within the brief's limit. Appendix keeps every detail for the founder, opening with how the panel validated them. The founder's blank line stayed as the last slide. Earlier versions remain in git history.
- **v4, clarity pass (17:20).** Bjorn: the artifact still carried labels nobody could follow ("07:00 tablet, 1 h before food", "expected about 10 to 1", "judged on day 7, not clicks") and the phrase "what a woman is worth", which reduces a woman to a subscription. Simulated panel review, clarity only: every tile, footnote and rule rewritten as full sentences that say what the figure is and what it decides; "what a woman is worth" replaced everywhere (deck, appendix headings, PDF source) by "what a subscription earns back"; the sums are unchanged. Live artifact republished (v3), both PDFs regenerated from the edited HTML and checked slide by slide for overflow.
- **v5, appendix rebuilt (17:35).** Bjorn: the appendix is part of the pitch, it must carry the campaign numbers, not explain the project and the brief back to us. Rebuilt in English, one section per deck slide: the brief in numbers, the story of 100 visitors and plan A's $5,000 line items, what she sees (videos, landing page, application, member card, emails), the engine (open questions, AI labels, signal and contrast group, one ID, trust rules), the measurement plan with stop rules, plan B stages and ceiling, what a subscription earns back with the RevenueCat anchor and the founding price, and the models with English comments. Dropped: the Dutch working notes on the brief's rules and deliverables, decision timestamps, panel-round narrative. Deck section references updated; both PDFs regenerated; artifact republished (v4).
- **v6, slide 2 (17:45).** Bjorn: the example card on slide 2 did not say what it was. Rebuilt as a real member card (header, four rows with time and action) with a plain explanation beside it over the full width; funnel boxes tightened so the slide still fits the PDF page. Artifact v5.
- **v7, the $5,000 (17:55).** Bjorn: $10 a woman is not what the money buys; show where the $5,000 goes and which AI tooling and tokens sit in it. Slide 7 and appendix §2 now split plan A into build ($3,700 before the first invite: funnel and analytics, AI community research, videos and member cards with real women, community space) and run ($1,300: AI previews and classification, partner reports, reserve), with the AI stack per line (Claude API for research, previews and classification; Runway for captions, cuts and card rendering; no AI-generated people) and the point that $10 is an average, not a price. Artifact v6.

## 9. Appendix: models (recompute every number)

### funnel_model.py
```python
"""Funnelmodel AxisX: plan A ($5k, geen paid) en plan B ($50k, paid).
Elke aanname heeft een bron of het label ASSUMPTION (te meten op de eerste 500).
"""

DOEL_ONBOARDED = 500          # brief
D7 = 0.60                     # brief (founder's model)

# Stapconversies webfunnel
STAPPEN = [
    ("landing -> quiz start", 0.50, "Adapty web-to-app: 40-60%"),
    ("quiz start -> quiz complete", 0.60, "Adapty web-to-app: 50-70%"),
    ("quiz complete -> application", 0.70, "ASSUMPTION (Adapty quiz->paywall 70-85% als proxy)"),
    ("application -> approved (fit + quota)", 0.70, "ASSUMPTION, onze selectiekeuze"),
    ("approved -> onboarding complete (TestFlight)", 0.70, "ASSUMPTION, te meten"),
]


def funnel():
    tot = 1.0
    for naam, r, bron in STAPPEN:
        tot *= r
    return tot


def plan_a():
    conv = funnel()
    k = 0.20                    # K-factor-benchmark >0,20 'zeer goed' (blogbronnen, onderzoek-concurrentie-ai.md)
    via_referral = DOEL_ONBOARDED * k
    top = DOEL_ONBOARDED - via_referral
    bezoekers = top / conv
    print("PLAN A")
    for naam, r, bron in STAPPEN:
        print(f"  {naam:45s} {r:.0%}  ({bron})")
    print(f"  landing -> onboarding complete: {conv:.1%}")
    print(f"  onboarded via referral (K=0.20): {via_referral:.0f}; via funnel: {top:.0f}")
    print(f"  landing-bezoekers nodig: {bezoekers:,.0f}")
    print(f"  dag-7 actief bij 60%: {DOEL_ONBOARDED*D7:.0f}")
    budget = {
        "Web funnel + quiz builder + analytics": 1200,
        "LLM tokens (AI quiz preview, rebuild of system preview)": 600,
        "Content generation from real systems (visuals, short video)": 1500,
        "Answer pages (search + AI answer engines), generation + hosting": 400,
        "Founding Circle community space (beta)": 600,
        "Reserve (tests, extra tokens)": 700,
    }
    print(f"  budget totaal: ${sum(budget.values()):,}")
    for k_, v in budget.items():
        print(f"    {k_}: ${v:,}")
    print(f"  kosten per onboarded user (cash): ${sum(budget.values())/DOEL_ONBOARDED:.2f}")
    return conv


def kosten_per_onboarding(cpm, ctr, conv):
    cpc = cpm / (1000 * ctr)
    return cpc, cpc / conv


def plan_b(conv):
    print("\nPLAN B")
    cpm = 20.70   # Meta Health & Wellness 2025, influee.co (Triple Whale data)
    for ctr in (0.010, 0.0270):  # 2,70% = benchmark influee; 1,0% = conservatief (ASSUMPTION)
        cpc, cpo = kosten_per_onboarding(cpm, ctr, conv)
        print(f"  Meta CPM ${cpm} CTR {ctr:.1%}: CPC ${cpc:.2f}, kost per onboarding ${cpo:.2f}")
    # Google Search: CPC $5,26 gemiddeld alle branches (secundair), zoekintentie -> ASSUMPTION hogere conversie
    for conv_s in (conv, conv * 1.5):
        print(f"  Google CPC $5.26, conv {conv_s:.1%}: kost per onboarding ${5.26/conv_s:.2f}")
    # Creators: micro Reel $800-2.500 (Later 2026). ASSUMPTION: 20-60 onboardings per Reel
    print(f"  Creator Reel $1,500 / 20-60 onboardings: ${1500/60:.0f}-${1500/20:.0f}")

    # Getrapt plan met stijgende kosten (verzadiging). Startkost en stijging = ASSUMPTION, te meten.
    trappen = [("Stage 1: find the price, 4 channels", 10000, 20.0),
               ("Stage 2: 3x spend on best 2", 15000, 26.0),
               ("Stage 3: 3x again on best 1, find the break", 20000, 34.0)]
    reserve = 5000
    tot_users = 0
    print("  Trappen (kost per onboarding stijgt ~30% per stap, ASSUMPTION):")
    for naam, geld, cpo in trappen:
        n = geld / cpo
        tot_users += n
        print(f"    {naam}: ${geld:,} / ${cpo:.0f} = {n:,.0f} onboarded")
    print(f"    Reserve measurement + creative: ${reserve:,}")
    print(f"  totaal onboarded: {tot_users:,.0f}; blended ${45000/tot_users:.2f} per onboarding")
    for d7 in (0.40, 0.60):
        print(f"  dag-7 actief bij {d7:.0%}: {tot_users*d7:,.0f}")
    # Betalers: prijs GBP 100/jaar (brief). Free->paid onbekend: scenario 5/10/20% (ASSUMPTION)
    for p in (0.05, 0.10, 0.20):
        print(f"  betalers bij {p:.0%} van onboarded: {tot_users*p:,.0f}  (omzet jaar 1 ~GBP {tot_users*p*100:,.0f})")


def break_even():
    # GBP 100/jaar (brief). Apple Small Business Program: 15% commissie (developer.apple.com/app-store/small-business-program/)
    netto = 100 * 0.85
    print("\nBREAK-EVEN (jaar-1 netto omzet per betaler GBP %.0f, payback 12 maanden)" % netto)
    for p in (0.10, 0.20, 0.30):
        print(f"  free->paid {p:.0%} van onboarded: max kost per onboarding GBP {netto*p:.2f}")


if __name__ == "__main__":
    plan_b(plan_a())
    break_even()
```

### plan_b_model.py
```python
"""Plan B ($50k): getrapte test. Aannames gelabeld; benchmarks met bron in onderzoek-paid.md, induik-2/3."""
FX = 1.32  # currency-converter.org.uk, 4 okt 2026
STAGES = [  # naam, budget, kost per onboarding (ASSUMPTION: start uit Meta CPM $20.70 / CTR 1-2.7% / 1 op 10, +~30% per stap)
    ("S1 calibrate, 4 channels", 12000, 18.0),
    ("S2 3x daily spend, best 2", 15000, 23.0),
    ("S3 10x plan-A run-rate, best 1", 18000, 30.0),
]
RESERVE = 5000  # holdout/geo test + creative refresh
tot = 0
for n, b, c in STAGES:
    u = b / c; tot += u
    print(f"{n}: ${b:,} / ${c:.0f} = {u:,.0f} onboarded")
print(f"Total {tot:,.0f} onboarded, blended ${45000/tot:.2f}; reserve ${RESERVE:,}")
for d7 in (0.45, 0.60):  # 45% = ASSUMPTION paid colder than plan A; replaced by cohort-2 D7 from plan A
    print(f"  D7 {d7:.0%}: {tot*d7:,.0f} active, ${45000/(tot*d7):.0f} per D7-active")
for price in (100, 70):  # list price (brief) vs founding price (Bjorn 16:25)
    net = price * 0.85 * FX
    for c in (0.029, 0.062, 0.107):  # RevenueCat 2026: H&F median, H&F top quartile, hard paywall
        print(f"  price £{price}, paid {c:.1%}: {tot*c:,.0f} payers, value per onboarding ${net*c:.2f}")
print("Break-even conversion at blended cost:", f"{(45000/tot)/(100*0.85*FX):.1%} (list) / {(45000/tot)/(70*0.85*FX):.1%} (founding)")
```

### plan_b_model.py output
```
S1 calibrate, 4 channels: $12,000 / $18 = 667 onboarded
S2 3x daily spend, best 2: $15,000 / $23 = 652 onboarded
S3 10x plan-A run-rate, best 1: $18,000 / $30 = 600 onboarded
Total 1,919 onboarded, blended $23.45; reserve $5,000
  D7 45%: 863 active, $52 per D7-active
  D7 60%: 1,151 active, $39 per D7-active
  price £100, paid 2.9%: 56 payers, value per onboarding $3.25
  price £100, paid 6.2%: 119 payers, value per onboarding $6.96
  price £100, paid 10.7%: 205 payers, value per onboarding $12.01
  price £70, paid 2.9%: 56 payers, value per onboarding $2.28
  price £70, paid 6.2%: 119 payers, value per onboarding $4.87
  price £70, paid 10.7%: 205 payers, value per onboarding $8.40
Break-even conversion at blended cost: 20.9% (list) / 29.9% (founding)
```

