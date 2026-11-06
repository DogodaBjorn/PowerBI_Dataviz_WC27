# 03 - Focus-swap proof: decisive PBIX test (go/no-go before stage 6)

**Date:** 2026-11-06 · **Status:** not yet executed - Power BI Desktop was not
available in the research environment. This is the gate that turns the method in
`02-focuswissel-methode.md` from decided to proven. Build it in a **separate
PBIX** (a copy of the model or a mechanics-only file); never in the submission
file. Synthetic fixture data is allowed here and only here.

## Setup

1. Copy the project PBIP, or create `focuswissel-proof.pbix` and load a fixture
   table `ProofPackages` (one row per package: PackageID, Capex, NPV per
   scenario, category, shortlist flag). The external proof pack's CSV and the
   Deneb/HTML samples are usable starting points; treat them as untested
   originals and never copy their data into the submission.
2. Add the P2 structure from `02-focuswissel-methode.md`: disconnected
   single-select package selector (slicer on a disconnected table), one scatter
   (X capex, Y NPV, one point per package), right panel in two states
   (shortlist, plan details + waterfall), scenario slicer on the disconnected
   `Scenario` table.
3. Create the two display bookmarks: Data **off**, Display **on**, Current page
   **off**, **Selected visuals** only; the package selector stays outside the
   selected visuals.

## Tests and go/no-go

| # | Test | Go when |
|---|---|---|
| 1 | Selector persistence: pick a package, swap layout, swap back | the choice still drives highlight and panel |
| 2 | Scatter completeness: with a package chosen | all packages stay visible (no cross-filter to one point) and the chosen point is clearly highlighted |
| 3 | Panel consistency: open the plan state | details and waterfall show the same package; totals reconcile with the package table for all three scenarios |
| 4 | Click behaviour: click a scatter point, then swap layouts | record what happens (expected: the cross-selection clears); decide slicer-only or click-plus-slicer from the result |
| 5 | Route B spike (optional): Deneb scatter with `__selected__` opacity and cross-filtering exposure enabled | document redraw vs data-patch behaviour and render speed at 456 points |
| 6 | Route C extra (optional): Secure HTML `<details>` detail card | renders sanitized, works without scripts |
| 7 | Publish-to-Web: open the file's P2W link incognito at 1920x1080 and 1366 width; export PDF/PPT of both states | both states render and export acceptably (static is expected) |

Rule: 1-3 green means the native method holds and stage 6 builds it. Any red is
fixed inside the native route first; route B is considered only if the fix costs
more than the Deneb risk. Animation is never a requirement.

## After the test

Record the outcome in this file (date, Desktop build, what passed), update
`status.yaml`, and only then commit the P2 build at stage 6.
