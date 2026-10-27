---
name: budget-prognose
description: Rekent uit wat een budget oplevert (resultaten, CPA, haalbaarheid van het doel), met scenario's en afnemende meeropbrengst, en bewaakt de pacing tijdens een looptijd. Gebruik bij "is het doel haalbaar", "forecast", "prognose", "hoeveel levert dit op", "pacing", "wat als het budget halveert".
---

# Budget-prognose en pacing

## Snelle haalbaarheid
```
python -I scripts/prognose.py --budget 600000 --doel 150000 --cpa 3.82 --cpa-zonder-winnaar 5.75
```
Geeft: benodigde CPA (budget ÷ doel), verwachte resultaten per scenario, het gat tot het doel, en welke CPA-verbetering nodig is.

## Scenario's (altijd drie)
| Scenario | Aanname | Bron |
|---|---|---|
| Laag | CPA van de portefeuille zonder de topwinnaar, +15% voor afnemende meeropbrengst bij opschalen | concentratiecheck uit `data-doorrekenen` |
| Midden | Blended CPA van de vorige periode, +10% schaaleffect | data |
| Hoog | Winnende recepten schalen naar het aandeel uit het plan | hypotheses |
Afnemende meeropbrengst: bij 2-3× meer budget per kanaal stijgt de CPA meestal merkbaar; reken met een opslag en zeg dat het een aanname is. Seizoen (Black Friday, feestdagen) duwt CPM omhoog [CHECK per markt].

## Pacing tijdens de looptijd
- Verwachte uitgaven tot vandaag = budget × verstreken dagen ÷ totale dagen (pas aan voor piekmomenten).
- Pacing-index = werkelijke ÷ verwachte uitgaven; resultaat-index idem voor conversies.
- Uitgaven op schema maar resultaten eronder = CPA-probleem (zie `kpi-optimalisatie`), niet een budgetprobleem.

## Output (Engels)
"To reach X at $B we need CPA ≤ $T. Last period ran at $C (without the top creative $D). Scenarios: low N1, mid N2, high N3. The plan reaches the goal only if [condition]; the test budget is designed to prove [condition] by [date]."
