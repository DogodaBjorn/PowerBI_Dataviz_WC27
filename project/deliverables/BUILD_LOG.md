# BUILD_LOG — World Champs BCN 26 — Round 3

<!-- Maintained DURING stages 4 and 6 by the build-log skill. A reader who
never saw the chat must learn from this file: what exists, what remains
manual, which numbers rest on assumptions, when it was last validated. -->

Last validated: 2026-08-05 (G6 a11y pass) — `validate_tmdl.py --strict`: 15 files,
**1 error** (the standing `SourceRoot` drive-letter waiver, see 04-model-build.md),
0 warnings; **260 repo JSON files** well-formed, UTF-8 without BOM, 0 errors;
every PBIR file 0 errors against its published schema with remote `$ref`s resolved.
Model: 10 tables, **90 measures**, 8 relationships, 3 shared expressions
(SourceRoot parameter, Source, Schema). The `06 Display\Alt text` family is
**built** — the attribution blocker was cleared on 2026-08-05 (commit `f4b9420`).
Report: the D7 custom theme is installed and active, and a **report-level filter**
(`Movies[Adult] = false`, locked, pane visible) is written into `report.json`.
**The report is structurally complete**: `p0-box-office` (43) ·
`p1-act-i-profit` (47) · `p2-act-ii-ratings` (41) · `p3-act-iii-corrected-cut` (40) ·
`p9-end-credits` (37) · `tt-movie-poster` tooltip (14) = **222 visuals in six pages**
(5 visible + 1 tooltip — the contest maximum is 5), plus the **nine beat bookmarks**
(`bm_p1_b1..b3`, `bm_p2_b1..b3`, `bm_p3_b1..b3`). **The two contest-starter pages
were deleted in the G6 fix pass.** Nothing has been rendered in Desktop — see
*Manual steps* and *Known limitations*.

## Built

