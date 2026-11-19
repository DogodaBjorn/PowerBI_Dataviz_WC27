# Publish7 - final visual fixes (prompt for Claude Code)

Date: 2026-11-15
Related review: [28-review-final-check-publish7-2026-11-15.md](28-review-final-check-publish7-2026-11-15.md)
Scope: two visual fixes only. No data, model, calculation, selection, sorting, colour or other layout changes. No merge, no publication.

## Instruction

Apply only these two visual fixes for publish7 in DogodaBjorn/PowerBI_Dataviz_WC27.

Read project/project-state/active/28-review-final-check-publish7-2026-11-15.md on main first. The reviewed build is on rebuild-finalv3, package project/deliverables/final-check-publish7. Work from that version or its verified successor. Preserve existing work.

1. Your plan chart: walkthrough/19_p2-build-eight-moves.png shows only 7 bars for 8 selected moves. Energy programme (-$12.2M) is hidden behind a vertical scrollbar. Adjust row spacing and/or chart height so all selected moves, up to 10, are visible without scrolling. Keep names and values readable, with no clipping or overlap. Do not shrink the whole report.

2. Recommended view: give the "Hover a year" hint more space from "Cash positive above this line". Make the smallest local spacing adjustment needed so both remain clearly separated and readable. Keep their wording unchanged.

Keep the current native visuals. Do not change data, the model, calculations, selection behaviour, sorting, colours or unrelated layout. Apply both fixes in the relevant generator and regenerate the build through the existing build process, so a rebuild preserves them.

Verify with real selections of 3, 8 and 10 moves at both 1366px and 1920px viewport widths. For 8 moves, use the selection in the cited screenshot, including Energy programme. Inspect all six renders yourself: every selected bar visible, no scrollbar, readable labels and values, no regressions elsewhere. Check that counts, amounts, the "You" scatter point and cash line still agree. Also render and inspect the Recommended view at both widths to confirm the hint spacing. Rerun the relevant existing build and number checks.

Commit and push both fixes and the evidence screenshots on a separate fix branch. Report the branch, commit, changed files and checks actually completed. Do not merge or publish. These two fixes do not replace the separate private-window click test of the public report and do not establish full technical signoff.
