# PerformanceOps

Kennisbank, skills en rekenhulpen voor AI-marketing, performance marketing en analytics. Gebouwd voor AI Marketing Kombat Season 1 en herbruikbaar voor klantwerk.

> **Sinds 19 nov 2026 is dit de map `ai-marketing-kombat/` van de repository `contests`** (`E:\Contests`, alle wedstrijden van Bjorn; zie de `README.md` een niveau hoger). Hij kwam uit de repository `PerformanceOps` (`E:\PerformanceOps`), met zijn geschiedenis. Ronde 1 (de oude repository `indrive-kombat`) staat nu in `rondes/2026-10-21-indrive/`. Deze map is de projectroot: elk pad hieronder is relatief aan deze map.

## Snel starten in een ronde
1. Open een Claude Code-sessie in `E:\Contests\ai-marketing-kombat` (niet in `E:\Contests`: de skills laden alleen vanuit de map waar de sessie start).
2. Zeg "ronde start" en deel de brief. De skill `ronde-start` maakt de werkmap en het tijdschema; `brief-lezer` geeft de werkkaart.
3. Data: `python -I scripts/kpi_calc.py rondes/<ronde>/data/<bestand>.csv --target-cpa <doel> --by Channel,Format`
4. "How we worked" (hoe we AI gebruikten): begin bij [HOW-WE-WORKED.md](HOW-WE-WORKED.md).
5. Voor insturen: `python -I scripts/woordcheck.py rondes/<ronde>/inlevering.md --regels rondes/<ronde>/regels.md` en de skill `inlever-check`.

## Inhoud
| Map | Wat |
|---|---|
| `.claude/skills/` | 20 skills, van brief lezen tot AI-fouten-log, plus `panel-review` (expertpanel) |
| `knowledge/panel/` | Profielen van 8 experts voor het reviewpanel, met bronnen |
| `knowledge/platforms/` | Meta, Google, TikTok, LinkedIn, Pinterest, Snapchat, X/Reddit, retail media, programmatic/CTV, creators, plus vergelijking |
| `knowledge/kpis/` | KPI-woordenlijst, KPI-bomen, optimalisatie per KPI, scale/stop-regels |
| `knowledge/measurement/` | Attributie, incrementaliteit/MMM, tracking/privacy, testopzet, analyserecepten |
| `knowledge/creative/` | Creatieprincipes en velden van een AI-creatorbrief |
| `knowledge/luxury/` | Luxe-marketing en Fabergé-primer |
| `knowledge/ai-marketing/` | AI-toepassingen per funnelfase, AI-labels, risico's |
| `lessons/` | Lessen per ronde |
| `rondes/` | Werkmappen per ronde |
| `scripts/` | `kpi_calc.py`, `woordcheck.py`, `prognose.py` (alleen standaardbibliotheek) |

Items gemarkeerd met [CHECK] in de kennisbank zijn niet geverifieerd of kunnen verouderd zijn.

---
Part of the workspace of Björn Kats (DoGoDa). Map, status of all repos and agent briefings: [DogodaBjorn/workspace](https://github.com/DogodaBjorn/workspace) (private) · public overview: [github.com/DogodaBjorn](https://github.com/DogodaBjorn).
