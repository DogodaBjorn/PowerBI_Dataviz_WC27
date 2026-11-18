# scripts/prototype — px-prototype tooling

Playwright tools that turn an approved HTML design comp into build-ready
truth for stage 6 (px-prototype module):

| Tool | Output |
|---|---|
| `capture_references.mjs` | one exact-size **@2x PNG per screen** in `project/design-prototypes/reference_screenshots/` — the fidelity targets |
| `extract_layout.mjs` | `project/design-prototypes/layout.json` — exact getBoundingClientRect() rects, fonts, colors per element, in report-canvas coordinates |

## Setup — once per machine

```bash
cd scripts/prototype
npm install
npx playwright install chromium
```

`npm install` here once per machine; **`node_modules` is never committed**
(nor is `package-lock.json` churn part of any project deliverable). The
playwright version is pinned so rect measurements stay reproducible across
machines.

## Usage (from the repo root)

```bash
node scripts/prototype/capture_references.mjs project/design-prototypes/<comp>.html
node scripts/prototype/extract_layout.mjs   project/design-prototypes/<comp>.html
```

Both tools expect the comp convention: each screen is an element carrying
`data-screen-label`, sized exactly to its page canvas (1280x720 default;
tooltip pages at their own size). See
`.claude/skills/px-prototype/SKILL.md` for the full workflow and
`references/gotchas.md` for the hard-won pitfalls.

## Credit

Vendored and generalized from Bjorn's hp-world-champs pixel-perfect handoff
bundle (`design_handoff_powerbi/tools/`, MIT).
