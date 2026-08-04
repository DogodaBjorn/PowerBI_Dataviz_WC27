# Report craft floor

The last pass before a page is called built: verify the mechanics, refuse the
AI-tells. Run it on the rendered result, not the intention. A pinned design
contract or brand kit overrides anything here; habit does not. Translated to
Power BI from impeccable's craft floor + operate mode (Apache-2.0) and
taste-skill's AI-tells and density rules (MIT) — see CREDITS.md.

## Verify

Each item is a check on the built page. Batch them into one inspection round —
they share a render.

- **Contrast.** Every text/background pair ≥ 4.5:1 (large text and non-text
  meaning carriers ≥ 3:1). Run `python scripts/check_contrast.py` against the
  active theme; ad-hoc pairs via `--pair "#1F2933" "#F5F6F8"`. Exit 1 = not done.
- **Header spacing.** More space above a section header than below it — the
  header binds to what follows. Read the PBIR y-positions, don't eyeball.
- **One authored focal moment per page.** Exactly one element earned its size
  and the accent: the hero number, the annotated chart. Zero focal moments
  means no message; two means none either.
- **8px grid.** Every visual's x/y/width/height divisible by 8; page margin
  24px, card gutter 16px. Check the numbers in the PBIR source, not the canvas.
- **Tabular numerals for data columns.** Tables/matrices use a tabular-figure
  font (Segoe UI qualifies; verify whatever the brand kit picks), numbers
  right-aligned, one decimal discipline — columns must not wobble as values
  change.
- **States.** Page checked with slicers at defaults, with a filter combination
  that returns nothing, and with the longest real category names. Empty and
  overflow are states you shipped, not edge cases.

## Refuse

The category's lazy defaults. Reaching for one when the layout is free means
you were not deciding. Recognizing one means recomposing the page, not
softening the offender.

- **Full-page uniform KPI-card grid.** A wall of same-size cards is wallpaper
  (hard rule 6); one hero number earns its place, the rest support or leave.
- **Icon-in-colored-circle card headers.** The signature AI-dashboard tell. A
  card header is a label; decoration that carries no data goes.
- **Section-number decoration.** 01 / 02 / 03 eyebrows on page sections. The
  layout already orders the page; number only when the sequence itself informs.
- **Sparkline-as-decoration.** Sparklines and data bars serve scanning in a
  real column (visual-selection intent 10); a sparkline stuffed into a KPI
  card with no trend question is filler.
- **Two accent hexes.** One report, one accent — a second accent hue appearing
  on any page is a consistency-lock violation (hard rule 7).
- **Mixed corner radii.** One radius system report-wide, or the documented
  2-step scale — nothing ad hoc (hard rule 8).

The consistency locks themselves — one accent, one radius system, one
background treatment per archetype — live as rules 7–9 in
`.claude/rules/design-hard-rules.md` and fail the stage-6 gate on their own;
this floor exists to catch them before the gate does. With every check green,
spend the page on the message.
