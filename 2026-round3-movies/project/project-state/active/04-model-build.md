# 04 — Model build (stage 4, built 2026-08-04)

Built by pbir-operator, exactly per `03-model-blueprint.md` §9 build order.
Validators green at close: `validate_tmdl.py --strict` = 15 files, **0 errors,
0 warnings**; all 32 report/model JSON files well-formed, UTF-8 without BOM.
Desktop had the pbip open during the build — disk-only edits; the user must
close-without-saving and reopen (follow-ups below).

## What was built, per build-order step

1. **SourceRoot parameter + expression rewrites** (`definition/expressions.tmdl`)
   — new shared expression `SourceRoot` (text parameter, default `<set-me>\TMDB`);
   both hardcoded `C:\Users\shlindsay\...` paths in `Source` (was line 5) and
   `Schema` (was line 21) rewritten to
   `File.Contents(SourceRoot & "\TMDB_movie_dataset_v11.csv")`. Cleared both
   validator errors. `SourceRoot` added to `PBI_QueryOrder` in `model.tmdl`.
2. **Date table** (`definition/tables/Date.tmdl`) — partition M rewritten to
   deterministic `List.Dates` over **1800-01-01..2099-12-31** (verified min/max
   Release Date; no `DateTime.LocalNow()`); columns and their names unchanged
   (Date, Week Number, Month Number, Month Name, Year). Marked as date table:
   `dataCategory: Time` on the table + `isKey` on `Date[Date]` — syntax verified
   this session against Microsoft Learn TOM docs (`Table.DataCategory` value
   `Time`; `Column.IsKey`). `Month Name` now `sortByColumn: 'Month Number'`.
3. **Movies** (`definition/tables/Movies.tmdl`) — partition M steps added:
   `Release Year Key` (Date.Year of Release Date, null → −1, Int64, hidden
   column) and `Is Future Release` (Release Date > `#date(2026, 7, 24)`, null →
   false, Boolean). Column hygiene: `summarizeBy: none` on Vote Average, Vote
   Count, Revenue, Budget, Runtime, Popularity (with `SummarizationSetBy = User`
   so Desktop keeps the choice); Budget/Revenue formatString normalized to
   `\$#,0;(\$#,0)`. **New M columns materialize only at next refresh** — the CSV
   is not on this machine (verified); TMDL is complete and refresh-ready.
4. **Release Year dimension** (`definition/tables/Release Year.tmdl`, new) —
   M-generated per blueprint §4: `Year Key` (int, −1 unknown member, hidden),
   `Year Label` (text, "No date on record" for −1, sorted by `Year Sort`),
   `Year Sort` (int, unknown sorts last, hidden), `Year Status` (Past / Current
   / Future / No date vs anchor year 2026). `queryGroup: Dimensions`. Registered
   in `model.tmdl` (ref + query order). **Relationship #8** added:
   `Movies[Release Year Key]` *:1 `'Release Year'[Year Key]`, single direction
   (TMDL defaults), name `Movies_ReleaseYearKey_to_ReleaseYear_YearKey`.
5. **Profit trap** — starter measure renamed to `Profit (naive)`; DAX formula
   byte-identical (`SUM(Movies[Revenue]) - SUM(Movies[Budget])`); lineageTag
   preserved; trap docstring added; displayFolder
   `02 Lie 1 · Financials\Trap — kept as exhibit`; formatString normalized to
   `\$#,0;(\$#,0)`. **Routed question 5 resolved: same-batch binding update** —
   the one starter visual binding `[Profit]`
   (`…Report/definition/pages/22a73d6058ce40e505e0/visuals/e21488a8d900077091bd/visual.json`)
   updated in the same batch (projection, sort, filter, queryRef,
   nativeQueryRef); zero dangling `"Profit"` references confirmed by scan.
6. **`_Measures` build-out** — 32 new measures, every §5 row, each with `///`
   docstring, explicit formatString, and numbered displayFolder exactly per the
   taxonomy (01 Core ×3; 02 Lie 1 · Financials ×3 + kept trap; 03 Lie 2 ·
   Ratings ×8; 04 Lie 3 · Popularity ×4; 05 Data health · Time ×6; 06 Display
   ×8 stubs). Layering holds: base measures touch columns; everything else
   references measures. Duplicate-ID tolerance: `Popularity (as-is)` guards with
   HASONEVALUE + MAX; all RANKX measures rank over `ALLSELECTED(Movies[Movie
   ID])` with `CALCULATE(MAX/SUM(...))` per ID, so the 101 dup-ID rows collapse
   per ID instead of erroring; ALLSELECTED usage commented in-DAX per
   dax-patterns.

## Decisions and assumptions (none contradict the blueprint)

