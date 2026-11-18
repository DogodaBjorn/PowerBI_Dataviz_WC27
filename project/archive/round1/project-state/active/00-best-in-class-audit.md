# 00 - Best-in-class audit of the pitched entry (dataviz-canon)

**Date:** 2026-11-05 · **Stage:** 0 (intake in progress); this file is
canon-audit evidence for G0 and the input list for G1, G2 and G5.
**Method:** `dataviz-canon` skill (`.claude/skills/dataviz-canon/`),
20-dimension rubric, scored twice by independent agents on the same
artefact (the pitch comp `project/deliverables/pitch/goodnight-inn-three-ways.html`,
the mission, the draft creative-direction contract). Findings from both
runs are merged below; evidence is a file line, a visual or a measured
number. Nothing in `project/pbip/` exists yet, so Tier C is scored on
planned inputs, as the skill requires.

## Verdict

**Good, not championship-grade yet: 17/40.** Caps triggered: **A2** (no
KPI records; the hero margin has two definitions on one page) and **B8**
(measured contrast failures; no alt text or tab order designed). The
analysis behind the entry is championship-grade (the after-commission
margin flip, the $4.8 M counterfactual, the renovation-age correlation,
the $60.0 M foil, the folio). The visual execution and the definitions
are not yet, and everything that blocks is design-stage work that fits
in the Nov 8-10 window.

## Judging criteria, as a judge will score the comp today

| Criterion | Today (0-10) | Reachable by Nov 15 | What moves it |
|---|---|---|---|
| Analytical quality | 8 | 9 | one margin definition; one comparison base; KPI records judges can read in the .pbix |
| Insightfulness | 8 | 9 | the renovation-starvation "why" and the 2021 cohort on the page, not in the pitch |
| Visual effectiveness | 5 | 8 | 16:9 canvas, one hero per page, half the elements, 180-word budget |
| Creativity and innovation | 5 | 7 | the plan builder talks back: P2 headline as a measure |
| Accessibility | 4 | 8 | AA palette, alt text and tab order in the page-purpose contracts |
| **Total** | **30/50** | **41/50** | |

## Score table (0 basic · 1 good · 2 best in class)

| # | Dimension | Score | Evidence | Gap to 2 |
|---|---|---|---|---|
| A1 | Purpose, display type | 1 | MISSION §2 names Board and judges; `project-state/active/` was empty; display type not named | P1 = communication page, descriptive to diagnostic; P2 = prescriptive with scenarios (owes bands) |
| A2 | KPI records | **0** | no filled `contracts/metric.contract.yaml`; GOP margin = 44.4 % on the card (before commissions) and 33.7 % in the argument (after) | one record per number on both pages (DC-021) |
| A3 | Context on every number | 1 | occupancy card has no comparison (pitch lines 249-252); benchmark lives in a tooltip (MISSION §4) | benchmark and trend on the canvas |
| A4 | Message | 2 | insight titles on every chart (lines 254-264); P2 headline live (line 575) | DAX-driven titles must be contracted at s5 |
| B1 | Hierarchy | 1 | no hero on either page: four equal cards over three equal columns; P2 renders portrait (1.38 h:w) against a 16:9 canvas | one hero per page; visual budget declared |
| B2 | Cognitive-load budget | 1 | ~17 elements on P1, 509 / 705 words per page; Montreal sparkline belongs to no decision; not-funded reasons appear twice | <= 9 elements and <= 180 words per page |
| B3 | Chart integrity | 1 | waterfall drawn with `zoom:true` (line 541): truncated axis; stacked area puts OTA on top so its share is read against the 100 % edge (DC-010); index line with 2 series x 3 points is a slope chart | variance bars from zero; OTA on the baseline or as lines |
| B4 | Color | 1 | accent `#c2690a` on panel 3.75-3.88:1 (fails AA text); white on accent 3.95:1; greys `#8c96a0` 2.86:1 and `#c3cad1` 1.57:1 fail the 3:1 non-text floor; blue `#2f63a8` is a second accent (hard rule 7) | accent-ink for text; greys >= 3:1; decide blue's status |
| B5 | Text and numbers | 1 | comp in Newsreader / Public Sans / IBM Plex Mono; contract says Georgia / Segoe UI / Consolas (three families; Consolas absent on macOS under Publish-to-Web); axis text renders at ~6 px | two families, real fonts, 12 pt body floor |
| B6 | Interaction | 1 | builder state visible, lamps, reset, empty state designed; benchmark and sparkline detail only in hover | nothing essential in hover (DC-040) |
| B7 | Uncertainty | 1 | Low-High band labelled on the cumulative curve; run-rate hero and NPV show one scenario; band meaning not stated | state once what the band is (DC-020) |
| B8 | Accessibility | **0** | no alt text (SVGs `role="img"` without labels), no tab order, contrast failures above | design input at s5, not a stage-7 pass |
| B9 | Mobile, localization | 0 | out of contest scope except the 1366-wide test | accepted gap |
| C1 | Semantic model (planned) | 1 | starter is a star; measure table, docstrings, parameterized source planned (MISSION §3); no calculation group or dynamic format strings for Low/Expected/High switching | format strings for the scenario toggle |
| C2 | Performance (planned) | 1 | Import; ~13 visuals on P1; 4 sparklines x 24 points; departures board as native matrix; Publish-to-Web test planned | budget per page; SVG only within DC-053 |
| C3 | Trust | 1 | footer states source, weighting and base-year rule (line 266); the same page breaks it (NPS "since 2021", line 537) and uses two margin definitions | consistent semantics |
| C4 | Security | 0 | Publish-to-Web is public by design | accepted; invisible to judges |
| C5 | Consistency, governance | 1 | no brand kit or theme yet; second hue; three type families; mixed card treatments (borderless tiles, bordered folio, dashed callout) | theme carries the system; one card style per page |
| C6 | Lifecycle | 1 | PBIP/TMDL in git, hooks and validators present | fine for a contest |
| C7 | AI readiness | 1 | docstrings planned | invisible to judges |
| C8 | Adoption | 0 | not applicable to a contest | accepted |

