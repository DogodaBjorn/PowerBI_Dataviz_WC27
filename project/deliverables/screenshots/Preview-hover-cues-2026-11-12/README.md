# Preview: hover cues, 12 Nov 2026 (night)

**These are composites, not Desktop renders.** They start from the FinalV2 Desktop renders (`../ScreenshotsFinalV2/01`,
`02`, `03`), erase the header line and the 16 px ring-i badges (the Night zone from `backgrounds/canvas-night.jpg`, card
areas in white), and draw the new pills at their slots from `project/design-prototypes/opzet-layout.json`. Made by
`project/tools/preview_hover_cues.py`. Decision and reasoning: `project/project-state/active/18-hover-cues-2026-11-12.md`.

What differs from the real report:

- The pill words are set in Liberation Sans Bold (Arial metrics, the Mac fallback under Publish to Web). In Desktop they are
  Segoe UI Semibold, a little narrower and lighter.
- P2's slimmer source line is set in Liberation Sans, not Segoe UI.
- Everything else (charts, numbers, cards) is the FinalV2 render as it was.

| File | Shows |
|---|---|
| `preview_p1_brand-review.png` | P1: "Hover a bar" on F3 and "Hover a hotel" on F4 in their kicker rows; the header's top right clear; the Definitions chip at the right of the footer row; the source line 12 px lower, level with P2's |
| `preview_p2_recommended-A.png` | P2, rec: "Hover a dot" in the reading guide (the guide's "Hover a dot for its moves." is gone); "Hover a year" in the cumulative chart's legend row; the footer row: the slimmer source line, "Revisit the facts" (one pill, F1 to F4 each a hover zone) and Definitions; the recommendation tile as before |
| `preview_p2_considered-B-C.png` | P2, alts: "Hover a dot" in the small scatter's title row; "Hover a year" on the comparer; the same footer row |

Round 2 (same night): the first version put the three moves of A as chips in the recommendation tile; Björn found them too busy
and wanted all four findings back in a "Revisit the facts" group, so they moved to P2's footer row as one pill.

Still owed: Desktop renders 01-04 after the regeneration, and a hover test on the Definitions chips and the four zones of "Revisit the facts".
