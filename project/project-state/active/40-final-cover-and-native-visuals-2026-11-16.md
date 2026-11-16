# 40 · The final cover, and "100% native visuals" in cover and text (16 Nov 2026, night)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov:** after the answer that the report is still 100 % native visuals: "let's now redesign and
finalize the cover image where this is also part of the USP of my report, and let's incorporate it in the supportive
text."
**Nothing in the report or the model changed.** `main` untouched. Not published.

---

## 1 · The claim, and what it rests on

Read from the final copy's files after the save of 22:42: **194 visuals, every one a visual type of Power BI's own**
(81 cards, 69 text boxes, 9 buttons, 8 scatter charts, 6 line charts, 6 tables, 6 shapes, 3 images, 2 slicers, 3 bar
and column charts, 1 area chart); no `publicCustomVisuals`, no custom visual package; the registered resources are the
theme, the banner and tooltip backgrounds and the logo.
The one nuance: the bars in the hero table are images that DAX measures write and the native table shows. That is a
built-in feature, not a custom visual; the description says it in so many words.

## 2 · The cover (`project/deliverables/final-room-to-invest/gallery/cover-final.png`)

Drawn by `project/tools/gallery/cover_final.py` (HTML, headless Edge, 1920 x 1080; `--size 1920x1440` gives the 4:3
version that is beside it).

| Part | What |
|---|---|
| Headline | "456 ways to spend $60M. The best one spends $9.4M." (candidate a of doc 35) |
| Line under it | "A Board report for Goodnight Inn, the budget brand with the fullest hotels of the group. Think you can beat our plan? Build your own." |
| Badge | **"100% native Power BI visuals"**, the one light shape on the dark half |
| Proof line | "No custom visuals · 2 pages · 3 scenarios · all 456 packages computed" |
| Right half | the report itself, twice page 2: behind, "What waits, and why" with the 456 packages as dots (the chart the headline is about); in front, "Recommended: A" with the three plans highlighted and the plan bar with its clay step |

Why this and not candidate a as it was: the claim "all native" is only worth something next to the thing it is
about, so the report had to be on the cover; and the brief asks for "an image of your report". The dots of candidate a
are still there, as the report draws them.
At tile size (360 px) the headline reads; the badge reads from about 500 px.
Candidates a, b and c of doc 35 stay in the folder; `cover-final.png` is the one for the form.

## 3 · The text (`gallery/DESCRIPTION.md`)

- The teaser and the description end their opening with "Built with 100% native Power BI visuals: no custom visuals,
  nothing to install."
- A section of its own, "100% native Power BI visuals": the 194 visuals, what the bars, the highlighted rows, the
  tooltips and the three views are made of, and why it matters (opens wherever Power BI does, nothing to install or to
  approve, Power BI's own keyboard and screen-reader support).
- "How it is built" gained the line on one colour per decision (blue now, dark blue and clay for the later steps).
- The accessibility paragraph says "Body text, labels and numbers at WCAG AA contrast": the orange dot in the page
  label is 3.2:1 (doc 37), so "text contrast at WCAG AA" without a qualifier would not be true.
- The thumbnail's alt text describes the new cover; the form table names `cover-final.png`.
- A closing note holds what "100% native" rests on, for whoever is asked.

## 4 · Open

1. Bjorn reads the cover and the text; both are his to change.
2. He publishes from the window "Goodnight Inn - Room to Invest" and gives the link; then the gate and the walkthrough.
3. In the form: what it asks for the thumbnail (size, ratio) and which tag it offers.
4. Then File > Save as `.pbix`, the phone check, the post on 17 Nov.

## Log

- 16 Nov night: the visual types counted again; the cover redesigned and rendered in 16:9 and 4:3; the texts
  rewritten around the claim; committed and pushed.
