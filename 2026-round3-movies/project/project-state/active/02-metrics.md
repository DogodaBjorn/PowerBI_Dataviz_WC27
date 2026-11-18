# 02 — Metric architecture (glossary SIGNED 2026-08-04 — G2 passed)

Seven contracts in `active/metrics/`. Standing report-wide filter, proposed:
**Adult = FALSE excluded everywhere** (community gallery context), stated
once on the method panel. The glossary below is what the entrant signs.

| ID | Name | One line | Role in the story |
|---|---|---|---|
| M-001 | Movies | rows in context ("listings" where precision matters) | denominator, coverage funnel |
| M-002 | Financial coverage | share with Budget>0 AND Revenue>0 | Lie #1's shock number |
| M-003 | Profit (naive) | the starter's own trap, all rows, zeros as money | Lie #1, struck through |
| M-004 | Median profit (credible films) | median profit where financials are known | Lie #1's honest answer |
| M-005 | Rating (raw) | Vote Average, group-level always vote-weighted | Lie #2's raw material |
| M-006 | Rating (evidence-weighted) | Bayesian shrinkage toward global mean; m and C disclosed | Lie #2's honest answer |
| M-007 | Popularity (opaque) | undocumented score, ranked-only, never colored good/bad | Lie #3 |

Every contract embeds the theme mechanics: traps carry mandatory trap
markings; honest metrics carry disclosed assumptions (m, C, coverage floor);
selection bias and refused conclusions are on-canvas elements, not footnotes.

## Q2 — profiling queries that close G2

Run in the NEXT Claude session (Modeling MCP now available; Desktop must
have the pbip open) or paste into Desktop's DAX query view and report back.
Numbers land in the contracts' TO-VERIFY slots; then the glossary is signed.

```dax
EVALUATE ROW(
  "rows_total",        COUNTROWS(Movies),
  "adult_rows",        CALCULATE(COUNTROWS(Movies), Movies[Adult] = TRUE),
  "budget_zero",       CALCULATE(COUNTROWS(Movies), Movies[Budget] = 0),
  "revenue_zero",      CALCULATE(COUNTROWS(Movies), Movies[Revenue] = 0),
  "both_known",        CALCULATE(COUNTROWS(Movies), Movies[Budget] > 0, Movies[Revenue] > 0),
  "suspect_budget",    CALCULATE(COUNTROWS(Movies), Movies[Budget] > 0, Movies[Budget] < 10000),
  "future_releases",   CALCULATE(COUNTROWS(Movies), Movies[Release Date] > TODAY()),
  "no_release_date",   CALCULATE(COUNTROWS(Movies), ISBLANK(Movies[Release Date])),
  "votes_zero",        CALCULATE(COUNTROWS(Movies), Movies[Vote Count] = 0)
)
```

```dax
EVALUATE ROW(
  "vc_p50",  PERCENTILE.INC(Movies[Vote Count], 0.50),
  "vc_p75",  PERCENTILE.INC(Movies[Vote Count], 0.75),
  "vc_p90",  PERCENTILE.INC(Movies[Vote Count], 0.90),   -- candidate m (M-006)
  "vc_p99",  PERCENTILE.INC(Movies[Vote Count], 0.99),
  "C_weighted_mean", DIVIDE(SUMX(Movies, Movies[Vote Average] * Movies[Vote Count]), SUM(Movies[Vote Count]))
)
```

```dax
-- Lie #2 example candidates: high raw rating, tiny sample
EVALUATE TOPN(15, FILTER(Movies, Movies[Vote Count] > 0 && Movies[Vote Count] <= 20 && Movies[Vote Average] >= 9),
  Movies[Vote Average], DESC)
```

```dax
-- Duplicate-title share (M-001 caveat)
EVALUATE ROW("distinct_title_year",
  COUNTROWS(SUMMARIZE(Movies, Movies[Title], Movies[Release Date])))
```

## Q2 results — run 2026-08-04 via Modeling MCP (Desktop, localhost:63033)

All four contracted queries plus two follow-up probes (to explain anomalies).
Full table = 85,394 rows; percentages below are of that unless stated.

| Probe | Value | Share |
|---|---|---|
| rows_total | 85,394 | — |
| adult_rows | 1,358 | 1.6% |
| budget_zero | **0** | 0% (see finding F1) |
| revenue_zero | 67,436 | 79.0% |
| both_known (B>0 ∧ R>0) | 17,957 | 21.0% |
| suspect_budget (0<B<10k) | 51,634 | 60.5% |
| future_releases | 320 | 0.4% |
| no_release_date | 26,166 | 30.6% |
| votes_zero | 55,958 | 65.5% |
| vc_p50 / p75 / p90 / p99 | 0 / 1 / 106 / ~4,889 | — |
| C (vote-weighted mean rating) | 6.9594 | — |
| distinct (Title, Release Date) | 83,697 | dup surplus 1,697 rows = 2.0% |

Follow-up probes: Budget min = 1, no blanks, no negatives, 1,731 rows with
Budget = 1, median Budget = **$2,800**. Revenue min = **−12** (exactly one
negative row — it explains both_known 17,957 vs Revenue>0 17,958). Floored
coverage: B ≥ $10k ∧ R > 0 = **11,203 (13.1%)**; B ≥ $100k → 10,198 (11.9%);
B ≥ $10k ∧ R > 0 ∧ Adult = FALSE = 11,110 (13.2% of the 84,036 non-adult rows).

### Findings

