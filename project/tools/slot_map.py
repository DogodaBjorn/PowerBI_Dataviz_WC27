"""The slot map the generators read (doc 23 rule 9, the layout switch page by page).

Build step 5 copied opzet-layout-v10.json over opzet-layout.json and kept the old map as opzet-layout-v9.json. Until
step 6 moves page 2 over, page 2 and the tooltip pages only page 2 still uses (tt-f1 to tt-f4, the 'Revisit the facts'
chips) are read from v9; everything else from the current map. Step 6 empties V9_PAGES and the merge does nothing.
"""
import json
from pathlib import Path

DP = Path(__file__).resolve().parents[1] / "design-prototypes"
V9_PAGES = ("p2-investment-strategy", "tt-f1", "tt-f2", "tt-f3", "tt-f4")


def load_layout():
    cur = json.loads((DP / "opzet-layout.json").read_text(encoding="utf-8"))
    if not V9_PAGES:
        return cur
    old = {p["name"]: p for p in json.loads((DP / "opzet-layout-v9.json").read_text(encoding="utf-8"))["pages"]}
    pages = [old[p["name"]] if p["name"] in V9_PAGES else p for p in cur["pages"]]
    names = {p["name"] for p in pages}
    pages += [old[n] for n in V9_PAGES if n in old and n not in names]
    return {**cur, "pages": pages}
