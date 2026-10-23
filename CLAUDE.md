# PerformanceOps: AI Marketing, Performance & Analytics

Werkplaats en kennisbank van Bjorn voor performance marketing, analytics en AI in marketing. Eerste gebruik: AI Marketing Kombat Season 1 (track Performance & Analytics). Ook bruikbaar voor klantwerk.

## Taal en vorm
- Antwoord altijd in het Nederlands. Inleverstukken (tabellen, briefs, pitch) in het Engels, tenzij Bjorn anders vraagt.
- Snelheid gaat voor perfectie: eerst het antwoord, dan de onderbouwing.
- Schrijf lange stukken in delen naar een bestand, niet in één chatantwoord. In ronde 1 brak een lang antwoord halverwege af en kostte dat minuten.
- Geen em-dashes in inleverstukken; gewone komma's en punten.

## Waar alles staat
- `knowledge/platforms/`: per platform wat het kan, do's, don'ts, methode van succes, specs. `comparison.md` = de vergelijking tussen platformen.
- `knowledge/kpis/`: KPI-definities, KPI-bomen, optimalisatie per KPI, scale/stop-regels.
- `knowledge/measurement/`: attributie, incrementaliteit, MMM, tracking, testopzet, analyserecepten.
- `knowledge/creative/`: creatieprincipes en de velden van een uitvoerbare AI-creatorbrief.
- `knowledge/luxury/`: luxe-marketing en de Fabergé-primer (finale).
- `knowledge/ai-marketing/`: AI-toepassingen per funnelfase, AI-labels en risico's.
- `lessons/`: wat we leerden per ronde. Lees `lessons/ronde-1-indrive.md` voor elke nieuwe ronde.
- `rondes/<ronde>/`: werkmap per ronde (brief, data, concepten, inlevering, `ai-fouten.md`).
- `scripts/`: rekenhulpen zonder externe packages (alleen Python-standaardbibliotheek).

## Skills (in `.claude/skills/`)
Volgorde in een ronde: `ronde-start` → `brief-lezer` → (`panel-review`) → `data-doorrekenen` → (`panel-review`) → `kpi-optimalisatie` / `kanaalkeuze-budget` / `budget-prognose` → `hypotheses-en-tests` → `creative-brief-ai` → `panel-review` → `case-update` (telkens als er een update komt) → `inlever-check` → `ai-fouten-log`.
Overig: `concurrentie-onderzoek` (Loudbox, Meta Ad Library), `persona-bouwer`, `advertentieteksten`, `landingspagina-audit`, `meetplan`, `jury-pitch`, `ai-oplossing-pitch` (AI-voorstel voor een merk, bv. Fabergé), `luxe-merkpoort` (toets bij luxe merken), `web2wave-hackathon` (volledige Web2Wave-hackathonflow: doelgroepen, creative-onderzoek, generatie, quizfunnel met paywall; Engelstalig, van github.com/web2wave/skills; vereist de Web2Wave-MCP).
Panel: `knowledge/panel/panel.md` (standaard Seufert, Kaushik, Ritson, Sharp, Sanchez; reserves Binet, Sutherland, Holiday). Simulatie op publiek werk: geen verzonnen citaten, geen namen in de inlevering.

## Harde werkregels
- Reken altijd zelf na vanuit ruwe aantallen (spend, impressies, klikken, installs, conversies). Vertrouw geen aangeleverde ratio's.
- Beoordeel op de business-KPI van de brief (bv. CPA eerste rit), nooit op CTR, CPI of IPM alleen.
- Onmogelijke data (meer conversies dan installs, ratio's boven 100%) is geen bewijs: uitsluiten en benoemen.
- Beschrijf beeld alleen na het zelf te hebben bekeken (keyframe, preview). In ronde 1 beschreven twee AI's een keyframe verkeerd.
- De brief is wet: formaat, toegestane waarden, verboden woorden, merkregels. Leg de regels vast in `rondes/<ronde>/regels.md` en toets elke inlevering daartegen.
- Houd per ronde `ai-fouten.md` bij: elke AI-fout die we vangen, met wat het had moeten zijn. Nodig voor "how you worked".
- Gebruik de MCP's waar ze data bieden (`loudbox-demo`, Meta Ad Library via `claude_ai_Meta_Ad`, GA4 via `analytics-mcp`) en zeg welke tool welke bevinding gaf.
- Niets publiceren, insturen of live zetten zonder expliciet ja van Bjorn.
