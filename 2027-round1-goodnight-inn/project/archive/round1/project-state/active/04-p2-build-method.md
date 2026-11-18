# 04 - P2 build method (the build description Claude builds from)

**Date:** 2026-11-06 · **Decided by:** Björn, 16:33: "ik wil een echte
beschrijving van de bouwmethode waar Claude mee kan bouwen." · **Status:** this
is the decided method. Deviations go back through Björn, not into the build.
Every "verify" below names a concrete check with a fallback, not open research.

## Architecture (decided)

Native visuals only on P2. No Deneb, no HTML Content in the base build. No
animation or morph anywhere: the state swap is instant by design. One persistent
scatter on the left; one right panel with two display states; one disconnected
package selector; one disconnected scenario selector. The package choice and the
layout state are independent systems that never write to each other.

## Model additions (stage 3/4)

Grain declared first (star-schema rule); everything derived from the provided
tables, per the contest's provided-data rule:

1. `Package` - one row per valid package (456 of 1,024 subsets; validity rules in
   `01-richting-p1-p2.md`). Columns: PackageID (e.g. `01+02+10`), CapexUSD, NPV
   for Low / Expected / High, 2032 run-rate for Low / Expected / High,
   RoomsAdded, RoomsRefreshed, ProjectCount, GrowthCount, ShortlistLabel
   (`A` / `B` / `C` / blank), plus the criterion text per shortlist label.
   Derivation (pure calculated table vs reshaped helper from provided data) is
   decided at stage 3; the offline reference is
   `project/analysis/15_portfolio_search.py`. Validation: exactly 456 rows.
2. `PackageProject` - bridge, one row per PackageID x ProjectID membership.
3. `PlanSelector` - disconnected, PackageID + display label. **No
   relationships.** Single-select is set on the slicer, not in the table.
4. `Scenario` - disconnected Low / Expected / High (exists in the sketch model
   per the D4 mechanics table).

Relationships: `Package` 1-* `PackageProject` *-1 `InvestmentProjects`.
`PlanSelector` and `Scenario`: none. Waterfall totals must reconcile with the
`Package` row for every scenario (offline reference: max abs error 1.4e-14
without overlap stress).

## Measures (concept DAX: `.claude/skills/fx-focus/references/pakketmodel-dax.md`)

- `Selected Package = COALESCE(SELECTEDVALUE(PlanSelector[PackageID]), "01+02+10")`
  - fallback is preset A, so the panel is never empty.
- `Selected Scenario = COALESCE(SELECTEDVALUE(Scenario[Scenario]), "Expected")`.
- `Package NPV (sel)` / `Package Run-rate (sel)` - SWITCH on Selected Scenario
  over the three columns; format strings survive the switch (DC-056).
- `Package Highlight = IF(Package[PackageID] = [Selected Package], 1, 0)` -
  drives the chosen point's color/size.
- `Package Project NPV` / `Package Project Capex` - TREATAS over the bridge for
  the waterfall.
- Text measures: panel title, the three shortlist card bodies, the uncertainty
  line. Quality per project in dataset units only
  (`SatisfactionChangePts`, never summed, never as predicted NPS).

## Page construction (stage 6)

- **Left:** one scatter. X = capex, Y = NPV (selected scenario), one point per
  package; base color = contains-refresh vs not; `Package Highlight` marks the
  chosen package; presets A/B/C labeled (category label or calculated column).
- **Right top:** `PlanSelector` as single-select slicer (or three buttons A/B/C
  plus the slicer for own choice - one of the two, not both); scenario slicer
  Low / Expected / High.
- **Right panel, state Shortlist:** three preset cards (criterion, composition,
  capex, NPV Low/Expected/High, hotel reach) plus the standing uncertainty line
  (running costs net unverified; overlap partially stress-tested).
- **Right panel, state Plan:** chosen package composition, waterfall of project
  NPV contributions, details (payback, timeline, risks), back button to
  Shortlist. An optional separate Werkplan expand is allowed.
- **Bookmarks:** `P2 Shortlist` and `P2 Plan`: Data **off**, Display **on**,
  Current page **off**, **Selected visuals** = the panel group only. The
  selector and the scatter stay outside. Canvas buttons switch states.
- **Point clicks:** may cross-highlight inside the scatter's own panel at most;
  they never trigger a bookmark and the selection story never depends on them
  (applying a bookmark clears cross-selections by design).

## Verification (part of the build)

- Gate tests 1-3 of `03-focuswissel-testplan.md` in a proof PBIX on the first
  build day; outcomes recorded in that file before the real P2 is committed.
