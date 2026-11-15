# Two visual fixes after publish 7: the evidence (15 Nov 2026)

**For:** Bjorn, and the agent that reviewed `final-check-publish7/` and wrote the prompt for these fixes.
**What this is:** renders of branch `fix/publish7-visual-fixes`, which holds the two fixes that
`project/project-state/active/29-prompt-publish7-final-visual-fixes-2026-11-15.md` (on `main`) asks for. The account
of the round, with what changed and why, is `project/project-state/active/30-fix-round-doc29-two-visual-fixes-2026-11-15.md`.

**Status: not merged, not published.** The report on the public link is still publish 7, without these fixes.

## The two fixes in one look

| File | What it shows |
|---|---|
| `detail/plan-tile_8-moves_before-after.png` | Fix 1. Left: publish 7 with eight moves, seven bars and a scrollbar. Right: this branch, eight bars |
| `detail/plan-tile_3-8-10-moves.png` | Fix 1. The "Your plan" tile with 3, 8 and 10 moves picked, at twice the page's size |
| `detail/hover-hint_before-after.png` | Fix 2. Top: publish 7, the hint right above "Cash positive above this line". Bottom: this branch |
| `detail/hover-hint_three-cases.png` | Fix 2. The capital plan's chart in Low, Expected and High: no line reaches the hint |

## The renders

Each view at two sizes. `1920/` is the page at 100 %: one px per page px, what a 1920 px wide browser window shows.
`1366/` is the page at 64 %: the size Power BI fits the page to in a 1366 px wide window (measured on publish 7,
`final-check-publish7/walkthrough/22_p2-recommended-1366px-window.png`).

| File (in both folders) | The view | What to see |
|---|---|---|
| `build-03-moves` | Build your own as it opens: package A's three moves | Three bars; Picked 3 moves, $9.4M; the dot "You" on A; the two cash lines are one |
| `build-08-moves` | A's three plus Breakfast, Gatwick, Toronto, Kingston and the Energy programme: the selection of `walkthrough/19_p2-build-eight-moves.png` | Eight bars, Energy programme the last, no scrollbar; $46.5M, −$21.2M, +$8.3M, 17.9%, as on capture 19 |
| `build-10-moves` | All ten moves | Ten bars, no scrollbar; $100.7M, the budget alarm |
| `build-09-moves-without-app` | Nine moves, the booking app left out | The rules line takes two lines here; the first bar stands clear of it |
| `build-00-nothing-picked` | Nothing picked | The empty state: the taller tile holds its one sentence |
| `recommended-Expected`, `-Low`, `-High` | Recommended: A, per case | The hint right of "The 2028 gate"; "Cash positive above this line" stands alone |
| `what-waits-Expected` | What waits, and why | Not touched by this round; here to show it |

## How they were made, and what they are not

Power BI Desktop 2.159 on a throwaway copy of the project, the page cut into four strips and captured through the
Desktop Bridge at the device scale that gives each size (`project/tools/desktop_shots/fix29/shoot.py`). The text is
drawn by Desktop at that size, not scaled down from a larger picture. The two sizes of a strip are held against each
other, and a strip that misses a visual in one of them is captured again.

- **These are not captures of the published report in a browser.** That needs a publish, which this round does not
  do. Power BI scales the whole page to the window, so the layout (which bars show, what stands next to what) is the
  same at every size; how the service draws small text at 64 % is seen only on the link.
- The browser's own bar and the service's footer are not in the pictures. A 1366 px window shows the page as in
  `1366/` with those around it.
- The strips meet at page x 480, 960 and 1440; a mark next to a seam can stand 1 to 2 px off.
- The before pictures in `detail/` are publish 7's own captures from `final-check-publish7/walkthrough/` (the
  published report in a browser); the after pictures are Desktop renders. The comparison is of what is drawn where,
  not of pixels.

## Checks

`checks/` holds the reports of the checks rerun on this branch's build: every text against the approved wording
(`build_checks.txt`), every number against the organisers' workbook (`number_checks.txt`), every alt text
(`alt_texts.txt`), the file checks (`file-checks.txt`) and what changed in the report's files against publish 7's
build (`changed-against-publish7.txt`: sixteen visuals, their position or size only).

## Still open

The click test of the public link in a private window (doc 28), and, if the fixes are taken, an eighth publish with
the gate on it. Neither is part of this round.
