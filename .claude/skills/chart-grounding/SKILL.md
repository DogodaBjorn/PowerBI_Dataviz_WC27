---
name: chart-grounding
description: >-
  Canonical chart-choice and chart-craft grounding for pbi-atelier, compiled by
  BookCompiler from Alan Smith's How Charts Work (the author behind the FT Visual
  Vocabulary) reconciled with the existing writing, usability and visual-design canon,
  with page-level provenance. Use at stage 2 when choosing measures that will be
  charted, at stage 5 when mapping intents to visuals and writing page-purpose
  contracts, at stage 6 when setting axes, colours, titles and labels, at stage 7 for
  the cold read and alt text, and whenever a visual choice is questioned or critiqued.
---

# Chart grounding for pbi-atelier

The atelier's promise is "3-second clarity, 3-minute trust". This skill is the
judgment layer behind both halves of it: the 3-second half needs the right form for the
reader's question, the 3-minute half needs honest measures, scales and words. Credit:
the chart canon below is re-derived from Alan Smith, *How Charts Work* (FT Publishing,
2022), via the BookCompiler canon (CP-051 to CP-072); see CREDITS.md.

## Position among this repo's assets

- `design/visual-selection.md`, `design/chart-selection.csv`, `design/design-doctrine.md`,
  `.claude/rules/design-hard-rules.md`, the brand kits, and the `dataviz-polish` and
  `design-critique` skills stay the operational authority for procedures and concrete
  values. This canon is their judgment layer: use it to decide, explain and critique.
- Where the canon and a local doc disagree, flag it to the user with both sides; never
  silently override either way. Known differences are listed below.
- Full canonical detail and provenance: `references/principles.md`. Inheritance index
  (adapted rules PBA-C-001 to 006 and their CP parents): `adapter.yaml`.

## The canon, applied to pbi-atelier

**Stage 1 and 2: the question and the measure**

- Every page question becomes reader questions per visual before any visual is named
  [CP-051]. A requested chart type is a cue to ask what the reader should learn.
- Chart the measure that answers the question: rates with the denominator stated when
  groups differ in size, gaps from a named reference, ratios with the threshold marked;
  keep original units recoverable in tooltips or labels [CP-065].
- Look beneath every summary before it becomes a KPI card: median for skewed values,
  split pooled patterns by segment, open catch-all categories [CP-060].

**Stage 5: intent to form (page-purpose contracts)**

- Each visual in a page-purpose contract records: reader question, intent (from the
  10-intent table), canonical family, chosen form, one alternative, and what the form
  sacrifices; a needed sacrifice gets a companion visual or tooltip, not an overloaded
  chart [CP-051, PBA-C-001].
- Sentence, table or chart: if the geometry adds nothing to the title, it is a KPI card
  or a sentence; if readers look values up, it is a table set for scanning [CP-052].
- Precise comparisons as position or length on a shared baseline; area, 3D and volume
  never carry a comparison the decision depends on [CP-053].

| Atelier intent (visual-selection.md) | Canonical family | Canon says, in short |
|---|---|---|
| 1 Magnitude | magnitude [CP-054] | sorted bars from zero, story item highlighted; connected dots for 2-3 series per category; log dots or symbols for extreme ranges |
| 2 Change over time | change over time [CP-055] | line by default; 1-3 highlighted series over grey; slope for two points; small multiples on one axis; columns only for a sparse single series |
| 3 Comparison across categories | magnitude [CP-054] | as above; horizontal bars for long labels, never rotated labels |
| 4 Ranking | ranking [CP-056] | sort by value; bump chart for position only; slope for two periods; ranked table for lookup |
| 5 Part-to-whole | part-to-whole [CP-061] | pie or donut only for a few labelled parts of one whole; stacked bars for several wholes; treemap for hierarchy; waterfall for a bridge |
| 6 Distribution | distribution [CP-059] | histogram for one shape; dot strip or beeswarm for findable items; boxplots by median for many groups, whisker convention stated |
| 7 Correlation | correlation [CP-058] | scatter, cause on x, causal or not stated; dual axis only for fluent audiences |
| 8 Flow / decomposition | flow [CP-063] | Sankey for stages, waterfall for running totals; never arrays of pies |
| 9 Deviation | deviation [CP-057] | bars from a named reference, direction labelled in words, only the misses coloured |
| 10 Detail lookup | sentence/table/chart [CP-052] | right-aligned tabular figures, one precision per column, spacing not rules |
| (none) | spatial [CP-062] | map only when place is the point; rates on filled maps, counts as symbols, pair with totals |
| pattern grids | heatmap [CP-064] | sorted rows and columns, few classes, values printed when they matter |