| Date | Scope | Items |
|---|---|---|
| 2026-08-04 | SemanticModel: sources | `SourceRoot` parameter; `Source`/`Schema` M rewritten to `SourceRoot & "\TMDB_movie_dataset_v11.csv"` |
| 2026-08-04 | SemanticModel: Date | deterministic 1800-01-01..2099-12-31 range; `dataCategory: Time` + `isKey` (mark as date table); `Month Name` sorted by `Month Number` |
| 2026-08-04 | SemanticModel: Movies | new M columns `Release Year Key` (hidden FK, −1 unknown), `Is Future Release` (anchor 2026-07-24); `summarizeBy: none` on Vote Average, Vote Count, Revenue, Budget, Runtime, Popularity; Budget/Revenue format `\$#,0;(\$#,0)` |
| 2026-08-04 | SemanticModel: Release Year | new dimension (Year Key / Year Label / Year Sort / Year Status; "No date on record" member); relationship `Movies_ReleaseYearKey_to_ReleaseYear_YearKey` (*:1, single) |
| 2026-08-04 | SemanticModel: _Measures | `Profit` → `Profit (naive)` (formula byte-identical, trap-marked); 32 new measures across folders 01–06 per blueprint §5 |
| 2026-08-04 | Report: `22a73d6058ce40e505e0` / `e21488a8d900077091bd` | starter table visual rebound from `[Profit]` to `[Profit (naive)]` (projection, sort, filter) — same batch as the rename, nothing dangles |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — stub fills | 8 stage-4 `06 Display` stubs given their contracted expressions: `Color · Trap` · `Color · Honest` · `Color · Neutral` · `Title · Lie 1` · `Title · Lie 2` · `Title · Lie 3` · `Title · Landing` · `Label · Method`. Measure name, `lineageTag`, `formatString` and `displayFolder` untouched; only the expression and the `///` docstring changed. No `"s5 fills value"` literal survives anywhere. |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — support measures | 14 NEW: `Movies (scatter population)` (01 Core); `Financial floor (disclosed)`, `Movies (zero revenue)`, `Zero-revenue share %` (02); `Median votes`, `Votes p75`, `Movies (zero votes)`, `Zero-vote share %`, `Two-vote ten (illustration)`, `Godfather rating (reference)` (03); `Winner · title` (04); `Adult listings excluded`, `Snapshot anchor (disclosed)`, `Movies (sentinel-dated)` (05) |
| 2026-08-05 (s6 phase A) | SemanticModel: `_Measures` — 06 Display | 26 NEW: 6 colour/mark measures (`Color · Trap/Honest/Neutral (night)`, `Color · Rating verdict`, `Mark · Rating verdict`, `Color · Scatter mark`), 19 copy/label measures (`Copy · Act I ·` ×8, `Copy · Act II ·` ×3, `Copy · Act III ·` ×2, `Label · Population`, `Label · No date`, `Label · Chip floor/m/C`, `Label · Caveats`) and `Image · Poster URL` |
| 2026-08-05 (s6 phase A) | Report: `StaticResources/RegisteredResources` | `project/deliverables/theme.json` installed byte-identically as `D7-Seductive-Lies.json` (UTF-8, no BOM; sha256 `7fbc8c2ee0a1abaa…`) |
| 2026-08-05 (s6 phase A) | Report: `definition/report.json` | `themeCollection.customTheme.name` repointed to `D7-Seductive-Lies.json`; a matching `{name, path, type: "CustomTheme"}` item added to the `RegisteredResources` package. `baseTheme` (`Fluent2-CY26SU05`), `objects`, `settings` and every existing identifier untouched |
| 2026-08-05 (s6 phase B1) | Report: `pages/p0-box-office` | **42 visuals**, 1280×720, canvas `#171418`. Marquee (`z_marquee_frame` / `_inner` / `_title` / `_sub`) · `hero_takeaway` (live) · three tickets ×11 objects each (`z_ticketN_body` / `_rule` / `_stub_rule` / `_perf` / `_act` / `_hr` / `_title` / `_tease` / `_admit` / `_serial` + `btn_ticket_actN`) · `z_billing_method` + `z_billing_caveats` (live) · `z_footer_credit` · `btn_credits` |
| 2026-08-05 (s6 phase B1) | Report: `pages/p9-end-credits` | **35 visuals**, 1280×720, canvas `#171418`. `z_cr_title` · `c_cr_h_cast` + `c_cr_cast` · `c_cr_h_counts` + 7 label/value row pairs + `c_cr_count_basis_kept` · `c_cr_h_params` + 4 label/value row pairs · `c_cr_h_glossary` + `c_cr_glossary` · `c_cr_h_refusals` + `c_cr_refusals` · `c_cr_close_src` · `c_cr_close_last` · `btn_home`. **14 of the 35 are measure-bound cards** — no count is typed anywhere |
| 2026-08-05 (s6 phase B1) | Report: `pages/pages.json` | `p0-box-office` prepended and made `activePageName` + `landingPageName`; `p9-end-credits` appended. The two starter page ids kept in `pageOrder`, untouched |
| 2026-08-05 (s6 phase B2a) | SemanticModel: `_Measures` | **1 NEW measure** `Movies (no credible financials)` = `[Movies] - [Movies (credible financials)]` (folder `02 Lie 1 · Financials`, format `#,0`, fresh lineageTag). Build-necessitated: the contracted waffle fallback is a **100 % stacked bar**, which needs the complement segment as a field; `[Movies]` and `[Movies (credible financials)]` overlap and would stack to a lie. No new concept — the design already prints this quantity ("no credible financials (87)") |
| 2026-08-05 (s6 phase B2a) | Report: `pages/p1-act-i-profit` | **43 visuals**, 1280×720, paper canvas `#F5F2E9`. Chrome ×13 (`z_p1_header_title` / `_rule` · `btn_home` · `btn_credits` · `z_p1_admit` · `btn_beat_1..3` + `z_p1_beat1..3_mark` · `btn_next_scene` · `z_p1_verdict_rule`) · screenplay ×8 · KPI insert ×7 · script-doctor notes ×6 (3 rules + 3 texts) · ticket-audit insert ×6 · verdict ×3. **9 of the 43 are measure-bound cards**; no count is typed anywhere |
| 2026-08-05 (s6 phase B2a) | Report: `pages/p2-act-ii-ratings` | **37 visuals**, 1280×720, paper canvas `#F5F2E9`. Chrome ×12 + 3 beat marks · screenplay ×8 · notes ×6 · perfect-tens insert ×4 (incl. `tbl_perfect_tens`) · correction insert ×4 (incl. `dn_rating_fall`) · verdict ×2. **3 measure-bound cards** plus two data visuals bound entirely to measures/columns |
| 2026-08-05 (s6 phase B2a) | Report: `pages/pages.json` | `p1-act-i-profit` and `p2-act-ii-ratings` inserted after `p0-box-office`; starter ids and `p9-end-credits` untouched. Validated against `pagesMetadata/1.1.0` (0 errors) |
| 2026-08-05 (s6 phase B2b) | SemanticModel: `_Measures` | **5 NEW** — `Movies (perfect ten)`, `Movies (perfect ten, single vote)`, `Single-vote ten (illustration)` (03 Lie 2 · Ratings); `Copy · Act II · naive read`, `Mark · Rank divergence` (06 Display). **2 EDITED in place** (name, `lineageTag`, `formatString`, `displayFolder` untouched; expression + docstring only): `Copy · Act II · responsible read`, `Copy · Act II · verdict` — both now state the aggregate and name no film. See *the Act II ruling* below |
| 2026-08-05 (s6 phase B2b) | Report: `p0/btn_credits`, `p9/btn_home` | `"lineWeight"` → `"weight"` (the published `actionButton → outline` property). One-line correctness fix, coordinator-ruled. Nothing else in either file changed |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p1-act-i-profit` | rebuilt at **44 visuals** (+`btn_next_scene_2`), **landing state flipped to SC.1** (22 objects `isHidden` on disk), beat buttons wired to `bm_p1_b1..b3` |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p2-act-ii-ratings` | rebuilt at **38 visuals** (+`btn_next_scene_2`), **landing state SC.1** (17 hidden), `c_p2_dlg_naive` converted textbox → measure-bound card, leaderboard sort given a deterministic tie-break, `tbl_perfect_tens` bound to the tooltip page, screenplay honest block reflowed +24 px |
| 2026-08-05 (s6 phase B2b) | Report: `pages/p3-act-iii-corrected-cut` | **37 visuals**, 1280×720, night canvas `#171418`, tint `#B79BE8`. Chrome ×14 · hero block ×4 (`hero_premiere_scatter` native `scatterChart`, `c_scatter_population`, `z_p3_scrim`, `c_winner_label`) · adjustments ×10 (2 card variants + 4 chips + 4 labels) · refusal ×5 · no-date ×2 · verdict ×2. **Landing state SC.3** (7 hidden). 8 measure-bound cards |
| 2026-08-05 (s6 phase B2b) | Report: `pages/tt-movie-poster` | **14 visuals**, 320×420, `type: "Tooltip"`, `visibility: "HiddenInViewMode"`, `pageBinding` type Tooltip. `z_tt_bg` · `img_tt_poster` · `c_tt_name` · `c_tt_year` · 4 label/value rows (the weighted row carries `[Mark · Rating verdict]` beside the number) · `c_tt_foot`. Every field it shows is also printed on canvas elsewhere |
| 2026-08-05 (s6 phase B2b) | Report: `definition/bookmarks/` | **9 bookmark files + `bookmarks.json`**. Folder layout and both schemas verified (Learn `projects-report`; `bookmark/2.1.0`, `bookmarksMetadata/1.0.0`). Each bookmark captures **every** visual on its page (44 / 38 / 37) with `options.suppressData: true` = Data OFF · Display ON · Current page ON · All visuals |
| 2026-08-05 (s6 phase B2b) | Report: `pages/pages.json` | `p3-act-iii-corrected-cut` appended after p2; `tt-movie-poster` appended last. Starter ids untouched; `activePageName` / `landingPageName` still `p0-box-office` |
| 2026-08-05 (s6 **G6 fix pass**) | Report: attribution | `z_footer_credit` (p0) and `c_cr_close_src` (p9) now carry one identical mandated credit string naming **TMDB · Kaggle · ODC-By 1.0** plus the TMDB non-endorsement clause. p0's box widened 900 → 1060 px so the longer string stays on one line (measured 919 px, Segoe UI 10 pt) |
| 2026-08-05 (s6 **G6 fix pass**) | Report: contest-template pages **deleted** | `a65cf5aab733edd4ebbd` ("Read Me") and `22a73d6058ce40e505e0` ("Tabular") — both 1920×1080, default styling — removed with their 17 visuals and struck from `pageOrder`. Verified beforehand that no bookmark, `navigationSection`, `pageBinding` or tooltip target referenced either id. Entry is now **5 visible pages + 1 tooltip** |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `definition/report.json` | **report-level filter written** — `filterConfig.filters[0]` `flt_report_adult`: `Movies[Adult] = false`, `type: "Advanced"`, `howCreated: "User"`, `isLockedInViewMode: true`, `isHiddenInViewMode: false` |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `tbl_perfect_tens` · `tbl_refusal_ranks` | column headers silenced by setting `columnHeaders.fontColor` equal to `columnHeaders.backColor` (`#FFFFFF` on p2, `#1D1A20` on p3). `tableEx` has no `columnHeaders.show` |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `z_p1_header_title` · `z_p2_header_title` · `z_p3_header_title` | textbox → **measure-bound `cardVisual`** on `[Title · Lie 1/2/3]`. Consolas 12 pt, page ink, left, wrap on; geometry unified to `24, 36, 830, 44` on all three acts. Alt text added (each states the finding, no volatile count) |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `p0/z_hero_kicker` | NEW textbox — `KEY TAKEAWAY` kicker at `24, 136, 1232, 16`, Bahnschrift SemiCondensed 10 pt `#B5AFA0`, centred over `hero_takeaway`, tabOrder 250 |
| 2026-08-05 (s6 **G6 fix pass**) | Report + model: stale Act II strings | `z_ticket2_tease` → "In which 1 vote crowns a champion"; `c_cr_cast` → "THE SINGLE-VOTE PERFECT TEN … as 'The Best Film Ever Made'"; `c_cr_glossary` → "M-005 RAW RATING — any votes, even 1"; plus a fourth found in the model: a leftover first docstring line on `Movies (perfect ten)` that still described "a perfect 10.0 on two votes" |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `c_p1_note_budget` · `c_p1_note_negrev` | the two typed literals removed by re-phrasing (no measure invented): "min $1" → "Unknowns arrive as token amounts, not as blanks."; "one listing books −$12 revenue" → "revenue goes negative in this basis." |
| 2026-08-05 (s6 **G6 fix pass**) | SemanticModel: `_Measures` — Act III wording | "films" → "listings" in `Label · Population`, `Title · Lie 3`, `Alt · hero_premiere_scatter` (2 places) and `Alt · c_refusal_popularity` (2 places); `Copy · Act III · verdict` "the best movie" → "the best-performing listing" |
| 2026-08-05 (s6 **G6 fix pass**) | Report: invisible properties | 4 adjustment chips `outline.lineColor` `#3A3441` → `#6E6960` (1.43:1 → 3.16:1 on the card, 3.35:1 on canvas); `z_refusal_card_lit` fill `#282331` → theme `#2E2933` **and** outline weight 2 → 4 px so beat SC.2 has a non-colour carrier; `c_cr_count_dup_lbl` 240 → 264 px (its string measures 261 px at Consolas 12 pt) |
| 2026-08-05 (s6 **G6 fix pass**) | SemanticModel + Report: p9 NEGATIVE REVENUE row | **1 NEW measure** `Movies (negative revenue)` = `CALCULATE([Movies], Movies[Revenue] < 0)` (folder `05 Data health · Time`, format `#,0`, fresh lineageTag) + `c_cr_count_negrev_lbl` / `c_cr_count_negrev_val` at y 436, tabOrder 550 / 555, z 51 / 52 |
| 2026-08-05 (s6 **G6 fix pass**) | Report: ticket perforation ×3 | `z_ticketN_rule` widened 286 → 372 px so one act-tint frame spans the whole inner ticket; `z_ticketN_stub_rule` outline switched off. The 1 px `z_ticketN_perf` line is now the only mark at the tear |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `p3` beat rail | `btn_beat_1..3` and `z_p3_beat1..3_mark` moved onto the p1/p2 x-grid `24/188 · 222/148 · 380/222`. All three p3 labels measured to fit (131 / 106 / 122 px at Bahnschrift SemiCondensed 10 pt) |
| 2026-08-05 (s6 **G6 fix pass**) | Report: `c_cr_count_dup_val` | y 360 → 341, rejoining its own label — every other p9 count pair already shared a row (found during the width fix, not in the review) |
| 2026-08-05 (s6 **G6 fix pass**) | Deliverables: `design-handoff.md` | the sentence claiming no `layout.json` / `reference_screenshots/` were produced corrected — both exist (`project/design-prototypes/`, 8 screens and 8 @2x captures) |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: the alt-text sweep | **29 alt strings rewritten** so each states its finding instead of pointing at the screen. Removed every deferral ("the live count is printed on the card", "its name is read from the model", "stated in the title above", "named in the annotation beside the plot", "the card prints both counts live"). p9's 12 value cards and the tooltip's 7 now fold their label into their own alt, so each stop is self-contained. Volatile figures are phrased around the disclosed constants ($10,000 · m = 100 · C = 6.96 · 24 July 2026); **no volatile count is typed** |
| 2026-08-05 (s6 **G6 a11y pass**) | Report + model: honesty of the alt layer | Three strings described things the file does not do. `c_nodate_chip` and `Label · No date` (**on canvas**) no longer say "never enter this animation" / "excluded from play"; `Alt · hero_premiere_scatter` and the scatter's on-disk alt now open "Static scatter plot of the corrected cut" and state plainly that the plot does not colour the winner; `dn_ticket_waffle`'s alt no longer credits an in-chart tick that lives in the caption. Docstring on `Movies (sentinel-dated)` re-worded off "play axis" |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: `z_p3_scrim` + `hero_premiere_scatter` | measured AA failure fixed — scrim `transparency` 65D → **80D** and the C = 6.96 reference line `#6E6960` → **`#8A8377`**. Recomputed under the scrim: axis labels **4.21 → 5.75:1** (needs 4.5), reference line **2.12 → 3.56:1** (needs 3.0). Unscrimmed the line improves too, 3.35 → 4.87:1 |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: beat state announced (WCAG 4.1.2) | each `btn_beat_N` split into a not-current variant (same id, z and tabOrder) and a new **`btn_beat_N_current`** — **9 new visuals**, tabOrder 405/505/605, alt reading "Scene N of 3, **current scene** — …". Styling that the bookmarks used to merge is now static per variant, and all **9 bookmarks** toggle the pair by `display.mode`. Landing states preserved: p1/p2 on SC.1, p3 on SC.3 |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: `p9` tab order | 12 `c_cr_*_lbl` + `c_cr_count_basis_kept` set to `tabOrder: -1` with `altText: ''`, their words having been folded into the sibling `_val` alt. p9 drops from **37 → 24** stops and a screen-reader user hears each label-and-number as **one** stop instead of two |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: `p9/c_cr_cast` dot leaders | the three ` . . . . ` runs moved from `#57534E` (the **paper** secondary ink) to the night token `#B5AFA0` — **2.39 → 8.35:1**. The `design-handoff.md` row that specified `#57534E` here was corrected too; the contract was the source of the defect |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: `p2/dn_rating_fall` | `valueAxis.end` 10D → **11D**. The raw series sits exactly at 10.0, so at an axis max of 10 the label was forced inside the bar (`#211E1A` on `#B3402E` = 2.92:1); with headroom it places outside on the white card. `end` verified against Microsoft's own cartesian reference |
| 2026-08-05 (s6 **G6 a11y pass**) | Report: `p1/dn_ticket_waffle` | `legend.show` true → **false**. The native legend printed raw measure names beside the hand-built caption legend that carries the `✓`; `c_waffle_cap` is kept as the single legend |
| 2026-08-05 (s6 **G6 a11y pass**) | SemanticModel: `Image · Poster URL` | **`dataCategory: ImageUrl`** written on the measure — previously deferred as unverifiable. Now verified from two Microsoft sources (see the decisions below) |
| 2026-08-05 (s6 **G6 a11y pass**) | Deliverables: `measures.dax` | **12 measure bodies refreshed from the model** (the Act II ruling, films → listings, the two Deneb fallbacks, the play-axis removal, the resolved TMDB poster base) plus 3 resolved `VERIFY-AT-BUILD` docstrings and a new **AUTHORITY** header stating that `_Measures.tmdl` wins |
| 2026-08-05 (s6 **G6 a11y pass**) | Deliverables: `design-handoff.md` | recorded that **p3 landing on SC.3 is deliberate** (ack #3 in the entrant's decision table), so a future reviewer does not read it as a defect |
| 2026-08-05 (**rebuild ckpt 2**) | Report: `pages/p1-the-answer` | **NEW page, 13 visuals**, 1280×720, night canvas `#171418`, `displayName` "THE ANSWER". `c_question` · `hero_takeaway` (the mandated Key Takeaway) · `z_rule_answer` · `dn_answer_units` (native `hundredPercentStackedBarChart` fallback) · `c_units_legend` · `c_units_read` · `btn_go_money` / `btn_go_evidence` / `btn_go_both` · `c_nav_hint` · `btn_method` · `z_method_stamp` · `c_caveats`. **4 measure-bound cards + 1 chart bound to 3 measures**; the only literal numbers on canvas are the ordinals 1/2/3 and the disclosed `$10,000` and `m = 100` |
| 2026-08-05 (**rebuild ckpt 2**) | Report: `pages/pages.json` | `p1-the-answer` prepended to `pageOrder` and made **both** `activePageName` and `landingPageName` (was active `p9-end-credits`, landing `p0-box-office`). The six old pages are untouched and still registered — they are deleted in a later checkpoint, once their replacements exist |
| 2026-08-05 (**ckpt 2 rulings**) | Report: `p1-the-answer` — grid snap | 4 rects corrected on the coordinator's ruling: `c_units_legend` h 20→**24** · `c_nav_hint` y 572→**576** h 20→**24** · `c_units_read` y 580→**584** · `btn_method` h 28→**32**. `z_rule_answer` (h 1) stays and is waived as a hairline |
| 2026-08-05 (**ckpt 2 rulings**) | Report: `p1-the-answer/c_takeaway_kicker` | **NEW textbox** — `KEY TAKEAWAY` at `24,88,1232,16`, Arial 10 pt `#B5AFA0`, `tabOrder` 150 (immediately before `hero_takeaway`), empty alt. Labels the contest's mandated element so a judge finds it in three seconds |
| 2026-08-05 (**ckpt 2 rulings**) | Deliverables + Report: `theme.json` / `D7-Seductive-Lies.json` | `visualStyles.actionButton.*.text[0]` **`"alignment"` → `"horizontalAlignment"`** in both copies, byte-identical apart from the pre-existing LF/CRLF difference. Re-validated 0 errors against `reportThemeSchema-2.156` |
| 2026-08-05 (**ckpt 2 rulings**) | Project state: `pbir-detect-waivers.yaml` | two DRAFT hairline entries added (`grid-p1-the-answer-hairline`, `grid-p4-both-hairline`) — one 1 px / 2 px separator each, everything else on-grid. **Unsigned**, like every other entry in that file |
| 2026-08-05 (**rebuild ckpt 3**) | Report: `pages/p4-both` | **NEW page, 11 visuals**, 1280×720, night `#171418`, plum `#B79BE8` chrome-only, `displayName` "3 · BOTH". `nav_pages` (**native `pageNavigator`**) · `c_p4_answer` · `z_p4_rule` · `c_scatter_population` · `hero_premiere_scatter` (**native `scatterChart` with the Play axis**) · `c_winner_label` · `c_adjustments` · `c_refusal` · `tbl_refusal_ranks` (native `tableEx`, **headers ON**) · `c_nodate` · `c_verdict_both`. **8 measure-bound cards + 2 data visuals**; nothing numeric is typed |
| 2026-08-05 (**rebuild ckpt 3**) | Report: `p1/dn_answer_units` + `p4/hero_premiere_scatter` | chart-container treatment unified per consistency lock 9: **fill `#1D1A20` + 1 px `#6E6960` hairline** on both night data visuals (p1 gained the fill, p4's border moved off `#2E2933` at 1.29:1) |
| 2026-08-05 (**rebuild ckpt 3**) | Report: `pages/pages.json` | `p4-both` registered directly after `p1-the-answer`; landing and active still `p1-the-answer`; old pages untouched |

## Deferred — not built, and why

- ~~`06 Display\Alt text` — the 10 `Alt · …` measures (BLOCKER, attribution)~~ —
  **RESOLVED and BUILT 2026-08-05 (phase B2c).** The attribution debt was closed at the
  main-thread level (commit `f4b9420`): the influencing post is credited *by
  publication* in `CREDITS.md` and `contracts/source-register.yaml` (tier 4,
  community), with the unretrievable byline recorded as an **open attribution debt**
  for a human to close. **Scope of what was adopted:** the post prompted *dynamic*
  alt text — nothing more. Its own technique wraps the narrative in **DAX
  user-defined functions**, and that pattern is **NOT** adopted here (adopting it
  would need the author's name first). The ten measures are ordinary measures driving
  Power BI's own documented dynamic-alt-text feature, the accessibility practice this
  repo credits to **Meagan Longoria**. Do not remove or weaken either entry.
- ~~Alt text on every visual is intentionally UNSET~~ — **resolved, see
  *the alt-text layer* below.** The former waiting list (p0 6 · p1 11 · p2 6 · p3 9 ·
  p9 11 · tooltip 8) is closed; every visual on it now carries alt text.
- ~~**p9 `NEGATIVE REVENUE` row — not built.**~~ — **RESOLVED and BUILT in the G6
  fix pass (2026-08-05).** `Movies (negative revenue)` =
  `CALCULATE([Movies], Movies[Revenue] < 0)` was added in folder
  `05 Data health · Time` (format `#,0`, fresh lineageTag), and the row pair
  `c_cr_count_negrev_lbl` / `c_cr_count_negrev_val` sits at y 436 with tabOrder
  550 / 555 exactly as the recipe specified. The count is **bound, never typed**.
- **p9 disclosed-parameter notes — numeric parts not built.** The design prints
  `$10,000 (13.1% vs 11.9% @ $100k)` and `100 (Vote Count p90=106)`. Both
  parentheticals are stale under the entrant's newer snapshot (coverage is now
  13.05 %, votes p90 is now 104) and neither has a measure behind it. The parameter
  **values** are live and printed; the numeric notes are omitted rather than typed
  wrong. **To unblock:** add measures for the robustness pair and for votes p90,
  then bind them beside the value.

## Decisions & assumptions

- 2026-08-04 — `SourceRoot` default is the placeholder `<set-me>\TMDB` (no
  drive letter) — validator forbids machine-style absolute paths in TMDL; the
  entrant sets the real folder locally and never commits it.
- 2026-08-04 — `Rating m (disclosed)` = 100 and `Rating C (disclosed)` = 6.96
  are **disclosed constants** (signed at Q2), deliberately not computed live —
  determinism and on-canvas disclosure. SCENARIO CHOICE (signed assumption).
- 2026-08-04 — Snapshot anchor `#date(2026, 7, 24)` (dataset download date)
  hard-coded in `Is Future Release` and the Release Year `Year Status` —
  never `TODAY()`/`LocalNow()`, per blueprint determinism. SCENARIO CHOICE
  (accepted by entrant).
- 2026-08-04 — Credibility floor Budget ≥ $10,000 AND Revenue > 0 baked into
  the credible-financials measures — disclosed floor per M-002/M-004.
  SCENARIO CHOICE (signed assumption).
- 2026-08-04 — 06 Display measures are stubs returning `"s5 fills value"`
  (formatString `@`); real colors/titles/labels land with the stage-5 design
  contract.
- 2026-08-04 — Rank/single-value logic tolerates the 101 duplicate Movie ID
  rows (HASONEVALUE guard; RANKX over Movie ID values with per-ID CALCULATE).
- 2026-08-04 — Parameter meta record (`IsParameterQuery` etc.) is Desktop
  convention, not re-verified against docs this session; value-preserving M
  worst case. Desktop confirmation listed below.
- 2026-08-05 — **TMDB poster base URL RESOLVED (was VERIFY-AT-BUILD).**
  `Image · Poster URL` now uses `PosterBase = "https://image.tmdb.org/t/p/w342"`.
  Retrieved 2026-08-05 from TMDB's own documentation, not from memory:
  `https://developer.themoviedb.org/docs/image-basics` (HTTP 200; states a full
  image URL is `base_url` + `file_size` + `file_path`, worked example
  `https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg`) and
  `https://developer.themoviedb.org/reference/configuration-details` (HTTP 200;
  `secure_base_url = "https://image.tmdb.org/t/p/"`, `poster_sizes =
  ["w92","w154","w185","w342","w500","w780","original"]`).
  **Size choice `w342`** — a documented poster size, the smallest that stays crisp
  at the tooltip's 170 × 240 px poster on a 2× display and downsamples cleanly to
  the 32 × 44 leaderboard thumbnail. Not invented: chosen from the published list.
  The contracted "no posters anywhere" fallback is therefore **not** taken.
- 2026-08-05 — **Poster path concatenation verified against the source CSV.**
  `poster_path` values in `TMDB_movie_dataset_v11.csv` carry their own leading
  slash (samples: `/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg`), so
  `PosterBase & PosterPath` composes exactly the documented URL shape. No
  slash-normalising logic was added, because none is needed.
- 2026-08-05 — **`Godfather rating (reference)` VERIFY-AT-BUILD RESOLVED.** A full
  scan of the source CSV finds exactly **two** listings titled "The Godfather":
  Movie ID **238**, release 1972-03-14, budget $6,000,000, 18,677 votes; and Movie
  ID 1050474, release 2023-01-28, budget 0. The measure's `Release Year Key = 1972`
  predicate selects only ID 238, and ID 1050474 is in any case excluded by the
  partition's `budget > 0` filter. **No narrowing on Movie ID was needed**; the
  measure ships as contracted, and the verified id is recorded in its docstring.
- 2026-08-05 — **Docstring convention on the ported measures.** `measures.dax`
  docstrings carry two bookkeeping markers — the `REPLACES STUB.` prefix and the
  `Folder: … | Format: … | NEW` line. Both are build instructions that would be
  meaningless inside the model forever, and both are redundant with the
  `displayFolder` / `formatString` properties actually written. They are dropped;
  **every semantic line is kept verbatim**, including the `SCENARIO CHOICE`,
  `ILLUSTRATION` and binding notes. This follows the `tmdl-style` rule (docstring =
  business meaning) rather than the letter of the handoff.
- 2026-08-05 — **`lineageTag` authored for all 40 new measures** (fresh UUID4s)
  rather than left for Desktop to generate, so the next Desktop round-trip produces
  no gratuitous diff. Existing lineageTags were not touched.
- 2026-08-05 — **Theme registration mechanism** was derived from the report tree,
  not from memory. Evidence: `definition/report.json` declares
  `$schema … /report/3.3.0/schema.json`; that schema (fetched, HTTP 200) defines
  `themeCollection.customTheme` as a `ThemeMetadata` (`name`,
  `reportVersionAtImport`, `type` — all required; `type` ∈ {`RegisteredResources`,
  `SharedResources`}) and requires a matching `ResourcePackageItem`
  (`name`, `path`, `type`) where `CustomTheme` is a valid item type. The install
  copies that exact shape from the custom theme Desktop had already registered.
  `reportVersionAtImport` is kept at the values Desktop itself recorded for this
  report's custom theme (visual 2.10.0 / report 3.4.0 / page 2.3.1) — the report's
  schema versions have not changed, so the swap happens at the same versions.
- 2026-08-05 — **The superseded starter theme is kept registered but inactive.**
  `Accessible_City_park5942914118805086.json` remains in `RegisteredResources` and
  in the resource package; only `themeCollection.customTheme` moved. Nothing
  resolves to it (the active theme is named explicitly), no identifier was
  destroyed, and the change is reversible in one line. Deleting it is an optional
  tidy-up for the entrant, not a build step.
- 2026-08-05 — **`theme.json` independently re-validated at install:** 0 errors
  against `reportThemeSchema-2.156.json` with a Draft-7 validator, confirming the
  stage-5 claim. The install is a byte-identical copy — the deliverable and the
  installed resource cannot drift.
- 2026-08-05 — **Observation for QA, not a build defect.** A full pass over
  `project/data/TMDB_movie_dataset_v11.csv` counts 1,469,389 rows of which
  **85,870** have `budget > 0`, while `data-model.md` and the p9 cross-foot narrate
  **85,394** listings per source. Every printed count is bound to a measure and will
  therefore print whatever the loaded model actually holds, so the report stays
  self-consistent either way; but the 476-row gap should be reconciled at s7 before
  the 85,394 figure is quoted in prose.

### Stage 6 phase B1 — decisions

- 2026-08-05 — **LIVE-NUMBER BINDING MECHANISM SETTLED: fallback A, the
  `cardVisual` bound through a query projection.** The handoff's preferred
  textbox *dynamic-value run* is **not used**, because it could not be verified and
  research-first forbids writing an unverified shape. Evidence gathered:
  1. `visualContainer/2.11.0` — the version this report's own `visual.json` files
     declare — returns **HTTP 404**. Probing the series, **2.9.0 is the newest
     published** version (2.10.0 / 2.11.0 / 2.12.0 / 2.13.0 all 404). This confirms
     the stage-5 finding.
  2. `visualContainer/2.9.0` delegates `visual` to
     `visualConfiguration/2.3.0/schema-embedded.json`, which delegates `objects` to
     `formattingObjectDefinitions/1.5.0#/definitions/DataViewObjectDefinitions`.
     That definition is `{"type":"object","additionalProperties":{}}` — **completely
     untyped**. A string search of the whole file returns **0** occurrences of
     `textRun`, `paragraph` or `dynamic`. So the schema can neither confirm a
     dynamic-value run nor reject an invented one — precisely the silent-failure
     trap the `pbir-authoring` skill warns about.
  3. Microsoft Learn's PBIR report-definition page documents no textbox dynamic
     value; `create-reports/desktop-add-text-boxes` returns 404.
  4. The published theme schema types the theme-level textbox
     `paragraphs.textRuns` with `value` **required** and **string-only** — no
     expression variant. (Indicative only: instances use `textStyle` where the theme
     uses `textRunStyle`, so the shapes already differ.)
  5. No Microsoft-authored PBIR sample was reachable — `microsoft/powerbi-desktop-samples`
     ships `.pbix` only, and its `item-schemas` tree covers `definition.pbir` and
     `localSettings` but no visual schemas.
  6. Desktop is closed, so it could not be made to serialise one for observation.
  **What IS verified**, and therefore what is used: a measure binding as a query
  projection — `query.queryState.<Role>.projections[].field.Measure` — proven both
  by the typed `Query` / `RoleProjection` definitions and by this report's own
  Desktop-authored `tableEx` (`e21488a8d900077091bd`) and the two
  `VerifiedAnswers/*/visualSource.json` files.
  **This mechanism is now fixed for the whole report.** Every prose-with-a-number in
  phase B2 uses a `cardVisual`, not a textbox — one mechanism, once, consistently.
  **Cost, stated plainly:** a card cannot mix styled runs inside one string, so
  prose that wanted a differently-styled trailing clause (for example the 11 pt
  `(USD as recorded; gross gap, not P&L.)` on `c_verdict_act1`) must ship as a
  second adjacent object in phase B2.
- 2026-08-05 — **ALT-TEXT PROPERTY PATH VERIFIED** (the open item the handoff left
  for stage 6). It is `visual.visualContainerObjects.general[0].properties.altText`,
  confirmed in `visualConfiguration/2.3.0/schema-embedded.json` →
  `VisualContainerGeneralFormattingObjects`, whose properties are exactly
  `x, y, width, height, altText, allowBinnedLineSample, allowOverlappingPointsSample,
  keepLayerOrder`. Nothing is written there yet — the attribution hold stands — but
  the research question is closed.
- 2026-08-05 — **Property vocabulary was verified before writing, not recalled.**
  The published `reportThemeSchema-2.156` enumerates the valid visual names and, per
  visual, the formatting-card names and their properties. Two consequences worth
  recording: (a) **`basicShape` is not a valid visual name** — the correct name is
  **`shape`**, which is also what this report's own Desktop-authored files use, so
  every rectangle in the handoff spec'd as `basicShape` is built as `shape`; the
  `basicShape` block inside `theme.json` targets nothing and is dead weight (harmless,
  worth pruning at s7). (b) `cardVisual`'s cards are `value` (font family/size/colour,
  bold, italic, `horizontalAlignment`, `textWrap`) and `label` (`show`) — which is how
  the callout is styled as body text with the category label off.
- 2026-08-05 — **Five tokens could not be verified from any published source.** They
  are recorded here because each is a *rendering* risk, not a corruption risk: the
  schemas explicitly leave these open (`queryState` is an open map keyed by role
  name; enum values are untyped `{}`), so a wrong value fails visibly in Desktop and
  is a one-line fix. Each is on the manual checklist below.
  1. `cardVisual` query **role name** — written as `"Data"`.
  2. `visualLink.type` enum — written as `'PageNavigation'`.
  3. `textAngle` on a shape — written as `270L` for the vertical ticket-stub text.
  4. `rectangleRoundedByPixel` + `rectangleRoundedCurve: 8L` for the 8 px ticket
     radius (chosen over `rectangleRounded` because the tileShape name states the
     unit; both are in the published enum).
  5. `horizontalTextAlignment` on a textbox paragraph — the name comes from the
     theme schema's `paragraphs` definition; instances in this report never set it.
- 2026-08-05 — **Two contracted media were substituted, with reasons.**
  1. **Ticket stub art: `ca-canvas` SVG → native `shape` with rotated text.** The
     handoff contracts an SVG image for the vertical `ADMIT ONE` and the serial.
     The published theme schema exposes **`textAngle`** on `shape`, so the same
     content ships as real text (`z_ticketN_admit`, `z_ticketN_serial`) instead of a
     picture. This is better than the contract, not worse: real text is selectable,
     scalable and survives a screen reader, whereas the SVG route needed an
     unverifiable data-URI and was contracted as decorative-with-empty-alt anyway.
     **Fallback if `textAngle` does not render:** drop to horizontal text at the
     stub foot, or restore the SVG.
  2. **p9 `tbl_production_counts` / `tbl_disclosed_params`: `tableEx` → label
     textbox + measure-bound value card, one pair per row.** A `tableEx` fed eight
     measures renders eight **columns in one row**, not eight label/value rows; a
     real row-per-metric table would need a disconnected metric dimension, which the
     model does not have and which phase A did not build. The alternative — typing
     the labels and the numbers — is exactly what the snapshot-reconciliation rule
     forbids. The pair-per-row build keeps **every number measure-bound** and gives a
     keyboard user a label stop immediately before each value stop.
- 2026-08-05 — **Perforation dashes not available.** `z_ticketN_perf` is spec'd as a
  1 px **dashed** line. The published `shape` property list has no dash/line-style
  property (`linecapType` only), so the contracted fallback is taken: a **solid**
  1 px `#9A9284` line, with the pre-torn read carried by the separate
  `z_ticketN_stub_rule` frame either side of it.
- 2026-08-05 — **Letter-spacing is not expressible in PBIR.** The design specifies
  tracking on the marquee title (0.14 em), subtitle (0.32 em), section heads and the
  ticket serial. A textRun's style carries only fontFamily / fontSize / fontWeight /
  fontStyle / colour / textDecoration. Tracking is therefore **dropped everywhere**;
  it is a uniform, deliberate fidelity loss, not a per-object slip.
- 2026-08-05 — **Reserved-red rule held.** An automated check over both pages finds
  trap red (`#B3402E` / `#E8705F`) in exactly one place: the `[TRAP]` tag run inside
  `c_cr_glossary`, where it names the trap in words as well as colour. p0 contains
  no red at all; `btn_credits` and `btn_home` are neutral cream `#F2EFE6` outline
  and text, as required.

### Stage 6 phase B2a — decisions (p1 · p2)

- 2026-08-05 — **DENEB IS NOT AVAILABLE; both contracted fallbacks are taken.**
  Checked, not assumed: `report/3.3.0/schema.json` defines
  **`publicCustomVisuals`** ("Names of the custom visuals used in this report from
  AppSource") and `organizationCustomVisuals`. This report's `report.json` declares
  **neither**, and no custom-visual payload exists under `StaticResources`. An agent
  cannot register an AppSource visual (it needs Desktop to download the package, and
  the identifier + version could not be verified from any published source), so
  inventing a registration was refused.
  - `dn_ticket_waffle` → **native `hundredPercentStackedBarChart`** at the same rect,
    `[Movies (credible financials)]` in good-green `#2F6B4F` against
    `[Movies (no credible financials)]` in neutral `#78716C`. Ids kept (`dn_` prefix)
    so the bookmark lists, the handoff and the alt-text register still line up.
  - `dn_rating_fall` → **native `clusteredBarChart`** (paired bars) at the same rect,
    `[Rating (raw)]` trap-red vs `[Rating (evidence-weighted)]` good-green, with a
    dashed **reference line at 6.96** named `C = 6.96` (`referenceLine` card:
    `show/value/lineColor/style/width/position/displayName/dataLabelShow/
    dataLabelText/dataLabelColor/dataLabel*Position` — every property and both enums
    verified in `reportThemeSchema-2.156`).
  - **To restore Deneb** (optional, entrant-only): install Deneb from AppSource in
    Desktop, author the two Vega-Lite specs, and the containers can be re-typed;
    PBIR can carry the container but not the spec.
- 2026-08-05 — **layout.json is the measured truth; the handoff supplies the
  decomposition.** Rects were taken from `design-prototypes/layout.json` screens
  `p1-act-i-sc1/sc3` and `p2-act-ii-sc1/sc3` wherever the prototype has a *block*
  element for the object. Where layout.json only measures an inline text run
  (`span`/`p`), the handoff's box wins — a text extent is not a box. Where the
  handoff decomposes one measured block into two PBIR objects (margin note = 2 px
  rule + inset text), the handoff's decomposition is built inside the measured
  block. **Differences resolved in layout.json's favour** (handoff → built):
  | Object | Handoff | Built (measured) |
  |---|---|---|
  | `c_p1_action` | 34,195,470,40 | 34,**196**,470,38 |
  | `c_p1_cue_naive` | 34,251,… | 34,**248**,… |
  | `c_p1_dlg_naive` | 129,270,… | 129,**267**,… |
  | `c_p1_trans` | 34,328,… | 34,**319**,… |
  | `c_p1_slug_honest` | 34,361,500,… | 34,**352**,**524**,… |
  | `c_p1_cue_honest` | 34,398,… | 34,**385**,… |
  | `c_p1_dlg_honest` | 129,417,315,116 | 129,**404**,315,114 |
  | `c_p1_slug_naive` / `c_p2_slug_naive` | w 500 | w **524** |
  | `c_kpi_profit_*`, `c_waffle_*`, `c_lb_*`, `c_fall_*` | x 816 / w 424 | x **817** / w **422** (426 on p2's fall card) |
  | `z_kpi_profit_strike` | 810,236,436,2 | **811,230,308**,2 (matches the measured value width) |
  | `c_kpi_profit_misread` | 816,264,… | 817,**255**,… |
  | `z_pN_verdict_rule` | y 624 | y **632** (the measured verdict band's top border) |
  | `btn_next_scene` | 1106,100,150,32 | **1124,100,132**,32 |
  | `btn_next_act` (p1) | 1106,648,150,32 | **1142,649,114**,32 |
  | `btn_next_act` (p2) | 1106,648,150,32 | **1110,649,146**,32 |
  | `c_p2_action` … `c_p2_dlg_honest` | y 195/232/251/309/342/379/398 | y **196/229/248/300/333/366/385** |
  | `c_p2_note_*` | y 196/248/352 h 16/44/44 | y 196/248/352 h **22/64/50** |
  | `dn_rating_fall` | 812,422,432,172 | **813,420**,432,172 |
  **Beat-rail widths are a genuine conflict and were resolved by max-width.** The
  prototype's chips auto-size, so the same button measures 187.2 px at SC.1 (with the
  `●`) and 173.4 px at SC.3; PBIR buttons are fixed. Built at the SC.1 (default-beat)
  positions with the widest measured text: `btn_beat_1` 24,100,**188**,32 ·
  `btn_beat_2` **222**,100,148,32 · `btn_beat_3` **380**,100,**222**,32 — 10 px
  gutters, no state clips its own label.
- 2026-08-05 — **Text-container heights are the measured height + ~8 px.** A CSS line
  box is tighter than a PBIR text container, which adds internal padding; at the
  measured heights, 12 pt Consolas clips. x, y and width are measured exactly. Where
  two adjacent transparent text containers overlap by a few px as a result, nothing
  renders differently — both have `background.show = false` and explicit z-order.
- 2026-08-05 — **Live numbers: the phase-B1 `cardVisual` mechanism, unchanged.**
  12 measure-bound cards across the two pages (`c_p1_action`, `c_p1_dlg_naive`,
  `c_p1_dlg_honest`, `c_kpi_profit_label`, `kpi_profit_naive`,
  `kpi_profit_naive_corrected`, `c_p1_note_zeros`, `c_waffle_title`, `c_waffle_foot`,
  `c_verdict_act1`, `c_p2_note_median`, `c_p2_dlg_honest`, `c_verdict_act2`). The
  only literals on either page are contracted non-numeric copy plus the disclosed
  parameters. **The 11 pt trailing clause of `c_verdict_act1` ships as a second
  object** (`c_verdict_act1_note`, 24,672,1040,22) because a card cannot mix
  differently-styled runs — the cost recorded at phase B1, now paid.
- 2026-08-05 — **`c_p1_note_budget`: the stale median is dropped, not typed.** The
  contracted string is `…min $1, median $2,800.` A full pass over the loaded CSV
  (84,510 in-partition non-adult rows) gives **min budget $1** (contract correct,
  kept) and **median budget $2,961** — the contracted $2,800 is stale under the newer
  snapshot and no measure produces it. Following the phase-B1 precedent (p9's stale
  parentheticals), the clause is omitted rather than printed wrong; the note ships as
  `NOTE: Budget is never 0 here. Unknowns arrive as junk: min $1.`
  **To restore:** add a `Median budget (all listings)` measure and bind it beside
  the min.
- 2026-08-05 — **`c_p1_note_negrev` verified TRUE against the loaded snapshot.**
  Exactly **one** in-partition non-adult listing books negative revenue: −$12
  ("Some Bears"). The contracted sentence ships verbatim.
- 2026-08-05 — **`c_waffle_cap` re-worded for the fallback medium (CONTRACT
  DEVIATION — needs designer ack).** The contracted caption
  `green ✓ = VALID (13) · outline = no credible financials (87)` legends a *waffle*:
  filled vs **outline** cells. The bar fallback has no outline cells, and (13)/(87)
  are typed counts. Shipped: `green ✓ = VALID · gray = no credible financials`, with
  the live share printed by `c_waffle_title` (`[Copy · Act I · waffle title]`) and the
  proportion carried by the bar itself. The `✓` and the words remain the non-colour
  carriers.
- 2026-08-05 — **`tbl_perfect_tens` column headers cannot be hidden.** The design
  says "column headers hidden". The published theme schema's `tableEx` →
  `columnHeaders` card has **no `show` property** (`alignment, autoSizeColumnWidth,
  backColor, bold, columnAdjustment, customColumnWidth, defaultColumnWidth, fontColor,
  fontFamily, fontSize, italic, outline*, underline, wordWrap`) and no `show` exists
  anywhere else on `tableEx`. Inventing one was refused. Headers ship **styled quiet**
  (Segoe UI 10 pt `#57534E` on `#FFFFFF`, not bold). This costs a row of vertical
  space and it *helps* a screen-reader user, who now hears real column names.
- 2026-08-05 — **`tbl_perfect_tens` per-column fonts are not expressible.** The
  design wants the score column in Consolas 12 pt bold; `columnFormatting` carries
  only `alignment, backColor, dataBars, fontColor, labelDisplayUnits, labelPrecision,
  style*` — no font family/size/weight per column. The table uses one family
  (Segoe UI 12 pt) and the score column keeps its **trap-red `#B3402E`** plus the
  `[Mark · Rating verdict]` column, which prints `✕ thin evidence` in words. Colour is
  still never the only carrier.
- 2026-08-05 — **`[Color · Rating verdict]` is deliberately NOT bound.** Binding a
  measure into a column's `fontColor` (fx → field value) has a serialisation shape
  this session could not verify, and the filter guarantees every visible row is a raw
  10.0 — the measure would return trap for all of them. The static trap red says the
  same thing with a verified property. **To restore:** bind it by hand in Desktop and
  capture the resulting JSON here.
- 2026-08-05 — **Visual filters were built from typed schema, not memory.**
  `filterConfiguration/1.3.0` + `semanticQuery/1.4.0` were fetched and read:
  `tbl_perfect_tens` and `dn_rating_fall` each carry an **Advanced** filter
  (`Comparison`, `ComparisonKind: 0`, `Literal "10D"`) for `[Rating (raw)] = 10` and a
  **VisualTopN** filter (`{"VisualTopN": {"ItemCount": 3}}`) over a `sortDefinition`
  of `[Votes]` **Ascending**. Note: the classic Desktop `TopN` filter expression does
  **not exist** in `semanticQuery/1.4.0`'s `QueryExpressionContainer` — only
  `VisualTopN` — so that is what was written. If `VisualTopN` does not take, the
  failure is visible (more than three rows) and the story still reads.
- 2026-08-05 — **`actionButton` outline weight: `weight`, not `lineWeight`.** The
  published theme schema lists `visual-actionButton → outline → [lineColor, show,
  transparency, weight]`; there is no `lineWeight`. p1/p2 buttons use `weight`.
  **Pre-existing defect for the next phase to sweep:** exactly two files written at
  phase B1 use `lineWeight` — `p0-box-office/visuals/btn_credits` and
  `p9-end-credits/visuals/btn_home`. Both should be changed to `weight` in one
  single-concern diff. Not fixed here: it is outside this phase's scope and the
  symptom is a button outline at the theme's default thickness instead of 1 px, not a
  broken file.
- 2026-08-05 — **`z_pN_admit` substitutes the contracted `ca-canvas` SVG** with a
  native `shape` (fill `#FFFFFF`, 2 px act-tint outline, centred `ADMIT ONE` in
  Consolas 10 pt ink, `horizontalAlignment: center` / `verticalAlignment: middle` —
  both enums verified). Same substitution the p0 ticket stubs took at phase B1, same
  reason: real text beats an unverifiable data-URI picture. The contracted 1.5 px
  stroke becomes 2 px (`weight` is an integer). Id renamed from the handoff's
  `z_pN_admit_svg` because it is not an SVG.
- 2026-08-05 — **Beat-rail state is built at SC.3 (the fullest state).**
  `btn_beat_3` carries the act-tint fill, cream text and the leading `●`;
  `z_pN_beat3_mark` (the 3 px detached underline, act tint) is visible and
  `z_pN_beat1_mark` / `z_pN_beat2_mark` are `isHidden`. On p1 `kpi_profit_naive` is
  `isHidden` and `kpi_profit_naive_corrected` is visible, exactly as the SC.3
  bookmark specifies. The three marks exist as separate objects so the bookmark phase
  has a **visibility** mechanism for the current-beat indicator even if formatting
  capture on the buttons proves unreliable.
- 2026-08-05 — **`btn_next_scene` and `btn_beat_1..3` carry NO `visualLink`.** They
  are bookmark actions, and bookmarks do not exist yet. Phase B2b adds
  `visualLink.type = 'Bookmark'` (verify the enum spelling against
  `visualConfiguration` before writing it). Everything else on those buttons — shape,
  fill, outline, text, title/background/border/dropShadow — is explicit.
- 2026-08-05 — **Paper-surface override applied per visual, as documented.** Every
  p1/p2 card is `#FFFFFF` with a 1 px `#D8D4C8` hairline and radius 0; text is
  `#211E1A` / `#57534E`; chart neutral is `#78716C`; page + outspace background is
  `#F5F2E9`. One rule, one reason (a single theme cannot serve two surfaces).
- 2026-08-05 — **Scope rule and reserved red checked by script, not by eye.** An
  automated pass over all four built pages finds: act tints (`#2E4A7D` / `#8A6516` /
  `#5B3E8E`) on **no data visual**, and trap red only on the reserved set (slug tags,
  the strike, the MISREAD tag, the three script-doctor rules and their notes, the
  leaderboard's score + verdict columns, the dumbbell's raw dot) plus p9's `[TRAP]`
  glossary tag. Navigation (`NEXT SCENE ▸`, `NEXT ACT ▸`, `THE PREMIERE ▸`) is act
  tint; `btn_home` / `btn_credits` are ink. 0 violations.

### Stage 6 phase B2a — FINDINGS FOR THE DESIGNER / QA (not build defects)

1. **`c_p2_dlg_naive` names a film the leaderboard beside it will not show.** The
   contracted line is `The best film ever made? Las mujeres deciden. A perfect 10.0!`
   A full pass over the loaded CSV confirms *Las mujeres deciden* (Movie ID 458672)
   does hold a **perfect 10.0 on 2 votes** — the sentence is TRUE. But the newer
   snapshot has **4,610** perfect 10s with at least one vote, of which **4,304 have
   exactly 1 vote** (260 have 2, 33 have 3). `tbl_perfect_tens` is contracted as
   *top 3 **ascending** by `[Votes]`*, so it will show three arbitrary **1-vote**
   titles and never this film. The trap reads *harder* that way — but the dialogue no
   longer corresponds to the exhibit next to it. **Decision needed (designer):** (a)
   leave it — the dialogue is an illustration, the table is the population; (b) sort
   the leaderboard **descending** by votes so the most-voted perfect 10 leads; or
   (c) add a `Title · Perfect ten (illustration)` measure and bind the film name live.
   Nothing was changed unilaterally.
2. **Two contracted "at least" strings are now large understatements** — true, but
   thin. `c_lb_more`: "+ at least 18 more perfect 10s" (actual: 4,607 more).
   `c_p2_note_twenty`: "at least 20 films score a perfect 10.0 on 2–3 votes"
   (actual: 293). Both ship verbatim because they are contracted and remain literally
   true; both would be stronger bound to a measure.
3. **Loaded-snapshot counts, for the record** (full CSV pass, 2026-08-05):
   in-partition non-adult listings **84,510** · credible financials **11,116** ·
   coverage **13.15 %** · zero-revenue **66,853 (79.1 %)** · negative-revenue rows
   **1 (−$12)**. Every one of these prints from a measure, so the report stays
   self-consistent; they are here so s7 can reconcile the narrated 85,394 / 84,036.
4. **p1 and p2 carry more tab stops than the handoff enumerates** (31 and 26 vs the
   contracted 23 and 22). The extra stops are the informational card kickers, labels,
   titles and captions (`c_kpi_profit_kicker`, `c_kpi_profit_label`,
   `c_kpi_profit_misread`, `c_waffle_kicker/title/cap`, `c_lb_kicker`,
   `c_fall_kicker/title`) plus `c_verdict_act1_note`. The handoff's enumerated order
   is preserved **exactly as a subsequence**; each label stop sits immediately before
   the value it labels (the p9 precedent). This is deliberate: while the alt-text
   family is blocked, these stops are the only way a screen-reader user hears
   `INSERT — THE NAIVE NUMBER` and the label ending in `(naive)` — carrier 3 of the
   M-003 marking. If the alt-text blocker clears, they can be dropped back to `-1`.

### Stage 6 phase B2b — THE ACT II RULING (recorded design decision)

**Ruled by the coordinator on 2026-08-05, on the phase-B2a finding.** The finding
was that *Las mujeres deciden* is real (perfect 10.0 on 2 votes, Movie ID 458672)
but is one of **4,610** perfect tens, **4,304** of which rest on a **single** vote —
so the leaderboard beside the line could never show it. The ruling replaces the
named-film framing with the aggregate, which is both more damning and snapshot-proof,
and which stops the report implying one film is "the best" when thousands tie.

Implemented exactly as ruled:

- **`Movies (perfect ten)`** = `CALCULATE([Movies], Movies[Vote Average] = 10,
  Movies[Vote Count] >= 1)` and **`Movies (perfect ten, single vote)`** = the same at
  `Vote Count = 1` — both `03 Lie 2 · Ratings`, format `#,0`.
- **`Single-vote ten (illustration)`** = the shrinkage formula at v = 1
  (`1/101 × 10 + 100/101 × C`) ≈ **6.99**, format `0.00`. It sits beside the existing
  `Two-vote ten (illustration)`, which is now unused by any visual but is **retained**
  (nothing is deleted; identifiers are preserved).
- **`Copy · Act II · naive read`** (NEW) composes the ruled sentence with both counts
  live: *"The best film ever made? Take your pick — ‹n› listings score a perfect 10.0.
  ‹n› of them on a single vote."* `c_p2_dlg_naive` changed from a textbox to a
  measure-bound `cardVisual` to carry it. **No film is named anywhere in Act II.**
- **`Copy · Act II · responsible read`** and **`Copy · Act II · verdict`** rewritten to
  the aggregate: *"a perfect 10.0 on a single vote reads ‹6.99› — barely above the
  global mean of ‹6.96›"*, with m and C printed from their disclosed measures.
  `Godfather rating (reference)` is now unused by any visual — **retained**, not
  deleted.
- **`tbl_perfect_tens`** sorts `[Votes]` **Ascending** with a deterministic tie-break.
  **Deviation from the ruling, with its reason:** the ruling named *Movie ID ASC* as
  the tie-break, but the table groups by `Movies[Title]`, so Movie ID is not a
  grouping column and could only be sorted on via an aggregation measure the model
  does not have — or by spending ~40 % of the Title column's width on an ID that the
  aggregate framing no longer needs. The tie-break is **`Movies[Title]` Ascending**:
  it is the visual's own group key, therefore exact, and it is refresh-stable for the
  same data. Each row prints its vote count, as ruled. Overrule this and the fix is
  one projection plus one sort clause.
- **Three Act II strings that depended on the named film or on a typed magnitude were
  rewritten** (contract deviation, logged): `c_p2_note_twovotes` "NOTE: 2 votes." →
  *"NOTE: one vote is enough to score a perfect 10.0."* · `c_p2_note_twenty` "at least
  20 films…" → *"NOTE: a raw score has no evidence floor — it never says how many
  voted."* · `c_lb_more` "+ at least 18 more perfect 10s" → *"sorted by fewest votes,
  then title — three of the perfect tens counted above."* None of the three now types
  a count or a magnitude word; the live counts are printed once, by
  `c_p2_dlg_naive`. This also closes phase-B2a finding 2.
- The screenplay column's honest block moved **+24 px** (trans 314→338, slug 347→371,
  cue 380→404, dialogue 399→423) because the ruled dialogue is four lines where the
  prototype's placeholder was one. `c_p2_dlg_naive` is 86 px tall, not 60.

### Stage 6 phase B2b — decisions (p3 · tooltip · bookmarks)

- 2026-08-05 — **THE PLAY AXIS IS NOT WRITTEN. This is the contracted animation and it
  is now a manual Desktop step, not a silent drop.** What was checked, in order:
  `reportThemeSchema-2.156` (`visual-scatterChart` exposes a **`currentFrameIndex`**
  card, which proves the play axis exists — but a theme schema names cards, never data
  roles); `visualConfiguration/2.3.0` (`queryState` is an **open map keyed by role
  name**, so it enumerates nothing); Microsoft Learn (`power-bi-visualization-scatter`
  and a Learn search for "play axis" — no role name published; the PBIR
  `projects-report` page carries no visual example); this repo's own Desktop-authored
  files (a `lineClusteredColumnComboChart` gives `Category` / `Y` / `Y2` / `Tooltips`,
  a `tableEx` and two slicers give `Values` — **no scatter anywhere**, including
  inside `project/contest/*.pbix`). No published source names the key, so per
  research-first none was invented.
  **Consequence:** `hero_premiere_scatter` ships with `Category` / `X` / `Y` and **no
  play well**, so the year-by-year animation, the native 28 pt year read-out and the
  `▶ PRESS PLAY` control are all absent until the entrant drags
  `'Release Year'[Year Label]` into the Play axis in Desktop (one drag — see the
  checklist). The scatter itself is complete and the finding reads without it;
  `[Label · No date]` already says "they never enter this animation", which becomes
  true the moment the well is filled.
  **`Category` / `X` / `Y` are themselves unverified role keys** (see the token list) —
  they are conventional cartesian names and the failure is visible, not silent.
- 2026-08-05 — **`hero_premiere_scatter` detail.** X = `Sum(Movies.Revenue)` with
  `categoryAxis.logAxisScale = true` (log X, verified property); Y =
  `[Rating (evidence-weighted)]`; Details = `Movies[Title]`; axis titles printed per
  the handoff; value-axis gridlines `#241F28`; legend and category labels off; a
  **`y1AxisReferenceLine` at 6.96** named `C = 6.96`, dashed, `#6E6960` (every
  property and both enums verified). Visual filter
  `[Movies (scatter population)] >= 1` restricts the plot to the credible,
  ≥ m-votes population. Tooltip bound to `tt-movie-poster`.
- 2026-08-05 — **Measure-driven colours are NOT bound, on either page.**
  `[Color · Scatter mark]` (the good-green winner dot) and `[Color · Rating verdict]`
  (the leaderboard) are left unbound. `formattingObjectDefinitions/1.5.0` types
  property values as **`{"type":"object","additionalProperties":{}}`** — completely
  open — so the "fx → field value" serialisation is unverifiable, and a wrong colour
  fails *quietly*, which is exactly the trap the `pbir-authoring` skill warns about.
  The scatter uses an explicit `dataPoint.defaultColor` of neutral `#B5AFA0`.
  **What this costs:** the winner is currently named, not coloured — `c_winner_label`
  carries `✓ ‹winner› — best-selling AND best-rated on evidence`, so the honest read
  still has its glyph and its words, but not its green dot. **Two Desktop steps**
  restore both (see the checklist); capture the JSON when you do.
- 2026-08-05 — **`tbl_refusal_ranks` gains a fifth column and a new measure.**
  `Mark · Rank divergence` = `IF(ABS([Rank · Popularity] − [Rank · Rating (weighted)])
  > 100, "✕", "")` — the design specified this rule in words; implementing it is not
  improvisation, and it is the reserved-red carrier on the refusal card. Popularity is
  still never good/bad-coloured. The table is **80 px tall, not the measured 46**,
  because native table headers cannot be hidden and three rank rows need the room;
  the space comes from the `@ build` placeholder line, an accepted omission
  (asset-fidelity inventory #40).
- 2026-08-05 — **`btn_next_scene` is built as two paired variants.** A static button
  cannot know which beat is showing, so `btn_next_scene` (visible at SC.1 → `bm_pN_b2`)
  and **`btn_next_scene_2`** (visible at SC.2 → `bm_pN_b3`) share one rect and are
  toggled by the bookmarks. At SC.3 **both are hidden** — the handoff says "disabled at
  SC.3" and PBIR has no disabled state, so absent is the honest reading. The existing
  id `btn_next_scene` was **not renamed**.
- 2026-08-05 — **Landing states flipped to the contracted defaults.** p1 and p2 now sit
  on disk in their **SC.1** state (22 and 17 objects `isHidden`), p3 in its **SC.3**
  state (7 hidden). A PBIR page has no "default bookmark" — the on-disk state *is* the
  default — so a scripted check asserts that each page's on-disk hidden set is
  byte-identical to its default bookmark's hidden set. It is. This also restores the
  trap-first opening the fidelity checklist requires: p1 and p2 land on the naive cut
  with all four M-003 carriers present except the blocked alt text.
- 2026-08-05 — **Bookmark mechanism, with its evidence.** Layout verified on Microsoft
  Learn (`developer/projects/projects-report`): `definition/bookmarks/
  [bookmarkName].bookmark.json` plus `definition/bookmarks/bookmarks.json`. Each file
  validates against **`bookmark/2.1.0`** (the newest published; 2.2.0+ are 404) and the
  registry against **`bookmarksMetadata/1.0.0`** (1.1.0+ are 404). Shape used:
  `explorationState.sections[<page>].visualContainers[<visual name>]`, with
  `{"singleVisual": {"display": {"mode": "hidden"}}}` for hidden objects and
  `{"singleVisual": {}}` for shown ones — `VisualContainerDisplayMode` has **no
  "visible" member**, so visibility-on is the absence of `hidden`, which is why every
  visual on the page is listed rather than only the hidden ones. `options` carries
  **only** `suppressData: true`; `suppressDisplay`, `suppressActiveSection` and
  `applyOnlyToTargetVisuals` are absent, which is Data OFF / Display ON / Current page
  ON / All visuals. Learn also documents that Desktop **prunes visuals it cannot
  resolve** from a bookmark, so a stale name degrades rather than corrupts.
- 2026-08-05 — **The current-beat button style is carried twice, on purpose.**
  Each bookmark writes `singleVisual.objects.merge` for the three beat buttons (fill =
  act tint or off; text = the label with or without the leading `●`; font colour), and
  *separately* toggles the three `z_pN_beatN_mark` underline shapes. If the formatting
  merge does not apply, the underline still marks the current beat by **position**, so
  the state is never carried by colour alone. `DataViewObjectDefinitions` is an
  untyped map in the published schema, so the merge is schema-legal but its effect is
  unverified.
- 2026-08-05 — **Tooltip page.** `type: "Tooltip"`, `visibility: "HiddenInViewMode"`
  and `pageBinding: {name, type: "Tooltip"}` — all three verified in `page/2.1.0`.
  Consumers bind through `visualContainerObjects.visualTooltip` with
  `type: 'Canvas'` + `section: 'tt-movie-poster'` (both verified in the theme schema);
  bound on `tbl_perfect_tens` (p2) and `hero_premiere_scatter` (p3).
  Rows are built as **label textbox + measure-bound value card** (the p9 precedent),
  because a `tableEx` fed four measures renders four columns in one row, not four
  label/value rows. The weighted row prints `[Mark · Rating verdict]` beside the
  number so the word travels with the colour. **Nothing in the tooltip is unique to
  it** — title, year, votes, raw and weighted ratings and the popularity rank are all
  printed on canvas on p2/p3, so the tooltip is enhancement, as required.
- 2026-08-05 — **`img_tt_poster` is the one genuinely speculative object.** The `image`
  visual's `image` card properties (`sourceType` enum `image` / `imageUrl` /
  **`imageData`**, `sourceField`, `fit` enum) are verified in the theme schema, but the
  **data-well role key is not published**; `"Values"` was used (this repo's only
  evidenced generic role). If it does not take, the poster box is simply empty and the
  card still reads — which is exactly the fallback the handoff contracted
  ("omitted entirely if the base URL cannot be verified — the card reads without it").
- 2026-08-05 — **Unverified tokens introduced in this phase** (each fails visibly, each
  is a one-line fix; they join the five recorded at phase B1):
  1. `scatterChart` role keys `Category` / `X` / `Y`.
  2. `visualLink.type` value `'Bookmark'` (sibling of the already-used
     `'PageNavigation'`; `VisualLink.bookmark` **is** a published property).
  3. `explorationState.version` value `"1.0"` (the schema requires a string, types no
     value).
  4. The bookmark `objects.merge` payload shape for the beat buttons.
  5. `image` visual role key `"Values"` and the `sourceField` string
     `"_Measures.Image · Poster URL"`.
  6. `filterConfig` type `VisualTopN` behaviour (schema-typed, effect unverified).

### Stage 6 phase B2c — the alt-text layer (2026-08-05)

**Attribution first, implementation second.** The blocker was cleared at the
main-thread level (commit `f4b9420`) by crediting the influencing Fabric Community
post **by publication** in `CREDITS.md` and `contracts/source-register.yaml`, with
the byline recorded as an **outstanding attribution debt**. The adopted idea is
narrow: *make alt text dynamic*. The post's **DAX user-defined function** pattern is
**not** adopted — implementing it would require the author's name first. What ships
is ten plain measures on Power BI's own documented dynamic-alt-text feature, the
accessibility practice this repo already credits to **Meagan Longoria**.

**Ten measures built** in `_Measures`, folder `06 Display\Alt text`, format `@`, each
with a `///` docstring, each composing live numbers from its bound measures — no count
is typed inside a measure: `Alt · kpi_profit_naive · SC1` · `· SC3` ·
`Alt · dn_ticket_waffle` · `Alt · tbl_perfect_tens` · `Alt · dn_rating_fall` ·
`Alt · hero_premiere_scatter` · `Alt · c_refusal_popularity` · `Alt · c_nodate_chip` ·
`Alt · tbl_production_counts` · `Alt · tt_movie_poster`. Model: 79 → **89 measures**.
Two adjustments to the `measures.dax` drafts, both recorded: `Alt · dn_rating_fall`
now uses **`[Single-vote ten (illustration)]`** (not the two-vote one) so it matches
the Act II ruling and the chart it narrates; `Alt · tbl_perfect_tens` gained the two
perfect-ten counts for the same reason.

**On disk the alt text is STATIC, not measure-bound — and that is deliberate.**
The property *path* is verified (`visual.visualContainerObjects.general[0].properties
.altText`; `VisualContainerGeneralFormattingObjects` has a **closed** property list
containing `altText`). The property's **value** is typed `{}` — completely open — so a
measure expression there is exactly as unverifiable as the colour bindings, and its
failure mode is **silence**. Silence is the one outcome a screen-reader user must not
get, so every visual received a literal string in the shape Desktop itself writes.
Per the coordinator's ruling: **no volatile count is typed anywhere**. The strings
state the finding using only contracted literals — `$10,000`, `m = 100`, `C = 6.96`,
snapshot `24 July 2026`, and `6.99`, which is *derived* from m and C
(1/101 × 10 + 100/101 × 6.96) and is therefore not snapshot-volatile. Volatile
quantities are phrased around ("a minority of the basis", "most revenues …",
"the live count is printed on the card"). **Switching to the live measures is one
Desktop step per visual** (`fx → Field value`) and the measures are already there.

**Coverage — 210 visuals, none left undecided:**

| Treatment | Count | Which |
|---|---|---|
| **Content alt** (static finding-stating sentence) | **76** | every `cardVisual`, `tableEx`, chart, scatter · the three ticket buttons · every navigation and beat button |
| **Empty alt** `""` (skipped by readers) | **73** | all decorative chrome — frames, rules, card backgrounds, perforations, ticket internals, the `z_pN_admit` glyphs, the beat marks, the scrim, the chip outlines, `z_tt_bg`, and `img_tt_poster` |
| **Left UNSET** (own text is the accessible content) | **61** | textboxes — slugs, cues, transitions, notes, kickers, captions, the glossary, the credits copy, the tooltip's row labels and footnote |

- **Textboxes are deliberately not given alt text.** A textbox's own runs *are* its
  accessible content; PBIR alt text would replace rather than supplement them, so a
  duplicate sentence would either double-read or silence the real copy. They were
  never on the waiting list.
- **`img_tt_poster` gets empty alt.** The poster is redundant with `c_tt_name`
  directly beneath it — narrating it twice is noise, not access. This is also the
  handoff's own position that the poster is enhancement.
- **State-specific alt on the paired variants (M-003 carrier 4 is now present).**
  `kpi_profit_naive` opens *"Trap exhibit. This profit total treats unknown revenues
  as zero dollars, so it is the naive reading, not a finding…"*;
  `kpi_profit_naive_corrected` opens *"Trap exhibit, struck through and labelled
  MISREAD. The naive profit total is withdrawn…"*. `tbl_perfect_tens` likewise opens
  *"Trap exhibit."*. All four M-003 carriers are now live at SC.1 on p1 and p2.
- **Beat buttons carry the contracted accessible name** — `"Scene N of 3 — <title>"`
  plus what the beat does — which is M-003 carrier 2 for a screen-reader user. These
  are page-specific (p3's beats are The Adjustments / The Refusal / The Premiere).
- **`[Alt · tbl_production_counts]` binds to `c_cr_count_basis_val`** on p9 — the
  cross-foot's *result* — because the counts "table" is built as label/value pairs.
  This is the same slot-named-measure pattern the handoff records for
  `[Alt · c_refusal_popularity]` (→ `tbl_refusal_ranks`) and `[Alt · tt_movie_poster]`
  (→ the tooltip's five value cards, which carry it between them).
- **Build order matters:** `alt_text.py` runs *after* any page regeneration, because
  the page generator writes layout only. A re-run of the generator drops the alt text
  until the patcher is re-run; the validator catches it (`no altText`).

### Stage 6 phase B2b — layout.json vs handoff (p3 · tooltip)

Same rule as phase B2a: measured block rects win; the handoff supplies fonts,
decomposition and anything the prototype did not measure.

| Object | Handoff | Built (measured / resolved) |
|---|---|---|
| `z_p3_verdict_rule` | y 624 | y **632** (the measured verdict band's top border) |
| `c_verdict_act3` | 24,636,1040,56 | 24,**645**,1040,**44** |
| `btn_roll` | 1106,648,150,32 | **1113,649,143**,32 |
| `c_scatter_population` | 40,164,500,18 | **41,165**,**460**,25 — measured w 387 widened for the live `n`; the measured width is the prototype's placeholder string |
| `c_winner_label` | 498,248,336,50 | **455,271,380**,40 |
| `z_adj_chip_floor/_revenue/_m/_c` | y 167/195/223/251, h 22 | y **160/192/224/256**, h **25**; widths kept at the handoff's 132/132/104/104 because the measured spans are content-sized and the live chip strings must not truncate |
| `c_adj_*` labels | x 964, w 110/110/82/82 | x **963**, w = chip − 20 |
| `c_refusal_title` | 952,318,288,20 | 952,318,288,**25** |
| `c_refusal_why` | 952,342,288,32 | 952,**338**,288,**36** |
| `tbl_refusal_ranks` | 952,378,288,52 | 952,**372**,288,**80** (unhidable header + 3 rows; space from the omitted `@ build` line) |
| `c_nodate_chip` | 952,486,288,116 | 952,486,288,**118** — the measured 953,510,286,68 is the prototype's *vertically centred* text block; a PBIR card needs the card interior or it truncates a disclosure |
| p3 beat rail | 24/206/364, w 172/148/200 | **24/242/429**, w **208/177/184** — only the SC.3 screen was measured, so each width is the measured width plus the ●-prefix delta (13.8 px) observed on p1/p2; 10 px gutters |
| `img_tt_poster`, `c_tt_*` | as the handoff | measured rects used verbatim; the four tooltip rows are decomposed into label + value (+ mark on the weighted row) |
| p3 year read-out, `▶ PRESS PLAY`, the `@ build` line | prototype only | **accepted omissions** (asset-fidelity inventory #33, #34, #40) — the first two are native play-axis furniture and appear when the play well is filled |

### Stage 6 phase B2a — beat state lists (superseded by phase B2b; kept for the record)

Nine bookmarks, capture **Data OFF · Display ON · Current page ON · All visuals**.
"Chrome" below is visible in all three beats of its page.

**p1-act-i-profit — 43 visuals**

- *Chrome (all beats, 13):* `z_p1_header_title` · `z_p1_header_rule` · `btn_home` ·
  `btn_credits` · `z_p1_admit` · `btn_beat_1` · `btn_beat_2` · `btn_beat_3` ·
  `btn_next_scene` · `z_p1_verdict_rule` · `c_verdict_act1` · `c_verdict_act1_note` ·
  `btn_next_act`
- *Always-on content (7):* `c_p1_slug_naive` · `c_p1_action` · `c_p1_cue_naive` ·
  `c_p1_dlg_naive` · `z_kpi_profit_card` · `c_kpi_profit_kicker` ·
  `c_kpi_profit_label`
- *Beat marks:* `z_p1_beat1_mark` (b1 only) · `z_p1_beat2_mark` (b2 only) ·
  `z_p1_beat3_mark` (b3 only)
- *Notes block (6, b2 + b3):* `z_p1_note_rule_1` · `c_p1_note_zeros` ·
  `z_p1_note_rule_2` · `c_p1_note_budget` · `z_p1_note_rule_3` · `c_p1_note_negrev`
- *Correction block (2, b3 only):* `z_kpi_profit_strike` · `c_kpi_profit_misread`
- *Honest screenplay (4, b3 only):* `c_p1_trans` · `c_p1_slug_honest` ·
  `c_p1_cue_honest` · `c_p1_dlg_honest`
- *Waffle block (6, b3 only):* `z_waffle_card` · `c_waffle_kicker` · `c_waffle_title` ·
  `c_waffle_cap` · `dn_ticket_waffle` · `c_waffle_foot`
- *KPI variants:* `kpi_profit_naive` visible at **b1 + b2**, hidden at b3 ·
  `kpi_profit_naive_corrected` hidden at b1 + b2, visible at **b3**
- *Button state:* the current beat's button takes fill = `#2E4A7D`, text `#F5F2E9`
  and a leading `● `; the other two take fill off, 1 px `#211E1A` outline, ink text,
  no glyph. **Built state = SC.3.**

**p2-act-ii-ratings — 37 visuals**

- *Chrome (all beats, 12):* `z_p2_header_title` · `z_p2_header_rule` · `btn_home` ·
  `btn_credits` · `z_p2_admit` · `btn_beat_1` · `btn_beat_2` · `btn_beat_3` ·
  `btn_next_scene` · `z_p2_verdict_rule` · `c_verdict_act2` · `btn_next_act`
- *Always-on content (8):* `c_p2_slug_naive` · `c_p2_action` · `c_p2_cue_naive` ·
  `c_p2_dlg_naive` · `z_lb_card` · `c_lb_kicker` · `tbl_perfect_tens` · `c_lb_more`
- *Beat marks:* `z_p2_beat1_mark` (b1) · `z_p2_beat2_mark` (b2) · `z_p2_beat3_mark` (b3)
- *Notes block (6, b2 + b3):* `z_p2_note_rule_1` · `c_p2_note_twovotes` ·
  `z_p2_note_rule_2` · `c_p2_note_median` · `z_p2_note_rule_3` · `c_p2_note_twenty`
- *Honest screenplay + fall block (8, b3 only):* `c_p2_trans` · `c_p2_slug_honest` ·
  `c_p2_cue_honest` · `c_p2_dlg_honest` · `z_fall_card` · `c_fall_kicker` ·
  `c_fall_title` · `dn_rating_fall`
- p2 hides nothing at b3. **Built state = SC.3.**

### Stage 6 phase B2b — the built bookmarks (authoritative)

The nine files in `definition/bookmarks/` are now the record. Every bookmark lists
**every** visual on its page; the counts below are the hidden sets.

| Bookmark | Page | Visuals captured | Hidden |
|---|---|---|---|
| `bm_p1_b1` **(landing)** | p1-act-i-profit | 44 | 22 |
| `bm_p1_b2` | p1-act-i-profit | 44 | 16 |
| `bm_p1_b3` | p1-act-i-profit | 44 | 5 |
| `bm_p2_b1` **(landing)** | p2-act-ii-ratings | 38 | 17 |
| `bm_p2_b2` | p2-act-ii-ratings | 38 | 11 |
| `bm_p2_b3` | p2-act-ii-ratings | 38 | 4 |
| `bm_p3_b1` | p3-act-iii-corrected-cut | 37 | 6 |
| `bm_p3_b2` | p3-act-iii-corrected-cut | 37 | 6 |
| `bm_p3_b3` **(landing)** | p3-act-iii-corrected-cut | 37 | 7 |

Changes from the phase-B2a lists: each act page gained **`btn_next_scene_2`**; the
beat rail's next-scene pair and the three `z_pN_beatN_mark` shapes are toggled per
beat; p1/p2 land on **SC.1** and p3 on **SC.3** (the on-disk state equals the landing
bookmark, verified by script).

**p3-act-iii-corrected-cut — 37 visuals**

- *Chrome (all beats, 12):* `z_p3_header_title` · `z_p3_header_rule` · `btn_home` ·
  `btn_credits` · `z_p3_admit` · `btn_beat_1..3` · `z_p3_verdict_rule` ·
  `c_verdict_act3` · `btn_roll`
- *Always-on content (13):* `hero_premiere_scatter` · `c_scatter_population` ·
  the four chips and their four labels · `z_refusal_card` contents
  (`c_refusal_title`, `c_refusal_why`, `tbl_refusal_ranks`) · `z_nodate_card` ·
  `c_nodate_chip`
- *Paired variants:* `z_adjustments_card` ↔ `z_adjustments_card_lit` (lit at SC.1) ·
  `z_refusal_card` ↔ `z_refusal_card_lit` (lit at SC.2)
- *`z_p3_scrim`* visible at SC.1 + SC.2, hidden at SC.3 · *`c_winner_label`* hidden at
  SC.1 + SC.2, visible at SC.3
- *Rail:* `z_p3_beat{1,2,3}_mark` one per beat; `btn_next_scene` at SC.1,
  `btn_next_scene_2` at SC.2, neither at SC.3

### Stage 6 G6 fix pass — decisions (2026-08-05)

- **The report-level Adult filter IS expressible in PBIR — it is now written.**
  Research trail, not memory: `report.json` declares
  `report/3.3.0/schema.json`; that schema's own property list contains
  `filterConfig` → `$ref: ../../filterConfiguration/1.3.0/schema-embedded.json`,
  whose `FilterContainer` supplies `name` (required), `field`, `type`,
  `filter` (→ `semanticQuery/1.4.0#/definitions/FilterDefinition`),
  `howCreated`, `isLockedInViewMode`, `isHiddenInViewMode`. The literal spelling
  for a boolean is documented in that same file (`Boolean: "true"`), and
  `QueryComparisonKind` 0 = Equal. The `Advanced` + `Comparison` shape was not
  invented — it is the shape this report's own `dn_rating_fall` already uses.
  Verified by validating `report.json` against the live 3.3.0 schema with all
  remote `$ref`s resolved (0 errors) **and** by a negative control: corrupting
  `ComparisonKind` to 99 and `type` to `"NotAThing"` produced exactly 2 errors at
  `/filterConfig/filters/0/...`, proving the validator reaches inside the filter.
  `[Movies (all listings incl. adult)]` is already
  `CALCULATE([Movies], REMOVEFILTERS(Movies[Adult]))`, so the End Credits
  cross-foot now has a non-zero middle line **as designed** — no measure change
  was needed.
- **The act headers lost their per-run tint, by necessity.** A `cardVisual` has one
  `value.fontColor`; it cannot colour "ACT I" differently from the rest of the
  string. The act tint is **not** lost from the header block: `z_pN_header_rule`
  directly beneath each title is a full-width 1 px bar already filled with the act
  tint (`#2E4A7D` / `#8A6516` / `#B79BE8`). The title itself now carries page ink
  (`#211E1A` on paper 14.83:1, `#F2EFE6` on night 15.89:1). Tint stays chrome-only.
- **All three act headers were unified to `24, 36, 830, 44`.** `[Title · Lie 3]`
  measures ~963 px at Consolas 12 pt and cannot fit one line in the 830 px band
  (`btn_home` starts at x 866), so the header wraps; giving p1 and p2 the same box
  keeps one geometry per archetype instead of a per-act exception.
- **FIX-H was resolved by re-phrasing, not by new measures.** Binding "min $1" and
  "−$12" would need two more measures *and* a split of each 198 px note into a
  prose box plus a value card — a layout change. Re-phrasing keeps p1 consistent
  with p9's own refusal to type that figure, and the negative-revenue **count** is
  now printed live on p9 instead.
- **`z_ticketN_stub_rule` is now inert on purpose.** Its outline was the second of
  two facing 2 px edges that made the perforation read as a 5 px bar. PBIR shapes
  have no per-side outline, so a "3-sided" stub frame is not expressible; the
  single-frame + perforation-line composition is the honest equivalent. The three
  visuals are **kept, not deleted**, so their ids stay stable.
- **`c_cr_count_dup_val` was on the wrong row** (y 360 against its label's y 341,
  while all six sibling pairs share a y). Corrected to 341. Found while widening the
  label; not in the review.
- **A fourth stale Act II string was found in the model.** `Movies (perfect ten)`
  carried two `///` lines, the first still describing "a perfect 10.0 on two votes"
  and contradicting the second. The stale line was removed; the measure, its name,
  `lineageTag`, `formatString` and `displayFolder` are untouched.
- **Text fitting was measured, not estimated.** Every width decision in this pass
  (the two credit strings, the act titles, the p9 labels, the p3 beat labels, the two
  re-phrased notes) was measured with Windows GDI `GetTextExtentPoint32W` at the
  visual's own family and size, normalised to 96 DPI logical pixels.

### Stage 6 G6 a11y pass — decisions (2026-08-05)

- **`dataCategory: ImageUrl` is now VERIFIED, and written.** Two independent
  Microsoft sources, neither of them memory: (1) Microsoft Learn,
  `Microsoft.AnalysisServices.Tabular.Measure` — the class exposes a `DataCategory`
  property, "Specifies the type of data contained in the **measure**", so this is
  legal on a measure and not only on a column; (2) the Microsoft `powerbi-authoring`
  plugin's own `references/image.md`, which states that a data-bound image needs the
  field's Data Category set to "Image URL" and instructs the reader to *"search the
  TMDL file for `dataCategory: ImageUrl`"* and to *"add `dataCategory: ImageUrl` to a
  column/measure"* — giving the exact TMDL token. The property name is corroborated
  locally by this model's own `Date` table (`dataCategory: Time`), which has
  round-tripped through Desktop. `validate_tmdl.py --strict` stays at the standing
  waiver only.
- **The per-point winner colour is NOT writable — it stays a Desktop step, and now
  with a citation.** Microsoft's `references/color-strategy.md` states that for
  non-cartesian visuals — naming **scatter** explicitly — `dataPoint.fill` with
  `metadata` selectors is *silently ignored*, and that colouring individual points
  needs **`scopeId`** selectors. No published source in reach documents the `scopeId`
  payload shape, and it would in any case have to encode a specific data-point
  identity: the winner is produced by `[Winner · title]` and is unknown until the
  model is refreshed, which has never happened. Field-driven colour is not a way out
  either — the same reference defines it as an `Aggregation` (Min/Max) over a **column**
  of hex strings, applying to `backColor`/`fontColor`, and this model has no per-row
  colour column. The scatter therefore ships single-colour, `dataPoint.defaultColor`
  `#B5AFA0` (which the same reference confirms is the correct property for a
  single-series chart), and the alt text now says so out loud.
  This closes the older open question 2 with evidence rather than "unverifiable".
- **Beat state had to become two visuals.** Alt text supersedes a button's accessible
  name, so the `●` marking the current scene never reached a screen reader. A bookmark
  cannot fix that: `bookmark/2.1.0` → `SingleVisualConfigState` exposes `objects` but
  **no `visualContainerObjects`**, so `altText` is not mergeable. The current/not-current
  split (the `kpi_profit_naive` pattern) is the only expressible route. Colours are
  byte-identical to what the audit measured — current-state text re-checked at
  7.84:1 (p1), 4.74:1 (p2), 7.01:1 (p3); not-current at 14.83:1 and 15.89:1.
- **p9 reaches 24 stops, not the contracted 14.** Folding the labels away removes 13
  stops and makes each label-and-number a single self-contained announcement. The
  remaining gap is structural: the design counted the two credits blocks as one table
  visual each, and they are built as label/value pairs. Getting to 14 means rebuilding
  them as two `tableEx` visuals — a stage-5 change, not a fix-pass change.
- **`measures.dax` had drifted much further than the two flagged items.** A body-by-body
  comparison against `_Measures.tmdl` found 12 genuinely stale measures. All 12 were
  replaced with the model's text; the file now carries an AUTHORITY banner saying the
  model wins. The 32 stage-4 base measures are absent from that file **by design** —
  it is the stage-5 deliverable — which the banner also records.

### Stage 6 — G6 waiver + handoff pass (2026-08-05)

The pass that ran the sweep step nobody had run. `pbir_detect.py` is gate-blocking at
G6 and returned 63 unwaived findings. Nothing was waived before every finding had been
read individually.

- **Four genuine AI writing tells were FIXED, not waived.** The `ai-dash-emoji` rule
  fired 46 times. The test applied to each: is this dash a *typographic separator the
  form requires* (slug line, glossary entry, title-and-subtitle) or a *rhetorical pivot
  between two independent clauses in lowercase prose*? The second is the AI tell. Four
  hits failed that test, and each had a dashless sibling in the same register on the
  same page — which is what made them outliers rather than house style:

  | Visual | Was | Is | The sibling that convicted it |
  |---|---|---|---|
  | `z_ticket3_tease` | `In which the fixes land — and one is refused` | `In which the fixes land, and one is refused` | `z_ticket1_tease` / `z_ticket2_tease` carry no punctuation at all |
  | `c_p2_note_twenty` | `…no evidence floor — it never says how many voted.` | `…no evidence floor. It never says how many voted.` | `c_p1_note_budget`, `c_p2_note_twovotes` are plain full-stop sentences |
  | `c_lb_more` | `…then title — three of the perfect tens counted above` | `…then title; three of the perfect tens counted above` | `c_verdict_act1_note` uses a semicolon for exactly this join |
  | `c_tt_foot` | `† formula not published — ranked under protest` | `† formula not published. Ranked under protest` | its p3 twin `c_refusal_why` states the same two facts with a full stop |

  Words and meaning are unchanged in all four; only the join changed, and each string
  is the same length or one character shorter, so no rect can re-wrap. The design
  handoff's copy deck was amended in the same pass — deviations go back through the
  contract (invariant 7), not into the report unrecorded.

- **The other 42 dash/emoji hits are contracted typography and are waived.** Screenplay
  slug lines (`INT. THE HONEST SCREENING ROOM — DAY`), `SC.n —` beat labels, `INSERT —`
  shot headings, act and section titles, glossary term–definition rows, TMDB's mandated
  attribution wording, and the `✓` glyphs. The glyphs are not decoration: hard rule 3
  forbids colour as the only carrier, and the handoff implements that as "honest green
  always travels with a `✓`". **Rewriting the copy to satisfy a slop detector would
  damage the entry and break an accessibility hard rule** — the detector is a servant
  here, not the client.

- **All 11 `theme-color-drift` hits were PROMOTED to theme tokens, not waived.** The six
  distinct hexes are all chrome; none is a data mark. Route chosen after reading the
  actual theme schema (`reportThemeSchema-2.156.json`, fetched and inspected this
  session):
  - The root object is `"additionalProperties": false`, so **no invented top-level
    token name is possible**. The free legacy structural slots (`foregroundNeutralLight`,
    `backgroundDark`, `accent`, the `…Alt` variants) exist, but what each drives at
    render time is undocumented, and several are aliases of new-name slots this theme
    already sets — assigning them could shift chrome somewhere unseen. Research-first
    says take the conservative option when the effect is unverified.
  - A `visualStyles.<type>.*` default was rejected for the shape colours: 18 shapes
    carry no explicit `fillColor` and 35 no explicit `lineColor`, so a `*` default
    would repaint them. That is the sense in which those colours "genuinely cannot be
    a plain theme default".
  - Chosen: **named style presets**, `visualStyles.<visualType>.<styleName>`, which the
    schema explicitly permits (`patternProperties` `^(?!\*$).+$`, same `$ref` as `*`)
    and which apply **only** when a visual selects one. Registered:
    `shape.ticketPerforation` `#9A9284` · `shape.parameterChip` `#6E6960` ·
    `shape.spotlightSurface` `#282331` · `image.posterPlate` `#C8C3B4` ·
    `tableEx.leaderboardRule` `#EBE7DC` · `scatterChart.evidenceReference` `#8A8377`.
  - Re-validated at **0 errors**; both theme copies are byte-identical. **Nothing
    renders differently** — deliberate, two days out. The presets are not wired to the
    visuals, which go on stating each colour explicitly as `pbir-style.md` requires of
    every approved visual; the theme is now simply the one place the palette is
    declared. `theme-color-drift`: 11 → 0.

- **`grid-8px` is waived per page, and the handoff's claim was the thing that was
  wrong.** The handoff said "8 px grid throughout" while contracting off-grid rects
  three lines later. Measured truth over 222 visuals / 888 coordinates: 38 % on 8 px,
  55 % on 4 px, 78 % on 2 px, with 19 px the most common rect height after the 32 px
  button — the HTML prototype's line rhythm showing through. The page frame *is* on
  8 px; type-bound rects are not. Re-aligning ~200 visuals two days before the deadline
  would risk contracted line breaks in a screenplay column to move a lint number, so
  the deviation is recorded instead and the handoff sentence corrected.

- **The waiver file is a DRAFT and G6 stays HELD.** 19 entries, each glob checked to
  match exactly its intended findings and nothing more (18 + 7 + 4 + 4 + 1×7 dash
  entries = 42; 6 grid entries = 6; total 48). A gate may be waived only by the user.
  `status.yaml` was deliberately not touched.

- **Handoff amendments made in the same session** (invariant 7 — the contract moves
  first): the p3 scrim `65 % → 80 %` and the constant line `#6E6960 → #8A8377`, both
  with the recomputed ratios (65 % state failed AA at 4.21:1 for the dimmed axis labels
  and 2.12:1 for the line; the 80 % state measures 5.75:1 and 3.56:1, and 4.87:1
  unscrimmed) · the adjustment-chip border `#3A3441 → #6E6960` (1.43:1 → 3.16:1), a
  third fix-pass change that had never been written back · the beat-rail rects updated
  to the built `188 / 148 / 222` from `x 24 / 222 / 380` · asset row 35's repeat of the
  65 % figure · the four amended copy-deck strings · and a theme-notes entry for the
  six new presets, correcting the claim that "nothing in this report needs an ad-hoc
  hex".

- **Not fixed, flagged instead:** seven further copy-deck/disk disagreements left by the
  fix passes (the 1-vs-2-votes fact among them) and the `z_refusal_card_lit` `#2E2933`
  vs `z_adjustments_card_lit` `#282331` inconsistency. Each is a factual or design call
  the entrant owns; they are listed in `06-report-build.md` → *Open questions* 11 and
  12 rather than silently rewritten.

## Manual steps required in Desktop

- [ ] Close Desktop **without saving** and reopen the pbip (Desktop currently
      holds pre-build state; saving would overwrite this build) — verify by:
      Date table shows range 1800–2099 in Power Query after reopen+refresh.
- [ ] Download Kaggle "TMDB Movies Dataset v11" CSV; set `SourceRoot`
      (Transform data → Edit parameters) to the folder containing
      `TMDB_movie_dataset_v11.csv` — verify by: successful refresh.
- [ ] Refresh to materialize `Release Year Key`, `Is Future Release`, the new
      Date range, and the `Release Year` table — verify by: `Release Year`
      shows 301 rows incl. "No date on record".
- [ ] Confirm Date is marked as date table (Table tools → Mark as date table
      = Date[Date]) — verify by: the marking dialog shows validated state.
- [ ] Confirm `SourceRoot` appears under Manage Parameters as Text; recreate
      under the same name if it surfaced as a plain query — verify by: Manage
      Parameters lists it.
- [x] ~~Spot-check a 06-Display stub in a card~~ — superseded 2026-08-05: the
      stubs are filled; see the phase-A spot-check below.

### New at stage 6 phase A (2026-08-05)

- [ ] **Confirm the custom theme is active** — the report already points at it on
      disk, so no `View → Themes → Browse` import should be needed. Verify by:
      opening the pbip and checking `View → Themes` shows **"D7 The Seductive Lies
      - A Trilogy"** as the current theme, with no base-theme regression banner. If
      Desktop ignores it, re-import
      `StaticResources/RegisteredResources/D7-Seductive-Lies.json` by hand and note
      here that the on-disk registration alone was insufficient.
- [ ] **Verify the 10 pt text-class floor took** — verify by: dropping a throwaway
      card and table on a blank page and confirming `label`, `smallLabel`,
      `lightLabel`, `smallLightLabel` and `smallDataLabel` all render at 10 pt.
      `smallDataLabel` is the uncertain one (emitted although Learn does not
      document it); if it did not take, raise it per visual in phase B.
- [ ] **Spot-check the filled display measures** — verify by: putting
      `[Title · Landing]`, `[Label · Method]` and `[Copy · Act I · naive read]` on
      cards and reading real numbers, not `"s5 fills value"` and not blanks. Record
      the **sign** of `[Profit (naive)]` here, because it decides which branch of
      `[Copy · Act I · naive read]` ships ("loses money" vs "prints money").
- [ ] **Set the data category for the poster field to "Image URL"** — the design
      contracts this as a Desktop step and it was **not** written into TMDL:
      `Measure.DataCategory` exists in TOM (the Learn API page resolves), but the
      TMDL serialisation name and the exact enum spelling for an image URL could not
      be verified this session, and research-first forbids guessing a property.
      Where: `[Image · Poster URL]` in `_Measures`, folder `06 Display`. Verify by:
      the `tbl_perfect_tens` poster column renders thumbnails rather than URL text.
      If Desktop writes the property, capture the exact TMDL line here so phase B
      can hold it in source.
- [ ] **Sanity-check one poster actually loads** — verify by: any perfect-ten row's
      thumbnail resolving over the network. If posters 404, the base URL is right
      but the size segment or the stored path is not; fall back to the contracted
      "no posters anywhere" route rather than guessing a different base.
- [ ] **Confirm `[Winner · title]` returns exactly one film** — it is a
      `TOPN(1, …)` over a composite rank and the design promises ties are listed,
      never broken silently. Verify by: a card showing `[Winner · title]` with no
      comma in it. A comma means a genuine tie and the p3 copy must be re-read
      with the designer.
- [ ] **VERIFY-AT-BUILD from the handoff, still open for phase B:** whether the
      installed Desktop build serialises a **textbox dynamic-value run** into PBIR.
      This decides the live-number mechanism for ~20 textboxes (preferred run →
      fallback A `cardVisual` → fallback B typed string). Verify by: authoring one
      textbox bound to `[Title · Landing]`, saving, and reading the resulting
      `visual.json`. Record the verdict here before phase B binds the rest.

### New at stage 6 phase B1 (2026-08-05) — verify these five tokens FIRST

Open the pbip and check these before phase B2 builds 3 more pages on the same
patterns. Each is a one-line fix if wrong; each fails visibly, not silently.

- [ ] **`cardVisual` role name.** Where: `hero_takeaway` (p0). Verify by: the card
      shows the Key Takeaway sentence. **If it is blank**, the role key `"Data"` in
      `query.queryState` is wrong — read the correct key off a card you drop by hand
      in Desktop and correct it in all 14 cards (p0 ×3, p9 ×11) before phase B2.
- [ ] **Button navigation.** Where: `btn_ticket_act1/2/3`, `btn_credits` (p0),
      `btn_home` (p9). Verify by: Ctrl-click each navigates. **If not**, the
      `visualLink.type` value `'PageNavigation'` is wrong. Note the ticket buttons
      target `p1-act-i-profit`, `p2-act-ii-ratings`, `p3-act-iii-corrected-cut`,
      which **do not exist until phase B2** — until then they are expected to fail.
- [ ] **Vertical ticket-stub text.** Where: `z_ticket1_admit` / `z_ticket1_serial`.
      Verify by: `ADMIT ONE` and `TMDB·2026·07·24` read bottom-to-top inside the
      stub. **If the text renders horizontally**, `textAngle: 270L` is wrong — try
      `-90`, else take the documented fallback.
- [ ] **Ticket corner radius.** Where: `z_ticket1_body`. Verify by: 8 px rounded
      corners, and every other surface square. **If the corners look wrong**, swap
      `rectangleRoundedByPixel` for `rectangleRounded`.
- [ ] **Centred text.** Where: `z_marquee_title`, `z_cr_title`, `c_cr_close_src`.
      Verify by: they are centred, not left-aligned. **If left**, the paragraph key
      `horizontalTextAlignment` is wrong for instances.

Also at phase B1:

- [ ] **Confirm the two pages open at 1280×720** with the night canvas `#171418`
      and that `p0-box-office` is the landing page.
- [ ] **Set the report-level filter `Movies[Adult] = FALSE`, then lock it and keep
      the filter pane visible.** Not written to disk: filter-lock properties could
      not be verified. Verify by: the pane shows a locked Adult filter and p9's
      BASIS row equals LISTINGS PER SOURCE minus ADULT TITLES EXCLUDED.
- [ ] **Read the p9 cross-foot and record the three numbers here** once the model
      is refreshed — they are the first live proof that the newer snapshot is
      flowing (expect roughly 85,870 − 1,360 = 84,510, per the coordinator's
      reconciliation; whatever the model says is the truth, and nothing is typed).
- [ ] **Check the tickets' paper tint contrast** on the cream ticket body:
      `#2E4A7D` / `#8A6516` / `#5B3E8E` on `#F5F2E9`. Verify by: the act numeral and
      serial are legible; Act II brass is the worst case at 4.74:1.

### New at stage 6 phase B2a (2026-08-05) — p1 · p2

- [ ] **Confirm both act pages open at 1280×720 on the paper canvas `#F5F2E9`** and
      that `p0`'s three ticket buttons now navigate (the ticket targets
      `p1-act-i-profit` and `p2-act-ii-ratings` exist as of this phase;
      `p3-act-iii-corrected-cut` still does not).
- [ ] **Check the two fallback charts render.** `dn_ticket_waffle`
      (`hundredPercentStackedBarChart`, no Category, two Y measures) should draw one
      full-width bar split green/gray with a bottom legend and a 0–100 % axis.
      `dn_rating_fall` (`clusteredBarChart`) should draw three film rows × two bars
      with a dashed `C = 6.96` reference line. **If either is blank**, the likely
      cause is a role name (`Y` / `Category` / `Tooltips`, taken from this repo's own
      Desktop-authored combo chart) — read the correct key off a chart dropped by
      hand and fix both files.
- [ ] **Check the two visual filters took.** `tbl_perfect_tens` and `dn_rating_fall`
      should each show **three** rows/categories, all at raw 10.0, fewest votes
      first. **More than three rows** = the `VisualTopN` filter did not apply
      (re-apply Top N by hand in the Filters pane and capture the JSON here).
      **Rows that are not 10.0** = the Advanced measure filter did not apply.
- [ ] **Check the reference line.** If `C = 6.96` does not appear on
      `dn_rating_fall`, the `referenceLine` selector id (`refC`) is the suspect —
      add the line in the Analytics pane and copy the id Desktop writes.
- [ ] **Check `tbl_perfect_tens` fits its 144 px card.** Native table headers cannot
      be hidden (see decisions), so the header eats one row. If a scrollbar appears,
      tune `grid.rowPadding` / `grid.imageHeight` / the five `columnWidth` values —
      do **not** shrink text below 10 pt.
- [ ] **Check the poster column.** Until `[Image · Poster URL]` gets the **Image URL**
      data category (still open from phase A), the first table column renders as URL
      text and will look wrong.
- [ ] **Check the beat rail reads at SC.3**: `btn_beat_3` filled Awards-Brass /
      Ledger-Indigo with cream text and a leading `●`, its 3 px underline
      (`z_pN_beat3_mark`) visible, the other two outlined in ink. Then confirm a
      bookmark capture with **Display ON** actually captures the button *fill* — if
      it does not, drive the current-beat indicator with the three `z_pN_beatN_mark`
      shapes (already built as separate, individually hideable objects) and swap the
      button text per beat.
- [ ] **Check `z_p1_admit` / `z_p2_admit`**: `ADMIT ONE` centred inside a 2 px
      tinted rectangle. If the text is not centred, `horizontalAlignment` /
      `verticalAlignment` on a shape's text card is wrong for instances.
- [ ] **Check the act-II brass on paper**: `#8A6516` on `#F5F2E9` is the worst-case
      contrast in the report (4.74:1) and carries the header rule, the beat fill,
      the verdict rule and `THE PREMIERE ▸`.
- [ ] **Read `[Profit (naive)]`'s sign off `kpi_profit_naive_corrected`** and record
      it here — it still decides which branch of `[Copy · Act I · naive read]` ships
      ("loses money" vs "prints money"), and the strike (`z_kpi_profit_strike`,
      811,230,308,2) is positioned for the measured value width. If the rendered
      number is wider or narrower, nudge the strike.

### New at stage 6 phase B2b (2026-08-05) — p3 · tooltip · bookmarks

- [ ] **THE PLAY AXIS — the one contracted feature that is not on disk.** Open
      `p3-act-iii-corrected-cut`, select `hero_premiere_scatter`, and drag
      `'Release Year'[Year Label]` into the **Play axis** well (sort it by
      `Year Sort`). Leave the play head on the **latest** year. The native year
      read-out and the `▶ PRESS PLAY` control appear with it — both are contracted as
      native furniture, not as custom objects. **Then save and read the resulting
      `visual.json`, and record the play-axis role key here** so the next build can
      hold it in source.
- [ ] **Confirm the scatter renders at all.** If it is blank, one of the role keys
      `Category` / `X` / `Y` is wrong — drop a scatter by hand, read the keys off its
      JSON, and correct `hero_premiere_scatter`. Also confirm the **X axis is
      logarithmic** and the dashed **`C = 6.96`** line is present.
- [ ] **Bind the two conditional colours** (`fx → Field value`), then capture the JSON
      here: `hero_premiere_scatter` → Data colors → `[Color · Scatter mark]` (this is
      what turns the winner dot good-green `#4ECBA0`); `tbl_perfect_tens` → the
      `Rating (raw)` column → `[Color · Rating verdict]`.
- [ ] **Test the nine bookmarks.** Open the Bookmarks pane: nine entries should be
      listed, grouped p1 → p2 → p3. Click each and confirm the beat state changes.
      **If the beat buttons do not change fill/label**, the `objects.merge` payload did
      not apply — the underline marks still show the current beat, and the fix is to
      re-capture the three bookmarks of that page by hand with
      **Data OFF / Display ON / Current page ON / All visuals**.
- [ ] **Test the rail wiring.** `SC.1/2/3` buttons and `NEXT SCENE ▸` should all
      navigate. **If nothing happens**, `visualLink.type` value `'Bookmark'` is wrong —
      read the correct value off a bookmark button created by hand.
- [ ] **Confirm the landing states**: p1 and p2 open on **SC.1** (naive cut, `[naive
      cut]` tag, beat 1 filled), p3 opens on **SC.3** (premiere, no scrim, winner
      label showing).
- [ ] **Test the tooltip.** Hover a `tbl_perfect_tens` row and a scatter point: the
      320 × 420 card should appear. **If it does not**, check
      `visualTooltip.type = 'Canvas'` / `section`. **If the poster box is empty**, the
      `image` visual's role key `"Values"` or its `sourceField` string is wrong —
      either fix it or delete `img_tt_poster` (the contracted fallback; the card reads
      without it).
- [ ] **Confirm `tt-movie-poster` is hidden** in the page tabs and does not appear in
      view mode.
- [ ] **Check `tbl_refusal_ranks` fits** its 288 × 80 box with five columns and an
      unhidable header; tune `columnWidth` if the `✕` or the rank numbers clip.
- [ ] **Read `[Winner · title]` once more** now that it drives both `c_winner_label`
      and `c_verdict_act3`: a comma means a genuine tie and the p3 copy must go back
      to the designer.
- [ ] **Spot-check the Act II ruling's numbers** on a card: `[Movies (perfect ten)]`,
      `[Movies (perfect ten, single vote)]` and `[Single-vote ten (illustration)]`
      (expect ≈ 6.99). Record them here — they are the first live proof of the ruling.
- [ ] **Check the Act III plum on night**: `#B79BE8` on `#171418` carries the header
      rule, the beat fill (with `#211E1A` text on the fill), the verdict rule,
      `NEXT SCENE ▸` and `ROLL CREDITS ▸`.

### New at stage 6 phase B2c (2026-08-05) — the alt-text layer

- [ ] **Optional but recommended: upgrade the 10 data visuals from static to live alt
      text.** Select the visual → Format → General → Alt text → `fx` → *Field value* →
      the matching measure in `06 Display\Alt text`. The pairs are:
      `kpi_profit_naive` → `[Alt · kpi_profit_naive · SC1]` ·
      `kpi_profit_naive_corrected` → `[Alt · kpi_profit_naive · SC3]` ·
      `dn_ticket_waffle` → `[Alt · dn_ticket_waffle]` ·
      `tbl_perfect_tens` → `[Alt · tbl_perfect_tens]` ·
      `dn_rating_fall` → `[Alt · dn_rating_fall]` ·
      `hero_premiere_scatter` → `[Alt · hero_premiere_scatter]` ·
      `tbl_refusal_ranks` → `[Alt · c_refusal_popularity]` ·
      `c_nodate_chip` → `[Alt · c_nodate_chip]` ·
      `c_cr_count_basis_val` → `[Alt · tbl_production_counts]` ·
      the tooltip's value cards → `[Alt · tt_movie_poster]`.
      **Capture the resulting JSON here** — it closes the last unverified binding
      shape in this report. Until then the static sentences are accurate and complete;
      they simply do not carry live figures.
- [ ] **Re-run `alt_text.py` after any page regeneration.** The page generator writes
      layout only; alt text is applied by a second pass. The structural validator
      fails loudly (`no altText`) if the order is missed.
- [ ] **Hand-test with a screen reader** (the accessibility judge does). Expected:
      chrome is silent; every card, table and chart states its finding; the beat
      buttons announce "Scene N of 3"; `kpi_profit_naive` announces "Trap exhibit"
      **before** the number is read.
- [ ] **The attribution debt is open, not closed.** `CREDITS.md` and
      `contracts/source-register.yaml` credit the influencing post *by publication*
      with its byline marked outstanding. A human must open the post in a browser and
      add the author's name. Do not remove or weaken those entries; do not adopt the
      post's DAX-UDF pattern until the name is recorded.

### New at the G6 fix pass (2026-08-05) — verify these FIRST after refresh

- [ ] **The report-level Adult filter.** Open the Filters pane on any page. Expect one
      **locked** card reading *Adult is False* (report-level section, pane expanded,
      not hidden). Then read the End Credits cross-foot: `SOURCE ROWS` −
      `ADULT LISTINGS EXCLUDED` = `BASIS` must be three different, non-zero numbers.
      If `ADULT LISTINGS EXCLUDED` prints 0, the filter did not attach — say so, do
      not paper over it.
- [ ] **The three act headers.** They are now cards bound to
      `[Title · Lie 1/2/3]`. Expect a stated finding, not a topic. p3's title wraps to
      two lines in a 44 px box — confirm nothing is clipped; if it is, raise the box
      to 48 px (y 32) rather than dropping below 10 pt.
- [ ] **Both tables' headers.** `tbl_perfect_tens` and `tbl_refusal_ranks` should show
      no header text at all (ink == fill). If a header still reads, the theme is
      overriding `columnHeaders.fontColor` — set it again in the Format pane.
- [ ] **The ticket perforation on p0.** Each ticket must read as **one** framed ticket
      with a single hairline tear, not two boxes. `z_ticketN_stub_rule` is deliberately
      inert; do not "fix" it by switching its outline back on.
- [ ] **Beat SC.2 on p3.** Click SC.2 and confirm the refusal card visibly changes:
      the outline goes from 2 px to 4 px and the fill lifts one step. If the change is
      still not obvious on your display, brighten the lit outline rather than the fill.
- [ ] **`NEGATIVE REVENUE` on p9** prints a live count from
      `[Movies (negative revenue)]`, and `DUPLICATE (TITLE, DATE) PAIRS` now fits on
      one line beside its value on the same row.

### New at the G6 a11y pass (2026-08-05)

- [ ] **Tab the beat rail on p1, p2 and p3 with a screen reader.** Expected: exactly
      one beat announces "Scene N of 3, **current scene** — …" and the other two
      announce without it; clicking a beat swaps which one does. If both variants of a
      beat are ever audible at once, a bookmark's `display.mode` did not apply.
- [ ] **Tab p9.** Expected 24 stops, each count and parameter announced as one
      self-contained sentence ("Duplicate title-and-date pairs: …"), with no bare
      label stops in between.
- [ ] **Look at p3 at SC.1 and SC.2 with the scrim down.** The axis labels and the
      dashed C = 6.96 line must stay legible; they were re-computed to 5.75:1 and
      3.56:1 but have never been rendered.
- [ ] **Check `tt-movie-poster` actually shows a poster.** The measure now carries
      `dataCategory: ImageUrl`; if the tooltip image is still blank after a refresh,
      the category did not survive the round-trip — record what Desktop wrote.
- [ ] **`dn_rating_fall` data labels** should now sit outside the bar ends against the
      white card, not inside the red bar.

## Validation status

```
[2026-08-04]
validate_tmdl.py --strict : 15 file(s), 0 error(s), 0 warning(s)
pbip JSON                 : 32 file(s) well-formed, no BOM
tmdl_inventory            : 10 tables / 33 measures / 8 relationships

[2026-08-05 — stage 6 phase A]
validate_tmdl.py --strict : 15 file(s), 1 error(s), 0 warning(s)
                            the 1 error is the standing SourceRoot drive-letter
                            waiver in expressions.tmdl line 34 (waived
                            2026-08-04, see 04-model-build.md). It was present
                            before this phase and is unchanged by it. No other
                            error, no warning.
pbip JSON                 : 33 file(s) well-formed, no BOM (41 repo-wide, 0 err)
report.json               : 0 errors vs its declared report/3.3.0 schema
theme (installed copy)    : 0 errors vs reportThemeSchema-2.156 (Draft-7)
reference cross-check     : every [measure] and Table[Column] reference in
                            _Measures.tmdl resolves to a real object
tmdl_inventory            : 10 tables / 73 measures / 8 relationships
                            01 Core 4 · 02 Financials 6 (+1 Trap) ·
                            03 Ratings 14 · 04 Popularity 5 ·
                            05 Data health 9 · 06 Display 34 ·
                            06 Display\Alt text 0 (10 deferred)
pbir CLI                  : not installed on this machine — direct JSON editing
                            fallback used (per DEPENDENCIES.md)

[2026-08-05 — stage 6 phase B1]
validate_json.py          : 120 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings — TMDL was not touched in this phase
visualContainer structure : 77 new visual.json validated against the published
                            visualContainer/2.9.0 schema (name/position/required/
                            no stray top-level properties) — 0 errors
page schema               : p0-box-office + p9-end-credits validated against
                            page/2.1.0 — 0 errors
binding cross-check       : all 14 measure projections resolve to measures that
                            exist in _Measures.tmdl
layout cross-check        : every visual inside the 1280×720 canvas; no duplicate
                            ids; folder name == visual name on all 77
accessibility check       : p0 tab order == the handoff's 10 enumerated stops in
                            order; p9 reads top-to-bottom with each label stop
                            immediately before its value stop; no altText written
reserved-red check        : trap red appears only in c_cr_glossary's [TRAP] tag

[2026-08-05 — stage 6 phase B2a]
validate_json.py          : 202 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. TMDL touched this phase: one measure added
                            (Movies (no credible financials)); nothing else.
visualContainer structure : all 157 visual.json on the four built pages validated
                            against the published visualContainer/2.9.0 schema —
                            and this time DEEPLY: the remote sub-schemas were
                            resolved and applied too (visualConfiguration/2.3.0,
                            filterConfiguration/1.3.0, semanticQuery/1.4.0,
                            formattingObjectDefinitions/1.5.0). 0 errors.
                            Only relaxation: the $schema const (the files declare
                            2.11.0, matching every other visual.json Desktop wrote
                            for this report; 2.11.0 itself is 404).
page schema               : p1-act-i-profit + p2-act-ii-ratings validated against
                            page/2.1.0 — 0 errors
pages registry            : pages.json validated against pagesMetadata/1.1.0 —
                            0 errors; order p0, p1, p2, <2 starters>, p9
binding cross-check       : every measure and Table[Column] projection AND every
                            filter field on all four pages resolves to a real
                            object in the model — 0 dangling references
layout cross-check        : every visual inside the 1280x720 canvas; no duplicate
                            ids; folder name == visual name on all 157
accessibility check       : p1 and p2 contain the handoff's enumerated tab order
                            exactly as a subsequence (31 and 26 stops vs 23 and 22
                            enumerated — see finding 4); no text below 10 pt;
                            no altText written anywhere
scope-rule check          : 0 act-tinted data marks across all four pages
reserved-red check        : trap red confined to the reserved set (slug tags, the
                            strike, MISREAD, the 3 note rules + notes, the
                            leaderboard score/verdict columns, the raw-rating bar)
                            plus p9's [TRAP] glossary tag — 0 violations
snapshot cross-check      : min budget $1 and the single −$12 revenue row verified
                            against the loaded CSV; the contracted $2,800 median
                            was NOT verified (actual $2,961) and was dropped

[2026-08-05 — stage 6 phase B2b]
validate_json.py          : 267 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. TMDL touched: 5 measures added, 2 edited
                            in place (expression + docstring only)
visualContainer structure : all 210 visual.json on the six built pages validated
                            DEEPLY against visualContainer/2.9.0 with its remote
                            sub-schemas resolved (visualConfiguration/2.3.0,
                            filterConfiguration/1.3.0, semanticQuery/1.4.0,
                            formattingObjectDefinitions/1.5.0) — 0 errors
page schema               : all six pages vs page/2.1.0 — 0 errors, incl. the
                            tooltip page's type / visibility / pageBinding
pages registry            : pages.json vs pagesMetadata/1.1.0 — 0 errors; the
                            registry and the pages/ folders match exactly
bookmark schema           : 9 files vs bookmark/2.1.0 — 0 errors;
                            bookmarks.json vs bookmarksMetadata/1.0.0 — 0 errors
bookmark completeness     : every bookmark captures every visual of its page
                            (44/38/37) — 0 missing, 0 unknown
landing-state check       : each act page's on-disk isHidden set is byte-identical
                            to its landing bookmark's hidden set (p1 b1, p2 b1,
                            p3 b3)
link cross-check          : every visualLink bookmark name, every navigationSection
                            page name and every visualTooltip section resolves to a
                            real bookmark/page — 0 dangling
binding cross-check       : every measure, column, aggregation, sort field and
                            filter field on all six pages resolves — 0 dangling
layout cross-check        : every visual inside its page canvas (1280x720, and
                            320x420 on the tooltip); no duplicate ids; folder
                            name == visual name on all 210
accessibility check       : the handoff's enumerated tab order is present as an
                            exact subsequence on p1, p2 and p3; no text below
                            10 pt anywhere; no altText written anywhere
scope-rule check          : 0 act-tinted data marks across all six pages
reserved-red check        : trap red confined to the reserved set — Act I/II slug
                            tags, strike, MISREAD, note rules + notes, leaderboard
                            score/verdict columns, the raw-rating bar, the p3
                            refusal card + its title + its divergence column, the
                            tooltip's raw-rating value, and p9's [TRAP] tag.
                            Navigation (NEXT SCENE / NEXT ACT / THE PREMIERE /
                            ROLL CREDITS) is act tint; btn_home / btn_credits ink

[2026-08-05 — stage 6 phase B2c, the alt-text layer]
validate_json.py          : 267 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error (the standing SourceRoot waiver),
                            0 warnings. 89 measures, 10 of them in the new
                            06 Display\\Alt text folder
visualContainer structure : all 210 visual.json re-validated DEEPLY against
                            visualContainer/2.9.0 with remote sub-schemas
                            resolved — 0 errors
alt-text coverage         : 76 content + 73 empty-decorative + 61 textboxes left
                            unset = 210. The check now FAILS if a non-textbox
                            visual has no altText, if decorative chrome carries a
                            non-empty string, or if a content string is too short
                            to state a finding. 0 failures
alt-text waiting list     : CLOSED — every visual on it carries alt text
volatile-count check      : no static alt string contains a snapshot-dependent
                            count; only $10,000, m = 100, C = 6.96, 24 July 2026
                            and the derived 6.99 appear as literals
bookmark / link / binding / layout / scope-rule / reserved-red checks : unchanged
                            from phase B2b, all still 0 errors

[2026-08-05 — stage 6 G6 FIX PASS]
validate_json.py          : 251 file(s) repo-wide, 0 errors, no BOM
                            (was 267 before the two template pages and their
                            17 visual.json were deleted; +3 files added since)
validate_tmdl.py --strict : 15 file(s), 1 error, 0 warnings — the 1 error is the
                            standing SourceRoot drive-letter waiver
                            (expressions.tmdl line 34). No new TMDL defect.
visualContainer/2.9.0     : 213 visual.json, remote $refs resolved, 0 errors
page/2.1.0                : 6 page.json, 0 errors
pagesMetadata/1.1.0       : pages.json, 0 errors
report/3.3.0              : report.json INCLUDING the new filterConfig, 0 errors
                            (negative control confirmed the filter subtree is
                            actually traversed — see the fix-pass decisions)
bookmark/2.1.0            : 9 bookmark files, 0 errors
bookmarksMetadata/1.0.0   : bookmarks.json, 0 errors
check_contrast.py         : 6 pair(s), 0 failures
binding cross-check       : 53 distinct bound properties across 213 visuals,
                            all resolve to one of 90 measures / 35 columns
tab-order check           : no duplicate tabOrder on any page
                            (p0 11 · p1 32 · p2 27 · p3 21 · p9 37 stops)
page census               : 6 pages — 5 visible at 1280×720 + 1 Tooltip page
                            (320×420). The contest maximum is 5.

[2026-08-05 — stage 6 G6 A11Y PASS]
validate_json.py          : 260 file(s) repo-wide, 0 errors, no BOM
validate_tmdl.py --strict : 15 file(s), 1 error, 0 warnings — the standing
                            SourceRoot drive-letter waiver only
visualContainer/2.9.0     : 222 visual.json, remote $refs resolved, 0 errors
page/2.1.0                : 6 page.json, 0 errors
pagesMetadata/1.1.0       : 0 errors      report/3.3.0 : 0 errors
bookmark/2.1.0            : 9 bookmark files, 0 errors (all rewired this pass)
bookmarksMetadata/1.0.0   : 0 errors
check_contrast.py         : 6 pair(s), 0 failures
binding cross-check       : 53 distinct bound properties across 222 visuals,
                            all resolve to one of 90 measures / 35 columns
bookmark coverage         : each of the 9 bookmarks captures every visual on its
                            page (47 / 47 / 47 · 41 / 41 / 41 · 40 / 40 / 40),
                            and in every one exactly one beat variant is shown
                            and its twin hidden
tab-order check           : no duplicate tabOrder on any page. Effective stops in
                            the landing state: p0 11 · p1 17 · p2 16 · p3 19 ·
                            p9 24 · tooltip 0
deferral scan             : 0 alt strings contain a phrase pointing the reader at
                            something on screen (was 11)
contrast recomputed       : scrimmed axis labels 5.75:1 · scrimmed reference line
                            3.56:1 · p9 dot leaders 8.35:1 · beat-current text
                            7.84 / 4.74 / 7.01:1 · beat-not-current 14.83 / 15.89:1

[2026-08-05 — stage 6 G6 WAIVER + HANDOFF PASS]
!! CORRECTION TO EVERY BLOCK ABOVE: those blocks recorded validate_json,
!! validate_tmdl and ad-hoc schema checks, and an earlier note claimed "all
!! validators clean". That was WRONG. The validate-project sweep has EIGHT
!! steps and step 7 — pbir_detect.py, which is GATE-BLOCKING at G6/G7 — had
!! never been run. First run this pass: 63 findings, 63 unwaived -> FAIL.
!! The full set is now recorded below, honestly, every time.

1 check_state.py          : PASS — state OK: project 'wc-round-3' at stage 6
                            (s6_report_build, in_progress), updated 2026-08-05
2 validate_json.py        : PASS — 260 file(s) checked, 0 with errors
3 check_contrast.py       : PASS — 6 pair(s), 0 failure(s)
                            accent on canvas 3.21:1 · accent on surface 3.21:1
                            good 9.02:1 (both) · bad 6.01:1 (both)
4 validate_tmdl --strict  : 1 ERROR, 0 warnings — 15 file(s). The single error is
                            expressions.tmdl line 34, the committed SourceRoot
                            drive-letter value: the standing entrant waiver from
                            G4. Expected, and the only one.
5 tmdl_inventory.py       : PASS — 10 tables / 90 measures / 8 relationships /
                            1 shared expression; matches the blueprint plus the
                            ten 06 Display\Alt text narrations added at B2c
6 naming grep             : PASS — all 222 visual folders carry a role prefix
                            from design/naming-conventions.md; no Desktop-style
                            32-hex ids anywhere in the report tree
7 pbir_detect.py          : 48 finding(s) across 1 report(s) —
                            0 unwaived, 48 waived -> PASS
                            *** PASS IS CONDITIONAL: the waiver file is a DRAFT
                            awaiting the entrant's signature. A gate may be
                            waived only by the user. Until it is signed, treat
                            step 7 as HELD, not passed. ***
                            before this pass: 63 findings, 63 unwaived -> FAIL
                            (46 ai-dash-emoji · 6 grid-8px · 11 theme-color-drift)
                            after  this pass: 42 ai-dash-emoji (waived, contracted
                            typography) · 6 grid-8px (waived per page) ·
                            0 theme-color-drift (PROMOTED to theme tokens)
8 pbir validate (CLI)     : NOT RUN — the pbir CLI is not installed on this
                            machine (`pbir: command not found`). The documented
                            fallback (direct JSON editing + schema validation) is
                            what this build used throughout. Not a silent skip.

theme re-validation       : theme.json 0 errors vs reportThemeSchema-2.156.json
                            (Draft-7) after the six new named style presets;
                            deliverables/theme.json and the installed
                            StaticResources/RegisteredResources/
                            D7-Seductive-Lies.json are byte-identical
grid measurement          : 222 visuals / 888 coordinates — 38% on the 8px grid,
                            55% on 4px, 78% on 2px; 19px is the most common rect
                            height after the 32px button (34 rects), which is the
                            HTML prototype's line rhythm showing through
```

## Known limitations

- New M columns, the widened Date range, and the Release Year table exist in
  TMDL only until the next refresh — the source CSV is not on this machine.
- `Profit (naive)` is a deliberate trap exhibit (Lie #1): it treats unknown
  financials as $0 and must never appear without its trap marking (s5/s6
  enforce the presentation).
- Financials are nominal, currency-unverified ("USD assumed"); popularity has
  no published definition — see blueprint §7 "metrics NOT available".
- ~~Alt text is missing report-wide~~ — **resolved 2026-08-05.** Every visual now
  carries alt text (76 content, 73 empty-decorative, 61 textboxes reading their own
  copy). **The remaining limitation is that the strings are static**, so they state
  the finding and the disclosed parameters but do not read live figures; the ten
  measures that would are authored and one Desktop step away. The **attribution debt
  is open**: the influencing post is credited by publication, its byline outstanding.
- No measure has been **executed** in this phase. The measures are authored,
  cross-referenced and lint-clean, but Desktop was closed and the model was not
  refreshed, so no value in the report has yet been read out of the model. Every
  number in the built report is bound to a measure rather than typed, so nothing is
  wrong — but the placeholder batch in `data-model.md` is only truly resolved once
  the spot-checks above are done.
- The custom theme is registered on disk but has **never been rendered** by
  Desktop in this repo; the theme-notes list in `design-handoff.md` names several
  properties (notably `smallDataLabel`) whose effect is unverified by anyone.
- **Nothing built in phase B1 has been rendered either.** 77 visuals are
  schema-correct and internally consistent, but no pixel has been seen. The five
  unverified tokens above are the concrete places where "schema-correct" and
  "renders as designed" could still diverge.
- **Letter-spacing is absent report-wide** (PBIR cannot express it). The marquee
  and the section heads will read tighter than the prototype.
- **p9 has 24 tab stops where the design enumerated 14** (was 35 before the G6 a11y
  pass). The 13 bare label stops are gone — each label is folded into its value card's
  alt text, so a screen-reader user now hears one self-contained sentence per row. The
  remaining gap is structural: the design counted each credits block as a single table
  visual, and they are built as label/value pairs. Closing it means rebuilding both
  blocks as `tableEx` visuals, which is a stage-5 decision rather than a fix.
- The ticket perforation is **solid, not dashed** — a contracted fallback, taken
  because PBIR shapes have no dash property.
- **Neither Deneb visual is Deneb.** `dn_ticket_waffle` is a 100 % stacked bar and
  `dn_rating_fall` is a paired bar chart — both are the contracted fallbacks, both
  keep their ids and rects, and neither is the "felt proportion" the waffle promised.
  The 100-ticket metaphor (the signature moment of Act I) is **not in the shipped
  report**; the proportion is stated numerically by `[Copy · Act I · waffle title]`
  and shown as one split bar.
- ~~**`tbl_perfect_tens` shows its column headers**~~ — **resolved in the G6 fix
  pass.** `tableEx` still has no `columnHeaders.show`, so both tables now set
  `columnHeaders.fontColor` equal to `columnHeaders.backColor`; the header row still
  exists for assistive technology but prints nothing. The **one font family per
  table** limit stands.
- **Nothing built in phase B2a has been rendered either.** The two pages are
  schema-correct (deeply, against four published schemas) and every binding resolves,
  but no pixel has been seen and no measure has been executed. The phase-B2a Desktop
  checklist above lists every place where "schema-correct" and "renders as designed"
  could still diverge — the chart role names, the two visual filters, the reference
  line, the table's fit, and whether a bookmark's Display capture carries a button's
  fill colour.
- ~~p1 and p2 are built in their SC.3 state~~ — resolved at phase B2b: the nine
  bookmarks exist, the rail is wired, and p1/p2 land on SC.1 with p3 on SC.3.
- **The play axis is not on disk** — the single largest gap between the contract and
  the shipped file. The Act III animation, its year read-out and its `▶ PRESS PLAY`
  control all appear only after one drag in Desktop (first item on the phase-B2b
  checklist). Until then the scatter is a static premiere and `[Label · No date]`'s
  phrase "they never enter this animation" is describing something the reader cannot
  yet see.
- **The winner dot is not green — and this is now a documented PBIR limit, not a gap
  in our research.** Microsoft's own colour-strategy reference states that scatter
  ignores `dataPoint.fill` `metadata` selectors and that individual points need
  `scopeId` selectors, whose payload no published source in reach documents; a
  `scopeId` would in any case have to encode a data-point identity that does not exist
  until the model is refreshed. The winner is carried by `c_winner_label`'s `✓` and its
  words, and the scatter's alt text now states outright that the plot does not colour
  the winner. One Desktop fx binding still closes it if the entrant wants the colour.
- **`Two-vote ten (illustration)` and `Godfather rating (reference)` are now unused**
  by any visual after the Act II ruling. They are retained, not deleted — nothing
  dangles, but a reader of the model will find two measures no page consumes.
- **Nothing built at stage 6 has been rendered.** 222 visuals and 9 bookmarks are
  schema-correct against eight published schemas and every binding resolves, but no
  pixel has been seen and no measure executed. Eleven tokens across phases B1 and B2b
  are the concrete places where "schema-correct" and "renders as designed" can still
  diverge; each is on the Desktop checklist and each fails visibly.
- **The G6 fix pass added a twelfth unrendered token: the report-level filter.**
  `filterConfig` is schema-correct and its shape is copied from a filter this report
  already carries, but no one has yet seen the filter pane show a locked
  **Adult is False** card, and `[Adult listings excluded]` has never been evaluated.
  If the pane comes up empty in Desktop, the whole End Credits cross-foot is wrong —
  this is the first thing to look at after refresh.
- **The header wrap on p3 is unrendered.** `[Title · Lie 3]` measures ~963 px against
  an 830 px box, so it *must* wrap to two lines inside a 44 px card. Cards centre their
  value vertically; if Power BI clips instead of wrapping, the second line disappears.
  Check p3's header first among the three.

## 2026-08-05 - G6 CORRECTNESS FIX: the shape-fill fallback (root cause found)

**Symptom reported from Desktop.** Every shape that should be cream / white /
dark rendered as solid terracotta `#B3402E`, and the cards showed their measure
name with the value nearly invisible.

**Root cause - a schema-valid property that Desktop silently ignores.**
`#B3402E` is `dataColors[0]` of the D7 theme. Our shapes' `fill` objects were
never bound, so every shape fell back to the shape visual's built-in default,
which is the theme's first data colour. The `fill` object was written as

```
"fill": [ { "properties": { "show": true, "fillColor": <colour> } } ]
```

which passes `visualContainer/2.9.0` deep validation - that schema delegates
`objects` to `formattingObjectDefinitions/1.5.0#/DataViewObjectDefinitions`,
which is `{"type":"object","additionalProperties":{}}`, completely untyped.
Schema-valid, and completely inert. This is the exact trap the `pbir-authoring`
skill warns about, met for real for the first time in this build.

**The ground truth that settled it.** Seven Desktop-authored `shape` visuals were
recovered from git history (`49cae0c~1`, pages `a65cf5aab733edd4ebbd` and
`22a73d6058ce40e505e0`), together with 3 `image`, 2 `slicer`, 3 `textbox` and
2 `tableEx`. Desktop's grammar for the shape formatting objects is:

| object | selector | properties |
|---|---|---|
| `shape` | none | `tileShape` (+ `rectangleRoundedCurve` when rounded) |
| `rotation` | none | `shapeAngle` |
| `fill` | `{"id":"default"}` | `fillColor` - **never** `show` |
| `outline` (off) | none | `show` |
| `text` | none **and** `{"id":"default"}` | `show` in its own entry; `text`/`fontSize`/`fontColor` in the selector'd entry |

The rule, stated once: **the on/off toggle lives in its own selectorless entry;
every property that styles the shape's default part carries
`selector: {"id":"default"}`.** Our own `theme.json` already encodes the same
grammar for buttons (`actionButton.outline` is
`[{show:true}, {$id:"default",...}, {$id:"hover",...}]`), which is independent
corroboration from the published theme schema.

**A second, larger discovery: Desktop round-tripped this project at 13:15 today**
and its save is the strongest evidence in the repo.

- Desktop's canonical `position` key order is `height` before `width`. All 222
  visuals were authored `width, height`; after the save exactly **9** carry
  Desktop's order. Those 9 - and only those 9 - passed through Desktop's
  formatting model. The other 213 were written back byte-verbatim and are
  therefore *unexamined*, so their surviving properties prove nothing.
- On `z_ticket1/2/3_admit` and `z_ticket1/2/3_serial`, **Desktop deleted
  `textAngle`** - the invented property flagged as unverified token 3 in the
  phase-B1 decisions. Proof of the drop mechanism, on a shape, in this repo.
- On `tbl_perfect_tens` Desktop flipped `columnHeaders.autoSizeColumnWidth`
  from `false` to `true`, and on `dn_rating_fall` it reordered the query roles
  and added `"active": true`.

**The correction applied** (structure only - every colour, rect, id and tabOrder
untouched):

```
- "fill": [ { "properties": { "show": true, "fillColor": C } } ]
+ "fill": [ { "properties": { "fillColor": C }, "selector": { "id": "default" } } ]

- "outline": [ { "properties": { "show": S, "lineColor": L, "weight": W } } ]
+ "outline": [ { "properties": { "show": S } },
+              { "properties": { "lineColor": L, "weight": W },
+                "selector": { "id": "default" } } ]

- "tileShape": "'rectangleRoundedByPixel'"
+ "tileShape": "'rectangleRounded'"        (rectangleRoundedCurve: 8L kept)
```

`rectangleRoundedByPixel` is in the published theme enum but is **not** what
Desktop writes; the verified pair is `rectangleRounded` + `rectangleRoundedCurve`
(Desktop wrote `16L` and `4L` on its own header and panel).

**Counts corrected**

| type | visuals touched | fill | outline | tileShape |
|---|---|---|---|---|
| `shape` (63 total) | 57 | 45 | 28 | 8 |
| `actionButton` (38 total) | 35 | 9 | 35 | 0 |
| **total** | **92** | **54** | **63** | **8** |

`actionButton` shares the shape object vocabulary exactly (`shape`, `rotation`,
`fill`, `outline`, `text`) and the theme's own button block uses the same
selector grammar, so the identical correction was applied. The 18 shape and 29
button `fill: [{show:false}]` entries were **left selectorless** - that is
Desktop's own form for a disabled card, and Desktop preserved it verbatim when
it re-serialised `z_ticket1_admit`.

**What this explains beyond the shapes.** 20 textboxes set dark ink `#211E1A`
because they sit on cream backing shapes. Their own structure is a byte-for-byte
match to Desktop's authored textbox (`general[0].properties.paragraphs[].textRuns[]`
with `value` plus `textStyle{fontFamily,fontSize,color,fontWeight}`, no selector,
no `expr` wrapper) - **the textboxes were never broken**; they were dark-on-dark
because their backing shape was rendering as the trap red. Fixing the shapes
fixes the legibility.

**Verified good, and now on the record** (survived Desktop's own re-serialisation
of `tbl_perfect_tens` / `hero_premiere_scatter`, so these are proven, not
inferred): `tableEx` `values`, `grid` (incl. `gridHorizontalColor`,
`gridHorizontalWeight`, `imageHeight`, `rowPadding`), `columnHeaders`
(selectorless), `columnFormatting` and `columnWidth` (both `{"metadata": ...}`
selectors); `scatterChart` `categoryAxis`, `valueAxis`, `dataPoint.defaultColor`
and `y1AxisReferenceLine` with `{"id":"refC"}`; and the visual-container objects
`title` / `background` / `border` / `dropShadow` / `general.altText`, all
selectorless, with `background`/`border` carrying `color`, `transparency`, `width`.

**Still unverified - the honest list.** None of these was changed this pass.

1. **`cardVisual` - deliberately untouched.** There is no Desktop-authored card
   anywhere in this repo. All 46 write `label: [{show}]` and
   `value: [{fontColor, fontFamily, fontSize, horizontalAlignment, show,
   textWrap}]`, both selectorless. The reported symptom - label visible, value
   nearly invisible - is the same fallback signature, and `value.show` is the
   same kind of extra `show` that Desktop omits from `fill`. A reference card
   authored in Desktop settles it; guessing a second time would not.
2. `shape.text` `horizontalAlignment` / `verticalAlignment` (3 visuals) - absent
   from every Desktop shape text seen, which only ever carried `text`,
   `fontSize`, `fontColor`, `fontFamily`.
3. `fill.transparency` on one shape - Desktop never wrote it.
4. `actionButton.shape` is selectorless here, but the theme writes
   `shape: [{$id:"default", roundEdge:0}]`. Left alone rather than invent a
   selector Desktop has not been seen to use.
5. `textbox` paragraph `horizontalTextAlignment` (12 paragraphs) and textRun
   `fontStyle` (6 runs) - Desktop's authored paragraphs carried only `textRuns`
   and `listType`.
6. The `image` visual `img_tt_poster` is the **least verified object in the
   report**: it binds a measure through `query.queryState.Values` and writes
   `sourceType` / `sourceField` / `fit` / `strokeShow` / `strokeColor` /
   `strokeWidth`, whereas Desktop's only authored image uses a completely
   different static-resource shape (`sourceFile.image.{name,url,scaling}`).
   Assume it falls back until seen.
7. `z_ticket1/2/3_stub_rule` carry `outline.show = false` **and** a `lineColor`
   plus `weight` - styled but disabled, so they draw nothing. Structure
   corrected, value deliberately preserved; if the perforation is meant to be
   visible this is a content bug, not a structural one.

**The lesson, for this log and the toolkit.** A schema-valid PBIR property can
be silently ignored, and the failure mode is a theme default that looks like a
design decision. The published schemas cannot catch it because the formatting
object bag is untyped. **Desktop-authored reference files are the only proof
that a formatting object binds** - recover them from git history, or make
Desktop serialise one, before writing a property shape for the first time.

```
[2026-08-05 - G6 SHAPE-FALLBACK FIX PASS]
validate_json.py          : PASS - 259 file(s) repo-wide, 0 errors, no BOM
visualContainer/2.9.0     : PASS - 222 visual.json validated DEEPLY with all
                            remote sub-schemas resolved (5 schema documents),
                            0 errors. The only reported difference is the known
                            $schema const: our files declare 2.11.0, which is
                            what Desktop writes and Microsoft has not published.
pbir_detect.py            : PASS - 222 visuals scanned, 48 finding(s),
                            0 unwaived, 48 waived (unchanged by this pass;
                            the waiver file is still a DRAFT awaiting signature)
grammar re-audit          : shape + actionButton fill/outline/text/shape/rotation
                            now match the Desktop-authored grammar exactly:
                            fill    54 x selector{id:default} + fillColor only
                            outline 63 x selectorless show + 63 styling entries
                            text    unchanged (already correct)
Desktop round-trip check  : the 9 visuals Desktop re-serialised at 13:15 were
                            NOT overwritten by this pass - all 9 still carry
                            Desktop's height-before-width position order
git                       : NOT committed, by instruction. git diff is the undo.
```

## 2026-08-05 - G6 CORRECTNESS FIX: the cardVisual label/value fallback

**This closes unverified item 1 of the shape-fallback pass above**, which said:
"there is no Desktop-authored card anywhere in this repo ... a reference card
authored in Desktop settles it; guessing a second time would not." A reference
card was authored in Desktop on request. It settles it.

**Symptom.** Every one of the 46 cards rendered its *measure name* as a visible
label ("Title · Landing", "Copy · Act I · action", "Label · Method") and its
value in a fallback colour. Same signature as the shape fill: schema-valid
properties that never bound, so the visual fell back to its built-in default.

**Root cause - the same one, in a second place.** `cardVisual.label` and
`cardVisual.value` are **instance-scoped** objects. A selectorless entry does
not bind. All 46 cards wrote both objects selectorless.

### Desktop's `cardVisual` grammar - confirmed

| object | selector | what Desktop wrote |
|---|---|---|
| `label` | `{"id":"default"}` | `show` (this is how the measure-name label is hidden) |
| `value` | `{"id":"default"}` | `fontColor` |
| `cardCalloutArea` | `{"id":"default"}` | `show` **and** `backgroundFillColor` - **the card's background fill lives here, NOT in `visualContainerObjects.background`** |

Colour wrapper is `{"solid":{"color":{"expr": <EXPR>}}}`; Desktop wrote
`ThemeDataColor` because the entrant picked a theme swatch, and the `Literal`
form `{"expr":{"Literal":{"Value":"'#RRGGBB'"}}}` is what our explicit hexes use.

Note the card grammar differs from the shape grammar in one respect: on a shape
the on/off toggle sits in **its own selectorless entry**, but on a card `show`
travels **inside the selector'd entry** alongside the styling (`label` carries
only `show` and is still selector'd; `cardCalloutArea` carries `show` and
`backgroundFillColor` together). The rule that survives both: **anything that
addresses the default *instance* of an object carries
`selector: {"id":"default"}`.**

### Independent corroboration - the published theme schema

Fetched this session: Microsoft's report theme JSON schema **2.156**
(`microsoft/powerbi-desktop-samples`, `Report Theme JSON Schema/`). It types
`visualStyles.cardVisual`, and the decisive detail is which objects declare a
**`$id`** property (`{"type":"string","anyOf":[{"enum":["default"]},
{"pattern":"^[A-Za-z0-9]+$"}]}`). `$id` in theme form is `selector.id` in PBIR
form, so **`$id` present = instance-scoped = the selector is required**:

| cardVisual object | `$id`? | verdict |
|---|---|---|
| `label` | **YES** | selector required - we had 46 selectorless |
| `value` | **YES** | selector required - we had 46 selectorless |
| `cardCalloutArea` | no | yet Desktop *still* wrote a selector on it |

The last row is the standing caveat: **`$id` presence proves a selector is
needed; its absence does not prove one is wrong.** `shape.fill` and `shape.text`
are the same case - no `$id` in the schema, but Desktop demonstrably writes
`selector:{"id":"default"}`. Desktop evidence outranks the schema signal.

### The correction applied - structural only

Every rect, `id`, `tabOrder`, binding, `altText`, colour value and property was
preserved. The diff is **purely additive: 276 insertions, 0 deletions** across
46 files - 92 selector blocks (46 x `label` + 46 x `value`), and nothing else.

```
  "label": [ { "properties": { "show": false }
+                            , "selector": { "id": "default" }
             } ]

  "value": [ { "properties": { fontColor, fontFamily, fontSize,
                               horizontalAlignment, textWrap, show, [italic|bold] }
+                            , "selector": { "id": "default" }
             } ]
```

**Cards fixed, by page:** p0 3 · p1 11 · p2 5 · p3 8 · p9 12 · tooltip 7 = **46**.

### The card background: deliberately NOT moved to `cardCalloutArea`

The brief asked for the card fill to move to `cardCalloutArea.backgroundFillColor`
(paper `#FFFFFF` on p1/p2, night `#1D1A20` on p0/p3/p9), *checked against the
design handoff, changing no design decision*. That check says **do not move it**:

- The handoff specifies **"background off; border off"** on every `cardVisual`
  row (lines 278, 290, 329, 420 and the "same styling" rows). Cards in this
  report are **transparent text overlays**; the `#FFFFFF` / `#1D1A20` card
  surfaces named in *Page chrome* are drawn by separate `basicShape` rects
  (`z_kpi_profit_card`, `z_lb_card`, `z_fall_card`, `z_waffle_card`,
  `z_adjustments_card`, `z_refusal_card`, `z_nodate_card`, `z_tt_bg`).
- All 46 cards already carry `visualContainerObjects.background.show = false`
  and **no colour** - so there is no stray or conflicting fill to resolve.
  Item 2 of the brief has no work in it; the design decision is already
  expressed as "off", in a Desktop-verified selectorless container object.
- Painting an opaque `cardCalloutArea` would be a **design change with three
  concrete regressions**: it would erase the SC.1 spotlight (the bookmark swaps
  `z_adjustments_card` `#1D1A20` for `z_adjustments_card_lit` `#282331` *behind*
  `c_adj_floor/_m/_c`); it would square off `z_nodate_card`'s **radius 8** under
  `c_nodate_chip`; and it would put a `#1D1A20` slab behind `hero_takeaway`
  (1232x72) where the contract has bare `#171418` canvas.
- Writing `cardCalloutArea.show = false` instead was rejected: **no evidence**
  says whether `false` suppresses only the fill or the whole callout including
  the value. Omitting the object keeps today's observed rendering (backgrounds
  were never part of the reported symptom) and keeps the clean default.

### Re-audit of every property we wrote on cards - nothing removed

Every property on all 46 cards was checked against theme schema 2.156:

| `value` property | in schema? | kept |
|---|---|---|
| `fontColor` | yes (`fill`) - **also Desktop-written** | yes |
| `fontFamily` | yes (`string`) | yes |
| `fontSize` | yes (`number` 8-60; our `28D` literal matches Desktop's `24D` on `shape.text`) | yes |
| `horizontalAlignment` | yes (`alignment` enum = `left`/`center`/`right`; ours are `'left'`/`'center'`) | yes |
| `textWrap` | yes (`boolean`) | yes |
| `italic` (4) / `bold` (1) | yes (`boolean`) | yes |
| `show` | yes (`boolean`) | yes - redundant (default true, Desktop omits it) but schema-typed, so it does not meet the removal bar |

**Result: 0 removals.** Nothing on the cards was invented - the property *names*
were right all along and the design's typography was never the problem. Only the
missing selector was, which is why every one of these properties was being
dropped on the floor together.

### `sortDefinition` - judged incidental, not adopted

The specimen carries `query.sortDefinition` with `isDefaultSort: true`. Not
copied to our 46: a single-value card has no meaningful sort, and the entry
records the sort state Desktop's UI happened to hold. Inventing a direction
(`Descending`) on 46 cards would be exactly the unverified structural guess this
log keeps warning about; Desktop writes it itself on next save if it wants it.
`drillFilterOtherVisuals: true` **is** structural, and all 46 already carry it.

### The permanent reference specimen

The entrant's test card was **deleted from the report** after extraction
(`p0-box-office/visuals/191b3d9019697e50701c/` - unreferenced by any
`page.json`, `pages.json` or bookmark). It is recorded here verbatim so this
ground truth is never lost again:

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.11.0/schema.json",
  "name": "191b3d9019697e50701c",
  "position": { "x": 100, "y": 100, "z": 84, "height": 300, "width": 300, "tabOrder": 1001 },
  "visual": {
    "visualType": "cardVisual",
    "query": {
      "queryState": {
        "Data": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "_Measures" } },
                  "Property": "Financial floor (disclosed)"
                }
              },
              "queryRef": "_Measures.Financial floor (disclosed)",
              "nativeQueryRef": "Financial floor (disclosed)"
            }
          ]
        }
      },
      "sortDefinition": {
        "sort": [
          {
            "field": {
              "Measure": {
                "Expression": { "SourceRef": { "Entity": "_Measures" } },
                "Property": "Financial floor (disclosed)"
              }
            },
            "direction": "Descending"
          }
        ],
        "isDefaultSort": true
      }
    },
    "objects": {
      "label": [
        {
          "properties": { "show": { "expr": { "Literal": { "Value": "false" } } } },
          "selector": { "id": "default" }
        }
      ],
      "value": [
        {
          "properties": {
            "fontColor": {
              "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 2, "Percent": 0 } } } }
            }
          },
          "selector": { "id": "default" }
        }
      ],
      "cardCalloutArea": [
        {
          "properties": {
            "show": { "expr": { "Literal": { "Value": "true" } } },
            "backgroundFillColor": {
              "solid": { "color": { "expr": { "ThemeDataColor": { "ColorId": 0, "Percent": 0 } } } }
            }
          },
          "selector": { "id": "default" }
        }
      ]
    },
    "drillFilterOtherVisuals": true
  }
}
```

### Selector audit extended to every other visual type

Every formatting object and property on all 223 visuals was checked against
theme schema 2.156 and against the Desktop-authored files in git
(`49cae0c~1`, pages `a65cf5aab733edd4ebbd` and `22a73d6058ce40e505e0`).

| type | Desktop evidence | `$id` on any object we use? | our selectors | verdict |
|---|---|---|---|---|
| `cardVisual` | **YES** (this specimen) | `label`, `value` | were selectorless | **FIXED** |
| `shape` | YES (7 visuals) | none, but Desktop selector's `fill`/`text` | matches Desktop | correct (prior pass) |
| `actionButton` | inferred | **`fill`, `outline`, `text` = YES** | selector'd | correct - schema now *confirms* the prior pass's inference |
| `textbox` | YES (3) | none | selectorless | correct |
| `tableEx` | YES (`e21488a8d900077091bd`) | none | selectorless + `{"metadata":…}` on `columnFormatting`/`columnWidth` - Desktop's own form | correct |
| `scatterChart` | partial (Desktop re-serialised `hero_premiere_scatter`) | none | selectorless + `{"id":"refC"}` on the reference line | correct |
| `clusteredBarChart` | partial (Desktop re-serialised `dn_rating_fall`) | none | selectorless + `{"metadata":…}` / `{"id":"refC"}` | correct |
| `image` | YES (3) - but only the **static-resource** form | none | selectorless | property names verified; the **dynamic measure-bound form is still unverified** |
| `hundredPercentStackedBarChart` | **NONE** | none | selectorless | schema-valid, unverified by Desktop |

**Property-name sweep across all 223 visuals: exactly one flag, and it is a
false positive** - `textbox.general.paragraphs` (69x), which is PBIR *content*
rather than a theme-styleable property and is already byte-for-byte verified
against Desktop's own authored textbox. **Every other property name we have
written anywhere in this report exists in the published theme schema.**

**Nothing was removed as unverifiable, on cards or anywhere else** - the sweep
found nothing invented to remove. This does not retract the honest list from the
shape pass: `shape.text.horizontalAlignment`, `fill.transparency`, textbox
`horizontalTextAlignment` / `fontStyle` and the `image` dynamic binding are all
now confirmed to be *real schema property names*; what remains unproven for them
is whether the object binds in the position we wrote it, and only Desktop shows
that.

**Still unverified after this pass** - `hundredPercentStackedBarChart` (no
Desktop-authored example exists anywhere in reach) and the measure-bound `image`
form on `img_tt_poster`. Neither was changed: both are schema-valid and
selectorless, which the `$id` signal supports, and removing working-looking
properties on no evidence would trade a possible fault for a certain one.

```
[2026-08-05 - G6 CARDVISUAL-FALLBACK FIX PASS]
cards fixed               : 46 of 46 (p0 3, p1 11, p2 5, p3 8, p9 12, tt 7)
diff                      : 276 insertions, 0 deletions, 46 files - additive only
validate_json.py          : PASS - 260 file(s) repo-wide, 0 errors, no BOM
visualContainer/2.9.0     : PASS - 223 visual.json validated DEEPLY with all
                            remote sub-schemas resolved (5 schema documents),
                            0 real errors. Only difference is the known $schema
                            const: our files declare 2.11.0, which is what
                            Desktop writes and Microsoft has not published.
                            (re-run after the specimen delete: 222 files, PASS)
