# BUILD_LOG — World Champs BCN 26 — Round 3

<!-- Maintained DURING stages 4 and 6 by the build-log skill. A reader who
never saw the chat must learn from this file: what exists, what remains
manual, which numbers rest on assumptions, when it was last validated. -->

Last validated: 2026-08-05 — `validate_tmdl.py --strict`: 15 files, **1 error**
(the standing `SourceRoot` drive-letter waiver, see 04-model-build.md), 0
warnings; **267 repo JSON files** well-formed, UTF-8 without BOM, 0 errors;
`report.json` 0 errors against its declared `report/3.3.0` schema.
Model: 10 tables, **89 measures**, 8 relationships, 3 shared expressions
(SourceRoot parameter, Source, Schema). The `06 Display\Alt text` family is
**built** — the attribution blocker was cleared on 2026-08-05 (commit `f4b9420`).
Report: the D7 custom theme is installed and active. **The report is
structurally complete**: `p0-box-office` (42) · `p1-act-i-profit` (44) ·
`p2-act-ii-ratings` (38) · `p3-act-iii-corrected-cut` (37) · `p9-end-credits`
(35) · `tt-movie-poster` tooltip (14) = **210 visuals in six pages**, plus the
**nine beat bookmarks** (`bm_p1_b1..b3`, `bm_p2_b1..b3`, `bm_p3_b1..b3`). The two
starter pages are untouched. Nothing has been rendered in Desktop — see
*Manual steps* and *Known limitations*.

## Built

| Date | Scope | Items |
|---|---|---|
| 2026-08-04 | SemanticModel: sources | `SourceRoot` parameter; `Source`/`Schema` M rewritten to `SourceRoot & "\TMDB_movie_dataset_v11.csv"` |
| 2026-08-04 | SemanticModel: Date | deterministic 1800-01-01..2099-12-31 range; `dataCategory: Time` + `isKey` (mark as date table); `Month Name` sorted by `Month Number` |
| 2026-08-04 | SemanticModel: Movies | new M columns `Release Year Key` (hidden FK, −1 unknown), `Is Future Release` (anchor 2026-07-24); `summarizeBy: none` on Vote Average, Vote Count, Revenue, Budget, Runtime, Popularity; Budget/Revenue format `\$#,0;(\$#,0)` |
| 2026-08-04 | SemanticModel: Release Year | new dimension (Year Key / Year Label / Year Sort / Year Status; "No date on record" member); relationship `Movies_ReleaseYearKey_to_ReleaseYear_YearKey` (*:1, single) |
| 2026-08-04 | SemanticModel: _Measures | `Profit` → `Profit (naive)` (formula byte-identical, trap-marked); 32 new measures across folders 01–06 per blueprint §5 |
| 2026-08-04 | Report: `22a73d6058ce40e505e0` / `e21488a8d900077091bd` | starter table visual rebound from `[Profit]` to `[Profit (naive)]` (projection, sort, filter) — same batch as the rename, nothing dangles |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — stub fills | 8 stage-4 `06 Display` stubs given their contracted expressions: `Color · Trap` · `Color · Honest` · `Color · Neutral` · `Title · Lie 1` · `Title · Lie 2` · `Title · Lie 3` · `Title · Landing` · `Label · Method`. Measure name, `lineageTag`, `formatString` and `displayFolder` untouched; only the expression and the `///` docstring changed. No `"s5 fills value"` literal survives anywhere. |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — support measures | 14 NEW: `Movies (scatter population)` (01 Core); `Financial floor (disclosed)`, `Movies (zero revenue)`, `Zero-revenue share %` (02); `Median votes`, `Votes p75`, `Movies (zero votes)`, `Zero-vote share %`, `Two-vote ten (illustration)`, `Godfather rating (reference)` (03); `Winner · title` (04); `Adult listings excluded`, `Snapshot anchor (disclosed)`, `Movies (sentinel-dated)` (05) |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — 06 Display | 26 NEW: 6 colour/mark measures (`Color · Trap/Honest/Neutral (night)`, `Color · Rating verdict`, `Mark · Rating verdict`, `Color · Scatter mark`), 19 copy/label measures (`Copy · Act I ·` ×8, `Copy · Act II ·` ×3, `Copy · Act III ·` ×2, `Label · Population`, `Label · No date`, `Label · Chip floor/m/C`, `Label · Caveats`) and `Image · Poster URL` |
| 2026-08-05 (s6 phase A) | Report: `StaticResources/RegisteredResources` | `project/deliverables/theme.json` installed byte-identically as `D7-Seductive-Lies.json` (UTF-8, no BOM; sha256 `7fbc8c2ee0a1abaa…`) |
| 2026-08-05 (s6 phase A) | Report: `definition/report.json` | `themeCollection.customTheme.name` repointed to `D7-Seductive-Lies.json`; a matching `{name, path, type: "CustomTheme"}` item added to the `RegisteredResources` package. `baseTheme` (`Fluent2-CY26SU05`), `objects`, `settings` and every existing identifier untouched |
| 2026-08-05 (s6 phase B1) | Report: `pages/p0-box-office` | **42 visuals**, 1280×720, canvas `#171418`. Marquee (`z_marquee_frame` / `_inner` / `_title` / `_sub`) · `hero_takeaway` (live) · three tickets ×11 objects each (`z_ticketN_body` / `_rule` / `_stub_rule` / `_perf` / `_act` / `_hr` / `_title` / `_tease` / `_admit` / `_serial` + `btn_ticket_actN`) · `z_billing_method` + `z_billing_caveats` (live) · `z_footer_credit` · `btn_credits` |
| 2026-08-05 (s6 phase B1) | Report: `pages/p9-end-credits` | **35 visuals**, 1280×720, canvas `#171418`. `z_cr_title` · `c_cr_h_cast` + `c_cr_cast` · `c_cr_h_counts` + 7 label/value row pairs + `c_cr_count_basis_kept` · `c_cr_h_params` + 4 label/value row pairs · `c_cr_h_glossary` + `c_cr_glossary` · `c_cr_h_refusals` + `c_cr_refusals` · `c_cr_close_src` · `c_cr_close_last` · `btn_home`. **14 of the 35 are measure-bound cards** — no count is typed anywhere |
| 2026-08-05 (s6 phase B1) | Report: `pages/pages.json` | `p0-box-office` prepended and made `activePageName` + `landingPageName`; `p9-end-credits` appended. The two starter page ids kept in `pageOrder`, untouched |
| 2026-08-05 (s6 phase B2a) | SemanticModel: `_Measures` | **1 NEW measure** `Movies (no credible financials)` = `[Movies] - [Movies (credible financials)]` (folder `02 Lie 1 · Financials`, format `#,0`, fresh lineageTag). Build-necessitated: the contracted waffle fallback is a **100 % stacked bar**, which needs the complement segment as a field; `[Movies]` and `[Movies (credible financials)]` overlap and would stack to a lie. No new concept — the design already prints this quantity ("no credible financials (87)") |
| 2026-08-05 (s6 phase B2a) | Report: `pages/p1-act-i-profit` | **43 visuals**, 1280×720, paper canvas `#F5F2E9`. Chrome ×13 (`z_p1_header_title` / `_rule` · `btn_home` · `btn_credits` · `z_p1_admit` · `btn_beat_1..3` + `z_p1_beat1..3_mark` · `btn_next_scene` · `z_p1_verdict_rule`) · screenplay ×8 · KPI insert ×7 · script-doctor notes ×6 (3 rules + 3 texts) · ticket-audit insert ×6 · verdict ×3. **9 of the 43 are measure-bound cards**; no count is typed anywhere |
| 2026-08-05 (s6 phase B2a) | Report: `pages/p2-act-ii-ratings` | **37 visuals**, 1280×720, paper canvas `#F5F2E9`. Chrome ×12 + 3 beat marks · screenplay ×8 · notes ×6 · perfect-tens insert ×4 (incl. `tbl_perfect_tens`) · correction insert ×4 (incl. `dn_rating_fall`) · verdict ×2. **3 measure-bound cards** plus two data visuals bound entirely to measures/columns |
| 2026-08-05 (s6 phase B2a) | Report: `pages/pages.json` | `p1-act-i-profit` and `p2-act-ii-ratings` inserted after `p0-box-office`; starter ids and `p9-end-credits` untouched. Validated against `pagesMetadata/1.1.0` (0 errors) |
| 2026-08-05 (s6 phase B2b) | SemanticModel: `_Measures` | **5 NEW** — `Movies (perfect ten)`, `Movies (perfect ten, single vote)`, `Single-vote ten (illustration)` (03 Lie 2 · Ratings); `Copy · Act II · naive read`, `Mark · Rank divergence` (06 Display). **2 EDITED in place** (name, `lineageTag`, `formatString`, `displayFolder` untouched; expression + docstring only): `Copy · Act II · responsible read`, `Copy · Act II · verdict` — both now state the aggregate and name no film. See *the Act II ruling* below |
| 2026-08-05 (s6 phase B2b) | Report: `p0/btn_credits`, `p9/btn_home` | `"lineWeight"` → `"weight"` (the published `actionButton → outline` property). One-line correctness fix, coordinator-ruled. Nothing else in either file changed |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p1-act-i-profit` | rebuilt at **44 visuals** (+`btn_next_scene_2`), **landing state flipped to SC.1** (22 objects `isHidden` on disk), beat buttons wired to `bm_p1_b1..b3` |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p2-act-ii-ratings` | rebuilt at **38 visuals** (+`btn_next_scene_2`), **landing state SC.1** (17 hidden), `c_p2_dlg_naive` converted textbox → measure-bound card, leaderboard sort given a deterministic tie-break, `tbl_perfect_tens` bound to the tooltip page, screenplay honest block reflowed +24 px |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p3-act-iii-corrected-cut` | **37 visuals**, 1280×720, night canvas `#171418`, tint `#B79BE8`. Chrome ×14 · hero block ×4 (`hero_premiere_scatter` native `scatterChart`, `c_scatter_population`, `z_p3_scrim`, `c_winner_label`) · adjustments ×10 (2 card variants + 4 chips + 4 labels) · refusal ×5 · no-date ×2 · verdict ×2. **Landing state SC.3** (7 hidden). 8 measure-bound cards |
| 2026-08-05 (s6 phase B2b) | Report: `pages/tt-movie-poster` | **14 visuals**, 320×420, `type: "Tooltip"`, `visibility: "HiddenInViewMode"`, `pageBinding` type Tooltip. `z_tt_bg` · `img_tt_poster` · `c_tt_name` · `c_tt_year` · 4 label/value rows (the weighted row carries `[Mark · Rating verdict]` beside the number) · `c_tt_foot`. Every field it shows is also printed on canvas elsewhere |
| 2026-08-05 (s6 phase B2b) | Report: `definition/bookmarks/` | **9 bookmark files + `bookmarks.json`**. Folder layout and both schemas verified (Learn `projects-report`; `bookmark/2.1.0`, `bookmarksMetadata/1.0.0`). Each bookmark captures **every** visual on its page (44 / 38 / 37) with `options.suppressData: true` = Data OFF · Display ON · Current page ON · All visuals |
| 2026-08-05 (s6 phase B2b) | Report: `pages/pages.json` | `p3-act-iii-corrected-cut` appended after p2; `tt-movie-poster` appended last. Starter ids untouched; `activePageName` / `landingPageName` still `p0-box-office` |

## Deferred — not built, and why

