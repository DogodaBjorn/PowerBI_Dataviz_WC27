---
name: px-prototype
description: Pixel-perfect build pipeline from an approved HTML design comp (px-prototype module). Use when a project's stage-5 creative direction is approved as an HTML comp and stage 6 must recreate it exactly - capture reference screenshots, extract rects, build PBIR at measured positions, verify within +-2px.
---

# px-prototype

**Module gate:** requires `px-prototype` in `project/project.yaml` →
`modules`. If disabled, say so and stop. Requires Node + Playwright set up
once per machine (`scripts/prototype/README.md`).

When the approved design direction exists as an HTML comp, that comp is the
**source of truth for look and layout** — an extension of the design
handoff, not a replacement: ids, bindings, and intents still come from the
handoff quartet (`templates/design-handoff.template.md`).

## Golden rules

1. **Never eyeball positions — measure them.** `extract_layout.mjs` dumps
   exact getBoundingClientRect() values per element, relative to each
   screen's top-left = report-canvas coordinates.
2. **Rects are copied verbatim** into each `visual.json`
   `position: {x, y, z, width, height}`. No rounding to taste, no nudging.
3. **One screen per report page.** Screens carry `data-screen-label` and are
   sized exactly to the page canvas — 1280x720 default; tooltip pages at
   their own size (e.g. 320x240).
4. **References before building.** Capture the @2x PNGs first; they are the
   fidelity targets the build is judged against.
5. **Deneb-first for charts needing pixel control** (dn-deneb, deneb-studio
   module): Vega-Lite gives exact mark geometry native visuals cannot
   promise. Native visuals stay fine for forms they render faithfully.

## Procedure

1. **Stage 5, at approval:** the comp lands in
   `project/design-prototypes/<comp>.html` (self-contained; screens carry
   `data-screen-label` matching page ids). Run both tools from the repo root:
   ```bash
   node scripts/prototype/capture_references.mjs project/design-prototypes/<comp>.html
   node scripts/prototype/extract_layout.mjs   project/design-prototypes/<comp>.html
   ```
   Outputs: `project/design-prototypes/reference_screenshots/<page>.png`
   (@2x) and `project/design-prototypes/layout.json`. Record both in the
   design handoff as the measurement source.
2. **Stage 6, per page:** read the handoff row + the page's `layout.json`
   entry; build each visual at its measured rect — static text as textboxes,
   KPI values as cards bound to handoff measures, pixel-critical charts as
   Deneb specs, buttons/images per handoff. All authoring goes through
   `pbir-operator` with the usual small-diff + validate discipline.
3. **Verify:** desk-check every built `position` against `layout.json`
   (±2px tolerance); compare composition, type sizes, and colors against the
   reference screenshot (remember @2x: halve pixel measurements). Deviations
   are fidelity findings — fix or get user acceptance.
4. **Read `references/gotchas.md` before the first page** — encoding,
   template, font, and screenshot pitfalls that cost real hours in the field.

## What this verifies — and what it cannot

The screenshot-diff loop verifies the **HTML-comp fidelity chain**: comp →
measured rects → PBIR source. It proves the source files honor the comp; it
does **not** prove what Power BI renders. Rendered Power BI pixels still
require the s7 human review in Desktop/Service, or the `ms-authoring`
Desktop Bridge when available — record the remaining rendered-pixel checks
in BUILD_LOG as Desktop-manual steps.

## Done when

References and `layout.json` exist and are referenced by the handoff, every
built visual sits within ±2px of its measured rect with copy verbatim, and
BUILD_LOG lists the rendered-pixel verification steps still owed to s7.
