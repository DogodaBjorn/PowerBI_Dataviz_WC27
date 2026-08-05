# Data model — World Champs BCN 26 — Round 3

The model as the D7 build needs it: a faithful summary of the stage-3 blueprint as
actually built at stage 4 (`03-model-blueprint.md`, `04-model-build.md`), not a
re-design. Nothing here changes the model; the four support measures marked NEW are
a small, recorded extension the design requires (see *Measures the design adds*).

Built state at G4 close: **10 tables · 8 relationships · 33 measures ·
3 shared expressions** · `validate_tmdl --strict` 0 errors, 0 warnings
(one standing waiver: the committed `SourceRoot` value is the entrant's local
drive-letter path — waived 2026-08-04, see `04-model-build.md`).

## Star schema

```
   Genres              Keyword              Production Company
      │ 1                 │ 1                     │ 1
      ▼ *                 ▼ *                     ▼ *
  Genre Bridge       Keyword Bridge      Production Company Bridge
      │                   │                       │
      └────── m:m weak, single direction (bridge filters Movies) ──────┐
                                                                       ▼
                                MOVIES  (fact, 85,394 listing rows)
                                  │ *                        │ *
                    Release Date  ▼ 1                        ▼ 1  Release Year Key
                          Date (MARKED date table,     Release Year (year grain,
                          1800-01-01 … 2099-12-31)     incl. "No date on record")

                                _Measures  (measure table, 33 measures, folders 01–06)
```

| Table | Kind | Grain (one row means…) | Source (parameterized) |
|---|---|---|---|
| Movies | fact | one TMDB movie **listing** from the starter's `budget > 0` load (85,394 rows; `Movie ID` is NOT unique — 101 duplicate-ID rows) | `Source` expression → `File.Contents(SourceRoot & "\TMDB_movie_dataset_v11.csv")` |
| Genre Bridge | factless bridge | one (listing, genre) assignment, parsed from the raw comma-separated field | same, unfiltered |
| Keyword Bridge | factless bridge | one (listing, keyword) assignment | same, unfiltered |
| Production Company Bridge | factless bridge | one (listing, company) credit | same, unfiltered |
| Genres | dimension | one distinct genre string | same, unfiltered |
| Keyword | dimension | one distinct keyword string | same, unfiltered |
| Production Company | dimension | one distinct company string | same, unfiltered |
| Date | dimension (**marked**) | one calendar day | M-generated, deterministic |
| Release Year | dimension | one release-year bucket, incl. the explicit unknown member | M-generated, deterministic |
| _Measures | measure table | — | calculated `{ BLANK() }` |

Bridges are declared m:m weak with single-direction filter flow (dimension → bridge →
Movies). No bidirectional filters anywhere, no snowflakes, one path per fact–dimension
pair. The written justification for keeping the starter's declaration lives in
blueprint §3 and is not re-opened here.

## The marked Date dimension

- `Date[Date]`, range **1800-01-01 … 2099-12-31**, contiguous, deterministic
  (no `DateTime.LocalNow()` — the range is anchored on the data's own verified min
  and max Release Date, both of which are sentinel-suspect extremes kept on purpose).
- Marked as a date table in TMDL: `dataCategory: Time` on the table, `isKey` on
  `Date[Date]` (syntax verified against Microsoft Learn TOM docs at stage 4).
- Columns: `Date`, `Week Number`, `Month Number`, `Month Name` (sorted by
  `Month Number`), `Year`.
- Because the range now covers every real and sentinel date, the blank bucket on any
  Date axis is **exactly** the dateless listings — no longer polluted by out-of-range
  dates. That is what makes the "no date on record" story countable.

## The Release Year dimension and its "No date on record" member

A marked date table cannot carry a labelled blank member, so the labelled unknown
lives one grain up. Kimball's explicit unknown member with surrogate key −1 (source
register, Tier 2).

