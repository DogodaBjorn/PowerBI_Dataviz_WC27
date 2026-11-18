# Build step 3 · proof renders (13 Nov 2026)

Taken in a throwaway copy (Desktop 2.159, Windows culture nl-NL) on the regenerated model of build step 3
(doc 23). The session's screen was 540 px wide, so each page was captured at about 1000 px: enough to see that every
visual draws, not a pixel reference. No render is compared with the comp in this step; nothing in the report changed.

| File | What it shows |
|---|---|
| `01-p1-current-report-on-new-model.png` | The Brand Review of today's report (FinalV2 with the hover cues) on the new model: every visual draws |
| `02-p2-current-report-on-new-model.png` | The Investment Strategy, Recommended, Expected: every visual draws. The note reads "(F2, F4, F1)": the kiosks answer F4 (D4) |
| `03-f3-label-safe-nl-NL.png` | The F3 chart of the copy bound to `NPS 2025 (label-safe)`: "−4.9" with a decimal point in the Dutch Desktop, while the F4 bars beside it still print "87,4%" |

The numbers themselves are proven by `project/tools/number_checks.py`; its report is `project/analysis/output/number_checks.txt`.
