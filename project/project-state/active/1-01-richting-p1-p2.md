# 01 - Direction: P1 factual comparison, P2 package scatter with focus swap

**Date:** 2026-11-06 · **Decided by:** Björn (WhatsApp, direction set 15:40 and
confirmed as the method to record at 16:22: "zet de technische uitwerking en de
inhoudelijke keuze in de repo") · **Stage:** 0 (intake in progress); this file is
the stage-1/2/5 input that supersedes the page maps in `MISSION-goodnight-inn.md`
§2/§4 and refines the P2 side of `PITCH-D4-what-if-merged.md` (PR #2). Numbers are
hypotheses from the offline decode (`project/analysis/`); per the do-not-fabricate
rule every figure is re-derived from the model at stage 4/6 before it lands on a
canvas.

## What is decided

- **P1, The Brand Review: a factual four-brand comparison plus Goodnight Inn
  geography.** No repeated scatter on P1; no loose row of repeating KPI cards. A
  do-nothing projection is optional and, if shown, labeled as scenario logic from
  the provided `FinanceAssumptions` - never as a model outcome.
- **P2, The Investment Strategy: a package scatter with a focus swap.** All valid
  packages in one scatter, a Low/Expected/High scenario switch, a shortlist of
  three criteria-based presets, and a detail plus waterfall view for the chosen
  package. The scatter and the waterfall are Björn's explicit keeps (15:11, 15:13).
- **Method:** the factual, well-supported matrix first, the pretty visual second.
  Explanation lives in tooltips; essential uncertainty never hides in a tooltip.
- **The shortlist is lens-dependent.** There is no universal winner; Low and High
  change the ranking. Each preset answers a different stated criterion.

## The model behind P2 (re-derive before use)

- **456 valid packages** of the 1,024 subsets of 10 initiatives; validity: capex
  <= $60 M, >= 3 initiatives, >= 1 growth initiative, GI-02 only with GI-01 and
  phased after it.
- Conventions (own model): constant 2025 dollars, 8% monthly discounting, horizon
  2027-2032, no residual value. 6 packages are NPV-positive in Expected, none in
  Low. The earlier start plan 01+02+04+05+07+10 scores -31.1 in this model vs
  -29.5 in the repo convention (monthly discounting, GI-02 sequencing); record
  which convention the canvas uses.
- Presets (Expected-based criteria, corrected 15:40):
  - **A - max NPV:** 01+02+10, capex $9.4 M, NPV Low/Expected/High = -5.4 / +3.3
    / +12.6.
  - **B - most dataset-rated hotels with NPV >= 0** (tie: highest NPV):
    01+09+10, capex $11.65 M, Expected +2.7. (Replaces the earlier
    "balans 01+02+09+10" preset; the criterion selects 01+09+10.)
  - **C - max NPV including the refresh of the ten oldest:** 01+07+10, capex
    $36.9 M, Expected -23.3. (Label correction: an earlier PDF labeled C as
    "01+02+07+10, $38.9 M, -23.9"; that label was wrong, the ranking CSV was
    right. Cheapest valid refresh 07+09+10 at $36.1 M is not the best-refresh
    claim.)
- **Quality stays in dataset units.** `InvestmentScenarios[SatisfactionChangePts]`
  is shown per project, never summed across overlapping hotel groups and never
  presented as predicted NPS. In this dataset NPS tracks OverallScore almost
  perfectly (r = 0.999 across hotels, about 27.9 NPS per score point
  historically); that is a data property, not an intervention effect.
- **Open consequential uncertainties, stated on or near the canvas:** running
  costs net are unverified (GI-01 netting is no proof for GI-10; a gross-cost
  reading moves the best base package's Expected NPV to about -0.5); project
  overlap is only partially stress-tested (top package +3.26 to +1.83 in the
  tested case) and known untested overlaps remain; no residual value means no
  absolute invest/do-not-invest claim.

## P1 facts, corrected by the second opinion (6 Nov)

- GN room comfort 7.17, lowest of the four brands; the ten refresh hotels 6.69
  vs 7.29 for the rest.
- Renovation pattern: 44 hotels show renovations (not 50); every brand shows the
  same comfort-vs-age pattern and GN's average renovation is more recent, so no
  causal "starved of renovation" claim without that nuance. Rising room-condition
  complaints are not unique to GN.
- Margin 44.4% before / 33.7% after distribution costs; that moves GN from
  position 1 to 2 (P&K Select 34.7%): the advantage shrinks, it does not flip to
  a loss. Margin fell at 50/50 hotels 2024-25; absolute profit fell at 43/50.
- NPS 3.3 vs 8.5 in 2021; NPS vs hotel age r = -0.79 across 44 hotels -
  correlation, not causation.

## Explicitly not claimed

- No morph or animation promise for the focus swap; see
  `02-focuswissel-methode.md`.
- "Exactly two visible pages" is our design rule from the starter Read Me
  (`project/contest/page-count-ruling.md`). The Round 1 blog post does not state
  a page limit (verified 6 Nov); it does state "at least four built-in visuals".
- Synthetic test data (external proof packs, our own fixtures) never enters the
  submission; provided data only.

## Open before stage 6

- The P2 interaction proof in a separate PBIX: `03-focuswissel-testplan.md`.
- Render check of the sketched P1/P2 wireframes in Desktop (nothing has been
  rendered; all layouts so far are text sketches and HTML comps).
- Publish-to-Web render test and the gallery tag from the contest gallery.
