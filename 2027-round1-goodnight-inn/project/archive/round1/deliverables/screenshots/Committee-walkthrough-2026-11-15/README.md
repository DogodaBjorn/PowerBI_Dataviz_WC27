# Committee walkthrough · the published report, 15 Nov 2026

**For:** the five reviewers of 13 and 14 Nov (jury, investor, UI/UX, clarity for a newcomer, dataviz and
storytelling), for review round 3. The prompt for that round is `project/build-steps/review-round3.txt`: read it
before anything else here.

**What this is:** the report "Goodnight Inn" as a judge gets it today. Every capture is the Publish to Web link,
sixth publish (15 Nov 2026, 12:37 UTC), opened signed out in headless Edge with a fresh profile, English browser, in
the order a judge clicks. It is the build of branch `rebuild-finalv3` at `6227d6f`, the version that passed the
Publish to Web gate on every check. Nothing here is a Desktop render or a comp. This is the version that will be
submitted on 17 Nov unless a review finds a reason to change it.

**Not the version you reviewed.** The reviews of 14 Nov read the fourth publish (`../Committee-walkthrough-2026-11-14/`,
same file names, so any view can be laid beside its predecessor). What was changed since, and what was left on
purpose, is in `project/project-state/active/25-action-plan-to-9-2026-11-15.md`. The round 3 prompt asks you to form
your own view of this set first and to open that document only afterwards.

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

`link.txt` says which report and which publish the link served during the run. The link itself is not in the
repository; Bjorn can give it to you.

## What the captures do not show

- **Motion and the mouse.** Hover states are single frames. What happens when the mouse rests on a button after a
  click is in `../PublishToWeb-2026-11-15-publish6/` (captures 05 and 06).
- **Touch and keyboard.** A real finger on a phone is still Bjorn's to try. The keyboard was walked with real keys in
  the published report: Tab through page 1 and through each of page 2's three views, then Enter, the arrows and Esc
  inside the hero table and the move selector. Every stop with its role and its spoken name is in
  `../PublishToWeb-2026-11-15-publish6/keys2_walk.txt`. No one has listened to a screen reader: what was checked is
  the text a screen reader is handed.
- **Other browser languages.** A Dutch and a German browser draw the pages equal to the English one to the pixel
  (`../PublishToWeb-2026-11-15-publish6/gate-summary.txt`).
- **Every state.** The package tooltip on B is not here, and Build your own has many more combinations of moves than
  the five shown.

## How it was made

`project/tools/desktop_shots/walkthrough/walk.py <link> <work dir> <out dir>`: seven browser runs through
`../step12/web.mjs`, about five minutes. The link is passed on the command line and is not stored in the repository.
After a republish, run it again; `link.txt` shows which publish the captures are of.