| Column | Type | Notes |
|---|---|---|
| `Year Key` | int, hidden | **−1 = unknown**; otherwise the release year |
| `Year Label` | text | `"1937"` … `"2099"`, and `"No date on record"` for −1; sorted by `Year Sort` |
| `Year Sort` | int, hidden | unknown sorts **last** |
| `Year Status` | text | `Past` / `Current` / `Future` / `No date`, relative to the disclosed snapshot anchor 2026-07-24 |

- FK on the fact: `Movies[Release Year Key]` (hidden), `Date.Year([Release Date])`
  with null → −1.
- Relationship #8: `Movies[Release Year Key]` \*:1 `'Release Year'[Year Key]`, single
  direction, name `Movies_ReleaseYearKey_to_ReleaseYear_YearKey`.
- **This is the axis of the Act III play animation.** Dateless listings are a
  first-class, labelled, countable bucket — never dropped, never "(Blank)". They are
  excluded from the play axis and *counted where they are excluded*
  (`c_nodate_chip`, bound to `[Label · No date]`).
- **s5 design call on the open question "unknown first or last":** the "No date on
  record" member sorts **last** (the model's default `Year Sort`), so the play axis
  runs chronologically and the unknown bucket never leads the story. It is disclosed
  by the no-date chip rather than by a leading axis member.

## Measure inventory by display folder

The numbered taxonomy was fixed at G3 and is not renamed. Counts below are
**built (33)** plus **design additions (50 new, and 8 stage-4 stubs whose expressions
are replaced)** = **83 measures** after stage 6 implements `measures.dax`. The
additions break down as 26 in `06 Display`, 10 in `06 Display\Alt text`, and 14
support measures in folders 01–05.

**01 Core** — counts and denominators
`Movies` · `Movies (credible financials)` · `Movies (all listings incl. adult)`
· *NEW* `Movies (scatter population)`

**02 Lie 1 · Financials** — the trap and its honest counterpart
`Financial coverage %` · `Median profit (credible)` · `Mean profit (credible)`
· *NEW* `Financial floor (disclosed)` · *NEW* `Movies (zero revenue)`
· *NEW* `Zero-revenue share %`

**02 Lie 1 · Financials\Trap — kept as exhibit**
`Profit (naive)` — the starter formula, byte-identical, kept as the exhibit

**03 Lie 2 · Ratings** — raw, disclosed parameters, evidence-weighted
`Votes` · `Rating (raw)` · `Rating m (disclosed)` · `Rating C (disclosed)`
· `Rating (evidence-weighted)` · `Rating gap (raw − weighted)`
· `Movies with evidence (votes ≥ m)` · `Evidence share %`
· *NEW* `Median votes` · *NEW* `Votes p75` · *NEW* `Movies (zero votes)`
· *NEW* `Zero-vote share %` · *NEW* `Two-vote ten (illustration)`
· *NEW* `Godfather rating (reference)`

**04 Lie 3 · Popularity** — display-only value and rank divergence
`Popularity (as-is)` · `Rank · Popularity` · `Rank · Rating (weighted)`
· `Rank · Revenue` · *NEW* `Winner · title`

**05 Data health · Time** — undated / future / duplicates
`Movies (undated)` · `Undated share %` · `Movies (future-dated)`
· `Movies (distinct title + date)` · `Duplicate listings` · `Duplicate Movie IDs`
· *NEW* `Adult listings excluded` · *NEW* `Snapshot anchor (disclosed)`
· *NEW* `Movies (sentinel-dated)`

**06 Display** — dynamic titles, labels, semantic colours (the design contract)
Replacing the eight stage-4 stubs: `Color · Trap` · `Color · Honest`
· `Color · Neutral` · `Title · Lie 1` · `Title · Lie 2` · `Title · Lie 3`
· `Title · Landing` · `Label · Method`.
New: `Color · Trap (night)` · `Color · Honest (night)` · `Color · Neutral (night)`
· `Color · Rating verdict` · `Mark · Rating verdict` · `Color · Scatter mark`
· `Copy · Act I · action` · `Copy · Act I · naive read`
· `Copy · Act I · note zeros` · `Copy · Act I · responsible read`
· `Copy · Act I · waffle title` · `Copy · Act I · waffle foot`
· `Copy · Act I · verdict` · `Copy · Act I · kpi label`
· `Copy · Act II · note median` · `Copy · Act II · responsible read`
· `Copy · Act II · verdict` · `Label · Population` · `Label · No date`
· `Copy · Act III · winner label` · `Copy · Act III · verdict`
· `Label · Chip floor` · `Label · Chip m` · `Label · Chip C`
· `Label · Caveats` · `Image · Poster URL`

