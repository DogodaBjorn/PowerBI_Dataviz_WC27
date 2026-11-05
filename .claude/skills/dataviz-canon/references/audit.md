# Best-in-class audit - the 20-dimension rubric

Scores a *whole report* (or a design contract before build) against the
canon in `canon.md`. It sits beside, not instead of, the atelier's gate
scores: G5's seven passes rate creative *directions* (/70), G6's ten
dimensions rate *fidelity to the handoff* (/40). This rubric rates
*distance from best in class* - the question a judge, an executive sponsor
or a client's CoE asks. Use it at G1/G2 (as required inputs), at G5 (as a
pre-build pass on the chosen direction), at G7 (as delivery evidence) and
for any contest or showpiece submission.

Score each dimension **0 basic · 1 good · 2 best in class**. Evidence
column is mandatory: a score without a file path, a visual name or a
measured number is an opinion, not an audit.

## Tier A - Meaning (the inputs an agent must have *before* building)

| # | Dimension | 0 basic | 1 good | 2 best in class (verifiable) | Canon | Atelier owner |
|---|---|---|---|---|---|---|
| A1 | Purpose & display type | Topic-based ("Sales report") | Named audience | Documented process → users → decisions → top questions; display type named (monitoring / analytical / communication); capability level named (descriptive → prescriptive) | DC-015, 017, 018, 030 | s0/s1, intake + requirements contracts |
| A2 | KPI anatomy | Raw numbers | Some targets | Every KPI: definition, formula, grain, period, owner, source, target/reference, direction, interpretation rule; leading/lagging balance | DC-021, 022 | s2 metric contracts |
| A3 | Context on every number | Bare cards | PY or target on some | Comparison + trend + benchmark on every headline; IBCS scenarios where finance | DC-039, 037 | dataviz-polish moves 4, 7 |
| A4 | Message | Generic titles | Clear titles | One takeaway per page; DAX-driven insight titles that stay true under filtering | DC-039 | dataviz-polish move 1, copy-polish |

## Tier B - Cognition (the generation rules)

| # | Dimension | 0 | 1 | 2 best in class (verifiable) | Canon | Atelier owner |
|---|---|---|---|---|---|---|
| B1 | Hierarchy (3-30-300) | Random placement | KPIs top-left | Readers answer the page question in ~3 s in a test; page template followed (header → KPIs → dominant visual → support → detail) | DC-016, 031 | page-archetypes, ca-canvas |
| B2 | Cognitive-load budget | Everything on one page | Some grouping | A visual budget per page is declared and met; no legend/mark separation; whitespace groups; no module the delete test can remove | DC-012, 013 | dataviz-polish review pass |
| B3 | Chart choice & integrity | Pies, gauges, 3-D | Bars and lines | Relationship-first; bullets/variance for target comparisons; small multiples share one scale; no truncated axes or dual-axis tricks; measure matches the question | DC-010, 033, 034, 035 | chart-grounding, visual-selection |
| B4 | Color | Rainbow | Brand palette | Grey + one accent; semantic colors consistent report-wide; CVD-safe; diverging midpoint correct; never color alone | DC-037 | design-hard-rules, theme |
| B5 | Text & numbers | Defaults | Consistent | Type hierarchy; direct labels; locale-correct formats; units once; consistent decimals | DC-038 | report-craft-floor, tb-tables |
| B6 | Interaction | Slicer wall, hidden filters | Grouped slicers | Visible state; tooltips/drillthrough for depth; no self-filtering KPIs; predictable navigation; nothing essential only in hover | DC-040 | nv-navigation, tt-tooltips |
| B7 | Uncertainty | Point forecasts | Some ranges | Labeled bands for forecasts/scenarios; error-bar meaning stated | DC-020 | dn-deneb, dataviz-polish move 4 |
| B8 | Accessibility | None | Some alt text | Alt text, tab order, WCAG 2.2 AA measured, Show-data checked; public sector: DigiToegankelijk | DC-042 | ax-audit, check_contrast.py |
| B9 | Mobile & localization | Ignored | Mobile layout exists | Deliberate mobile formatting; translation-ready labels and model | DC-043 | theme-from-brand-kit (assess) |

## Tier C - System (the post-build checks)

| # | Dimension | 0 | 1 | 2 best in class (verifiable) | Canon | Atelier owner |
|---|---|---|---|---|---|---|
| C1 | Semantic model | Flat / lift-and-shift | Star schema | Shared model, thin report; calculation groups + dynamic format strings; field parameters; every measure documented | DC-055–057 | star-schema rule, tmdl-patterns, dax-patterns |
| C2 | Performance | Slow, unmeasured | Acceptable | Measured render and query times; budget per page; storage mode chosen deliberately; SVG/visual-calc budgets respected | DC-053, 058, 059 | validate-project (manual: Performance Analyzer) |
| C3 | Trust & data quality | None | Refresh date | Refresh time, definitions one step away, quality flags, consistent semantics; Wang & Strong dimensions checked | DC-023, 041 | tt-tooltips trust tooltip, nl-definities |
| C4 | Security | Workspace roles only | RLS | RLS/OLS per persona; Viewer role for restricted consumers; export considered; impersonation-tested | DC-060 | s7 (manual) |
| C5 | Consistency & governance | Per-report styling | Shared theme | Design system; organizational theme; custom-visual allow-list with owners and exit; consistency locks hold | DC-045, 050, 062 | design-hard-rules locks, theme |
| C6 | Lifecycle | Manual publish | Dev/Prod | Git (PBIP/TMDL), BPA, DAX/data tests, documented test categories, pipelines | DC-061 | validate-project, build-log |
| C7 | AI readiness | Unprepared | Descriptions | AI data schema, verified answers, instructions tested; Copilot limits understood | DC-070–072 | tmdl-patterns docstrings (extend) |
| C8 | Adoption & observability | Unknown | Usage tracked | Usage + task tests + decision log; owner and review date per item; unused content retired | DC-003 | s7 retrospective |

## Scoring

Total /40. **0–13 basic · 14–27 good · 28–40 best in class.**
A **0 on A2, C3 or B8 caps the rating at "good"** regardless of total: an
undefined KPI, an untrustworthy number or an inaccessible page is never
best in class.

For a *contest entry* the judging criteria usually map as: Insightfulness
→ A1–A4 + B7; Visual effectiveness → B1–B6; Creativity → the signature
moment (G5 pass 7) *constrained by* B2–B4; Accessibility → B8. Score the
tier the judges score, and say which dimensions a contest cannot see
(C4, C6, C8 are usually invisible to a judge - do not spend contest time
there beyond what the rules require).

## Output format

```
## Best-in-class audit - <report or contract> - <date>

Verdict: <one sentence: basic / good / best in class, and the one thing that decides it>

| # | Dimension | Score | Evidence (path / visual / number) | Gap to 2 |
|---|---|---|---|---|
| A1 | ... | 1 | project/project-state/active/01-requirements.md §2 | display type not named |
...
Total: NN/40 → <band>. Caps triggered: <none | A2 / C3 / B8>.

### Must change before <gate>
1. <dimension> - <concrete change> - <who / which skill> - <verify how>

### Accepted gaps
<dimension - reason - accepted by whom>
```

Every "must change" row names the atelier skill or stage that owns the
fix and the command or check that proves it. A finding without an owner
is a wish.
