# Committee walkthrough · the published report, 14 Nov 2026

**For:** the five reviewers of 13 Nov (jury, investor, UI/UX, clarity for a newcomer, dataviz and storytelling;
docs `19-*.md` in `project/project-state/active/`), for a second walk through the entry.

**What this is:** the report "Goodnight Inn" as a judge gets it. Every capture is the Publish to Web link, fourth
publish (14 Nov 2026, 20:45 UTC), opened signed out in headless Edge with a fresh profile, English browser, in the
order a judge clicks. It is the build of branch `rebuild-finalv3` at `71a5abb`, the one that passed the Publish to
Web gate. Nothing here is a Desktop render or a comp.

**Not the version you reviewed.** The reviews of 13 Nov read FinalV2. This is the rebuild made from them: the
requirements in doc 20, the build guideline in doc 21, the comp in doc 22, the twelve build steps and Bjorn's
decisions in doc 23. Two things to expect: page 2's middle tab is now "What waits, and why" (was "Considered: B and
C"), and the tooltip pages `tt-f1` to `tt-f4` are gone.

## The walk

Captures 01 to 21 and 23 are the report page, 1920 x 1080, pixel for pixel as the browser draws it.

| File | What a judge did | What it shows |
|---|---|---|
| `01_p1-brand-review` | opened the link | Page 1, The Brand Review |
| `02_p1-tooltip-f3-oldest-band` | mouse on F3's bar "10 years or more" | tooltip `tt-f3-band` |
| `03_p1-tooltip-f4-toronto` | mouse on Toronto's dot in F4 | tooltip `tt-f4-hotel` |
| `04_p1-tooltip-definitions` | mouse on the Definitions chip (bottom right, both pages) | tooltip `tt-glossary` |
| `05_p2-recommended-expected` | clicked "Next: what we fund, and why" | Page 2 as it opens: Recommended: A, Expected case |
| `06_p2-recommended-low` | clicked the scenario pill Low | Recommended, Low case |
| `07_p2-recommended-high` | clicked High | Recommended, High case |
| `08_p2-recommended-tooltip-year` | back on Expected, mouse on the capital plan's chart | tooltip `tt-year` |
| `09_p2-what-waits-expected` | clicked the tab "What waits, and why" | What waits, Expected |
| `10_p2-what-waits-low` | Low | What waits, Low |
| `11_p2-what-waits-high` | High | What waits, High |
| `12_p2-what-waits-tooltip-a` | Expected, mouse on A's disc | tooltip `tt-package`, package A |
| `13_p2-what-waits-tooltip-c` | mouse on C's disc | `tt-package`, package C |
| `14_p2-what-waits-tooltip-grey-package` | mouse on a grey dot | `tt-package`, one of the 456 packages |
| `15_p2-what-waits-tooltip-year` | mouse on the comparison chart | `tt-year` |
| `16_p2-build-opening-package-a` | clicked the tab "Build your own" | Build as it opens: package A is picked |
| `17_p2-build-six-moves` | added Breakfast, Gatwick and Toronto | six moves, $26.1M |
| `18_p2-build-tooltip-your-plan` | mouse on the dot "You" | `tt-package` for the judge's own six moves |
| `19_p2-build-eight-moves` | added Kingston and the energy programme | eight moves, $46.5M: the bars scroll from here on |
| `20_p2-build-over-budget` | left only Energy, Boston and the refresh | $69.3M: over the $60.0M budget |
| `21_p2-build-nothing-picked` | removed the last three | the empty state |
| `22_p2-recommended-1366px-window` | a 1366 x 768 browser window | the whole window, with Power BI's own bar, on Recommended |
| `23_p1-row-clicked` | clicked a row of page 1's folio table | Power BI marks the clicked row; nothing else on the page changes |

`zoom/` holds the left and the right half of views 01, 05, 09 and 16 at twice the size (2 device pixels per page
pixel, a second run at that scale): use these for the small text, the table cells and the axis labels.

`texts/` holds, per page view, every visible text and every `aria-label` (the alt texts a screen reader gets), one
per line, read from the published page. The views with the 456-package chart are long: each dot has a label.

`link.txt` says which report and which publish the link served during the run.

## What the captures do not show

- **Motion and the mouse.** Hover states are single frames. While the mouse rests on a button, Power BI adds its own
  bubble "Click here to follow"; the captures were taken with the mouse parked in the page's margin, so it is not on
  them.
- **Touch and keyboard.** A real finger on a phone is still Bjorn's to try. The Tab order was walked with real keys
  in the gate (logo, eyebrow, headline, subtitle, the four KPIs, F1).
- **Other browser languages.** A Dutch and a German browser draw every page and tooltip equal to the English one to
  the pixel; one proof capture is in the gate's folder.
- **Every state.** The package tooltip on B is not here, and Build your own has many more combinations of moves
  than the five shown.

The evidence for the touch, keyboard and language points is `../PublishToWeb-2026-11-14/` (the gate's captures and
summary) and doc 23, "Step 12".

## Known before you start

Every deviation from the approved comp is listed, with its reason, in `../FinalV3/README.md` ("Outside 2 px, by
design or by Power BI") and was accepted by Bjorn on 14 Nov (doc 23, "Open questions": all eleven closed). The
Desktop renders in `../FinalV3/` are older than this set on two points you will see here: the hero table's caption
is one sentence, and the plan bar's segments have white seams of 3 px.

## How it was made

`project/tools/desktop_shots/walkthrough/walk.py <link> <work dir> <out dir>`: seven browser runs through
`../step12/web.mjs`, about five minutes. The link is passed on the command line and is not stored in the repository.
After a republish, run it again; `link.txt` shows which publish the captures are of.