- **F1 — Budget "0 = unknown" does NOT hold here.** Not a single Budget is 0
  or blank; the unknowns arrive as junk small values instead (min 1, median
  $2,800, 60.5% under $10k). `Budget > 0` is vacuously true on every row, so
  M-002 as originally worded measures only `Revenue > 0`. The contracted
  fallback triggers: coverage takes a minimum-plausible floor. Proposed
  **floor = Budget ≥ $10,000**, robust to the choice (13.1% at $10k vs 11.9%
  at $100k). Revenue keeps the plain `> 0` test (79.0% zeros behave as the
  classic TMDB unknown).
- **F2 — Coverage is 13.1%, not single-digit, and the table is 85k rows, not
  ~1M.** The M-002 "expected order of magnitude" note was wrong on both
  counts; corrected in the contract. Still Lie #1's shock number: 87% of
  listings have no credible financials.
- **F3 — One negative Revenue row (−12)** — exclude via `Revenue > 0`; noted
  in M-002.
- **F4 — The evidence desert is extreme:** median listing has **0 votes**,
  p75 has 1. m = p90 = 106 → proposed communicable **m = 100**; **C = 6.96**
  (vote-weighted global mean). Lie #2 candidates confirmed by profiling: ≥20
  non-adult films rate a perfect 10.0 on 2–3 votes (e.g. *Las mujeres
  deciden* 2017, *House* (de, date unknown), *Logos* 2025) — weighted score ≈ 7.0,
  a fall from rank #1 to mid-pack.
- **F5 — Dates:** 30.6% of rows have no release date and 320 are
  future-dated — a s3 date-dimension decision (unknown-date member; future
  flag), recorded here so the blueprint inherits it.

## Open questions

- None open at G2 close. Resolved at signature (entrant, 2026-08-04
  in-session): (a) M-002/M-004 credibility floor Budget ≥ $10,000 confirmed;
  (b) M-006 parameters m = 100, C = 6.96 confirmed. Both remain disclosed
  on-canvas assumptions per their contracts.

## Carried forward — entrant's "over time" seed (2026-08-04)

At signature the entrant flagged that the messy dates (F5: 30.6% dateless,
320 future-dated) hold a story *over time*, not just a caveat. Routing:
- **s3**: the Date dimension must make the mess first-class — an explicit
  unknown-date member and a future-release flag, so dateless rows are
  countable, never silently dropped by a date axis.
- **s5**: candidate page/section concept — coverage and evidence *over
  release year* (e.g. financial coverage by year, vote-evidence by year);
  conceptualizing this into the dashboard happens at stage 5 (creative
  direction), constrained by what the s3 model supports.

## SNAPSHOT RECONCILIATION (2026-08-05) — the data moved under us, the conclusions did not

The Q2 profiling above was run against the model as shipped in the contest
starter (loaded from the original author's CSV). The entrant later downloaded
their own copy of the Kaggle TMDB v11 dataset and refreshed, which turns out
to be a **newer snapshot**: 1,469,389 source rows vs the starter's ~930k.
Recomputed directly from `project/data/TMDB_movie_dataset_v11.csv` on
2026-08-05:

| Fact | Q2 (starter snapshot) | Current snapshot | Story impact |
|---|---|---|---|
| Listings (budget > 0) | 85,394 | **85,870** | count only |
| Adult excluded | 1,358 | **1,360** | count only |
| Basis (non-adult) | 84,036 | **84,510** | count only |
| Revenue = 0 | 67,436 (79.0%) | **67,836 (79.0%)** | **identical %** |
| Budget < $10k (junk) | 51,634 (60.5%) | **52,041 (60.6%)** | unchanged |
| Credible (≥$10k ∧ rev>0) | 11,203 (13.1%) | **11,209 (13.05%)** | unchanged |
| Credible, non-adult | 11,110 (13.2%) | **11,116 (13.15%)** | unchanged |
| No release date | 26,166 (30.6%) | **26,429 (30.8%)** | unchanged |
| Negative revenue | 1 | **1** | identical |
| Votes p50 / p75 / p90 | 0 / 1 / 106 | **0 / 1 / 104** | unchanged |
| C (vote-weighted mean) | 6.9594 | **6.9594** | **identical** |

**Every signed parameter survives unchanged** — the $10,000 credibility floor,
m = 100 (p90 rounds to 100 from either 106 or 104), and C = 6.96. **No
re-signature is required**: the entrant signed the *parameters and
definitions*, not the row counts, and each parameter was chosen for
robustness rather than fitted to a snapshot.

The headline claims are untouched: 79.0% of revenues are unknown-as-zero,
~87% of listings lack credible financials, the median listing has zero votes,
and Budget is never 0. That a snapshot change of half a million source rows
moved no conclusion is itself the round's thesis working — disclosed
parameters and measure-bound numbers survive their data being replaced.

**Build consequence:** every printed figure in the report binds live to a
measure (design-handoff.md, "Live-number binding"), so the report is
self-consistent against whatever is loaded. The counts written in prose
across the s2–s5 documents are superseded by this table; data-health figures
quoted from Q2 (duplicate pairs, future-dated) are likewise superseded by
their live measures at build. s7 business validation checks against the
LOADED model, not against the Q2 numbers.

## Gate G2 checklist

- [x] One contract per KPI, edge cases hunted (traps contracted AS traps)
- [x] TO-VERIFY slots filled from profiling output above (run 2026-08-04)
- [x] Entrant signed the glossary 2026-08-04 in-session, incl. the $10k
      floor and m=100/C=6.96 (recorded in status.yaml gate note)