- **SourceRoot default is `<set-me>\TMDB`, not a drive-letter path.** The
  validator/hook errors on any `X:\` literal (hard floor); the blueprint only
  requires "placeholder default, never a committed user path". A drive-letter
  placeholder would have re-introduced the error the step exists to clear.
  Note: once the entrant sets a real local path, their local expressions.tmdl
  will carry a machine path — local-only state, not for commit.
- **Parameter meta record** `meta [IsParameterQuery=true, Type="Text",
  IsParameterQueryRequired=true]` is the Desktop serialization convention; the
  exact field names were not re-verifiable against reachable docs this session.
  Conservative by construction: M's `meta` is value-preserving, so worst case
  SourceRoot behaves as a plain text query and the parameterization still works.
  Desktop confirmation is in the follow-ups.
- **Measure count 33 vs "~28"** — blueprint arithmetic approximation; amendment
  note written into §9 of the blueprint. No scope added.
- **`formatString: @` on the eight 06-Display text measures** — tmdl-style
  demands an explicit formatString on every measure; `@` is the standard text
  placeholder token. Desktop normally leaves text measures format-less, so
  verify in Desktop (follow-ups).
- **`VAR m` readability variable** in `Rating (evidence-weighted)` — identical
  semantics to the blueprint's sketch, per dax-patterns VAR discipline.
- **`Rank · Revenue`** implements "Revenue > 0 only" as: rank population =
  revenue-known listings within the viewer's selection; BLANK for listings
  whose revenue is unknown (no rank fabricated from a 0).
- **Relationship #8 has a human-readable name** (new object; readable diffs).
  All existing Desktop hash identifiers untouched.
- **`SummarizationSetBy = User` / `changedProperty`** written where properties
  were deliberately set, so Desktop treats them as user choices and does not
  re-infer implicit aggregations.
- Display-stub value is the literal text `"s5 fills value"` — obviously
  unfinished by design; s5 supplies real values via the design contract.

## Inventory vs blueprint gate targets

`tmdl_inventory.py` (2026-08-04): **10 tables** (target 10 ✓), **8
relationships** (target 8 ✓), **33 measures** (target ~28 — see §9 build note
✓), **Movies 19 columns** (17 + 2 new ✓), **SourceRoot** shared expression
present (✓; the script's headline "1 shared expression" counts only the
file-head expression — `EXPR_RE` lacks `re.M` — actual count is 3: SourceRoot,
Source, Schema). `validate_tmdl.py --strict`: 0 errors, 0 warnings (was 2 + 2
at baseline).

## Desktop follow-ups (user checklist)

- [ ] (a) Close Power BI Desktop **without saving**, then reopen the pbip —
      Desktop currently holds the pre-build state in memory and would overwrite
      this build on save.
- [ ] (b) Download the Kaggle "TMDB Movies Dataset v11" CSV (not on this
      machine — verified) and set `SourceRoot` to its folder (Transform data →
      Edit parameters). The file must be named `TMDB_movie_dataset_v11.csv`
      inside that folder. Do not commit the local path.
- [ ] (c) Refresh to materialize: `Movies[Release Year Key]`,
      `Movies[Is Future Release]`, the 1800–2099 Date range, and the
      `Release Year` table.
- [ ] (d) Confirm Date is marked as date table (Table tools → Mark as date
      table shows Date[Date]) — TMDL marking verified against TOM docs, but a
      Desktop-side confirmation closes the loop.
- [ ] (e) Confirm `SourceRoot` appears under Manage Parameters as a Text
      parameter; if it shows as a plain query, recreate it via Manage
      Parameters under the same name (value semantics identical).
- [ ] (f) Spot-check one 06-Display measure in a card: it should render the
      text "s5 fills value" (confirms the `@` format behaves).

## Post-refresh close-out (2026-08-04, after user follow-ups)

Entrant completed (a)–(c): CSV placed at `project\data\TMDB_movie_dataset_v11.csv`
(added to .gitignore), `SourceRoot` set, refresh run, saved from Desktop.
Desktop's TMDL round-trip: SourceRoot block moved to file end with the real
value + a `Navigatie` annotation (Dutch UI); trailing-newline churn on
Release Year.tmdl. All benign — accepted as-is.

**STANDING WAIVER (entrant, 2026-08-04):** the committed `SourceRoot` value is
a drive-letter path (`E:\PowerBI Set-up\wc-round-3\project\data\`), which
`validate_tmdl --strict` flags as its one error. Waived standing by the
entrant: it is the working local value, Desktop rewrites it on every save, the
path is the repo's own data folder, and no client-identifiable content is
involved. G6/G7 sweeps cite this waiver; expected steady-state is exactly
1 error at expressions.tmdl (SourceRoot line) and no others. Framework
feedback (for the template repo): the validator needs an allowlist mechanism
for the active source parameter's local value.

**Verify at s6 entry (Desktop open + MCP):** `Genres` and `Production Company`
came back from the round-trip with `PBI_ResultType = Exception` annotations —
possibly a transient pre-parameter preview error, but confirm both tables
have plausible row counts after refresh before building on them.

## Open questions

None new. Routed question 5 (Profit rename vs starter binding) resolved above:
same-batch binding update, nothing dangles.

## REBUILD CHECKPOINT 1 — model deltas (2026-08-05, pbir-operator)

Authority: the approved rebuild plan `i-told-you-i-giggly-castle.md`. The
verified contest question is **"What makes a movie successful?"** and the story
now leads with the answer, so the model gains the objects that answer it. Scope
here is the **semantic model only**; the theme and `report.json` deltas from the
same checkpoint are logged in `06-report-build.md`.

### What was added

- **`Movies[Budget Band]` + `[Budget Band Sort]`** — `Below floor` under the
  disclosed $10,000 floor, then `$10k–100k` / `$100k–1M` / `$1M–10M` /
  `$10M–50M` / `$50M–100M` / `$100M+`. The band is only meaningful above the
  floor, so sub-floor rows are **labelled**, never binned as if their budget
  were known.
- **`Movies[Vote Band]` + `[Vote Band Sort]`** — `0` / `1–9` / `10–99` /
  `100–999` / `1,000+`.
- **`'Release Year'[Decade]` + `[Decade Sort]`** — decade labels, with the −1
  unknown member carried through as **"No date on record"** and sorted last at
  2100 (the convention `Year Sort` already uses). The dateless 30.8% stay
  first-class on an era axis.
- **`Counts`** (8 rows) and **`Parameters`** (4 rows) — calculated tables, both
  `ref`'d in `model.tmdl`. `Counts` supplies only the row *labels* of the method
  page's cross-foot; the values come from `[Value · Count line]`, which
  dispatches to the measure that already owns each count.
- **24 measures** (90 → 114) and **5 measure-body rewrites** with names and
  `lineageTag`s preserved. Full inventory in `BUILD_LOG.md`.

### Decisions taken here

- **`Counts` and `Parameters` are deliberately unrelated to `Movies`.** The
  star-schema rule wants that in writing: they are presentation/disclosure axes,
  not dimensions, and a relationship would filter the fact table meaninglessly.
- **No measure was added without a consumer named in the plan** — the entrant's
  "a builder doesn't put nails where they don't need", applied to the model.
- **`Share · money` / `Share · evidence` are aliases** of `Financial coverage %`
  / `Evidence share %` rather than second `DIVIDE`s, keeping one calculation in
  one home while giving the answer page its own `Share ·` vocabulary.
- **No parameter changed.** The floor ($10,000), m (100), C (6.96) and the
  snapshot anchor (2026-07-24) are exactly as signed at G2/G3; `Parameters` only
  *prints* them alongside their derivation and robustness.

### Research-first note

Neither a calculated column nor a `DATATABLE` calculated table existed anywhere
in this model, so the syntax could not be settled against it. It was verified
against Microsoft-authored TMDL in `microsoft/Analysis-Services`
(`pbidevmode/fabricps-pbip/SamplePBIP/`): `Calendar.tmdl` for the calculated
column form, `Dynamic Measure.tmdl` for the `DATATABLE` calculated table,
`Parameter - Dimension.tmdl` for the multi-line `calculated` partition body.
`PBI_Id` was omitted rather than invented — Desktop writes it on save.

### Validation at close

`validate_tmdl.py --strict`: 17 files, **1 error, 0 warnings** — the error is the
standing SourceRoot drive-letter waiver at `expressions.tmdl:34`, i.e. the
expected steady state. Reference integrity checked mechanically: every
`[measure]` and `Table[Column]` reference in `_Measures.tmdl` resolves. All 90
pre-existing measures present, 0 `lineageTag`s changed.

### Open questions

- **Gate not yet met: the six snapshot numbers are unreproduced.** The
  calculated columns and tables are definitions on disk; they materialise only
  when the entrant refreshes in Desktop. Until then nothing binding to
  `Movies[Budget Band]`, `Movies[Vote Band]`, `'Release Year'[Decade]`, `Counts`
  or `Parameters` can be checked. **This blocks report work per the plan's
  checkpoint-1 gate.**
- `[Winner · title]` returns a comma-joined list on ties. `Title · Landing`'s
  50-word guard has two frames (38-word and 33-word); a tie long enough to blow
  50 words even on the short frame would need a copy decision, not a third
  branch. No tie is expected with the current data — recorded so it is not a
  surprise later.
