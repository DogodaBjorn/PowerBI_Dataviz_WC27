# 03 — Model blueprint (stage 3, drafted 2026-08-04)

Starter model inventoried 2026-08-04 (`python scripts/tmdl_inventory.py`: 9 tables,
7 relationships, 1 measure, 1 shared expression; `validate_tmdl --strict`: 2 errors —
machine paths in expressions.tmdl lines 5 and 21 — plus 2 warnings on the Profit
measure). Design serves Angle 3 ("Three seductive lies"), metric contracts
M-001..M-007, and the entrant's over-time seed (02-metrics.md, F5). Deltas only —
express lifecycle; every KEEP below is a verified fact, not an assumption.
Drafted by model-auditor; written by main thread (auditor is read-only).

## 1. Grain declarations (first, per doctrine)

- **Movies** (fact) — ONE ROW MEANS: one TMDB movie *listing* (one `Movie ID`) from
  the contest starter's load, which keeps only rows with a populated `budget > 0`
  (filter is in the starter's own M partition — this is why the table is 85,394
  rows, not ~930k). `Movie ID` uniqueness is assumed (TMDB primary key) but not
  enforced by any relationship in the current model (the bridge relationships are
  declared m:m) — s4 verifies with `COUNTROWS` vs `DISTINCTCOUNT`. 2.0% of rows
  share a (Title, Release Date) pair across distinct IDs, so the word is
  "listings", never "films", where precision matters (M-001).
- **Genre Bridge** (factless bridge) — ONE ROW MEANS: one (movie listing, genre)
  assignment parsed from the raw CSV's comma-separated `genres` field. Built from
  the UNFILTERED `Source` expression: it contains Movie IDs that do not exist in
  the loaded Movies table (harmless for filtering; do not count bridge rows as
  assignments of loaded movies).
- **Keyword Bridge** (factless bridge) — ONE ROW MEANS: one (movie listing,
  keyword) assignment, same construction and same unfiltered-source caveat.
- **Production Company Bridge** (factless bridge) — ONE ROW MEANS: one (movie
  listing, production company) credit, same construction and caveat.

Dimension grains: **Genres** — one row per distinct genre string; **Keyword** — one
row per distinct keyword string; **Production Company** — one row per distinct
company string (all three parsed from the unfiltered source, so they may carry
members with zero loaded movies). **Date** — one row per calendar day. **Release
Year** (ADD) — one row per release-year bucket, including one explicit
"No date on record" member (key −1); year buckets cover the full span of the data
including future years.

## 2. Target star schema

```
   Genres (KEEP)         Keyword (KEEP)        Production Company (KEEP)
      │ 1                   │ 1                     │ 1
      ▼ *                   ▼ *                     ▼ *
  Genre Bridge (KEEP)   Keyword Bridge (KEEP)  Production Company Bridge (KEEP)
      │                     │                       │
      └──── m:m weak, single (bridge filters Movies) ────┐
                                                         ▼
                    MOVIES  (fact — KEEP; hygiene CHANGEs + 2 ADD columns)
                      │ *                          │ *
        Release Date  ▼ 1                          ▼ 1   Release Year Key (ADD)
              Date (CHANGE: range, mark,      Release Year (ADD: unknown member,
              determinism, sort)              year status, sort)

                    _Measures (CHANGE: taxonomy + ~28 measures; Profit KEPT as exhibit)
```

ADD: `Release Year` dim, `Movies[Release Year Key]`, `Movies[Is Future Release]`,
`SourceRoot` parameter. CHANGE: Date partition + marking, `_Measures` build-out,
Movies column hygiene, expressions parameterization. KEEP: all 9 starter tables,
all 7 starter relationships (identifiers untouched — Desktop hash names stay, per
mutation safety), the Movies `budget > 0` load filter (the signed Q2 numbers are
of this 85,394-row subset; changing the load scope would invalidate the glossary),
the `Facts` / `Dimensions` / `Bridge Tables` queryGroups.

## 3. Relationship audit (verified in relationships.tmdl)

