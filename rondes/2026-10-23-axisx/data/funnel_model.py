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


if __name__ == "__main__":
    plan_b(plan_a())
