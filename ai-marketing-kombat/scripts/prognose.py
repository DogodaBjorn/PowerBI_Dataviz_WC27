"""Haalbaarheid van een doel bij een budget, in drie scenario's. Alleen standaardbibliotheek.

Gebruik:
  python -I scripts/prognose.py --budget 600000 --doel 150000 --cpa 3.82
         [--cpa-zonder-winnaar 5.75] [--cpa-hoog 3.0] [--opslag 0.10]

Laag   = CPA zonder topwinnaar (of 1,5x CPA als onbekend) + 15% schaalopslag
Midden = blended CPA + opslag (default 10%) voor afnemende meeropbrengst
Hoog   = --cpa-hoog als opgegeven, anders blended CPA zonder opslag
De opslagen zijn aannames; noem ze zo in de inlevering.
"""
import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--budget", type=float, required=True)
    ap.add_argument("--doel", type=float, required=True, help="gewenst aantal resultaten")
    ap.add_argument("--cpa", type=float, required=True, help="blended CPA vorige periode")
    ap.add_argument("--cpa-zonder-winnaar", type=float)
    ap.add_argument("--cpa-hoog", type=float)
    ap.add_argument("--opslag", type=float, default=0.10)
    a = ap.parse_args()

    nodig = a.budget / a.doel
    print(f"Benodigde CPA: {a.budget:,.0f} / {a.doel:,.0f} = {nodig:.2f}\n")

    laag_cpa = (a.cpa_zonder_winnaar or a.cpa * 1.5) * 1.15
    scenarios = [
        ("Laag", laag_cpa, "zonder topwinnaar" if a.cpa_zonder_winnaar else "1,5x CPA (geen concentratiedata)", "+15%"),
        ("Midden", a.cpa * (1 + a.opslag), "blended CPA", f"+{a.opslag:.0%}"),
        ("Hoog", a.cpa_hoog or a.cpa, "opgegeven doel-CPA plan" if a.cpa_hoog else "blended CPA", "geen"),
    ]
    print(f"{'Scenario':<8} {'CPA':>7} {'Resultaten':>12} {'% doel':>7} {'Gat':>10}  basis (opslag)")
    for naam, cpa, basis, opslag in scenarios:
        res = a.budget / cpa
        gat = a.doel - res
        print(f"{naam:<8} {cpa:>7.2f} {res:>12,.0f} {res / a.doel:>7.0%} {max(gat, 0):>10,.0f}  {basis} ({opslag})")

    verbetering = 1 - nodig / (a.cpa * (1 + a.opslag))
    if verbetering > 0:
        print(f"\nOm het doel te halen moet de CPA {verbetering:.0%} lager dan het middenscenario.")
    else:
        print(f"\nHet middenscenario haalt het doel met {-verbetering:.0%} CPA-marge.")


if __name__ == "__main__":
    main()
