---
name: im-imagery
description: Generate on-brand illustrative imagery for report chrome (imagery-studio module) - Gemini renders anchored on the brand kit's imagery profile, always 2-3 candidates for user choice. Use when a design direction calls for cover heroes, section dividers, empty-state art, or subtle background textures.
---

# im-imagery

**Module gate:** requires `imagery-studio` in `project/project.yaml` →
`modules`. If disabled, say so and stop.

## Procedure

1. **Contract check first:** imagery placements exist only if the stage-5
   design contract names them (page-purpose + wireframe slot in the design
   handoff). At stage 6, a request for new imagery goes back through the
   contract — never freelanced into the build.
2. **Doctrine check** (`modules/imagery-studio/README.md`): imagery is
   chrome — cover hero, section-divider band, empty state, faint background
   texture. Never a data visual, never behind/inside a data area, never
   per-card decoration. Doesn't fit → recommend canvas-studio furniture or
   nothing.
3. **Resolve the profile:** `design/brand-kits/<kit>/imagery-profile.yaml`
   (scaffold in `design/brand-kits/_template/`). Substitute its palette
   *role references* with hexes from the kit's `brand.yaml` (or neutral
   defaults from `.claude/rules/design-hard-rules.md`). The accent role is
   the report's one accent — consistency lock 7 applies to imagery. No
   profile → offer to fill one with the user or skip imagery; never
   improvise a style.
4. **Compose render specs** per `modules/imagery-studio/imagery-guide.md`
   §2 into `project/deliverables/imagery/_specs/` — scene is subject-only,
   size/aspect from the profile's report-use defaults. Never request text,
   numbers, or logos in a scene.
5. **Render 2–3 candidates per placement** with
   `scripts/imagery/render_image.mjs` (guide §3). Exit 2 = no Gemini key:
   record the degradation in the handoff/BUILD_LOG and proceed without
   imagery — the design must stand on canvas-studio furniture alone.
6. **Present the candidates; the user chooses.** Never auto-pick. Reject
   candidates yourself first if off-palette, containing text artifacts, or
   too loud for the surface (textures: contrast-check against ink). Chosen
   file → `im_<purpose>_<page-id>.png`; losers stay as rejected paths.
7. **Hand over:** the design handoff records each placement (asset
   filename, slot, scaling, crop if any). At stage 6, `pbir-operator`
   registers per guide §5 — file into
   `project/pbip/<report>.Report/StaticResources/RegisteredResources/`,
   `report.json` → `resourcePackages` item (`type: Image`), image visual
   referencing it via `ResourcePackageItem` — and logs every placement in
   the BUILD_LOG. This skill produces assets and instructions; it does not
   edit `project/pbip/` itself.

## Done when

Every contracted placement has a user-chosen asset in
`project/deliverables/imagery/` with its spec JSON beside it, no generated
image contains text or an off-kit hue, and the handoff carries filename +
slot + registration instructions (or the recorded no-key degradation).