Total 17/40 → good. Caps: A2, B8.

## Contest compliance (blocker severity)

| Rule | Status in the comp |
|---|---|
| One brand, named on both pages | at risk: P2 masthead reads "THE MORNING PLAN · 2027-2032", no brand |
| Exactly two visible pages | ok (overlay and tooltip pages hidden) |
| Page names "The Brand Review" / "The Investment Strategy" | comp uses other names; keep the contest names as tab names, editorial titles inside |
| >= 3 initiatives, >= 1 growth, <= $60 M | ok (6 / 4 / $51.3 M) |
| Estimated costs **and expected returns** per initiative | **fail**: departures board has capex, dates, rooms, status, no return per initiative (annual OP impact, payback year) |
| Financial **and operational** impact through Dec 2032 | partial: rooms shown; `SatisfactionChangePts` not shown |
| Tie each initiative to a P1 finding | partial: move names imply it; nothing on P2 names the finding |
| Choices, risks, trade-offs explained | ok, but as ~170 words of bullets |
| >= 4 core visuals | ok |
| Provided data only; scenario logic labelled | ok in D1; a borrowed D3 fan needs its label on canvas |
| Publish-to-Web rendering | font risk (Consolas); nothing else non-native |

## Must change before the Nov 11 build (ordered)

1. **KPI records for every number on both pages** (A2, C3). One margin definition on the hero (or both margins on the card, as MISSION §4 specifies); one comparison base for the KPI band; a headline true under either margin ("Full, flat, and paying the middleman: 44 % before commissions, 34 % after"). Owner: `s2-metrics`, `definition-steward`. Verify: filled `contracts/metric.contract.yaml` for the four cards and every titled visual; the deltas share one base period.
2. **Canvas decided once and the comp re-rendered at it in the real fonts** (B5, hard rule 1). 1920x1080 (starter canvas, judges' monitors), 12 pt body floor so the 1366-wide test reads; Georgia + Segoe UI, drop the mono or keep it for figures only. Owner: `s5-design`, `px-prototype`. Verify: comp opens at the canvas with no font fallback; rect extraction runs clean; `project/design-prototypes/d1-wake-up-call.html` exists.
3. **One hero per page, half the elements, 180-word budget** (B1, B2). P1 hero = the middleman (stacked area with the $4.8 M/yr annotation on the chart, folio beside it); plateau collapses to one visual; the fading welcome shows room comfort vs years since refresh (r = -0.92) plus the renovation-spend bar ($0.98 M vs $5.9-7.9 M per hotel); the four sparklines become one line of three numbers with sparklines in a tooltip page. P2 hero = the impact chart (plan vs flat 2025-dollar baseline, cumulative net and payback as an on-chart annotation); six uniform impact numbers become one hero card plus a secondary row. Owner: `s5-design`, `ca-canvas`, `dataviz-polish` (moves 1, 3, 4, 7, S2, S4). Verify: element count and word count per page in the page-purpose contract; 3-second read gives the contracted sentence.
4. **Chart integrity** (B3). Waterfall as variance bars from zero ending at -$2.2 M (the native waterfall cannot reproduce a zoomed baseline); OTA on the baseline of the stacked area or shares as lines with OTA in amber; the index chart becomes a slope chart or a title clause. Owner: `chart-grounding` at s5. Verify: y-axis starts at zero; OTA first in the category order.
5. **Accessibility as a design input** (B8, B4). Accent text through `#8c4a06` or `#9a5008` (>= 5.6:1); greys >= 3:1 (`#7a8590`); stacked-area labels in ink outside the bands; blue registered as a semantic "our channel" token with a written reason, or dropped; alt-text sentence and tab order per visual in the page-purpose contracts. Owner: `bk-brand-kit`, `theme-from-brand-kit`, `ax-audit`. Verify: `scripts/check_contrast.py` passes every pair including overlay states; each page-purpose contract has an alt-text line per visual.
6. **The returns the contest requires, on the canvas** (compliance, A3). Departures board gains annual OP impact (Expected), payback year and the P1 finding it answers per initiative (consider a Gantt: initiative x 2027-2032, rooms-out shading); `SatisfactionChangePts` as the operational impact number; "Not funded" and "Risks" to one line each with the long form in the "How we calculated this" overlay; the $60.0 M foil as the fourth unfunded line. Owner: `s5-design`, `tb-tables`. Verify: every initiative row shows cost, return, payback and its P1 finding.
7. **P2 headline as a measure** (A4, creativity). "$51.3 M of $60 M on 6 projects: +$7.6 M a year by 2032 (Expected)" bound to the builder and scenario state, with a designed message when the plan is invalid or empty. Owner: `dax-patterns`, `pbir-operator` at s6. Verify: title changes with the slicer; empty state renders the designed message.
8. **Scenario switching keeps its formats** (C1, DC-056). If Low/Expected/High or metric switching is done through a field parameter or calculation group, dynamic format strings are specified at s3/s4 so currency and percentage never swap. Owner: `s3-model-design`, `tmdl-patterns`. Verify: format string expression present on the calculation items; a switched visual shows the right format in Desktop.
9. **Uncertainty stated once** (B7). The Low-High band's meaning (sum of per-project Low/High scenarios) printed near the curve; Low/High labels at the line ends instead of a subtitle note. Owner: `s5-design`. Verify: the sentence is on the page.
10. **Chrome and brand** (compliance, C5). "GOODNIGHT INN" in both mastheads; `z_*` footer identical on both pages including the dataset credit; one corner radius and one card treatment per page, declared in the handoff. Owner: `s5-design`, `s6-report-build`. Verify: fidelity review dimension 4.

Majors to fold into stage 5: designed states (builder with nothing ticked; scenario cleared to Expected via bookmark; Low = High collapse on cheap projects; the 40-character project name in the slicer); the 2021 renovation cohort marked on the dot strip; the folio kicker with the annual commission total; alt text drafted at s5, not s7.

## Accepted gaps

B9 mobile (only the 1366-wide test is in scope); C4 security (public by design); C7 and C8 (invisible to judges). C1 and C2 build findings are deferred to stages 3-4, with item 8 kept because it is decided at design time.

## Open questions

- Direction: the draft contract still reads `chosen: "<D1 | D2 | D3>"`, `user_decided: false`. D1 is favoured in the pitch; the decision and `chosen_because` are the user's to record (invariant 1).
- Does the do-nothing baseline go on the canvas (D3's fan borrowed into D1), and in constant 2025 dollars (recommended) or nominal from FinanceAssumptions?
- Disruption: total revenue or room revenue only?
- $8.7 M contingency vs funding GI-09?
- Is a dark surface allowed (affects D2 only)?
- Does the Nov 11 pbiviz go/no-go date stand?
- Which fonts the Power BI service ships for Publish-to-Web (research-first item; decides whether any third face survives).

## Timeline fit

G0-G2 (Nov 5-6): record the direction; KPI records (item 1). G3-G4 (Nov 6-7): item 8. G5 (Nov 8-10): items 2-7, 9, 10 in the comps and page-purpose contracts; re-score with this rubric before G5 closes (target >= 28/40 on the contract, no caps). Build Nov 11-14; G6 Nov 15; G7 Nov 16-17 with `ax-audit` and a final canon audit as delivery evidence.