- Totals reconcile per scenario; scenario switch keeps formats; alt text, tab
  order and contrast pass ax-audit; Publish-to-Web incognito render at
  1920x1080 and 1366 width; PDF/PPT export static is expected and acceptable.

## Decided fallbacks

- Scatter conditional color unsupported in the Desktop version in use ->
  highlight via a second series (all packages grey + the selected package as an
  accent series); never via self-filtering.
- Selector does not fit the panel -> move it to a top bar; the pattern is
  unchanged.
- Test 4 confirms clicks die on state swap (expected) -> clicks are documented
  view-only; nothing in the design depends on them.

## The package matrix (the source of the scatter and the shortlist)

The matrix is built once, reproducibly, and everything on P2 reads from it. It is
never assembled ad hoc for the scatter, and the presets are never hand-picked
points. Axes confirmed by Björn 16:41: **X = total package capex in $M; Y = NPV
through 2032 in $M for the selected scenario** (Low/Expected/High), with the zero
line visible. There is deliberately **no NPS-growth axis**: the provided
quality effects cannot be summed into a defensible NPS prediction.

**Universe and validity.** The 10 initiatives in `InvestmentProjects` give 1,024
subsets. A subset is a valid package when: total capex <= $60 M
(`Brands[InvestmentBudgetUSD]`); it holds >= 3 initiatives; >= 1 has
`GrowthInitiative = Yes`; GI-02 appears only with GI-01 and is phased after it.
That leaves **456 valid packages** - the validation count for the `Package`
table at stage 4.

**Cash-flow engine (per package, per scenario).** Derived only from
`InvestmentProjects`, `InvestmentScenarios`, `InvestmentProjectProperties`,
`FinanceParameters` and `FinanceAssumptions`: capex phased per project,
disruption (rooms out of service), ramped benefit from go-live, dependency
sequencing (GI-02 after GI-01). Conventions: constant 2025 dollars; 8% monthly
discounting; horizon through December 2032; no residual value. Outputs per
package per scenario: capex, NPV, 2032 run-rate, payback year (or "beyond
horizon"), rooms added/refreshed, hotel counts.

**Uncertainty is stated, not smoothed.** Zero packages are NPV-positive in Low;
six in Expected. Running costs net are unverified (GI-01 netting is no proof
for GI-10; a gross reading moves the best base package's Expected NPV to about
-0.5). Project overlap is only partially stress-tested (top package +3.26 ->
+1.83 in the tested case). The panel carries this as a standing line; no
absolute invest/do-not-invest claim (no residual value in the model).

**Shortlist selection rules (explicit, Expected lens).**
- **A - max NPV:** argmax NPV over all 456 -> 01+02+10 (capex $9.4 M, NPV
  -5.4 / +3.3 / +12.6).
- **B - widest rated reach with NPV >= 0:** argmax count of hotels with a
  dataset satisfaction value, subject to Expected NPV >= 0; ties broken by
  higher NPV -> 01+09+10 (capex $11.65 M, Expected +2.7).
- **C - best with the ten-oldest refresh:** argmax NPV subject to containing
  GI-07 -> 01+07+10 (capex $36.9 M, Expected -23.3).
The rules, not the points, are recorded; when the scenario slicer changes, the
matrix and the ranking recompute while the preset labels keep their criterion.
**Superseded 7 Nov (review v2, `07-fixgids-review-v2.md` K1):** the rules are
applied once, on the Expected case (`Package[Preset]`), and the three packages
stay fixed in every scenario; only their numbers follow the scenario. Re-applying
the rules per scenario left B empty in Low (a broken plan state) and gave C two
different Low NPVs (REVIEW B1, M6).
Known label corrections: an earlier PDF called C "01+02+07+10, $38.9 M, -23.9"
(wrong label, right ranking CSV) and B "01+02+09+10" (the criterion selects
01+09+10); cheapest valid refresh 07+09+10 at $36.1 M is not the best-refresh
package. Earlier start plan 01+02+04+05+07+10 = -31.1 in this model vs -29.5 in
the repo convention (monthly discounting, GI-02 sequencing); the canvas states
its convention.

**Reproducibility and checks.** Reference implementation:
`project/analysis/15_portfolio_search.py`. At stage 3/4 the matrix is rebuilt
inside the model (calculated table or reshaped helper, both allowed); checks:
456 rows; per-scenario reconciliation of bridge totals against package rows
(offline max abs error 1.4e-14 without overlap stress); every figure on the
canvas traceable to a matrix row. Synthetic fixture data stays out of the
submission.
