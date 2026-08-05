# 06 — Report build (stage 6)

Detail lives in `project/deliverables/BUILD_LOG.md` (the `build-log` skill's file):
what exists, every decision and assumption, every manual-Desktop step, and the
validation record. This file is the stage's state + open questions.

## Progress

| Phase | Scope | Status |
|---|---|---|
| A | Display measures filled + 40 new measures; D7 theme installed and made active | done 2026-08-05 |
| B1 | `p0-box-office` (42 visuals) · `p9-end-credits` (35 visuals) · pages registry | done 2026-08-05 |
| **B2a** | **`p1-act-i-profit` (43 visuals) · `p2-act-ii-ratings` (37 visuals)** | **done 2026-08-05** |
| B2b | `p3-act-iii-corrected-cut` · `tt-movie-poster` tooltip · the nine beat bookmarks | not started |
| C | Desktop round-trip: refresh, render, work the manual checklist | not started |

157 visuals built across four pages. `validate_json.py`: 202 files, 0 errors.
`validate_tmdl.py --strict`: 1 error, the standing `SourceRoot` waiver.
All 157 `visual.json` validate against the published `visualContainer/2.9.0`
schema **with its remote sub-schemas resolved** (visualConfiguration 2.3.0,
filterConfiguration 1.3.0, semanticQuery 1.4.0, formattingObjectDefinitions 1.5.0).

## Open questions

1. **`c_p2_dlg_naive` names a film the leaderboard will not show.** *Las mujeres
   deciden* really does hold a perfect 10.0 on 2 votes in the loaded snapshot, but
   4,304 listings hold a perfect 10.0 on **1** vote, so `tbl_perfect_tens`
   (contracted: top 3 **ascending** by `[Votes]`) will show three 1-vote titles
   instead. **Designer decides:** leave it as an illustration · sort the leaderboard
   descending · or add a `Title · Perfect ten (illustration)` measure and bind the
   name live. Nothing changed unilaterally. (BUILD_LOG → phase B2a findings, 1.)
2. **`c_waffle_cap` was re-worded for the fallback medium** — the contracted caption
   legends waffle cells ("outline = …") that the 100 % stacked bar does not have.
   Needs designer ack. (BUILD_LOG → phase B2a decisions.)
3. **Two contracted "at least" strings are large understatements** under the newer
   snapshot ("+ at least 18 more perfect 10s" vs 4,607; "at least 20 films … on 2–3
   votes" vs 293). True as written, shipped verbatim, better bound to measures.
4. **Alt text is still blocked on attribution** (rule `attribution.md`, blocker
   severity). p1/p2 add 18 visuals to the waiting list. Until it clears, the fourth
   M-003 carrier is missing and the extra tab stops on p1/p2 are what carry the
   trap marking to a screen-reader user.
5. **Deneb is not registered in this report** (`report.json` declares no
   `publicCustomVisuals`), so both Deneb visuals ship as their contracted native
   fallbacks. Restoring them is an entrant-side Desktop action, not an agent action.
6. **`btn_beat_1..3` and `btn_next_scene` have no action yet** — they are bookmark
   actions and the bookmarks are phase B2b. Verify the `visualLink.type` enum
   spelling for a bookmark action against `visualConfiguration` before writing it.
7. **Nothing built at stage 6 has been rendered.** No measure has been executed and
   no pixel seen; the BUILD_LOG's Desktop checklists are the gate for that.
