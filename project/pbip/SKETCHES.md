# Direction sketches (first pass, 2026-11-06)

Three separate reports on one shared semantic model, one per creative direction from
`project/PITCH-goodnight-inn-directions.md`. They are **sketches**: layout, bindings
and copy follow the pitch, every number is derived in the model, nothing is pixel-
fitted yet. Stage 5 (comps, critique, convergence) and stage 6 (fidelity build) still
follow once a direction is chosen.

| File | Direction | Pages |
|---|---|---|
| `D1-wake-up-call.pbip` | D1 Wake-up call, the Board briefing (paper, navy ink, amber) | p1 Wake-up call · p2 The morning plan |
| `D2-fifty-keys.pbip` | D2 Fifty keys, the night-desk wall (navy, amber lights) | p1 The wall tonight · p2 The wall in 2032 |
| `D3-two-futures.pbip` | D3 Two futures, the ledger (cream, ink, mono figures) | p1 2032 if we do nothing · p2 2032 with the plan |
| `PillowKey.SemanticModel/` | Shared model (TMDL): the organisers' 16 tables + `_Measures`, `ProjectCashflow`, `HotelOutlook`, helper tables | |

## Regenerate

```
python project/tools/sketch_model.py      # model
python project/tools/sketch_reports.py    # the three reports (overwrites the .Report folders)
powerbi-report-author validate project/pbip/D1-wake-up-call.Report
python scripts/pbir_detect.py
```

The generators are the source of truth for this pass; edit them, not the JSON. Once a
direction is chosen, the chosen report moves into the normal pbir-operator flow and
the generator for it is retired.

## Opening

Open a `.pbip` in Power BI Desktop (Store build 2.159). The model loads from the
organisers' public blob through the `DataFile` parameter; the first open needs a
refresh: **Home > Refresh**, answer the "Webinhoud openen" dialog with Verbinden
(anonymous access), about 12 minutes on the first run. Each report opens its own copy of
the model, so refresh once per report you open (nothing is saved to `.pbi/cache.abf`
until you save in Desktop).

Headless alternative used for this pass (no EULA, no Modeling MCP):

```
powershell -ExecutionPolicy Bypass -File project\tools\refresh_desktop_model.ps1 -Port <AS port>
powershell -ExecutionPolicy Bypass -File project\tools\sync_measures_to_desktop.ps1 -Port <AS port>
powerbi-desktop reload --pid <Desktop pid>; powerbi-desktop screenshot <page id> --pid <pid> --output x.png
```

The refresh script finds the port itself when one Desktop is open; `sync_measures` pushes
the `_Measures` TMDL into the live model so a measure edit does not need a reopen.

## Verified 2026-11-06 (Desktop 2.159, Publish-to-Web not yet tested)

All six pages render with live data; the mission's headline numbers re-derive in the
model: occupancy 79.4 %, RevPAR $84.80, GOP margin 44.4 % (33.7 % after distribution),
NPS +3.3, OTA share 50.0 %, distribution cost $22.7 M ($4.8 M above the 2021 mix), the
folio $109.31 / keep $89.64 vs $111.56 / keep $107.09, plan A $51.3 M on six projects,
run-rate +$7.6 M, NPV at 8 % −$29.5 M, payback after 2032, baseline margin 44.4 % → 41.7 %,
capacity wall Toronto 2028, Kuala Lumpur and Montréal 2029, Gatwick 2030.

Known sketch gaps (stage-5/6 work, not bugs): the wall (D2) scrolls at 720 px, legends
truncate channel names, the D1 KPI delta line clips, the D2 capacity wall is eight lines
in one chart rather than small multiples, the departures board shows only the selected
projects (no "not funded" rows), the year stepper and plan builder are plain slicers.

Lessons that cost time, kept for stage 4: `InvestmentProjects -> Brands` plus
`InvestmentProjectProperties -> Hotels` makes an ambiguous path (dropped the former; pages
filter `InvestmentProjects[Brand]`); a calculated table that uses CALCULATE and has a
relationship back to the tables it reads is a circular dependency in Desktop (both
calculated tables are written with FILTER / SUMX / LOOKUPVALUE only); `start` and `scope`
are reserved words in DAX variable names; cards and data labels must use display units
"None" when the format string already scales to millions.

## Model notes (hypotheses re-derived, not typed in)

- `ProjectCashflow`: project × scenario × month 2027-2032. Capex phased evenly over the
  duration, disruption = RoomsOutOfServicePct × the mapped hotels' 2025 revenue per month
  during works (brand-wide projects map to the whole brand), benefit = annual operating
  profit impact / 12 × ramp 50 / 85 / 100 percent after go-live. Ramp, horizon and
  discount rate are read from `FinanceParameters`.
- `HotelOutlook`: hotel × year 2025-2032 do-nothing projection from `FinanceAssumptions`
  (regional demand, ADR and cost inflation), demand capped at 97 percent occupancy.
  Scenario logic, labeled as such on every visual that uses it.
- Scenario toggle: the disconnected `Scenario` table drives the measures through a
  column filter on `ProjectCashflow[Scenario]`; Expected when nothing is selected.
- Plan builder: a slicer on `InvestmentProjects[Short Name]`, pre-selected to the six
  recommended projects; `Plan Valid (text)` prints the contest constraints.
- Open points for stage 2 contracts: whether `AnnualRunningCostUSD` is already inside the
  organisers' operating-profit impact (assumed yes, per the mission); disruption on total
  revenue with no cost relief (conservative).
