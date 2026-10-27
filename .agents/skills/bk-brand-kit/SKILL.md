---
name: bk-brand-kit
description: Create or refine a brand kit by structured interview (brand-kit-studio module) - translate brand materials into design roles, validate contrast and fallbacks, write design/brand-kits/<kit>/brand.yaml. Use when the user wants a brand kit, house style, or client theme foundation - including when the client has no house style and needs one proposed.
---

# bk-brand-kit

**Module gate:** requires `brand-kit-studio` in `project/project.yaml` →
`modules` (in the template repo, outside a project, proceed — kits are
template assets). If disabled, say so and stop; `/project-init` or a one-line
edit enables it.

## Procedure

1. Collect materials: style guide, website URL, logo files, an existing
   report or deck if one exists. Read them before asking anything.
2. Interview per `modules/brand-kit-studio/interview-guide.md` — roles, not
   favorites. Confirm what materials imply; ask only what they don't answer.
3. Copy `design/brand-kits/_template/` to `design/brand-kits/<kit>/`
   (kebab-case kit name, client alias not real name in shareable repos) and
   fill `brand.yaml` completely — no `<placeholders>` left.
4. Place assets (logo) in the kit's `assets/`; record usage constraints.
5. **Validate before declaring done:**
   - AA contrast: ink/canvas, ink/surface, accent/both, good/both, bad/both
     (compute contrast ratios; don't eyeball);
   - good vs bad distinct under color-blind simulation (avoid pure
     red/green pairs; check hue + lightness separation);
   - categorical ramp: ≤6, mutually distinguishable, accent first;
   - every font family has a realistic Power BI-safe fallback.
   Record failed-and-accepted checks as comments in the kit.
6. Offer activation: set `brand_kit: <kit>` in `project/project.yaml`; if a
   project is past stage 5, note that `theme-from-brand-kit` must be re-run
   and the theme re-applied.

## No-brand path

When step 1 yields nothing — no style guide, no usable website, no house
style — propose candidates from the template's intelligence instead of
inventing tastefully:

1. Query the design-intelligence layer for the client's industry:
   `python design/intelligence/search.py "<industry>"` (add mood words —
   "fintech authoritative", "healthcare warm"). It returns role-token
   palette and style directions, not favorites.
2. Add 1–2 ready-made starter kits from `design/brand-kits/starter-*/` —
   ten pre-validated kits adapted from Anthropic's theme-factory themes;
   each header comment names its source theme, WCAG adjustments, and a
   "best for" line. Match on industry + personality, not on taste.
3. **Showcase, then choose** (theme-factory's interaction pattern): render
   2–4 candidates side by side as a swatch sheet — canvas/surface strip,
   ink on both, accent, the good/bad pair, the 6-step categorical ramp,
   and one type-sample line per candidate. An HTML swatch sheet or image
   works; a bare hex list does not. Never pick silently: ask which
   candidate (or which elements of which) and wait for the explicit choice.
4. Copy the winner to `design/brand-kits/<kit>/` and rejoin the procedure
   at step 2 — the interview shrinks to confirming personality adjectives,
   good/bad semantics, and type. Pick fonts by mood via
   `design/brand-kits/_font-pairings.md` (Power BI-safe pairings only).
5. Validate exactly as step 5. Starter kits pass as shipped, but any
   client tweak re-runs
   `python scripts/check_contrast.py --kit design/brand-kits/<kit>/brand.yaml`.

## Done when

`brand.yaml` is complete and validated, assets are in place, and the user
knows how the kit flows into theme.json via `theme-from-brand-kit`.
