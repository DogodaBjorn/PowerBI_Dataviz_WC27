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
| **Daniel Marsh-Patrick** — [Deneb](https://deneb.guide/) and [HTML Content](https://html-content.com/) | Declarative Vega-Lite visuals inside Power BI: the middle rung between native and custom-visual development. His HTML Content docs (interactivity, sanitization) grounded the Secure-card patterns in fx-focus. Round 4 (2026-11-10): the move selector `dn_build_selector` follows his Advanced Cross-Filtering docs (`pbiCrossFilterApply` with a filter expression, `pbiCrossFilterClear`, `__selected__`) and the PBIR Implementation Guide (the `jsonSpec` literal, `provider`, `selectionMode`). | deneb-studio; fx-focus; `project/tools/build_selector_spec.py`, `opzet_report.py` (`deneb_selector`) |
| **Microsoft Power BI / Fabric teams** | PBIP/PBIR/TMDL open formats, the base themes, `pbiviz` tooling, and the core-visuals work (Miguel Myers and team: new card, reference labels, button slicer). | everywhere; custom-visual-studio; nav-studio |
| **UW Interactive Data Lab** — [Vega-Lite](https://vega.github.io/vega-lite/) | The grammar Deneb speaks. | deneb-studio |
| **Microsoft** — [skills-for-fabric](https://github.com/microsoft/skills-for-fabric) | The official powerbi-authoring plugin (five authoring skills), the Power BI Modeling MCP server (Node ≥ 18), and the Desktop Bridge — referenced, never vendored; two short README/Learn quotes cited in the adapter. MIT-licensed repo; consulted via web 2026-08-04 (no local clone to pin — Learn overview `git_commit_id 463305865f2f2b332991b5354bf082098729ee24`). | `ms-authoring` adapter skill, DEPENDENCIES.md |

## Practitioners whose published work shaped the modules

| Who | What we learned from them | Where it lands |
|---|---|---|
| **[bibb.pro](https://bibb.pro/)** | Modern button-slicer UI patterns (segmented controls, tabs, toggles, clickable KPI cards, image items), navbar thinking, wireframing and layout writing. | nav-studio, canvas-studio |
| **[Valerie Junk](https://www.valeriejunk.nl/)** (PorcuBI) | Tables and matrices as visuals that work *with* the user; storytelling per audience; adoption-first design. | table-studio |
| **[Kerry Kolosko](https://kerrykolosko.com/)** | SVG/HTML micro-visualization craft: sparklines, in-cell marks, SVG-in-DAX as a discipline. Round 6 (2026-11-10): the package tooltip's range bar, moves list and move grid are SVG-in-DAX measures in native image visuals, after her conventions (`%23` for `#`, single quotes inside the SVG, Image URL data category). | icon-studio, table-studio; `sketch_model.py` (`TT Range SVG`, `TT Moves SVG`, `TT Move Grid (svg)`) |
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
| **Alan Smith** (*How Charts Work*, FT Publishing 2022; via the BookCompiler canon CP-051 to CP-072) | Relationship-first chart choice beyond the familiar forms, scale and map honesty, writing the chart (finding titles, metadata subtitles, annotation). | .claude/skills/chart-grounding |
| **IBCS** (Rolf Hichert et al.) | Notation consistency and variance-visualization rigor. | source register, table-studio |
| **Nielsen Norman Group** | Evidence-based dashboard usability. | source register |
| **Don Norman** (*The Design of Everyday Things*, revised 2013) | Signifiers: a visible mark that says where an action is possible. The hover badge of 12 Nov 2026 (a Tangerine ring-i on every visual that opens a page tooltip) was that idea in our words; since the same night it is the hover tag (a pill with a filled Tangerine disc and the instruction, on every hover target) and the hover chips. | `sketch_model.py` (`HOVER_TAGS`, `_pill()`), `opzet_report.py` (`hover_tag()`, `hover_chip()`) |
| **Jakob Nielsen** ([10 usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/), Nielsen Norman Group) | Recognition rather than recall: put the meaning on the mark instead of in a legend the reader has to remember. Why the hover tag of 12 Nov 2026 says "Hover a bar" on the card itself and the far-away "hover for more" legend left. | `sketch_model.py` (`HOVER_TAGS`), `opzet_report.py` (`hover_tag()`) |
| **W3C** ([WCAG 2.2](https://www.w3.org/TR/WCAG22/)) | The accessibility criteria our contrast script and audit implement. | a11y-studio, check_contrast.py |

## The dashboard canon (dataviz-canon skill)

Re-derived from a merged research synthesis (2026-11-05; see
`research/log/2026-11-05-dataviz-best-in-class-canon.md`). Nothing copied;
each principle in `references/canon.md` carries a `DC-nnn` id and names its
source. Credits below are additional to the method and standards table above
(Tufte, Knaflic, FT/Alan Smith, IBCS, Nielsen Norman and W3C already stand
there and are reused by the canon).

| Who | What we owe them | Where it lands |
|---|---|---|
| **Stephen Few** (*Information Dashboard Design*, *Show Me the Numbers*, Perceptual Edge) | The dashboard definition (monitoring, one screen, at a glance), the bullet graph as the gauge's replacement, the critique of memorability research, the accessibility position we answer. | dataviz-canon DC-001, 017, 033, 042 |
| **Alberto Cairo** (*The Functional Art*, *How Charts Lie*) | Truthful, functional, beautiful, insightful, enlightening as five qualities; how readers get misled. | dataviz-canon DC-001 |
| **Jonathan Schwabish, Claus Wilke, Andy Kirk** | Chart catalogue, principled form choice, the design process context → data → editorial → design. | dataviz-canon DC-033, 038 |
| **Nick Desbarats** (Practical Reporting) | Display taxonomy (name which kind of display you build); why Good/Satisfactory/Poor bands and percent-deviation flags mislead. | dataviz-canon DC-017, 039 |
| **Steve Wexler, Jeffrey Shaffer, Andy Cotgreave, Amanda Makulec** (*The Big Book of Dashboards*, *Dashboards That Deliver*) | The broader dashboard definition and scenario-based critique. | dataviz-canon DC-017 |
| **Dona Wong** (*WSJ Guide to Information Graphics*) | Number formatting, scale and labeling rules for business charts. | dataviz-canon DC-036, 038 |
| **Lisa Charlotte Muth** ([Datawrapper](https://www.datawrapper.de/blog/)) | Grey as the most important color; emphasize with color; light-grey diverging midpoints. | dataviz-canon DC-037 |
| **William Cleveland & Robert McGill; Jeffrey Heer & Michael Bostock; Jock Mackinlay; Jacques Bertin; Colin Ware; Tamara Munzner & Matthew Brehmer; Ben Shneiderman** | The perceptual ranking of encodings and its replication; visual variables and pre-attentive attributes; the task typology; overview first, zoom and filter, details on demand. | dataviz-canon DC-010, 011, 015, 016 |
| **John Sweller** (Cognitive Load Theory) | Intrinsic, extraneous and germane load; the split-attention effect behind direct labeling. | dataviz-canon DC-012 |
| **Alper Sarikaya, Michael Correll, Lyn Bartram, Melanie Tory, Danyel Fisher; Benjamin Bach et al.** | The dashboard design space and genres (TVCG 2019); dashboard design patterns (TVCG 2023). | dataviz-canon DC-019 |
| **Scott Bateman et al.; Michelle Borkin et al.** | The memorability evidence that frames the chartjunk debate. | dataviz-canon DC-014 |
| **Jessica Hullman, Matthew Kay, Lace Padilla** | Uncertainty visualization: hypothetical outcome plots, the deterministic construal error, labeled bands. | dataviz-canon DC-020, audit B7 |
| **Robert Kaplan & David Norton** (Balanced Scorecard) | Outcomes balanced with drivers; leading and lagging indicators. | dataviz-canon DC-022 |
| **Richard Wang & Diane Strong** | Data quality as the consumer experiences it (intrinsic, contextual, representational, accessibility). | dataviz-canon DC-023, audit C3 |
| **IBCS Association** (Jürgen Faisst, Diego Berea et al.) and **ISO** | ISO 24896:2026 Notation for Business Reporting, which lifts the IBCS notation to an international standard. | dataviz-canon DC-037, §6 |
| **Kurt Buhler** ([SQLBI](https://www.sqlbi.com/) and [Data Goblins](https://data-goblins.com/)) *(canon adoption)* | The 3-30-300 rule; "useful before beautiful"; the Excel lift-and-shift failure mode; report-specific objects; the Copilot critique. | dataviz-canon DC-004, 016, 030, 054, 071 |
| **Marco Russo & Alberto Ferrari** ([SQLBI](https://www.sqlbi.com/)) *(canon adoption)* | Calculation-group precedence, dynamic format strings, the "shades of grey" stance on pie charts. | dataviz-canon DC-035, 056 |
| **Ruben Van de Voorde** ([Tabular Editor blog](https://tabulareditor.com/blog/)) | What "good" means in a Power BI report: time-to-insight, hidden states, self-filtering KPIs, the maintenance cost of elaborate cards. | dataviz-canon DC-031, 040, 051 |
| **Chris Webb** ([Crossjoin](https://blog.crossjoin.co.uk/)) | The 32,766-character text-value fact and the chunked-image workaround; Copilot AI-instruction practice. | dataviz-canon DC-053 |
| **Miguel Myers and the Power BI Core Visuals team** *(canon adoption)* | The core-visuals vision (new card, reference labels, button slicer) as the native path for KPI cards. | dataviz-canon DC-051 |
| **Benn Stancil; Simon Späti** | The "BI is dead" debate and its rebuttal: semantics and governance matter more under AI. | dataviz-canon DC-071 |
| **Gartner** | The analytics capability ladder (descriptive to prescriptive) used to classify page purpose. | dataviz-canon DC-018 |
| **Microsoft Learn authors** | Copilot limits and Prep-data-for-AI; implementation-planning test categories; RLS/OLS behavior with workspace roles. Round 6: 'Create report tooltips in Power BI' (any size, not interactive, not read by screen readers), which set the text-twin rule for every SVG in the package tooltip and the chips' alt texts. Round 10 (2026-11-11): 'Extend visuals with report page tooltips' (keep the page small, 320 x 240 as the reference, design at Actual Size, same theme as the report) and 'Visual tooltips in Power BI' (tooltip autoscale, "Tooltip size is affected by canvas size"), with the report definition schema's `useScaledTooltips`; together they set the 480 px tooltip pages and the scaled-tooltip setting of the opzet. | dataviz-canon DC-060, 061, 070; `opzet_report.py` (tooltip pages, `useScaledTooltips`) |


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
| **Leonxlnx** — [taste-skill](https://github.com/DogodaBjorn/taste-skill) *(third adoption, round 9, 2026-11-11)* | The production-test tells of section 9.F applied to the report's own copy: section-number eyebrows replaced by a statement plus the page name, the middle dot rationed to one per line, no micro-meta chains. Re-expressed in the copy rewrite; nothing copied. | MIT | `sketch_model.py` text measures, `opzet_report.py` (`EYEBROW`), round-9 SELF-REVIEW |
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

## Vendored skills in this project (PowerBI_Dataviz_WC27)

Copied verbatim into `.claude/skills/` on 2026-11-05 so the build runs with no
install step; each folder carries its source license. Manifest with commits:
`.claude/skills/VENDORED.md`.

| Skill folder | Source (fork of) | Author | License | Used for |
|---|---|---|---|---|
| `impeccable` | DogodaBjorn/impeccable @ 5e572c8 (upstream pbakaus/impeccable) | Paul Bakaus | Apache-2.0 | design, critique and polish of the stage-5 HTML comps and the pitch page |
| `design-taste-frontend` | DogodaBjorn/taste-skill @ e988add (upstream Leonxlnx/taste-skill) | Leonxlnx | MIT | anti-slop checks on comps; its consistency locks are already adapted in `design-hard-rules.md` |
| `humanizer` | DogodaBjorn/humanizer @ 523374d (upstream blader/humanizer) | Siqi Chen | MIT | AI-prose tells in report copy and the gallery post, beside `copy-polish` |
| `frontend-design`, `webapp-testing` | DogodaBjorn/skills_two @ b29e7cf (upstream anthropics/skills) | Anthropic | per folder LICENSE.txt | comp aesthetics; Playwright checks of comps and the Publish-to-Web render |
| `brainstorming`, `writing-plans`, `systematic-debugging`, `verification-before-completion` | DogodaBjorn/superpowers @ 3dcbd5c (upstream obra/superpowers) | Jesse Vincent | MIT | engineering discipline during DAX, pbiviz and projection work |

Contest material: dataset, starter file and brief by Microsoft Fabric Community,
Power BI Dataviz World Champs 2027 Round 1 (post by slindsay); Contest Advisory
Committee: Karin Szilágyi, Aanor Le Gouic, Taylor Amy, Santhana Lakshmi
Ponnurasan, Paulo Grijo. The starter model was decoded offline with
`pbixray` (MIT, Hugoberry) for the evidence pack.

### Report set-up (opzet) of 2026-11-06

| Who | What we owe them | Where it lands |
|---|---|---|
| **Microsoft** — [json-schemas](https://github.com/microsoft/json-schemas) (MIT) | The published PBIR schemas (page, visual container, visual configuration, semantic query, bookmark) that the generated report is validated against, read from the public mirror because developer.microsoft.com is not reachable here; the schema showed that `visualLink` sits in `visualContainerObjects` and that a TopN filter is an `In` over a subquery. | `project/tools/schema_check.py`, `project/tools/opzet_report.py` |
| **Julian Berman et al.** — [jsonschema](https://github.com/python-jsonschema/jsonschema) and referencing (MIT) | The validator behind `schema_check.py` (installed with pip, not vendored). | `project/tools/schema_check.py` |
| **Microsoft Fabric Community forum contributors** (threads on the Azure Maps visual and Publish to web, 2023-2024) | The reported limitation that Azure Maps does not render under Publish to web, which is why the geography is a native matrix. Community reports, not documentation: recorded as an open check. | `project-state/active/05-doorlichting-nieuwe-opzet.md` A11 |
| **Microsoft Playwright team** (Apache-2.0) | Headless Chromium for the comp capture, slot check and background rendering (the machine's install; the px-prototype pin is unchanged). | `project/tools/opzet_capture.mjs`, `opzet_backgrounds.mjs` |

### Brand kits for this project (goodnight-inn, goodnight-inn-hanger)

Both kits are original work (2026-11-06); these are the people and tools they
stand on. Re-derived in our own words; nothing copied.

| Who | What we owe them | Where it lands |
|---|---|---|
| **Jenni Romaniuk** (*Building Distinctive Brand Assets*; category entry points) | The test for assets that are unique, famous and ownable; thinking in the moments a traveller needs a bed. | goodnight-inn-hanger guide §2-3 |
| **Byron Sharp** (*How Brands Grow*) | Mental availability and distinctiveness over differentiation: why option 2 breaks the category's navy-and-gold code. | goodnight-inn-hanger guide §2-3, brand-options page |
| **Kevin Lane Keller** (customer-based brand equity) | The salience-performance-judgment-resonance ladder used to read the brand data. | goodnight-inn-hanger guide §2, promise scorecard |
| **Margaret Mark & Carol S. Pearson** (*The Hero and the Outlaw*) | The Everyman archetype as the brand's voice. | goodnight-inn-hanger guide §2 |
| **April Dunford** (*Obviously Awesome*) | Positioning by components: who it is for, category, unique value, proof. | goodnight-inn-hanger guide §2 |
| **Theodore Levitt** | Sell the outcome, not the product: the asleep-to-awake story. | goodnight-inn-hanger guide §2 |
| **Paul Rand; Chermayeff & Geismar & Haviv** (*Identify*) | Logo principles (simple, appropriate, distinctive; works small and in one color) and the tests run on both marks. | both guides, logo sections |
| **Vincent Connare** (Trebuchet MS), **Matthew Carter** (Verdana, Georgia) | Screen typefaces that ship with Windows and macOS. | both kits' typography |
| **Eben Sorkin** (Gelasio, OFL-1.1) | Georgia's metric twin, outlined in option 1's wordmark. | goodnight-inn assets |
| **Bonnie Shaver-Troup, Thomas Jockin et al.** (Lexend, OFL-1.1) | The lettering outlined in option 2's wordmark. | goodnight-inn-hanger assets |
| **Fontsource** (MIT packaging), **HarfBuzz** (Behdad Esfahbod et al., MIT), **fontTools** (Just van Rossum et al., MIT) | Font delivery, shaping and outlining for `project/tools/brand_logos.py`. | logo generator |

### Research-based rebuild (plan 09, applied on v3 in plan 11)

The KPI choices of the 9 November rebuild follow Björn's research note
`research/2026-11-09-brand-kpis-wat-echt-telt.md`. No figure from these
sources lands on the canvas; they argue for the form only (plan 09,
do-not-fabricate). Re-derived in our own words; nothing copied.

| Who | What we owe them | Where it lands |
|---|---|---|
| **Kantar BrandZ** (Meaningful Different framework) and the **IPA** (brand difference and pricing power) | Pricing power as the place where brand equity reaches the P&L. Applied as room-rate (ADR) growth since 2023 against the sister brands, after `project/analysis/42_price_index.py` showed a 2021 = 100 index measures the COVID recovery. | `project/tools/sketch_model.py` (`F1 Note (text)`, `adr_chg`), P1 F1 note |
| **Timothy L. Keiningham, Bruce Cooil, Lerzan Aksoy, Tor W. Andreassen, Jay Weiner** (*A Longitudinal Examination of Net Promoter and Firm Revenue Growth*, Journal of Marketing, 2007) | NPS predicts growth no better than satisfaction: NPS stays on P1 as an operational quality signal (KPI cell "Guest quality: net promoter score", F3), not as the brand's one number or a growth measure. | P1 KPI band label, F3, the footer line |
| **Thinkbox, Ebiquity, EssenceMediacom, Gain Theory, Mindshare, Wavemaker** (*Profit Ability 2*, 2024) | Business metrics over media metrics, and the marginal test: show why the next euro is not spent. | `Rec Held (text)` (the marginal clause), the footer line on P1 and P2 |
| **Andrew Ehrenberg, Gerald Goodhardt, Patrick Barwise** (Double Jeopardy, Journal of Marketing, 1990) and the **Ehrenberg-Bass Institute** | Growth through reach rather than loyalty, used only as a labelled reading of the data ("Our reading:"), never as a chart. | `F2 Note (text)` |

### Brand kit goodnight-inn-wakeup 3.1 (design rebuild, plan 10)

Original work (2026-11-08/09). The palette's three hex values come from a
reference Björn shared; everything else is drawn here. Re-derived in our own
words; nothing copied.

| Who | What we owe them | Where it lands |
|---|---|---|
| **@niki.aroca** (Instagram reel, shared by Björn on 2026-11-08) | The palette Oat Cream `#E9E5D6`, Coffee Blue `#2589D8`, Tangerine `#FF783D`, used as given. No layout, image or lettering from the reel or its posters is used. | `design/brand-kits/goodnight-inn-wakeup/brand.yaml` color block |
| **Tokotype** (Plus Jakarta Sans, OFL-1.1) | The lettering outlined in the 3.x wordmark "goodnight inn." | `assets/gi-*.svg`, `project/tools/brand_logos_v3.py` |
| **Microsoft** (Segoe UI) | The report typeface: Power BI's own default (Windows only; Mac fallback Arial). | kit typography |
| **Steve Matteson** (Open Sans, OFL-1.1) | Open stand-in for Segoe UI, embedded in the HTML comps so they render the same everywhere; never in the report. | `comps/*.html`, `project/tools/comps_v3.py` |
| **Gustavo M. Machado, Manuel M. Oliveira, Leandro A. F. Fernandes** (*A Physiologically-based Model for Simulation of Color Vision Deficiency*, IEEE TVCG 2009) | The simulation matrices behind the protan/deutan/tritan separation checks of the palette. | kit validation notes |
| **Fontsource** (MIT packaging), **HarfBuzz**, **fontTools**, **Microsoft Playwright team** (Apache-2.0), **NumPy** and **Pillow** (BSD, HPND) | Font delivery and outlining; comp and background rendering; the optional night-glow canvas. | `project/tools/brand_logos_v3.py`, `comps_v3.py`, `brand_canvas_v3.py` |
