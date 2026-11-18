---
name: s5-design
description: Lifecycle stage 5 - creative direction and design contract. Develop the report story, query the design-intelligence layer, propose three divergent design directions (rendered as hi-fi HTML comps when the px-prototype module is enabled), run the critique gate, and compile the winner into the design handoff quartet with its asset-fidelity inventory. Produces 05-design.md, page-purpose contracts, and the quartet in deliverables/.
---

# s5-design

**Question answered:** what should this report *be*, and exactly how will it
look? Primary agent: `report-designer`. This stage is the studio's
differentiator — do not compress it into "pick a layout".

## Procedure

1. **Story first.** From the requirements and metrics, write the report
   narrative: which pages, in what order, each answering one question for one
   audience. One `contracts/page-purpose.contract.yaml` per page (archetype
   from `design/page-archetypes.md`, intents from
   `design/visual-selection.md`). Include a Definitions page.
2. **Look before you invent.** Before drafting any direction, query the
   design-intelligence layer for the client's industry and context:
   ```bash
   python design/intelligence/search.py "<industry> dashboard" --domain style
   python design/intelligence/search.py "<industry>" --domain color
   ```
   Usage and Power BI caveats: `design/intelligence/README.md` — hits are
   inspiration to translate, never orders. Cite what was used *or overruled*,
   with the reason, in the `design_intelligence` block of
   `creative-direction.contract.yaml`. When mapping analytical intents to
   visuals, consult `design/chart-selection.csv` (per-form when/when_not with
   the `pbi_native`/`deneb` route); typography choices consult
   `design/brand-kits/_font-pairings.md` — Power BI-safe pairings only.
   Also read this client's own taste memory before drafting anything:
   `python scripts/learnings.py search --type taste`. Any entry that shapes
   a direction is surfaced as **"Prior learning applied: `<key>`"** — the
   client should never have to reject the same idea twice.
3. **Diverge.** Invoke the `design-critique` skill to produce **three
   genuinely divergent directions** in `creative-direction.contract.yaml`.
   Different in kind — metaphor, mood, density — not three accent colors.
   Each direction also declares in the contract:
   - a one-line **Design Read** — what the reader sees first, and why that
     works for this audience;
   - its **dials** — `DENSITY: compact|balanced|airy` and
     `VARIANCE: strict|expressive`.
   **With the `px-prototype` module enabled**, each direction is rendered as
   one hi-fi HTML comp at 1280x720 in `project/design-prototypes/` —
   **exactly three comps, one approval point**: the user picks a direction
   they can *see*, not imagine. Comps must never over-promise: ingredients
   PBIR cannot reproduce (animation, transitions, arbitrary CSS effects —
   blurs, masks, blend modes) are forbidden in the comp itself. Without the
   module, the prose path remains — say so to the user: directions are
   argued, not rendered. With the `fg-figma` module enabled and the Figma
   MCP connected, the three comps may additionally be published as
   side-by-side Figma frames for clients who review in Figma.
4. **Critique and converge.** Argue each direction against
   `design/design-doctrine.md` per audience; present all three honestly to
   the user; the user picks (record `chosen_because` in their terms) and the
   fidelity checklist is written. Log the verdicts to the project memory —
   the winner and each rejection, with the user's reasons:
   `python scripts/learnings.py add --type taste --key <direction-slug>
   --insight "approved|rejected: <reason in the user's terms>"
   --source 05-design.md`. **On approval, with px-prototype:** capture
   reference screenshots and extract rects from the winning comp (both tools,
   per the `px-prototype` skill) and record
   `project/design-prototypes/layout.json` + `reference_screenshots/` in the
   handoff as the measurement source. Then fill the handoff's
   **Asset-fidelity inventory**: every visual ingredient of the winner maps
   to one implementation medium — native visual / `dn-deneb` / `ca-canvas`
   SVG / `ic-icons` / `im-imagery` / accepted omission with reason. An
   unmapped ingredient blocks G5 closure.
5. **Compile the quartet** into `project/deliverables/`:
   - `design-handoff.md` (from `templates/design-handoff.template.md`) —
     per page: grid layout, every visual with id (naming conventions), intent,
     bound measures, polish moves, and exact property expectations; plus the
     filled Asset-fidelity inventory;
   - `data-model.md` (from the template) — the model as the designer needs
     it, including the not-available list verbatim;
   - `measures.dax` (from the template) — paste-ready display/support
     measures the design adds (insight titles, semantic-color measures),
     layered on the stage-4 model;
   - `theme.json` — via the `theme-from-brand-kit` skill (brand kit or
     neutral defaults), including the design brief's tokens.
6. Fill `design-brief.contract.yaml`; write `05-design.md` tying it together
   with `## Open questions`.

## Gate G5 checklist

- [ ] Every page has a purpose contract with a written 3-second message and
      3-minute path
- [ ] Design intelligence queried before directions were drafted; findings
      cited (used or overruled) in the creative-direction contract
- [ ] Three directions documented, each with Design Read + dials; critique
      honest, user chose — with px-prototype: exactly three 1280x720 comps
      existed at the approval point (without it: the prose path was stated)
- [ ] Asset-fidelity inventory complete — every winning-comp ingredient
      mapped to a medium or an accepted omission; nothing in the comp that
      PBIR cannot reproduce
- [ ] Quartet complete and internally consistent (same tokens in brief,
      theme.json, and handoff; same visual ids in handoff and measures)
- [ ] Fidelity checklist written (stage 6 will be judged against it)

Then hand back to `/next`.
