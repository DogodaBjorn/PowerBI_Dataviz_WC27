---
name: data-doorrekenen
description: Rekent campagne- of creativedata (CSV/xlsx) zelf door, doet sanity checks, rangschikt op de business-KPI en levert inzichten in het format Insight · Evidence · So what. Gebruik bij een dataset in een case, "reken door", "wat zegt de data", "beste creatives".
---

# Data doorrekenen: van ruwe aantallen naar inzichten

## Stap 1. Rekenen (script, niet uit het hoofd)
```
python -I scripts/kpi_calc.py rondes/<ronde>/data/<bestand>.csv --kpi first_rides --target-cpa 4.0
```
Het script herkent kolommen als spend, impressions, clicks, installs, conversions (of geef `--map spend=Cost,conv=First rides`). Uitvoer: per rij CPM, CTR, CPC, CVR, CPI, IPM, CPA, actieratio; ranking op CPA; concentratie (aandeel resultaat van de top-1/top-3 en blended CPA met en zonder de winnaar); correlaties tussen bovenstroomse metrics en de business-KPI; vlaggen voor onmogelijke data. Schrijft ook `<bestand>-kpis.csv`.

Geen script mogelijk (xlsx, raar formaat)? Zet het eerst om naar CSV of reken in Python met de standaardbibliotheek. Toon altijd één rekensom volledig uitgeschreven in de evidence.

## Stap 2. Sanity checks vóór je iets rangschikt
- Meer conversies dan installs/klikken, ratio's boven 100%, CPA onder kostprijs van een klik: uitsluiten, benoemen als inzicht ("niet bruikbaar als bewijs").
- Kleine aantallen (< ~30 conversies): richting, geen bewijs. Zeg dat.
- Gedeelde elementen (zelfde keyframe, zelfde eindscherm, zelfde kop): bekijk de creatives zelf via MCP of preview. Beschrijf nooit beeld dat je niet zag.
- Benchmarks uit de brief gaan voor algemene benchmarks.

## Stap 3. Zoek de vijf standaardpatronen
1. **Concentratie**: draagt één winnaar het totaal? Blended KPI met en zonder.
2. **Bovenstrooms ≠ benedenstrooms**: correleert CTR/CPI/IPM met de business-KPI? Vaak niet. Dan wordt dat de scale/stop-regel.
3. **Format/plaatsing vs concept**: zelfde concept in ander format, ander resultaat?
4. **Hook/kop**: winnaars delen een openingsmoment of een USP in de kop?
5. **Gaten**: waar komt het budget van de komende periode terecht, en waar is het minst getest?

Extra splitsingen: kanaal × format × taal × persona × boodschap. Gebruik `knowledge/measurement/analysis-recipes.md`.

## Stap 4. Schrijf de inzichten
Tabel, Engels, 3 tot 5 rijen:

| Insight | Evidence | So what |
|---|---|---|
| Eén zin, een bewering. | Creative-ID's, getallen, één rekensom met formule, vergelijkingsgroep. | Wat we nu anders doen: een regel, test of budgetkeuze. |

Regels: elk inzicht moet een beslissing veranderen; geen "interessant om te weten". Het So what voedt een hypothese of een scale/stop-regel.

## Kennis
`knowledge/kpis/kpi-glossary.md`, `knowledge/kpis/kpi-tree.md`, `knowledge/measurement/analysis-recipes.md`.
