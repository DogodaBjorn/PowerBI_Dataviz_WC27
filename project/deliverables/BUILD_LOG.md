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
Report: starter pages untouched; the D7 custom theme is installed and active.
Page/visual authoring is stage 6 **phase B**.

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
