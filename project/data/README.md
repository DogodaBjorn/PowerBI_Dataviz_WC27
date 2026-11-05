# Contest data (local only)

Nothing in this folder is committed except this file. Put here:

| File | Source |
|---|---|
| `PillowKey_Starter.pbix` | https://datavizcontests.blob.core.windows.net/worldchamps-atl27/PillowKey_Starter.pbix |
| `PillowKey_Dataset.xlsx` (optional local copy) | https://datavizcontests.blob.core.windows.net/worldchamps-atl27/PillowKey_Dataset.xlsx — the model's `DataFile` parameter points at this public URL; keep a local copy as fallback |
| `round-1-blog-page.mht` | the Round 1 post, saved from community.fabric.microsoft.com (text version in `project/contest/`) |
| Official Rules PDF | linked from the post (`project/contest/round-1-links.txt`); read it for the deadline time zone and the contest tag |

The parquet exports produced by `project/analysis/02_export_tables.py` can live in
`project/analysis/data/` (also ignored).