- ~~`06 Display\Alt text` — the 10 `Alt · …` measures (BLOCKER, attribution)~~ —
  **RESOLVED and BUILT 2026-08-05 (phase B2c).** The attribution debt was closed at the
  main-thread level (commit `f4b9420`): the influencing post is credited *by
  publication* in `CREDITS.md` and `contracts/source-register.yaml` (tier 4,
  community), with the unretrievable byline recorded as an **open attribution debt**
  for a human to close. **Scope of what was adopted:** the post prompted *dynamic*
  alt text — nothing more. Its own technique wraps the narrative in **DAX
  user-defined functions**, and that pattern is **NOT** adopted here (adopting it
  would need the author's name first). The ten measures are ordinary measures driving
  Power BI's own documented dynamic-alt-text feature, the accessibility practice this
  repo credits to **Meagan Longoria**. Do not remove or weaken either entry.
- ~~Alt text on every visual is intentionally UNSET~~ — **resolved, see
  *the alt-text layer* below.** The former waiting list (p0 6 · p1 11 · p2 6 · p3 9 ·
  p9 11 · tooltip 8) is closed; every visual on it now carries alt text.
- **p9 `NEGATIVE REVENUE` row — not built.** The design's counts table lists a
  negative-revenue count, but no measure produces it (`measures.dax` has none and
  `data-model.md`'s field map lists only seven count measures). Typing `1 (−$12)`
  would be a literal count, which the snapshot-reconciliation rule forbids.
  **To unblock:** add a `Movies (negative revenue)` measure in folder
  `05 Data health · Time`, then add the row pair `c_cr_count_negrev_lbl` / `_val`
  at y 436 with tabOrder 550 / 555.
- **p9 disclosed-parameter notes — numeric parts not built.** The design prints
  `$10,000 (13.1% vs 11.9% @ $100k)` and `100 (Vote Count p90=106)`. Both
  parentheticals are stale under the entrant's newer snapshot (coverage is now
  13.05 %, votes p90 is now 104) and neither has a measure behind it. The parameter
  **values** are live and printed; the numeric notes are omitted rather than typed
  wrong. **To unblock:** add measures for the robustness pair and for votes p90,
  then bind them beside the value.

## Decisions & assumptions

- 2026-08-04 — `SourceRoot` default is the placeholder `<set-me>\TMDB` (no
  drive letter) — validator forbids machine-style absolute paths in TMDL; the
  entrant sets the real folder locally and never commits it.
- 2026-08-04 — `Rating m (disclosed)` = 100 and `Rating C (disclosed)` = 6.96
  are **disclosed constants** (signed at Q2), deliberately not computed live —
  determinism and on-canvas disclosure. SCENARIO CHOICE (signed assumption).
- 2026-08-04 — Snapshot anchor `#date(2026, 7, 24)` (dataset download date)
  hard-coded in `Is Future Release` and the Release Year `Year Status` —
  never `TODAY()`/`LocalNow()`, per blueprint determinism. SCENARIO CHOICE
  (accepted by entrant).
- 2026-08-04 — Credibility floor Budget ≥ $10,000 AND Revenue > 0 baked into
  the credible-financials measures — disclosed floor per M-002/M-004.
  SCENARIO CHOICE (signed assumption).
- 2026-08-04 — 06 Display measures are stubs returning `"s5 fills value"`
  (formatString `@`); real colors/titles/labels land with the stage-5 design
  contract.
- 2026-08-04 — Rank/single-value logic tolerates the 101 duplicate Movie ID
  rows (HASONEVALUE guard; RANKX over Movie ID values with per-ID CALCULATE).
- 2026-08-04 — Parameter meta record (`IsParameterQuery` etc.) is Desktop
  convention, not re-verified against docs this session; value-preserving M
  worst case. Desktop confirmation listed below.
- 2026-08-05 — **TMDB poster base URL RESOLVED (was VERIFY-AT-BUILD).**
  `Image · Poster URL` now uses `PosterBase = "https://image.tmdb.org/t/p/w342"`.
  Retrieved 2026-08-05 from TMDB's own documentation, not from memory:
  `https://developer.themoviedb.org/docs/image-basics` (HTTP 200; states a full
  image URL is `base_url` + `file_size` + `file_path`, worked example
  `https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg`) and
  `https://developer.themoviedb.org/reference/configuration-details` (HTTP 200;
  `secure_base_url = "https://image.tmdb.org/t/p/"`, `poster_sizes =
  ["w92","w154","w185","w342","w500","w780","original"]`).
  **Size choice `w342`** — a documented poster size, the smallest that stays crisp
  at the tooltip's 170 × 240 px poster on a 2× display and downsamples cleanly to
  the 32 × 44 leaderboard thumbnail. Not invented: chosen from the published list.
  The contracted "no posters anywhere" fallback is therefore **not** taken.
- 2026-08-05 — **Poster path concatenation verified against the source CSV.**
  `poster_path` values in `TMDB_movie_dataset_v11.csv` carry their own leading
  slash (samples: `/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg`), so
  `PosterBase & PosterPath` composes exactly the documented URL shape. No
  slash-normalising logic was added, because none is needed.
- 2026-08-05 — **`Godfather rating (reference)` VERIFY-AT-BUILD RESOLVED.** A full
  scan of the source CSV finds exactly **two** listings titled "The Godfather":
  Movie ID **238**, release 1972-03-14, budget $6,000,000, 18,677 votes; and Movie
  ID 1050474, release 2023-01-28, budget 0. The measure's `Release Year Key = 1972`
  predicate selects only ID 238, and ID 1050474 is in any case excluded by the
  partition's `budget > 0` filter. **No narrowing on Movie ID was needed**; the
  measure ships as contracted, and the verified id is recorded in its docstring.
- 2026-08-05 — **Docstring convention on the ported measures.** `measures.dax`
  docstrings carry two bookkeeping markers — the `REPLACES STUB.` prefix and the
  `Folder: … | Format: … | NEW` line. Both are build instructions that would be
  meaningless inside the model forever, and both are redundant with the
  `displayFolder` / `formatString` properties actually written. They are dropped;
  **every semantic line is kept verbatim**, including the `SCENARIO CHOICE`,
  `ILLUSTRATION` and binding notes. This follows the `tmdl-style` rule (docstring =
  business meaning) rather than the letter of the handoff.
- 2026-08-05 — **`lineageTag` authored for all 40 new measures** (fresh UUID4s)
  rather than left for Desktop to generate, so the next Desktop round-trip produces
  no gratuitous diff. Existing lineageTags were not touched.
- 2026-08-05 — **Theme registration mechanism** was derived from the report tree,
  not from memory. Evidence: `definition/report.json` declares
  `$schema … /report/3.3.0/schema.json`; that schema (fetched, HTTP 200) defines
  `themeCollection.customTheme` as a `ThemeMetadata` (`name`,
  `reportVersionAtImport`, `type` — all required; `type` ∈ {`RegisteredResources`,
  `SharedResources`}) and requires a matching `ResourcePackageItem`
  (`name`, `path`, `type`) where `CustomTheme` is a valid item type. The install
  copies that exact shape from the custom theme Desktop had already registered.
  `reportVersionAtImport` is kept at the values Desktop itself recorded for this
  report's custom theme (visual 2.10.0 / report 3.4.0 / page 2.3.1) — the report's
  schema versions have not changed, so the swap happens at the same versions.
- 2026-08-05 — **The superseded starter theme is kept registered but inactive.**
  `Accessible_City_park5942914118805086.json` remains in `RegisteredResources` and
  in the resource package; only `themeCollection.customTheme` moved. Nothing
  resolves to it (the active theme is named explicitly), no identifier was
  destroyed, and the change is reversible in one line. Deleting it is an optional
  tidy-up for the entrant, not a build step.
- 2026-08-05 — **`theme.json` independently re-validated at install:** 0 errors
  against `reportThemeSchema-2.156.json` with a Draft-7 validator, confirming the
  stage-5 claim. The install is a byte-identical copy — the deliverable and the
  installed resource cannot drift.
- 2026-08-05 — **Observation for QA, not a build defect.** A full pass over
  `project/data/TMDB_movie_dataset_v11.csv` counts 1,469,389 rows of which
  **85,870** have `budget > 0`, while `data-model.md` and the p9 cross-foot narrate
  **85,394** listings per source. Every printed count is bound to a measure and will
  therefore print whatever the loaded model actually holds, so the report stays
  self-consistent either way; but the 476-row gap should be reconciled at s7 before
  the 85,394 figure is quoted in prose.

### Stage 6 phase B1 — decisions

- 2026-08-05 — **LIVE-NUMBER BINDING MECHANISM SETTLED: fallback A, the
  `cardVisual` bound through a query projection.** The handoff's preferred
  textbox *dynamic-value run* is **not used**, because it could not be verified and
  research-first forbids writing an unverified shape. Evidence gathered:
  1. `visualContainer/2.11.0` — the version this report's own `visual.json` files
     declare — returns **HTTP 404**. Probing the series, **2.9.0 is the newest
     published** version (2.10.0 / 2.11.0 / 2.12.0 / 2.13.0 all 404). This confirms
     the stage-5 finding.
  2. `visualContainer/2.9.0` delegates `visual` to
     `visualConfiguration/2.3.0/schema-embedded.json`, which delegates `objects` to
     `formattingObjectDefinitions/1.5.0#/definitions/DataViewObjectDefinitions`.
     That definition is `{"type":"object","additionalProperties":{}}` — **completely
     untyped**. A string search of the whole file returns **0** occurrences of
     `textRun`, `paragraph` or `dynamic`. So the schema can neither confirm a
     dynamic-value run nor reject an invented one — precisely the silent-failure
     trap the `pbir-authoring` skill warns about.
  3. Microsoft Learn's PBIR report-definition page documents no textbox dynamic
     value; `create-reports/desktop-add-text-boxes` returns 404.
  4. The published theme schema types the theme-level textbox
     `paragraphs.textRuns` with `value` **required** and **string-only** — no
     expression variant. (Indicative only: instances use `textStyle` where the theme
     uses `textRunStyle`, so the shapes already differ.)
  5. No Microsoft-authored PBIR sample was reachable — `microsoft/powerbi-desktop-samples`
     ships `.pbix` only, and its `item-schemas` tree covers `definition.pbir` and
     `localSettings` but no visual schemas.
  6. Desktop is closed, so it could not be made to serialise one for observation.
  **What IS verified**, and therefore what is used: a measure binding as a query
  projection — `query.queryState.<Role>.projections[].field.Measure` — proven both
  by the typed `Query` / `RoleProjection` definitions and by this report's own
  Desktop-authored `tableEx` (`e21488a8d900077091bd`) and the two
  `VerifiedAnswers/*/visualSource.json` files.
  **This mechanism is now fixed for the whole report.** Every prose-with-a-number in
  phase B2 uses a `cardVisual`, not a textbox — one mechanism, once, consistently.
  **Cost, stated plainly:** a card cannot mix styled runs inside one string, so
  prose that wanted a differently-styled trailing clause (for example the 11 pt
  `(USD as recorded; gross gap, not P&L.)` on `c_verdict_act1`) must ship as a
  second adjacent object in phase B2.
- 2026-08-05 — **ALT-TEXT PROPERTY PATH VERIFIED** (the open item the handoff left
  for stage 6). It is `visual.visualContainerObjects.general[0].properties.altText`,
  confirmed in `visualConfiguration/2.3.0/schema-embedded.json` →
  `VisualContainerGeneralFormattingObjects`, whose properties are exactly
  `x, y, width, height, altText, allowBinnedLineSample, allowOverlappingPointsSample,
  keepLayerOrder`. Nothing is written there yet — the attribution hold stands — but
  the research question is closed.
- 2026-08-05 — **Property vocabulary was verified before writing, not recalled.**
  The published `reportThemeSchema-2.156` enumerates the valid visual names and, per
  visual, the formatting-card names and their properties. Two consequences worth
  recording: (a) **`basicShape` is not a valid visual name** — the correct name is
  **`shape`**, which is also what this report's own Desktop-authored files use, so
  every rectangle in the handoff spec'd as `basicShape` is built as `shape`; the
  `basicShape` block inside `theme.json` targets nothing and is dead weight (harmless,
  worth pruning at s7). (b) `cardVisual`'s cards are `value` (font family/size/colour,
  bold, italic, `horizontalAlignment`, `textWrap`) and `label` (`show`) — which is how
  the callout is styled as body text with the category label off.