**06 Display\Alt text** — the accessibility family (dynamic alt text)
`Alt · kpi_profit_naive · SC1` · `Alt · kpi_profit_naive · SC3`
· `Alt · dn_ticket_waffle` · `Alt · tbl_perfect_tens` · `Alt · dn_rating_fall`
· `Alt · hero_premiere_scatter` · `Alt · c_refusal_popularity`
· `Alt · c_nodate_chip` · `Alt · tbl_production_counts` · `Alt · tt_movie_poster`

### Measures the design adds outside 06 Display (blueprint amendment)

Fourteen of the fifty new measures are counts and constants, not strings, so they
belong in folders 01–05 rather than 06. They extend the signed §5 list and must be
recorded as a blueprint amendment when G5 closes:
`Movies (scatter population)`, `Financial floor (disclosed)`,
`Movies (zero revenue)`, `Zero-revenue share %`, `Median votes`, `Votes p75`,
`Movies (zero votes)`, `Zero-vote share %`, `Two-vote ten (illustration)`,
`Godfather rating (reference)`, `Winner · title`, `Adult listings excluded`,
`Snapshot anchor (disclosed)`, `Movies (sentinel-dated)`.
No new tables, no new columns, no new relationships. Nothing in the model changes.

## Field map (what the report binds to)

Full per-visual binding lives in `design-handoff.md`; this is the model-side view.

| Report element | Binding | Notes |
|---|---|---|
| `hero_takeaway` (p0) | `[Title · Landing]` | Key Takeaway with two live counts |
| `z_billing_method` / `z_billing_caveats` (p0) | `[Label · Method]` / `[Label · Caveats]` | the scope stamp, live |
| `btn_ticket_act1/2/3` teasers (p0) | `[Financial coverage %]`, `[Median votes]`, static refusal phrase | M-002 / M-005 / M-007 |
| `kpi_profit_naive` (p1) | `[Profit (naive)]` + `[Copy · Act I · kpi label]` | trap exhibit — never unmarked |
| `dn_ticket_waffle` (p1) | `[Financial coverage %]`, `[Movies (credible financials)]`, `[Movies]` | 100-cell waffle, 13 valid |
| `c_p1_*` script blocks (p1) | `[Copy · Act I · …]` family | live numbers in prose |
| `tbl_perfect_tens` (p2) | `Movies[Title]`, `[Rating (raw)]`, `[Votes]`, `[Image · Poster URL]`, `[Color · Rating verdict]`, `[Mark · Rating verdict]` | filter `[Rating (raw)] = 10` |
| `dn_rating_fall` (p2) | `Movies[Title]`, `[Rating (raw)]`, `[Rating (evidence-weighted)]`, `[Rating C (disclosed)]` | dumbbell, C reference line |
| `hero_premiere_scatter` (p3) | X `Movies[Revenue]` (log), Y `[Rating (evidence-weighted)]`, Details `Movies[Title]`, Play `'Release Year'[Year Label]`, colour `[Color · Scatter mark]` | population filters below |
| `tbl_refusal_ranks` (p3) | `Movies[Title]`, `[Rank · Popularity]`, `[Rank · Rating (weighted)]`, `[Rank · Revenue]` | Top 3 by `[Rank · Popularity]` |
| `c_nodate_chip` (p3) | `[Label · No date]` | the labelled unknown |
| `tbl_production_counts` (p9) | `[Movies (all listings incl. adult)]`, `[Adult listings excluded]`, `[Movies]`, `[Duplicate listings]`, `[Duplicate Movie IDs]`, `[Movies (undated)]`, `[Movies (future-dated)]` | the cross-foot |
| `tbl_disclosed_params` (p9) | `[Financial floor (disclosed)]`, `[Rating m (disclosed)]`, `[Rating C (disclosed)]`, `[Snapshot anchor (disclosed)]` | every parameter on canvas |
| `tt-movie-poster` (tooltip) | `[Image · Poster URL]`, `Movies[Title]`, `'Release Year'[Year Label]`, `[Votes]`, `[Rating (raw)]`, `[Rating (evidence-weighted)]`, `[Rank · Popularity]` | poster is enhancement only |

