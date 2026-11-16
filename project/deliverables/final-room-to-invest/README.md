# Room to Invest: the final round (16 Nov 2026)

**For:** Bjorn, and whoever checks the entry after him.
**What this is:** the evidence of the last round on the report: the entry's name, less text, the header higher on the
banner and even gaps between the cards. Branch `final/room-to-invest`, moved into `rebuild-finalv3`. The account of
the round is `project/project-state/active/31-final-round-room-to-invest-2026-11-16.md`.

**Status: not published.** The public link still shows publish 7. Bjorn publishes "Goodnight Inn - Room to Invest"
himself; the check of the link in a browser (the gate) comes after that.

## What changed

1. **The name.** Entry, report and file are "Goodnight Inn - Room to Invest". The pages keep their names: "The
   Wake-up Call" and "Room to Invest".
2. **Text.** 28 wordings changed or left; all of them, before and after, are in `TEXT-before-after.md`. Page 1's
   notes, link lines and subtitle went from 211 to 161 words; page 1 as a whole from 469 to 413. Page 2's Recommended
   view went from 639 to 608 words: its long lines are the ones the reviewers asked for in publish 7, and they kept
   their content. One line is gone altogether: "Picked: 3 moves, $9.4M of $60.0M" under the list in Build your own.
3. **Layout.** Headline, subtitle and tabs 12 px higher, the Scenario row 16 px; the first row of cards starts at
   y 148 (was 168); 24 px between the rows, above the footer row and under it (was 24, 24, 20, 8 on page 1 and 16,
   28, 8 on page 2). Page 2's subtitle stands level with page 1's (it stood 9 px lower). On page 1 the three notes
   are two lines and stand on one line across the cards, as do the three "Page 2: ..." lines; the charts took the
   room (I 248 to 280 px high, II 144 to 160, III 216 to 256).

## The files

| File | What it shows |
|---|---|
| `before-after_page1.png`, `before-after_page2.png` | Publish 7 above, this build under it |
| `renders/page1.png` | Page 1 |
| `renders/page2-recommended-Expected.png`, `-Low`, `-High` | Recommended: A, per case |
| `renders/page2-what-waits-Expected.png` | What waits, and why |
| `renders/page2-build-03-moves.png`, `-10-moves`, `-nothing-picked` | Build your own: as it opens, all ten moves (the alarm), the empty state |
| `TEXT-before-after.md` | Every changed text |
| `checks/` | The check reports of this build: texts (138 of 138), numbers (809 of 809), alt texts (0 flags), the file checks, and the card edges measured on the renders |

## How to read the renders

They are Power BI Desktop renders of a throwaway copy, one px per page px, taken in four strips
(`project/tools/desktop_shots/fix29/shoot.py`). They show what is drawn where. Two things they do not show:

- **The banner as a host draws it.** The banner is the page's background picture, and each host places that picture
  itself. In the renders it is drawn as a plain dark band down to y 232, where the picture's banner ends in the file,
  so the cards hang 84 px into it. Measured on publish 7, a full-screen browser shows the banner's end about 16 px
  higher and a 1366 px window about 25 px higher; Desktop shifts it by its window's shape, 14 to 40 px on a normal
  screen. So expect the cards to hang about 68 px into the banner in a browser, less in Desktop. Only the published
  link shows it as the judges get it.
- **The night-glow artwork** of the banner (the gradient and the hanger). It is unchanged.

The seams of the strips are at page x 480, 960 and 1440; a mark next to a seam can stand 1 to 2 px off.

## Left as it is, on purpose

- The gap between cards that stand side by side stays 16 px; the card widths hang on it.
- In Build your own the list of moves now ends 56 px above its card's lower edge, where the "Picked" line stood.
- Under the three lines of the 2028 gate the plan card is empty on the left; the cash chart keeps its size.
- The banner is not drawn by a visual on the page (that would be exact in every host). Bjorn took that visual out in
  round 10; it stays out unless he asks for it.

## After this round: the report as it is submitted (16 Nov, later)

