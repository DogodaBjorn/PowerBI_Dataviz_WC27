# Review set: Goodnight Inn report, rendered by Power BI Desktop (7 Nov 2026)

## What this is
A two-page Power BI report entered in the Power BI Dataviz World Champs 2027 (Round 1). The brief: Goodnight Inn, one
of four hotel brands in the Pillow & Key Group, gets up to $60M to invest in 2027-2032. Readers are the group's Board
and the contest judges. The owner's direction is "an investor deck, not a playground: simple, effective, no frills".

- **P1, The Brand Review**: the problem, in four findings (F1 margin after commissions, F2 online agencies, F3 NPS
  by years since renovation, F4 where the hotels are full), with a KPI band on top.
- **P2, The Investment Strategy**: the advice. Fund package A ($9.4M: booking app, kiosks at 20 desks, revenue
  management) and hold $50.6M back. The scatter shows all 456 packages the rules allow (capex vs NPV through 2032).
  The right panel has a scenario switch (Low / Expected / High) and a "Package in focus" dropdown (A, B, C are rules;
  any single package can be picked too). "Open the plan for the package in focus" swaps the panel to the plan state
  (waterfall, initiative table, cumulative net impact, ops numbers, risks); "Back to the recommendation" swaps back.

Contest rules: 2 pages, at least 4 core visuals, package at most $60M, at least 3 initiatives, at least 1 growth
initiative, impact through 2032, Publish to Web, built-in fonts only.

## How the images were made
Every image was rendered by Power BI Desktop itself, at exactly 1920 x 1080 (what a 1920-wide Publish-to-Web viewer
sees). States 02-16 were set by applying the report's own stored bookmark and slicer values. The L-series are real
clicks on the canvas, in order (Desktop needs Ctrl+click to fire a button in edit mode).

Environment facts, so you can tell report from tool:
- Desktop runs with a Dutch (nl-NL) locale. Numbers formatted by a visual use a decimal comma (79,4%), and the
  waterfall's total bar label reads "Totaal". Text built in DAX is en-US (64.7%). Treat the locale as ONE item.
- In the L-series the mouse stays where it clicked: hover states, the visual header icons (filter/focus/...) and the
  tooltip "CTRL+klik hier om volgen" ("Ctrl+click to follow") are Desktop edit-mode chrome. But do judge a button's
  hover/pressed look if its text becomes hard to read.

## Files
- `01_P1_brand-review.png`: page 1.
- `02`-`07`: P2 landing state. 02 = A, Expected (how the page opens). 03/04 = Low/High. 05/06 = focus B/C.
  07 = focus on a non-preset package that spends the full $60M.
- `08`-`13`: P2 plan state (after "Open the plan"). 08-10 = A in Expected/Low/High, 11 = B, 12 = C, 13 = the $60M package.
- `14`/`15`: focus B in the Low scenario (landing, plan). `16`: plan C in Low.
- `L1a`-`L4c`: live click sequence. L1 button round trip; L2 click the High tile, round trip; L3 open the dropdown,
  pick C, round trip; L4 click the raspberry scatter point (package A), then round trip.
- `detail/`: 2x crops (header, KPI band, each finding card, footer; the P2 panel of every state; the scatter of
  some states). Use these to read small text.
- `comp/`: the approved design comp (HTML mock) the build should follow.

## What I need from you
A rigorous, independent visual and editorial review of what is on these images. In particular:
1. Defects: clipping, truncation, overlap, misalignment, empty or broken states, wrong or missing labels, text that
   does not fit, contrast problems, anything that looks unfinished.
2. Consistency: the same number or name shown in two places must agree, within a state and across states; the
   panel must change when (and only when) it should.
3. Legibility at real size, including at 1366 wide (the page then scales to 71%; check the smallest text).
4. The story: does each page make one point that a board member gets in 10 seconds; does P2 read as a clear
   recommendation; is anything there that does not earn its place.
5. Deviations from the approved comp that make it worse.

Report each finding with: severity (blocker / major / minor / polish), the file(s) and where on the page, what is
wrong, why it matters for this audience, and a concrete fix. End with an overall verdict and the top 5 fixes in
order. Write it to `REVIEW.md` in this folder and also return it.