pbir_detect.py            : PASS - 0 unwaived findings
theme-schema property     : 223 visuals swept against reportThemeSchema-2.156;
  sweep                     1 flag, a false positive (textbox paragraphs).
                            0 properties removed as unverifiable.
specimen                  : 191b3d9019697e50701c recorded verbatim above, then
                            deleted from p0-box-office (no page/bookmark refs)
git                       : NOT committed, by instruction. git diff is the undo.
```

## 2026-08-05 — REBUILD CHECKPOINT 1: model deltas + theme (no report pages)

The report is being rebuilt to the approved plan
(`i-told-you-i-giggly-castle.md`). Checkpoint 1 is **disk-only model and theme
work** — no page was touched. The verified contest question is *"What makes a
movie successful?"*, and the story now **leads with the answer**: success is two
different things, money and evidence, and they almost never coincide.

Governing constraint applied throughout, from the entrant: **every element must
have a function — "a builder doesn't put nails where they don't need."** Applied
to measures too: nothing below was added without a named consumer in the plan.

### Built — Task A: three calculated columns (+ three sort companions)

| Column | Table | Shape |
|---|---|---|
| `Budget Band` | Movies | `Below floor` (under the disclosed $10,000 floor) · `$10k–100k` · `$100k–1M` · `$1M–10M` · `$10M–50M` · `$50M–100M` · `$100M+` |
| `Budget Band Sort` | Movies | 1–7, hidden, `sortByColumn` target |
| `Vote Band` | Movies | `0` · `1–9` · `10–99` · `100–999` · `1,000+` |
| `Vote Band Sort` | Movies | 1–5, hidden, `sortByColumn` target |
| `Decade` | Release Year | `1800s`…`2090s`, with the −1 unknown member mapped to **"No date on record"** so a dateless listing is never silently dropped from an era axis |
| `Decade Sort` | Release Year | decade's first year; unknown member last at 2100, matching `Year Sort`'s existing convention |

### Built — Task B: two calculated tables

- **`Counts`** — 8 rows (`Line`, `Sort`): Listings per source · Adult excluded ·
  Basis · Duplicate (title,date) pairs · Duplicate IDs · No release date ·
  Future-dated · Negative revenue. **Labels only — every value comes from
  `[Value · Count line]`**, so no count is ever typed into the model.
- **`Parameters`** — 4 rows (`Name`, `Value`, `Derivation`, `Robustness`,
  `Sort`): the financial floor, m, C and the snapshot anchor, each with how it
  was derived and how sensitive the answer is to it.
- Both are **deliberately unrelated to `Movies`**: they are presentation /
  disclosure axes, not dimensions. A relationship would filter the fact table
  meaninglessly. Recorded here because the star-schema rule requires the
  justification in writing.
- Registered in `model.tmdl` as `ref table Counts` / `ref table Parameters`.

### Built — Task C: 24 new measures (90 → 114)

- `01 Core` — `Movies (money bar only)` · `Movies (evidence bar only)` ·
  `Movies (one bar only)` · `Movies (neither bar)` · `Share · both` ·
  `Share · one bar only` · `Share · neither` · `Share · money` · `Share · evidence`
- `02 Lie 1 · Financials` — `Median revenue multiple (credible)`
- `05 Data health · Time` — `Value · Count line`
- `06 Display` — `Title · Budget return` · `Title · Coverage era` ·
  `Title · Vote distribution` · `Label · Adjustments` · `Label · Refusal` ·
  `Label · Tooltip head` · `Copy · Answer · units read` · `Copy · Money · trap` ·
  `Copy · Evidence · trap`
- `06 Display\Alt text` — `Alt · dn_answer_units` · `Alt · ch_budget_return` ·
  `Alt · ch_coverage_by_era` · `Alt · ch_vote_distribution`

### Rewritten — Task D: five bodies, **names and lineageTags untouched**

`Title · Landing` (the Key Takeaway) · `Title · Lie 1` → the MONEY page's answer ·
`Title · Lie 2` → EVIDENCE · `Title · Lie 3` → BOTH · `Label · Caveats` (extended
with the mandated attribution). Each carries a `///` line stating the reframe and,
on the three act titles, an explicit note that the name is kept **because every
binding downstream addresses the measure by name**.

