# 02 — Metric architecture (glossary DRAFT — G2 pending profiling + signature)

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

## Gate G2 checklist

- [x] One contract per KPI, edge cases hunted (traps contracted AS traps)
- [ ] TO-VERIFY slots filled from profiling output above
- [ ] Entrant signs the glossary (records in status.yaml gate note)