**Standing filter, report level:** `Movies[Adult] = FALSE`, **visible and locked** in
the filter pane. Every number above is therefore on the 84,036-listing basis;
`[Movies (all listings incl. adult)]` is the only measure that reaches past it, and it
exists purely so the end-credits page can cross-foot the exclusion.

**Act III scatter population filters** (visual level, printed on canvas):
`Movies[Budget] >= 10000` AND `Movies[Revenue] > 0` AND `Movies[Vote Count] >= 100`,
and `'Release Year'[Year Key]` excludes −1, 1800 and 2099.

## Placeholder batch — compute at build, never from memory

Every `{PLACEHOLDER}` in the approved prototype resolves to one of these. **Stage 6
reads each number out of the model** (Desktop, or the modeling MCP's DAX query
operations) and records the value and the date in `BUILD_LOG.md`. Typing a number
from this document, from the prototype, or from memory is a G6 defect.

| # | Placeholder in the prototype | Resolve from | Lands in |
|---|---|---|---|
| 1 | `{NAIVE_PROFIT}` **and its sign** | `[Profit (naive)]`; the sign drives the copy branch inside `[Copy · Act I · naive read]` | `kpi_profit_naive`, `c_p1_dlg_naive` |
| 2 | `{MEDIAN_PROFIT}` | `[Median profit (credible)]` | `c_p1_dlg_honest`, `c_waffle_foot` |
| 3 | `{MEAN_PROFIT}` | `[Mean profit (credible)]` | `c_p1_dlg_honest`, `c_waffle_foot` |
| 4 | `{TOP3_POP_RANKS}` — top-3 popularity **film names** plus their weighted-rating and revenue ranks | `Movies[Title]` filtered to `[Rank · Popularity] <= 3`, with `[Rank · Rating (weighted)]` and `[Rank · Revenue]` | `tbl_refusal_ranks` |
| 5 | `{GODFATHER_W}` | `[Godfather rating (reference)]` — verify exactly one listing matches | `c_p2_dlg_honest` |
| 6 | `{SCATTER_N}` | `[Movies (scatter population)]` | `c_scatter_population` |
| 7 | `{WINNER}` | `[Winner · title]` — SCENARIO CHOICE composite, disclosed on canvas | `c_winner_label`, `c_verdict_act3` |
| 8 | Out-of-window / sentinel year counts | `[Movies (sentinel-dated)]` (years 1800 and 2099) plus `[Movies (future-dated)]` | `c_nodate_chip` |
| 9 | Dateless-bucket coverage | `[Movies (undated)]`, `[Undated share %]`, and `[Financial coverage %]` evaluated inside `'Release Year'[Year Label] = "No date on record"` | `c_nodate_chip`, p9 counts |
| 10 | Third perfect-ten film name (leaderboard row 3) and rows 3–4 of the dumbbell | `Movies[Title]` where `[Rating (raw)] = 10`, ordered ascending by `[Votes]` | `tbl_perfect_tens`, `dn_rating_fall` |
| 11 | Tooltip year and popularity rank | `'Release Year'[Year Label]`, `[Rank · Popularity]` | `tt-movie-poster` |
| 12 | Every count in the billing block and the end-credits counts table | `[Label · Method]` and the `tbl_production_counts` bindings | p0, p9 |

