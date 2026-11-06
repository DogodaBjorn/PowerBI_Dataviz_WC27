# 05 - Repository audit and the new report set-up (opzet)

**Date:** 2026-11-06 · **Asked by:** Björn ("kijk of jij op basis van een volledige
doorlichting van de repository een nieuwe opzet van het op te leveren rapport kunt
bouwen") · **Stage:** 0 (intake in progress). This file records the audit, the
decisions it applies, the set-up that was built, and what is still open. It does
not close any gate; status.yaml is updated with a gate note only.

Built from: `01-richting-p1-p2.md` (P1/P2 direction), `02-focuswissel-methode.md`
and `04-p2-build-method.md` (the decided P2 method), `00-brand-decision.md` (kit
`goodnight-inn-hanger`), `00-best-in-class-audit.md` (the canon gaps), the contest
rules (`project/contest/`), and the organisers' workbook, downloaded 6 Nov into
`project/data/` (gitignored).

## 1. Audit: what the repository holds and where it disagrees with itself

### Verified true

| Check | Result | Evidence |
|---|---|---|
| The workbook reproduces the offline evidence | The crosscheck script run on the downloaded `PillowKey_Dataset.xlsx` gives output identical to the committed `output/crosscheck.txt` (byte-for-byte, trailing spaces aside) | `analysis/17_crosscheck_dutch_review.py` |
| Margins exclude distribution cost | Confirmed from the workbook's Contents sheet: MonthlyPerformance is "Monthly rooms, revenue and operating expenses per hotel (excludes distribution costs)". The 44.4 % / 33.7 % margin pair stands; the open "confirm the wording" item in MISSION §3 and SCOUT §6 is closed | `analysis/data/Contents.csv` (local) |
| 456 valid packages; presets A / B / C | Reproduced exactly: 456 of 1,024; A = 01+02+10, B = 01+09+10, C = 01+07+10 in the Expected lens, with the second opinion's values (A -5.5 / +3.3 / +12.7, B +2.7, C -23.4, 6 packages NPV-positive in Expected, 0 in Low) under the decided monthly discounting | `analysis/40_package_matrix.py`, `output/packages.txt` |
| Contest constraints | Unchanged: one brand, two visible pages (starter Read Me), >= 4 core visuals, <= $60 M, >= 3 initiatives with >= 1 growth, impact through 2032, provided data only, accessibility scored, Publish-to-Web | `MISSION-goodnight-inn.md` §1 |

### Inconsistencies found (each with the action taken)

| # | Finding | Action |
|---|---|---|
| A1 | **Two page maps in force.** `MISSION` §2/§4 (and `CLAUDE.md`'s pointer to it as "stage-0 source of truth") still describe the "Wake-up call" KPI band, three story columns and the plan builder. `01-richting-p1-p2.md` (6 Nov) supersedes them: P1 = factual four-brand comparison plus geography, P2 = package scatter with focus swap. The three sketch reports D1-D3 were built on the superseded map. | The new set-up follows 01/02/04. MISSION and the sketches stay as history; nothing deleted. Suggest a one-line "superseded by 01-richting for the page map" note in MISSION (not done: Björn's file). |
| A2 | **"The group starved the brand" does not survive the cross-brand view.** Goodnight Inn's median years since refresh is **7** against 8-9 at the sisters; only **22 %** of its hotels are 10+ years since refresh against 40-48 %. The low dollars per hotel ($0.98 M vs $5.9-7.9 M) are a segment effect (130-room budget inns). What holds: no renovation started since December 2020, and *within* the brand comfort falls with refresh age (r = -0.92; the ten oldest score 6.69 vs 7.29). | P1 makes no causal starvation claim (01-richting already asked for this nuance). The headline "Do not disturb, since 2020." stays (literally true); the subtitle states the date, not a cause. `brand-guide.md` §1 ("The product is tired") and MISSION E17 still carry the old framing: flagged, not edited. |
| A3 | **Two NPV conventions.** The sketch model discounted annual buckets (plan A -29.5); 04-p2-build-method decided monthly discounting (-31.1 / -31.3). | Model unified on the decided convention: `ProjectCashflow[DiscountFactor]` = 1.08^-(k/12), k = months after January 2027; `NPV @ 8%` uses it. The D1/D3 sketch NPV figures move accordingly (plan A -29.7 -> -31.3). |
| A4 | **GI-02 sequencing missing in the model.** Kiosks (GI-02) depend on the app (GI-01) but started January 2027 in `ProjectCashflow`. | New column `InvestmentProjects[Planned Start]`: a project with a DependsOn starts when its prerequisite goes live (GI-02: October 2027, live April 2028). Generic, so P&K Select's PS-01 -> PS-03 follows the same rule. |
| A5 | **Presets move with the scenario lens.** B in High = 01+02+09+10; C in Low = 01+02+07, in High = 01+02+07+10. A fixed "B = 01+09+10" label would be wrong outside Expected. | Presets are rules evaluated in DAX (`Preset A/B/C Package`), as 04 says: "the rules, not the points, are recorded". |
| A6 | **Dangling references on main.** `01-richting` and the focus-swap research log cite `project/contest/page-count-ruling.md` and `PITCH-D4-what-if-merged.md`; both live only on the open, unmerged PR #2. | Not fixed here (PR #2 is Björn's call); recorded so the references are not trusted as present. |
| A7 | **Canvas and theme drift in the sketches.** D1-D3 are 1280x720 with their own navy/amber palettes; the chosen kit assumes 1920x1080 and its compiled theme (`deliverables/theme.json`) is applied nowhere. `creative-direction.draft.yaml` still describes all directions in navy/amber/Georgia. | The new report is 1920x1080 on the compiled kit theme. The draft contract is left for stage 5. |
| A8 | **Comps referenced but absent.** `creative-direction.draft.yaml` and the canon audit point at `project/design-prototypes/d1..d3*.html`; none exist. | `project/design-prototypes/` now holds the opzet comp, its slot map and @2x references. |
| A9 | **No metric contracts yet** (canon audit cap A2) and no page-purpose contracts. | Not written here (stage 1-2 work). §4 lists every number on the canvas with its measure, so the contracts have a ready inventory. |
| A10 | **Tooling gaps.** `pbir_lib.filter_topn` writes a TopN shape that fails Microsoft's semanticQuery schema (it was never used, so the sketches are unaffected); `scripts/prototype/extract_layout.mjs` measures in a 1600x1200 viewport, smaller than this project's canvas. | Project-local fixes: a schema-valid TopN in `tools/opzet_report.py`; `tools/opzet_capture.mjs` measures at 1920x1080 and checks every slot against the slot map. The framework tool is template-repo work. |
| A11 | **Map visual risk.** Community threads report that the Azure Maps visual does not render under Publish to web (no Microsoft Learn page found, Learn is not reachable from this environment). | Geography is a native matrix plus a bar chart, not a map. Recorded as open question 5. |

## 2. The new set-up (what was built)

Files (all reproducible from the repo root):

| Artefact | Path | Made by |
|---|---|---|
| Package matrix, project economics, yearly flows | `project/analysis/output/packages.{txt,csv}`, `project_economics.csv`, `project_yearly.csv` | `python -I project/analysis/40_package_matrix.py project/analysis/data project/analysis/output` |
| Facts for the comp | `project/design-prototypes/opzet-data.json`, `analysis/output/opzet_facts.txt` | `analysis/41_opzet_facts.py` |
| Slot map (single source of positions) | `project/design-prototypes/opzet-layout.json` | hand-designed on the 8 px grid |
| HTML comp, three screens | `project/design-prototypes/opzet-goodnight-inn.html` | `python project/tools/build_opzet_comp.py` |
| @2x references and slot check | `project/design-prototypes/reference_screenshots/opzet-*.png`, `opzet-layout-check.json` | `node project/tools/opzet_capture.mjs` (0 slot deviations, 0 overflows) |
| Page backgrounds (cards + lockup) | `project/deliverables/backgrounds/*.{svg,png}` | `node project/tools/opzet_backgrounds.mjs` |
| Semantic model additions | `project/pbip/PillowKey.SemanticModel` | `python project/tools/sketch_model.py` |
| The report | `project/pbip/GoodnightInn-opzet.pbip` + `.Report` | `python project/tools/opzet_report.py` |
| Schema validation | n/a | `python project/tools/schema_check.py <files>` (Microsoft json-schemas) |

### P1 · The Brand Review: "Do not disturb, since 2020."

3-second message: *the fullest rooms and the widest margin before commissions; last
of four brands on guests, channels and complaints.* Reading order = tab order:
headline > subtitle > comparison table > geography > three trends > footer.

| Slot | Visual | Bound to | Why it is there |
|---|---|---|---|
| `hero_brand_compare` | table, 13 lines x 4 brands + rank + change since 2023, grouped F1-F3 | `KpiLine`, `KPI Text GI/PS/MO/PP`, `KPI Rank (text)`, `KPI Change since 2023 (text)` | the factual comparison 01-richting asks for: matrix first. Rank is a word ("last of 4"), color repeats it (Harbour / Ember), ADR and RevPAR shown but not ranked (segment) |
| `tbl_geo` | matrix, region x location type, occupancy and hotel count, three-step tint | `Occupancy and Hotels (text)`, `Occupancy Heat Color` | F4, the geography: airports 82.0 %, highway 77.5 % |
| `ch_fullest_hotels` | bar, top 7 by 2025 occupancy, airports in raspberry | `Occupancy % 2025`, `Hotel Bar Color` | where the brand is full (five of seven are airports) |
| `ch_trend_margin`, `ch_trend_ota`, `ch_trend_nps` | lines 2021-2025, Goodnight Inn raspberry, sisters plum-slate | `Trend * GI/PS/MO/PP`; titles from `Trend Title * (text)` | F1-F3 over time: margin after commissions 36.5 % (2023) -> 33.7 %; OTA share 33.0 % -> 50.0 % while the sisters stayed at 23-36 %; NPS down every year to +3.3 |

Findings carry codes so P2 can answer them: **F1** full, margin slipping · **F2**
paying the middleman · **F3** the weakest welcome · **F4** full at the airports.

### P2 · The Investment Strategy: "Please make up the room."

Built exactly to `04-p2-build-method.md`: native visuals only, one persistent
scatter, one disconnected package selector (`PlanSelector`), one disconnected
scenario selector, two panel states swapped by display-only bookmarks.

| Slot | Visual | Bound to |
|---|---|---|
| `hero_packages` | scatter of the 456 packages, X capex, Y NPV through 2032 (selected scenario), zero line; raspberry = in focus, plum = no refresh, lilac-grey = with refresh | `Package`, `Package NPV (sel)`, `Package Point Color/Size` |
| `sl_scenario`, `sl_package` | Low / Expected / High tiles; dropdown with A / B / C first, then every package | `Scenario`, `PlanSelector[Label]` |
| shortlist state | three preset tiles: criterion, composition, capex, NPV, Low-High range, 2032 run-rate; the standing uncertainty line; button to the plan | `Preset A/B/C *`, `Uncertainty (text)`, `bm_p2_plan` |
| plan state (hidden by default) | title, waterfall of NPV per initiative, initiative table (finding answered, capex, live, run-rate, NPV, dataset guest points), cumulative net Low / Expected / High, rooms added / refreshed / hotels rated, risk sentence, back button | `Focus *`, `Plan Title (text)`, `Plan Risk (text)`, `bm_p2_shortlist` |

Contest coverage on P2: >= 3 initiatives and >= 1 growth (validity rules of every
point), within $60 M (validity and subtitle), costs and returns per initiative
(table, waterfall), financial and operational impact through 2032 (cumulative
chart, run-rate, rooms, hotels rated), choices/risks/trade-offs (preset criteria,
risk sentence, uncertainty line), each initiative tied to a P1 finding (`Answers
Finding`). Core visuals: 10 tables/charts across both pages (minimum 4).

### Conventions recorded (the canvas states them)

- NPV: constant 2025 dollars, monthly flows discounted at the FinanceParameters rate
  (8 %) to January 2027, through December 2032, no residual value.
- Disruption: rooms out of service lose that share of the mapped hotels' 2025 total
  revenue during works, no cost relief (unchanged from the sketches).
- Dependent projects start when the prerequisite goes live.
- Package values are sums of initiative values (the dataset has no interaction terms;
  overlap remains a stated uncertainty, per 01-richting).
- Guest effect: `SatisfactionChangePts` per initiative on its touched hotels; never
  summed into NPS (01-richting).

## 3. Verification so far

| Check | Result |
|---|---|
| `validate_tmdl.py --strict` on the regenerated model | 0 errors, 0 warnings (dry run) |
| `validate_json.py`, `pbir_detect.py` on the new report | 0 errors; taste-lint PASS, 0 findings (dry run) |
| Microsoft json-schemas (pages, visual containers, filters, bookmarks, report) | 57 / 57 files valid (dry run) |
| Comp slot check (every visual within +-2 px of the slot map) | 0 deviations, 0 overflows |
| DAX evaluation | **not run**: no Power BI engine in this environment. The offline scripts are the reference the model must reproduce. |

The pbir-operator's run inside `project/pbip/` is recorded in the commit that adds
this file.

## 4. Desktop checks still owed (each with its fallback)

1. **Refresh the model** (DataFile blob), then check: `Package` has 456 rows;
   preset A = 01+02+10 at +$3.3 M Expected; `NPV @ 8%` for 01+02+04+05+07+10 =
   -$31.3 M; no circular-dependency error on Package / PackageProject / PlanSelector
   (all read `ALLNOBLANKROW`). Fallback if Desktop reports a cycle: materialize
   `Package` from `analysis/output/packages.csv` logic as a Power Query step over the
   same provided tables.
2. **Focus-swap proof** (`03-focuswissel-testplan.md`, tests 1-4) can now run on this
   report itself, not only on a separate proof file: pick a package, swap states,
   swap back.
3. **VERIFY shapes** in `opzet_report.py`: page background image (fallback: set it in
   Format page from `deliverables/backgrounds/`), scatter field-value color (fallback:
   second series, as 04 decides), title bound to a measure (fallback: a card above the
   chart), constant line at zero (fallback: the subtitle sentence), action-button text
   and fill objects (fallback: format in Desktop, the bookmark link itself is
   schema-checked), table field-value font and background colors.
4. **Fonts:** Trebuchet MS and Verdana in Desktop's font menu; a column of 1s and 8s
   right-aligned in Verdana (00-brand-decision open question).
5. **Publish-to-Web** at 1920x1080 and 1366 width, both P2 states.
6. **Logo state on P2:** the kit wants the awake hanger on P2; only the sleeping
   lockup exists as a lockup. Needs an awake lockup from `brand_logos.py`.

## Open questions (for Björn)

1. **Which package does the Board get as the recommendation?** The method shows three
   rules and defaults to A (01+02+10: $9.4 M, +$3.3 M NPV, answers F1, F2, F3-check-in),
   which leaves $50.6 M unspent and the oldest rooms (F3) and the full airports (F4)
   unanswered. C (01+07+10: $36.9 M, -$23.4 M through 2032, no value after 2032
   counted) answers F3 at a stated in-horizon cost. The contest asks for a
   recommendation; the canvas currently presents a choice. Suggestion: name one
   preset as "our recommendation" with one sentence of why, keep the other two as the
   trade-off.
2. Keep the brand-guide sentence "The product is tired" and MISSION E17 as they are,
   or correct them to the within-brand reading (A2)?
3. Merge or close PR #2 so the page-count ruling the 6 Nov files cite is on main (A6).
4. The D1-D3 sketches: keep as history, or retire them now that the opzet uses the
   decided direction?
5. Map: accept the matrix-plus-bars geography, or test a map visual under
   Publish-to-Web first (A11)?
