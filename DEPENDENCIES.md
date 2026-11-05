# Dependencies

pbi-atelier vendors **no** third-party code or documentation, with one deliberate
exception: the MIT-licensed design-intelligence search tooling under
`design/intelligence/` (see CREDITS.md — Next Level Builder). It runs on the Python
stdlib alone and needs no install. Everything below is an external tool you install
yourself. Adapter skills check presence and version at use time and degrade
gracefully when a tool is absent.

## Pinned dependencies

| Dependency | Pin | Role | License |
|---|---|---|---|
| Python | ≥ 3.11 | `scripts/` validators, hooks' JSON parsing, and the vendored `design/intelligence/` search tooling. Stdlib only — no pip installs required. | PSF |
| `pbir-cli` (PyPI) | `== 0.9.25` | Headless PBIR report authoring, driven via the `pbir-cli` adapter skill. | **Custom Non-Commercial — read below** |
| Microsoft powerbi-authoring plugin | **installed 2026-08-04**: `powerbi-authoring@fabric-collection` v0.3.10, user scope (`claude plugin install powerbi-authoring@fabric-collection`); Modeling MCP auto-registered as `npx @microsoft/powerbi-modeling-mcp@latest`; reference clone at `E:\Claude Repositories\skills-for-fabric` @ `28f29ab` | Official agentic authoring surface (five skills + Power BI Modeling MCP, Node ≥ 18 + Desktop Bridge), via the `ms-authoring` adapter skill. Preferred execution/verification layer when installed: headless DAX checks at G7, rendered-screenshot evidence for fidelity review. | Microsoft terms (skills-for-fabric repo: MIT) |
| Figma MCP + figma-use skill suite | optional; session-level | Client-review frames and design explorations, via the `fg-figma` module. Detected at use time; degrades to the HTML-comp path when absent. | Figma terms |

Installed state on this machine (2026-08-04): `scripts/prototype` has `npm install`
done with Chromium fetched (`npx playwright install chromium`); `GEMINI_CONFIG_PATH`
is set user-wide to the existing key file at
`E:\TrainerBjornOps\secrets\google-api-config.json` (key resolution smoke-tested).
| Node.js + `pbiviz` | ≥ 20 / latest | Only if the `custom-visual-studio` module is enabled. Never commit `node_modules`. | MIT |
| Node.js + Playwright | ≥ 18 / `playwright == 1.61.1` (pinned in `scripts/prototype/package.json`) | Optional — only if the `px-prototype` module is enabled. Run `npm install` once per machine inside `scripts/prototype/`; `node_modules` is never committed. | Apache-2.0 (Playwright) |
| Google Gemini image API (`GEMINI_API_KEY`) | model `gemini-2.5-flash-image` | Optional — only if the `imagery-studio` module is enabled (`im-imagery` skill, `scripts/imagery/render_image.mjs`; Node ≥ 18, zero npm dependencies). Key resolves via `--config` JSON → `GEMINI_CONFIG_PATH` → `GEMINI_API_KEY`; with no key the renderer exits 2 and the skill degrades gracefully to canvas-studio chrome. See `modules/imagery-studio/README.md`. | Google API terms |
| Power BI Desktop | current monthly | Rendered review; the small set of steps that cannot be done headlessly (tracked per-project in BUILD_LOG). | Microsoft terms |

Install `pbir`:

```bash
uv tool install pbir-cli==0.9.25
# or: pip install pbir-cli==0.9.25
pbir --version
```

Update the pin deliberately: bump the version here, re-run a project validation
sweep, and note breaking changes. The `pbir-cli` adapter skill reads this file's pin
and warns on mismatch.

## The pbir license — read before client work

`pbir` (by Kurt Buhler and Maxim Anatsko) ships under a **Custom Non-Commercial
License**. As of the pinned version it states, among other things, that:

- commercial purposes include *"using the Software to provide paid consulting or
  development services"*, and
- creation of derivative works is forbidden without the authors' consent.

Consequences for this repository and its users:

1. **This repo contains zero pbir code or documentation** — only references to the
   tool and our own usage conventions. The repo itself is therefore cleanly
   MIT-licensed and shareable.
2. **If you use `pbir` in paid client work, obtain written permission from its
   authors first** (the license invites commercial licensing inquiries), or work
   without it: the `pbir-authoring` skill documents the direct-JSON-editing
   fallback, which produces identical artifacts.
3. If you fork or share this template, these terms travel with you — point your
   users at this file.

## Version provenance

Projects instantiated from this template record `TEMPLATE_VERSION` in
`project/project.yaml`. When the template evolves, that field tells you which
migration notes apply.