| # | From | To | Declared | Direction (verified default) | Verdict |
|---|---|---|---|---|---|
| 1 | Production Company Bridge[Production Company ID] | Production Company[Production Company ID] | m:1 (defaults) | single; dim filters bridge | KEEP |
| 2 | Genre Bridge[Genre ID] | Genres[Genre ID] | m:1 (defaults) | single; dim filters bridge | KEEP |
| 3 | Keyword Bridge[Keyword ID] | Keyword[Keyword ID] | m:1 (defaults) | single; dim filters bridge | KEEP |
| 4 | Movies[Movie ID] | Genre Bridge[Movie ID] | `toCardinality: many` ⇒ **m:m weak** (fromCardinality stays default many) | single; TOM one-direction flows To→From ⇒ bridge filters Movies | KEEP w/ justification |
| 5 | Movies[Movie ID] | Keyword Bridge[Movie ID] | m:m weak | single; bridge filters Movies | KEEP w/ justification |
| 6 | Movies[Movie ID] | Production Company Bridge[Movie ID] | m:m weak | single; bridge filters Movies | KEEP w/ justification |
| 7 | Movies[Release Date] | Date[Date] | m:1 (defaults) | single; Date filters Movies | KEEP (Date table itself CHANGEs, §4) |

**Doctrine call on 4–6.** No bidirectional filters anywhere (clean against the
star-schema rule). The m:m weak declaration does discard the known uniqueness of
`Movies[Movie ID]`; the doctrine-pure alternative is 1:* (Movies one-side) with a
bidirectional cross-filter on the bridge leg — the standard bridge pattern (Kimball,
multivalued dimensions; SQLBI, many-to-many patterns — see source register). Both
give identical filter semantics for every metric in this report (dimension → bridge
→ Movies). The only capability lost by the current design is fact→dimension
propagation (e.g. "distinct genres among credible films"), which no M-metric or
planned page needs. Decision: **KEEP as-is, this paragraph is the written
justification** — rebuilding working starter relationships days before deadline is
risk without benefit. No snowflakes exist. One path per fact–dimension pair; no
ambiguity. ADD relationship #8: `Movies[Release Year Key]` *:1
`'Release Year'[Year Key]`, single direction, dim filters fact.

## 4. Date dimension — current vs required

**Current (verified in Date.tmdl):** M-generated `List.Dates` from 1937-01-01 to
`DateTime.LocalNow()` — contiguous but **non-deterministic** (end drifts every
refresh) and **too short**: the 320 future-dated listings (and any pre-1937
releases, if they exist — see Open questions) fall outside the table and land in
the same relationship blank row as the 26,166 dateless rows, conflating "unknown"
with "future". **Not marked as a date table** (no mark in TMDL). `Month Name` has
no sortByColumn. No business flags. Columns: Date, Week Number, Month Number,
Month Name, Year.

**Required:**
1. **Deterministic, data-anchored range** — start = Jan 1 of min(Release Date)
   year, end = Dec 31 of max(Release Date) year (covers all future-dated rows).
   Contiguous by construction; no `DateTime.LocalNow()`.
2. **Marked as date table** on `Date[Date]` (exact TMDL syntax verified against
   current docs at s4, per research-first — do not write from memory).
3. `Month Name` sorted by `Month Number`.
4. After the range fix, the blank bucket on any Date axis is *exactly* the
   dateless rows — no longer polluted by out-of-range dates.

