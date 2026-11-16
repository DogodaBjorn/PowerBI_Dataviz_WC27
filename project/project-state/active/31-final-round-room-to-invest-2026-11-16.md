# 31 · The final round: "Room to Invest", less text, the header and the gaps (16 Nov 2026)

**For:** Bjorn, and the agent that picks the project up after him.
**Asked by Bjorn on 16 Nov:** (1) the entry is called Room to Invest, not The Wake-up Call; (2) every sentence tested
on two questions, does it add value and can it be as clear with fewer words; (3) the header texts sit too low on the
banner: lift them, let the top row of cards hang into the banner again, spread the whitespace that frees evenly.
**Plan:** approved by Bjorn in plan mode before the work (name, layout numbers, every text before and after).
**Branch:** `final/room-to-invest`, cut from `rebuild-finalv3` at `59383fd`, moved into `rebuild-finalv3` when the
checks and the renders were done. `main` untouched. **Not published.**
**Rules:** doc 23 section 1 (generators only, checks green, Desktop in a throwaway copy, every window of mine closed
without saving, Bjorn publishes).
**Evidence:** `project/deliverables/final-room-to-invest/` (its README lists the files).

---

## 0 · Result

| Asked | Status | In one line |
|---|---|---|
| The name | done | Entry, report and file "Goodnight Inn - Room to Invest"; the pages keep "The Wake-up Call" and "Room to Invest" |
| Less text | done | 28 wordings changed or left; page 1's running text 211 to 161 words, page 2's Recommended view 639 to 608 |
| Header higher, cards into the banner | done | Headline, subtitle and tabs 12 px up, the first card row from y 168 to 148, the banner picture as it was |
| Whitespace even | done | 24 px between the rows, above the footer row and under it, on both pages |
| Checks | green | Texts 138 of 138, numbers 809 of 809, alt texts 0 flags, accessibility 0, strip 0, schema 206 files 0 failing |
| Publish, gate on the link | **open** | Bjorn publishes; the gate and the walkthrough run on the new link |

---

## 1 · What was found before anything changed

- **The header rows had not moved.** Headline y 60, subtitle y 108, cards y 168 since layout v9. What moves is the
  banner: it is the page's background picture with Fit, and every host places that picture itself. The picture's
  banner ends at y 232. On publish 7 it ends at y 216 in a full-screen browser and about y 207 in a 1366 px window;
  Desktop shifts it with the shape of its window (14 px at 100 %, 38 px at 60 %, rounds 8 and 9). So the cards hung
  48 px into the banner in a browser and 25 px or less in Desktop. The same cause as rounds 8 and 9.
- On this session's screen (tall and narrow) Desktop puts the banner's end above the headline: a whole-page capture
  there is no reference for the banner (the tile README says the same). The browser on the published link is.
- The scene as a visual under the page, exact in every host, left on Bjorn's request in round 10 and stays out.
- The gaps were uneven: page 1 had 24, 24 and 20 px between the rows and 8 px under the footer row; page 2 had 16,
  28 and 8.

## 2 · Layout

| | Was | Is |
|---|---|---|
| Headline, both pages | y 60 | y 48 |
| Subtitle page 1 | y 108 | y 96 |
| Subtitle page 2 | y 108 in a 48 px slot, its line 9 px lower than page 1's | y 96 in a 24 px slot, built like page 1's |
| Tabs | y 60 | y 48 |
| Scenario label and pills | y 112 | y 96 |
| First card row | y 168 | y 148 |
| Page 1 cards | 168 to 288, 312 to 776, 800 to 1024 | 148 to 268, 292 to 756, 780 to 1004 |
| Page 2 cards | 168 to 656, 672 to 1016 | 148 to 636, 660 to 1004 |
| Footer row | y 1044 | y 1028 |

- The logo row stays at y 12: it is the page's top margin.
- **The banner picture is unchanged** (`canvas-night.jpg` comes out byte-equal). `brand_canvas_v3.py` now says "first
  card row + 84" where it said + 64. The cards hang 84 px into the banner in the file: about 68 px in a full-screen
  browser, about 60 px in a 1366 px window, about 45 px in Desktop at fit-to-window.
- **Page 1's finding cards.** The notes are two lines (were three) and stand on one line across the three cards
  (y 660), as do the link lines (y 716). The charts took the room: I 248 to 280 px, II 144 to 160 (its folio table
  moved down with it), III 216 to 256. The plan said + 24 px each; putting notes and links on one line gave + 32,
  + 16 and + 40. The two typed names in chart I were placed again by its scale (y 441 and 463) and stand on their
  line and band in the render.
- The gap between cards side by side stays 16 px.
- **Tab order, page 2.** With the tabs a row above the subtitle, the accessibility check asked for the reading order
  by rows: headline, tabs, subtitle, Scenario (the subtitle came before the tabs). Set in `opzet-layering.json`.

