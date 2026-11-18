# px-prototype gotchas

Hard-won lessons from the hp-world-champs pixel-perfect build (Bjorn's
`design_handoff_powerbi` handoff bundle, MIT — adapted with thanks). Read
before the first page; each of these cost real iteration time.

## Comp conventions (the tools depend on them)

- Every screen element carries `data-screen-label`; the label becomes the
  screenshot filename (non-word characters → underscores), so **set labels
  equal to page ids** or you get orphaned PNGs.
- Screens must be sized exactly to their page canvas. A comp screen at
  1281px wide poisons every rect on that page.
- Both tools wait a few seconds for the comp runtime and webfonts to settle
  before measuring/capturing. If the comp lazy-loads content later than
  that, rects and screenshots capture the unfinished state — check the
  first PNG before trusting the batch.
- The measuring viewport (1600x1200) must exceed the largest screen or
  rects clip. Bump it in `extract_layout.mjs` for oversized canvases.
- Comp-viewer runtime scripts (image slotting, navigation helpers) exist
  for browser viewing only — never port them into the report.

## Screenshot workflow

- Captures are **@2x** (`deviceScaleFactor: 2`): a 1280x720 screen yields a
  2560x1440 PNG. When measuring on the PNG, **halve everything** before
  comparing to PBIR positions. Forgetting this is the classic "everything
  is exactly 2x off" hour-loss.
- Capture references **before** building anything, and recapture whenever
  the comp changes — stale references make the fidelity loop lie.
- Screens are screenshotted element-by-element (`scrollIntoViewIfNeeded`),
  so a comp taller than the viewport is fine; a screen with CSS transforms
  or zoom on an ancestor is not — rects come back scaled.

## Encoding and copy

- Copy is **verbatim**, including typographic characters (middle dot `·`,
  em dash `—`, curly quotes). These are the first casualties of a careless
  copy-paste through a terminal.
- Write all JSON as **UTF-8 without BOM** (repo default). A BOM or
  mojibake in a `textRuns.value` passes schema validation and only shows
  up as garbage in the rendered report.
- `layout.json` truncates own-text to 80 chars — it locates elements; the
  comp (or handoff) is the copy source, not `layout.json`.

## PBIR template usage

- Scaffold pages and textboxes from skeletons, then fill — don't write
  visual JSON from memory (invariant: research first, check the `$schema`).
  Minimal shapes that worked:
  - **Page:** `$schema` ...`/page/1.0.0/schema.json`, `name`,
    `displayName`, `displayOption: "FitToPage"`, `width`/`height`
    (1280/720), page `objects.background` color from the theme token.
  - **Textbox visual:** `$schema` ...`/visualContainer/1.0.0/schema.json`,
    `position {x,y,z,width,height}`, `visualType: "textbox"`,
    `objects.general[0].properties.paragraphs[].textRuns[]` with
    `textStyle {fontFamily, fontSize, fontWeight, color}`, and
    `drillFilterOtherVisuals: false`.
- `fontSize` inside `textRuns.textStyle` is a **string with px units**
  (`"13px"`), unlike most formatting objects. Mixing the conventions
  renders at default size with no error.
- Give every visual an explicit `z` — chrome below data below overlays.
  Unset z-order resolves differently in Desktop than in the source order.
- Tooltip pages keep their own canvas size and tooltip page binding; don't
  inherit the 1280x720 default onto them.

## Fonts and rendering parity

- A display font used in the comp must be **installed on the build/review
  machine under its exact name** (e.g. `Crimson Pro`, not
  `Crimson Pro Regular`), or Power BI silently substitutes and every text
  rect drifts. If embedding/installing is impossible, pick the documented
  fallback **and flag it** in BUILD_LOG — never substitute silently.
- Browser text metrics ≠ Power BI text metrics. Rects for text boxes come
  from the comp, but line wrapping may differ by a pixel or two — that is
  what the ±2px tolerance is for. Anything beyond ±2px is a finding, not
  tolerance.

## Measurement discipline

- `layout.json` lists every element ≥2px, so it is noisy: work from the
  handoff's visual list and use `layout.json` to look up each visual's
  rect, not the other way round.
- Rects are relative to the screen's top-left — already report-canvas
  coordinates. Do not add page margins on top.
- Colors in `layout.json` come back as `rgb()`/`rgba()` computed values;
  convert to the brief's hex tokens, and use the **token** hex (comp and
  theme must agree — if they don't, that's a stage-5 defect to raise, not
  a value to average).
