# Figma craft — transferable build discipline

Distilled from Bjorn's proven `figma-infographic-design` workflow
(TrainerBjornOps, internal IP), re-expressed for Power BI report surfaces.
The `figma-use` skill governs HOW to call the plugin API; this file
governs WHAT to build and in WHAT order.

## Choosing a mechanism

Ask per element: **what must the reader SEE happen?**

- change or throughput → flow (items through a filter/funnel)
- proportion or outcome → fraction, small table, or one big result number
- a choice → decision tree (question, yes/no branches, two option cards)
- structure or make-up → anatomy with annotation arrows
- asymmetry ("A yes, B no") → blocked arrow with a badge on the route
- sequence or progress → roadmap spine / step tracker
- something to remember → checklist, sticky note, rule-of-the-day line

One mechanism per element; the mechanism carries the message, text only
clarifies. Comparisons demand **parallel anatomy**: identical structure,
only the values differ — any layout difference between the two reads as
meaning.

## Pages and versioning

- Direction mirrors: `s5 · Direction <A|B|C> · <name> · vN`.
- Explorations: `Explore <subject> vN · <style name>`.
- A new version is a NEW page; earlier pages stay. The user judges by
  comparing versions side by side — v1 standing next to v2 is a feature.
- Tokens: bind fills/text to Figma variables when the file has them;
  otherwise use the active brand kit's hexes (`design/brand-kits/<kit>/`
  or the neutral defaults in `.claude/rules/design-hard-rules.md`).
  Hardcode nothing a token covers.

## Build order

1. One read call first: page list, available fonts
   (`listAvailableFontsAsync`), any image hashes needed.
2. Create the page; then one element (or one comp frame section) per
   `use_figma` call, strictly sequential.
3. After every call: screenshot the frame, compare against the plan, fix
   before continuing. Overlapping decorations are the most common
   fix-round — always verify positions visually.
4. Close with an overview screenshot of the whole page (temporary group,
   small scale, then ungroup) before showing the user anything.

## Quality gate before the user sees it

- The page's message is visible in 3 seconds; headings alone tell the
  story (the skim layer).
- Every number matches its contract verbatim; a source line sits on any
  frame that carries claims.
- No overlap anywhere (checked on screenshots); margins respected.
- Color grammar follows the brand kit and the one-accent lock; every
  tokenable property is bound, not hardcoded.
- Zero em dashes in text layers; ` · ` or a colon instead. No AI-stock
  phrasing (the copy-polish watchlist applies to frame copy too).
- Logos placed as assets/instances, never redrawn or recolored.

## Feedback-derived rules

User feedback on an exploration is converted into a dated `type=taste`
entry in `project/project-state/learnings.jsonl` via
`scripts/learnings.py`. Read the existing taste entries BEFORE planning a
new exploration — each one starts above the last. Founding examples from
the source workflow: loose cards without a shared ground read as messy
(one continuous background is the glue); "step by step" needs a visible
progress mechanism, not just numbers in a corner.

## Plugin API pitfalls (all hit in production)

- `resize()` BEFORE setting `layoutMode`, or the frame collapses to hug;
  then `primaryAxisSizingMode = 'FIXED'` and resize again.
- `layoutSizingHorizontal/Vertical = 'FILL'` only works AFTER
  `appendChild` into an auto-layout parent.
- Wrapping text needs `textAutoResize = 'HEIGHT'` plus an explicit width,
  or the node becomes a strand / runs off the frame — check right edges.
- Images: read intrinsic size via `getImageByHash(...).getSizeAsync()`
  and use scaleMode `FIT`; `FILL` crops silently. WebP renders white in
  fills — convert to PNG locally first.
- Verify font style names exactly (families differ: `ExtraBold` vs
  `Extra Bold`, some have only Regular/Bold).
- `figma.setCurrentPageAsync` at most once per call; never switch pages
  in a loop.
- Scripts are atomic: on error nothing mutated — fix and rerun the call.
