# design-critique scoring reference

Rubrics for both jobs. G5 rates *directions* (0-10, seven passes); G6 rates
the *built report* (0-4, ten dimensions, /40). Adapted to Power BI from
gstack plan-design-review / design-review (MIT) and impeccable's critique
health score (Apache-2.0) — see CREDITS.md.

## G5 — the seven passes (0-10 per direction)

Score each direction on every pass. Pattern per pass: score → one line on
the gap → what would close it. Never skip a pass because a direction "is
obviously fine there"; a pass with no findings gets a score and "no issues".

1. **Reading path.** First, second, and third read of the page.
   *A 10:* the 3-second message lands unaided; the 3-minute trust path is
   walkable (labels, comparisons, definitions in reach); the worst page —
   the Detail table — still looks composed, not just the hero.
2. **State coverage.** Include no-data and all-slicers-cleared.
   *A 10:* empty results, cleared slicers, and longest-real-category-name
   states are designed appearances the comp accounts for, not accidents the
   operator will discover.
3. **Slop risk.** The category's lazy defaults (`design/report-craft-floor.md`
   Refuse list).
   *A 10:* nothing on the page could be swapped into a generic SaaS
   dashboard unnoticed — no uniform KPI-card wall, no icon-in-circle
   headers, no decoration carrying zero data.
4. **Brand alignment.**
   *A 10:* every color, type, and chrome choice traces to a brand-kit token
   or a cited design-intelligence hit, and a reader who knows the client
   says "that's ours" before reading a number.
5. **Accessibility.**
   *A 10:* every pair ≥ 4.5:1 (large text/non-text ≥ 3:1), color never the
   only meaning carrier, fonts are Power BI-safe with realistic fallbacks,
   tab and reading order follow the layout.
6. **Dial fit.** Declared `DENSITY` / `VARIANCE` vs the comp's actual
   behavior.
   *A 10:* the measured feel matches the declaration — an "airy" claim is
   not hiding a cramped grid, "strict" variance is not leaking one-off
   styles.
7. **Signature-moment strength.**
   *A 10:* the element a reader would describe to a colleague exists, is
   mapped to a buildable medium in the asset-fidelity inventory, and is the
   direction's own — not a borrowed trope with the client's accent color.

Calibration: 8+ = minor notes only; 5-7 = presentable with named gaps;
below 5 = rework the direction before showing the user (a weak third
direction is fake divergence).

### Unresolved-decisions table

```
DECISION NEEDED                  | IF DEFERRED, WHAT HAPPENS
---------------------------------|--------------------------------
Empty-state look on Detail page? | Operator ships a blank canvas
Mobile layout for Overview?      | Desktop layout squeezed, unread
```

Empty, or every row user-acknowledged in writing, before G5 closes.
Acknowledged rows carry into the design handoff as accepted risks.

## G6 — the ten fidelity dimensions (0-4 each, /40)

Anchors: 0 = absent or contradicts the handoff · 2 = partially per handoff,
drift visible · 4 = indistinguishable from the contract. Honest scoring:
most first builds land 24-32.

| # | Dimension | 4 means |
|---|-----------|---------|
| 1 | Layout fidelity | rects/grid per handoff; px-prototype: verbatim `layout.json` positions |
| 2 | Theme & tokens | theme registered/applied; token values match the design brief |
| 3 | Typography | sizes, weights, tabular numerals per handoff and craft floor |
| 4 | Chrome consistency | `z_*` identical across pages; consistency locks (hard rules 7-9) hold |
| 5 | Visual properties | every visual's explicit properties match its handoff row |
| 6 | Polish moves | each listed dataviz-polish move present and working |
| 7 | Copy | copy-polish clean; insight titles state findings, not topics |
| 8 | Accessibility | contrast green, color never alone, alt text, tab order |
| 9 | States | no-data, cleared slicers, longest labels ship as designed |
| 10 | Signature & craft | signature moment survived the build; Verify list green, no Refuse pattern |

Bands: **36-40** ship · **30-35** fix high + medium first · **< 30** the
build is not the design — drain the fix queue, then re-score before the gate
reopens.

### Triage → severity mapping

- **high** — breaks the first impression, reader trust, or a contract →
  review-finding severity `blocker`/`major`
- **medium** — felt subconsciously, dulls polish → `major`/`minor`
- **polish** — separates good from great → `minor`/`polish`

Findings unfixable from PBIR source (needs Desktop, client copy, source
data) are triaged normally but marked deferred in the review-finding note
and the BUILD_LOG manual-steps checklist.

## fix-tasks.jsonl

Path: `project/project-state/fix-tasks.jsonl`. One JSON object per line,
one line per open finding, written at synthesis time, ordered high → medium
→ polish. Fields (all required):

```json
{"id": "F-001", "priority": "high", "page": "Overview",
 "finding": "Hero KPI at x=312 not x=320 - breaks 8px grid and comp rect",
 "verify": "python scripts/validate_json.py project/pbip/Report/definition/pages/Overview/visuals/kpi_hero/visual.json"}
```

- `id` matches the review-finding `finding_id`; the contract stays the
  human record — resolution status lives there, not here.
- `finding` is one line, observed → expected.
- `verify` is the exact command (or named check, e.g. "±2px diff of
  kpi_hero vs layout.json") that proves the fix.

`pbir-operator` works the file top-down: one line = one single-concern diff,
run `verify` plus the standard hooks, update the matching review-finding
`resolution`, next line. Never batch lines into one diff.
