# Work log: AxisX, AI Marketing Kombat Stage 2

Team: Bjorn (human lead). Models: Claude (Claude Code, main session plus parallel sessions) and ChatGPT (strategy context). Time: 15:07 to 17:07, 23 Oct 2026.
Full session exports are attached: `worklog-sessie-export.md` (main Claude session, prompts, model answers, every tool call) and `worklog-parallel-*.md` (three parallel Claude sessions run by Bjorn: research deep dives, hooks, campaign name).

## 1. How we worked (short)
1. Started from a fixed round routine: work folder, rules file from the brief, AI-errors file, tool check (Meta Ad Library, WebSearch, Loudbox).
2. Sent questions to the organisation first; a simulated expert panel cut 11 draft questions to 9 short, practical ones.
3. Research in parallel: three Claude research agents (audience, paid economics, competitors and AI risk), five deep dives in a parallel session (economic anchor, ceiling, ad policy, quiz-to-day-7 measurement, Ad Library run lengths), and a ChatGPT session for the strategic core.
4. Every number traced to a source or labelled as an assumption; small Python models (`funnel_model.py`, `plan_b_model.py`) so each figure can be recomputed.
5. A simulated panel of marketing experts (AI role-play based on public work of leading practitioners) reviewed the questions, the campaign, plan A and the hooks; it changed the plan five times (see section 4).
6. The human made the strategic calls (section 3); the model proposed, calculated and wrote.

## 2. Prompts (Bjorn's, in order, main session)
- Brief PDF shared; "start the round".
- "Kun je de vijf vragen even langs ons panel laten gaan?" (panel on the questions)
- "En nu samenkomen tot praktische vragen aub?"
- Full brief part 2 pasted.
- "Dit is een heel goede vervolgstap!" (research go)
- "Nee we zijn hier nog lang niet aan toe ... laat Avinash Kaushik mij even helpen dit verder te verduidelijken" (rejected building the deck, asked for plain-language numbers)
- "Active founder D7 = feedback given in the first 7 days; D14 report as second metric. Leg dit vast."
- ChatGPT context extract added: "AI-powered community-led acquisition", Founding 500.
- "Panel review this plan, which metrics define success? Plus: targeted private invites from the founder, advised by AI, to community leads with her own story."
- "Take GDPR fully on board: AI may analyse and advise, then delete data; public role, not profiling."
- Deep dives 2-6 + market research file: "check with the panel whether we have a solid base, present part 1: what do we do with A?"
- Selection note + hook-builder/taste results pasted: "what do we use in text and visuals?"
- "Keep the questions as open as possible; classify with AI; build a test group of people without those signals."
- "Everyone who applies to the Founding Circle gets a lower price at launch."

## 3. Human decisions that shaped the solution
- Strategy core is Bjorn's: AI-powered community-led acquisition (ABM on communities, not on individuals) and private founder invites to community leads.
- GDPR line: AI analyses public conversations at theme level, raw data deleted afterwards, leads chosen on public role, no profiling, founder sends every message herself.
- Steering metrics: Active founder D7 (feedback in week 1) and day-14 doctor report, on top of the brief's KPIs.
- Open questions instead of a tick-box quiz, AI classification of her own words, and a contrast group without the signals.
- Founding price for every applicant as an extra reason to apply.
- Last slide left blank for the founder's own sentence; pitch card written by Bjorn.

## 4. What the model proposed that we rejected or changed, and why
| Model proposed | What we did | Why |
|---|---|---|
| 11 questions to the organisation | 9 short practical questions | Must be answerable directly |
| Build the deck right after the first funnel model | Rejected; first analysis and a real campaign | Numbers were not clear enough yet ("abracadabra") |
| "Selection on fit is how we hit 60% day 7", no caveat | Added a random contrast group | Selection inflates retention; the investor plan would inherit a number that doesn't scale (panel) |
| Recruit women who don't yet recognise perimenopause (ChatGPT) | Removed | The brief rules them out for the first 500 |
| "Is this perimenopause?" as quiz hook (research agent) | Removed | Same reason |
| Lifetime free for all founders and friends (idea in the ChatGPT session) | Kept only as a risk scenario | Price model and cost per user unknown |
| Closed 8-question quiz | Replaced by 4 open questions + AI classification | Matches how the app works; signals in her own words |
| Many hooks (13+) | 4 kept; vague, fear-based and brand-first openers cut | Must land in 3 seconds, work muted, be sayable by a real person |
| Model writing the founder's first line | Left blank on purpose | It must be hers |

## 5. AI errors we caught
| AI said | Should have been | Caught by |
|---|---|---|
| Compared cost per onboarding in dollars with a break-even in pounds | Convert with a sourced FX rate first (1.32) | Plain-language review |
| "1, 2 or 3 in 10 onboarded women will pay" (no source) | Public anchor 2.1-6.2% download-to-paid (RevenueCat 2026); a woman is worth $2-7 in year 1, not $11-34. This turned plan B into an honest test | Deep dive 2 |
| "Selection on fit" as the retention lever without caveat | Contrast group | Simulated panel |
| "Is this perimenopause?" hook | Out of scope per brief | Hook check |
| A shell command hung on an empty `cat` and created a stray empty file | Stopped, file removed | Claude itself |

## 6. Tools and skills used
- Claude Code skills: ronde-start, panel-review (4 rounds), meetplan logic, hooks (viral-hooks, hook-generator in a parallel session), artifact-free PDF build.
- Meta Ad Library (MCP `ads_library_search`): 5,247 active UK ads on "perimenopause", named-woman advertorial pages, anna app as the only direct app advertiser, run-length lower bounds.
- Web2Wave creative trends (MCP): run lengths of Flo and BioID creatives (200-435 days).
- WebSearch / WebFetch via research agents: KFF, Gallup, Clutch, RevenueCat, Adapty, StatCounter, ONS, US Census, Eurostat, Meta and Google policy pages, Apple TestFlight docs.
- Python (standard library): funnel and plan B models.
- ChatGPT: strategic context extract (community-led acquisition, Founding 500).
- Loudbox demo: checked, not used (workspace held other data).

## 7. Files behind the deck
plan-A.md Â· plan-B.md Â· funnel-inhoud.md Â· meetplan.md Â· hooks.md Â· data/ (research tables, models, deep dives) Â· panel-log.md Â· ai-fouten.md Â· afwijzingen.md

## 8. Appendix: models (recompute every number)

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
        print(f"  price Â£{price}, paid {c:.1%}: {tot*c:,.0f} payers, value per onboarding ${net*c:.2f}")
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

## 9. Final iteration (16:43-16:55)
Bjorn rejected the first deck ("this isn't it") and set the structure himself: open the pitch on "What they'll see. What they don't see." (the woman's visible and invisible life; the campaign's visible front and invisible engine), split plan A, plan B and the success metrics into What they'll see / What they don't see / What you'll see per phase (pre-activation, landing, open questions, Founders Circle, other channels), and move all technical detail to an appendix written in plain language. A Claude Design brand pass was considered and dropped for time; the deck was restyled by hand toward a warmer, more trustworthy look (warm paper, plum and terracotta, serif headlines, the member "system card" as the recurring asset). The founder's blank line stayed as the last slide. The first deck version remains in git history.
