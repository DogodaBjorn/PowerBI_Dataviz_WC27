# 06 — Report build (stage 6)

Detail lives in `project/deliverables/BUILD_LOG.md` (the `build-log` skill's file):
what exists, every decision and assumption, every manual-Desktop step, and the
validation record. This file is the stage's state + open questions.

## Progress

| Phase | Scope | Status |
|---|---|---|
| A | Display measures filled + 40 new measures; D7 theme installed and made active | done 2026-08-05 |
| B1 | `p0-box-office` (42 visuals) · `p9-end-credits` (35 visuals) · pages registry | done 2026-08-05 |
| B2a | `p1-act-i-profit` · `p2-act-ii-ratings` | done 2026-08-05 |
| B2b | Act II ruling · `p3-act-iii-corrected-cut` · `tt-movie-poster` · 9 bookmarks | done 2026-08-05 |
| **B2c** | **The alt-text layer — 10 measures + alt text on all 210 visuals** | **done 2026-08-05** |
| **G6-fix** | **QA fix pass: 3 blockers + 12 majors from the 24/40 review** | **done 2026-08-05** |
| **G6-a11y** | **Accessibility fix pass: the 10 findings of the a11y audit** | **done 2026-08-05** |
| C | Desktop round-trip: refresh, render, work the manual checklist | not started |

**The report is structurally complete.** 222 visuals across six pages
(p0 43 · p1 47 · p2 41 · p3 40 · p9 37 · tooltip 14) plus nine beat bookmarks —
**5 visible pages + 1 tooltip page**, against a contest maximum of 5. The two
contest-starter pages ("Read Me", "Tabular") were deleted in the fix pass.
Model: **90 measures**, including the ten `06 Display\Alt text` narrations.
Alt-text coverage: 89 content · 86 empty-decorative · 47 textboxes reading their own
copy. **The waiting list is closed**, and after the a11y pass **no alt string defers
the reader to something on screen** (was 11).

All 222 `visual.json`, all six `page.json`, `pages.json`, `report.json`, the nine
`*.bookmark.json` and `bookmarks.json` validate against their published schemas
(`visualContainer/2.9.0` with remote sub-schemas resolved, `page/2.1.0`,
`pagesMetadata/1.1.0`, `report/3.3.0`, `bookmark/2.1.0`, `bookmarksMetadata/1.0.0`).
Binding cross-check: 53 bound properties, all resolve.

## Validation record — the full sweep (2026-08-05, after the waiver/handoff pass)

**Correction.** This file previously recorded only `validate_json` and
`validate_tmdl`, and an earlier note claimed "all validators clean". That was wrong:
the `validate-project` sweep has eight steps and step 7, `pbir_detect.py`, is
**gate-blocking at G6/G7** and had never been run. It failed with 63 unwaived
findings. The complete set, run in the sweep's own order:

| # | Validator | Result | Note |
|---|---|---|---|
| 1 | `check_state.py` | **PASS** | `state OK: project 'wc-round-3' at stage 6 (s6_report_build, in_progress), updated 2026-08-05` |
| 2 | `validate_json.py` | **PASS** | `260 file(s) checked, 0 with errors` |
| 3 | `check_contrast.py` | **PASS** | `6 pair(s), 0 failure(s)` — accent 3.21:1 canvas/surface, good 9.02:1, bad 6.01:1 |
| 4 | `validate_tmdl.py --strict` | **1 ERROR (expected)** | `15 file(s), 1 error(s), 0 warning(s) [strict]` — `expressions.tmdl:34`, the committed `SourceRoot` drive-letter value. This is the standing entrant waiver recorded at G4; it is the *only* strict error and no warnings remain |
| 5 | `tmdl_inventory.py` | **PASS** | 10 tables, **90 measures**, 8 relationships, 1 shared expression — matches the blueprint plus the ten `06 Display\Alt text` narrations added at B2c |
| 6 | Naming grep | **PASS** | all 222 visual folders carry a `design/naming-conventions.md` role prefix; no Desktop-style 32-hex ids anywhere in the report tree |
| 7 | `pbir_detect.py` | **PASS *only if the entrant signs*** | `48 finding(s) across 1 report(s) — 0 unwaived, 48 waived -> PASS`. Was 63/63 unwaived → FAIL. See below |
| 8 | `pbir validate` (CLI) | **not run** | the `pbir` CLI is not installed on this machine (`pbir: command not found`); the documented fallback, direct JSON editing plus schema validation, is what this build used throughout |

### How `pbir_detect` went 63 → 48, and why 48 is not zero

Every one of the 63 findings was inspected individually. **15 were fixed, 48 are
argued in a DRAFT waiver file.**

- **`ai-dash-emoji` 46 → 42.** The 46 hits were read one by one against their own
  page's copy register. **Four were genuine AI writing tells** — a spaced em-dash
  used as a rhetorical pivot between two independent clauses, in lowercase prose,
  each with a dashless sibling string in the same register on the same page. Those
  four were **rewritten, not waived**: `z_ticket3_tease`, `c_p2_note_twenty`,
  `c_lb_more`, `c_tt_foot` (details in BUILD_LOG → *G6 waiver + handoff pass*). The
  remaining 42 are contracted typography — screenplay slug lines, `SC.n —` beat
  labels, `INSERT —` shot headings, act/section titles, glossary term–definition
  rows, TMDB's mandated attribution wording, and the `✓` glyphs that
  design-hard-rule 3 **requires** as the non-colour carriers. Rewriting those would
  break the design contract and remove an accessibility carrier.
- **`theme-color-drift` 11 → 0.** All 11 were **promoted, not waived**. The six
  distinct chrome hexes are now named style presets in `theme.json`
  (`ticketPerforation` `#9A9284`, `parameterChip` `#6E6960`, `spotlightSurface`
  `#282331`, `posterPlate` `#C8C3B4`, `leaderboardRule` `#EBE7DC`,
  `evidenceReference` `#8A8377`), re-validated at **0 errors** against
  `reportThemeSchema-2.156.json`. A named preset only applies when a visual selects
  it, so nothing renders differently — deliberate, this close to delivery.
- **`grid-8px` 6 → 6, waived per page.** The layout was measured from the approved
  HTML prototype, whose type sits on a ~19 px line rhythm. Measured over all 222
  visuals / 888 coordinates: 38 % on the 8 px grid, 55 % on 4 px, 78 % on 2 px; 19 px
  is the most common rect height after the 32 px button. The handoff *contracts*
  those off-grid rects, so the build matches its contract — the handoff sentence
  claiming "8 px grid throughout" was the error and has been corrected. Re-aligning
  ~200 visuals two days before the deadline is the wrong trade.

**The waiver file is a DRAFT.** `project/project-state/pbir-detect-waivers.yaml`
carries 19 entries (13 `ai-dash-emoji` covering 42 findings, 6 `grid-8px`, one per
page). Each glob was checked to match exactly its intended findings and nothing more.
**A gate may be waived only by the user**: until the entrant signs these entries,
**G6 stays HELD** even though the detector now prints PASS with the file in place.

## G6 fix pass (2026-08-05) — what changed

Fourteen of the fifteen findings are closed on disk; one (FIX-C) is closed **and**
proved a schema question the build had left open. Full record in BUILD_LOG →
*Stage 6 G6 fix pass*.

- **The report-level Adult filter is expressible in PBIR, and is now written.**
  `report/3.3.0` declares `filterConfig` → `filterConfiguration/1.3.0`; the
  `Advanced`/`Comparison` shape was taken from a filter this report already carries,
  and the boolean literal spelling from the schema's own documentation. Validated
  against the live schema with remote `$ref`s resolved, plus a negative control that
  proved the validator reaches inside the filter subtree.
- **The mandated dataset attribution now names TMDB, Kaggle and ODC-By 1.0**, in one
  identical string on p0 and p9 — written *before* the template pages were deleted,
  so the credit was never absent from the entry.
- The three act headers are measure-bound; the Key Takeaway has a kicker; both tables'
  headers are silenced; the p3 beat rail is on the p1/p2 grid; the ticket perforation
  is one frame plus one hairline; the p9 negative-revenue row exists and is bound.
- Two extra defects were found and fixed during the pass: a stale Act II docstring on
  `Movies (perfect ten)`, and `c_cr_count_dup_val` sitting one row below its label.

## G6 accessibility pass (2026-08-05) — what changed

All ten audit findings are closed on disk except the one that is a documented PBIR
limit (the scatter winner colour), which is now closed *as an answer* rather than as a
gap. Full record in BUILD_LOG → *Stage 6 G6 a11y pass*.

- **The alt layer now speaks.** 29 strings rewritten; the deferral scan that found 11
  offenders returns 0. p9's 12 value cards and the tooltip's 7 fold their label into
  their own alt, so every stop is a self-contained sentence. Nothing volatile is typed —
  the disclosed constants carry the meaning.
- **The alt layer is also honest again.** Three strings described a Play axis and an
  in-chart tick that do not exist on disk; they now describe what ships, on canvas
  (`Label · No date`) as well as in the narration.
- **A measured AA failure is fixed with recomputed numbers**: the p3 scrim at 80D and a
  lighter reference line take the axis text from 4.21 to **5.75:1** and the C line from
  2.12 to **3.56:1**.
- **Beat state is announced** (WCAG 4.1.2) via 9 new current-variant buttons and 9
  rewired bookmarks — required because `bookmark/2.1.0` cannot merge
  `visualContainerObjects`, so alt text is not bookmark-switchable.
- **`dataCategory: ImageUrl` moved from "unverifiable" to written**, on two Microsoft
  sources.
- `measures.dax` had drifted in **12** measures, not the 2 reported; all were refreshed
  from the model and the file now names the model as authoritative.

## Decisions recorded this stage

- **The Act II ruling (2026-08-05, coordinator, design authority).** Act II no longer
  names a film. The naive read is the aggregate — *n* listings score a perfect 10.0,
  *n* of them on a single vote — and the corrected read is the aggregate too: a
  perfect 10.0 on one vote weights to ≈ 6.99, barely above C = 6.96. Five measures
  added, two rewritten in place, three Act II strings re-worded. Full record and the
  one deviation (the leaderboard tie-break) in BUILD_LOG → *THE ACT II RULING*.
- **The play axis is a manual Desktop step, not a silent drop** (see open question 1).
- **Measure-driven colours are not bound** — the fx-field-value serialisation is
  unverifiable; the honest carriers are words and glyphs (see open question 2).
- **Both Deneb visuals ship as their contracted native fallbacks** — Deneb is not
  registered in this report and an agent cannot register it.

## Open questions

1. **The play axis is not on disk — the contracted Act III animation is one Desktop
   drag away.** No published source (theme schema, visualConfiguration,
   Microsoft Learn, this repo's own Desktop-authored files, the contest `.pbix`)
   names the scatter's play-axis role key, so per research-first none was invented.
   `hero_premiere_scatter` ships complete except the Play well. **Entrant action:**
   drag `'Release Year'[Year Label]` into Play, leave the head on the latest year,
   save, and record the role key in BUILD_LOG.
2. **`[Color · Scatter mark]` and `[Color · Rating verdict]` are unbound — and for the
   scatter this is now an ANSWERED question, not an open one.** Microsoft's own
   colour-strategy reference states that scatter silently ignores `dataPoint.fill`
   `metadata` selectors and that per-point colour needs `scopeId` selectors, whose
   payload is undocumented and which would have to encode a data-point identity that
   does not exist until the model is refreshed. The winner is carried by
   `c_winner_label`'s `✓` and its words, and the scatter's alt text now says plainly
   that the plot does not colour the winner. Two `fx → Field value` bindings in Desktop
   still close it if the entrant wants the colour.
3. **Alt text is built; the attribution debt is OPEN.** The blocker was cleared at the
   main-thread level (commit `f4b9420`) by crediting the influencing Fabric Community
   post *by publication* in `CREDITS.md` and `contracts/source-register.yaml`, with
   the byline recorded as an outstanding debt. **A human must still retrieve the
   author's name.** Scope adopted: *dynamic alt text* only — the post's DAX
   user-defined-function pattern is NOT used, and must not be until the name is
   recorded. Implementation is plain measures on Power BI's own documented feature
   (a11y practice credited to Meagan Longoria). All four M-003 carriers are now live
   at SC.1.
   **Remaining sub-item:** the alt strings on disk are **static**, because the
   *value* of `general.altText` is typed as an open object and a measure binding there
   would fail silently. They state the finding with the disclosed parameters and never
   type a volatile count. Upgrading the ten data visuals to their `Alt · …` measures
   via `fx → Field value` is one Desktop step each.
4. **Six new unverified tokens** (scatter role keys · `visualLink.type = 'Bookmark'` ·
   `explorationState.version` · the bookmark `objects.merge` payload · the `image`
   visual's role key and `sourceField` · `VisualTopN` behaviour) join the five from
   phase B1. Each fails visibly and each is a one-line fix; all are on the Desktop
   checklist.
5. ~~**Native table headers cannot be hidden**~~ — **closed in the G6 fix pass.**
   `tableEx` still has no `columnHeaders.show`, so both tables now set the header
   `fontColor` equal to the header `backColor` (`#FFFFFF` on p2, `#1D1A20` on p3):
   the row keeps its semantics for assistive technology and prints nothing. The
   **no per-column font** limit stands, and both may still need a `columnWidth` tune
   in Desktop.
6. **`Two-vote ten (illustration)` and `Godfather rating (reference)` are now unused**
   by any visual after the Act II ruling. Retained, not deleted.
7. **Nothing built at stage 6 has been rendered.** No measure has been executed and no
   pixel seen; BUILD_LOG's Desktop checklists are the gate for that, and s7 still owns
   the 85,394 / 84,036 / 84,510 snapshot reconciliation.
8. **The report-level filter has never been seen attached.** It is schema-correct and
   modelled on a filter this report already carries, but the End Credits cross-foot is
   the trust anchor of the entry and it now depends on that filter actually binding in
   Desktop. **First check after refresh:** the Filters pane shows a locked *Adult is
   False* card, and `[Adult listings excluded]` prints a non-zero number.
9. **The p3 act header must wrap to render fully.** `[Title · Lie 3]` measures ~963 px
   against an 830 px box (the band `btn_home` leaves), so the card wraps to two lines
   in 44 px. If Desktop clips instead of wrapping, raise the box to y 32 / h 48 —
   never drop the type below the 10 pt floor.
10. **The `pbir_detect` waivers are UNSIGNED — this is what holds G6.** 19 DRAFT
    entries in `project/project-state/pbir-detect-waivers.yaml`. A gate may be waived
    only by the user. **Entrant action:** read the 13 `ai-dash-emoji` and 6 `grid-8px`
    entries, approve or strike any of them (striking one brings its findings back),
    and record the decision in `status.yaml`'s s6 `gate_note`. `status.yaml` was
    deliberately **not** touched by the build.
11. **The copy deck and the disk still disagree in seven places the fix passes changed
    and never wrote back.** Four were amended in this pass because they were the
    strings being edited; the rest are listed here rather than silently rewritten,
    because each is a factual claim only the entrant can rule on:
    `z_ticket2_tease` (deck "In which 2 votes crown a champion" / disk "1 vote") ·
    `c_p2_note_twovotes` (deck "NOTE: 2 votes." / disk "one vote is enough to score a
    perfect 10.0.") · glossary `M-005 RAW RATING` (deck "any votes, even 2" / disk
    "even 1") · `c_p1_note_budget` (deck "min $1, median $2,800" / disk "token
    amounts, not blanks") · `c_p1_note_negrev` (deck "one listing books −$12 revenue"
    / disk "revenue goes negative in this basis") · `c_waffle_cap` (deck carries the
    counts "(13)"/"(87)", disk does not) · both TMDB attribution strings (deck carries
    the short form, disk the long ODC-BY form written in the G6 fix pass — the disk
    version is the better one). **Entrant action:** confirm the 1-vs-2-votes fact, then
    reconcile the deck to disk in one pass.
12. **`z_refusal_card_lit` and `z_adjustments_card_lit` disagree on disk.** The handoff
    contracts `#282331` for both spotlight variants; `z_adjustments_card_lit` uses it,
    `z_refusal_card_lit` uses `#2E2933`. One of the two is wrong and it is a design
    call, not a build call — left as found, flagged here. `#282331` is now a theme
    token (`shape.spotlightSurface`), so aligning the refusal card is a one-value edit
    if the entrant wants the pair consistent.

13. ~~**The shape-fill fallback is fixed; the `cardVisual` half of the same bug is
    NOT.**~~ **RESOLVED 2026-08-05** — the entrant authored the reference card and
    handed it back, and the correction was mechanical exactly as predicted. Full
    evidence in BUILD_LOG under "G6 CORRECTNESS FIX: the cardVisual label/value
    fallback", which also records the specimen verbatim. Answer to the three
    questions the card was asked to settle: `label` hides via
    `{"properties":{"show":false},"selector":{"id":"default"}}`; `value.fontColor`
    is correct as written; and **yes, `value` needs the selector** — that missing
    selector was the whole bug. All 46 cards fixed (p0 3, p1 11, p2 5, p3 8, p9 12,
    tooltip 7); diff purely additive, 276 insertions / 0 deletions. Independently
    corroborated by the published report theme schema 2.156, which declares a `$id`
    property on `cardVisual.label` and `cardVisual.value` (= instance-scoped =
    selector required). The specimen also revealed that a card's background fill
    belongs in `cardCalloutArea.backgroundFillColor`, **not** in
    `visualContainerObjects.background` — no change was needed here, because the
    design contract specifies "background off" on every card (the `#FFFFFF` /
    `#1D1A20` surfaces are drawn by separate `basicShape` rects) and all 46 already
    carry `background.show = false` with no colour.
14. **Property shapes still unverified — the list shortened on 2026-08-05.** All
    222 visuals were swept against the published report theme schema 2.156 during
    the cardVisual pass: **every property name we have written anywhere in this
    report exists in that schema** (the single flag, `textbox.general.paragraphs`
    69x, is a false positive — it is PBIR content, not a theme-styleable property,
    and is byte-for-byte identical to Desktop's own authored textbox). So nothing
    is *invented*; what stays unproven is whether an object binds in the position
    we wrote it, which only Desktop shows. Two remain genuinely unverified:
    `hundredPercentStackedBarChart` (`dn_ticket_waffle` — no Desktop-authored
    example of this type exists anywhere in reach) and the **measure-bound**
    `image` form on `img_tt_poster` (Desktop's three authored images all use the
    static-resource `sourceFile.image.{name,url,scaling}` shape instead). The
    schema sweep also *confirmed* the previous pass's inference on
    `actionButton`: `fill`, `outline` and `text` all declare `$id`, so the
    selector'd form applied there was right. Each fails visibly rather than
    corruptly, and each is one line to fix once seen.
15. **`z_ticket1/2/3_stub_rule` are styled but disabled.** Each carries
    `outline.show = false` together with a `lineColor` and `weight`, so the ticket
    perforation draws nothing. The structural correction was applied; the `false`
    was deliberately preserved because changing it is a design call. **Entrant
    action:** if the perforation is meant to be visible, flip those three to `true`.
