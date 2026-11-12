"""2x detail crops (logical page coordinates x2) for the reviewer, plus the approved comp."""
import shutil
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
RAW, OUT = HERE / "raw2x", HERE / "review" / "detail"
OUT.mkdir(parents=True, exist_ok=True)
COMP = Path(r"E:\PowerBI_Dataviz_WC27\project\design-prototypes\reference_screenshots")
(HERE / "review" / "comp").mkdir(exist_ok=True)
for f in COMP.glob("*.png"):
    shutil.copyfile(f, HERE / "review" / "comp" / f.name)

P1 = {"header": (0, 0, 1920, 176), "kpi-band": (24, 176, 1872, 136), "F1-margin": (24, 312, 624, 480),
      "F2-middleman": (648, 312, 624, 480), "F3-fading-welcome": (1272, 312, 624, 480), "F4-where-full": (24, 792, 1872, 232),
      "footer": (0, 1016, 1920, 64)}
P2_FIXED = {"header": (0, 0, 1920, 176), "footer": (0, 1016, 1920, 64)}
PANEL, SCATTER = (1080, 176, 816, 848), (24, 176, 1056, 848)


def crop(src, name, box):
    x, y, w, h = box
    Image.open(src).crop((2 * x, 2 * y, 2 * (x + w), 2 * (y + h))).save(OUT / f"{name}@2x.png")


crop(RAW / "01_P1_brand-review@2x.png", "01_P1_header", P1["header"])
for k, b in P1.items():
    crop(RAW / "01_P1_brand-review@2x.png", f"01_P1_{k}", b)
for k, b in P2_FIXED.items():
    crop(RAW / "02_P2_landing_A_Expected@2x.png", f"02_P2_{k}", b)
for f in sorted(RAW.glob("*_P2_*@2x.png")):
    stem = f.name.replace("@2x.png", "")
    crop(f, f"{stem}__panel", PANEL)
    if stem[:2] in ("02", "03", "04", "05", "06", "07", "14"):
        crop(f, f"{stem}__scatter", SCATTER)
print(len(list(OUT.glob("*.png"))), "detail crops")
