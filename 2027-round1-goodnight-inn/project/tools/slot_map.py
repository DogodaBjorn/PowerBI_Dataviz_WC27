"""The slot map the generators read (doc 23 rule 9, the layout switch page by page).

Build step 5 copied opzet-layout-v10.json over opzet-layout.json and kept the old map as opzet-layout-v9.json; page 2
and the tooltip pages only the old page 2 used (tt-f1 to tt-f4, the 'Revisit the facts' chips) were still read from v9.
Build step 6 moved page 2 over: V9_PAGES is empty, every page comes from opzet-layout.json and the v9 file is no longer
read (it stays in the folder as the record of FinalV2's layout).
"""
import json
from pathlib import Path

DP = Path(__file__).resolve().parents[1] / "design-prototypes"
V9_PAGES = ()


def load_layout():
    cur = json.loads((DP / "opzet-layout.json").read_text(encoding="utf-8"))
    if not V9_PAGES:
        return cur
    old = {p["name"]: p for p in json.loads((DP / "opzet-layout-v9.json").read_text(encoding="utf-8"))["pages"]}
    pages = [old[p["name"]] if p["name"] in V9_PAGES else p for p in cur["pages"]]
    names = {p["name"] for p in pages}
    pages += [old[n] for n in V9_PAGES if n in old and n not in names]
    return {**cur, "pages": pages}
