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
| C | Desktop round-trip: refresh, render, work the manual checklist | not started |

**The report is structurally complete.** 213 visuals across six pages
(p0 43 · p1 44 · p2 38 · p3 37 · p9 37 · tooltip 14) plus nine beat bookmarks —
**5 visible pages + 1 tooltip page**, against a contest maximum of 5. The two
contest-starter pages ("Read Me", "Tabular") were deleted in the fix pass.
Model: **90 measures**, including the ten `06 Display\Alt text` narrations.
Alt-text coverage: 76 content · 73 empty-decorative · 61 textboxes reading their own
copy. **The waiting list is closed.**

`validate_json.py`: 251 files, 0 errors. `validate_tmdl.py --strict`: 1 error, the
standing `SourceRoot` waiver. All 213 `visual.json`, all six `page.json`,
`pages.json`, `report.json`, the nine `*.bookmark.json` and `bookmarks.json` validate
against their published schemas (`visualContainer/2.9.0` with remote sub-schemas
resolved, `page/2.1.0`, `pagesMetadata/1.1.0`, `report/3.3.0`, `bookmark/2.1.0`,
`bookmarksMetadata/1.0.0`). Binding cross-check: 53 bound properties, all resolve.

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
2. **`[Color · Scatter mark]` and `[Color · Rating verdict]` are unbound.** The winner
   dot is therefore neutral, not good-green; it is carried by `c_winner_label`'s `✓`
   and its words. Two `fx → Field value` bindings in Desktop close this.
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