Bjorn finished the layout himself in Desktop (saved 11:32) and asked for one more edit on that version: card IV by
location type. `last-edit/` shows the result, captured from the final copy: `page1.png`, `card-IV.png`,
`card-III.png`, `page2-recommended-Expected.png`, and the check reports in `last-edit/checks/`. The account is
`project/project-state/active/32-last-edit-card-IV-by-location-type-2026-11-16.md`. The renders and the text file
above show the state before his own pass: the positions differ, and the link lines now start "Investment Option:".

## After Bjorn's second pass (16 Nov, afternoon)

Bjorn saved again at 13:18 (headline higher, eyebrow top right, Back in the footer row, Highway darker) and asked for
two things on that version: no raw SVG text on hover in the hero table, and the bottom card ending at the same height
on both pages. `hover-align/` shows the result: `page1.png` and `page2.png` (throwaway copy), `final-copy-page1.png` and
`final-copy-page2.png` (the final copy), and the check reports in `hover-align/checks/`. The account is
`project/project-state/active/33-hover-text-and-bottom-card-2026-11-16.md`. `last-edit/` shows the state before his
second pass.

## The cash chart by case (16 Nov, afternoon)

Bjorn found the cash chart at the foot of page 2 too grey. Each case now has its own colour (Low Burnt Tangerine,
Expected Coffee Blue, High Night), the case in view is the thick line, and the zero line is Night with a light shade
under it. `plan-chart/` shows it: `chart-before.png`, `chart-expected.png`, `chart-low.png`, `chart-high.png`
(throwaway copy), `final-copy-page2.png` (the final copy) and the check reports in `plan-chart/checks/`. The account is
`project/project-state/active/34-plan-chart-by-case-2026-11-16.md`.

## The gallery post (16 Nov, evening)

`gallery/` holds what goes into the Contests Gallery form: three cover candidates for the gallery tile (`cover-a.png`,
recommended: the 456 packages; `cover-b.png`: the two pages; `cover-c.png`: one room night), `cover-a-1920x1440.png`
for a 4:3 tile, the two pages as they stand (`report-page1.png`, `report-page2.png`) and `DESCRIPTION.md` with the
title, the teaser, the description and the alt text. The account is
`project/project-state/active/35-gallery-post-cover-and-description-2026-11-16.md`.

## Package A at a glance (16 Nov, late evening)

Bjorn could not see at one glance what package A is. Its three rows in the table now stand on a light blue ground,
the recommendation card has a Coffee Blue outline, every decision has one colour in the table and in the plan bar, and
a tranche is called a step. `package-a/` shows it: `page2-before.png`, `page2-after-outline.png`,
`page2-variant-tinted-card.png` (not chosen), `final-copy-page2.png` and the check reports. The account is
`project/project-state/active/36-package-a-at-a-glance-2026-11-16.md`.

## Grounds for step 2 and step 3 (16 Nov, night)

On Bjorn's save of 21:48. The rows of step 2 and step 3 in the table have a light ground in their own colour, and the
same three grounds stand behind the labels over the plan bar. `step-tints/` shows it: `page2-before.png`,
`page2-recommended.png`, `page2-what-waits.png`, `page2-build-your-own.png`, `page1-as-saved-21h48.png` and the check
reports. The account is `project/project-state/active/37-step-grounds-table-and-plan-bar-2026-11-16.md`.

## Step 3 in clay (16 Nov, night)

Bjorn chose clay as the third accent: step 3 is clay in the plan bar and in the table, the three plans stay highlighted
in the table, and the grounds over the plan bar of the round before are gone. `step3-accent/` shows it: `options.png`
(the sketch he chose from), `page2-before.png`, `page2-recommended-clay.png` and the check reports. The account is
`project/project-state/active/38-step-3-in-clay-2026-11-16.md`.

## The table's text in the middle of its row (16 Nov, night)

A native table has no vertical alignment; row padding puts text and bar in the middle of the row. The two reference
lines are a stroke per row now, a dashed line. `rows-centred/` shows it: `table-before.png`, `table-after.png`,
`table-tried-unbroken-line.png` (dropped), `page2-recommended.png` and the check reports. The account is
`project/project-state/active/39-hero-table-rows-centred-2026-11-16.md`.
