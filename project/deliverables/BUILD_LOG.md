# BUILD_LOG — PowerBI_Dataviz_WC27 (Goodnight Inn, DVWC27 Round 1)

<!-- Maintained DURING stages 4 and 6 by the build-log skill. A reader who
never saw the chat must learn from this file: what exists, what remains
manual, which numbers rest on assumptions, when it was last validated. -->

Last validated: 2026-11-07, v2 "D1 briefing, stripped" (summary below; rendered and queried in Power BI Desktop 2.159, Oct 2026)
Model: `PillowKey.SemanticModel`, 27 tables, 260 measures, 22 relationships (shared by all four reports)
Report: `GoodnightInn-opzet.Report`, 2 pages at 1920x1080, 68 visuals (P1 39, P2 29, of which 7 cards, 2 logos and 12 KPI-cell parts), 9 core chart/table visuals, 2 bookmarks.
Also on disk: the three direction sketches D1/D2/D3 (`project/pbip/SKETCHES.md`), not rebuilt in this pass.

Lifecycle note: `status.yaml` still says stage 0. This is a pre-gate opzet (set-up)
pass. The generators are the source of truth, so do not hand-edit the generated
JSON/TMDL; edit `project/tools/sketch_model.py` / `project/tools/opzet_report.py` and
regenerate.

## Built

