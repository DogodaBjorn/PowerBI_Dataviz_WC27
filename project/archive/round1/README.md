# Round 1 archive

**For:** Bjorn, and the agent that opens this project next.
**What this is:** everything that led to the Round 1 entry and is no longer in use: the round documents, every set of
renders, the step prompts and the three early sketches. Put together here on 18 Nov 2026, on Bjorn's word ("put
everything together and archive old parts old steps"). Nothing was deleted; the files only moved.

**The rule for old paths:** a path `project/X` that no longer exists is now `project/archive/round1/X`. The documents
in here still name each other and the renders by their old paths; read them with that rule.

## What is where

| Folder | What it holds |
|---|---|
| `project-state/active/` | Round documents 00 to 40 (56 files): the reviews, the build plans, the logs per step, the last rounds of 16 Nov. The closing state (doc 41) and the jury assessment of the field (doc 32, 17 Nov) stayed in `project/project-state/active/` |
| `deliverables/screenshots/` | 40 sets of renders, 7 to 15 Nov: the Desktop sets, FinalV1 to FinalV3, the Publish to Web gate runs of publish 4, 5 and 6, the committee walkthroughs, the renders per build step |
| `deliverables/final-room-to-invest/` | The evidence per round of 16 Nov (hover-align, last-edit, package-a, plan-chart, rows-centred, step-tints, step3-accent, renders, checks, the before and after of the texts). The gallery post and the LinkedIn post stayed in `project/deliverables/final-room-to-invest/` |
| `deliverables/final-check-publish7/`, `deliverables/fix-publish7-visual-fixes/` | The package for the last check of publish 7, and the two visual fixes after it |
| `deliverables/pitch/`, `deliverables/deneb-specs/` | The three directions as a browsable page; the Deneb selector that was dropped for a native one |
| `pbip/` | The three sketch reports D1, D2, D3 of 6 Nov, with `SKETCHES.md` |
| `build-steps/` | The prompts of the twelve build steps and of review rounds 2 and 3 |

## What did not move, and why

- `project/tools/` and `project/design-prototypes/`: the scripts call each other across the step folders, and the
  checks read the layout files. They stay one working set.
- `project/pbip/GoodnightInn-opzet.Report`: the generator's own report. The checks and the model's trim read it.
- `project/analysis/`: the facts behind every number, reproducible.

## An old state as it was

The files in here do not open in Power BI Desktop from this folder: a sketch report looks for the model beside it,
and the model in the repository is the entry's. To see an old state whole, check out its commit:

| State | Commit |
|---|---|
| The entry as entered | tag `round1-entry-2026-11-16` |
| FinalV2 (the old `main`) | `c8d13c6` |
| Publish 4 (the first gate) | `71a5abb` |
| Publish 6 | `6227d6f` |
| Publish 7 | `a86e4ef` |
| "The Wake-up Call" build | `7b84bfa` |

The branches these states were built on are gone from GitHub (18 Nov); their commits are all in `main`.
