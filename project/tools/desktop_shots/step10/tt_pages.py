"""Build step 10 of doc 23: the tooltip pages as they open on a hover, rendered as ordinary pages of the THROWAWAY copy.

A tooltip page shows nothing without the hovered item, and the Desktop Bridge captures pages, not hovers. So each view
becomes a scratch page r_<view> in the copy: the tooltip page's own visuals, the page type dropped (an ordinary page,
fitted to the window), and the hover's context as page filters (the package, the year, the band, the hotel, the case).

  python tt_pages.py <copy dir>          refresh the copy's report from project/pbip (file by file) and write the views
  then: powerbi-desktop reload --pid <pid>; node ../cap.mjs <pid> r_<view> 3 <out>.png   (the views are printed)

Never run it on project/pbip (doc 23 rule 6).
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "project" / "tools"))
from pbir_lib import filter_in  # noqa: E402

SRC = ROOT / "project" / "pbip" / "GoodnightInn-opzet.Report"
COPY = Path(sys.argv[1])
DST = COPY / "THROWAWAY.Report"
assert DST.exists() and "pbip" not in DST.parts, DST

GI = filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_r_brand")


def case(c):
    return filter_in("Scenario", "Scenario", [c], "flt_r_case")


def pkg(i):
    return filter_in("Package", "PackageID", [i], "flt_r_pkg")


A, B, C, EIGHT = "01+02+10", "01+09+10", "01+07+10", "01+02+03+04+05+06+09+10"  # Package[Preset] A, B, C; one of the two packages of eight moves
VIEWS = [  # view, tooltip page, filters
    ("pkg_a_expected", "tt-package", [pkg(A), case("Expected")]),
    ("pkg_a_low", "tt-package", [pkg(A), case("Low")]),
    ("pkg_b_expected", "tt-package", [pkg(B), case("Expected")]),
    ("pkg_c_expected", "tt-package", [pkg(C), case("Expected")]),
    ("pkg_eight_expected", "tt-package", [pkg(EIGHT), case("Expected")]),
    ("year_2030_expected", "tt-year", [filter_in("Date", "Year", [2030], "flt_r_year"), case("Expected")]),
    ("band_oldest", "tt-f3-band", [GI, filter_in("Hotels", "Renovation Age Sort", [3], "flt_r_band")]),
    ("hotel_gatwick", "tt-f4-hotel", [GI, filter_in("Hotels", "HotelID", ["GI027"], "flt_r_hotel")]),
    ("glossary", "tt-glossary", []),
]

shutil.copytree(SRC, DST, dirs_exist_ok=True, ignore=lambda d, names: [n for n in names if n == ".pbi"])
pages_dir = DST / "definition" / "pages"
for old in pages_dir.glob("r_*"):
    shutil.rmtree(old)
order = json.loads((pages_dir / "pages.json").read_text(encoding="utf-8"))
order["pageOrder"] = [p for p in order["pageOrder"] if not p.startswith("r_")]
for view, src_page, filters in VIEWS:
    name = f"r_{view}"
    shutil.copytree(pages_dir / src_page, pages_dir / name)
    pj = json.loads((pages_dir / name / "page.json").read_text(encoding="utf-8"))
    for k in ("type", "visibility", "pageBinding"):
        pj.pop(k, None)
    pj.update({"name": name, "displayName": name, "displayOption": "FitToPage"})
    if filters:
        pj["filterConfig"] = {"filters": filters}
    else:
        pj.pop("filterConfig", None)
    (pages_dir / name / "page.json").write_text(json.dumps(pj, indent=2, ensure_ascii=False), encoding="utf-8")
    order["pageOrder"].append(name)
    print(name, pj["width"], pj["height"])
(pages_dir / "pages.json").write_text(json.dumps(order, indent=2, ensure_ascii=False), encoding="utf-8")
