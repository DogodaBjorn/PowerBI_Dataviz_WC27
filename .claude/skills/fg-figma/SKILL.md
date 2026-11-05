---
name: fg-figma
description: Figma as an optional design surface (fg-figma module) - publish the three s5 direction comps as side-by-side Figma pages for clients who review in Figma, build showpiece explorations (cover pages, infographic-style definition pages) with mechanism-mapping discipline, or pull an approved Figma exploration back into the px-prototype pipeline. Use when the Figma MCP is connected and design work should surface in Figma.
---

# fg-figma

**Module gate:** requires `fg-figma` in `project/project.yaml` →
`modules`. If disabled, say so and stop.

**Surface check:** the Figma MCP must be present in the session (the
`use_figma` tool and the `figma-use` skill appear in the available lists).
Absent → one line — "Figma MCP not connected; proceeding on the HTML-comp
path" — and stop. Nothing in the lifecycle depends on this module.

**MANDATORY skill load:** invoke the `figma-use` skill BEFORE every
`use_figma` call — the Figma MCP requires it and skipping it causes
hard-to-debug failures. Likewise `figma-create-new-file` before
`create_new_file`.

Figma is a *surface*, never a source of truth: contracts and the design
handoff decide content; the HTML comp remains the measurement source for
px-prototype. One Figma file per project (user-provided or created after
loading `figma-create-new-file`); record its URL in `05-design.md`.
Consistency locks (design-hard-rules 7–9) apply inside Figma too — one
accent, one radius system, one background treatment per archetype.

## Job A — publish s5 directions for Figma-side review

When the client reviews in Figma, mirror the three stage-5 direction comps
as side-by-side frames:

1. One page per direction, named `s5 · Direction <A|B|C> · <name> · vN`.
   Versions are **never overwritten**: a revision is a `vN+1` page; earlier
   pages stay so directions and versions compare side by side.
2. Frames at canvas size (1280×720 unless the project decided otherwise),
   content **verbatim from the comp** — same copy, same numbers, no polish
   the comp doesn't have. Build per `references/figma-craft.md`.
3. Record page names + file URL in `05-design.md`. The approval point is
   still gate G5; Figma comments return as critique input for
   `design-critique`, never as silent edits to comp or contract.

## Job B — showpiece explorations

Cover pages, infographic-style definition pages, contest one-offs.

1. **Content first.** Pull the real titles, numbers, and definitions from
   the contracts (metric contracts, page-purpose, handoff quartet) before
   opening Figma. Contracts are the source of truth — never invent, round,
   or rename a number in Figma.
2. **Mechanism-mapping on paper before any API call.** Per element choose
   exactly ONE visual mechanism (the choosing question and catalog:
   `references/figma-craft.md`) and write the element plan — what each
   element shows and which numbers it carries. A mapped exploration comes
   out calm; one improvised inside Figma comes out muddled.
3. Explorations get their OWN page, `Explore <subject> vN · <style name>`;
   never overwrite an earlier exploration — the user compares versions.
4. Build one element per `use_figma` call, screenshot after each (hard
   rules below); finish with an overview screenshot before showing
   anything.

## Job C — pull an approved exploration back

Always via px-prototype, never Figma → PBIR directly:

1. Export the approved page (`get_screenshot` / export, @2x).
2. Either **re-express it as a self-contained HTML comp** in
   `project/design-prototypes/` and run the normal capture/extract pair
   (the clean path — full px-prototype fidelity chain), or use the @2x
   exports as reference screenshots and measure rects from them
   (remember @2x: halve pixel measurements).
3. From there the `px-prototype` skill owns the chain, and the
   asset-fidelity inventory still gates every ingredient — anything PBIR
   cannot reproduce is mapped to a medium or an accepted omission before
   G5 closes.

## Hard rules (transferable, non-negotiable)

1. **One element per `use_figma` call, strictly sequential.** Screenshot
   after every call; fix before the next. Small enough to recover, large
   enough to reuse shared chrome.
2. **One mechanism per element.** Two ideas means two elements or one cut.
3. **Numbers verbatim from contracts.** A showpiece that rounds or renames
   numbers breaks trust in the whole report.
4. **Feedback becomes a dated rule.** When the user reacts to an
   exploration, append a dated `type=taste` entry to
   `project/project-state/learnings.jsonl` via `scripts/learnings.py`, so
   the next exploration starts above this one.
5. **Explorations never write project state.** No edits to contracts,
   `project/pbip/`, the state machine, or deliverables from a Figma
   session; the pull-back (Job C) is its own explicit, user-approved step.

## Done when

The job's pages exist under their naming convention with no earlier
version overwritten, every frame passed its screenshot check, content
traces verbatim to contracts/comps, `05-design.md` records the file URL
and page names, and any pull-back went through the px-prototype chain
with the asset-fidelity inventory honored.
