# Vendored third-party skills

Copied into this project on 2026-11-05 so Claude Code finds them with no install
step. They sit beside the atelier's own skills; the atelier's rules and gates still
apply when they are used. Each folder keeps its source license. Update by copying the
folder again from the source repository and bumping the commit here.

| Folder | Source repository (fork → upstream) | Commit | License | Why it is here |
|---|---|---|---|---|
| `impeccable/` | DogodaBjorn/impeccable → pbakaus/impeccable | 5e572c8 (2026-07-26) | Apache-2.0 (`LICENSE.impeccable`, `NOTICE.impeccable.md`) | `/impeccable critique`, `polish`, `audit` on the stage-5 HTML comps and the pitch page. Its scripts expect Node; the markdown guidance works without them. |
| `design-taste-frontend/` | DogodaBjorn/taste-skill → Leonxlnx/taste-skill | e988add (2026-07-23) | MIT (`LICENSE.taste-skill`) | Anti-slop pre-flight on comps. Its consistency locks are already adapted into `.claude/rules/design-hard-rules.md` (rules 7–9). |
| `humanizer/` | DogodaBjorn/humanizer → blader/humanizer | 523374d (2026-07-21) | MIT (`LICENSE`) | AI-prose tells in report copy, tooltips and the Contests Gallery post; complements the atelier's `copy-polish`. |
| `frontend-design/` | DogodaBjorn/skills_two → anthropics/skills | b29e7cf (2026-07-24) | see `LICENSE.txt` in folder | Distinctive, non-templated aesthetics for the three direction comps. |
| `webapp-testing/` | DogodaBjorn/skills_two → anthropics/skills | b29e7cf (2026-07-24) | see `LICENSE.txt` in folder | Playwright checks of comps and of the Publish-to-Web render at stage 7. |
| `brainstorming/` | DogodaBjorn/superpowers → obra/superpowers | 3dcbd5c (2026-07-23) | MIT (`LICENSE.superpowers`) | Divergent exploration before stage 5 converges. |
| `writing-plans/` | same | 3dcbd5c | MIT | Plans for the pbiviz or Deneb build if the §6 gate opens. |
| `systematic-debugging/` | same | 3dcbd5c | MIT | DAX, projection-table and custom-visual defects. |
| `verification-before-completion/` | same | 3dcbd5c | MIT | Evidence before any gate is declared closed. |

Not vendored, by decision:

- **ui-ux-pro-max** — already inside the atelier as `design/intelligence/` (same author,
  MIT); refresh its `data/` from the source repo if the search feels stale.
- **gstack** — needs a bun build and a global install (`./setup`); use it from
  `~/.claude/skills/gstack/` if wanted (its `/qa`, `/design-review`, `/browse`).
- caveman, i-have-adhd, graphify, hyperframes, remotion skills, marketing and
  social-media skills — not relevant to this build.
- Microsoft's `powerbi-authoring` plugin and the Modeling MCP — installed at user
  scope, used through the atelier's `ms-authoring` adapter (see `DEPENDENCIES.md`).
