# fg-figma

Figma as an **optional design surface**. Nothing in the lifecycle depends
on it: contracts stay the source of truth for content, the HTML comp stays
the measurement source for px-prototype. When the Figma MCP is connected,
the module adds three jobs:

1. **s5 direction review** — mirror the three stage-5 direction comps as
   side-by-side Figma frames for clients who review and comment in Figma.
   One named page per direction; new versions land as new pages, earlier
   versions are never overwritten.
2. **Showpiece explorations** — cover pages, infographic-style definition
   pages, contest one-offs — built under the mechanism-mapping discipline:
   the element plan is written on paper *before* the first API call.
3. **Pull-back** — an approved Figma exploration re-enters the pipeline
   through px-prototype (export/screenshot → HTML comp or reference
   screenshots → measured rects), never Figma → PBIR directly.

## What it adds

- **The `fg-figma` skill**: surface detection, the three job procedures,
  and the transferable hard rules — content first, one mechanism per
  element, one element per `use_figma` call with a screenshot check after
  each, feedback captured as dated taste rules, explorations sealed off
  from project state.
- **`references/figma-craft.md`** (in the skill): the mechanism-choosing
  question, page/versioning conventions, build-call grain, and the Figma
  Plugin API pitfalls learned the hard way.

## Honest limits

Figma frames are *pictures* of the design, not the design contract. The
approval point remains the s5 gate; Figma comments come back as critique
input, never as silent edits. A Figma exploration proves nothing about
what PBIR can render — the asset-fidelity inventory still gates every
ingredient on the way back in.

## Flow

Enable `fg-figma` in `project/project.yaml` → at stage 5, if the client
reviews in Figma, publish the three comps as direction pages; any time, run
showpiece explorations on their own pages; on approval, pull the winner
back through the px-prototype chain. Without the Figma MCP in the session
the skill says so in one line and stops.

## Credit

Distilled from Bjorn's own proven `figma-infographic-design` skill
(TrainerBjornOps): the content-first workflow, mechanism-mapping before
building, one-element-one-call with screenshot verification, exploration
pages that never overwrite earlier versions, and the dated
feedback-derived-rules loop — battle-tested on the TrainerBjörn/DoGoDa
infographic-carousel work. Internal IP, re-expressed for report design.
The Figma MCP itself (`figma-use` and sibling skills) is Figma's official
tooling and governs *how* to call the plugin API.
