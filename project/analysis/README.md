# Evidence pipeline

Every number in `MISSION-goodnight-inn.md`, `SCOUT-pillowkey-round1.md` and
`PITCH-goodnight-inn-directions.md` comes from these scripts, run against the
organisers' starter file. They are the provenance of the evidence pack, not the
report's source of truth: the semantic model re-derives everything at stage 4.

Requirements: Python ≥ 3.11, `pip install -r requirements.txt` (pandas, pyarrow,
pbixray, numpy). Since 6 Nov the parquet folder can also come straight from the
workbook (`PillowKey_Dataset.xlsx`, one parquet per sheet, `Contents` kept as CSV):
the crosscheck output reproduces identically from either source. Run scripts with `python -I` and pass paths as arguments.

| Script | Reads | Produces |
|---|---|---|
| `01_dump_model.py <pbix>` | starter `.pbix` | tables, schema, relationships, Power Query, parameters (`output/model_dump.txt`) |
| `02_export_tables.py <pbix> <outdir>` | starter `.pbix` | one parquet per table in `<outdir>` (the input of everything below; not committed) |
| `03_starter_report_text.py <Report/definition>` | unzipped starter report | the starter's hidden Read Me and Judging Criteria pages as text |
| `10_reference_tables.py <data>` | parquet | brands, finance parameters and assumptions, hotel portfolio |
| `11_brand_kpis.py <data>` | parquet | brand × year KPIs, guest scores (weighted), complaints, channels, segments, integrity checks (`output/perf.txt`) |
| `12_projects.py <data>` | parquet | the 40 projects with hotels, scenarios, constraints (`output/proj.txt`) |
| `13_scenario_reconciliation.py <data>` | parquet | reproduces the scenario revenue impacts from their drivers |
| `14_hotel_level.py <data>` | parquet | per-hotel KPIs, renovation effects, seasonality by brand (`output/hotels.txt`) |
| `15_portfolio_search.py <data>` | parquet | brute-force budget-feasible portfolios per brand with NPV through 2032 |
| `16_hypothesis_checks.py <data>` | parquet | renovation natural experiment, resort-type seasonality, capacity signals |
| `20_goodnight_inn_deep_dive.py <data>` | parquet | the Goodnight Inn evidence pack: channels in dollars, project hotels, 2021 cohort, per-project economics, candidate plans (`output/gi.txt`) |
| `21_baseline_projection.py <data>` | parquet | do-nothing 2026–2032 from FinanceAssumptions, capacity wall |
| `22_column_codex.py <data>` | parquet | every column of every table with ranges and distinct values (`output/codex.txt`) |
| `30_pitch_data.py <data> <json>` + `31_baseline_bridge.py <data> <json>` | parquet | the JSON behind `deliverables/pitch/goodnight-inn-three-ways.html` |
| `40_package_matrix.py <data> <outdir> [--annual]` | parquet | the P2 package matrix: 456 valid Goodnight Inn packages, NPV / run-rate per scenario, presets A/B/C per lens, sensitivity (`output/packages.txt`, `packages.csv`, `project_economics.csv`, `project_yearly.csv`); monthly discounting by default (04-p2-build-method) |
| `41_opzet_facts.py <data> <packages.csv> <project_economics.csv> <json>` | parquet + 40's output | the facts behind the opzet comp: four-brand comparison and ranks, geography, refresh ages, P2 projects (`output/opzet_facts.txt`, `design-prototypes/opzet-data.json`) |
| `17_crosscheck_dutch_review.py <data>` | parquet | verification of the Dutch data review of 4 Nov 2026: margins after distribution, per-hotel trends, comfort vs renovation age, complaint momentum, renovation spend per brand, sister event study, NPV conventions (`output/crosscheck.txt`) |
| `tools/extract_mht.py` | the saved blog page | the contest brief as text and its links (`project/contest/`) |

Modelling choices baked into the quick economics (to be decided properly in the
stage-2 metric contracts): earliest start for every project; capex phased evenly;
rooms out of service lose their full share of the property's 2025 revenue with no
cost relief; ramp-up 50 / 85 / 100 %; 8 % discount to 2026; no terminal value;
portfolio Low/High = sum of each project's Low/High.
