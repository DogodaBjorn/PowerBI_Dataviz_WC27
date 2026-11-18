# Design handoff — <project name>

<!-- The design source of truth. Stage 6 builds EXACTLY this; the fidelity
review judges the build against this file. Copy to project/deliverables/
and fill. Keep placeholders in <> until resolved. -->

Direction: **<chosen direction name>** (see creative-direction contract)
Design Read: <one line — what the reader sees first, and why that works>
Dials: DENSITY <compact|balanced|airy> · VARIANCE <strict|expressive>
Canvas: <1280x720> · Theme: `theme.json` · Brand kit: <kit|neutral defaults>

## Reading me

- Visual ids follow `design/naming-conventions.md` and match `measures.dax`.
- "Polish" entries reference the numbered moves in the `dataviz-polish` skill.
- Anything not specified here defaults to the theme — visual-level overrides
  below are exceptions and each carries its reason.

## Page chrome (identical on every page)

| Element | Id | Spec |
|---|---|---|
| Masthead | `z_masthead` | <height, background token, title + page-question text spec> |
| Navigation | `z_nav` | <placement, states> |
| Footer | `z_footer` | <freshness stamp binding, definitions link> |

---

## Page 1 — `<p1-name>` (<archetype>)

**Question:** <from the page-purpose contract>
**3-second message:** <the sentence>
**Layout:** <grid description: rows/columns in px on the 8px grid>

| Id | Visual | Intent | Data | Polish | Explicit properties |
|---|---|---|---|---|---|
| `kpi_<x>` | KPI card | magnitude | <measure(s)> | 7 (hero + micro) | <title mode, background, border, radius> |
| `hero_<x>` | <type> | <intent> | <fields/measures> | 1, 3, 4 | <axis ranges, reference line, label spec> |
| `sl_<x>` | Slicer | — | <field> | — | <style, default state> |

**Interactions:** <cross-filter behavior, drill-through target, tooltip page>
**Leaves out:** <what was deliberately excluded>

<!-- Repeat the page block per page, Definitions page included. -->

---

## Definitions page — `<p9-definitions>`

Content from the metric contracts (02-metrics.md glossary), period
conventions, freshness, caveats, and the not-available list verbatim.

## Asset-fidelity inventory

<!-- Filled at s5 approval from the winning direction (its HTML comp when
the px-prototype module rendered one; the prose direction otherwise).
Every visual ingredient of the winner maps to exactly one implementation
medium; an unmapped ingredient blocks gate G5. Comps never over-promise:
ingredients PBIR cannot reproduce (animation, transitions, arbitrary CSS
effects — blurs, masks, blend modes) are removed from the comp at s5, not
inventoried away as omissions after the fact. -->

Measurement source (px-prototype module only):
`project/design-prototypes/layout.json` ·
`project/design-prototypes/reference_screenshots/` (@2x)

| Ingredient (from winner) | Page / slot | Medium | Notes |
|---|---|---|---|
| <hero chart treatment> | <p1 / hero> | <native visual \| dn-deneb \| ca-canvas SVG \| ic-icons \| im-imagery \| omitted — reason> | <> |
| <page background / card slots> | <all / chrome> | <ca-canvas SVG> | <> |
| <nav icon set> | <all / z_nav> | <ic-icons> | <> |
| <cover hero image> | <p1 / masthead> | <im-imagery> | <registered by pbir-operator at s6> |

## Manual steps expected in Desktop

<!-- Anything the design knows cannot be authored headlessly; BUILD_LOG
will confirm or extend this list at stage 6. -->

- <step>

## Fidelity checklist (from the creative-direction contract)

- [ ] <defining element 1>
- [ ] <defining element 2>
- [ ] <defining element 3>

## Rejected paths

<!-- Each losing s5 direction with the one-line reason it lost, from the
critique gate. Recorded so a later session never resurrects one as a fresh
idea. Do not re-litigate without new requirements. -->

- **<losing direction name>** — <one line: why it lost>
- **<losing direction name>** — <one line: why it lost>