Verified mechanically after the pass: **90 pre-existing measures still present,
0 lineageTags changed, 0 measures lost.**

### Decisions & assumptions

- **`Share · money` and `Share · evidence` are aliases**, not second `DIVIDE`s
  (`= [Financial coverage %]` / `= [Evidence share %]`). The brief said
  "each `DIVIDE(…, [Movies])`"; the aliases compute exactly that while keeping
  *one calculation, one home*. Precedent in-model: `Alt · c_nodate_chip`.
- **`Title · Landing`'s word guard is arithmetic, not a guess.** The long frame
  is 38 words, the short frame (which drops "— and they rarely coincide") is 33.
  The winner's own word count is measured at run time as *spaces + 1* and added;
  the long frame is used while `38 + winnerWords <= 50`. Simulated across winner
  titles of 1–17 words: never exceeds 50. With today's winner (*The Lord of the
  Rings: The Return of the King*, 10 words) it renders at **48 words**, or 46 if
  standalone em-dashes are not counted.
  **Residual, stated honestly:** `[Winner · title]` returns a comma-joined list
  on ties. A tie long enough to blow 50 words would need a copy change, not a
  third branch — recorded rather than silently handled. The measure also assumes
  `hero_takeaway` carries no visual-level filter, so the winner is never blank.
