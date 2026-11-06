# BUILD_LOG — PowerBI_Dataviz_WC27 (Goodnight Inn, DVWC27 Round 1)

<!-- Maintained DURING stages 4 and 6 by the build-log skill. A reader who
never saw the chat must learn from this file: what exists, what remains
manual, which numbers rest on assumptions, when it was last validated. -->

Last validated: 2026-11-06, after the brand-kit pass (summary below; headless only, no Desktop render yet)
Model: `PillowKey.SemanticModel`, 27 tables, 227 measures, 22 relationships (shared by all four reports)
Report: `GoodnightInn-opzet.Report`, 2 pages at 1920x1080, 46 visuals (P1 15, P2 31), 10 core chart/table visuals, 2 bookmarks.
Also on disk: the three direction sketches D1/D2/D3 (`project/pbip/SKETCHES.md`), not rebuilt in this pass.

Lifecycle note: `status.yaml` still says stage 0. This is a pre-gate opzet (set-up)
pass. The generators are the source of truth, so do not hand-edit the generated
JSON/TMDL; edit `project/tools/sketch_model.py` / `project/tools/opzet_report.py` and
regenerate.

## Built

| Date | Scope | Items |
|---|---|---|
| 2026-11-06 | first Desktop open: two load errors fixed (`sketch_model.py`, `opzet_report.py`, plus the generated `Package.tmdl` and `ch_fullest_hotels/visual.json`) | **Model:** `Package` failed with "De syntaxis voor Rows is onjuist": `Rows` is a reserved DAX word (visual-calculation axis), so `VAR Rows` is now `VAR PkgRows`. `PackageProject` and `PlanSelector` only failed through `Package`. Checked in Desktop with the corrected expression as a query: 456 packages; 01+02+04+05+07+10 gives capex $51.3 M, 27 hotels rated, NPV Expected -$31,295,462 and run-rate Expected $7.58 M, all equal to `project/analysis/output/packages.csv`. **Report:** the `flt_top7` TopN filter on `ch_fullest_hotels` crashed Desktop (`SemanticQueryRewriter.rewriteOrderBy`, "Cannot read properties of undefined (reading 'accept')"). Its subquery OrderBy pointed at `{"Entity": "_Measures"}` without declaring it in the subquery's `From`. `_Measures` is now declared as alias `m` and referenced as `{"Source": "m"}`. Not yet re-rendered in Desktop after the fix. |
| 2026-11-06 | brand-kit pass, goodnight-inn-hanger `brand-guide.md` sections 2-6 (`sketch_model.py`, `opzet_report.py`, `opzet-layout.json`, `opzet_backgrounds.mjs`) | **Model:** `KpiLine` regrouped along the brand promise (`F2 · Booked with us?`, `F3 · A good night?` / `A fair price?` / `Recommend us?`; rows re-sorted to comfort, roomcond, compl, value, nps). `KPI Rank (text)` now reads ▲ best of n / ▼ last of n (`UNICHAR(9650/9660)`). `Trend Title Margin/OTA/NPS (text)` shortened. 7 new measures in `09 Package matrix`: `Initiative Chip` (inline SVG data URI, `dataCategory: ImageUrl`), `Initiative Status (text)`, `Initiative Status Color`, `Initiative Capex`, `Initiative NPV (sel)`, `Initiative Run-rate (sel)`, `Initiative Guest Effect (text)`. Contrast fix: `Package Point Color` with-refresh dots `#B8B0BE` to plum-slate `#82798A`. **Report:** kit type floor (captions 13 px / 10 pt, body 11 pt, headline 37 px = 28 pt on `z_headline`, `z_headline2`); shorter trend titles and `z_footer` / `z_footer2`; P2 panel widened to 800 px (content x 1112, width 752: `z_tile_preset_a/b/c`, `ch_plan_waterfall`, `tbl_plan_initiatives`, `ch_plan_cumulative`, `c_plan_ops`). `tbl_plan_initiatives` now lists all ten Goodnight Inn initiatives (focus filter removed; the P2 page filter keeps Brand = Goodnight Inn), columns chip, Status, Initiative, Answers, Capex, Live, Run-rate, NPV, Guest pts; Status font colour from `Initiative Status Color`. `ch_plan_cumulative`: Low / High as 1 px raspberry hairlines, Expected 2 px raspberry. `bg-p2-investment-strategy.png` re-rendered with the awake hanger. Changed: 41 visual.json, P2 `page.json`, P2 background. Unchanged: `c_subtitle`, `c_compare_title`, `c_geo_title`, `ch_fullest_hotels`, `c_subtitle2`, P1 background, both bookmarks. |
| 2026-11-06 | report `GoodnightInn-opzet` (new, `opzet_report.py`) | P1 `p1-brand-review`: `z_masthead`, `z_headline`, `c_subtitle`, `c_compare_title`, `c_compare_sub`, `hero_brand_compare`, `c_geo_title`, `c_geo_sub`, `tbl_geo`, `ch_fullest_hotels`, `c_full_title`, `ch_trend_margin`, `ch_trend_ota`, `ch_trend_nps`, `z_footer`. P2 `p2-investment-strategy`: `z_masthead2`, `z_headline2`, `c_subtitle2`, `sl_scenario`, `sl_package`, `c_scatter_title`, `c_scatter_sub`, `hero_packages`, `c_short_title`, `z_tile_preset_a/b/c`, `c_preset_a/b/c_head`, `c_preset_a/b/c_mix`, `c_preset_a/b/c_nums`, `c_uncertainty`, `btn_open_plan`, `c_plan_title`, `ch_plan_waterfall`, `tbl_plan_initiatives`, `ch_plan_cumulative`, `c_plan_ops`, `c_plan_risk`, `btn_back`, `z_footer2`. Bookmarks `bm_p2_shortlist` (hides the 7 plan visuals) and `bm_p2_plan` (hides the 15 shortlist visuals), display-only (`suppressData`, target visuals only). Page backgrounds `bg-p1-brand-review.png`, `bg-p2-investment-strategy.png` (byte-identical to `project/deliverables/backgrounds/`). |
| 2026-11-06 | model (`sketch_model.py`) | `InvestmentProjects`: new `Planned Start`, new `Answers Finding`, `Completion Date` now from `Planned Start`. `ProjectCashflow`: start from `Planned Start`, new `DiscountFactor`. New tables `KpiLine`, `Package`, `PackageProject`, `PlanSelector`. New relationships `PackageProject[PackageID]` to `Package[PackageID]`, `PackageProject[ProjectID]` to `InvestmentProjects[ProjectID]`. 92 new measures (`08 Brand comparison` 38, `09 Package matrix` 52, `03 Guest`: `Value for Money (weighted)`, `Room Condition Complaints per 1k`). `NPV @ 8%` redefined. |

