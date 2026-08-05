# BUILD_LOG — World Champs BCN 26 — Round 3

<!-- Maintained DURING stages 4 and 6 by the build-log skill. A reader who
never saw the chat must learn from this file: what exists, what remains
manual, which numbers rest on assumptions, when it was last validated. -->

Last validated: 2026-08-05 — `validate_tmdl.py --strict`: 15 files, **1 error**
(the standing `SourceRoot` drive-letter waiver, see 04-model-build.md), 0
warnings; 33 pbip JSON files well-formed, UTF-8 without BOM (41 repo-wide, 0
errors); `report.json` 0 errors against its declared `report/3.3.0` schema.
Model: 10 tables, **73 measures**, 8 relationships, 3 shared expressions
(SourceRoot parameter, Source, Schema). Ten further measures (the
`06 Display\Alt text` family) are **deferred** — see *Deferred*.
Report: the D7 custom theme is installed and active; **p0-box-office (42 visuals)
and p9-end-credits (35 visuals)** are built. The two starter pages are untouched.
p1/p2/p3 and the tooltip page are stage 6 **phase B2**.

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

## Deferred — not built, and why

- **`06 Display\Alt text` — the 10 `Alt · …` measures (BLOCKER, attribution).**
  `Alt · kpi_profit_naive · SC1` · `Alt · kpi_profit_naive · SC3` ·
  `Alt · dn_ticket_waffle` · `Alt · tbl_perfect_tens` · `Alt · dn_rating_fall` ·
  `Alt · hero_premiere_scatter` · `Alt · c_refusal_popularity` ·
  `Alt · c_nodate_chip` · `Alt · tbl_production_counts` · `Alt · tt_movie_poster`.
  The dynamic-alt-text technique comes from the Fabric Community post
  *"Accessibility in Action: Building Reusable Alternative Text Logic"* supplied by
  the entrant; the author's name is not retrievable by an agent (the community site
  answers 403). Attribution rule 5 makes shipping an uncredited adopted technique a
  **blocker-severity defect**, so the family is not implemented.
  **To unblock:** open the post in a browser, read the author's name, add them to
  `contracts/source-register.yaml` **and** `CREDITS.md`, then implement the ten
  measures (expressions are ready in `measures.dax`) in folder
  `06 Display\Alt text`, format `@`.
  **Consequence if it stays blocked:** every data visual loses its live-number alt
  text, which is the accessibility judge's hand-tested surface (05-design.md,
  finding 1). No other measure depends on this family, so nothing dangles today.
- Nothing else from `measures.dax` was deferred. `Image · Poster URL` **was** built
  — its VERIFY-AT-BUILD base URL was retrieved successfully (see below).
- **Alt text on every p0/p9 visual is intentionally UNSET** (not empty-string, not
  a typed sentence) pending the same attribution blocker. Verified by a build check
  that fails if the token `altText` appears in any generated `visual.json`.
  **Visuals awaiting alt text once unblocked:** p0 — `hero_takeaway`,
  `z_billing_method`, `z_billing_caveats`, `btn_ticket_act1/2/3` (the ticket teaser
  stat lives in the button's alt text per the handoff); p9 — the 11 measure-bound
  value cards. Decorative chrome (frames, rules, perforations, ticket internals)
  must receive **empty** alt text at the same time, per the accessibility package.
  **The property path is now verified** — see the phase-B1 decisions below — so this
  is a pure attribution hold, no longer a research question.
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
```

## Known limitations

- New M columns, the widened Date range, and the Release Year table exist in
  TMDL only until the next refresh — the source CSV is not on this machine.
- `Profit (naive)` is a deliberate trap exhibit (Lie #1): it treats unknown
  financials as $0 and must never appear without its trap marking (s5/s6
  enforce the presentation).
- Financials are nominal, currency-unverified ("USD assumed"); popularity has
  no published definition — see blueprint §7 "metrics NOT available".
- **Alt text is missing report-wide** until the attribution blocker above is
  cleared. This is user-visible to exactly the reader the accessibility judge
  represents: a screen-reader user gets no narration for any data visual. It is a
  deliberate hold, not an oversight.
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
