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
