---
name: kpi-optimalisatie
description: Diagnosticeert een performance-KPI (CPA, ROAS, CAC, CPM, CTR, CVR, CPI, payback, leadkwaliteit, brand lift) via de KPI-boom en geeft de hefbomen per laag en per platform, met wat je niet moet doen en hoe lang je wacht. Gebruik bij "CPA te hoog", "hoe verbeteren we ROAS", "optimaliseer voor", "waarom daalt", of een KPI-doel in een brief.
---

# KPI-optimalisatie: eerst de boom, dan de hefboom

## 1. Leg de doel-KPI vast
- Welke KPI telt voor de business (eerste rit, eerste aankoop, gekwalificeerde lead, boutique-afspraak)? Dat is de noemer van de CPA.
- Doelwaarde met rekensom (bv. budget ÷ doelvolume = max CPA).
- Welke KPI's zijn alleen signalen (CTR, CPI, IPM, hook rate)?

## 2. Ontleed in drivers
CPA = CPM ÷ (1000 × CTR × CVR) en voor apps: CPA = CPI ÷ actieratio.
ROAS = (CTR × CVR × AOV × 1000) ÷ CPM.
Vergelijk elke driver met de benchmark of de vorige periode. De driver met de grootste afwijking is de bindende beperking; daar begin je. Zie `knowledge/kpis/kpi-tree.md` voor het rekenvoorbeeld.

## 3. Hefbomen per laag
| Laag | Raakt vooral | Typische hefboom |
|---|---|---|
| Doelgroep/signaal | CPM, CVR | breed + sterke conversiesignalen (CAPI, Enhanced Conversions), first-party lijsten, uitsluitingen |
| Creative | CTR, hook, CVR | USP in de kop, hook in 0-2 s, productmoment leesbaar, meer concepten (niet meer varianten) |
| Aanbod | CVR, AOV | aanbod dat merkconform is (geen korting als dat merkvreemd is) |
| Landing/onboarding | CVR, actieratio | één taak per pagina, snelheid, frictie in eerste gebruik weg |
| Bieden | CPA, volume | optimaliseer op het diepste event met genoeg volume; tCPA/tROAS pas na stabiel volume |
| Budget/structuur | leerfase, CPM | consolideren, 20-30% stappen, geen dagelijkse wijzigingen |
| Plaatsing/frequentie | CPM, CTR | plaatsing per format, frequency caps bij merk- en luxecampagnes |
| Meting | alles | dedupliceren, incrementaliteit testen voor je schaalt |

Per platform: `knowledge/kpis/optimization-playbooks.md` en `knowledge/platforms/<platform>.md`.

## 4. Lever op
1. Diagnose in 3 regels: welke driver, hoeveel afwijking, waarom waarschijnlijk.
2. Top 3 acties, gesorteerd op verwachte impact ÷ moeite, met de KPI die het moet bewegen.
3. Wat we niet doen (de verleidelijke fout, bv. optimaliseren op CTR).
4. Wanneer we oordelen: minimum events en dagen.
5. Scale/stop-regel (zie `knowledge/kpis/scale-stop-rules.md`).

## Valkuilen
- Optimaliseren op een signaal dat niet correleert met de business-KPI.
- Elke dag ingrijpen: reset de leerfase.
- Kanalen vergelijken op platform-gerapporteerde CPA: attributievensters verschillen. Zie `knowledge/measurement/attribution.md`.
- Bij luxe: niet optimaliseren op goedkope CPM/CPC; zie `luxe-merkpoort`.