- 2026-08-05 — **Five tokens could not be verified from any published source.** They
  are recorded here because each is a *rendering* risk, not a corruption risk: the
  schemas explicitly leave these open (`queryState` is an open map keyed by role
  name; enum values are untyped `{}`), so a wrong value fails visibly in Desktop and
  is a one-line fix. Each is on the manual checklist below.
  1. `cardVisual` query **role name** — written as `"Data"`.
  2. `visualLink.type` enum — written as `'PageNavigation'`.
  3. `textAngle` on a shape — written as `270L` for the vertical ticket-stub text.
  4. `rectangleRoundedByPixel` + `rectangleRoundedCurve: 8L` for the 8 px ticket
     radius (chosen over `rectangleRounded` because the tileShape name states the
     unit; both are in the published enum).
  5. `horizontalTextAlignment` on a textbox paragraph — the name comes from the
     theme schema's `paragraphs` definition; instances in this report never set it.
- 2026-08-05 — **Two contracted media were substituted, with reasons.**
  1. **Ticket stub art: `ca-canvas` SVG → native `shape` with rotated text.** The
     handoff contracts an SVG image for the vertical `ADMIT ONE` and the serial.
     The published theme schema exposes **`textAngle`** on `shape`, so the same
     content ships as real text (`z_ticketN_admit`, `z_ticketN_serial`) instead of a
     picture. This is better than the contract, not worse: real text is selectable,
     scalable and survives a screen reader, whereas the SVG route needed an
     unverifiable data-URI and was contracted as decorative-with-empty-alt anyway.
     **Fallback if `textAngle` does not render:** drop to horizontal text at the
     stub foot, or restore the SVG.
  2. **p9 `tbl_production_counts` / `tbl_disclosed_params`: `tableEx` → label
     textbox + measure-bound value card, one pair per row.** A `tableEx` fed eight
     measures renders eight **columns in one row**, not eight label/value rows; a
     real row-per-metric table would need a disconnected metric dimension, which the
     model does not have and which phase A did not build. The alternative — typing
     the labels and the numbers — is exactly what the snapshot-reconciliation rule
     forbids. The pair-per-row build keeps **every number measure-bound** and gives a
     keyboard user a label stop immediately before each value stop.
- 2026-08-05 — **Perforation dashes not available.** `z_ticketN_perf` is spec'd as a
  1 px **dashed** line. The published `shape` property list has no dash/line-style
  property (`linecapType` only), so the contracted fallback is taken: a **solid**
  1 px `#9A9284` line, with the pre-torn read carried by the separate
  `z_ticketN_stub_rule` frame either side of it.
- 2026-08-05 — **Letter-spacing is not expressible in PBIR.** The design specifies
  tracking on the marquee title (0.14 em), subtitle (0.32 em), section heads and the
  ticket serial. A textRun's style carries only fontFamily / fontSize / fontWeight /
  fontStyle / colour / textDecoration. Tracking is therefore **dropped everywhere**;
  it is a uniform, deliberate fidelity loss, not a per-object slip.
- 2026-08-05 — **Reserved-red rule held.** An automated check over both pages finds
  trap red (`#B3402E` / `#E8705F`) in exactly one place: the `[TRAP]` tag run inside
  `c_cr_glossary`, where it names the trap in words as well as colour. p0 contains
  no red at all; `btn_credits` and `btn_home` are neutral cream `#F2EFE6` outline
  and text, as required.

### Stage 6 phase B2a — decisions (p1 · p2)

