# 41 · Closing state of Round 1, and the cleanup (17 Nov 2026)

**For:** Bjorn, and the agent that opens this project next.
**Asked by Bjorn on 17 Nov:** "can you do a full on cleanup after all the work now that we have published the final
version?"
**State:** the entry is published and posted. Since 18 Nov the entry is `main` (one branch); the entered state is tag `round1-entry-2026-11-16`. Sections 6 and 7 are the cleanups of 18 Nov; where they differ from what stands above them, the later section holds. **Paths in this document are relative to the entry folder** `2027-round1-goodnight-inn/`.

---

## 1 · What was entered

| What | Where |
|---|---|
| The report | `Goodnight Inn - Room to Invest/Goodnight Inn - Room to Invest.pbip` in this entry folder (until 18 Nov: `E:\Goodnight Inn - Room to Invest`) = `project/pbip/GoodnightInn-final.Report` (equal value for value; his last save is of 16 Nov 23:17) |
| The model | `project/pbip/PillowKey.SemanticModel`, 341 measures, equal to the final copy's measure for measure |
| The gallery post | title "The goodnight inn: Room to invest"; texts in `project/deliverables/final-room-to-invest/gallery/DESCRIPTION.md`; cover `gallery/cover-tile.png` |
| The LinkedIn post | `project/deliverables/final-room-to-invest/linkedin/` (film, still, `POST.md`) |
| The account of 16 Nov | docs 31 to 40, one per round, with the evidence per round: in `project/archive/round1/` since 18 Nov |

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

## 6 · The second cleanup (18 Nov 2026)

**Asked by Bjorn on 18 Nov:** "I still need someone to fully clean up all the separate folders and work for the
Dataviz WorldCup entry.. there's a whole lot of previous work that needs to be dropped". On the three choices put to
him: drop all the git leftovers; merge into `main` and keep one branch; and for the old work inside the repository:
"put everything together and archive old parts old steps".

| What | Done |
|---|---|
| `E:\_throwaway_f5`, `E:\GoodnightInn-publish`, `-publish4`, `-publish6`, `E:\Goodnight Inn - The Wake-up Call` | to the Recycle Bin of E: (not open in Desktop, no `.pbix` in them; they can be put back from there) |
| Scratch folders of 23 finished sessions of this project (7 to 15 Nov) | removed, 1.3 GB: throwaway copies, captures, gate runs. Folders of other projects and of running sessions were left |
| Seven stashes | dropped (Desktop saves of 7 to 13 Nov, all of states before the rebuild) |
| 21 branches on GitHub that were merged into `rebuild-finalv3` | deleted; their commits are in `main` |
| The branch `ccr-f6fb2153-52yiq7` (6 Nov, the D4 "what-if" pitch and a page-count ruling, never merged) | deleted, locally and on GitHub; that one commit is gone |
| `rebuild-finalv3` into `main` | merged; `main` kept the five documents Bjorn's own agent had put there. `rebuild-finalv3` deleted afterwards. The repository has one branch and one tag |
| Old parts and old steps inside the repository | moved, not deleted, to `project/archive/round1/` under their old relative paths (about 940 files, 205 MB): round documents 00 to 40, the 40 render sets, the evidence per round of 16 Nov, the publish 7 packages, the pitch page, the Deneb spec, the D1-D3 sketches, the step prompts. `project/archive/round1/README.md` says what is where |

**Left where it was, on purpose:** `project/tools/`, `project/design-prototypes/`, `project/analysis/` and `project/pbip/GoodnightInn-opzet.Report`
(the scripts call each other and the checks read these); the gallery and LinkedIn material in
`project/deliverables/final-room-to-invest/`; doc 32 (the jury assessment of the field, 17 Nov) beside this document.

**Checked after the move**, on `project/pbip/GoodnightInn-final.Report`, against the same run before it:
`save_diff.py` 0 differences with Bjorn's copy (341 measures both sides), `strip_check.py` 0, `compliance_check.py`
all ok, `build_checks.py --static` all ok, `a11y_check.py` the same four (the orange dot, doc 37).

**Still with Bjorn:**

- `E:\Goodnight Inn - Room to Invest` stays: it is the copy he opens and published from, and the post can be edited
  until the deadline.
