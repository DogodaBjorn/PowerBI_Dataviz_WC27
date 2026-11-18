---
name: dataviz-polish
description: The finishing pass that takes a correct report to premium - ten ranked high-leverage moves (insight titles, semantic color, focal contrast, sparklines, small multiples...) plus a showpiece tier and anti-patterns. Use during stage 5 design specification and stage 6 build, whenever the user asks to polish or level up a report, or when preparing a contest or executive showpiece submission.
---

# dataviz-polish

Polish is specified at stage 5 (the handoff names each move per visual) and
executed at stage 6 — it is not freelance decoration at build time. Gate for
every move: does it sharpen the 3-second message or deepen the 3-minute
trust? If neither, it's ornament — skip it. (The declutter/focus lineage
here owes Tufte's data-ink principle and Knaflic's *Storytelling with
Data*; micro-viz craft owes Kerry Kolosko — see CREDITS.md.)

## The ten moves, ranked by impact ÷ effort

1. **Insight titles.** A DAX measure composes the title sentence
   ("Margin +2.1pt vs Q1, driven by North") bound via title → fx → field
   value. The single biggest perceived-intelligence upgrade a report can get.
   One short clause, always traceable to a measure — long titles are where
   insight goes to die.
2. **Semantic color.** A measure returns a hex token (from the theme's
   good/bad/neutral) through conditional formatting, so color states the
   verdict. The pattern is `SWITCH(SIGN([Δ]), 1, good, -1, bad, neutral)`
   returning theme tokens, never hard-coded hexes. If the brand kit defines
   a watch state between good and bad, use its token — never invent one ad
   hoc. Always paired with a sign or label — never color alone.
3. **One focal point.** The story series carries the accent; every other
   series drops to the neutral gray. If everything is highlighted, nothing is.
   The eye should land on the answer in under a second — size, intensity,
   and position are preattentive; use those, not decoration.
4. **Reference lines and bands.** Target, average, or last-year as a quiet
   labeled line/band turns "a number" into "a number in context". A bar at
   82 means nothing until the line says "target 75". Good/bad zones behind
   a scatter or trend band the same way — analytics pane where the visual
   supports it, a faint background shape where it doesn't.
5. **Sparklines and data bars in tables.** A standings board instead of a
   number grid — trend and magnitude scannable per row. Beyond bars and
   sparklines, a background scale or direction arrow only where the column
   earns it (encoding order and limits: `tb-tables`).
6. **Small multiples.** Beyond ~4 series, split into panels with synced axes
   (the native well, or measure-driven where the visual lacks it); gray
   context + one accent per panel. Restrict to the top N panels.
7. **Hero number + micro-context.** KPI cards carry a delta and a tiny trend
   next to the big number; a number without context is a quiz question.
8. **Progressive disclosure.** Overview stays clean; depth lives in
   drill-through and hover tooltips (tooltip pages). Nothing important is
   *only* in a tooltip.
9. **Field parameters.** One chart, a slicer to switch metric/dimension —
   collapses near-duplicate visuals and pages.
10. **Sparing motion.** At most one bookmark-driven state change per page,
    and only when it answers a real question. Utility states — a reset
    button, a filter-panel toggle — don't count against that budget; story
    states do. Motion is salt, not sauce.

## Showpiece tier (contest and executive submissions)

For work judged on finish — contest entries, executive showpieces — a
second tier sits on top of the conservative ten. The tier's own bar is
*clever, but clear*: every technique must raise clarity in the same stroke
as cleverness — a trick that impresses but slows comprehension is cut.
Two non-negotiables:
showpiece work still obeys every design hard rule and consistency lock
(WCAG AA contrast, color never the only carrier, one accent, one radius
system, one background treatment per archetype — see
`.claude/rules/design-hard-rules.md`), and every showpiece move is
contracted at stage 5, named per page or visual in the design handoff like
the numbered moves — never improvised at build time.

- **S1 — Editorial framing.** Masthead, question-led subtitles, a closing
  footer, and one short measure-backed narrative sentence per page. If the
  narrative DAX grows elaborate it grows wrong; one clause per finding.
- **S2 — Annotation layer.** The "why" goes on the chart — a callout at
  the peak, the anomaly, the inflection — not buried in a tooltip (move 8
  still holds: depth may live deeper, the story may not).
- **S3 — Editorial type hierarchy.** One display serif for hero numbers
  and headlines, one grotesk for labels, one mono for kickers and meta — a
  single scale declared in the brand kit/theme, identical on every page.
- **S4 — Hero KPI at full dress.** Move 7 via Card (new): big value,
  reference-label delta (▲/▼ vs prior), and a tiny sparkline in one card.
- **S5 — Full in-cell encoding.** Move 5 extended per `tb-tables`: data
  bars, sparklines, a background scale on the score column, direction
  arrows — the plain value always stays present.
- **S6 — Info affordance.** A quiet ⓘ opening definitions or methodology
  (tooltip page or drill-through) instead of crowding the canvas with
  caveats.

Reality check: several showpiece surfaces (Card (new) reference labels,
table cell elements and sparklines, analytics reference lines, bookmarks)
are Desktop-manual — build what `pbir-authoring`/`pbir-cli` can, and put
the rest on the BUILD_LOG manual-Desktop-steps checklist. Showpiece pages
must also survive export: contests and boards judge screenshots and PDFs,
so nothing essential lives only in hover or interaction. The tier raises
finish, not the bar of proof — the review pass below and the s6 fidelity
review judge showpiece pages exactly like any other, and `ax-audit` still
gates alt text, tab order, and measured contrast.

## Anti-patterns (reject on sight)

3-D anything; pies for ranking; gauges by default; dual axes implying
causation; rainbow categorical palettes; KPI-card wallpaper; decorative
icons on every card; gridlines darker than data; redundant axis titles and
heavy borders where whitespace and alignment already structure; legends
when direct labels fit; "creative" interactions that hide the answer
behind a click;
dynamic narrative so elaborate it turns fragile or wrong.

## Review pass (5 steps, any page)

1. Read the page for 3 seconds — write down the message you got. Is it the
   contracted one?
2. Delete test: name one element that could go. If you can, it goes.
3. Squint test: does the visual hierarchy survive blur? (hero > support > chrome)
4. Trust walk: periods labeled, units and comparison basis explicit on
   every number, baselines honest, definitions one step away.
5. Consistency sweep: formats, colors, terminology identical across pages.
