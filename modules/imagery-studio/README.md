# imagery-studio

Generates on-brand illustrative imagery for **report chrome**: cover-page
heroes, section dividers, empty-state illustrations, and faint background
textures. Renders come from Gemini image generation, but they stay on-brand
by construction — every render is conditioned on the brand kit's *real*
style-anchor images plus a profile-pinned style spec, palette, and negative
prompt.

Imagery complements the other visual modules; it replaces none of them:
canvas-studio still owns page layout and furniture-only background SVGs,
icon-studio still owns functional marks. Imagery is the third, most sparing
layer — identity art on non-data surfaces.

## Doctrine: chrome, never a data visual

The design hard rules ban "decorative images that carry no data" from data
surfaces — and generated imagery does not get an exemption. It earns its
place only as *contracted identity chrome*:

- **Allowed surfaces:** cover page hero, section-divider band, empty/error
  state, a faint full-canvas texture that stays far below data-ink contrast.
- **Never:** behind or inside a data area, as a stand-in for a visual, or
  sprinkled per-card. If a chart would fight the image, the image loses.
- **No text in images.** Words, numbers, and logos live in the report layer
  (text boxes, `z_` visuals) — the renderer hard-appends the no-text
  negatives, and a render that sneaks text in is rejected, not cropped.
- **One accent** (consistency lock 7): imagery draws from the same palette
  roles as everything else; it never introduces a second accent hue.
- **Contracted at s5.** Imagery placements are part of the design handoff
  (page-purpose + slot on the wireframe). Stage 6 builds exactly that;
  imagery freelanced at build time is a gate failure like any other
  deviation.

## Flow

1. Enable `imagery-studio` in `project/project.yaml` → `modules`.
2. Fill `design/brand-kits/<kit>/imagery-profile.yaml` (scaffold in
   `design/brand-kits/_template/`) — style spec, palette *roles* referencing
   `brand.yaml`, negatives, and 2–5 real style-anchor images.
3. At stage 5, run the `im-imagery` skill: it composes render specs per
   [imagery-guide.md](imagery-guide.md), calls
   `scripts/imagery/render_image.mjs`, and always produces **2–3 candidates
   per placement** in `project/deliverables/imagery/` for the user to choose
   from. No key configured → the skill records the degradation and the
   design falls back to canvas-studio furniture alone.
4. At stage 6, `pbir-operator` registers the chosen files in the report's
   `StaticResources/RegisteredResources/` per the guide's PBIR recipe and
   logs each placement in the BUILD_LOG.

## What ships with the module

- [imagery-guide.md](imagery-guide.md) — profile → render spec → candidates
  → PBIR registration, including the exact three-part `RegisteredResources`
  wiring.
- `scripts/imagery/render_image.mjs` — zero-dependency (Node ≥ 18) Gemini
  renderer; key via `GEMINI_API_KEY` or a config JSON, clear-message exit
  when absent.
- `design/brand-kits/_template/imagery-profile.yaml` — the profile scaffold.

## Credit

The profile-driven, anchor-conditioned rendering approach (real sketch
images as style anchors + pinned palette + hard negative prompt) is adapted
from Bjorn's own LinkedInContentOps publishing pipeline (first-party,
private repo) — re-parameterized here for brand kits and PBIR targets.
Image generation itself is Google Gemini (`gemini-2.5-flash-image`); see
DEPENDENCIES.md for the pinned model and API notes.
