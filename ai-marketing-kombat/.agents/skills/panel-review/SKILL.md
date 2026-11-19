---
name: panel-review
description: Laat een gesimuleerd panel van gerenommeerde marketingexperts (standaard Seufert, Kaushik, Ritson, Sharp, Sanchez) de brief-analyse, data-analyse of het plan ter discussie stellen, met een echte discussie en een moderator die het tot concrete aanscherpingen terugbrengt. Gebruik bij "panel", "tweede mening", "laat het panel kijken", "stress test", "review het plan", na brief, analyse of plan.
---

# Panel-review: het plan onder vuur, daarna scherper

Het panel is een **simulatie** op basis van het publieke werk van echte experts (profielen in `knowledge/panel/`). Het zijn hun denkrichtingen, niet hun woorden. Geen verzonnen citaten; een letterlijk citaat alleen uit het profiel met bron.

## Wanneer
Drie vaste momenten in een ronde. Per moment een andere vraag aan het panel:
| Moment | Input | Vraag aan het panel |
|---|---|---|
| Na `brief-lezer` | `brief-kaart.md`, `regels.md` | Lezen we de opdracht goed? Wat missen we, wat is de echte vraag achter de vraag? |
| Na `data-doorrekenen` | inzichten + `-kpis.csv` | Kloppen de conclusies, wat is ruis, welke alternatieve verklaring? |
| Na `hypotheses-en-tests` / creative brief | `inlevering.md` | Zou dit winnen? Wat valt om bij de jury? |

## Samenstelling
Standaard (`knowledge/panel/panel.md`):
1. **Eric Seufert**: app-groei, meten na ATT, platformmechaniek.
2. **Avinash Kaushik**: analytics, incrementaliteit, "so what".
3. **Mark Ritson**: diagnose, strategie, tactiek; brand én performance; bot.
4. **Byron Sharp**: bereik onder alle categoriekopers, mentale en fysieke beschikbaarheid, onderscheidende merkkenmerken.
5. **Savannah Sanchez**: performance-creative, hooks, UGC.
Reserves: Les Binet, Rory Sutherland, Taylor Holiday. Wisselen: "panel met Holiday in plaats van Seufert". Voor luxe/Fabergé: Binet en Sutherland altijd erin.

## Modi
- **Snel (standaard tijdens een ronde, ~3 minuten)**: één pass, alle leden in één antwoord. Lees eerst alle vijf profielen.
- **Diep (buiten de ronde of bij een groot besluit)**: elk lid als aparte subagent met alleen zijn eigen profiel en de input, zodat ze elkaar niet napraten; daarna de discussie en synthese hier. Kost ongeveer 5× zoveel tokens; vraag Bjorn eerst.
- **Extern**: schrijf `rondes/<ronde>/panel-prompt.md` met de input en de vijf lenzen, om in ChatGPT te plakken als echt onafhankelijke tweede mening. De uitkomst komt terug in stap 4.

## Verloop
**Stap 1. Eerste oordeel (per lid, 4-6 regels).**
Elk lid: oordeel in één zin (sterk / twijfel / zwak), de twee grootste problemen, elk met de exacte regel of cel waar het over gaat en een concreet voorstel, plus één vraag die de jury zou kunnen stellen. Blijf in de eigen lens; geen herhaling van wat een ander al zei.

**Stap 2. Discussie (de 2-3 grootste meningsverschillen).**
Kies de punten waar leden het oneens zijn (bv. Ritson: "meer targeting" tegen Sharp: "breed bereik"; Kaushik: "bewijs het eerst" tegen Sanchez: "test gewoon meer creatives"). Per punt 2-4 korte beurten, met argument en tegenargument. Leden mogen van mening veranderen als het argument goed is.

**Stap 3. Moderator-synthese (de moderator is Codex, geen expert).**
| # | Onderdeel | Aanscherping | Wie, waarom | Impact op juryscore | Moeite | Besluit |
|---|---|---|---|---|---|---|
Sorteer op impact ÷ moeite. Besluit = doen / niet doen / Bjorn beslist. Weeg een lid lager als het punt in zijn blinde vlek valt (zie profiel) of tegen een harde regel van de brief ingaat. **De brief gaat altijd voor op het panel.**

**Stap 4. Doorvoeren.**
Na Bjorns keuze: pas de werkbestanden aan, noteer in `rondes/<ronde>/panel-log.md` wat er veranderde en waarom. Zet een aanscherping die een AI-fout blootlegde ook in `ai-fouten.md`.

## Regels
- Kritiek zonder fix telt niet. Elk punt verwijst naar een regel en heeft een voorstel.
- Geen beleefdheid: het panel zoekt wat er mis is. Lof alleen als het iets is dat zeker moet blijven.
- Tijdens een ronde maximaal 5 aanscherpingen doorvoeren; de rest naar `lessons/`.
- Namen van panelleden horen niet in de inlevering. In "How we worked" mag wel: "We stress-tested the plan with a simulated expert panel (AI role-play based on public work of leading practitioners); it changed X."
