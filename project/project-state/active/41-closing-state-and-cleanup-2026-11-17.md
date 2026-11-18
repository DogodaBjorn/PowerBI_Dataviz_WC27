# 41 · Closing state of Round 1, and the cleanup (17 Nov 2026)

**For:** Bjorn, and the agent that opens this project next.
**Asked by Bjorn on 17 Nov:** "can you do a full on cleanup after all the work now that we have published the final
version?"
**State:** the entry is published and posted. Branch `rebuild-finalv3`, tag `round1-entry-2026-11-16`. `main` untouched.

---

## 1 · What was entered

| What | Where |
|---|---|
| The report | `E:\Goodnight Inn - Room to Invest\Goodnight Inn - Room to Invest.pbip` = `project/pbip/GoodnightInn-final.Report` (equal value for value; his last save is of 16 Nov 23:17) |
| The model | `project/pbip/PillowKey.SemanticModel`, 341 measures, equal to the final copy's measure for measure |
| The gallery post | title "The goodnight inn: Room to invest"; texts in `project/deliverables/final-room-to-invest/gallery/DESCRIPTION.md`; cover `gallery/cover-tile.png` |
| The LinkedIn post | `project/deliverables/final-room-to-invest/linkedin/` (film, still, `POST.md`) |
| The account of 16 Nov | docs 31 to 40 in this folder, one per round; evidence per round under `project/deliverables/final-room-to-invest/` |

The report is hand-finished. It is never regenerated; an edit goes through a script in `project/tools/final_edit/`
(f4 to f10), after `save_diff.py` has read Bjorn's last save.

## 2 · What the cleanup did

- **Bjorn's save of 23:17** read and taken in untouched: Desktop renumbered layers in 80 files, the order of the
  visuals is the same, nothing else changed.
- **Two tools that lived in temporary folders are in the repository now:** `project/tools/final_edit/save_diff.py`
  (a Desktop save against the repository, value by value; `--take` takes it in) and
  `project/tools/desktop_shots/crop_page.py` (a page out of a capture).
- **The gallery folder holds what is used:** `cover-tile.png`, `.jpg`, `cover-tile-as-shown.png`, the two page images
  and `DESCRIPTION.md`. The three candidates, `cover-final` and every `.html` went to `gallery/earlier/`; the cover
  scripts write there.
- **Sixteen local branches that are merged into `rebuild-finalv3` removed** (fourteen are still on GitHub; two were
  local only and are part of this branch's history).
- **A tag on the entered state:** `round1-entry-2026-11-16`.
- **Temporary files removed:** this session's scratch folder (437 MB: nine throwaway copies of the report, captures,
  one-off scripts, and a file with the Publish to Web link of an earlier publication), the Edge profile of the cover
  renders, a downloaded package file.
- **Left over from the gate runs of 14 Nov:** two headless Edge processes still running after three days, and three
  profile folders `%LOCALAPPDATA%\Temp\p2w-*` of 1.4 GB together. Stopped (after reading their command lines) and
  removed. `step12/gate.py` leaves these behind: clear them at the end of a gate run.
- **No Desktop window was open**; nothing was closed.
- **The agent's notes** (outside the repository): the index line of this project went from 7,028 to 474 characters,
  the closing state stands on top of the project note, and the rule about Bjorn's own Desktop window is written down.

## 3 · Not done, and why

| What | Why not | Who |
|---|---|---|
| `E:\_throwaway_f5`, `E:\GoodnightInn-publish`, `-publish4`, `-publish6`, `E:\Goodnight Inn - The Wake-up Call` (26 MB together) | superseded copies, but removing a folder directly under `E:\` is refused to the agent, on purpose | Bjorn |
| Older reports and their Publish to Web links in the Power BI service | live things: nothing goes off without Bjorn's yes, and the link in the gallery post must stay | Bjorn |
| Seven stashes (Desktop saves of 7 to 13 Nov, parked) | cannot be undone once dropped; all are of states before the rebuild | Bjorn says, the agent drops |
| Branches on GitHub (24) | outward; all work is in `rebuild-finalv3` | Bjorn says, the agent removes |
| `rebuild-finalv3` into `main` | the standing rule: never `main`, no pull request, unless Bjorn asks | Bjorn says |
| The local branch `ccr-f6fb2153-52yiq7` | not merged; left | - |

## 4 · Still open on the entry itself

1. **The gate was never run on the final publication.** The agent has not had its Publish to Web link. With the link:
   `step12/gate.py` and `walkthrough/walk.py`, first a bar in the hero table (the hover text of doc 33 was not tried
   again after doc 39), then What waits, Build your own, a year in the cash chart, Low and High, a hotel in card IV, Back.
2. On the gallery post: the cover on the tile (it was empty), the two labels the other entries carry, and the first
   line (the tile shows "Hey all,...").
3. No `.pbix` was found beside the final copy: File > Save as, if the form or the rules want the file.
4. The four `a11y_check` failures are the orange dot in the two page labels (doc 37).
5. The deadline is 18 Nov 23:59 Pacific (19 Nov 08:59 in the Netherlands); the post can be edited until then.

## 5 · Rules that held on 16 Nov and hold for Round 2

- Read Bjorn's save first (`save_diff.py`), take it in untouched, then edit.
- Try an edit on a throwaway copy in the scratch folder; captures only of throwaway windows.
- **Never `reload` Bjorn's own window** after an edit on its files: twice it left the canvas loose in the window.
  Close it with his leave (`desktop_shots/close_with_save.ps1`) and open it again.
- A new visual on page 2 needs its bookmark states and its "no filter" entries (`strip_check.py`); a colour outside
  the theme needs a waiver he confirms.
- When he asks for suggestions before building: a sketch, then wait.

## Log

- 17 Nov: the 23:17 save taken in; tools saved; gallery folder ordered; merged local branches removed; tag set;
  temporary files removed; this document.