**Unknown-date mechanism (binding, from the entrant's over-time seed):** a blank
`Release Date` cannot get a labeled member on a marked Date table (marking demands
a contiguous, blank-free date column), so the labeled mechanism lives one grain up:
- **ADD `Release Year` dimension** (M-generated): `Year Key` (int; −1 = unknown),
  `Year Label` (text; "1937" … "No date on record"), `Year Sort` (int; unknown
  sorts last by default — s5 may flip), `Year Status` ∈ {Past, Current, Future,
  No date} relative to the disclosed snapshot anchor. Kimball's explicit
  unknown-member row with surrogate key −1 (source register, Tier 2).
- **ADD `Movies[Release Year Key]`** (M step in the Movies partition:
  `Date.Year([Release Date])`, null → −1; hidden FK).
- Over-time pages (coverage by year, vote-evidence by year) use
  `'Release Year'[Year Label]` as the axis: dateless rows are a first-class,
  labeled, countable bucket — never dropped, never "(Blank)".
- The Date table remains the doctrinally required marked date dimension for any
  date-grain need; Release Year is a parallel coarser-grain dimension with its own
  single path — not a snowflake.

**Future-release flag:** lives on **Movies** — `Is Future Release` (M step:
`[Release Date] > #date(2026, 7, 24)`; dateless rows → FALSE). Anchor = the
dataset's own download date (from the starter's source comments), disclosed on the
method panel; never `TODAY()` (determinism). One flag, one home: Date-side flags
cannot classify dateless rows, and `'Release Year'[Year Status]` already covers
year-grain axis shading.

## 5. `_Measures` plan

Starter state: one measure (`Profit = SUM(Movies[Revenue]) - SUM(Movies[Budget])`),
no docstring, no folder (validator warnings); hidden `Value` column (keep).

**Numbered display-folder taxonomy (fixed at this gate):**

```
01 Core                      counts and denominators
02 Lie 1 · Financials        the trap and its honest counterpart
   02 …\Trap — kept as exhibit
03 Lie 2 · Ratings           raw, disclosed parameters, evidence-weighted
04 Lie 3 · Popularity        display-only value + rank divergence
05 Data health · Time        undated / future / duplicates
06 Display                   dynamic titles, labels, semantic colors (s5 fills values)
```