| Date | Scope | Items |
|---|---|---|
| 2026-11-07 | v2: back to the D1 briefing, stripped (`06-d1-briefing-opzet.md`; `opzet-layout.json` v2, `sketch_model.py`, `opzet_report.py`, `opzet_backgrounds.mjs`, `build_opzet_comp.py`, `41_opzet_facts.py`) | **P1** (39 visuals): message headline, a KPI band (`kpi_occ`, `kpi_margin`, `kpi_ota`, `kpi_nps`, each label + value + one comparison), F1 `ch_f1_margin` (margin before vs after commissions), F2 `ch_f2_ota` + the folio `tbl_f2_folio`, F3 `ch_f3_age` (NPS by years since the last renovation, dated hotels only), F4 `c_f4_types` + `ch_f4_fullest`; titles and notes are measures. The 13-row table, the geography matrix and the three trend charts are gone. **P2** (29 visuals): headline = the recommendation; the scatter keeps the focus swap, gets one fixed NPV axis for all scenarios (-$60M to +$20M from `packages.csv`) and smaller markers; the shortlist state is one recommendation block (`c_rec_*`) plus `c_alt_b`, `c_alt_c`, `c_not_funded`, `c_uncertainty`. No tiles: cards are now textbox visuals under the content (`z_card_*`) and the lockup an image visual (`z_logo`, asleep P1 / awake P2); the page background is colour only. **Model**: `Recommended Package` (highest NPV in Expected, fixed across scenarios; PlanSelector A points at it), KPI band, F1-F4 title/note, `Rec *`, `Alt B/C`, `Not Funded`, `Headline P2`, `Footer P2` measures; `Hotels[Renovation Age Sort]` / `[Renovation Age Label]`; FolioLine rows renamed; `USDM1` / `SUSDM` format strings corrected. **Facts**: folio, 2021-mix counterfactual and age bands added to `opzet-data.json`. |
| 2026-11-06 | first Desktop open: two load errors fixed (`sketch_model.py`, `opzet_report.py`, plus the generated `Package.tmdl` and `ch_fullest_hotels/visual.json`) | **Model:** `Package` failed with "De syntaxis voor Rows is onjuist": `Rows` is a reserved DAX word (visual-calculation axis), so `VAR Rows` is now `VAR PkgRows`. `PackageProject` and `PlanSelector` only failed through `Package`. Checked in Desktop with the corrected expression as a query: 456 packages; 01+02+04+05+07+10 gives capex $51.3 M, 27 hotels rated, NPV Expected -$31,295,462 and run-rate Expected $7.58 M, all equal to `project/analysis/output/packages.csv`. **Report:** the `flt_top7` TopN filter on `ch_fullest_hotels` crashed Desktop (`SemanticQueryRewriter.rewriteOrderBy`, "Cannot read properties of undefined (reading 'accept')"). Its subquery OrderBy pointed at `{"Entity": "_Measures"}` without declaring it in the subquery's `From`. `_Measures` is now declared as alias `m` and referenced as `{"Source": "m"}`. Not yet re-rendered in Desktop after the fix. |
| 2026-11-06 | brand-kit pass, goodnight-inn-hanger `brand-guide.md` sections 2-6 (`sketch_model.py`, `opzet_report.py`, `opzet-layout.json`, `opzet_backgrounds.mjs`) | **Model:** `KpiLine` regrouped along the brand promise (`F2 · Booked with us?`, `F3 · A good night?` / `A fair price?` / `Recommend us?`; rows re-sorted to comfort, roomcond, compl, value, nps). `KPI Rank (text)` now reads ▲ best of n / ▼ last of n (`UNICHAR(9650/9660)`). `Trend Title Margin/OTA/NPS (text)` shortened. 7 new measures in `09 Package matrix`: `Initiative Chip` (inline SVG data URI, `dataCategory: ImageUrl`), `Initiative Status (text)`, `Initiative Status Color`, `Initiative Capex`, `Initiative NPV (sel)`, `Initiative Run-rate (sel)`, `Initiative Guest Effect (text)`. Contrast fix: `Package Point Color` with-refresh dots `#B8B0BE` to plum-slate `#82798A`. **Report:** kit type floor (captions 13 px / 10 pt, body 11 pt, headline 37 px = 28 pt on `z_headline`, `z_headline2`); shorter trend titles and `z_footer` / `z_footer2`; P2 panel widened to 800 px (content x 1112, width 752: `z_tile_preset_a/b/c`, `ch_plan_waterfall`, `tbl_plan_initiatives`, `ch_plan_cumulative`, `c_plan_ops`). `tbl_plan_initiatives` now lists all ten Goodnight Inn initiatives (focus filter removed; the P2 page filter keeps Brand = Goodnight Inn), columns chip, Status, Initiative, Answers, Capex, Live, Run-rate, NPV, Guest pts; Status font colour from `Initiative Status Color`. `ch_plan_cumulative`: Low / High as 1 px raspberry hairlines, Expected 2 px raspberry. `bg-p2-investment-strategy.png` re-rendered with the awake hanger. Changed: 41 visual.json, P2 `page.json`, P2 background. Unchanged: `c_subtitle`, `c_compare_title`, `c_geo_title`, `ch_fullest_hotels`, `c_subtitle2`, P1 background, both bookmarks. |
| 2026-11-06 | report `GoodnightInn-opzet` (new, `opzet_report.py`) | P1 `p1-brand-review`: `z_masthead`, `z_headline`, `c_subtitle`, `c_compare_title`, `c_compare_sub`, `hero_brand_compare`, `c_geo_title`, `c_geo_sub`, `tbl_geo`, `ch_fullest_hotels`, `c_full_title`, `ch_trend_margin`, `ch_trend_ota`, `ch_trend_nps`, `z_footer`. P2 `p2-investment-strategy`: `z_masthead2`, `z_headline2`, `c_subtitle2`, `sl_scenario`, `sl_package`, `c_scatter_title`, `c_scatter_sub`, `hero_packages`, `c_short_title`, `z_tile_preset_a/b/c`, `c_preset_a/b/c_head`, `c_preset_a/b/c_mix`, `c_preset_a/b/c_nums`, `c_uncertainty`, `btn_open_plan`, `c_plan_title`, `ch_plan_waterfall`, `tbl_plan_initiatives`, `ch_plan_cumulative`, `c_plan_ops`, `c_plan_risk`, `btn_back`, `z_footer2`. Bookmarks `bm_p2_shortlist` (hides the 7 plan visuals) and `bm_p2_plan` (hides the 15 shortlist visuals), display-only (`suppressData`, target visuals only). Page backgrounds `bg-p1-brand-review.png`, `bg-p2-investment-strategy.png` (byte-identical to `project/deliverables/backgrounds/`). |
| 2026-11-06 | model (`sketch_model.py`) | `InvestmentProjects`: new `Planned Start`, new `Answers Finding`, `Completion Date` now from `Planned Start`. `ProjectCashflow`: start from `Planned Start`, new `DiscountFactor`. New tables `KpiLine`, `Package`, `PackageProject`, `PlanSelector`. New relationships `PackageProject[PackageID]` to `Package[PackageID]`, `PackageProject[ProjectID]` to `InvestmentProjects[ProjectID]`. 92 new measures (`08 Brand comparison` 38, `09 Package matrix` 52, `03 Guest`: `Value for Money (weighted)`, `Room Condition Complaints per 1k`). `NPV @ 8%` redefined. |