**Basis note that changes several prototype numbers.** The prototype was drawn before
unresolved decision #1 defaulted to the *filter-true* basis. Under the locked Adult
filter the report's own denominator is **84,036**, not 85,394, and coverage reads
**13.2%**, not 13.1%. Every count above is therefore bound live rather than typed, and
the 85,394 figure survives in exactly one place: the end-credits cross-foot, where it
is labelled "listings per source".

## Scenario logic (labelled)

Choices, not facts. Each one is labelled on canvas at the place named.

- **Financial credibility floor, Budget ≥ $10,000** — labelled on the p1 waffle title
  and footer, on the p3 adjustment chips, and on the p9 parameters table with its
  robustness pair (13.1% at $10k vs 11.9% at $100k).
- **Reliability threshold m = 100** — labelled on the p2 dialogue and dumbbell, the p3
  chips, the p9 parameters table (with its derivation, Vote Count p90 = 106).
- **Shrinkage target C = 6.96** — the same three places; drawn as a reference line on
  both the dumbbell and the premiere scatter so it is visible, not just stated.
- **Snapshot anchor 2026-07-24** — the dataset's own download date; drives
  `Is Future Release` and `Year Status`. Labelled in the billing block, the ticket
  serials and the p9 parameters table. Never `TODAY()`.
- **"Best-selling AND best-rated" = lowest sum of revenue rank and evidence-weighted
  rating rank** (`[Winner · title]`) — a stated composite, not an industry
  definition. Labelled beside the winner annotation on p3 and in the p9 glossary.
- **Adult exclusion as a report-level filter** rather than baked into measures —
  visible, locked, and cross-footed on p9.

## Metrics NOT available — do not fabricate

Verbatim from `03-model-blueprint.md` §7. This list is rendered on the end-credits
page as **SCENES DELETED — CLAIMS WE REFUSE**; every row must be traceable there.

| Asked / tempting | Why the source cannot support it | Nearest honest proxy + caveat |
|---|---|---|
| Popularity's meaning or derivation | TMDB does not publish the formula | None. Display value + rank only, with the "definition not published" marker (M-007) |
| Inflation- or currency-normalized financials | No currency or CPI fields; TMDB currency normalization unverifiable | Nominal values "as recorded (USD assumed)" — caveat on every financial visual |
| True profitability (marketing costs, distribution splits) | Not in the dataset | Revenue − Budget labeled "gross gap, not P&L" |
| Verified correctness of the credible-financials subset | No external ground truth | $10k floor heuristic, disclosed, robustness shown ($10k → 13.1% vs $100k → 11.9%) |
| Claims about the full TMDB catalogue (~930k movies) | Starter partition filters `budget > 0` before import; 85,394 rows loaded | Claims scoped to "listings with a populated budget field"; disclosed on method panel |
| Distinct-film count | 2.0% duplicate (Title, Release Date) pairs across distinct TMDB IDs; no reliable dedup key | Row count labeled "listings"; dup share shown (M-001) |
| "Representative" movie-economics claims | Credible-financials rows self-select big-studio / US / recent | Claim scoping on-canvas (M-004): "credible" ≠ "representative" |

## Freshness & refresh

- **Data through:** the disclosed snapshot anchor **2026-07-24**, the dataset's own
  download date. The reader can tell three ways: the billing block on p0, the serial
  printed on every ticket stub (`TMDB·2026·07·24`), and the parameters table on p9.
- **Refresh cadence:** none. This is a contest snapshot of a static CSV, deliberately
  anchored so every number is reproducible. `Is Future Release` and `Year Status` are
  computed against the anchor constant, never against `TODAY()` — a refresh on a
  later date changes nothing.
- **Source:** `SourceRoot` text parameter → `TMDB_movie_dataset_v11.csv`. The CSV is
  git-ignored; the committed parameter value is the entrant's local path under the
  standing waiver recorded in `04-model-build.md`.
- **Attribution:** "Source data by TMDB — this product uses TMDB data but is not
  endorsed or certified by TMDB", printed on p0 and p9.