**The Profit trap is KEPT, not deleted.** Its formula stays byte-identical — the
formula *is* Lie #1's exhibit. At s4 it is renamed to **`Profit (naive)`** (per
M-003), given docstring `/// TRAP — Lie #1 exhibit: treats unknown financials as
real money. Never present as a finding.`, displayFolder
`02 Lie 1 · Financials\Trap — kept as exhibit`, and a normalized formatString
(the starter's `\$#,0.###############` oddity → `\$#,0;(\$#,0)`). One starter
visual binds `[Profit]`
(`…Report\definition\pages\22a73d6058ce40e505e0\visuals\e21488a8d900077091bd\visual.json`);
pbir-operator sequences the rename with either updating that binding in the same
batch or the s6 page retirement — never leaves it dangling.

**Measure list** (docstring + explicit formatString on every one, per tmdl-style):

| Folder | Measure | DAX sketch | Format |
|---|---|---|---|
| 01 | Movies | `COUNTROWS(Movies)` | `#,0` |
| 01 | Movies (credible financials) | `CALCULATE([Movies], Movies[Budget] >= 10000, Movies[Revenue] > 0)` | `#,0` |
| 01 | Movies (all listings incl. adult) | `CALCULATE([Movies], REMOVEFILTERS(Movies[Adult]))` — method-panel reconciliation | `#,0` |
| 02 | Profit (naive) | KEPT starter formula, renamed/foldered as above | `\$#,0;(\$#,0)` |
| 02 | Financial coverage % | `DIVIDE([Movies (credible financials)], [Movies])` | `0.0%` |
| 02 | Median profit (credible) | `CALCULATE(MEDIANX(Movies, Movies[Revenue] - Movies[Budget]), Movies[Budget] >= 10000, Movies[Revenue] > 0)` | `\$#,0;(\$#,0)` |
| 02 | Mean profit (credible) | same filter, `AVERAGEX` — shown only as the mean-vs-median outlier-drag evidence | `\$#,0;(\$#,0)` |
| 03 | Votes | `SUM(Movies[Vote Count])` | `#,0` |
| 03 | Rating (raw) | `DIVIDE(SUMX(Movies, Movies[Vote Average] * Movies[Vote Count]), SUM(Movies[Vote Count]))` — vote-weighted at every grain (per-movie it equals Vote Average; 0 votes → BLANK, never 0); plain AVERAGE of Vote Average is forbidden (M-005) | `0.00` |
| 03 | Rating m (disclosed) | `100` — signed assumption, constant | `#,0` |
| 03 | Rating C (disclosed) | `6.96` — signed vote-weighted global mean, computed once at Q2, constant | `0.00` |
| 03 | Rating (evidence-weighted) | `VAR v = SUM(Movies[Vote Count]) RETURN IF(v = 0, BLANK(), DIVIDE(v, v + [Rating m (disclosed)]) * [Rating (raw)] + DIVIDE([Rating m (disclosed)], v + [Rating m (disclosed)]) * [Rating C (disclosed)])` — movie grain (contract); group views use Rating (raw) | `0.00` |
| 03 | Rating gap (raw − weighted) | difference of the two — Lie #2's fall-from-#1 column | `+0.00;-0.00;0.00` |
| 03 | Movies with evidence (votes ≥ m) | `CALCULATE([Movies], Movies[Vote Count] >= 100)` | `#,0` |
| 03 | Evidence share % | `DIVIDE([Movies with evidence (votes ≥ m)], [Movies])` — vote-evidence-by-year axis | `0.0%` |
| 04 | Popularity (as-is) | `IF(HASONEVALUE(Movies[Movie ID]), MAX(Movies[Popularity]))` — BLANK at any group grain; never aggregated (M-007) | `0.0` |
| 04 | Rank · Popularity | `RANKX(ALLSELECTED(Movies[Movie ID]), CALCULATE(MAX(Movies[Popularity])))` | `0` |
| 04 | Rank · Rating (weighted) | RANKX over ALLSELECTED movies by [Rating (evidence-weighted)] | `0` |
| 04 | Rank · Revenue | RANKX by `CALCULATE(SUM(Movies[Revenue]))`, Revenue > 0 only | `0` |
| 05 | Movies (undated) | `CALCULATE([Movies], ISBLANK(Movies[Release Date]))` | `#,0` |
| 05 | Undated share % | `DIVIDE([Movies (undated)], [Movies])` | `0.0%` |
| 05 | Movies (future-dated) | `CALCULATE([Movies], Movies[Is Future Release] = TRUE)` | `#,0` |
| 05 | Movies (distinct title + date) | `COUNTROWS(SUMMARIZE(Movies, Movies[Title], Movies[Release Date]))` | `#,0` |
| 05 | Duplicate listings | `[Movies] - [Movies (distinct title + date)]` | `#,0` |
| 06 | Color · Trap / Color · Honest / Color · Neutral | semantic color hex from the s5 theme (placeholders until the design contract lands) | text |
| 06 | Title · Lie 1 / Lie 2 / Lie 3 / Landing | dynamic insight titles; copy contracted at s5 | text |
| 06 | Label · Method | concatenated disclosure string (floor $10k, m=100, C=6.96, anchor 2026-07-24, Adult excluded) | text |

Layering rule holds: base measures touch columns; everything else references
measures. **Adult exclusion mechanism (proposed):** a report-level filter on
`Movies[Adult] = FALSE` — visible in the filter pane, which is itself on-theme —
rather than baking the filter into every measure; `[Movies (all listings incl.
adult)]` reconciles the raw total on the method panel. Entrant confirms (Open
questions).

**Column hygiene CHANGEs on Movies (s4, small diffs):** `summarizeBy: none` on
Vote Average, Vote Count, Revenue, Budget, Runtime, Popularity (a summed rating is
its own little lie — kill all implicit aggregations; columns stay visible for
axes); normalize Budget/Revenue formatString; new FK `Release Year Key` hidden.

## 6. Metric map (every contract, one line)

| ID | Path |
|---|---|
| M-001 | `_Measures[Movies]` = COUNTROWS(Movies) — "listings"; dup caveat via `[Duplicate listings]` |
| M-002 | `_Measures[Financial coverage %]` = DIVIDE([Movies (credible financials)], [Movies]); credible = Budget ≥ 10000 AND Revenue > 0 (signed floor; also excludes the one −12 Revenue row) |
| M-003 | starter measure KEPT: `_Measures[Profit (naive)]` = SUM(Movies[Revenue]) − SUM(Movies[Budget]) — trap-marked, never unaccompanied |
| M-004 | `_Measures[Median profit (credible)]` = MEDIANX over Revenue − Budget on the credible set; `[Mean profit (credible)]` beside it as outlier-drag evidence |
| M-005 | `_Measures[Rating (raw)]` = vote-weighted mean of Movies[Vote Average] by Movies[Vote Count]; BLANK at 0 votes |
| M-006 | `_Measures[Rating (evidence-weighted)]` = shrinkage with m = 100, C = 6.96 (both disclosed constants); BLANK at 0 votes ("no evidence", never C) |
| M-007 | `_Measures[Popularity (as-is)]` (single-movie guard, never aggregated, never good/bad-colored) + `[Rank · Popularity]` vs `[Rank · Rating (weighted)]` vs `[Rank · Revenue]` for the divergence view |

## 7. Metrics NOT available — do not fabricate

| Asked / tempting | Why the source cannot support it | Nearest honest proxy + caveat |
|---|---|---|
| Popularity's meaning or derivation | TMDB does not publish the formula | None. Display value + rank only, with the "definition not published" marker (M-007) |
| Inflation- or currency-normalized financials | No currency or CPI fields; TMDB currency normalization unverifiable | Nominal values "as recorded (USD assumed)" — caveat on every financial visual |
| True profitability (marketing costs, distribution splits) | Not in the dataset | Revenue − Budget labeled "gross gap, not P&L" |
| Verified correctness of the credible-financials subset | No external ground truth | $10k floor heuristic, disclosed, robustness shown ($10k → 13.1% vs $100k → 11.9%) |
| Claims about the full TMDB catalogue (~930k movies) | Starter partition filters `budget > 0` before import; 85,394 rows loaded | Claims scoped to "listings with a populated budget field"; disclosed on method panel |
| Distinct-film count | 2.0% duplicate (Title, Release Date) pairs across distinct TMDB IDs; no reliable dedup key | Row count labeled "listings"; dup share shown (M-001) |
| "Representative" movie-economics claims | Credible-financials rows self-select big-studio / US / recent | Claim scoping on-canvas (M-004): "credible" ≠ "representative" |

## 8. Sources — parameterization (hard-rule violation, must fix)

`expressions.tmdl` hardcodes `C:\Users\shlindsay\Downloads\TMDB\TMDB_movie_dataset_v11.csv`
in **both** `Source` (line 5) and `Schema` (line 21) — confirmed by
`validate_tmdl --strict` (2 errors). Fix at s4: ADD text parameter `SourceRoot`
(placeholder default, entrant sets locally, never a committed user path); CHANGE
both expressions to `File.Contents(SourceRoot & "\TMDB_movie_dataset_v11.csv")`.
This is the only data source in the model.

## 9. Build order for s4 (small single-concern diffs)

1. `SourceRoot` parameter + both expression rewrites (clears the 2 validator errors).
2. Date partition rewrite (deterministic range) + mark as date table + Month Name sort.
3. Movies M steps: `Release Year Key`, `Is Future Release`; column hygiene batch.
4. `Release Year` table + relationship #8.
5. Profit rename/docstring/folder (+ starter-visual binding decision).
6. `_Measures` build-out, folder by folder; validate after each batch
   (`validate_tmdl --strict`, then `tmdl_inventory` diff against this blueprint).

Gate-4 diff targets: **10 tables** (9 + Release Year), **8 relationships**,
**~28 measures** (1 kept + ~27 new incl. display stubs), 2 new Movies columns,
1 new shared expression parameter, 0 validator errors.

## Open questions

None blocking G3. Entrant accepted the blueprint 2026-08-04 in-session,
including the not-available list, the snapshot anchor 2026-07-24 (was Q2), and
the report-level Adult filter mechanism (was Q3). Routed onward, not open:

1. **True minimum Release Date** — s4 verifies via Modeling MCP; the new Date
   range anchors to the verified min either way.
4. **"No date on record" position on year axes** (first or last) — s5 design
   call; the model supports either via `Year Sort`.
5. **Timing of the Profit rename** vs the one starter visual binding `[Profit]` —
   pbir-operator sequences (same-batch binding update or s6 page retirement).
