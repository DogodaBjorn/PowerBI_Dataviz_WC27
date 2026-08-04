# Tech radar

Living record of techniques, tools, and patterns assessed for this toolkit.
Rings: **adopted** (in the repo) · **trial** (in, unproven on a real
project) · **assess** (promising, not built) · **hold** (deliberately not,
with reason). Maintained by `/scout` runs and stage-7 retrospectives.

Last updated: 2026-08-04 (toolkit-integration sweep: Claude Repositories + TrainerBjornOps + Microsoft agentic stack absorbed).

## Adopted

| Item | Owner in repo | Since |
|---|---|---|
| Button-slicer UI patterns (segmented/tabs/toggle/KPI cards/image items) | nav-studio | v0.2.0 |
| Functional SVG icons + state variants | icon-studio | v0.2.0 |
| SVG-in-DAX dynamic marks | icon-studio guide; reused by table-studio | v0.2.0 |
| Brand kit → theme + hard-rule tokens compilation | theme-from-brand-kit (core) | v0.1.0 |
| Insight titles, semantic color, focal-contrast polish moves | dataviz-polish (core) | v0.1.0 |

## Trial (implemented v0.3.0 — first real project use decides)

| Item | Owner in repo | Watch for |
|---|---|---|
| Deneb/Vega-Lite bespoke visuals with token-injected specs | deneb-studio | spec maintenance cost; Deneb/Vega-Lite version churn |
| Premium table architecture + in-cell micro-viz | table-studio | native cell-elements surface evolving |
| Report-page tooltip patterns (mini-trend, trust, breakdown) | tooltip-studio | headless tooltip-assignment support in PBIR |
| Wireframe-first SVG page backgrounds | canvas-studio | background-image format support; regeneration discipline |
| Scripted WCAG contrast gate + audit checklist | a11y-studio + scripts/check_contrast.py | alt-text/tab-order property surface in PBIR |
| HTML-comp → pixel-perfect PBIR pipeline (rects verbatim, ±2px) | px-prototype + scripts/prototype/ | comp-vs-rendered divergence; Playwright/Node churn |
| Design-intelligence queries at s5 (palettes/typography/charts/styles) | design/intelligence/ + chart-selection.csv | data staleness vs Power BI visual evolution |
| Deterministic PBIR taste-lint with waivers | scripts/pbir_detect.py (G6/G7 gate, warn-only hook) | false-positive rate on legitimate showpiece layouts |
| Scored dual-isolated fidelity review + fix queue | design-critique + fix-tasks.jsonl | scoring overhead vs value on small reports |
| Report-copy AI-tell sweep (NL + EN) | copy-polish | Dutch tell list needs growth from real projects |
| Generative on-brand imagery for report chrome | imagery-studio (im-imagery) | Gemini output consistency; anchor quality per brand |
| Figma as optional client-review/exploration surface | fg-figma | Figma MCP availability per session; sync discipline |
| Per-client learnings memory (taste, decisions, pitfalls) | scripts/learnings.py + stage hooks in s2/s5/s7 | entry quality; whether skills actually consult it |
| Skill authoring/regression discipline | skill-forge | first real forge cycle still to run |
| Starter brand kits + PBI-safe font pairings for no-brand clients | design/brand-kits/starter-*/ + _font-pairings.md | client reception; palette-to-industry fit |

## Assess (natural /scout subjects)

| Item | Why interesting | Note |
|---|---|---|
| New card visual reference labels & collage layouts | native modern KPI cards (GA Nov 2025), still evolving fast | fold into dataviz-polish/table-studio when the surface stabilizes |
| Light/dark report variants | reader-environment fit | extension of theme-from-brand-kit, not a module |
| Mobile canvas layouts | underserved delivery surface | needs a real project demand first |
| backend-stories (PBIP DAX/M → backend user stories) | reverse-engineering add-on | carried from v0.1.0 future-ideas |
| fabric-deploy (deployment pipelines / Fabric CLI adapter) | delivery automation with safety hooks | deploys stay user-run regardless |
| dx-profile (source profiling at s1 + independent cross-foot workbook recomputing top KPIs outside DAX at s7) | evidence over hearsay in requirements AND in delivery | absorbs the v0.1.0 data-profiler idea; doctrine available in Anthropic's xlsx skill (skills_two) |
| Headless DAX validation of metric contracts at G7 | expected-vs-observed per contract, scripted instead of manual Desktop checks | **available now** via Power BI Modeling MCP (ms-authoring); wire when the plugin is installed |
| Rendered-pixel evidence for fidelity review and s7 | closes "the agent cannot see pixels" with real pixels, not the HTML proxy | **available now** via Desktop Bridge screenshots (ms-authoring); alternative: REST export-to-file on Pro/Fabric |
| cr-express post-delivery change lane | one-line mini-contract → single-concern diff → pbir_detect + targeted validation | keeps the audit trail without full-ceremony reopening |
| Report-takeover / redesign flow (audit-first, keep/retire inventory, modernisation levers) | most common consulting scenario; also the migration path for the three legacy client repos (KlantenKPI, KTO MVP, RecruitmentHub) | pattern in taste-skill §11 + impeccable document/extract |
| Parallel per-page PBIR builds (task-brief per page, progress ledger) | PBIR pages are separate folders — conflict-free fan-out; evening instead of a week on 7-page builds | pattern in superpowers subagent-driven-development |
| Deneb preview harness (render Vega-Lite specs to PNG pre-Desktop) | visual iteration for the one fully-controlled visual type | vl-convert or Playwright page; cheap once px-prototype's Node footprint exists |
| Monthly release-radar automation (PBIR/TMDL/Deneb schema churn) | research-first rule's fastest-aging knowledge | pattern in last30days-skill (keyless Reddit/HN/GitHub) |

## Hold

| Item | Reason |
|---|---|
| Glassmorphism / gradient-heavy styling | conflicts with the design doctrine's restraint principle and the hard-rules forbidden list; revisit only if the doctrine changes |
| Persona-pack module | stage-1 audience/decision mapping already covers the need |
| Performance-tooling module | real subject, different skillset (model/DAX perf, not UI/UX); reconsider as its own track |
| Hand-rolled DAX bar-charts-in-SVG beyond simple marks | maintenance trap; real charts belong in visuals (icon-studio guide draws the line) |
