---
name: fx-focus
description: Focus-swap pattern for the P2 investment page - one source of truth for the selected package (disconnected single-select), display-only bookmark states, highlight-by-measure, and the route B/C upgrade gates. Use when building or reviewing the P2 package scatter, the shortlist/plan panel swap, or any layout-state interaction in this project.
---

# fx-focus

The decided P2 interaction method (`project/project-state/active/02-focuswissel-methode.md`,
research in `research/log/2026-11-06-focuswissel-onderzoek.md`). The method is
decided, not yet proven: the gate is `project/project-state/active/03-focuswissel-testplan.md`.

## Rules (apply in order)

1. **One source of truth for the selection.** The chosen package lives in a
   disconnected single-select selector (slicer or buttons) that DAX reads via
   `SELECTEDVALUE`. Never derive "the chosen package" from a scatter click:
   applying a bookmark clears cross-selections by design, so clicks do not
   survive a layout swap; slicer selections do.
2. **Bookmarks swap layout only.** Two pre-designed layout states, bookmarks
   with Data off, Display on, Current page off, Selected visuals only; the
   selector stays outside the selected visuals. A bookmark never changes the
   package or scenario selection.
3. **The scatter never filters itself.** All valid packages stay visible; the
   chosen package is highlighted by a measure (color/size flag). A connected
   slicer on the package table would reduce the scatter to one point - use the
   disconnected pattern or disable that interaction explicitly, and test it.
4. **Clicks may filter, never navigate.** A point click must not trigger a
   bookmark or state change.
5. **No morph claims.** The swap is instant. Do not promise, design toward, or
   spend effort on an animated shrink/grow between states; there is no
   documented native mechanism and Deneb/Vega does not provide one either.
6. **Test before build.** Stage 6 starts on this pattern only after tests 1-3
   of the test plan pass in a separate PBIX.

## Route gates

- **Route B (Deneb persistent visual, internal focus state):** requires the
  `deneb-studio` module gate and the dn-deneb justification gate, plus the
  route-B spike in the test plan (selection, `__selected__` styling,
  cross-filter exposure, render speed at 456 points). Deneb 2.0 Continuous
  View / Data Patching helps state retention; it is not animation.
- **Route C (HTML Content):** Regular is on hold as architecture (own-frame
  animation only, scripting not formally supported, certification/export risk).
  A Secure `<details>` detail card is allowed without a gate, built from a
  measure, tested in the P2W render pass.

## DAX patterns

See `references/pakketmodel-dax.md`: the 456-package table concept, the
package-project bridge, the disconnected selector, the highlight measure and
the waterfall contribution measures. All concept-stage until the test plan
runs; per the research-first rule, verify every property against the current
Desktop version before writing it.

## Done when

The test plan's go criteria 1-3 are recorded green, the selector drives every
P2 visual, the scatter shows all packages with a visible highlight, and no
file, tooltip or conversation promises an animated transition.
