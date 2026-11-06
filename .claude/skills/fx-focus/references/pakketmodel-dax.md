# fx-focus reference: the package model and its DAX (concept stage)

Everything here is a **concept, not Desktop-tested**. Source implementation to
mirror: `project/analysis/15_portfolio_search.py` (the offline search that
produced the 456 valid packages). Per the contest rules the submission may only
use provided data plus measures, calculated tables and parameters - the offline
pipeline is the specification, not a data source. Synthetic fixture data never
enters the submission.

## Grain declaration first

- `Package`: one row per valid package (456 of the 1,024 subsets of the 10
  initiatives). Key: PackageID. Attributes: capex, NPV per scenario, run-rate,
  rooms added/refreshed, counts, validity flags, shortlist label (A/B/C or
  blank).
- `PackageProject` (bridge): one row per package x initiative membership.
- The scatter plots `Package`; the waterfall plots `PackageProject` joined to
  `InvestmentProjects`; the scenario slicer filters `ProjectCashflow[Scenario]`.
  Never mix the package grain and the project grain in one visual without the
  bridge.

## Disconnected selector

```dax
-- A disconnected table (calculated table over Package, or DATATABLE for the
-- presets) with no relationship to anything:
PlanSelector = ALLNOBLANKROW ( Package[PackageID] )

Selected Package =
COALESCE ( SELECTEDVALUE ( PlanSelector[PackageID] ), "A" )  -- fallback: preset A
```

Single-select enforced in the slicer settings. Because the table is
disconnected, the selection cannot filter the scatter; it only steers measures.

## Highlight measure

```dax
Package Highlight =
IF ( Package[PackageID] = [Selected Package], 1, 0 )
```

Used as the scatter's conditional color/size field (verify the current Desktop
version's conditional formatting surface for scatter data colors before writing
PBIR - research-first rule). All 456 points stay visible; the chosen one is
marked. Do not rely on cross-highlight from a click for this.

## Waterfall contribution (per chosen package)

```dax
Package Project NPV =
CALCULATE (
    [Project NPV],
    TREATAS (
        CALCULATETABLE (
            VALUES ( PackageProject[ProjectID] ),
            PackageProject[PackageID] = [Selected Package]
        ),
        InvestmentProjects[ProjectID]
    )
)
```

Same shape for capex and run-rate. The waterfall's total must reconcile with
the package row (offline check: 456 x 3 scenarios closed to 1.4e-14 without
overlap stress); totals are a test, per dax-patterns.

## Scenario

The disconnected `Scenario` table (already in the model, see the D4 pitch
mechanics) filters `ProjectCashflow[Scenario]`; Expected when nothing is
selected. Scenario switching keeps its format strings (DC-056).

## Quality, honestly

`Satisfaction Points Selected` sums `SatisfactionChangePts` only across
non-overlapping hotel groups or is shown per project; never presented as
predicted NPS. NPS follows OverallScore almost perfectly in this dataset, so it
adds no second signal and is context, not an axis.

## Open verification list

- Calculated-table derivation of the 456 packages in pure DAX (1,024 subsets
  with validity rules and GI-01/GI-02 sequencing) vs a reshaped helper table
  from the provided data - decide at stage 3, test at stage 4.
- "Clear all slicers" button action as the reset - verify in Desktop.
- Scatter conditional formatting by measure in the current PBIR schema - verify
  against the file's `$schema` URL before writing.
