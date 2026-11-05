---
name: validate-project
description: Run the full pbi-atelier validation sweep (JSON, TMDL strict, state machine, contrast, naming, pbir validate when available) and interpret the failures. Use at stage gates 4/6/7, before commits of pbip changes, and whenever the user asks "is everything valid".
---

# validate-project

The integrated sweep. Hooks validate per-file on write; this skill validates
the whole, in order of cheapest-first:

## The sweep

1. **State:** `python scripts/check_state.py` — stage/gate consistency.
2. **JSON:** `python scripts/validate_json.py` — repo-wide well-formedness
   (includes `project/deliverables/theme.json`).
3. **Contrast (core, no module needed):** `python scripts/check_contrast.py`
   — WCAG thresholds on the standard token pairs; auto-resolves
   `theme.json` → active brand kit → neutral defaults, exits 1 on any
   failing pair. Quote its printed pair table verbatim as gate evidence —
   contrast is measured, not asserted. The deeper a11y checks (alt text,
   tab order, color-never-alone) stay in `ax-audit` (a11y-studio module).
4. **TMDL:** `python scripts/validate_tmdl.py --strict` — errors *and*
   warnings (docstrings, displayFolder, formatString) must be clean at gates.
5. **Inventory:** `python scripts/tmdl_inventory.py project/pbip` — regenerate
   and diff against the blueprint (stage ≥ 4).
6. **Naming:** grep the report tree for violations — visual/page folders not
   matching `design/naming-conventions.md` prefixes, and any Desktop-style
   32-hex-char ids.
7. **Taste-lint (gate-blocking at G6/G7):**
   `python scripts/pbir_detect.py project/pbip` — deterministic checks of the
   craft floor and consistency locks against the PBIR source (accent lock,
   radius system, 8px grid, dash/emoji tells, kicker repeats, theme color
   drift, flat type hierarchy, literal text-on-fill contrast). Honors the
   waiver file `project/project-state/pbir-detect-waivers.yaml`; every waiver
   needs a reason, unwaived findings exit 1 and fail the gate. Quote the
   summary line as gate evidence. (The PostToolUse hook runs the same
   detector warn-only on pbip writes — mid-build noise never blocks; only
   this sweep does.)
8. **Tool validation:** if the pbir CLI is present, `pbir validate` on the
   report (per the `pbir-cli` adapter).

## Interpreting failures

- Fix causes, not symptoms: a TMDL space-indent error usually means a
  copy-paste from a non-TMDL source — re-check the whole block, not the line.
- An inventory-vs-blueprint diff is a *decision point*: either the build is
  wrong (fix it) or the blueprint is stale (update it via its stage, with the
  user).
- Machine-path errors: introduce/extend the source parameter, never "fix" by
  editing the path to a different literal.
- Never silence a validator (deleting checks, loosening globs) — that is a
  governance change only the user makes in the template repo.

## Reporting

Summarize per layer: pass/fail + the first actionable failure each. At
gates, paste the summary into the stage's numbered file as evidence.
