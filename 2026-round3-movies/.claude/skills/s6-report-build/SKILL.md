---
name: s6-report-build
description: Lifecycle stage 6 - report build. The pbir-operator authors PBIR exactly per the design handoff quartet (verbatim measured rects when the px-prototype module is enabled), holds the craft floor, applies the specified polish moves, maintains the BUILD_LOG, and passes the copy-polish sweep and the fidelity review. Produces the report under project/pbip/ and 06-build.md.
---

# s6-report-build

**Question answered:** does the built report honor the design contract?
Primary agent: `pbir-operator`; `qa-reviewer` + `design-critique` close the gate.

## Procedure

1. Re-read the quartet (`design-handoff.md`, `data-model.md`, `measures.dax`,
   `theme.json`). The handoff is the specification — a build idea that isn't
   in it goes back to stage 5, not into the report. Its **Asset-fidelity
   inventory** routes every ingredient to its medium (native / `dn-deneb` /
   `ca-canvas` / `ic-icons` / `im-imagery`); with the `px-prototype` module
   enabled it also names `project/design-prototypes/layout.json` +
   `reference_screenshots/` as the measurement source.
2. **Craft floor before authoring.** Read `design/report-craft-floor.md`
   immediately before the first edit: the **Refuse** list constrains what
   you may draft at all; the **Verify** list runs on every built page and
   once more before the gate.
3. Implement `measures.dax` into the model's `_Measures` table first (display
   measures: insight titles, semantic colors), per `tmdl-patterns`. Names
   byte-identical to the handoff.
4. Register and apply `theme.json`, then build page chrome (`z_*`) once and
   replicate it — chrome drift across pages is the most common fidelity
   finding.
5. Build page by page from the handoff tables: create each visual with its
   contracted id (`design/naming-conventions.md`), bind its data, set its
   **explicit properties** (a visual missing them is not approved), and apply
   its listed polish moves (`dataviz-polish`).
   - Prefer the `pbir-cli` adapter for creation, formatting, conditional
     formatting, and validation; fall back to direct JSON per `pbir-authoring`.
   - **px-prototype enabled:** each visual's rect is copied **verbatim** from
     its `layout.json` entry into `visual.json` `position` — no rounding, no
     nudging (`px-prototype` skill; Deneb-first for pixel-critical charts).
   - Small diffs; hooks validate every touched file.
6. Maintain `project/deliverables/BUILD_LOG.md` (via the `build-log` skill)
   **as you go**: decisions, assumptions, and every step that must be finished
   in Desktop — never at the end from memory.
7. After the last page: full `validate-project` sweep, then — before G6
   closes — the **`copy-polish` sweep** over every user-visible string
   (visual titles/subtitles, insight-title wording, tooltips, textboxes,
   page names, button labels, deliverable prose), then the `design-critique`
   **fidelity review** against the handoff and the fidelity checklist.
   `design-critique` owns the review's method and scoring — run it as
   written, don't restate or improvise it here. **px-prototype enabled:**
   the G6 fidelity evidence includes the ±2px comparison of every built
   `position` against `layout.json` and the check against
   `reference_screenshots/` (@2x — halve pixel measurements). Deviations
   become review findings: fix or get user acceptance.
8. Write `06-build.md`: build summary, findings and their resolutions,
   inventory of pages/visuals.

## Gate G6 checklist

- [ ] `validate-project` green (JSON, TMDL strict, naming, state)
- [ ] Every visual matches its handoff row (id, data, properties, polish)
- [ ] Craft floor holds: Verify list green on every page, no Refuse-list
      pattern shipped
- [ ] `copy-polish` sweep clean over every user-visible string
- [ ] px-prototype (when enabled): every position within ±2px of
      `layout.json`; reference-screenshot comparison recorded as gate
      evidence
- [ ] Fidelity review clean or every deviation user-accepted
- [ ] BUILD_LOG current, including the manual-Desktop-steps checklist

Then hand back to `/next`.
