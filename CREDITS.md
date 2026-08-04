# Credits

**Credit where it is due — no negotiations.** This toolkit stands on the
work of the people and communities below. Nothing here was copied from
them: every technique is re-derived in this repo's own words and code, and
this file plus in-file credit lines say plainly where the ideas came from.
(One deliberate exception: the MIT-licensed design-intelligence search
tooling is vendored under `design/intelligence/` — see its entry below.)
If you fork or share this repository, these credits travel with it. If you
adopt a new idea into it, add its source here in the same change
(see `.claude/rules/attribution.md` — this is a hard rule, not a courtesy).

## Tools this repo drives

| Who | What we owe them | Where it lands |
|---|---|---|
| **Kurt Buhler & Maxim Anatsko** — the [pbir CLI](https://pypi.org/project/pbir-cli/) | Headless PBIR authoring as a practice; the reason agent-driven report building is tractable at all. Custom non-commercial license — respected, never vendored. | `pbir-cli` adapter skill, DEPENDENCIES.md |
| **Daniel Marsh-Patrick** — [Deneb](https://deneb.guide/) | Declarative Vega-Lite visuals inside Power BI: the middle rung between native and custom-visual development. | deneb-studio |
| **Microsoft Power BI / Fabric teams** | PBIP/PBIR/TMDL open formats, the base themes, `pbiviz` tooling, and the core-visuals work (Miguel Myers and team: new card, reference labels, button slicer). | everywhere; custom-visual-studio; nav-studio |
| **UW Interactive Data Lab** — [Vega-Lite](https://vega.github.io/vega-lite/) | The grammar Deneb speaks. | deneb-studio |
| **Microsoft** — [skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | The official powerbi-authoring plugin (five authoring skills), the Power BI Modeling MCP server (Node ≥ 18), and the Desktop Bridge — referenced, never vendored; two short README/Learn quotes cited in the adapter. MIT-licensed repo; consulted via web 2026-08-04 (no local clone to pin — Learn overview `git_commit_id 463305865f2f2b332991b5354bf082098729ee24`). | `ms-authoring` adapter skill, DEPENDENCIES.md |

## Practitioners whose published work shaped the modules

| Who | What we learned from them | Where it lands |
|---|---|---|
| **[bibb.pro](https://bibb.pro/)** | Modern button-slicer UI patterns (segmented controls, tabs, toggles, clickable KPI cards, image items), navbar thinking, wireframing and layout writing. | nav-studio, canvas-studio |
| **[Valerie Junk](https://www.valeriejunk.nl/)** (PorcuBI) | Tables and matrices as visuals that work *with* the user; storytelling per audience; adoption-first design. | table-studio |
| **[Kerry Kolosko](https://kerrykolosko.com/)** | SVG/HTML micro-visualization craft: sparklines, in-cell marks, SVG-in-DAX as a discipline. | icon-studio, table-studio |
| **[Davide Bacci](https://deneb.guide/community/resources)** | What Deneb can really do — the showcase that sets the bar. | deneb-studio |
| **[Mara Pereira](https://www.datapears.com/)** (Data Pears) | Design-tool-first canvases: wireframes and designed backgrounds as the foundation of premium layout. | canvas-studio |
| **[Reid Havens](https://www.havensconsulting.net/)** (Havens Consulting) | Report-page tooltips as a designed layer, including field-parameter-driven tooltip content. | tooltip-studio |
| **[Meagan Longoria](https://datasavvy.me/)** | The Power BI accessibility checklist that defined the practice: measured contrast, alt text, tab order, color-never-alone. | a11y-studio |
| **[Kurt Buhler](https://data-goblins.com/)** (Data Goblins) | Power BI design and agentic-development practice beyond the CLI itself. | source register, scout runs |

## Method & standards the doctrine stands on

| Who | What we owe them | Where it lands |
|---|---|---|
| **Ralph Kimball & Margy Ross** | Dimensional modeling: grain-first, star schemas, conformed dimensions. | star-schema rule, stage 3 |
| **Marco Russo & Alberto Ferrari** ([SQLBI](https://www.sqlbi.com/)) | DAX correctness and patterns; the standard the dax-patterns skill defers to. | dax-patterns, source register |
| **Daniel Otykier** ([Tabular Editor](https://tabulareditor.com/)) | Model-hygiene practice and the Best Practice Analyzer tradition. | source register |
| **Edward Tufte** | The data-ink principle — "ink serves data" is his idea in our words. | design-doctrine |
| **Cole Nussbaumer Knaflic** ([Storytelling with Data](https://www.storytellingwithdata.com/)) | Declutter-and-focus discipline; context in titles. | design-doctrine, dataviz-polish |
| **Financial Times** ([Visual Vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)) | Intent-first chart selection — the ancestor of our 10-intent table. | design/visual-selection.md |
| **IBCS** (Rolf Hichert et al.) | Notation consistency and variance-visualization rigor. | source register, table-studio |
| **Nielsen Norman Group** | Evidence-based dashboard usability. | source register |
| **W3C** ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)) | The accessibility criteria our contrast script and audit implement. | a11y-studio, check_contrast.py |

## Skill repositories whose ideas were adopted

Same rule as everywhere else: nothing copied — each idea is re-expressed in
our own words, with an in-file credit line where it lands. The commit pins
the exact revision consulted (repos were read via forks under
`github.com/DogodaBjorn`; licenses and copyrights are the upstream authors').

| Who | What we adopted | License · commit | Where it lands |
|---|---|---|---|
| **Siqi Chen** — [humanizer](https://github.com/DogodaBjorn/humanizer) | The AI-writing-tell catalog (itself distilling Wikipedia's ["Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), WikiProject AI Cleanup), re-expressed as an eight-tell list for report copy; cluster-based detection (judge clusters, don't flatten legitimate formal prose); the principle that a provided writing sample outranks the style rules. | MIT (LICENSE, © 2025 Siqi Chen) · `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | copy-polish |
| **Corey Haines** — [marketingskills](https://github.com/DogodaBjorn/marketingskills) | The specificity rule (concrete outcomes beat vague topic labels); sweep discipline adapted from the Seven Sweeps (sequential focused passes, so-what test); action-oriented button-label guidance from the CTA rules. | MIT (LICENSE, © 2025 Corey Haines) · `c21a984a56da10fb6085e6334f6f60929220a4da` | copy-polish |
| **Leonxlnx** — [taste-skill](https://github.com/DogodaBjorn/taste-skill) | The three Consistency Locks (one accent color per report, one corner-radius system, one background treatment per page archetype), re-expressed as hard rules 7–9. | MIT (LICENSE, © 2026 Leonxlnx) · `e988add20dab0fa97d7a76781c48961c8184288e` | `.claude/rules/design-hard-rules.md` |
| **Yonathan Cohen** (Tool Monsters) — [handoff-skill](https://github.com/DogodaBjorn/handoff-skill) | The seven-section verbatim-state session-handoff format with its zero-invention rules, adapted into the user-global `handoff` skill that feeds the `next` skill's handoff intake. | MIT (LICENSE, © 2026 Yonathan Cohen (Tool Monsters)) · `348e67e29e357466c8a757d0c1cbc320335ba03d` | global `~/.claude/skills/handoff`, next skill step 0 |
| **Next Level Builder** — [ui-ux-pro-max](https://github.com/DogodaBjorn/ui-ux-pro-max-skill) | The BM25 design-intelligence search tooling (`search.py`, `core.py`, `design_system.py`) and its data CSVs (colors, typography, charts, styles, ui-reasoning), **vendored** into `design/intelligence/` — this repo's one vendored-code exception, permitted by MIT; only change is the `DATA_DIR` relocation in `core.py`. Additionally adapted (not copied): `charts.csv` rewritten for Power BI as `design/chart-selection.csv` (when/when-not kept; web-library column replaced with `pbi_native`/`deneb`; intent column keyed to visual-selection.md), and the mood keywords plus pairing structure of 22 of 74 `typography.csv` font pairings re-expressed with Power BI-safe fonts. | MIT (LICENSE, © 2024 Next Level Builder) · `3b5df7547964f0cb3424de74cff55b69039250d3` | `design/intelligence/`, `design/chart-selection.csv`, `design/brand-kits/_font-pairings.md` |
| **Paul Bakaus** — [impeccable](https://github.com/DogodaBjorn/impeccable) | The Verify/Refuse craft-floor structure and its check items (contrast thresholds, heading-spacing rule, one authored moment per page, refuse-the-defaults framing) from `craft-floor.md`, plus states coverage and consistency-over-surprise from `operate.md`, translated to Power BI reports; prose adapted, in-file attribution included. | Apache-2.0 (LICENSE, © 2025 Paul Bakaus) · `5e572c8b8af3e108ab52ce4180adb4d6eb1c2ebc` | `design/report-craft-floor.md` |
| **Leonxlnx** — [taste-skill](https://github.com/DogodaBjorn/taste-skill) *(second adoption)* | The AI-tells catalog (icon-in-circle headers, section numbers, decorative sparklines) and the content-density rules, adapted into the Refuse list of the report craft floor; the consistency locks are referenced there via design hard rules 7–9 rather than restated. | MIT (LICENSE, © 2026 Leonxlnx) · `e988add20dab0fa97d7a76781c48961c8184288e` | `design/report-craft-floor.md` |
| **Anthropic, PBC** — [theme-factory](https://github.com/DogodaBjorn/skills_two) (Anthropic skills repo, read via the `skills_two` fork) | The 10 preset theme palettes and names (Ocean Depths, Sunset Boulevard, Forest Canopy, Modern Minimalist, Golden Hour, Arctic Frost, Desert Rose, Tech Innovation, Botanical Garden, Midnight Galaxy), adapted into complete starter brand kits — expanded onto the full brand-role schema, WCAG-adjusted, fonts remapped to Windows-safe faces, modifications noted per file as Apache-2.0 §4(b) requires; plus the showcase-then-choose interaction pattern in bk-brand-kit's no-brand path. | Apache-2.0 (skills/theme-factory/LICENSE.txt, © 2026 Anthropic, PBC) · `b29e7cf65e5cb78a5ac33d582270551bc74a14eb` | `design/brand-kits/starter-*/`, bk-brand-kit |
| **Paul Bakaus** — [impeccable](https://github.com/DogodaBjorn/impeccable) *(second adoption)* | Deterministic anti-pattern detector rule logic re-expressed in Python (nothing imported): flat-type-hierarchy ratio threshold, dash-as-AI-tell, repeated-section-kicker, design-system color-drift concept, neutral-vs-chromatic channel spread, and the advisory-vs-failure separation that became the waiver mechanism. | Apache-2.0 (LICENSE, © 2025 Paul Bakaus) · `5e572c8b8af3e108ab52ce4180adb4d6eb1c2ebc` | `scripts/pbir_detect.py` |
| **Garry Tan** — [gstack](https://github.com/DogodaBjorn/gstack) | 0–10 scoring per review pass with a what-a-10 anchor; unresolved-decisions table gating closure; high/medium/polish triage; the atomic one-fix-one-diff loop with per-fix re-verification and the machine-readable fix-task JSONL; the append-only learnings/decisions JSONL pattern (schema and supersede-instead-of-edit) re-expressed as original code. | MIT (LICENSE, © 2026 Garry Tan) · `a3259400a366593e0c909dd9ac3e59752efd2488` | design-critique, `project/project-state/fix-tasks.jsonl`, `scripts/learnings.py` |
| **Jesse Vincent** — [superpowers](https://github.com/obra/superpowers) | The claim-requires-fresh-evidence discipline (verification-before-completion) that became the lifecycle's Gate-evidence floors; the TDD-for-skills method (baseline-test without the skill first, capture rationalizations verbatim, re-test under pressure) at the heart of skill-forge. | MIT (LICENSE, © 2025 Jesse Vincent) · `3dcbd5c4b48e02263fbf4a3c01e3fe4f81d584d9` | `lifecycle/lifecycle.md` Gate evidence, skill-forge |
| **Anthropic, PBC** — [skill-creator](https://github.com/DogodaBjorn/skills_two) *(second adoption, same repo)* | The description trigger-eval concept (a fresh agent sees only name+description; count trigger/no-trigger over repo-realistic prompts) and quick-validate hygiene, folded into skill-forge and the first description audit. | Apache-2.0 (© 2026 Anthropic, PBC) · `b29e7cf65e5cb78a5ac33d582270551bc74a14eb` | skill-forge, `research/skill-descriptions-audit.md` |

## First-party repositories backported

Bjorn's own prior work, folded back into the template. Listed for provenance
(these are not third-party debts), with the exact revision consulted.

| Source repo | What moved | Provenance · commit | Where it lands |
|---|---|---|---|
| **hp-world-champs** (`E:\PowerBI Set-up\hp-world-champs`, design_handoff_powerbi bundle) | Playwright layout-extraction and reference-capture tools (`tools/extract_layout.mjs`, `tools/capture_references.mjs`), generalized (LEGO/HP specifics stripped, defaults parameterized, 1280×720 canvas and @2x capture kept); the pixel-perfect skill's golden rules, workflow, and ±2px definition of done; minimal PBIR template shapes (incl. the `"13px"`-string fontSize quirk); the `playwright 1.61.1` pin. | MIT (repo LICENSE, © 2026 Bjorn / dogoda.nl — own prior client work) · `dddbc82db28f047e55cc0ad205d07bd553f7b1b6` | `scripts/prototype/`, px-prototype module (`.claude/skills/px-prototype/`) |
| **LinkedInContentOps** (`E:\TrainerBjornOps\LinkedInContentOps`, private) | The anchor-conditioned Gemini image renderer (rewritten from the `@google/genai` SDK to a zero-dependency fetch against the generateContent REST endpoint); the image-profile pattern (style_spec + palette + negatives + style anchors + default sizes) as `imagery-profile.yaml` with hexes replaced by brand-role references; the config/secrets resolution pattern with graceful no-key degradation. | First-party, no LICENSE file — adopted by ownership (bjorn@dogoda.nl), not under a license grant · `3a8ccd9bb97b38f03e7b5d1fa2341ee74623f5db` | `scripts/imagery/render_image.mjs`, `design/brand-kits/_template/imagery-profile.yaml`, imagery-studio module |
| **TrainerBjornOps** (`E:\TrainerBjornOps`, private — `figma-infographic-design` skill) | The Figma working discipline: content-first (contracts are the source of truth, never invent numbers in Figma), mechanism-mapping before any API call, one element per `use_figma` call with a screenshot check after each, explorations on their own never-overwritten pages, feedback captured as dated rules, and explorations never touching pipeline state. | First-party, no LICENSE file — adopted by ownership (bjorn@dogoda.nl) · `3a8ccd9bb97b38f03e7b5d1fa2341ee74623f5db` | fg-figma module (`.claude/skills/fg-figma/`) |

## Built with

This repository was designed and authored with **Claude Code** (Anthropic),
which also does the heavy lifting inside it. Copyright and license of the
repo content: see [LICENSE](LICENSE) (MIT, © Bjorn / dogoda.nl).

---

*Missing or mis-stated credit? That's a defect — open an issue or fix it
directly. Over-attribution costs a line; under-attribution costs integrity.*
