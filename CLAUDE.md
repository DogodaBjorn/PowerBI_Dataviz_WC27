# PowerBI_Dataviz_WC27 — project context (read first)

This repository is a **pbi-atelier project** (not the template): `project/project.yaml`
exists, the lifecycle is at stage 0, and all work serves the Power BI Dataviz World
Champs 2027 Round 1 entry for **Goodnight Inn**. Deadline **November 18, 2026**;
plan to submit November 17.

- Stage-0 source of truth: `project/MISSION-goodnight-inn.md` (kickoff prompt at the
  bottom). Dataset mechanics and the four-brand comparison: `project/SCOUT-pillowkey-round1.md`.
  Three creative directions with scores: `project/PITCH-goodnight-inn-directions.md`
  and the browsable version `project/deliverables/pitch/goodnight-inn-three-ways.html`.
  Pre-filled stage-5 contract draft: `project/creative-direction.draft.yaml`.
- Contest rules as blocker-severity: one brand, exactly two visible pages, ≥ 4 core
  visuals, ≤ $60 M, ≥ 3 initiatives with ≥ 1 growth, impact through 2032, provided
  data only, accessibility scored, **must render under Publish-to-Web** (built-in
  fonts only, embedded images only).
- Every number in the mission and pitch is a hypothesis from an offline decode of the
  starter `.pbix` (`project/analysis/`, reproducible); re-derive in the model before
  it lands in a visual.
- Contest data lives in `project/data/` (gitignored): the starter `.pbix` and the
  blog page. The dataset itself loads from the organisers' public blob via the
  model's `DataFile` parameter.
- Vendored third-party skills sit beside the atelier's own in `.claude/skills/`;
  see `.claude/skills/VENDORED.md` and `CREDITS.md`.

---

# pbi-atelier — operating contract

You are working in **pbi-atelier**, an agent-driven studio for building premium
Power BI reports through a gated lifecycle. This file is a router: deep knowledge
lives in skills, rules, and `design/` — load it when a stage needs it, not before.

## What this repository is

- A **template** (no `project/project.yaml` filled in yet): you may improve the
  framework itself. Run `/project-init` to start a project.
- A **project** (`project/project.yaml` exists): all work serves that project.
  Framework files (`.claude/`, `lifecycle/`, `contracts/`, `design/`, `scripts/`)
  are read-only reference; changes to them belong in the template repo.

## The lifecycle

State lives in `project/project-state/status.yaml` (schema:
`lifecycle/status.schema.yaml`; definitions: `lifecycle/lifecycle.md`).
The daily driver is `/next` — it reads the state, reports gate status, and routes.

| # | Stage | Skill | Primary agent |
|---|---|---|---|
| 0 | Intake | `/s0-intake` | requirements-analyst |
| 1 | Requirements | `/s1-requirements` | requirements-analyst |
| 2 | Metric architecture | `/s2-metrics` | definition-steward |
| 3 | Model design | `/s3-model-design` | model-auditor |
| 4 | Model build | `/s4-model-build` | pbir-operator |
| 5 | Creative direction & design contract | `/s5-design` | report-designer |
| 6 | Report build | `/s6-report-build` | pbir-operator |
| 7 | Validation & delivery | `/s7-deliver` | qa-reviewer |

## Eleven invariants

1. **The durable truth is the repository, not the chat.** Every decision lands in
   `project/project-state/active/`; update `status.yaml` at every gate; never
   advance a stage silently.
2. **Research first.** Never trust memory for TMDL/PBIR schema fields, enum values,
   or theme properties — verify against the file's `$schema` URL or Microsoft Learn
   before writing.
3. **Declare grain first.** No fact table, measure, or relationship before its grain
   is written in the model blueprint.
4. **One metric, one contract.** Every KPI has a filled `contracts/metric.contract.yaml`
   before implementation. Same-name metrics may still be different metrics.
5. **Do not fabricate.** Metrics not derivable from the sources go on the
   "not available" list; scenario logic (targets, composite scores) is labeled as such.
6. **Only `pbir-operator` mutates `project/pbip/`**, in small single-concern diffs,
   validating after every change.
7. **Design is contracted.** Stage 6 builds exactly what the stage-5 design contract
   specifies; deviations go back through the contract, not into the report.
8. **3-second clarity, 3-minute trust.** Every page states one message at a glance
   and withstands scrutiny on drill-down. Never default Power BI styling.
9. **No machine-specific paths, no client-identifiable content** in anything that
   could leave the project repo. Data sources are parameterized.