- The older reports in the Power BI service and their Publish to Web links ("GoodnightInn-opzet", "Goodnight Inn",
  possibly "Goodnight Inn - The Wake-up Call"): live things, nothing goes off without his yes, and the link in the
  gallery post must stay.
- Section 4 is unchanged: the gate on the final publication waits for its link.
- Left alone because they are of the 2026 contest, not of this entry: `E:\World Champs R2`, and in Downloads the
  `World Champs BCN 26` files (three of them the same 51 MB file) and three `PowerBI_Setup_DatavizWC` zips.

## 7 · One repository, a folder per entry (18 Nov 2026, later)

**Asked by Bjorn:** "put everything in the same PowerBI Data Viz folder and repository, also older entries..
migrate everything into own entry folders ... I don't want any separate folders on my E anymore". On the two
choices put to him: move both 2026 build repositories in with their history; starter files in, duplicates out.

| What | Done |
|---|---|
| This project (everything that stood at the repository's root) | moved as it was into `2027-round1-goodnight-inn/`; history kept. The tools find their root from their own place; six one-off helpers with a typed path were repointed |
| `E:\Goodnight Inn - Room to Invest` (Bjorn's own copy) | moved into this entry folder under the same name and tracked in git; `save_diff.py` reads it there. This supersedes the first bullet under "Still with Bjorn" in section 6 |
| The 2026 Round 2 build, repository `hp-world-champs` (`E:\PowerBI Set-up\hp-world-champs`) | merged with its 67 commits into `2026-round2-the-boy-who-came-back/`; its files outside git (data, the `.pbix`, caches, `node_modules`) moved along; the old folder to the Recycle Bin |
| The 2026 Round 3 build, repository `wc-round-3` (`E:\PowerBI Set-up\wc-round-3`) | the same, 42 commits, into `2026-round3-movies/` |
| `E:\World Champs R2` (repository `world-champs-r2`) | its files into `2026-round2-the-boy-who-came-back/contest-starter/`. It was labelled the Round 2 deliverable; it is the organisers' package, file for file (equal to their zip and to the starter kept in `E:\PowerBI Set-up\_archive`) |
| Loose files | the Round 1 starter of 2026 from Downloads into `2026-round1/contest/`; three copies of the Round 3 starter in Downloads (equal to the one in the project) to the Recycle Bin; on the OneDrive Desktop the copy of the Round 2 package (76 of 76 files equal) to the Recycle Bin and its zip into `contest-starter/` |

**Checked after the move**, from this entry folder: `save_diff.py` 0 differences between Bjorn's copy and
`project/pbip/GoodnightInn-final.Report` (341 measures both sides); `strip_check.py`, `compliance_check.py`,
`build_checks.py --static` and `a11y_check.py` give the same output as before the first move, to the byte. For the
two 2026 projects the tree in this repository equals the tree of the old repository's last commit.

**How to work here now:** open `2027-round1-goodnight-inn/` as the working directory. Bjorn opens the report from
`Goodnight Inn - Room to Invest/` in this folder; a save of his shows in `git status`, and `save_diff.py --take`
still carries it into `project/pbip/GoodnightInn-final.Report`.

**Still with Bjorn:** the three older repositories on GitHub (`hp-world-champs`, public and pinned; `wc-round-3`;
`world-champs-r2`) still exist: archive or delete them when he wants. The older reports in the Power BI service and
section 4 are unchanged. Not moved: `E:\PowerBI Set-up\_archive` (a backup zip of `hp-world-champs` and the
Round 2 starter) and three `PowerBI_Setup_DatavizWC` zips in Downloads: they are of the set-up, not of an entry.

## Log

- 17 Nov: the 23:17 save taken in; tools saved; gallery folder ordered; merged local branches removed; tag set;
  temporary files removed; this document.
- 18 Nov: the second cleanup (section 6): old copies on E: to the Recycle Bin, scratch folders removed, stashes and branches dropped, `rebuild-finalv3` merged into `main`, old parts and steps moved to `project/archive/round1/`.
- 18 Nov, later: one repository with a folder per entry (section 7): this project into `2027-round1-goodnight-inn/`, Bjorn's copy into it, the two 2026 builds merged in with their history.