- 2026-08-05 — **DENEB IS NOT AVAILABLE; both contracted fallbacks are taken.**
  Checked, not assumed: `report/3.3.0/schema.json` defines
  **`publicCustomVisuals`** ("Names of the custom visuals used in this report from
  AppSource") and `organizationCustomVisuals`. This report's `report.json` declares
  **neither**, and no custom-visual payload exists under `StaticResources`. An agent
  cannot register an AppSource visual (it needs Desktop to download the package, and
  the identifier + version could not be verified from any published source), so
  inventing a registration was refused.
  - `dn_ticket_waffle` → **native `hundredPercentStackedBarChart`** at the same rect,
    `[Movies (credible financials)]` in good-green `#2F6B4F` against
    `[Movies (no credible financials)]` in neutral `#78716C`. Ids kept (`dn_` prefix)
    so the bookmark lists, the handoff and the alt-text register still line up.
  - `dn_rating_fall` → **native `clusteredBarChart`** (paired bars) at the same rect,
    `[Rating (raw)]` trap-red vs `[Rating (evidence-weighted)]` good-green, with a
    dashed **reference line at 6.96** named `C = 6.96` (`referenceLine` card:
    `show/value/lineColor/style/width/position/displayName/dataLabelShow/
    dataLabelText/dataLabelColor/dataLabel*Position` — every property and both enums
    verified in `reportThemeSchema-2.156`).
  - **To restore Deneb** (optional, entrant-only): install Deneb from AppSource in
    Desktop, author the two Vega-Lite specs, and the containers can be re-typed;
    PBIR can carry the container but not the spec.
- 2026-08-05 — **layout.json is the measured truth; the handoff supplies the
  decomposition.** Rects were taken from `design-prototypes/layout.json` screens
  `p1-act-i-sc1/sc3` and `p2-act-ii-sc1/sc3` wherever the prototype has a *block*
  element for the object. Where layout.json only measures an inline text run
  (`span`/`p`), the handoff's box wins — a text extent is not a box. Where the
  handoff decomposes one measured block into two PBIR objects (margin note = 2 px
  rule + inset text), the handoff's decomposition is built inside the measured
  block. **Differences resolved in layout.json's favour** (handoff → built):
  | Object | Handoff | Built (measured) |
  |---|---|---|
  | `c_p1_action` | 34,195,470,40 | 34,**196**,470,38 |
  | `c_p1_cue_naive` | 34,251,… | 34,**248**,… |
  | `c_p1_dlg_naive` | 129,270,… | 129,**267**,… |
  | `c_p1_trans` | 34,328,… | 34,**319**,… |
  | `c_p1_slug_honest` | 34,361,500,… | 34,**352**,**524**,… |
  | `c_p1_cue_honest` | 34,398,… | 34,**385**,… |
  | `c_p1_dlg_honest` | 129,417,315,116 | 129,**404**,315,114 |
  | `c_p1_slug_naive` / `c_p2_slug_naive` | w 500 | w **524** |
  | `c_kpi_profit_*`, `c_waffle_*`, `c_lb_*`, `c_fall_*` | x 816 / w 424 | x **817** / w **422** (426 on p2's fall card) |
  | `z_kpi_profit_strike` | 810,236,436,2 | **811,230,308**,2 (matches the measured value width) |
  | `c_kpi_profit_misread` | 816,264,… | 817,**255**,… |
  | `z_pN_verdict_rule` | y 624 | y **632** (the measured verdict band's top border) |
  | `btn_next_scene` | 1106,100,150,32 | **1124,100,132**,32 |
  | `btn_next_act` (p1) | 1106,648,150,32 | **1142,649,114**,32 |
  | `btn_next_act` (p2) | 1106,648,150,32 | **1110,649,146**,32 |
  | `c_p2_action` … `c_p2_dlg_honest` | y 195/232/251/309/342/379/398 | y **196/229/248/300/333/366/385** |
  | `c_p2_note_*` | y 196/248/352 h 16/44/44 | y 196/248/352 h **22/64/50** |
  | `dn_rating_fall` | 812,422,432,172 | **813,420**,432,172 |
  **Beat-rail widths are a genuine conflict and were resolved by max-width.** The
  prototype's chips auto-size, so the same button measures 187.2 px at SC.1 (with the
  `●`) and 173.4 px at SC.3; PBIR buttons are fixed. Built at the SC.1 (default-beat)
  positions with the widest measured text: `btn_beat_1` 24,100,**188**,32 ·
  `btn_beat_2` **222**,100,148,32 · `btn_beat_3` **380**,100,**222**,32 — 10 px
  gutters, no state clips its own label.
- 2026-08-05 — **Text-container heights are the measured height + ~8 px.** A CSS line
  box is tighter than a PBIR text container, which adds internal padding; at the
  measured heights, 12 pt Consolas clips. x, y and width are measured exactly. Where
  two adjacent transparent text containers overlap by a few px as a result, nothing
  renders differently — both have `background.show = false` and explicit z-order.
- 2026-08-05 — **Live numbers: the phase-B1 `cardVisual` mechanism, unchanged.**
  12 measure-bound cards across the two pages (`c_p1_action`, `c_p1_dlg_naive`,
  `c_p1_dlg_honest`, `c_kpi_profit_label`, `kpi_profit_naive`,
  `kpi_profit_naive_corrected`, `c_p1_note_zeros`, `c_waffle_title`, `c_waffle_foot`,
  `c_verdict_act1`, `c_p2_note_median`, `c_p2_dlg_honest`, `c_verdict_act2`). The
  only literals on either page are contracted non-numeric copy plus the disclosed
  parameters. **The 11 pt trailing clause of `c_verdict_act1` ships as a second
  object** (`c_verdict_act1_note`, 24,672,1040,22) because a card cannot mix
  differently-styled runs — the cost recorded at phase B1, now paid.
- 2026-08-05 — **`c_p1_note_budget`: the stale median is dropped, not typed.** The
  contracted string is `…min $1, median $2,800.` A full pass over the loaded CSV
  (84,510 in-partition non-adult rows) gives **min budget $1** (contract correct,
  kept) and **median budget $2,961** — the contracted $2,800 is stale under the newer
  snapshot and no measure produces it. Following the phase-B1 precedent (p9's stale
  parentheticals), the clause is omitted rather than printed wrong; the note ships as
  `NOTE: Budget is never 0 here. Unknowns arrive as junk: min $1.`
  **To restore:** add a `Median budget (all listings)` measure and bind it beside
  the min.
- 2026-08-05 — **`c_p1_note_negrev` verified TRUE against the loaded snapshot.**
  Exactly **one** in-partition non-adult listing books negative revenue: −$12
  ("Some Bears"). The contracted sentence ships verbatim.
- 2026-08-05 — **`c_waffle_cap` re-worded for the fallback medium (CONTRACT
  DEVIATION — needs designer ack).** The contracted caption
  `green ✓ = VALID (13) · outline = no credible financials (87)` legends a *waffle*:
  filled vs **outline** cells. The bar fallback has no outline cells, and (13)/(87)
  are typed counts. Shipped: `green ✓ = VALID · gray = no credible financials`, with
  the live share printed by `c_waffle_title` (`[Copy · Act I · waffle title]`) and the
  proportion carried by the bar itself. The `✓` and the words remain the non-colour
  carriers.
- 2026-08-05 — **`tbl_perfect_tens` column headers cannot be hidden.** The design
  says "column headers hidden". The published theme schema's `tableEx` →
  `columnHeaders` card has **no `show` property** (`alignment, autoSizeColumnWidth,
  backColor, bold, columnAdjustment, customColumnWidth, defaultColumnWidth, fontColor,
  fontFamily, fontSize, italic, outline*, underline, wordWrap`) and no `show` exists
  anywhere else on `tableEx`. Inventing one was refused. Headers ship **styled quiet**
  (Segoe UI 10 pt `#57534E` on `#FFFFFF`, not bold). This costs a row of vertical
  space and it *helps* a screen-reader user, who now hears real column names.
- 2026-08-05 — **`tbl_perfect_tens` per-column fonts are not expressible.** The
  design wants the score column in Consolas 12 pt bold; `columnFormatting` carries
  only `alignment, backColor, dataBars, fontColor, labelDisplayUnits, labelPrecision,
  style*` — no font family/size/weight per column. The table uses one family
  (Segoe UI 12 pt) and the score column keeps its **trap-red `#B3402E`** plus the
  `[Mark · Rating verdict]` column, which prints `✕ thin evidence` in words. Colour is
  still never the only carrier.
- 2026-08-05 — **`[Color · Rating verdict]` is deliberately NOT bound.** Binding a
  measure into a column's `fontColor` (fx → field value) has a serialisation shape
  this session could not verify, and the filter guarantees every visible row is a raw
  10.0 — the measure would return trap for all of them. The static trap red says the
  same thing with a verified property. **To restore:** bind it by hand in Desktop and
  capture the resulting JSON here.
- 2026-08-05 — **Visual filters were built from typed schema, not memory.**
  `filterConfiguration/1.3.0` + `semanticQuery/1.4.0` were fetched and read:
  `tbl_perfect_tens` and `dn_rating_fall` each carry an **Advanced** filter
  (`Comparison`, `ComparisonKind: 0`, `Literal "10D"`) for `[Rating (raw)] = 10` and a
  **VisualTopN** filter (`{"VisualTopN": {"ItemCount": 3}}`) over a `sortDefinition`
  of `[Votes]` **Ascending**. Note: the classic Desktop `TopN` filter expression does
  **not exist** in `semanticQuery/1.4.0`'s `QueryExpressionContainer` — only
  `VisualTopN` — so that is what was written. If `VisualTopN` does not take, the
  failure is visible (more than three rows) and the story still reads.
- 2026-08-05 — **`actionButton` outline weight: `weight`, not `lineWeight`.** The
  published theme schema lists `visual-actionButton → outline → [lineColor, show,
  transparency, weight]`; there is no `lineWeight`. p1/p2 buttons use `weight`.
  **Pre-existing defect for the next phase to sweep:** exactly two files written at
  phase B1 use `lineWeight` — `p0-box-office/visuals/btn_credits` and
  `p9-end-credits/visuals/btn_home`. Both should be changed to `weight` in one
  single-concern diff. Not fixed here: it is outside this phase's scope and the
  symptom is a button outline at the theme's default thickness instead of 1 px, not a
  broken file.
- 2026-08-05 — **`z_pN_admit` substitutes the contracted `ca-canvas` SVG** with a
  native `shape` (fill `#FFFFFF`, 2 px act-tint outline, centred `ADMIT ONE` in
  Consolas 10 pt ink, `horizontalAlignment: center` / `verticalAlignment: middle` —
  both enums verified). Same substitution the p0 ticket stubs took at phase B1, same
  reason: real text beats an unverifiable data-URI picture. The contracted 1.5 px
  stroke becomes 2 px (`weight` is an integer). Id renamed from the handoff's
  `z_pN_admit_svg` because it is not an SVG.
- 2026-08-05 — **Beat-rail state is built at SC.3 (the fullest state).**
  `btn_beat_3` carries the act-tint fill, cream text and the leading `●`;
  `z_pN_beat3_mark` (the 3 px detached underline, act tint) is visible and
  `z_pN_beat1_mark` / `z_pN_beat2_mark` are `isHidden`. On p1 `kpi_profit_naive` is
  `isHidden` and `kpi_profit_naive_corrected` is visible, exactly as the SC.3
  bookmark specifies. The three marks exist as separate objects so the bookmark phase
  has a **visibility** mechanism for the current-beat indicator even if formatting
  capture on the buttons proves unreliable.
- 2026-08-05 — **`btn_next_scene` and `btn_beat_1..3` carry NO `visualLink`.** They
  are bookmark actions, and bookmarks do not exist yet. Phase B2b adds
  `visualLink.type = 'Bookmark'` (verify the enum spelling against
  `visualConfiguration` before writing it). Everything else on those buttons — shape,
  fill, outline, text, title/background/border/dropShadow — is explicit.
- 2026-08-05 — **Paper-surface override applied per visual, as documented.** Every
  p1/p2 card is `#FFFFFF` with a 1 px `#D8D4C8` hairline and radius 0; text is
  `#211E1A` / `#57534E`; chart neutral is `#78716C`; page + outspace background is
  `#F5F2E9`. One rule, one reason (a single theme cannot serve two surfaces).
- 2026-08-05 — **Scope rule and reserved red checked by script, not by eye.** An
  automated pass over all four built pages finds: act tints (`#2E4A7D` / `#8A6516` /
  `#5B3E8E`) on **no data visual**, and trap red only on the reserved set (slug tags,
  the strike, the MISREAD tag, the three script-doctor rules and their notes, the
  leaderboard's score + verdict columns, the dumbbell's raw dot) plus p9's `[TRAP]`
  glossary tag. Navigation (`NEXT SCENE ▸`, `NEXT ACT ▸`, `THE PREMIERE ▸`) is act
  tint; `btn_home` / `btn_credits` are ink. 0 violations.

### Stage 6 phase B2a — FINDINGS FOR THE DESIGNER / QA (not build defects)

1. **`c_p2_dlg_naive` names a film the leaderboard beside it will not show.** The
   contracted line is `The best film ever made? Las mujeres deciden. A perfect 10.0!`
   A full pass over the loaded CSV confirms *Las mujeres deciden* (Movie ID 458672)
   does hold a **perfect 10.0 on 2 votes** — the sentence is TRUE. But the newer
   snapshot has **4,610** perfect 10s with at least one vote, of which **4,304 have
   exactly 1 vote** (260 have 2, 33 have 3). `tbl_perfect_tens` is contracted as
   *top 3 **ascending** by `[Votes]`*, so it will show three arbitrary **1-vote**
   titles and never this film. The trap reads *harder* that way — but the dialogue no
   longer corresponds to the exhibit next to it. **Decision needed (designer):** (a)
   leave it — the dialogue is an illustration, the table is the population; (b) sort
   the leaderboard **descending** by votes so the most-voted perfect 10 leads; or
   (c) add a `Title · Perfect ten (illustration)` measure and bind the film name live.
   Nothing was changed unilaterally.
2. **Two contracted "at least" strings are now large understatements** — true, but
   thin. `c_lb_more`: "+ at least 18 more perfect 10s" (actual: 4,607 more).
   `c_p2_note_twenty`: "at least 20 films score a perfect 10.0 on 2–3 votes"
   (actual: 293). Both ship verbatim because they are contracted and remain literally
   true; both would be stronger bound to a measure.
3. **Loaded-snapshot counts, for the record** (full CSV pass, 2026-08-05):
   in-partition non-adult listings **84,510** · credible financials **11,116** ·
   coverage **13.15 %** · zero-revenue **66,853 (79.1 %)** · negative-revenue rows
   **1 (−$12)**. Every one of these prints from a measure, so the report stays
   self-consistent; they are here so s7 can reconcile the narrated 85,394 / 84,036.
4. **p1 and p2 carry more tab stops than the handoff enumerates** (31 and 26 vs the
   contracted 23 and 22). The extra stops are the informational card kickers, labels,
   titles and captions (`c_kpi_profit_kicker`, `c_kpi_profit_label`,
   `c_kpi_profit_misread`, `c_waffle_kicker/title/cap`, `c_lb_kicker`,
   `c_fall_kicker/title`) plus `c_verdict_act1_note`. The handoff's enumerated order
   is preserved **exactly as a subsequence**; each label stop sits immediately before
   the value it labels (the p9 precedent). This is deliberate: while the alt-text
   family is blocked, these stops are the only way a screen-reader user hears
   `INSERT — THE NAIVE NUMBER` and the label ending in `(naive)` — carrier 3 of the
   M-003 marking. If the alt-text blocker clears, they can be dropped back to `-1`.

### Stage 6 phase B2b — THE ACT II RULING (recorded design decision)

**Ruled by the coordinator on 2026-08-05, on the phase-B2a finding.** The finding
was that *Las mujeres deciden* is real (perfect 10.0 on 2 votes, Movie ID 458672)
but is one of **4,610** perfect tens, **4,304** of which rest on a **single** vote —
so the leaderboard beside the line could never show it. The ruling replaces the
named-film framing with the aggregate, which is both more damning and snapshot-proof,
and which stops the report implying one film is "the best" when thousands tie.

Implemented exactly as ruled:

- **`Movies (perfect ten)`** = `CALCULATE([Movies], Movies[Vote Average] = 10,
  Movies[Vote Count] >= 1)` and **`Movies (perfect ten, single vote)`** = the same at
  `Vote Count = 1` — both `03 Lie 2 · Ratings`, format `#,0`.
- **`Single-vote ten (illustration)`** = the shrinkage formula at v = 1
  (`1/101 × 10 + 100/101 × C`) ≈ **6.99**, format `0.00`. It sits beside the existing
  `Two-vote ten (illustration)`, which is now unused by any visual but is **retained**
  (nothing is deleted; identifiers are preserved).
- **`Copy · Act II · naive read`** (NEW) composes the ruled sentence with both counts
  live: *"The best film ever made? Take your pick — ‹n› listings score a perfect 10.0.
  ‹n› of them on a single vote."* `c_p2_dlg_naive` changed from a textbox to a
  measure-bound `cardVisual` to carry it. **No film is named anywhere in Act II.**
- **`Copy · Act II · responsible read`** and **`Copy · Act II · verdict`** rewritten to
  the aggregate: *"a perfect 10.0 on a single vote reads ‹6.99› — barely above the
  global mean of ‹6.96›"*, with m and C printed from their disclosed measures.
  `Godfather rating (reference)` is now unused by any visual — **retained**, not
  deleted.
- **`tbl_perfect_tens`** sorts `[Votes]` **Ascending** with a deterministic tie-break.
  **Deviation from the ruling, with its reason:** the ruling named *Movie ID ASC* as
  the tie-break, but the table groups by `Movies[Title]`, so Movie ID is not a
  grouping column and could only be sorted on via an aggregation measure the model
  does not have — or by spending ~40 % of the Title column's width on an ID that the
  aggregate framing no longer needs. The tie-break is **`Movies[Title]` Ascending**:
  it is the visual's own group key, therefore exact, and it is refresh-stable for the
  same data. Each row prints its vote count, as ruled. Overrule this and the fix is
  one projection plus one sort clause.
- **Three Act II strings that depended on the named film or on a typed magnitude were
  rewritten** (contract deviation, logged): `c_p2_note_twovotes` "NOTE: 2 votes." →
  *"NOTE: one vote is enough to score a perfect 10.0."* · `c_p2_note_twenty` "at least
  20 films…" → *"NOTE: a raw score has no evidence floor — it never says how many
  voted."* · `c_lb_more` "+ at least 18 more perfect 10s" → *"sorted by fewest votes,
  then title — three of the perfect tens counted above."* None of the three now types
  a count or a magnitude word; the live counts are printed once, by
  `c_p2_dlg_naive`. This also closes phase-B2a finding 2.
- The screenplay column's honest block moved **+24 px** (trans 314→338, slug 347→371,
  cue 380→404, dialogue 399→423) because the ruled dialogue is four lines where the
  prototype's placeholder was one. `c_p2_dlg_naive` is 86 px tall, not 60.

### Stage 6 phase B2b — decisions (p3 · tooltip · bookmarks)

- 2026-08-05 — **THE PLAY AXIS IS NOT WRITTEN. This is the contracted animation and it
  is now a manual Desktop step, not a silent drop.** What was checked, in order:
  `reportThemeSchema-2.156` (`visual-scatterChart` exposes a **`currentFrameIndex`**
  card, which proves the play axis exists — but a theme schema names cards, never data
  roles); `visualConfiguration/2.3.0` (`queryState` is an **open map keyed by role
  name**, so it enumerates nothing); Microsoft Learn (`power-bi-visualization-scatter`
  and a Learn search for "play axis" — no role name published; the PBIR
  `projects-report` page carries no visual example); this repo's own Desktop-authored
  files (a `lineClusteredColumnComboChart` gives `Category` / `Y` / `Y2` / `Tooltips`,
  a `tableEx` and two slicers give `Values` — **no scatter anywhere**, including
  inside `project/contest/*.pbix`). No published source names the key, so per
  research-first none was invented.
  **Consequence:** `hero_premiere_scatter` ships with `Category` / `X` / `Y` and **no
  play well**, so the year-by-year animation, the native 28 pt year read-out and the
  `▶ PRESS PLAY` control are all absent until the entrant drags
  `'Release Year'[Year Label]` into the Play axis in Desktop (one drag — see the
  checklist). The scatter itself is complete and the finding reads without it;
  `[Label · No date]` already says "they never enter this animation", which becomes
  true the moment the well is filled.
  **`Category` / `X` / `Y` are themselves unverified role keys** (see the token list) —
  they are conventional cartesian names and the failure is visible, not silent.
- 2026-08-05 — **`hero_premiere_scatter` detail.** X = `Sum(Movies.Revenue)` with
  `categoryAxis.logAxisScale = true` (log X, verified property); Y =
  `[Rating (evidence-weighted)]`; Details = `Movies[Title]`; axis titles printed per
  the handoff; value-axis gridlines `#241F28`; legend and category labels off; a
  **`y1AxisReferenceLine` at 6.96** named `C = 6.96`, dashed, `#6E6960` (every
  property and both enums verified). Visual filter
  `[Movies (scatter population)] >= 1` restricts the plot to the credible,
  ≥ m-votes population. Tooltip bound to `tt-movie-poster`.
- 2026-08-05 — **Measure-driven colours are NOT bound, on either page.**
  `[Color · Scatter mark]` (the good-green winner dot) and `[Color · Rating verdict]`
  (the leaderboard) are left unbound. `formattingObjectDefinitions/1.5.0` types
  property values as **`{"type":"object","additionalProperties":{}}`** — completely
  open — so the "fx → field value" serialisation is unverifiable, and a wrong colour
  fails *quietly*, which is exactly the trap the `pbir-authoring` skill warns about.
  The scatter uses an explicit `dataPoint.defaultColor` of neutral `#B5AFA0`.
  **What this costs:** the winner is currently named, not coloured — `c_winner_label`
  carries `✓ ‹winner› — best-selling AND best-rated on evidence`, so the honest read
  still has its glyph and its words, but not its green dot. **Two Desktop steps**
  restore both (see the checklist); capture the JSON when you do.
- 2026-08-05 — **`tbl_refusal_ranks` gains a fifth column and a new measure.**
  `Mark · Rank divergence` = `IF(ABS([Rank · Popularity] − [Rank · Rating (weighted)])
  > 100, "✕", "")` — the design specified this rule in words; implementing it is not
  improvisation, and it is the reserved-red carrier on the refusal card. Popularity is
  still never good/bad-coloured. The table is **80 px tall, not the measured 46**,
  because native table headers cannot be hidden and three rank rows need the room;
  the space comes from the `@ build` placeholder line, an accepted omission
  (asset-fidelity inventory #40).
- 2026-08-05 — **`btn_next_scene` is built as two paired variants.** A static button
  cannot know which beat is showing, so `btn_next_scene` (visible at SC.1 → `bm_pN_b2`)
  and **`btn_next_scene_2`** (visible at SC.2 → `bm_pN_b3`) share one rect and are
  toggled by the bookmarks. At SC.3 **both are hidden** — the handoff says "disabled at
  SC.3" and PBIR has no disabled state, so absent is the honest reading. The existing
  id `btn_next_scene` was **not renamed**.
- 2026-08-05 — **Landing states flipped to the contracted defaults.** p1 and p2 now sit
  on disk in their **SC.1** state (22 and 17 objects `isHidden`), p3 in its **SC.3**
  state (7 hidden). A PBIR page has no "default bookmark" — the on-disk state *is* the
  default — so a scripted check asserts that each page's on-disk hidden set is
  byte-identical to its default bookmark's hidden set. It is. This also restores the
  trap-first opening the fidelity checklist requires: p1 and p2 land on the naive cut
  with all four M-003 carriers present except the blocked alt text.
- 2026-08-05 — **Bookmark mechanism, with its evidence.** Layout verified on Microsoft
  Learn (`developer/projects/projects-report`): `definition/bookmarks/
  [bookmarkName].bookmark.json` plus `definition/bookmarks/bookmarks.json`. Each file
  validates against **`bookmark/2.1.0`** (the newest published; 2.2.0+ are 404) and the
  registry against **`bookmarksMetadata/1.0.0`** (1.1.0+ are 404). Shape used:
  `explorationState.sections[<page>].visualContainers[<visual name>]`, with
  `{"singleVisual": {"display": {"mode": "hidden"}}}` for hidden objects and
  `{"singleVisual": {}}` for shown ones — `VisualContainerDisplayMode` has **no
  "visible" member**, so visibility-on is the absence of `hidden`, which is why every
  visual on the page is listed rather than only the hidden ones. `options` carries
  **only** `suppressData: true`; `suppressDisplay`, `suppressActiveSection` and
  `applyOnlyToTargetVisuals` are absent, which is Data OFF / Display ON / Current page
  ON / All visuals. Learn also documents that Desktop **prunes visuals it cannot
  resolve** from a bookmark, so a stale name degrades rather than corrupts.
- 2026-08-05 — **The current-beat button style is carried twice, on purpose.**
  Each bookmark writes `singleVisual.objects.merge` for the three beat buttons (fill =
  act tint or off; text = the label with or without the leading `●`; font colour), and
  *separately* toggles the three `z_pN_beatN_mark` underline shapes. If the formatting
  merge does not apply, the underline still marks the current beat by **position**, so
  the state is never carried by colour alone. `DataViewObjectDefinitions` is an
  untyped map in the published schema, so the merge is schema-legal but its effect is
  unverified.
- 2026-08-05 — **Tooltip page.** `type: "Tooltip"`, `visibility: "HiddenInViewMode"`
  and `pageBinding: {name, type: "Tooltip"}` — all three verified in `page/2.1.0`.
  Consumers bind through `visualContainerObjects.visualTooltip` with
  `type: 'Canvas'` + `section: 'tt-movie-poster'` (both verified in the theme schema);
  bound on `tbl_perfect_tens` (p2) and `hero_premiere_scatter` (p3).
  Rows are built as **label textbox + measure-bound value card** (the p9 precedent),
  because a `tableEx` fed four measures renders four columns in one row, not four
  label/value rows. The weighted row prints `[Mark · Rating verdict]` beside the
  number so the word travels with the colour. **Nothing in the tooltip is unique to
  it** — title, year, votes, raw and weighted ratings and the popularity rank are all
  printed on canvas on p2/p3, so the tooltip is enhancement, as required.
- 2026-08-05 — **`img_tt_poster` is the one genuinely speculative object.** The `image`
  visual's `image` card properties (`sourceType` enum `image` / `imageUrl` /
  **`imageData`**, `sourceField`, `fit` enum) are verified in the theme schema, but the
  **data-well role key is not published**; `"Values"` was used (this repo's only
  evidenced generic role). If it does not take, the poster box is simply empty and the
  card still reads — which is exactly the fallback the handoff contracted
  ("omitted entirely if the base URL cannot be verified — the card reads without it").
- 2026-08-05 — **Unverified tokens introduced in this phase** (each fails visibly, each
  is a one-line fix; they join the five recorded at phase B1):
  1. `scatterChart` role keys `Category` / `X` / `Y`.
  2. `visualLink.type` value `'Bookmark'` (sibling of the already-used
     `'PageNavigation'`; `VisualLink.bookmark` **is** a published property).
  3. `explorationState.version` value `"1.0"` (the schema requires a string, types no
     value).
  4. The bookmark `objects.merge` payload shape for the beat buttons.
  5. `image` visual role key `"Values"` and the `sourceField` string
     `"_Measures.Image · Poster URL"`.
  6. `filterConfig` type `VisualTopN` behaviour (schema-typed, effect unverified).

### Stage 6 phase B2c — the alt-text layer (2026-08-05)

**Attribution first, implementation second.** The blocker was cleared at the
main-thread level (commit `f4b9420`) by crediting the influencing Fabric Community
post **by publication** in `CREDITS.md` and `contracts/source-register.yaml`, with
the byline recorded as an **outstanding attribution debt**. The adopted idea is
narrow: *make alt text dynamic*. The post's **DAX user-defined function** pattern is
**not** adopted — implementing it would require the author's name first. What ships
is ten plain measures on Power BI's own documented dynamic-alt-text feature, the
accessibility practice this repo already credits to **Meagan Longoria**.

**Ten measures built** in `_Measures`, folder `06 Display\Alt text`, format `@`, each
with a `///` docstring, each composing live numbers from its bound measures — no count
is typed inside a measure: `Alt · kpi_profit_naive · SC1` · `· SC3` ·
`Alt · dn_ticket_waffle` · `Alt · tbl_perfect_tens` · `Alt · dn_rating_fall` ·
`Alt · hero_premiere_scatter` · `Alt · c_refusal_popularity` · `Alt · c_nodate_chip` ·
`Alt · tbl_production_counts` · `Alt · tt_movie_poster`. Model: 79 → **89 measures**.
Two adjustments to the `measures.dax` drafts, both recorded: `Alt · dn_rating_fall`
now uses **`[Single-vote ten (illustration)]`** (not the two-vote one) so it matches
the Act II ruling and the chart it narrates; `Alt · tbl_perfect_tens` gained the two
perfect-ten counts for the same reason.

**On disk the alt text is STATIC, not measure-bound — and that is deliberate.**
The property *path* is verified (`visual.visualContainerObjects.general[0].properties
.altText`; `VisualContainerGeneralFormattingObjects` has a **closed** property list
containing `altText`). The property's **value** is typed `{}` — completely open — so a
measure expression there is exactly as unverifiable as the colour bindings, and its
failure mode is **silence**. Silence is the one outcome a screen-reader user must not
get, so every visual received a literal string in the shape Desktop itself writes.
Per the coordinator's ruling: **no volatile count is typed anywhere**. The strings
state the finding using only contracted literals — `$10,000`, `m = 100`, `C = 6.96`,
snapshot `24 July 2026`, and `6.99`, which is *derived* from m and C
(1/101 × 10 + 100/101 × 6.96) and is therefore not snapshot-volatile. Volatile
quantities are phrased around ("a minority of the basis", "most revenues …",
"the live count is printed on the card"). **Switching to the live measures is one
Desktop step per visual** (`fx → Field value`) and the measures are already there.

**Coverage — 210 visuals, none left undecided:**

| Treatment | Count | Which |
|---|---|---|
| **Content alt** (static finding-stating sentence) | **76** | every `cardVisual`, `tableEx`, chart, scatter · the three ticket buttons · every navigation and beat button |
| **Empty alt** `""` (skipped by readers) | **73** | all decorative chrome — frames, rules, card backgrounds, perforations, ticket internals, the `z_pN_admit` glyphs, the beat marks, the scrim, the chip outlines, `z_tt_bg`, and `img_tt_poster` |
| **Left UNSET** (own text is the accessible content) | **61** | textboxes — slugs, cues, transitions, notes, kickers, captions, the glossary, the credits copy, the tooltip's row labels and footnote |

- **Textboxes are deliberately not given alt text.** A textbox's own runs *are* its
  accessible content; PBIR alt text would replace rather than supplement them, so a
  duplicate sentence would either double-read or silence the real copy. They were
  never on the waiting list.
- **`img_tt_poster` gets empty alt.** The poster is redundant with `c_tt_name`
  directly beneath it — narrating it twice is noise, not access. This is also the
  handoff's own position that the poster is enhancement.
- **State-specific alt on the paired variants (M-003 carrier 4 is now present).**
  `kpi_profit_naive` opens *"Trap exhibit. This profit total treats unknown revenues
  as zero dollars, so it is the naive reading, not a finding…"*;
  `kpi_profit_naive_corrected` opens *"Trap exhibit, struck through and labelled
  MISREAD. The naive profit total is withdrawn…"*. `tbl_perfect_tens` likewise opens
  *"Trap exhibit."*. All four M-003 carriers are now live at SC.1 on p1 and p2.
- **Beat buttons carry the contracted accessible name** — `"Scene N of 3 — <title>"`
  plus what the beat does — which is M-003 carrier 2 for a screen-reader user. These
  are page-specific (p3's beats are The Adjustments / The Refusal / The Premiere).
- **`[Alt · tbl_production_counts]` binds to `c_cr_count_basis_val`** on p9 — the
  cross-foot's *result* — because the counts "table" is built as label/value pairs.
  This is the same slot-named-measure pattern the handoff records for
  `[Alt · c_refusal_popularity]` (→ `tbl_refusal_ranks`) and `[Alt · tt_movie_poster]`
  (→ the tooltip's five value cards, which carry it between them).
- **Build order matters:** `alt_text.py` runs *after* any page regeneration, because
  the page generator writes layout only. A re-run of the generator drops the alt text
  until the patcher is re-run; the validator catches it (`no altText`).

### Stage 6 phase B2b — layout.json vs handoff (p3 · tooltip)

Same rule as phase B2a: measured block rects win; the handoff supplies fonts,
decomposition and anything the prototype did not measure.

| Object | Handoff | Built (measured / resolved) |
|---|---|---|
| `z_p3_verdict_rule` | y 624 | y **632** (the measured verdict band's top border) |
| `c_verdict_act3` | 24,636,1040,56 | 24,**645**,1040,**44** |
| `btn_roll` | 1106,648,150,32 | **1113,649,143**,32 |
| `c_scatter_population` | 40,164,500,18 | **41,165**,**460**,25 — measured w 387 widened for the live `n`; the measured width is the prototype's placeholder string |
| `c_winner_label` | 498,248,336,50 | **455,271,380**,40 |
| `z_adj_chip_floor/_revenue/_m/_c` | y 167/195/223/251, h 22 | y **160/192/224/256**, h **25**; widths kept at the handoff's 132/132/104/104 because the measured spans are content-sized and the live chip strings must not truncate |
| `c_adj_*` labels | x 964, w 110/110/82/82 | x **963**, w = chip − 20 |
| `c_refusal_title` | 952,318,288,20 | 952,318,288,**25** |
| `c_refusal_why` | 952,342,288,32 | 952,**338**,288,**36** |
| `tbl_refusal_ranks` | 952,378,288,52 | 952,**372**,288,**80** (unhidable header + 3 rows; space from the omitted `@ build` line) |
| `c_nodate_chip` | 952,486,288,116 | 952,486,288,**118** — the measured 953,510,286,68 is the prototype's *vertically centred* text block; a PBIR card needs the card interior or it truncates a disclosure |
| p3 beat rail | 24/206/364, w 172/148/200 | **24/242/429**, w **208/177/184** — only the SC.3 screen was measured, so each width is the measured width plus the ●-prefix delta (13.8 px) observed on p1/p2; 10 px gutters |
| `img_tt_poster`, `c_tt_*` | as the handoff | measured rects used verbatim; the four tooltip rows are decomposed into label + value (+ mark on the weighted row) |
| p3 year read-out, `▶ PRESS PLAY`, the `@ build` line | prototype only | **accepted omissions** (asset-fidelity inventory #33, #34, #40) — the first two are native play-axis furniture and appear when the play well is filled |

### Stage 6 phase B2a — beat state lists (superseded by phase B2b; kept for the record)

Nine bookmarks, capture **Data OFF · Display ON · Current page ON · All visuals**.
"Chrome" below is visible in all three beats of its page.

**p1-act-i-profit — 43 visuals**

- *Chrome (all beats, 13):* `z_p1_header_title` · `z_p1_header_rule` · `btn_home` ·
  `btn_credits` · `z_p1_admit` · `btn_beat_1` · `btn_beat_2` · `btn_beat_3` ·
  `btn_next_scene` · `z_p1_verdict_rule` · `c_verdict_act1` · `c_verdict_act1_note` ·
  `btn_next_act`
- *Always-on content (7):* `c_p1_slug_naive` · `c_p1_action` · `c_p1_cue_naive` ·
  `c_p1_dlg_naive` · `z_kpi_profit_card` · `c_kpi_profit_kicker` ·
  `c_kpi_profit_label`
- *Beat marks:* `z_p1_beat1_mark` (b1 only) · `z_p1_beat2_mark` (b2 only) ·
  `z_p1_beat3_mark` (b3 only)
- *Notes block (6, b2 + b3):* `z_p1_note_rule_1` · `c_p1_note_zeros` ·
  `z_p1_note_rule_2` · `c_p1_note_budget` · `z_p1_note_rule_3` · `c_p1_note_negrev`
- *Correction block (2, b3 only):* `z_kpi_profit_strike` · `c_kpi_profit_misread`
- *Honest screenplay (4, b3 only):* `c_p1_trans` · `c_p1_slug_honest` ·
  `c_p1_cue_honest` · `c_p1_dlg_honest`
- *Waffle block (6, b3 only):* `z_waffle_card` · `c_waffle_kicker` · `c_waffle_title` ·
  `c_waffle_cap` · `dn_ticket_waffle` · `c_waffle_foot`
- *KPI variants:* `kpi_profit_naive` visible at **b1 + b2**, hidden at b3 ·
  `kpi_profit_naive_corrected` hidden at b1 + b2, visible at **b3**
- *Button state:* the current beat's button takes fill = `#2E4A7D`, text `#F5F2E9`
  and a leading `● `; the other two take fill off, 1 px `#211E1A` outline, ink text,
  no glyph. **Built state = SC.3.**

**p2-act-ii-ratings — 37 visuals**

- *Chrome (all beats, 12):* `z_p2_header_title` · `z_p2_header_rule` · `btn_home` ·
  `btn_credits` · `z_p2_admit` · `btn_beat_1` · `btn_beat_2` · `btn_beat_3` ·
  `btn_next_scene` · `z_p2_verdict_rule` · `c_verdict_act2` · `btn_next_act`
- *Always-on content (8):* `c_p2_slug_naive` · `c_p2_action` · `c_p2_cue_naive` ·
  `c_p2_dlg_naive` · `z_lb_card` · `c_lb_kicker` · `tbl_perfect_tens` · `c_lb_more`
- *Beat marks:* `z_p2_beat1_mark` (b1) · `z_p2_beat2_mark` (b2) · `z_p2_beat3_mark` (b3)
- *Notes block (6, b2 + b3):* `z_p2_note_rule_1` · `c_p2_note_twovotes` ·
  `z_p2_note_rule_2` · `c_p2_note_median` · `z_p2_note_rule_3` · `c_p2_note_twenty`
- *Honest screenplay + fall block (8, b3 only):* `c_p2_trans` · `c_p2_slug_honest` ·
  `c_p2_cue_honest` · `c_p2_dlg_honest` · `z_fall_card` · `c_fall_kicker` ·
  `c_fall_title` · `dn_rating_fall`
- p2 hides nothing at b3. **Built state = SC.3.**

### Stage 6 phase B2b — the built bookmarks (authoritative)

The nine files in `definition/bookmarks/` are now the record. Every bookmark lists
**every** visual on its page; the counts below are the hidden sets.

| Bookmark | Page | Visuals captured | Hidden |
|---|---|---|---|
| `bm_p1_b1` **(landing)** | p1-act-i-profit | 44 | 22 |
| `bm_p1_b2` | p1-act-i-profit | 44 | 16 |
| `bm_p1_b3` | p1-act-i-profit | 44 | 5 |
| `bm_p2_b1` **(landing)** | p2-act-ii-ratings | 38 | 17 |
| `bm_p2_b2` | p2-act-ii-ratings | 38 | 11 |
| `bm_p2_b3` | p2-act-ii-ratings | 38 | 4 |
| `bm_p3_b1` | p3-act-iii-corrected-cut | 37 | 6 |
| `bm_p3_b2` | p3-act-iii-corrected-cut | 37 | 6 |
| `bm_p3_b3` **(landing)** | p3-act-iii-corrected-cut | 37 | 7 |

Changes from the phase-B2a lists: each act page gained **`btn_next_scene_2`**; the
beat rail's next-scene pair and the three `z_pN_beatN_mark` shapes are toggled per
beat; p1/p2 land on **SC.1** and p3 on **SC.3** (the on-disk state equals the landing
bookmark, verified by script).

**p3-act-iii-corrected-cut — 37 visuals**

- *Chrome (all beats, 12):* `z_p3_header_title` · `z_p3_header_rule` · `btn_home` ·
  `btn_credits` · `z_p3_admit` · `btn_beat_1..3` · `z_p3_verdict_rule` ·
  `c_verdict_act3` · `btn_roll`
- *Always-on content (13):* `hero_premiere_scatter` · `c_scatter_population` ·
  the four chips and their four labels · `z_refusal_card` contents
  (`c_refusal_title`, `c_refusal_why`, `tbl_refusal_ranks`) · `z_nodate_card` ·
  `c_nodate_chip`
- *Paired variants:* `z_adjustments_card` ↔ `z_adjustments_card_lit` (lit at SC.1) ·
  `z_refusal_card` ↔ `z_refusal_card_lit` (lit at SC.2)
- *`z_p3_scrim`* visible at SC.1 + SC.2, hidden at SC.3 · *`c_winner_label`* hidden at
  SC.1 + SC.2, visible at SC.3
- *Rail:* `z_p3_beat{1,2,3}_mark` one per beat; `btn_next_scene` at SC.1,
  `btn_next_scene_2` at SC.2, neither at SC.3

## Manual steps required in Desktop

- [ ] Close Desktop **without saving** and reopen the pbip (Desktop currently
      holds pre-build state; saving would overwrite this build) — verify by:
      Date table shows range 1800–2099 in Power Query after reopen+refresh.
- [ ] Download Kaggle "TMDB Movies Dataset v11" CSV; set `SourceRoot`
      (Transform data → Edit parameters) to the folder containing
      `TMDB_movie_dataset_v11.csv` — verify by: successful refresh.
- [ ] Refresh to materialize `Release Year Key`, `Is Future Release`, the new
      Date range, and the `Release Year` table — verify by: `Release Year`
      shows 301 rows incl. "No date on record".
- [ ] Confirm Date is marked as date table (Table tools → Mark as date table
      = Date[Date]) — verify by: the marking dialog shows validated state.
- [ ] Confirm `SourceRoot` appears under Manage Parameters as Text; recreate
      under the same name if it surfaced as a plain query — verify by: Manage
      Parameters lists it.
- [x] ~~Spot-check a 06-Display stub in a card~~ — superseded 2026-08-05: the
      stubs are filled; see the phase-A spot-check below.

### New at stage 6 phase A (2026-08-05)

- [ ] **Confirm the custom theme is active** — the report already points at it on
      disk, so no `View → Themes → Browse` import should be needed. Verify by:
      opening the pbip and checking `View → Themes` shows **"D7 The Seductive Lies
      - A Trilogy"** as the current theme, with no base-theme regression banner. If
      Desktop ignores it, re-import
      `StaticResources/RegisteredResources/D7-Seductive-Lies.json` by hand and note
      here that the on-disk registration alone was insufficient.
- [ ] **Verify the 10 pt text-class floor took** — verify by: dropping a throwaway
      card and table on a blank page and confirming `label`, `smallLabel`,
      `lightLabel`, `smallLightLabel` and `smallDataLabel` all render at 10 pt.
      `smallDataLabel` is the uncertain one (emitted although Learn does not
      document it); if it did not take, raise it per visual in phase B.
- [ ] **Spot-check the filled display measures** — verify by: putting
      `[Title · Landing]`, `[Label · Method]` and `[Copy · Act I · naive read]` on
      cards and reading real numbers, not `"s5 fills value"` and not blanks. Record
      the **sign** of `[Profit (naive)]` here, because it decides which branch of
      `[Copy · Act I · naive read]` ships ("loses money" vs "prints money").
- [ ] **Set the data category for the poster field to "Image URL"** — the design
      contracts this as a Desktop step and it was **not** written into TMDL:
      `Measure.DataCategory` exists in TOM (the Learn API page resolves), but the
      TMDL serialisation name and the exact enum spelling for an image URL could not
      be verified this session, and research-first forbids guessing a property.
      Where: `[Image · Poster URL]` in `_Measures`, folder `06 Display`. Verify by:
      the `tbl_perfect_tens` poster column renders thumbnails rather than URL text.
      If Desktop writes the property, capture the exact TMDL line here so phase B
      can hold it in source.
- [ ] **Sanity-check one poster actually loads** — verify by: any perfect-ten row's
      thumbnail resolving over the network. If posters 404, the base URL is right
      but the size segment or the stored path is not; fall back to the contracted
      "no posters anywhere" route rather than guessing a different base.
- [ ] **Confirm `[Winner · title]` returns exactly one film** — it is a
      `TOPN(1, …)` over a composite rank and the design promises ties are listed,
      never broken silently. Verify by: a card showing `[Winner · title]` with no
      comma in it. A comma means a genuine tie and the p3 copy must be re-read
      with the designer.
- [ ] **VERIFY-AT-BUILD from the handoff, still open for phase B:** whether the
      installed Desktop build serialises a **textbox dynamic-value run** into PBIR.
      This decides the live-number mechanism for ~20 textboxes (preferred run →
      fallback A `cardVisual` → fallback B typed string). Verify by: authoring one
      textbox bound to `[Title · Landing]`, saving, and reading the resulting
      `visual.json`. Record the verdict here before phase B binds the rest.

### New at stage 6 phase B1 (2026-08-05) — verify these five tokens FIRST

Open the pbip and check these before phase B2 builds 3 more pages on the same
patterns. Each is a one-line fix if wrong; each fails visibly, not silently.

- [ ] **`cardVisual` role name.** Where: `hero_takeaway` (p0). Verify by: the card
      shows the Key Takeaway sentence. **If it is blank**, the role key `"Data"` in
      `query.queryState` is wrong — read the correct key off a card you drop by hand
      in Desktop and correct it in all 14 cards (p0 ×3, p9 ×11) before phase B2.
- [ ] **Button navigation.** Where: `btn_ticket_act1/2/3`, `btn_credits` (p0),
      `btn_home` (p9). Verify by: Ctrl-click each navigates. **If not**, the
      `visualLink.type` value `'PageNavigation'` is wrong. Note the ticket buttons
      target `p1-act-i-profit`, `p2-act-ii-ratings`, `p3-act-iii-corrected-cut`,
      which **do not exist until phase B2** — until then they are expected to fail.
- [ ] **Vertical ticket-stub text.** Where: `z_ticket1_admit` / `z_ticket1_serial`.
      Verify by: `ADMIT ONE` and `TMDB·2026·07·24` read bottom-to-top inside the
      stub. **If the text renders horizontally**, `textAngle: 270L` is wrong — try
      `-90`, else take the documented fallback.
- [ ] **Ticket corner radius.** Where: `z_ticket1_body`. Verify by: 8 px rounded
      corners, and every other surface square. **If the corners look wrong**, swap
      `rectangleRoundedByPixel` for `rectangleRounded`.
- [ ] **Centred text.** Where: `z_marquee_title`, `z_cr_title`, `c_cr_close_src`.
      Verify by: they are centred, not left-aligned. **If left**, the paragraph key
      `horizontalTextAlignment` is wrong for instances.

Also at phase B1:

- [ ] **Confirm the two pages open at 1280×720** with the night canvas `#171418`
      and that `p0-box-office` is the landing page.
- [ ] **Set the report-level filter `Movies[Adult] = FALSE`, then lock it and keep
      the filter pane visible.** Not written to disk: filter-lock properties could
      not be verified. Verify by: the pane shows a locked Adult filter and p9's
      BASIS row equals LISTINGS PER SOURCE minus ADULT TITLES EXCLUDED.
- [ ] **Read the p9 cross-foot and record the three numbers here** once the model
      is refreshed — they are the first live proof that the newer snapshot is
      flowing (expect roughly 85,870 − 1,360 = 84,510, per the coordinator's
      reconciliation; whatever the model says is the truth, and nothing is typed).
- [ ] **Check the tickets' paper tint contrast** on the cream ticket body:
      `#2E4A7D` / `#8A6516` / `#5B3E8E` on `#F5F2E9`. Verify by: the act numeral and
      serial are legible; Act II brass is the worst case at 4.74:1.

### New at stage 6 phase B2a (2026-08-05) — p1 · p2

- [ ] **Confirm both act pages open at 1280×720 on the paper canvas `#F5F2E9`** and
      that `p0`'s three ticket buttons now navigate (the ticket targets
      `p1-act-i-profit` and `p2-act-ii-ratings` exist as of this phase;
      `p3-act-iii-corrected-cut` still does not).
- [ ] **Check the two fallback charts render.** `dn_ticket_waffle`
      (`hundredPercentStackedBarChart`, no Category, two Y measures) should draw one
      full-width bar split green/gray with a bottom legend and a 0–100 % axis.
      `dn_rating_fall` (`clusteredBarChart`) should draw three film rows × two bars
      with a dashed `C = 6.96` reference line. **If either is blank**, the likely
      cause is a role name (`Y` / `Category` / `Tooltips`, taken from this repo's own
      Desktop-authored combo chart) — read the correct key off a chart dropped by
      hand and fix both files.
- [ ] **Check the two visual filters took.** `tbl_perfect_tens` and `dn_rating_fall`
      should each show **three** rows/categories, all at raw 10.0, fewest votes
      first. **More than three rows** = the `VisualTopN` filter did not apply
      (re-apply Top N by hand in the Filters pane and capture the JSON here).
      **Rows that are not 10.0** = the Advanced measure filter did not apply.
- [ ] **Check the reference line.** If `C = 6.96` does not appear on
      `dn_rating_fall`, the `referenceLine` selector id (`refC`) is the suspect —
      add the line in the Analytics pane and copy the id Desktop writes.
- [ ] **Check `tbl_perfect_tens` fits its 144 px card.** Native table headers cannot
      be hidden (see decisions), so the header eats one row. If a scrollbar appears,
      tune `grid.rowPadding` / `grid.imageHeight` / the five `columnWidth` values —
      do **not** shrink text below 10 pt.
- [ ] **Check the poster column.** Until `[Image · Poster URL]` gets the **Image URL**
      data category (still open from phase A), the first table column renders as URL
      text and will look wrong.
- [ ] **Check the beat rail reads at SC.3**: `btn_beat_3` filled Awards-Brass /
      Ledger-Indigo with cream text and a leading `●`, its 3 px underline
      (`z_pN_beat3_mark`) visible, the other two outlined in ink. Then confirm a
      bookmark capture with **Display ON** actually captures the button *fill* — if
      it does not, drive the current-beat indicator with the three `z_pN_beatN_mark`
      shapes (already built as separate, individually hideable objects) and swap the
      button text per beat.
- [ ] **Check `z_p1_admit` / `z_p2_admit`**: `ADMIT ONE` centred inside a 2 px
      tinted rectangle. If the text is not centred, `horizontalAlignment` /
      `verticalAlignment` on a shape's text card is wrong for instances.
- [ ] **Check the act-II brass on paper**: `#8A6516` on `#F5F2E9` is the worst-case
      contrast in the report (4.74:1) and carries the header rule, the beat fill,
      the verdict rule and `THE PREMIERE ▸`.
- [ ] **Read `[Profit (naive)]`'s sign off `kpi_profit_naive_corrected`** and record
      it here — it still decides which branch of `[Copy · Act I · naive read]` ships
      ("loses money" vs "prints money"), and the strike (`z_kpi_profit_strike`,
      811,230,308,2) is positioned for the measured value width. If the rendered
      number is wider or narrower, nudge the strike.

### New at stage 6 phase B2b (2026-08-05) — p3 · tooltip · bookmarks

- [ ] **THE PLAY AXIS — the one contracted feature that is not on disk.** Open
      `p3-act-iii-corrected-cut`, select `hero_premiere_scatter`, and drag
      `'Release Year'[Year Label]` into the **Play axis** well (sort it by
      `Year Sort`). Leave the play head on the **latest** year. The native year
      read-out and the `▶ PRESS PLAY` control appear with it — both are contracted as
      native furniture, not as custom objects. **Then save and read the resulting
      `visual.json`, and record the play-axis role key here** so the next build can
      hold it in source.
- [ ] **Confirm the scatter renders at all.** If it is blank, one of the role keys
      `Category` / `X` / `Y` is wrong — drop a scatter by hand, read the keys off its
      JSON, and correct `hero_premiere_scatter`. Also confirm the **X axis is
      logarithmic** and the dashed **`C = 6.96`** line is present.
- [ ] **Bind the two conditional colours** (`fx → Field value`), then capture the JSON
      here: `hero_premiere_scatter` → Data colors → `[Color · Scatter mark]` (this is
      what turns the winner dot good-green `#4ECBA0`); `tbl_perfect_tens` → the
      `Rating (raw)` column → `[Color · Rating verdict]`.
- [ ] **Test the nine bookmarks.** Open the Bookmarks pane: nine entries should be
      listed, grouped p1 → p2 → p3. Click each and confirm the beat state changes.
      **If the beat buttons do not change fill/label**, the `objects.merge` payload did
      not apply — the underline marks still show the current beat, and the fix is to
      re-capture the three bookmarks of that page by hand with
      **Data OFF / Display ON / Current page ON / All visuals**.
- [ ] **Test the rail wiring.** `SC.1/2/3` buttons and `NEXT SCENE ▸` should all
      navigate. **If nothing happens**, `visualLink.type` value `'Bookmark'` is wrong —
      read the correct value off a bookmark button created by hand.
- [ ] **Confirm the landing states**: p1 and p2 open on **SC.1** (naive cut, `[naive
      cut]` tag, beat 1 filled), p3 opens on **SC.3** (premiere, no scrim, winner
      label showing).
- [ ] **Test the tooltip.** Hover a `tbl_perfect_tens` row and a scatter point: the
      320 × 420 card should appear. **If it does not**, check
      `visualTooltip.type = 'Canvas'` / `section`. **If the poster box is empty**, the
      `image` visual's role key `"Values"` or its `sourceField` string is wrong —
      either fix it or delete `img_tt_poster` (the contracted fallback; the card reads
      without it).
- [ ] **Confirm `tt-movie-poster` is hidden** in the page tabs and does not appear in
      view mode.
- [ ] **Check `tbl_refusal_ranks` fits** its 288 × 80 box with five columns and an
      unhidable header; tune `columnWidth` if the `✕` or the rank numbers clip.
- [ ] **Read `[Winner · title]` once more** now that it drives both `c_winner_label`
      and `c_verdict_act3`: a comma means a genuine tie and the p3 copy must go back
      to the designer.
- [ ] **Spot-check the Act II ruling's numbers** on a card: `[Movies (perfect ten)]`,
      `[Movies (perfect ten, single vote)]` and `[Single-vote ten (illustration)]`
      (expect ≈ 6.99). Record them here — they are the first live proof of the ruling.
- [ ] **Check the Act III plum on night**: `#B79BE8` on `#171418` carries the header
      rule, the beat fill (with `#211E1A` text on the fill), the verdict rule,
      `NEXT SCENE ▸` and `ROLL CREDITS ▸`.

### New at stage 6 phase B2c (2026-08-05) — the alt-text layer

- [ ] **Optional but recommended: upgrade the 10 data visuals from static to live alt
      text.** Select the visual → Format → General → Alt text → `fx` → *Field value* →
      the matching measure in `06 Display\Alt text`. The pairs are:
      `kpi_profit_naive` → `[Alt · kpi_profit_naive · SC1]` ·
      `kpi_profit_naive_corrected` → `[Alt · kpi_profit_naive · SC3]` ·
      `dn_ticket_waffle` → `[Alt · dn_ticket_waffle]` ·
      `tbl_perfect_tens` → `[Alt · tbl_perfect_tens]` ·
      `dn_rating_fall` → `[Alt · dn_rating_fall]` ·
      `hero_premiere_scatter` → `[Alt · hero_premiere_scatter]` ·
      `tbl_refusal_ranks` → `[Alt · c_refusal_popularity]` ·
      `c_nodate_chip` → `[Alt · c_nodate_chip]` ·
      `c_cr_count_basis_val` → `[Alt · tbl_production_counts]` ·
      the tooltip's value cards → `[Alt · tt_movie_poster]`.
      **Capture the resulting JSON here** — it closes the last unverified binding
      shape in this report. Until then the static sentences are accurate and complete;
      they simply do not carry live figures.
- [ ] **Re-run `alt_text.py` after any page regeneration.** The page generator writes
      layout only; alt text is applied by a second pass. The structural validator
      fails loudly (`no altText`) if the order is missed.
- [ ] **Hand-test with a screen reader** (the accessibility judge does). Expected:
      chrome is silent; every card, table and chart states its finding; the beat
      buttons announce "Scene N of 3"; `kpi_profit_naive` announces "Trap exhibit"
      **before** the number is read.
- [ ] **The attribution debt is open, not closed.** `CREDITS.md` and
      `contracts/source-register.yaml` credit the influencing post *by publication*
      with its byline marked outstanding. A human must open the post in a browser and
      add the author's name. Do not remove or weaken those entries; do not adopt the
      post's DAX-UDF pattern until the name is recorded.

## Validation status

```
[2026-08-04]
validate_tmdl.py --strict : 15 file(s), 0 error(s), 0 warning(s)
pbip JSON                 : 32 file(s) well-formed, no BOM
tmdl_inventory            : 10 tables / 33 measures / 8 relationships

[2026-08-05 — stage 6 phase A]
validate_tmdl.py --strict : 15 file(s), 1 error(s), 0 warning(s)
                            the 1 error is the standing SourceRoot drive-letter
                            waiver in expressions.tmdl line 34 (waived
                            2026-08-04, see 04-model-build.md). It was present
                            before this phase and is unchanged by it. No other
                            error, no warning.
pbip JSON                 : 33 file(s) well-formed, no BOM (41 repo-wide, 0 err)
report.json               : 0 errors vs its declared report/3.3.0 schema
theme (installed copy)    : 0 errors vs reportThemeSchema-2.156 (Draft-7)
reference cross-check     : every [measure] and Table[Column] reference in
                            _Measures.tmdl resolves to a real object
tmdl_inventory            : 10 tables / 73 measures / 8 relationships
                            01 Core 4 · 02 Financials 6 (+1 Trap) ·
                            03 Ratings 14 · 04 Popularity 5 ·
                            05 Data health 9 · 06 Display 34 ·
                            06 Display\Alt text 0 (10 deferred)
pbir CLI                  : not installed on this machine — direct JSON editing
                            fallback used (per DEPENDENCIES.md)

[2026-08-05 — stage 6 phase B1]
validate_json.py          : 120 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings — TMDL was not touched in this phase
visualContainer structure : 77 new visual.json validated against the published
                            visualContainer/2.9.0 schema (name/position/required/
                            no stray top-level properties) — 0 errors
page schema               : p0-box-office + p9-end-credits validated against
                            page/2.1.0 — 0 errors
binding cross-check       : all 14 measure projections resolve to measures that
                            exist in _Measures.tmdl
layout cross-check        : every visual inside the 1280×720 canvas; no duplicate
                            ids; folder name == visual name on all 77
accessibility check       : p0 tab order == the handoff's 10 enumerated stops in
                            order; p9 reads top-to-bottom with each label stop
                            immediately before its value stop; no altText written
reserved-red check        : trap red appears only in c_cr_glossary's [TRAP] tag

[2026-08-05 — stage 6 phase B2a]
validate_json.py          : 202 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. TMDL touched this phase: one measure added
                            (Movies (no credible financials)); nothing else.
visualContainer structure : all 157 visual.json on the four built pages validated
                            against the published visualContainer/2.9.0 schema —
                            and this time DEEPLY: the remote sub-schemas were
                            resolved and applied too (visualConfiguration/2.3.0,
                            filterConfiguration/1.3.0, semanticQuery/1.4.0,
                            formattingObjectDefinitions/1.5.0). 0 errors.
                            Only relaxation: the $schema const (the files declare
                            2.11.0, matching every other visual.json Desktop wrote
                            for this report; 2.11.0 itself is 404).
page schema               : p1-act-i-profit + p2-act-ii-ratings validated against
                            page/2.1.0 — 0 errors
pages registry            : pages.json validated against pagesMetadata/1.1.0 —
                            0 errors; order p0, p1, p2, <2 starters>, p9
binding cross-check       : every measure and Table[Column] projection AND every
                            filter field on all four pages resolves to a real
                            object in the model — 0 dangling references
layout cross-check        : every visual inside the 1280x720 canvas; no duplicate
                            ids; folder name == visual name on all 157
accessibility check       : p1 and p2 contain the handoff's enumerated tab order
                            exactly as a subsequence (31 and 26 stops vs 23 and 22
                            enumerated — see finding 4); no text below 10 pt;
                            no altText written anywhere
scope-rule check          : 0 act-tinted data marks across all four pages
reserved-red check        : trap red confined to the reserved set (slug tags, the
                            strike, MISREAD, the 3 note rules + notes, the
                            leaderboard score/verdict columns, the raw-rating bar)
                            plus p9's [TRAP] glossary tag — 0 violations
snapshot cross-check      : min budget $1 and the single −$12 revenue row verified
                            against the loaded CSV; the contracted $2,800 median
                            was NOT verified (actual $2,961) and was dropped

[2026-08-05 — stage 6 phase B2b]
validate_json.py          : 267 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. TMDL touched: 5 measures added, 2 edited
                            in place (expression + docstring only)
visualContainer structure : all 210 visual.json on the six built pages validated
                            DEEPLY against visualContainer/2.9.0 with its remote
                            sub-schemas resolved (visualConfiguration/2.3.0,
                            filterConfiguration/1.3.0, semanticQuery/1.4.0,
                            formattingObjectDefinitions/1.5.0) — 0 errors
page schema               : all six pages vs page/2.1.0 — 0 errors, incl. the
                            tooltip page's type / visibility / pageBinding
pages registry            : pages.json vs pagesMetadata/1.1.0 — 0 errors; the
                            registry and the pages/ folders match exactly
bookmark schema           : 9 files vs bookmark/2.1.0 — 0 errors;
                            bookmarks.json vs bookmarksMetadata/1.0.0 — 0 errors
bookmark completeness     : every bookmark captures every visual of its page
                            (44/38/37) — 0 missing, 0 unknown
landing-state check       : each act page's on-disk isHidden set is byte-identical
                            to its landing bookmark's hidden set (p1 b1, p2 b1,
                            p3 b3)
link cross-check          : every visualLink bookmark name, every navigationSection
                            page name and every visualTooltip section resolves to a
                            real bookmark/page — 0 dangling
binding cross-check       : every measure, column, aggregation, sort field and
                            filter field on all six pages resolves — 0 dangling
layout cross-check        : every visual inside its page canvas (1280x720, and
                            320x420 on the tooltip); no duplicate ids; folder
                            name == visual name on all 210
accessibility check       : the handoff's enumerated tab order is present as an
                            exact subsequence on p1, p2 and p3; no text below
                            10 pt anywhere; no altText written anywhere
scope-rule check          : 0 act-tinted data marks across all six pages
reserved-red check        : trap red confined to the reserved set — Act I/II slug
                            tags, strike, MISREAD, note rules + notes, leaderboard
                            score/verdict columns, the raw-rating bar, the p3
                            refusal card + its title + its divergence column, the
                            tooltip's raw-rating value, and p9's [TRAP] tag.
                            Navigation (NEXT SCENE / NEXT ACT / THE PREMIERE /
                            ROLL CREDITS) is act tint; btn_home / btn_credits ink

[2026-08-05 — stage 6 phase B2c, the alt-text layer]
validate_json.py          : 267 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. 89 measures, 10 of them in the new
                            06 Display\\Alt text folder
visualContainer structure : all 210 visual.json re-validated DEEPLY against
                            visualContainer/2.9.0 with remote sub-schemas
                            resolved — 0 errors
alt-text coverage         : 76 content + 73 empty-decorative + 61 textboxes left
                            unset = 210. The check now FAILS if a non-textbox
                            visual has no altText, if decorative chrome carries a
                            non-empty string, or if a content string is too short
                            to state a finding. 0 failures
alt-text waiting list     : CLOSED — every visual on it carries alt text
volatile-count check      : no static alt string contains a snapshot-dependent
                            count; only $10,000, m = 100, C = 6.96, 24 July 2026
                            and the derived 6.99 appear as literals
bookmark / link / binding / layout / scope-rule / reserved-red checks : unchanged
                            from phase B2b, all still 0 errors
```

## Known limitations

- New M columns, the widened Date range, and the Release Year table exist in
  TMDL only until the next refresh — the source CSV is not on this machine.
- `Profit (naive)` is a deliberate trap exhibit (Lie #1): it treats unknown
  financials as $0 and must never appear without its trap marking (s5/s6
  enforce the presentation).
- Financials are nominal, currency-unverified ("USD assumed"); popularity has
  no published definition — see blueprint §7 "metrics NOT available".
- ~~Alt text is missing report-wide~~ — **resolved 2026-08-05.** Every visual now
  carries alt text (76 content, 73 empty-decorative, 61 textboxes reading their own
  copy). **The remaining limitation is that the strings are static**, so they state
  the finding and the disclosed parameters but do not read live figures; the ten
  measures that would are authored and one Desktop step away. The **attribution debt
  is open**: the influencing post is credited by publication, its byline outstanding.
- No measure has been **executed** in this phase. The measures are authored,
  cross-referenced and lint-clean, but Desktop was closed and the model was not
  refreshed, so no value in the report has yet been read out of the model. Every
  number in the built report is bound to a measure rather than typed, so nothing is
  wrong — but the placeholder batch in `data-model.md` is only truly resolved once
  the spot-checks above are done.
- The custom theme is registered on disk but has **never been rendered** by
  Desktop in this repo; the theme-notes list in `design-handoff.md` names several
  properties (notably `smallDataLabel`) whose effect is unverified by anyone.
- **Nothing built in phase B1 has been rendered either.** 77 visuals are
  schema-correct and internally consistent, but no pixel has been seen. The five
  unverified tokens above are the concrete places where "schema-correct" and
  "renders as designed" could still diverge.
- **Letter-spacing is absent report-wide** (PBIR cannot express it). The marquee
  and the section heads will read tighter than the prototype.
- **p9 has 35 tab stops where the design enumerated 14**, because the two credits
  tables are built as label/value pairs rather than one table visual each. The
  reading order is correct and every value is preceded by its label, but a judge
  counting stops against the design document will see the difference.
- The ticket perforation is **solid, not dashed** — a contracted fallback, taken
  because PBIR shapes have no dash property.
- **Neither Deneb visual is Deneb.** `dn_ticket_waffle` is a 100 % stacked bar and
  `dn_rating_fall` is a paired bar chart — both are the contracted fallbacks, both
  keep their ids and rects, and neither is the "felt proportion" the waffle promised.
  The 100-ticket metaphor (the signature moment of Act I) is **not in the shipped
  report**; the proportion is stated numerically by `[Copy · Act I · waffle title]`
  and shown as one split bar.
- **`tbl_perfect_tens` shows its column headers** and uses one font family for all
  columns — both are limits of the native table visual, not choices.
- **Nothing built in phase B2a has been rendered either.** The two pages are
  schema-correct (deeply, against four published schemas) and every binding resolves,
  but no pixel has been seen and no measure has been executed. The phase-B2a Desktop
  checklist above lists every place where "schema-correct" and "renders as designed"
  could still diverge — the chart role names, the two visual filters, the reference
  line, the table's fit, and whether a bookmark's Display capture carries a button's
  fill colour.
- ~~p1 and p2 are built in their SC.3 state~~ — resolved at phase B2b: the nine
  bookmarks exist, the rail is wired, and p1/p2 land on SC.1 with p3 on SC.3.
- **The play axis is not on disk** — the single largest gap between the contract and
  the shipped file. The Act III animation, its year read-out and its `▶ PRESS PLAY`
  control all appear only after one drag in Desktop (first item on the phase-B2b
  checklist). Until then the scatter is a static premiere and `[Label · No date]`'s
  phrase "they never enter this animation" is describing something the reader cannot
  yet see.
- **The winner dot is not green.** `[Color · Scatter mark]` and
  `[Color · Rating verdict]` are unbound because the fx-field-value serialisation could
  not be verified; the winner is carried by `c_winner_label`'s `✓` and words instead.
  Two Desktop bindings close this.
- **`Two-vote ten (illustration)` and `Godfather rating (reference)` are now unused**
  by any visual after the Act II ruling. They are retained, not deleted — nothing
  dangles, but a reader of the model will find two measures no page consumes.
- **Nothing built at stage 6 has been rendered.** 210 visuals and 9 bookmarks are
  schema-correct against eight published schemas and every binding resolves, but no
  pixel has been seen and no measure executed. Eleven tokens across phases B1 and B2b
  are the concrete places where "schema-correct" and "renders as designed" can still
  diverge; each is on the Desktop checklist and each fails visibly.
