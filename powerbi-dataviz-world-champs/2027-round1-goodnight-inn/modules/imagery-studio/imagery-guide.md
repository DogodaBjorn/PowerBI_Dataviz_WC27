# Imagery guide: profile → candidates → registered resource

## 1. The profile

Each brand kit that wants imagery carries an `imagery-profile.yaml` beside
its `brand.yaml` (scaffold: `design/brand-kits/_template/imagery-profile.yaml`).
The profile's job is to make renders reproducible and on-brand:

| Field | Job |
|---|---|
| `style_spec` | One paintable paragraph: medium, linework, mood, motifs |
| `palette` | **Role references** into `brand.yaml` → `color.*` — never hexes; the skill resolves them at render time so a rebrand re-renders from one source of truth |
| `negative` | Brand-specific bans; the renderer always appends the no-text set on top |
| `style_anchors` | 2–5 real reference images (repo-relative paths) — these carry the style more than any text; no anchors = expect drift |
| `sizes` | Default render targets per report use (cover hero, section divider, background texture, empty state), at 2× the canvas slot |

No profile → don't improvise one from adjectives. Derive it with the user
(brand-kit-studio interview covers imagery when the kit is created) or skip
imagery for this project.

## 2. Composing a render spec

The skill writes one small JSON per render into
`project/deliverables/imagery/_specs/<asset-id>.json`:

```json
{
  "scene": "a lone lighthouse on a data-shaped archipelago, morning light",
  "style_spec": "<verbatim from the profile>",
  "palette": { "dominant": "#F5F6F8", "ink": "#1F2933", "accent": "#2563A8" },
  "negative": "<verbatim from the profile>",
  "style_anchors": ["design/brand-kits/<kit>/assets/anchors/a.webp"],
  "aspect_ratio": "16:9"
}
```

Rules:

- `scene` describes **subject only** — style lives in `style_spec`, colors
  in `palette`. Scenes name concrete objects, not abstractions ("a desk with
  a notebook and coffee", not "collaboration").
- Palette hexes come from the *active* brand kit (or the neutral defaults in
  `.claude/rules/design-hard-rules.md`), resolved from the profile's role
  references. The accent role is the report's one accent — never substitute
  another hue.
- Never put text, labels, numbers, or logo requests in the scene. The
  renderer hard-appends the no-text negatives; a returned image that still
  contains text is a rejected candidate, not a cropping exercise.
- `aspect_ratio` must be model-supported (`1:1`, `4:3`, `3:4`, `16:9`,
  `9:16`, `21:9`); off-ratio slots (divider bands) render at the nearest
  ratio and are cropped at placement — record the crop in the handoff.

## 3. Rendering

```
node scripts/imagery/render_image.mjs \
  --spec project/deliverables/imagery/_specs/<asset-id>.json \
  --out  project/deliverables/imagery/<asset-id>_c1.png \
  --root <repo root>
```

Key resolution: `--config <json>` → `GEMINI_CONFIG_PATH` env (JSON path) →
`GEMINI_API_KEY` env; config JSON shape `{ "apiKey": "...", "model": "..." }`.
Keys never enter the repo — config JSONs live outside it.

Exit codes: `0` wrote the PNG; `2` no key configured — **graceful
degradation**: note it in the handoff/BUILD_LOG, design proceeds on
canvas-studio furniture alone; `1` anything else (bad spec, HTTP error,
blocked prompt — the message says which; blocked prompts get one softened
retry, then the placement is dropped).

## 4. Candidates — always a choice, never a decree

Per contracted placement, render **2–3 candidates** (vary the scene
phrasing or motif between them — same spec re-runs also vary naturally) as
`<asset-id>_c1.png`, `_c2.png`, `_c3.png`. Present them to the user;
the user picks or rejects all. The chosen file is copied to its final name
`im_<purpose>_<page-id>.png` (e.g. `im_hero_p0-cover.png`); losing
candidates stay in `deliverables/imagery/` as rejected paths.

Judge candidates before presenting: on-palette? no text artifacts? quiet
enough for its surface (a background texture must sit far below data-ink
contrast — verify with `scripts/check_contrast.py` against the ink token)?

## 5. Registering in PBIR (stage 6, pbir-operator only)

Registration is three coordinated edits — verified against
`hp-world-champs/project/pbip/second-build.Report` (schema
report `3.4.0` / visualContainer `2.10.0`):

1. **File:** copy the PNG to
   `project/pbip/<report>.Report/StaticResources/RegisteredResources/<file>.png`.
2. **Manifest:** in `definition/report.json` → `resourcePackages`, ensure the
   `RegisteredResources` package exists and append an item:

   ```json
   { "name": "RegisteredResources", "type": "RegisteredResources",
     "items": [ { "name": "im_hero_p0-cover.png",
                  "path": "im_hero_p0-cover.png", "type": "Image" } ] }
   ```

3. **Reference:** an `image` visual (`visualType: "image"`) whose
   `objects.image[0].properties.sourceFile.image` carries:

   ```json
   "name": { "expr": { "Literal": { "Value": "'im_hero_p0-cover.png'" } } },
   "url":  { "expr": { "ResourcePackageItem": {
              "PackageName": "RegisteredResources",
              "PackageType": 1,
              "ItemName": "im_hero_p0-cover.png" } } },
   "scaling": { "expr": { "Literal": { "Value": "'Fit'" } } }
   ```

   Title/background/border off in `visualContainerObjects`; z-order below
   data visuals and chrome (`tabOrder` negative for pure chrome); page-level
   *background image* properties are the Desktop-manual alternative when a
   full-page fill is wanted (BUILD_LOG entry, fit = Fit, transparency per
   handoff).

Each placement gets a BUILD_LOG "Built" row (asset id + page) and, when the
Desktop-manual path is used, a manual-steps entry with a verify-by note.

## 6. Change discipline

- **Rebrand:** palette roles re-resolve → re-render all imagery from the
  same specs; anchors change only if the brand's reference art changed.
- **New placement:** back through the s5 contract (page-purpose + wireframe
  slot + handoff), then render — never straight into the report.
- Hand-retouched PNGs are drift: the spec JSON is the source of truth;
  fix the spec and re-render.