## Decisions & assumptions

- 2026-11-06: `NPV @ 8%` now discounts monthly to January 2027 via `ProjectCashflow[DiscountFactor]`, through 2032, no terminal value (convention in `project/project-state/active/04-p2-build-method.md`). It replaces the annual discount to 2026.
- 2026-11-06: GI-02 starts when GI-01 goes live (`InvestmentProjects[Planned Start]` = later of own earliest start and the prerequisite's go-live). This shifts GI-02's cashflow in `ProjectCashflow`.
- 2026-11-06: the model is shared, so both changes above also apply to the D1/D2/D3 sketches. Their bindings all still resolve (field-reference check: 0 unresolved), but their NPV, payback and timing numbers will differ from the figures recorded in `project/pbip/SKETCHES.md` (e.g. NPV at 8 % -$29.5 M) after the next refresh. `05-doorlichting-nieuwe-opzet.md` expects -$31.3 M for 01+02+04+05+07+10.
- 2026-11-06: the scatter's with-refresh dots (`hero_packages`, `Package Point Color`) use plum-slate `#82798A` instead of the kit's lilac-grey `#B8B0BE`. The colour carries meaning, so it has to clear the 3:1 non-text contrast floor: `#82798A` is 4.16:1 on Sheet `#FFFFFF`, while `#B8B0BE` is only 2.1:1. This is a deliberate deviation from the brand kit.
- Preset packages and scenario defaults: see `project/project-state/active/05-doorlichting-nieuwe-opzet.md`. SCENARIO CHOICE: `sl_scenario` defaults to `Expected`.
- 2026-11-07: the recommendation is package A, 01+02+10 (Björn; `06-d1-briefing-opzet.md`). `Recommended Package` derives it as the highest NPV in Expected rather than typing the id, and it stays fixed when the scenario changes; only its numbers follow the scenario.
- 2026-11-07: "pays back by 2032" means NPV through 2032 at least zero, everywhere (scatter, `Alt C`, `Not Funded`).
- 2026-11-07: the fading welcome uses dated hotels only (44 of 50), weighted by survey responses: +6.8 / +3.8 / -4.9. MISSION E10 had +6.8 / +4.0 / -4.6; the difference is the weighting. The six never-renovated hotels are left out rather than given their opening date.
- 2026-11-07: number words in text measures use explicit division (`fm()` / `sfm()` in `sketch_model.py`). DAX `FORMAT()` with the `,,` scaling form printed "$4,806,360.8M".
- 2026-11-07: Desktop shows measure-formatted numbers in the machine's locale (nl-NL: "79,4%") and `FORMAT()` text in the model's culture (en-US: "64.7%"). Under Publish to Web the viewer's locale decides. For a consistent preview in Desktop, set File > Options > Regional settings to English (United States).

## Manual steps required in Desktop

Source list with fallbacks: `project/project-state/active/05-doorlichting-nieuwe-opzet.md` section 4.

Checked in Desktop on 7 Nov through the Desktop bridge (renders at 3x of a 540 px-wide display) and the Modeling MCP (DAX):

- [x] Model loads with 0 partition errors; `Package` 456 rows; A = 01+02+10, NPV +$3,276,891 / Low -$5.47M / High +$12.72M, run-rate $3.529M, all equal to `packages.csv`; folio, age bands and KPI band equal to `opzet-data.json`; titles and notes read correctly in Low, Expected and High
- [x] Zero line on the scatter; field-value colours on scatter, F3 and F4; ▲ / ▼ glyphs in Verdana
- [x] Action buttons show their text and fill (with `show` outside the state selector)
- [x] `Initiative Chip` renders as an image at 28 x 20 px; all ten initiatives fit `tbl_plan_initiatives` (plan state, rendered from a throwaway `--plan-state` copy)
- [x] Asleep lockup on P1, awake on P2, as image visuals
- [ ] Focus-swap proof (`03-focuswissel-testplan.md` tests 1-4) — P2 — verify by: package and scenario selections survive both bookmark swaps (needs clicks; the bridge cannot click)
- [ ] Fonts Trebuchet MS / Verdana present and figures align — both pages
- [ ] Publish-to-Web render at 1920x1080 and 1366 wide, both P2 states
- [ ] Re-check D1/D2/D3 headline numbers after refresh and update `SKETCHES.md` (shared-model change)
- [ ] Rendered review per page (fonts, clipping, interactions) — see 07 checklist

## Validation status

```
2026-11-07, v2 (all three generators re-run)
validate_tmdl --strict : 31 file(s), 0 error(s), 0 warning(s)
validate_json (opzet)  : 77 file(s) checked, 0 with errors
MS json-schema check   : 76 files, 0 failing
pbir_detect opzet      : 68 visuals, 0 findings -> PASS
pbir validate (0.9.33) : warnings only (visual count per page, schema 2.11 resolved to bundled 2.13, undersized-card heuristics on text cards)
Desktop                : model loads, 0 partition errors; both pages and the P2 plan state rendered and reviewed
```

```
2026-11-06, after the brand-kit pass incl. the Package Point Color contrast fix (both generators re-run)
validate_tmdl --strict : 31 file(s), 0 error(s), 0 warning(s)
validate_json (repo)   : 161 file(s) checked, 0 with errors
validate_json (pbip)   : 150 file(s) checked, 0 with errors
pbir_detect opzet      : 46 visuals, 0 findings -> PASS
pbir_detect all        : 4 reports (D1 35, D2 20, D3 22, opzet 46 visuals), 0 findings -> PASS
MS json-schema check   : 57 files, 0 failing (opzet .Report + .pbip)
check_state            : state OK, stage 0 (s0_intake, in_progress)
grid / naming          : 46 visuals on the 8 px grid, all prefixes valid, both pages 1920x1080, bookmarks bm_p2_*
field references       : opzet 112, D1 92, D2 68, D3 61, 0 unresolved against the TMDL
D1/D2/D3 report files  : 104 files byte-unchanged
type floor             : no visible text below 10 pt / 13 px (only a hidden value axis at 9 pt on ch_fullest_hotels and empty tile runs on z_tile_preset_*)
```

## Known limitations

- The Desktop renders on 7 Nov came from a 540 px-wide display. A page background image with Fit drifted off the visuals there, because Desktop scaled the canvas non-uniformly. That is why cards and logo are visuals now. A full-size review on a normal screen and under Publish to Web is still owed.
- Logo on P2: the awake lockup is derived (the kit's lockup with the awake mark's eyes), not a kit asset. Retire the derivation in `opzet_backgrounds.mjs` once `brand_logos.py` emits `goodnight-inn-lockup-awake.svg` (05, check 6).
- The pre-v2 opzet measures (`KPI Text *`, `Trend Title *`, `Preset A *`, `Shortlist Title`, `Subtitle P1`, `Geo Title`) are no longer bound to the opzet report but stay in the shared model.
