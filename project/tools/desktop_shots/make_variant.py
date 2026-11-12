"""Throwaway review copy of GoodnightInn-opzet for Desktop screenshots. Never committed; deleted after the review.

Copies the generated report to GoodnightInn-opzet-review.*, then:
  * every page opens at Actual size (1920 x 1080 CSS px) so the bridge captures at full resolution;
  * applies a P2 bookmark exactly as stored (each target visual hidden/shown per the bookmark JSON), so the render
    shows what clicking the button would show;
  * sets the package-in-focus and scenario slicers.
usage: python make_variant.py <shortlist|plan> <A|B|C|label...> <Low|Expected|High>
"""
import json
import shutil
import sys
from pathlib import Path

PBIP = Path(r"E:\PowerBI_Dataviz_WC27\project\pbip")
NAME, REV = "GoodnightInn-opzet", "GoodnightInn-opzet-review"
P2 = "p2-investment-strategy"
LABELS = {"A": "A · Our recommendation", "B": "B · Breakfast instead of kiosks", "C": "C · Why not renovate? For comparison"}


def rd(p):
    return json.loads(p.read_text(encoding="utf-8"))


def wr(p, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def set_slicer(vj, value):
    v = rd(vj)
    cond = v["visual"]["objects"]["general"][0]["properties"]["filter"]["filter"]["Where"][0]["Condition"]["In"]
    cond["Values"] = [[{"Literal": {"Value": "'" + value.replace("'", "''") + "'"}}]]
    wr(vj, v)


def main(state, focus, scenario, page="p2", view="all"):
    src, dst = PBIP / f"{NAME}.Report", PBIP / f"{REV}.Report"
    assert dst.name.endswith("-review.Report")
    if dst.exists():
        # refresh in place file by file: Desktop holds the folder open between reloads
        for f in sorted(dst.rglob("*"), reverse=True):
            if f.is_file() and ".pbi" not in f.parts:
                f.unlink()
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(".pbi"), dirs_exist_ok=True)
    pbip = rd(PBIP / f"{NAME}.pbip")
    pbip["artifacts"][0]["report"]["path"] = f"{REV}.Report"
    wr(PBIP / f"{REV}.pbip", pbip)
    d = dst / "definition"
    # (Actual size was tried: the bridge then captures only the visible strip, and its region capture refuses the
    #  page because Desktop reports it 20 px taller than logical. Fit-to-page at scale 3 gives ~2300 px wide.)
    bm = rd(d / "bookmarks" / f"bm_p2_{state}.bookmark.json")
    shown, hidden = [], []
    for page, sec in bm["explorationState"]["sections"].items():
        for vname, vc in sec["visualContainers"].items():
            vj = d / "pages" / page / "visuals" / vname / "visual.json"
            v = rd(vj)
            if vc.get("singleVisual", {}).get("display", {}).get("mode") == "hidden":
                v["isHidden"] = True
                hidden.append(vname)
            else:
                v.pop("isHidden", None)
                shown.append(vname)
            wr(vj, v)
    set_slicer(d / "pages" / P2 / "visuals" / "sl_package" / "visual.json", LABELS.get(focus, focus))
    set_slicer(d / "pages" / P2 / "visuals" / "sl_scenario" / "visual.json", scenario)
    set_slicer(d / "pages" / P2 / "visuals" / "sl_view" / "visual.json", "Zoom on A, B, C" if view == "zoom" else "All packages")
    pj = d / "pages" / "pages.json"
    pages = rd(pj)
    pages["activePageName"] = "p1-brand-review" if page == "p1" else P2
    wr(pj, pages)
    print(json.dumps({"state": state, "focus": LABELS.get(focus, focus), "scenario": scenario, "shown": sorted(shown), "hidden": sorted(hidden)}))


if __name__ == "__main__":
    main(*sys.argv[1:6])