**How it is built.** The slot map `opzet-layout.json` carries the new positions. The measured chart rects typed in
`opzet_report.py` (`PLOT_RECT`, `F4_RECT`, `PROOF_RECT`, `YOU_RECT`, `PLAN_RECT`, `CMP_RECT`, `BARS_RECT`, and the
zero line of the plan chart's typed ticks) stay as they were measured; `moved()` shifts each by what its card has
moved since. A comparison of every visual's position before and after showed each one moving with its row; the
eight typed ticks and end labels of the plan chart were the ones that did not, and now do.

## 3 · Text

Every changed line is in `project/deliverables/final-room-to-invest/TEXT-before-after.md`. In short:

- **Page 1.** The subtitle lost its second sentence (the Next button says it). Two KPI labels and one KPI line are
  shorter. The three notes under the charts are two lines each. The four link lines start "Page 2:".
- **Page 2.** Subtitle, the caption under the ten moves, the first line under the recommendation's numbers, ledger
  row IV, the milestones ("Live:" once) and the Build chart's title are shorter. The 2028 gate is three lines: the
  sentence about the refresh left, tranche 3's label above it says "2028 gate, only with a case beyond 2032".
- **Gone:** "Picked: 3 moves, $9.4M of $60.0M" under the list in Build your own (visual, measure and spec slot); the
  your-plan tile says the count, the capex and the budget.
- **Definitions:** eight of the seventeen lines lost words; no term left.
- **Kept on purpose:** headlines and card titles (they are the findings), the caveats ("an association, not proof of
  cause", "A rule, not a forecast", "not discounted", the 6 hotels without a date), and the content of the seven
  lines the reviewers asked for in publish 7. That is why page 2 lost few words.

Two wordings differ from the approved plan, both because of what the render showed:
- Note I ended "like the other brands: no price premium absorbs it." and ran to a third line. It now ends "no faster
  than the other brands."
- Ledger row IV keeps the move's name: "kiosks; check-in complaints there up 43% since 2021" (the plan dropped
  "kiosks" too, and then the row no longer named its move like the three other rows).

The approved wording (`rebuild-v10-spec.json`) was rewritten from the model after each difference was read
(`build_checks.py --write-spec`), plus by hand the three typed link lines and the slot that left. The text check
counts 138 results now, not 142: the four views of Build your own each lost the footer's slot.

## 4 · Checks and renders

- On a throwaway copy's model: `build_checks.py` 138 of 138, `number_checks.py` 809 of 809, `alt_texts.py` 0 flags.
- Files: `a11y_check.py` 0 failures, `strip_check.py` 0, `compliance_check.py` 5 of 5, `schema_check.py` 206 files 0
  failing, `pbir_detect.py` 0 unwaived, `validate_tmdl.py --strict` 0 errors.
- Renders at one px per page px: page 1; Recommended in Low, Expected and High; What waits; Build with 3, 10 and 0
  moves. Read one by one: no clipped line, no line that wraps where it should not, ten bars without a scrollbar.
- The card edges measured on the renders (`fix29/gaps.py`): rows start at 148, 292 and 780 on page 1 and at 148 and
  660 on page 2, within the 1 to 2 px a card's shadow costs the measurement.
- Tools: `fix29/shoot.py` takes page 1 too (state `p1`); `step9/round.py` draws the banner under the strips to
  where its picture ends (first card row + 84), not to y 168.

## 5 · Known, and left

- Build your own: the list of moves ends 56 px above its card's lower edge, where the "Picked" line stood.
- Recommended: under the three lines of the gate the plan card is empty on the left.
- In Desktop the banner's end depends on the window; only a visual on the page would fix that, and that visual was
  taken out in round 10.
- `final-check-publish7/` and `fix-publish7-visual-fixes/` describe earlier states (publish 7; the fix build).

## 6 · Open

1. Bjorn publishes from the window "Goodnight Inn - Room to Invest" (a new name is a new report in the service) and
   makes its Publish to Web link.
2. The gate (`step12/gate.py`, reference: the gate run of publish 7) and the walkthrough on that link. Expected
   differences from publish 7: everything in sections 2 and 3, the findings as I to IV, the page names.
3. After the gate: File > Save as `Goodnight Inn - Room to Invest.pbix`, the phone check (portrait too: there the
   banner's end is where the host puts it), the description, the submission on 17 Nov.

## Log

- 16 Nov: plan approved; branch; layout, text and tools; checks green; renders read; evidence written.
- 16 Nov: branch pushed, `rebuild-finalv3` moved forward to it (`18f0122`). The final copy written from that build to
  `E:\Goodnight Inn - Room to Invest\Goodnight Inn - Room to Invest.pbip`, opened and refreshed; on its own model texts
  138 of 138, numbers 809 of 809, alt texts 0 flags; its report and model files equal `project/pbip` file for file; page
  names "The Wake-up Call" and "Room to Invest". The window stays open for Bjorn (publish, later Save as). The older
  window "Goodnight Inn - The Wake-up Call" is Bjorn's to close; its folder is left alone.
