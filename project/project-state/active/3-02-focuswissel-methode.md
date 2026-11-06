# 02 - Focus-swap method for P2 (decision and claim status)

**Date:** 2026-11-06 · **Decided by:** Björn ("wat kunnen we nu vaststellen als
methode?" - answered and confirmed for recording) · **Stage:** 0; input to stages
3/4 (model) and 6 (build). Research basis and sources:
`research/log/2026-11-06-focuswissel-onderzoek.md`. Execution pattern: `.claude/skills/fx-focus/`; build description: `04-p2-build-method.md`.

## The decision, in one paragraph

**Native Power BI as the basis, the package choice decoupled from the layout,
bookmarks only for the layout states.** Two pre-designed layout states on P2
swapped by display-only bookmarks; the package choice lives in a persistent,
disconnected single-select selector that DAX reads; the scatter always shows all
valid packages and highlights the chosen one; the right panel swaps between
shortlist and plan (details plus waterfall). A layout swap is instant - it is not
a morph, and no smooth shrink/grow transition is promised anywhere. Deneb or HTML
Content are possible later upgrades (routes B and C below), never the base.

## Why this shape (the load-bearing evidence)

1. **Bookmarks capture visibility, filters, slicers and spotlight, with Data /
   Display / Current page / Selected visuals options** - so a display-only,
   selected-visuals bookmark swaps layouts without touching data state
   (Microsoft Learn, desktop-bookmarks).
2. **Applying a bookmark clears existing cross-filters and cross-highlights by
   design** (Microsoft answer on the community thread, citing the same docs).
   A scatter click selection therefore does not reliably survive a layout swap;
   a slicer selection does. That is why the selector, not the click, is the
   source of truth.
3. **There is no documented native morph** between bookmarks or layout states.
   A swap is a visibility change, not an animated transition.
4. **Deneb cannot provide a built-in morph either:** Vega dropped animated
   transitions in 3.0 ("not currently supported", porting guide); Vega-Lite
   animation is limited to discrete frame animation with linear interpolated
   animation an open enhancement (vega-lite issue 9590). Deneb 2.0 adds
   Continuous View / Data Patching (issue 374: prevents redraw on data changes,
   including cross-filtering) - useful for a persistent custom visual, still not
   animation. Deneb's canvas renderer exists and the categorical data window is
   30,000 rows (PR 683), so 456 points are not a data-limit problem; render
   performance still needs a live test.
5. **HTML Content:** the Secure edition sanitizes scripts but supports selection
   styling, tooltips and restricted SMIL/CSS animation (html-content.com docs) -
   fine for a detail card. The Regular edition's scripting is not formally
   supported and animates only inside the visual's own frame; it cannot resize
   native neighbours (no supported visual-API route), and it adds certification,
   accessibility and export risk. Not a primary architecture. Power BI Embedded
   customLayout can move visuals but is not available under Publish-to-Web.

## Routes and status

| Route | Status | Note |
|---|---|---|
| A - native: two layout states, display bookmarks, disconnected single-select selector, highlight-by-measure | **chosen base** | all parts documented; the combination is proven only by the test in `03-focuswissel-testplan.md` |
| B - one persistent Deneb visual with an internal focus state | parked upgrade | real selection + performance test required first; Continuous View helps state retention, it is not a morph |
| C - HTML Content Regular as the page architecture | not recommended | own-frame animation only, scripting not formally supported, certification/export risk; a Secure `<details>` card is allowed as a detail extra |

## Still unproven (do not claim before the test)

- Package choice persisting across the layout swap, all 456 points remaining
  visible with the chosen point highlighted, and details plus waterfall following
  the same selection - in one real PBIX.
- Scatter click behaviour across a bookmark switch (expected: cleared).
- Publish-to-Web rendering, PDF/PPT export, and the certification/accessibility
  consequences of any custom visual.
