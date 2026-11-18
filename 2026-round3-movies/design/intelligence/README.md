# Design intelligence — query-only lookup layer

BM25 search over curated design-knowledge CSVs. Vendored from
**ui-ux-pro-max** by Next Level Builder (MIT) — repo `ui-ux-pro-max-skill`,
see CREDITS.md. Local changes: `DATA_DIR` in `core.py` points at the
sibling `data/` folder; only five CSVs are vendored.

**Query-only data.** These CSVs are lookup tables, never context. Run a
search, read the 1-3 hits, close the file. Never load a CSV wholesale into
context, never paste more rows than the query returned.

## Files

| File | Holds | Domain flag |
|---|---|---|
| `search.py` | CLI entry point | — |
| `core.py` | BM25 engine + domain config | — |
| `design_system.py` | `--design-system` aggregator (partial here, see below) | — |
| `data/charts.csv` | 25 chart forms: when to use, when NOT, a11y notes | `chart` |
| `data/colors.csv` | Semantic palettes per product type (hex roles + notes) | `color` |
| `data/typography.csv` | Font pairings: mood, best-for, Google Fonts refs | `typography` |
| `data/styles.csv` | ~100 UI styles: keywords, effects, do/don't, checklists | `style` |
| `data/ui-reasoning.csv` | Pattern/anti-pattern decision rules per product category | (used by `--design-system` only) |

## Query commands (run from the pbi-atelier root)

```bash
python design/intelligence/search.py "executive dashboard" --domain chart
python design/intelligence/search.py "fintech" --domain color
python design/intelligence/search.py "professional corporate" --domain typography
python design/intelligence/search.py "minimal dashboard" --domain style
python design/intelligence/search.py "<query>"              # auto-detect domain
python design/intelligence/search.py "<query>" -n 5 --full  # more hits, untruncated
```

Only the four domains above are vendored; any other `--domain` (or
`--stack`) answers "File not found" — that is expected, not a defect.
`--design-system` runs but skips domains whose CSVs are absent
(fonts/motion/landing); prefer single-domain queries here anyway — palette
and type decisions belong to the brand kit, not this tool.

## Power BI caveats

Results speak web (CSS, Chart.js, hover states). Translate, don't obey:

- Chart picks route through `design/visual-selection.md` and
  `design/chart-selection.csv` (the Power BI adaptation of `charts.csv`
  with `pbi_native`/`deneb` columns) — not the web library column.
- Hex values are inspiration only; tokens come from the active brand kit
  and must pass `python scripts/check_contrast.py`.
- Anything violating `.claude/rules/design-hard-rules.md` or
  `design/report-craft-floor.md` loses, whatever the CSV says.
