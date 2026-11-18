# px-prototype

Turns an approved HTML design comp into build-ready truth. When stage 5
ends with a comp the user has actually SEEN and approved, this module
closes the gap between "looks right in the browser" and "is right in
PBIR":

```
approved HTML comp (project/design-prototypes/<comp>.html)
        ↓ capture_references.mjs        one exact-size @2x PNG per screen
        ↓ extract_layout.mjs            layout.json - exact rects, fonts, colors
stage 6: rects copied verbatim into visual.json positions
        ↓ Deneb-first for charts needing pixel control
verify: ±2px against layout.json + reference screenshots
```

## What it adds

- **Measurement over eyeballing**: `scripts/prototype/` (Playwright) dumps
  getBoundingClientRect() per element in report-canvas coordinates — the
  build never guesses a position.
- **Fidelity targets**: exact-size @2x reference screenshots per screen,
  the evidence the fidelity review diffs against.
- **The `px-prototype` skill**: golden rules, per-page workflow, and
  `references/gotchas.md` — the encoding, template, font, and screenshot
  pitfalls learned the hard way.

## Honest limits

The screenshot-diff loop verifies the **HTML-comp fidelity chain** (comp →
rects → PBIR source). It does not see what Power BI renders: rendered
pixels still require the s7 human review, or the `ms-authoring` Desktop
Bridge when available. BUILD_LOG carries those steps explicitly.

## Flow

Enable `px-prototype` in `project/project.yaml` → at stage-5 approval the
comp is measured and captured; at stage 6 `pbir-operator` builds each page
from the handoff row + measured rects; the fidelity review checks ±2px.
One-time machine setup: see `scripts/prototype/README.md`.

## Credit

Backported from Bjorn's proven **hp-world-champs** pixel-perfect pipeline
(`design_handoff_powerbi` handoff bundle: `powerbi-pixel-perfect` skill,
Playwright tools, PBIR templates — MIT). The one-approval-point HTML-comp
idea aligns with the impeccable-style comps-first practice noted in the
toolkit integration plan.