## Decisions & assumptions

- 2026-11-06: `NPV @ 8%` now discounts monthly to January 2027 via `ProjectCashflow[DiscountFactor]`, through 2032, no terminal value (convention in `project/project-state/active/04-p2-build-method.md`). It replaces the annual discount to 2026.
- 2026-11-06: GI-02 starts when GI-01 goes live (`InvestmentProjects[Planned Start]` = later of own earliest start and the prerequisite's go-live). This shifts GI-02's cashflow in `ProjectCashflow`.
- 2026-11-06: the model is shared, so both changes above also apply to the D1/D2/D3 sketches. Their bindings all still resolve (field-reference check: 0 unresolved), but their NPV, payback and timing numbers will differ from the figures recorded in `project/pbip/SKETCHES.md` (e.g. NPV at 8 % -$29.5 M) after the next refresh. `05-doorlichting-nieuwe-opzet.md` expects -$31.3 M for 01+02+04+05+07+10.
- 2026-11-06: the scatter's with-refresh dots (`hero_packages`, `Package Point Color`) use plum-slate `#82798A` instead of the kit's lilac-grey `#B8B0BE`. The colour carries meaning, so it has to clear the 3:1 non-text contrast floor: `#82798A` is 4.16:1 on Sheet `#FFFFFF`, while `#B8B0BE` is only 2.1:1. This is a deliberate deviation from the brand kit.
- Preset packages, recommendation choice and scenario defaults: see `project/project-state/active/05-doorlichting-nieuwe-opzet.md` (open question 1 is still open). SCENARIO CHOICE: `sl_scenario` defaults to `Expected`.

## Manual steps required in Desktop

Source list with fallbacks: `project/project-state/active/05-doorlichting-nieuwe-opzet.md` section 4.

- [ ] Refresh the model (DataFile parameter, anonymous web access) — `PillowKey.SemanticModel` — verify by: `Package` has 456 rows, no circular-dependency error on `Package` / `PackageProject` / `PlanSelector`, `NPV @ 8%` for 01+02+04+05+07+10 = -$31.3 M
- [ ] VERIFY: page background image — both pages — verify by: the PNG renders at Fit, 0 % transparency
- [ ] VERIFY: title text bound to a measure — `ch_trend_margin`, `ch_trend_ota`, `ch_trend_nps` — verify by: titles show the `Trend Title ... (text)` strings
- [ ] VERIFY: scatter field-value colour and the zero constant line — `hero_packages` — verify by: focus dot raspberry, plum / plum-slate (`#82798A`) split, line labelled at 0
- [ ] VERIFY: action-button text and fill objects — `btn_open_plan`, `btn_back` — verify by: labels and fills render; clicking swaps `bm_p2_shortlist` / `bm_p2_plan`
- [ ] VERIFY: table field-value font and background colours — `tbl_geo` (matrix, `values.backColor`), `hero_brand_compare` (table, `values.backColorPrimary` / `fontColorPrimary`)
- [ ] VERIFY: `Initiative Chip` renders as an image, not as text, through `dataCategory: ImageUrl` on the measure — `tbl_plan_initiatives` — verify by: the first column shows the state chip (raspberry for funded) instead of a `data:image/svg+xml` string
- [ ] VERIFY: chip image size — `tbl_plan_initiatives` (no image-size object is written, so Desktop uses its default) — verify by: chip reads at about 24 px tall without clipping the row; fallback: Format > Image size 24 px
- [ ] VERIFY: ▲ / ▼ glyphs from `KPI Rank (text)` render in Verdana — `hero_brand_compare` — verify by: triangles show (no tofu boxes) and sit on the baseline
- [ ] VERIFY: awake lockup on the P2 background — `p2-investment-strategy` (`bg-p2-investment-strategy.png`; derived in `opzet_backgrounds.mjs` as the kit lockup with the awake mark's eyes) — verify by: P2 shows the awake hanger and P1 the sleeping one, both crisp at 1920x1080 and under Publish-to-Web
- [ ] Focus-swap proof (`03-focuswissel-testplan.md` tests 1-4) — P2 — verify by: package and scenario selections survive both bookmark swaps
- [ ] Fonts Trebuchet MS / Verdana present and figures align — both pages
- [ ] Publish-to-Web render at 1920x1080 and 1366 wide, both P2 states
- [ ] Re-check D1/D2/D3 headline numbers after refresh and update `SKETCHES.md` (shared-model change)
- [ ] Rendered review per page (fonts, clipping, interactions) — see 07 checklist

## Validation status

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

- No Desktop render of `GoodnightInn-opzet` yet; the VERIFY shapes above are schema-valid but not visually confirmed.
- P2 presents three presets rather than one recommendation until open question 1 in `05-doorlichting-nieuwe-opzet.md` is decided.
- Logo on P2: the awake lockup is derived (the kit's lockup with the awake mark's eyes), not a kit asset. Retire the derivation in `opzet_backgrounds.mjs` once `brand_logos.py` emits `goodnight-inn-lockup-awake.svg` (05, check 6).
