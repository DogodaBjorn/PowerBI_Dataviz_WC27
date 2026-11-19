---
name: brief-lezer
description: Leest een case-brief (PDF, tekst, xlsx-template) en geeft Bjorn in één scherm de opdracht, de inleverstukken, de harde regels, de verborgen hints, een tijdplan en de valkuilen. Gebruik bij "lees de brief", een nieuwe ronde, een nieuw brief-bestand of een gedeelde brieftekst.
---

# Brief-lezer: de brief in één scherm

Doel: binnen 5 minuten weet Bjorn wat er ingeleverd moet worden, waaraan het moet voldoen en waar de punten liggen. Geen samenvatting van alles, wel een werkkaart.

## Werkwijze
1. Lees de hele brief, inclusief bijlagen, voetnoten en het inlevertemplate (xlsx/docx). Een PDF zonder tekstlaag: open via de Read-tool per pagina of vraag om een tekstversie. Lees elke pagina; hints staan vaak in bijlagen.
2. Schrijf de werkkaart naar `rondes/<ronde>/brief-kaart.md` en de regels naar `rondes/<ronde>/regels.md` (die gebruikt `inlever-check` later).
3. Geef in de chat alleen de werkkaart (Nederlands; citaten uit de brief in het Engels, letterlijk).

## Werkkaart (vaste opbouw, max ~60 regels)

**1. De opdracht in 2 zinnen.** Merk, markt, doelgroep, periode, doel-KPI met getal (bv. "150.000 eerste ritten tegen max $4,00 CPA eerste rit").

**2. Wat je inlevert.** Tabel: onderdeel · aantal · verplichte velden · toegestane waarden (letterlijk uit het template) · max lengte. Noem het formulier/template expliciet.

**3. Harde regels (gates).** Alles wat een inzending ongeldig maakt: merkregels, verboden woorden, verplichte elementen, formaten, cultuur- en castingregels, AI-labeling. Elke regel met paginaverwijzing.

**4. Hoe de jury scoort.** Letterlijke beoordelingscriteria en impliciete signalen ("counts only if", "we will check", "must", "at least"). Zet per criterium wat het bewijs moet zijn.

**5. De data.** Welke bestanden, welke kolommen, welke KPI's moet je zelf berekenen, wat is benchmark. Vermeld meteen verdachte waarden.

**6. Verborgen hints.** Zinnen in persona's, marktcontext of bijlagen die nog niemand gebruikt maar een hypothese sterker maken (in ronde 1: "most rides are shared", "market is oversupplied", "peer trust"). Minimaal 5.

**7. Valkuilen.** Waar een snelle lezer of een AI de fout in gaat: misleidende metrics, verwarrende definities ("choose vehicle type" telt wel, "choose mode of transport" niet), formaatbeperkingen, data die niet klopt.

**8. Tijdplan.** Verdeel de beschikbare tijd over de inleverstukken (zie `ronde-start` voor het 60- en 120-minutenschema). Markeer het eerste moment waarop iets ingevuld moet zijn.

**9. Eerste drie acties.** Concreet, met de skill die erbij hoort.

## Tips om mee te geven
- Lees het inlevertemplate vóór de data. Het template bepaalt je antwoordvorm.
- Elke regel uit "Harde regels" komt later terug in het veld "Must not appear" of in de inlever-check.
- Brief-cijfers die je zelf afleidt (bv. doel-CPA = budget ÷ doelvolume) altijd met de rekensom tonen.
- Bij updates tijdens de ronde: `case-update`.

## Kennis
- Platformverschillen: `knowledge/platforms/comparison.md`
- KPI-definities: `knowledge/kpis/kpi-glossary.md`
- Lessen vorige rondes: `lessons/`