**Stage 6: building the visual**

- Axes: bar and column value axes start at zero, always (check that the axis start is
  not set above zero in the visual's format JSON); line and dot visuals of rates may zoom, with the benchmark as a
  constant line and the range stated; small multiples share one axis [CP-066, PBA-C-003].
- Colour by job: sequential for ordered values, diverging only around a meaningful
  centre, qualitative for categories, one saturated highlight over grey via conditional
  formatting - never the default theme rainbow [CP-069, CP-038]. Lightness carries every
  distinction [CP-043].
- Label the data directly (data labels, line-end or series labels where the visual
  offers them, a Deneb spec where it does not); legends are a fallback [CP-068].
- Words: the visual title states the finding with a verb that names the relationship;
  the subtitle carries measure, unit, universe and period; annotations on turning points
  and targets; the source in the page footer [CP-067, CP-026, PBA-C-004].
- Show uncertainty when it is material (forecast bands, error bars with their meaning
  stated); never rank values whose intervals overlap [CP-070, CP-019].

**Stage 7: delivery**

- Cold read: show each page without the briefing to someone who has not seen it; if what
  they say is not the title, fix the visual [CP-034, CP-067].
- Alt text per visual: chart type, what is measured, what it shows [CP-043].
- Unfamiliar forms (beeswarm, slope, Marimekko) get a reading key on the canvas or in the
  tooltip, and are reused across pages rather than reinvented [CP-071].

## Where the canon and the atelier's docs differ (flagged, not edited)

These are proposals for the user to accept or reject; until then the local docs win.

1. **No spatial intent.** `visual-selection.md` files maps under comparison
   (`chart-selection.csv`: "3 Comparison (spatial)"). The canon treats spatial as its
   own family with its own gate: map only when place is the point, filled maps show rates
   or ranks never raw counts, counts go to symbols, classes chosen after looking at the
   distribution [CP-062, PBA-C-005]. Proposed: an 11th intent "Spatial".
2. **Declutter versus enrich.** `design-doctrine.md` principle 2 ("remove before adding")
   matches CP-001; the canon also records CP-072 (enrich rather than dumb down) as a
   genuine tension with CP-001. Resolution used here: operational and KPI pages follow
   the doctrine; explanatory and showpiece pages may layer one secondary relationship at
   a time with a key (PBA-C-006). Proposed: one sentence in the doctrine naming this
   display-mode split.
3. **Dual axes.** The atelier avoids them ("dual-axis lines implying causation"); the
   canon is sceptical, not prohibitive: fluent audiences only, each axis coloured like its
   series, both ranges justified, otherwise index both series to one axis [CP-058]. The
   atelier's stricter rule is a legitimate narrowing; keep it unless a client audience
   reads dual axes daily.
4. **Missing forms in `chart-selection.csv`.** The canon gives decision rules for slope
   charts, connected dot plots (instead of paired bars), bump charts, diverging stacked
   (spine) charts for survey sentiment, beeswarms and Lorenz curves [CP-054 to CP-059].
   Proposed: rows for these with their native or Deneb route.
5. **Heatmap placement.** The CSV files the matrix heatmap under distribution; the canon
   places heatmaps wherever pattern across many cells beats exact values (calendar,
   category grid, dense scatter) [CP-064]. Minor; no change needed unless it confuses.

## Critique checklist

- Which reader question does this visual answer, and which family does its form
  actually emphasise? [CP-051]
- Is the plotted measure the one the question needs, with its denominator? [CP-065]
- Would a sentence, a KPI card or a table serve this reader better? [CP-052]
- Does any axis, window or bin choice create or hide the story? Is the benchmark drawn?
  [CP-066]
- Does the title state a finding that the visual's most prominent feature proves?
  [CP-067]
- Blur and greyscale: does the highlight land on the item the title names, and does
  meaning survive without hue? [CP-038, CP-069, CP-043]

## Never

- Never truncate a bar or column axis; change the form or the measure instead [CP-066].
- Never colour a filled map by raw counts [CP-062].
- Never 3D, exploded or many-sliced pies, never arrays of pies for flows [CP-061, CP-063].
- Never a title whose verb claims causation the evidence lacks [CP-058, CP-019].
- Never let the software's suggested visual or default palette make the choice [CP-051,
  CP-069].
