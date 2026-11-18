"""A throwaway copy of the project for Desktop work (doc 23 rule 6): the project itself is never opened for checks.

Usage: python throwaway_copy.py <project pbip dir> <destination dir> [--keep-cache] [--name STEM]

Copies GoodnightInn-opzet.Report and PillowKey.SemanticModel to <destination>, with the report folder and the
.pbip sharing one stem (default THROWAWAY), because `powerbi-desktop reload` finds the report folder by the .pbip's
name. The Desktop caches (.pbi folders) are left out unless --keep-cache is given: after a MODEL change the copy
must open without them and be refreshed once ('Nu vernieuwen' in the banner, or refresh_desktop_model.ps1 -Port);
with the old cache Desktop keeps the old calculated tables.
"""
import shutil
import sys
from pathlib import Path

args = [a for a in sys.argv[1:] if not a.startswith("--")]
SRC, DST = Path(args[0]), Path(args[1])
KEEP = "--keep-cache" in sys.argv
STEM = sys.argv[sys.argv.index("--name") + 1] if "--name" in sys.argv else "THROWAWAY"
if "--name" in sys.argv:
    args.remove(STEM)
SRC_REPORT, MODEL = "GoodnightInn-opzet.Report", "PillowKey.SemanticModel"

if DST.exists():
    shutil.rmtree(DST)
DST.mkdir(parents=True)
skip = (lambda d, names: []) if KEEP else (lambda d, names: [n for n in names if n == ".pbi"])
shutil.copytree(SRC / SRC_REPORT, DST / f"{STEM}.Report", ignore=skip)
shutil.copytree(SRC / MODEL, DST / MODEL, ignore=skip)
pbip = (SRC / "GoodnightInn-opzet.pbip").read_text(encoding="utf-8").replace(SRC_REPORT, f"{STEM}.Report")
(DST / f"{STEM}.pbip").write_text(pbip, encoding="utf-8")
print(f"copy written: {DST / (STEM + '.pbip')}" + ("" if KEEP else " (no cache: refresh once after opening)"))