10. **Guidance persuades, enforcement decides.** Skills and rules shape reasoning;
    hooks, validators, and `settings.json` scopes are the hard floor. Never work
    around a failing hook — fix the cause.
11. **Credit where it is due — no negotiations.** Every adopted idea carries a
    named credit in the implementing file and in `CREDITS.md`; removing an
    attribution is a blocker-severity defect (rule: `attribution.md`).

## Routing beyond the lifecycle

| Need | Go to |
|---|---|
| TMDL / DAX / PBIR conventions | skills `tmdl-patterns`, `dax-patterns`, `pbir-authoring` |
| Visual choice, page layout, polish | `design/` docs + skills `design-critique`, `dataviz-polish`, `chart-grounding` (canon judgment layer for chart choice, scales and chart words) |
| Is this report best in class? (audit, contest prep, KPI anatomy, what the canon says) | skill `dataviz-canon` (dashboard-level canon with DC-ids + the 20-dimension audit) |
| Brand kit → theme | skill `theme-from-brand-kit` (kits in `design/brand-kits/`) |
| Driving the `pbir` CLI / MS plugin | adapter skills `pbir-cli`, `ms-authoring` |
| Full validation sweep | skill `validate-project` |
| Build documentation | skill `build-log` |
| Add-on modules (brand kit, custom visuals, NL, icons, nav, Deneb, tables, tooltips, canvas, a11y, imagery, pixel comps) | `modules/README.md`; module skills are prefixed `bk-`, `cv-`, `nl-`, `ic-`, `nv-`, `dn-`, `tb-`, `tt-`, `ca-`, `ax-`, `im-`, `px-` |
| P2 focus swap (package selector, bookmark states, Deneb/HTML route gates) | skill `fx-focus` + `project/project-state/active/02-focuswissel-methode.md` |
| Screenshot review v2 op de opzet (fixgids met acceptatiechecks, volgorde tot 18 nov) | `project/project-state/active/07-fixgids-review-v2.md` + `research/log/2026-11-07-screenshot-review-v2.md` |
| Verbeterplan ronde 3 (Bjorns feedback 7 nov: C-framing, scatter-tooltips, nullijn, canvasruimte, merkherkenning + open punten ronde 2) | `project/project-state/active/08-verbeterplan-ronde-3.md` |
| Rebuild-pakket 9 nov: deel A inhoud (KPI-onderzoek, R1-R5) + deel B design (merkkit goodnight-inn-wakeup 3.1, night header, D1-D7), gezamenlijke bouwvolgorde | `project/project-state/active/09-research-based-rebuild.md` + `project/project-state/active/10-design-rebuild.md` |
| Rebuild 09+10 gebouwd op v3 (afstemming plannen tegen main vs. v3-build, besluiten 9 nov: night-glow-waiver, 12 pt, R1 als zin in F1, toegankelijkheidscontrole en a11y_check.py) | `project/project-state/active/11-rebuild-v3-reconciliation.md` |
| FinalV1 → FinalV2 (12 nov): review doc 14, bouwplan doc 15 (M1-M5, S1-S6, N1-N6), bouwlog doc 16 (wat gebouwd, afwijkingen, restpunten van verificatie 17 gedaan: watervalnamen, echte klikrenders), verificatie doc 17 (controle-agent, P2W-poort open) | `project/project-state/active/14-review-finalv2-2026-11-12.md`, `15-bouwplan-finalv2-2026-11-12.md`, `16-finalv2-bouwlog-2026-11-12.md`, `17-verificatie-finalv2-2026-11-12.md`; renders `project/deliverables/screenshots/ScreenshotsFinalV2/` |
| Hover-cues opnieuw (12 nov, nacht: Bjorn vond hint, Definitions en 'Revisit the facts' off brand, onopvallend en allemaal in de kophoek): hover-tags met eigen woorden op elk hoverdoel, Definitions-chip rechts in de voetregel, op P2 'Revisit the facts' als één pil met F1-F4 ernaast (ronde 2; de zet-chips in de tegel waren te druk) | `project/project-state/active/18-hover-cues-2026-11-12.md`; preview `project/deliverables/screenshots/Preview-hover-cues-2026-11-12/` |
| Rolreviews 13 nov (jury, UI/UX, investeerder, nieuwkomer, dataviz/storytelling) en het goedgekeurde eisenpakket voor de storytelling-rebuild (D1-D6 akkoord Bjorn; R-G/R-P1/R-P2/R-W/R-B/R-TT/R-X, tiers T1-T3, cut line 15 nov) | `project/project-state/active/19-*.md`, `20-requirements-storytelling-2026-11-13.md`; feiten `project/analysis/50_storytelling_checks.py` |
| Power BI build guideline 13 nov: constructie-audit (PB-01..07), patronen P-1..8, bouwbladen met slots per pagina en state, modelwerklijst, artifact-brief, bouwvolgorde met spikes S-1..8; N-1..N-5 akkoord Bjorn 13 nov (native selector, 2.8 blijft, What waits als tabel, tt-f1..f4 weg, kapitaalplan-indeling), doc 20 daarop geamendeerd | `project/project-state/active/21-powerbi-build-guideline-2026-11-13.md` |
| Rebuild comp v10 (13 nov, akkoord Bjorn): de vaste comp van P1 en P2 in drie states, slotkaart v10 en bouwspec (kolombreedtes, assen, labelposities, exacte tekst per view en scenario), plus de regels tegen overloop en botsende labels; afwijkingen van doc 21 per slot en per constructie | `project/project-state/active/22-rebuild-comp-v10-handoff-2026-11-13.md`; `project/design-prototypes/rebuild-comp-v10.html`, `opzet-layout-v10.json`, `rebuild-v10-spec.json` |
| Bouwplan FinalV3 (13 nov): de rebuild in twaalf korte sessies achter elkaar, per stap scope, Bjorns deel, klaar-als-check en een log; voortgangstabel en regels voor elke stap. De prompts staan als tekstbestanden klaar: `step-01.txt` t/m `step-12.txt`, `next.txt` (eerstvolgende stap), `resume.txt` | `project/project-state/active/23-build-workplan-finalv3-2026-11-13.md`; `project/build-steps/` |
| Dataviz/storytelling review v2 (14 nov) op FinalV3 zoals gepubliceerd (score ≈ 8.8 jury, 8.4 investeerder; fixlijst DS2-01..12, één ronde copy/kleur, één publicatie) | `project/project-state/active/24-review-dataviz-storytelling-v2-2026-11-14.md` |
| Reviewronde 3 (15 nov) op publicatie 6: vijf V3-reviews, de laatste copyronde (zeven regels, wat bewust is gelaten) en publicatie 7 met poort; pakket voor de laatste controle door Bjorns eigen agent | `project/project-state/active/26-*.md`, `27-round3-copy-round-publish7-2026-11-15.md`; `project/deliverables/final-check-publish7/README.md` |
| Fixronde doc 29 (15 nov, na publicatie 7): twee visuele fixes op branch `fix/publish7-visual-fixes`, niet gemerged en niet gepubliceerd: tien balken zonder schuifbalk in "Your plan" (tegel 64 px hoger, slotmap), hover-tag rechts van "The 2028 gate"; bewijs en renders op 100 % en 64 % | `project/project-state/active/30-fix-round-doc29-two-visual-fixes-2026-11-15.md`; `project/deliverables/fix-publish7-visual-fixes/README.md`; `project/tools/desktop_shots/fix29/` |
| Slotronde 16 nov: naam "Goodnight Inn - Room to Invest", minder tekst (28 formuleringen, elk voor en na), koprijen 12 px hoger, eerste kaartrij op y 148, overal 24 px tussen de rijen; branch `final/room-to-invest`, in `rebuild-finalv3`, niet gepubliceerd | `project/project-state/active/31-final-round-room-to-invest-2026-11-16.md`; `project/deliverables/final-room-to-invest/README.md`; `project/tools/desktop_shots/fix29/` (shoot.py ook voor pagina 1, gaps.py) |
| Laatste edit 16 nov: het rapport is vanaf Bjorns Desktop-save van 11:32 met de hand afgemaakt (`project/pbip/GoodnightInn-final.Report` is wat wordt ingezonden, de generator schrijft het niet meer); kaart IV per locatietype (kleur en teken), balk kaart III Burnt Tangerine; edits alleen via `project/tools/final_edit/`; niet gepubliceerd | `project/project-state/active/32-last-edit-card-IV-by-location-type-2026-11-16.md`; `project/deliverables/final-room-to-invest/last-edit/` |
| Hover en uitlijning 16 nov middag: op Bjorns Desktop-save van 13:18 (kop hoger, eyebrow rechtsboven, Back in de voetregel, Highway donkerder); twee onzichtbare afdekkers over de balkkolommen van `tbl_hero` (anders toont de tabel de SVG-bron als tooltip), kaart IV eindigt gelijk met de onderste kaart van pagina 2, Back weer klikbaar; edit `project/tools/final_edit/f5_hover_align.py`; niet gepubliceerd | `project/project-state/active/33-hover-text-and-bottom-card-2026-11-16.md`; `project/deliverables/final-room-to-invest/hover-align/` |
| Kaschart per scenario 16 nov middag: in de cumulatieve kasgrafiek van pagina 2 heeft elk scenario zijn eigen kleur (Low Burnt Tangerine gestreept, Expected Coffee Blue, High Night gestippeld), het gekozen scenario is de dikke lijn, de nullijn is Night met een lichte tint eronder; drie nieuwe measures `A Cumulative In View (...)` (340); edit `project/tools/final_edit/f6_plan_cases.py`, generators gelijk; niet gepubliceerd | `project/project-state/active/34-plan-chart-by-case-2026-11-16.md`; `project/deliverables/final-room-to-invest/plan-chart/` |
| Gallerypost 16 nov avond: eisen van het inzendformulier (wat zeker is en wat niet), drie covers voor de gallerytegel (a: 456 pakketten, aanbevolen; b: de twee pagina's; c: één kamernacht) uit `project/tools/gallery/cover.py`, en de teksten voor de post (titel, teaser, beschrijving, alt-tekst); rapport en model ongewijzigd | `project/project-state/active/35-gallery-post-cover-and-description-2026-11-16.md`; `project/deliverables/final-room-to-invest/gallery/` |
| Pakket A in één oogopslag 16 nov laat: de drie rijen van pakket A op een lichtblauw vlak, de aanbevelingskaart met een Coffee Blue-rand, één kleur per besluit (A blauw, stap 2 Night, stap 3 leigrijs, ook in de tabel), en overal Step in plaats van Tranche; 341 measures; edit `project/tools/final_edit/f7_package_a.py`, open venster bijgewerkt met `f7_push_model.ps1`; niet gepubliceerd | `project/project-state/active/36-package-a-at-a-glance-2026-11-16.md`; `project/deliverables/final-room-to-invest/package-a/` |
| Vlakken voor stap 2 en 3, 16 nov nacht: de rijen van stap 2 en stap 3 in de tabel op een licht vlak in hun eigen kleur, dezelfde drie vlakken achter de labels boven de planbalk (`plan_tint_1..3`), NPV-balk van een stap in de stapkleur; op Bjorns save van 21:48 (o.a. oranje punt in de eyebrows, regel '44 of 50 hotels' weg); edit `project/tools/final_edit/f8_step_tints.py`; a11y: 4 meldingen, alle vier de oranje punt; niet gepubliceerd | `project/project-state/active/37-step-grounds-table-and-plan-bar-2026-11-16.md`; `project/deliverables/final-room-to-invest/step-tints/` |
| Stap 3 in klei, 16 nov nacht: Bjorn koos klei (#BC6F4A, Burnt Tangerine op 75 %) als derde accent voor stap 3 in planbalk en tabel; de vlakken boven de planbalk van doc 37 zijn weg, de drie plannen blijven gemarkeerd in de tabel (A lichtblauw, stap 2 licht Night, stap 3 licht klei); edit `project/tools/final_edit/f9_step3_clay.py`; niet gepubliceerd | `project/project-state/active/38-step-3-in-clay-2026-11-16.md`; `project/deliverables/final-room-to-invest/step3-accent/` |
| Tabeltekst in het midden van de rij, 16 nov nacht: een native tabel kent geen verticale uitlijning; rijpadding 5 px zet tekst en balk in het midden van een rij van 33 px, de balkafbeeldingen zijn 23 px en de twee referentielijnen lopen daardoor gestreept (per rij een streep, in de afbeelding zelf); een doorlopende lijn als vorm over de tabel is geprobeerd en verworpen; edit `project/tools/final_edit/f10_rows_centred.py`; niet gepubliceerd | `project/project-state/active/39-hero-table-rows-centred-2026-11-16.md`; `project/deliverables/final-room-to-invest/rows-centred/` |
| Keep the toolkit first-in-class (research any subject) | skill `scout` + `research/radar.md` |

## Environment notes

- Windows-first: hooks run under Git Bash; scripts are stdlib-only Python ≥ 3.11.
- External tools are pinned in `DEPENDENCIES.md`. The `pbir` CLI has a
  **non-commercial license** — see that file before paid use; direct JSON editing
  is the documented fallback.