- **Insight titles state findings computed live, never asserted directions.**
  `Title · Budget return` ranks the budget bands at run time and names the best
  and worst; if the ranking flips with the data, the sentence flips with it.
  `Title · Coverage era` holds out decades with fewer than 100 listings so a
  two-film decade cannot win on noise.
- **`Label · Refusal` deliberately carries no number.** It is a methodological
  position; a count would imply popularity had been scored after all. Precedent:
  `Alt · c_refusal_popularity`.
- **`Median revenue multiple (credible)` is a median of per-listing ratios**, not
  a ratio of sums — one blockbuster cannot speak for its band. Its `formatString`
  is written `0.0\×` (backslash-escaped literal, the same escape form as the
  model's existing `\$#,0`) rather than the quote-wrapped `"0.0""×"""` form.
  Identical rendering, no TMDL quote-escaping to get wrong.
- **`Label · Caveats` now carries the mandated attribution inside the measure**:
  `SOURCE DATA BY TMDB, DISTRIBUTED VIA KAGGLE UNDER ODC-BY 1.0 — THIS PRODUCT
  USES TMDB DATA BUT IS NOT ENDORSED OR CERTIFIED BY TMDB` — byte-identical to
  the string already on `z_footer_credit`. The credit now lives in a **bound
  string**, so it cannot be lost by deleting a text box during the rebuild.
- **The four new `Alt ·` measures stay inside the credited scope.** CREDITS.md
  and `contracts/source-register.yaml` credit the dynamic-alt-text prompt *by
  publication* (author byline still outstanding behind the community 403) and
  scope our use to **plain measures on Power BI's own documented feature, not the
  post's DAX-UDF pattern**. No UDF was written; the attribution debt was not
  deepened.

### Research-first — what was verified, and against what

TMDL calculated columns and `DATATABLE` calculated tables do **not** exist
anywhere in this model, so the existing tables could not settle the syntax.
Verified instead against **Microsoft-authored TMDL** in
`microsoft/Analysis-Services` (`pbidevmode/fabricps-pbip/SamplePBIP/`):

| Question | Specimen | Answer adopted |
|---|---|---|
| Calculated column form | `Calendar.tmdl` → `column 'Date (Year-Month)' = DATE([Year], [Month (#)],1)` | inline `= <DAX>`, `dataType` present, **no** `sourceColumn`, `isDataTypeInferred` present |
| Calculated table + DATATABLE | `Dynamic Measure.tmdl` | `partition <T> = calculated`, columns carry `dataType`, `isNameInferred`, `isDataTypeInferred`, `sourceColumn: [Name]` (bracketed) |
| Multi-line calculated source | `Parameter - Dimension.tmdl` | the indentation form (`source =` then a 4-tab body) is valid on a `calculated` partition — matches this repo's M-partition style |
| `sortByColumn` + `changedProperty` | this model's `Date.tmdl` / `Release Year.tmdl`, and `Calendar.tmdl` | unchanged repo form kept |

**Not verified, conservative choice made:** `PBI_Id` (Desktop's own
calculated-table annotation) was **omitted** from `Counts` and `Parameters`
rather than invented — Desktop generates it on save. `PBI_ResultType = Table`
was written and then removed: it is a Power Query navigation annotation and does
not belong on a calculated table.

### Built — Task E: report.json + theme

- **`report.json`:** the duplicate **unlocked** `Movies[Adult] = FALSE` filter
  (`1dade010cb9e3d8665cb`, `Categorical`, no lock) is deleted. Exactly one
  remains — `flt_report_adult`, named "Adult listings", `Advanced`,
  `isLockedInViewMode: true`, and now an **explicit** `isHiddenInViewMode: false`
  so "visible in the pane" is a decision on disk rather than an inherited default.
  `isHiddenInViewMode` verified optional-boolean in `filterConfiguration/1.3.0`.
- **`theme.json`** (and the installed `D7-Seductive-Lies.json`, content-identical;
  the deliverables copy is LF, the installed copy CRLF as Desktop wrote it):
  - **`visualStyles.cardVisual` added.** `label` `$id: "default"` `show: false`
    (this is how Desktop hides the measure-name label), `value` `$id: "default"`
    with `fontColor #F2EFE6` + `textWrap`, and `background`/`border`/`dropShadow`/
    `visualHeader`/`title`/`padding` off. The grammar is the entrant's own Desktop
    specimen, recorded verbatim in this log on 2026-08-05. **Without this block the
    global `"*"/"*"` rule painted `#1D1A20` behind all 46 cards — the black slabs.**
    No `fontFamily`/`fontSize` written at theme level: those belong to the
    `callout` text class and to the per-card properties, which already carry the
    design contract's typography.
  - **`visualStyles.pageNavigator` added** — one navigator replaces ~16 per-page
    buttons. `pages.showHiddenPages/showTooltipPages: false` (the hidden tooltip
    must not appear in it), `layout.orientation: 2` (Horizontal), fill off, and the
    current page marked by **outline weight 1 → 2 plus a brighter, bolded label**
    — never colour alone. `shape` written selectorless: unlike `actionButton`,
    `pageNavigator.shape` declares no `$id` in the schema and no Desktop specimen
    exists, so the conservative form was chosen.
  - **Legacy structural aliases added** — `foreground #F2EFE6`,
    `foregroundNeutralSecondary #B5AFA0`, `foregroundNeutralTertiary #78716C`,
    `backgroundLight #1D1A20`, `backgroundNeutral #2E2933`, mirroring the
    first/second/fourth-level elements and the night surfaces so nothing inherits
    Fluent2's LIGHT values on a night page.
  - **Fonts cut to the Mac-safe set.** `Bahnschrift SemiCondensed` and `Consolas`
    are **deleted from the design**. The mapping keeps the handoff's stated roles
    (line 102: Bahnschrift = display and chrome caps · Consolas = screenplay body
    and numerals · Georgia = verdicts and editorial framing):
    `callout` → **Courier New** · `largeTitle`, `header` → **Arial Black** ·
    `title` and all label classes → **Arial**. The 11 `Segoe UI` families inside
    `visualStyles` (chart axes, table text, button text) went to **Arial** in the
    same pass — the plan's constraint is report-wide, and leaving Segoe UI on the
    chart axes would have missed the visible half of it. **Georgia keeps no
    textClass slot**: it is applied per-visual, exactly as the handoff already does.
  - **`basicShape` pruned.** Dead: the valid visual name is `shape`, and a scan of
    all 222 visuals finds **zero** `basicShape` visuals (63 are `shape`).

### Validation status — 2026-08-05, checkpoint 1

```
validate_tmdl.py --strict : 17 file(s), 1 error, 0 warnings
                            The 1 error is the STANDING SourceRoot drive-letter
                            waiver (expressions.tmdl:34). Expected steady state.
validate_json.py          : 259 file(s), 0 errors, no BOM
theme vs reportThemeSchema-2.156 (fetched this session, jsonschema Draft7):
                            deliverables/theme.json           0 errors
                            RegisteredResources/D7-*.json     0 errors
theme negative control    : 7 deliberate faults injected; 6 CAUGHT
                            (cardVisual.value.fontSize range, pageNavigator
                            text/layout/outline enums, foreground type,
                            textClasses unknown class). 1 not caught - an unknown
                            property NAME inside cardVisual.label, because that
                            item schema does not set additionalProperties:false.
                            Every property name written was separately checked
                            against the schema's own property list.
model reference integrity : every [measure] and Table[Column] reference in
                            _Measures.tmdl resolves to a defined object (114
                            measures, 12 tables). 0 unresolved.
lineageTag preservation   : 90 pre-existing measures, 0 tags changed, 0 lost.
pbir_detect.py            : PASS - 48 findings, 0 unwaived (old pages, unchanged)
pbir CLI                  : NOT INSTALLED on this machine - direct JSON editing
                            used, per DEPENDENCIES.md's documented fallback.
git                       : NOT committed, by instruction. git diff is the undo.
```

### Manual steps required in Desktop — checkpoint 1

- [ ] **REFRESH the model.** The three calculated columns and the two calculated
      tables are **definitions on disk only** until Desktop recalculates. Nothing
      that binds to `Movies[Budget Band]`, `Movies[Vote Band]`,
      `'Release Year'[Decade]`, `Counts` or `Parameters` will resolve before then.
      *Verify:* the columns appear in the Fields list, `Counts` shows 8 rows and
      `Parameters` 4 rows.
- [ ] **Reproduce the six snapshot numbers before any report work** (the plan's
      checkpoint-1 gate): 84,510 listings · 11,116 credible (13.15%) ·
      66,853 zero-revenue (79.1%) · 4,610 perfect tens with 4,304 on a single
      vote · C = 6.96 · votes p90 ≈ 104.
- [ ] **Read `[Title · Landing]` on canvas and count the words.** Expected 48 with
      today's winner. If the winner ties and the string runs long, the guard falls
      back to the 33-word frame — check which frame rendered.
- [ ] **Confirm the theme reloads** and that the 46 existing cards no longer render
      a black slab or their measure name. (Those cards are due for replacement in
      later checkpoints; this is the theme-level check, not a page check.)
- [ ] **Font check after the next publish** — Courier New / Arial / Arial Black /
      Georgia only. Any Bahnschrift or Consolas still rendering means a per-visual
      override survived in a page file, not in the theme.

### Known limitations — checkpoint 1

- `project/deliverables/measures.dax` and `data-model.md` still describe the
  pre-rebuild model (90 measures, no bands, no `Counts`/`Parameters`). They are
  design-quartet documents outside this checkpoint's scope and are **now stale**.
- The old report pages still bind `[Title · Lie 1/2/3]` and `[Title · Landing]`
  into act-titled chrome. The measures now say something different from the
  chrome around them. That is expected mid-rebuild and resolves when the pages
  are rebuilt; it is **not** a defect to fix in the old pages.
- No page, visual or bookmark was touched in this checkpoint.

## 2026-08-05 — REBUILD CHECKPOINT 2: `p1-the-answer`, the new landing page

The first page of the rebuild. It **asks the contest question and answers it**:
success is two different things, money and evidence, they almost never coincide,
and most listings cannot be judged on either. Thirteen visuals, exactly the
thirteen the approved checkpoint specifies — the entrant's rule ("a builder does
not put nails where they do not need") was applied as a hard filter: **nothing was
added that is not in the list**, including the "KEY TAKEAWAY" kicker the old p0
carried (see *Open questions*).

### Built — the page

| id | type | function | binds | rect | tab |
|---|---|---|---|---|---|
| `c_question` | textbox | states the question the report answers | — | 24,40,1232,48 | 100 |
| `hero_takeaway` | cardVisual | the mandated Key Takeaway (≤50 words) | `[Title · Landing]` | 24,104,1232,96 | 200 |
| `z_rule_answer` | shape 1 px | separates the claim from its evidence | — | 24,216,1232,1 | **−1** |
| `dn_answer_units` | `hundredPercentStackedBarChart` | of 100 listings, how many can be judged at all | `[Share · both]` · `[Share · one bar only]` · `[Share · neither]` | 24,240,736,304 | 300 |
| `c_units_legend` | textbox | names the three states in words | — | 24,552,736,20 | 400 |
| `c_units_read` | cardVisual | reads the chart in one sentence, live | `[Copy · Answer · units read]` | 24,580,736,48 | 500 |
| `btn_go_money` | actionButton | → `p2-money` | — | 792,240,464,96 | 600 |
| `btn_go_evidence` | actionButton | → `p3-evidence` | — | 792,352,464,96 | 700 |
| `btn_go_both` | actionButton | → `p4-both` | — | 792,464,464,96 | 800 |
| `c_nav_hint` | textbox | the three tests run in order and are selectable | — | 792,572,464,20 | 900 |
| `btn_method` | actionButton | → `p5-method` | — | 792,600,464,28 | 1000 |
| `z_method_stamp` | cardVisual | snapshot · basis · adult exclusion · floor · m · C | `[Label · Method]` | 24,640,1232,24 | 1100 |
| `c_caveats` | cardVisual | standing caveats + the TMDB/Kaggle/ODC-By credit | `[Label · Caveats]` | 24,664,1232,32 | 1200 |

Tab order is the reading order of the table, buttons after the chart;
`z_rule_answer` is the page's only `tabOrder: -1`.

### The formatting grammar — applied, not re-derived

Both Desktop specimens recorded in this log on 2026-08-05 were followed exactly:

- **`shape` / `actionButton`** — the on/off toggle sits in its **own selectorless
  entry**; every property that styles the default part carries
  `"selector": {"id": "default"}`. So `actionButton.fill` is written as **two**
  entries (`{show:true}` selectorless **plus** `{fillColor}` selector'd), which is
  the shape that was missing when every fill fell back to theme red. Same for
  `outline` (`show` + `lineColor`/`weight`) and `text` (`show` + `text`/font/colour/
  alignment).
- **`cardVisual`** — `label` and `value` are instance-scoped, so `show` travels
  *inside* the selector'd entry alongside the styling. All four cards write
  `label {show:false}` and `value {show, fontFamily, fontSize, fontColor,
  horizontalAlignment, textWrap}`, both with `selector: {"id":"default"}`.
- **`textbox`** — `general.paragraphs[].textRuns[]` with raw `value` +
  `textStyle{fontFamily,fontSize,color}`, no `expr` wrapper (Desktop's own form).
- Every visual states `title` / `background` / `border` / `dropShadow` explicitly;
  `drillFilterOtherVisuals: true` on all 13.
- `shape` is the visual name (never `basicShape`); the buttons use the verified
  pair `tileShape: 'rectangleRounded'` + `rectangleRoundedCurve: 8L`.

### Decisions & assumptions — checkpoint 2

- **Button text is STATIC, and that is a verified-shape decision, not a shortcut.**
  A measure-bound (fx) button label has **no verified serialisation**: all 175
  existing `altText`/`text` literals in this report are `Literal` strings,
  `visualConfiguration/2.3.0` delegates `objects` to the untyped
  `formattingObjectDefinitions/1.5.0` bag, and no Desktop-authored button exists in
  the repo. Inventing one would be exactly the silent-drop trap this log already
  paid for twice. **Consequence, honestly stated:** the buttons could not carry a
  live headline number. They carry the destination, its ordinal and its question,
  and where a number belongs it is a **disclosed parameter** (the only literals the
  rebuild allows): `$10,000` on MONEY, `m = 100` on EVIDENCE. BOTH carries no
  number because none of its numbers is disclosed. **To upgrade:** bind the text in
  Desktop by hand, capture the JSON here, then re-author.
- **No volatile count is typed anywhere on the page.** A sweep of every on-canvas
  literal string returns exactly five numbers: the ordinals `1`, `2`, `3` and the
  disclosed `$10,000` and `100`. Everything else — the takeaway, the unit-chart
  read, the method stamp, the caveats — is a measure.
- **`dn_answer_units` is the native fallback; Deneb is still not registered.**
  Re-checked on disk this session, not assumed: `report.json` declares neither
  `publicCustomVisuals` nor `organizationCustomVisuals`, and no custom-visual
  payload exists under `StaticResources`. An agent cannot register an AppSource
  visual. The container therefore ships as a native `hundredPercentStackedBarChart`
  **at the contracted rect, under the contracted id, at the contracted tab
  position** — see *the Deneb swap* below.
- **The three unit states are a pure luminance ramp, deliberately colourless.**
  `Share · both` `#F2EFE6` → `Share · one bar only` `#8A8377` →
  `Share · neither` `#2E2933`. The honest-green/trap-red pair was **rejected here
  on purpose**: these three states describe *the record*, not the films
  (`Movies (neither bar)`'s own docstring says so), and painting them good/bad
  would import the value judgement the report refuses. A luminance ramp is also
  the colour-blind-safe choice, and it lets the words in `c_units_legend` do the
  identifying. Measured, in full:

  | pair | ratio | needs | verdict |
  |---|---|---|---|
  | `#F2EFE6` both vs `#8A8377` one (adjacent) | **3.27:1** | 3.0 | PASS |
  | `#8A8377` one vs `#2E2933` neither (adjacent) | **3.78:1** | 3.0 | PASS |
  | `#F2EFE6` vs canvas `#171418` | 15.89:1 | 3.0 | PASS |
  | `#8A8377` vs canvas | 4.87:1 | 3.0 | PASS |
  | `#2E2933` vs canvas | **1.29:1** | 3.0 | **below** — see the frame below |

  Three fills that are each ≥3:1 against a `#171418` canvas **and** ≥3:1 against
  each other is arithmetically impossible (the darkest would have to exceed
  luminance 1.53). The two **boundaries** — which is what carries the quantity —
  both clear 3:1, and identification is carried three more ways: the printed
  legend in reading order, the live sentence beneath, and the alt text.
- **The chart carries a 1 px `#6E6960` container frame, and it is not decoration.**
  Because the "neither" fill sits at 1.29:1 the bar's right end would otherwise
  fade into the page, and a 100 % bar whose 100 % mark is invisible cannot be felt
  as "of every 100". The frame draws that boundary at **3.35:1** and uses the same
  hairline token as `z_rule_answer`, so the page has one hairline colour.
- **Axes, legend and data labels are all explicitly OFF on the chart.** The value
  axis and legend would restate what `c_units_legend` and `c_units_read` already
  say; in-segment data labels are worse than useless here, because one label colour
  cannot stay legible across a `#F2EFE6` and a `#2E2933` fill. The chart's job is
  proportion; the numbers are the card's job.
- **Radius: a documented 2-step scale.** Controls (the four buttons) are
  `rectangleRounded` at 8 px; surfaces and the 1 px rule are square. Consistency
  lock 8 permits a documented 2-step scale, and rounding a 1 px line is meaningless.
  `pbir_detect`'s `radius-system` rule reads `border.radius` literals only, of which
  the page writes none, so the lock is measured clean either way.
- **`z_method_stamp` ships `textWrap: false`, on measurement.** The stamp's live
  string measures **1228 px** at Arial 10 pt (GDI, 96 DPI) against a 1232 px box —
  4 px of headroom. If a count gains a digit it wraps, and two 13 px lines cannot
  fit a 24 px card, so *both* lines would clip. With wrap off it degrades in the
  right order instead: snapshot, basis, adult exclusion, floor, m and C all render,
  and only the trailing `LISTINGS≠FILMS` clause truncates. The rect is contracted,
  so the alternative (a taller box) needs a designer nod — it is on the checklist.
- **Alt text follows the contracted rule exactly:** the chart gets it, prose cards
  do not (a card bound to a `Copy ·` measure already reads its own value aloud),
  `z_rule_answer` gets `''` and no tab stop, and the buttons are named by their own
  text. One alt string on the page, on `dn_answer_units`, phrased around the
  disclosed constants so it carries **no volatile count**. The model's
  `[Alt · dn_answer_units]` is *not* bound: dynamic alt text has no verified PBIR
  serialisation (the standing finding), so the measure stays ready for a Desktop fx
  binding while the on-disk literal says the same thing without live numbers.
- **Every colour on the page is a hex the theme declares** (`#F2EFE6` `#B5AFA0`
  `#171418` `#1D1A20` `#6E6960` `#8A8377` `#2E2933`). `theme-color-drift`: 0.
- **Fonts are the Mac-safe set only:** Arial Black 28 pt (the question), Georgia
  16/12 pt (the takeaway and the chart read), Arial 12/10 pt (buttons and chrome).
  No Bahnschrift, Consolas or Segoe UI is written anywhere on the page, and both
  theme copies are clean of all three (re-checked this session). Smallest type on
  the page is 10 pt — the floor, never crossed.

### The Deneb swap — exactly what changes when Deneb arrives

Nothing outside one file. `dn_answer_units` keeps its **id**, its **rect**
(24,240,736,304), its **z** (12) and its **tabOrder** (300), so tab order, the page
inventory and every reference to it survive the swap.

1. 🖥️ Install Deneb from AppSource in Desktop and let Desktop write
   `publicCustomVisuals` into `report.json` (an agent cannot register it).
2. In `visuals/dn_answer_units/visual.json` replace `visualType`
   `hundredPercentStackedBarChart` with Deneb's AppSource visual name **as Desktop
   writes it** (do not type it from memory — copy it out of the file Desktop saves).
3. Keep the query as-is: the same three measures in the same order feed the
   10 × 10 unit chart (`Share · both`, `Share · one bar only`, `Share · neither`).
4. Delete the four native cards (`categoryAxis`, `valueAxis`, `legend`, `labels`)
   and the three `dataPoint` metadata-selector fills; the Vega-Lite spec carries
   colour and geometry instead.
5. Keep `visualContainerObjects` **exactly as it stands** — the alt text is still
   required, and the 1 px `#6E6960` frame still bounds the 100 units.
6. Spec constraints from the plan, unchanged: renderer **SVG** (Canvas discards
   ARIA), selection **off**, CSS font stacks terminating in `sans-serif`/`serif`,
   and a `description` encoding on every mark layer so each cell emits an
   `aria-label`. Reuse the same luminance ramp and the fill-vs-outline carrier.
7. Re-run: `validate_json.py`, the deep `visualContainer/2.9.0` pass, `pbir_detect`.

### What dangles, and why that is deliberate

All four `visualLink` targets are written to page ids **that do not exist yet** —
`p2-money`, `p3-evidence`, `p4-both`, `p5-method`. This is the approved sequencing:
the names are fixed by the plan, so writing them now means no rewiring later. Until
those pages are built the four buttons are **inert in Desktop** (a navigation action
pointing at a missing section does nothing). Nothing else on the page depends on
them, and the old pages are unreachable from the new landing page until the
replacements land — which is expected mid-rebuild, not a defect.

### Findings for the coordinator — not build defects

1. **`grid-8px` fires on the new page and is left UNWAIVED.** `pbir_detect` reports
   *5 of 13 visuals off the 8 px grid*: `z_rule_answer` (h 1), `c_units_legend`
   (h 20), `c_units_read` (y 580), `c_nav_hint` (y 572, h 20), `btn_method` (h 28).
   **Every one of those coordinates is contracted in the approved checkpoint**, so
   they were not "corrected" unilaterally. A waiver is the user's to sign, not the
   operator's — the finding is reported here instead of being buried. Fixing it
   instead would cost four numbers (h 20→24, h 28→24 or 32, y 580→584, y 572→576)
   and needs the designer's word.
2. **A theme defect predating this checkpoint, reported not fixed.**
   `visualStyles.actionButton.*.text[0]` writes **`"alignment": "center"`**, but
   `reportThemeSchema-2.156`'s `visual-actionButton → text` card has no `alignment`
   property — the name is **`horizontalAlignment`** (the theme's own `pageNavigator`
   block uses the correct one). It validates only because that item schema does not
   set `additionalProperties: false`, and it is therefore **inert**: theme-level
   button text alignment never applies. p1 is unaffected because all four buttons
   write `horizontalAlignment` explicitly. Not fixed here: `project/deliverables/
   theme.json` is outside this agent's write scope, and the deliverable and the
   installed `D7-Seductive-Lies.json` must stay content-identical — so both copies
   have to change in one pass, by whoever owns the theme.
3. **Checkpoint 1's font cut verified clean.** Neither theme copy contains
   Bahnschrift, Consolas or Segoe UI. No checkpoint-1 miss to report on fonts.

### Manual steps required in Desktop — checkpoint 2

- [ ] **Open the report and land on `p1-the-answer`.** Confirm it opens as the
      landing page and that the six old pages are still present behind it.
- [ ] **Confirm `dn_answer_units` renders three segments.** It is bound with the
      `Y` role only and **no `Category` field** — a bar chart with values and no
      axis renders one bar in Desktop, but this repo has never had a Desktop-
      rendered `hundredPercentStackedBarChart`. *If it renders empty*, the fix is a
      single-row category field, not a re-design. Check the segment order is
      both → one → neither, left to right.
- [ ] **Confirm the four button fills and outlines render** (the regression this
      grammar exists to prevent). A blank or terracotta button means a selector was
      dropped somewhere.
- [ ] **Check `z_method_stamp` on one line.** With `textWrap: false` a too-long
      string truncates its tail; if the `LISTINGS≠FILMS` clause is cut, ask the
      designer for 24 → 40 px height rather than dropping to 9 pt (the 10 pt floor
      is a hard rule).
- [ ] **Count the Key Takeaway's words on canvas** (the plan's gate for this page).
      Expected 48 with today's winner; the guard falls back to a 33-word frame.
- [ ] **Keyboard walk the page:** 12 stops, in the order c_question → hero_takeaway
      → dn_answer_units → c_units_legend → c_units_read → the three buttons →
      c_nav_hint → btn_method → z_method_stamp → c_caveats. `z_rule_answer` must
      **not** take focus. Alt+Shift+F11 on the chart should read the alt string.
- [ ] **Verify `rectangleRounded` + `rectangleRoundedCurve: 8L` actually rounds the
      buttons.** If not, they render square, which is a cosmetic degradation only.

### Validation status — 2026-08-05, checkpoint 2

```
validate_json.py          : PASS - 273 file(s) repo-wide, 0 errors, no BOM
visualContainer/2.9.0     : PASS - 13 new visual.json validated DEEPLY with all
                            5 remote sub-schemas resolved, 0 real errors. Only
                            difference is the known $schema const (our files
                            declare 2.11.0, which is what Desktop writes).
page/2.1.0                : PASS - p1-the-answer/page.json, 0 errors
pagesMetadata/1.1.0       : PASS - pages.json, 0 errors
pbir_detect.py            : FAIL - 49 findings, 1 unwaived / 48 waived. The one
                            unwaived finding is grid-8px on pages/p1-the-answer
                            (contracted rects, see Findings 1). The 48 waived are
                            the pre-existing old-page set, unchanged by this pass.
check_contrast.py         : theme pairs 8/0 failures. Page pairs measured
                            individually (11 pairs, table above and below).
validate_tmdl.py --strict : 17 file(s), 1 error - the STANDING SourceRoot waiver.
                            No model file was touched in this checkpoint.
check_state.py            : OK (stage 6, in_progress)
measure resolution        : all 4 card/chart bindings resolve to defined measures
                            in _Measures.tmdl (Title · Landing, Copy · Answer ·
                            units read, Label · Method, Label · Caveats, plus the
                            three Share · measures on the chart)
git                       : NOT committed, by instruction. git diff is the undo.
```

**Every text/background pair introduced on this page, measured:**

| foreground | background | ratio | threshold | verdict |
|---|---|---|---|---|
| `#F2EFE6` question 28 pt | `#171418` canvas | 15.89:1 | 3.0 (large) | PASS |
| `#F2EFE6` takeaway 16 pt | `#171418` canvas | 15.89:1 | 4.5 | PASS |
| `#F2EFE6` chart read 12 pt | `#171418` canvas | 15.89:1 | 4.5 | PASS |
| `#B5AFA0` legend 10 pt | `#171418` canvas | 8.35:1 | 4.5 | PASS |
| `#B5AFA0` nav hint 10 pt | `#171418` canvas | 8.35:1 | 4.5 | PASS |
| `#B5AFA0` method stamp 10 pt | `#171418` canvas | 8.35:1 | 4.5 | PASS |
| `#B5AFA0` caveats 10 pt | `#171418` canvas | 8.35:1 | 4.5 | PASS |
| `#F2EFE6` button text 12 pt | `#1D1A20` button fill | 14.96:1 | 4.5 | PASS |
| `#B5AFA0` btn_method text 10 pt | `#171418` canvas | 8.35:1 | 4.5 | PASS |
| `#F2EFE6` button outline (non-text) | `#171418` canvas | 15.89:1 | 3.0 | PASS |
| `#B5AFA0` btn_method outline | `#171418` canvas | 8.35:1 | 3.0 | PASS |
| `#6E6960` rule + chart frame | `#171418` canvas | 3.35:1 | 3.0 | PASS |
| `#1D1A20` button fill vs canvas | `#171418` canvas | 1.06:1 | — | informational; the outline is the affordance |

### Open questions — checkpoint 2

- **No "KEY TAKEAWAY" kicker was built.** The old p0 carried `z_hero_kicker` so a
  judge could *find* the mandated element by name; the checkpoint list has 13
  visuals and no kicker, and "build only what is listed" won. If the coordinator
  wants the label back it is one textbox at `24,88,1232,16` and it costs one tab
  stop. **Designer's call, recorded rather than taken.**
- **The unit chart has no verified render.** See the manual checklist; this is the
  first `hundredPercentStackedBarChart` in the entry to matter visually.

## 2026-08-05 — CHECKPOINT 2 RULINGS APPLIED (coordinator)

Three rulings, all closed in one pass. Nothing else on `p1-the-answer` changed.

1. **Grid: snapped, not waived.** `c_units_legend` h 20→24 · `c_nav_hint` y 572→576
   h 20→24 · `c_units_read` y 580→584 · `btn_method` h 28→32. Every edge relation on
   the page survives (the legend still sits 8 px above the read card; the nav hint
   still butts the method button; nothing overlaps), and re-measured text still fits
   every box on one or two lines as before. `z_rule_answer` (h 1) stays: an 8 px
   separator is a slab, not a rule. **`pbir_detect` on the page: 1 finding, waived,
   0 unwaived.**
2. **`c_takeaway_kicker` built.** `KEY TAKEAWAY` at `24,88,1232,16`, Arial 10 pt
   `#B5AFA0` (8.35:1 on canvas), `tabOrder: 150` so a screen reader hears the label
   immediately before the takeaway it labels, `altText: ''` so the alt layer does not
   supersede and re-read the visible words. Page is now **14 visuals, 13 tab stops**.
3. **Theme `alignment` → `horizontalAlignment` fixed in both copies.**
   `visualStyles.actionButton.*.text[0]`. Both files still validate at **0 errors**
   against `reportThemeSchema-2.156`, and are content-identical (the deliverable is
   LF, the installed resource CRLF, exactly as before). The property is now the one
   the schema declares, so a future button that relies on the theme instead of
   stating its own alignment will actually get it.

## 2026-08-05 — REBUILD CHECKPOINT 3: `p4-both`, the payoff page

Night surface, plum act tint as chrome only, 11 visuals. The page states its answer
first and then shows the evidence: the animated scatter carries both bars at once,
and the right-hand column discloses what was adjusted, what was refused, and what was
left out — the entry's Responsible Data Use evidence, on the page where the payoff is.

### Built — the page

| id | type | function | binds | rect | tab |
|---|---|---|---|---|---|
| `nav_pages` | **pageNavigator** | navigation across all pages, current marked | — | 24,24,720,32 | 100 |
| `c_p4_answer` | cardVisual | the answer, before its evidence | `[Title · Lie 3]` | 24,72,1232,40 | 200 |
| `z_p4_rule` | shape 2 px plum | answer / evidence separator | — | 24,120,1232,2 | **−1** |
| `c_scatter_population` | cardVisual | who is in the plot, stated before the plot | `[Label · Population]` | 24,136,896,24 | 300 |
| `hero_premiere_scatter` | **scatterChart + Play** | both bars at once, animated over release year | X `Sum(Movies[Revenue])` log · Y `[Rating (evidence-weighted)]` · Details `Movies[Title]` · **Play `'Release Year'[Year Label]`** · `y1AxisReferenceLine` 6.96 | 24,160,896,456 | 400 |
| `c_winner_label` | cardVisual | names the film leading on both | `[Copy · Act III · winner label]` | 944,136,312,80 | 500 |
| `c_adjustments` | cardVisual | every applied parameter, in one place | `[Label · Adjustments]` | 944,224,312,96 | 600 |
| `c_refusal` | cardVisual | the refused adjustment and why | `[Label · Refusal]` | 944,336,312,80 | 700 |
| `tbl_refusal_ranks` | **tableEx** | the evidence for the refusal | `Movies[Title]` · `[Mark · Rank divergence]` · `[Rank · Popularity]` · `[Rank · Rating (weighted)]` · `[Rank · Revenue]` | 944,424,312,104 | 800 |
| `c_nodate` | cardVisual | the excluded unknown, counted where it is excluded | `[Label · No date]` | 944,536,312,80 | 900 |
| `c_verdict_both` | cardVisual | the closing finding: correlation shown, causation refused | `[Copy · Act III · verdict]` | 24,632,1232,56 | 1000 |

### THE PLAY AXIS — wired, and here is the evidence

**It did not need to be guessed and it was not left unwired.** The p3 hero already
carries a `Play` role, and that file is one of the **nine visuals Desktop
re-serialised** on 2026-08-05 (it is written `height` before `width` — Desktop's
canonical key order, the same signature that proved which files passed through
Desktop's formatting model). Desktop kept the role, kept its projection, and
**generated its own matching field filter** for `Release Year.Year Label` alongside
the ones for Title, Revenue and the rating measure — which is what Desktop does for a
populated field well. That is round-trip evidence, not inference:

```
"Play": { "projections": [ { "field": { "Column": {
    "Expression": { "SourceRef": { "Entity": "Release Year" } },
    "Property": "Year Label" } },
  "queryRef": "Release Year.Year Label", "nativeQueryRef": "Year Label" } ] }
```

So p4's hero is the p3 file **copied verbatim** with four deliberate changes: the
rect (24,160,896,456), the fonts (`Segoe UI` → **Arial** ×4 — the Mac-safe rule
applies to axis labels too, which is where checkpoint 1 had already caught the same
thing in the theme), the x-axis title (`Revenue (USD, log) — credible set` →
`Revenue (USD, log scale) · credible set`, dropping an em-dash from on-canvas text),
and the alt string, which now describes the animation instead of calling the plot
static. The log axis, the dashed `C = 6.96` reference line with its `{"id":"refC"}`
selector, `dataPoint.defaultColor` `#B5AFA0`, the canvas tooltip binding to
`tt-movie-poster` and the population floor filter (renamed `flt_p4_scatter_floor`)
all come across unchanged — every one of them already survived Desktop.

**The one thing that could NOT be settled from disk: which frame the play axis rests
on when the page opens.** Power BI starts a play axis at its first frame, which here
is the earliest release year holding at least one qualifying listing — a nearly empty
plot, which is exactly the "a judge who does not click sees an empty page" defect the
rebuild exists to remove. The published theme schema does expose
`scatterChart.currentFrameIndex.index`, which is almost certainly the lever, but the
frame count is unknowable before a refresh and no Desktop specimen sets it, so
**nothing was guessed**. It is the first item on the Desktop checklist, with two
recorded fixes: set the slider in Desktop, save, and capture whatever
`currentFrameIndex` Desktop writes; or sort the Play field descending so frame 0 is
the most recent year.

### `pageNavigator` — verified before writing, cleanly

Every property was checked against `reportThemeSchema-2.156` this session, not
recalled:

| written | verdict |
|---|---|
| `visualType: "pageNavigator"` | valid visual name (`visualStyles.pageNavigator`) |
| `pages.showHiddenPages` / `showTooltipPages` = false | both declared booleans — the hidden tooltip page can never appear |
| `layout.orientation = 2L` | the schema titles the enum: **2 = Horizontal**, 1 = Vertical, 0 = Grid. Checkpoint 1's assertion confirmed |
| `layout.cellPadding = 8L` | declared integer |
| `shape.tileShape 'rectangleRounded'` + `rectangleRoundedCurve 8L` | `shape` declares **no `$id`** → written selectorless, matching the theme |
| `fill [{show:false}]` | `fill` declares `$id`, but "off" is Desktop's selectorless form |
| `outline` = `[{show:true}]` + `$id` default / hover / selected | `$id` declared → selector required |
| `text` = `[{show:true}]` + `$id` default / hover / selected | `$id` declared; **no `text` property** on the card — page names come from the pages, so nothing to type |

**The current page is marked by outline weight 1 → 2 *and* a bolder, brighter label**
— never colour alone (hard rule 3). Colours are written explicitly on the visual
rather than left to the theme, and the default outline is `#6E6960` (3.35:1) rather
than the theme's `#57534E` (2.39:1), because a control boundary is a non-text carrier
and 2.39:1 does not clear 3:1. **Recommendation for the theme owner:** move the
theme's `pageNavigator.outline` default to `#6E6960` so the two agree; not done here,
because that is a design change beyond the one-key fix that was authorised.

### Decisions & assumptions — checkpoint 3

- **Five rects were snapped to the 8 px grid**, applying the coordinator's own
  checkpoint-2 ruling to this page's table: `c_scatter_population` h 22→**24** ·
  `hero_premiere_scatter` y 162→**160** h 454→**456** · `c_winner_label` h 76→**80** ·
  `c_refusal` h 76→**80** · `tbl_refusal_ranks` y 420→**424** h 100→**104**. **Every
  alignment in the spec is preserved**: the scatter still ends at y 616 exactly where
  it did, the right-hand column still ends level with it at 616, every gap in that
  column is still 8 px, and no rect moved by more than 4 px. Flagged prominently
  because it is a deviation from a literal rect table — revert in five numbers if the
  coordinator prefers the original and would rather waive.
- **`tbl_refusal_ranks` ships with column headers ON.** The p3 original hid them by
  painting the header text the same colour as its background (`tableEx` has no
  `columnHeaders.show`); the rebuild plan asks for real headers because they give a
  screen-reader user genuine column semantics. `wordWrap: true` lets
  `Rank · Rating (weighted)` wrap inside a 58 px column; measured, the header block
  and three filtered rows fit the 104 px box. Headers are `#B5AFA0` on `#171418`
  (8.35:1); values `#F2EFE6` (15.89:1).
- **The table's font moved Consolas → Arial** (values and headers). Consolas is one of
  the two faces the rebuild deleted; the p3 original still carries it, and that page
  is being replaced anyway.
- **Trap red survives on exactly one column**, `[Mark · Rank divergence]` (`#E8705F`,
  6.01:1), and the measure prints the divergence **in words** in the same cell, so
  colour is never the only carrier. The plum act tint appears **only** on
  `z_p4_rule` — no data mark on this page carries it, which is the standing
  scope rule.
- **Chart containers unified (consistency lock 9).** Both night data visuals now use
  one treatment: fill `#1D1A20`, 1 px `#6E6960` hairline. p1's unit chart gained the
  fill; p4's scatter border moved off `#2E2933` (1.29:1, effectively invisible). Under
  the fill the unit ramp measures `#F2EFE6` 14.96:1 · `#8A8377` 4.58:1 · `#2E2933`
  1.22:1, and the two **adjacent** boundaries that carry the quantity are unchanged at
  3.27:1 and 3.78:1.
- **Card type sizes were measured, not guessed** (GDI at 96 DPI, the live strings with
  today's winner title): `c_p4_answer` Georgia 14 pt = 1021 px in a 1232 px box, one
  line with ~200 px of headroom for a longer winner (16 pt fits today but leaves only
  115 px, and a wrap would clip in a 40 px card) · `c_verdict_both` Georgia 14 pt =
  two lines, 48 px in 56 · `c_winner_label` Georgia 12 pt = three lines, 61 px in 80 ·
  `c_refusal` Arial 10 pt = three lines, 51 px in 80 (11 pt needs four lines, 75 px in
  80 — too tight to trust) · `c_nodate` Arial 10 pt = three lines · `c_adjustments`
  Arial 10 pt = two lines · `c_scatter_population` Arial 10 pt = one line.
- **Alt text: the scatter and the table only.** Both literal, both phrased around the
  disclosed constants ($10,000 · 100 votes · C = 6.96) so **no volatile count is
  typed**; both state the finding rather than describing the screen. Prose cards carry
  none (they read their own measure aloud), `z_p4_rule` carries `''` and no tab stop,
  and `nav_pages` is named by its own page buttons.
- **Nothing numeric is typed on this page at all.** Unlike p1 — which legitimately
  prints `$10,000` and `m = 100` in button text — every number on p4 arrives through a
  measure, including the disclosed parameters (`[Label · Adjustments]`).

### Findings for the coordinator — checkpoint 3

1. **`nav_pages` will show six buttons until the old pages are deleted.** It renders
   one button per visible page: today that is `THE ANSWER`, `3 · BOTH` and the four
   surviving old pages, in `pageOrder`. At 720 px with 8 px cell padding they will be
   cramped, and the old names will look wrong beside the new ones. This is expected
   mid-rebuild and self-corrects at the deletion checkpoint; it is **not** a reason to
   narrow the navigator now.
2. **The scatter's opening frame** — see the play-axis note above. This is the one
   genuine Desktop dependency introduced by this checkpoint.
3. **`tbl_refusal_ranks` is the tightest object in the entry**: five columns and real
   headers in 312 px. It was measured to fit, but it is the first thing to check in
   Desktop after the play axis.

### Validation status — 2026-08-05, checkpoint 3 (and the ckpt-2 rulings)

```
validate_json.py          : PASS - 286 file(s) repo-wide, 0 errors, no BOM
visualContainer/2.9.0     : PASS - p1 14/14 and p4 11/11 validated DEEPLY with all
                            5 remote sub-schemas resolved, 0 real errors (only the
                            known $schema const difference: our files declare
                            2.11.0, which is what Desktop writes)
page/2.1.0                : PASS - p4-both/page.json 0 errors
pagesMetadata/1.1.0       : PASS - pages.json 0 errors
pbir_detect.py            : PASS - 247 visuals, 50 findings, 0 UNWAIVED, 50 waived.
                            The two new pages contribute exactly one finding each
                            (their 1 px / 2 px separator), both waived as hairlines.
                            No ai-dash-emoji, no theme-color-drift, no
                            text-fill-contrast, no accent-lock, no radius finding
                            from either rebuild page.
theme vs 2.156            : PASS - both copies 0 errors after the alignment fix
check_contrast.py         : theme pairs 8/0. p4 pairs measured individually below.
validate_tmdl.py --strict : 17 file(s), 1 error - the STANDING SourceRoot waiver.
                            No model file was touched in this checkpoint.
check_state.py            : OK (stage 6, in_progress)
binding resolution        : every measure and column bound on p4 resolves against
                            _Measures.tmdl / Movies / Release Year. 0 unresolved.
git                       : NOT committed, by instruction. git diff is the undo.
```

**Every pair introduced on `p4-both`, measured:**

| foreground | background | ratio | threshold | verdict |
|---|---|---|---|---|
| `#F2EFE6` answer 14 pt / winner 12 pt / refusal 10 pt / verdict 14 pt | `#171418` | 15.89:1 | 4.5 | PASS |
| `#B5AFA0` population / adjustments / no-date 10 pt | `#171418` | 8.35:1 | 4.5 | PASS |
| `#B5AFA0` navigator label (default state) | `#171418` | 8.35:1 | 4.5 | PASS |
| `#F2EFE6` navigator label (hover / selected, bold) | `#171418` | 15.89:1 | 4.5 | PASS |
| `#6E6960` navigator outline, default (non-text) | `#171418` | 3.35:1 | 3.0 | PASS |
| `#F2EFE6` navigator outline, hover / selected 2 px | `#171418` | 15.89:1 | 3.0 | PASS |
| `#B79BE8` plum separator (non-text chrome) | `#171418` | 7.71:1 | 3.0 | PASS |
| `#F2EFE6` table values 10 pt | `#171418` | 15.89:1 | 4.5 | PASS |
| `#B5AFA0` table headers 10 pt | `#171418` | 8.35:1 | 4.5 | PASS |
| `#E8705F` divergence column 10 pt | `#171418` | 6.01:1 | 4.5 | PASS |
| `#B5AFA0` scatter axis labels + titles 10 pt | `#1D1A20` card | 7.87:1 | 4.5 | PASS |
| `#8A8377` scatter `C = 6.96` reference line | `#1D1A20` card | 4.58:1 | 3.0 | PASS |
| `#B5AFA0` scatter points (non-text) | `#1D1A20` card | 7.87:1 | 3.0 | PASS |
| `#6E6960` chart hairline | `#171418` | 3.35:1 | 3.0 | PASS |
| `#57534E` table row gridlines | `#171418` | 2.39:1 | — | **below 3:1, accepted**: a row separator carries no meaning here (row order and real column headers do), and it is the theme's own `tableEx` gridline token |
| `#1D1A20` card fill | `#171418` | 1.06:1 | — | informational; the hairline is the boundary |

### Manual steps required in Desktop — checkpoint 3

- [ ] **Press play on `hero_premiere_scatter`.** Confirm the play control appears and
      the frames step through release years. Then decide the resting frame (see the
      play-axis note) and capture whatever Desktop writes.
- [ ] **Check `nav_pages` renders** as a horizontal row of page buttons, that the
      current page is outlined 2 px with a bold label, and that the tooltip page does
      **not** appear in it.
- [ ] **Check `tbl_refusal_ranks`** — five columns, real headers, three rows, nothing
      truncated to uselessness inside 312 px.
- [ ] **Keyboard walk p4:** 10 stops, nav_pages first, `z_p4_rule` never focused;
      Alt+Shift+F11 on the scatter and on the table.
- [ ] **Confirm the plum rule renders** (it is the one act-tint object on the page).
