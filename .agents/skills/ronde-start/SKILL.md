---
name: ronde-start
description: Zet een Kombat-ronde of andere getimede case klaar (werkmap, tools, tijdschema, checkpoints) en bewaakt de klok. Gebruik bij "we beginnen", "ronde start", "start de timer", of als Bjorn een nieuwe brief deelt met een tijdslimiet.
---

# Ronde-start: klaarzetten en de klok bewaken

## Vóór de start (5 minuten, liefst vóór je op Start drukt)
1. Maak `rondes/<jjjj-mm-dd>-<naam>/` met: `brief/` (originele bestanden), `data/`, `regels.md`, `ai-fouten.md`, `inlevering.md`.
2. Controleer de tools: `loudbox-demo` MCP (`describe_demo_data`), Meta Ad Library (`ads_library_search` via ToolSearch), WebSearch. Werkt iets niet: meld het meteen, niet halverwege.
3. Lees `lessons/` (laatste ronde) en noem de 3 lessen die nu tellen.
4. Noteer starttijd en eindtijd in `inlevering.md` bovenaan. Vraag de klok op met `Get-Date -Format HH:mm`.

## Tijdschema 120 minuten
| Minuut | Doel | Skill |
|---|---|---|
| 0-10 | Brief + template lezen, werkkaart, regels.md | `brief-lezer` |
| 10-30 | Data doorrekenen, sanity checks, 5 kandidaat-inzichten | `data-doorrekenen` |
| 30-40 | Concurrent/trend/reviews (alleen wat een hypothese voedt) | `concurrentie-onderzoek` |
| 40-65 | Hypotheses, ranking, budget, scale/stop | `hypotheses-en-tests`, `kanaalkeuze-budget` |
| 65-85 | Creative brief, standalone | `creative-brief-ai` |
| 85-100 | Inlever-check tegen de brief, fouten herstellen | `inlever-check` |
| 100-110 | How we worked + AI-fouten, overzetten in template | `ai-fouten-log` |
| 110-120 | Buffer. Insturen. Niets nieuws meer beginnen. | |

## Tijdschema 60 minuten
0-5 brief · 5-17 data · 17-35 hypotheses+budget · 35-47 creative brief · 47-55 check · 55-60 insturen.

## Checkpoints (Codex meldt ze zelf)
- Bij elk overgangsmoment: één regel "Checkpoint mm: klaar = …, open = …, volgende = …".
- Loopt een blok meer dan 5 minuten uit: zeg het en stel voor wat er korter kan.
- Vanaf 75% van de tijd: alleen nog afmaken en controleren, geen nieuwe analyses.
- 10 minuten voor eind: alles staat in het inlevertemplate, ook als het niet perfect is.

## Werkregels tijdens de ronde
- Antwoord kort; lange teksten direct naar bestand, in delen.
- Eén werkbestand per onderdeel. Geen v2/v3-bestanden; `git commit` bij elk checkpoint.
- Elke AI-fout die we vangen meteen in `ai-fouten.md`.
- Updates van de organisatie: direct `case-update`, niet opsparen.
