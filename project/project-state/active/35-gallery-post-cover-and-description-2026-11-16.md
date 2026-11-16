# 35 · The gallery post: cover image and description (16 Nov 2026, evening)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov, after doc 34:** he keeps the cash chart of doc 34 ("yes I like this, let's keep it, and
then this is it"). Left: a text for the entry page, one visual for the front cover of the entry in the gallery, the
requirements for both, and suggestions that make a curious reader click.
**Nothing in the report or the model changed.** `main` untouched. Not published.

---

## 1 · The requirements, and where each comes from

| Requirement | Source | How sure |
|---|---|---|
| The post holds: an image of the report, a short description that names the brand, the PBIX or the Publish to Web link, the official contest tag | Round 1 brief, `project/contest/round-1-brief.txt` | certain |
| Closes 18 Nov 2026, 11:59 p.m. Pacific (19 Nov, 08:59 in the Netherlands); one entry per round | Official Rules §3 and §5, `project/contest/official-rules-digest.md` | certain |
| Original work, no third-party images or fonts, nothing promoting alcohol; Microsoft may show the entry publicly | Official Rules §6 and §7 | certain |
| The form's fields: title, description, thumbnail image, an optional Publish to Web URL, an optional PBIX upload, a category or tag | Microsoft's how-to-submit posts of earlier rounds, read through search results | from earlier rounds |
| The thumbnail is the image shown on the gallery's main page | the same posts | from earlier rounds |
| A new entry passes moderation first: an hour in one post, up to 24 hours in another | the same posts | from earlier rounds |
| A pixel size, aspect ratio or file limit for the thumbnail; a limit on the description | not found anywhere | unknown |
| The exact contest tag | not in any document; the form shows it | unknown |

The community site answers an automated reader with 403, so the gallery, the entries already posted and the form
could not be read. That is the site's choice and it was not worked around. What the form says when Bjorn opens it
decides the last two rows.

Because of the moderation delay: post on 17 Nov as planned, not in the last hours.

## 2 · The cover: three candidates (`project/deliverables/final-room-to-invest/gallery/`)

Drawn by `project/tools/gallery/cover.py` (HTML, captured with headless Edge at 1920 x 1080); the `.html` of each is
beside its `.png`. Night ground, the logo, Segoe UI, the logo's orange for the one line that must be read. No image or
font from outside.

| File | The line | The picture | Why |
|---|---|---|---|
| `cover-a.png` **(recommended)** | 456 ways to spend $60M. The best one spends $9.4M. | every package the rules allow as a dot (capex against NPV through 2032, Expected case), the six that pay back in blue, package A marked | a counter-intuitive number, a shape that reads at tile size, and it ends in a dare: "Think you can beat ours? Build your own." Three reviewers of round 3 advised the 456-package chart for the image |
| `cover-b.png` | Full rooms. A slipping margin. | the two report pages as they are | the most literal "image of your report"; the pages themselves are not readable at tile size |
| `cover-c.png` | Same room. Same night. $17.47 apart. | one room night through an online agency and booked direct: what Goodnight Inn keeps, and the commission | the most human of the three, one fact anyone understands; it sells finding II, not the plan |

`cover-a-1920x1440.png` is cover a on a 4:3 canvas (the same composition with Night around it), for a form that crops
to 4:3. `cover.py --size 1920x1920 --only a` gives a square one.

`report-page1.png` and `report-page2.png` (1920 x 1080) are the two pages as they stand, for the body of the post.

**Checked against the open model** (the final copy's own, read-only query on its Package table,
`project/tools/gallery/packages.json`): 456 packages; 6 with an NPV of zero or more in the Expected case; package A
($9.4M, +$3.28M) is the highest of the 456 in the Low, the Expected and the High case. The script asserts the first
three before it draws. Cover c's amounts are card II's of page 1 (the script asserts that keeps + commission = what
the guest pays, and the $17.47).

At tile size (360 px wide) the headline of each cover reads; a plain page screenshot does not.

## 3 · The texts (`gallery/DESCRIPTION.md`)

A title, a teaser of about 60 words, the description of about 430 words (the question, page 1's four findings,
page 2's recommendation, three things to try, how it is built, accessibility, the credit line), an alt text for the
thumbnail, an optional line on how it was made (an AI coding agent did the file work; Bjorn decides whether it goes
in), and three lines to add if a reviewer asks. Every number is on the report. It replaces
`project/deliverables/final-check-publish7/DESCRIPTION-draft.md`, which still said "text contrast of 6.2:1 or more":
the colours changed since, so the new text says "WCAG AA", which is what `a11y_check.py` tests.

## 4 · Open

1. Bjorn picks a cover and reads the description; both are his to change.
2. Bjorn publishes from the window "Goodnight Inn - Room to Invest" and gives the link; then the gate and the
   walkthrough of doc 34 (hover a year in the cash chart and click Low and High first).
3. In the form: note what it asks for the thumbnail (size, ratio) and which tag it offers. A cover in another size
   is one run of `cover.py --size`.
4. Then File > Save as `.pbix`, the phone check, the post on 17 Nov.

## Log

- 16 Nov evening: requirements gathered (the community site refused the reader; brief, rules and search results
  used); three covers drawn and checked at tile size; texts written; committed and pushed.
- 16 Nov 20:45: Bjorn saved the final copy in Desktop again. Read against the repo value by value: the eyebrow of both
  pages moved left (page 1 x 1280 to 1200; page 2 x 1440 to 1400, its box 478 x 24.3), so it no longer ends at the
  page edge; nine other files differ in Desktop's serialization only; the cash chart of doc 34 is in the save as
  built; the model is equal (340 measures). Taken into `GoodnightInn-final.Report` untouched. File checks on it:
  a11y 0 failures, strip check 0, `pbir_detect` 0 unwaived. `report-page1.png` and `report-page2.png` in `gallery/`
  were captured again from the open final copy after this save, and `cover-b.png` was drawn again from them.
