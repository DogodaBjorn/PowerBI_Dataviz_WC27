"""The committee's walkthrough of the PUBLISHED report: every view a judge can reach, in the order a judge clicks.

usage: python walk.py <publish-to-web url> <work dir> <out dir>

Drives ..\\step12\\web.mjs (headless Edge, signed out, a fresh profile per run, en-US) and writes into <out dir>:
  01 to 23 .png   the report page at 1920 x 1080 as the browser draws it (22: the whole 1366 x 768 window)
  zoom/           the left and the right half of the four main views at 2 device px per page px (small text)
  texts/          every visible text and every aria-label of the main views, one per line
  link.txt        which report and which publish the link served during the run
The link is never written into the repository: pass it on the command line.
Coordinates are the report's own 1920 x 1080 (slot map v10; the same ones as ..\\step12\\plan.py).
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
WEB = HERE.parent / "step12" / "web.mjs"
URL, WORK, OUT = sys.argv[1], Path(sys.argv[2]).resolve(), Path(sys.argv[3]).resolve()
for d in (WORK, OUT, OUT / "zoom", OUT / "texts"):
    d.mkdir(parents=True, exist_ok=True)

NEXT = (1552, 1058)
TAB = {"rec": (1332, 80), "alts": (1556, 80), "build": (1780, 80)}
SCEN = {"low": (1648, 128), "expected": (1744, 128), "high": (1840, 128)}
PARK = (1912, 600)  # the page's right margin: no visual, no bubble, no header strip
ROW = {n: (900, 296 + 32 * i) for i, n in enumerate(
    ["booking", "revenue", "kiosks", "breakfast", "gatwick", "toronto", "kingston", "energy", "boston", "refresh"])}


class Run:
    def __init__(self, name, args):
        self.name, self.args = name, args
        self.steps = [{"op": "ready"}, {"op": "meta"}, {"op": "wait", "ms": 3000}]

    def wait(self, ms): self.steps.append({"op": "wait", "ms": ms})
    def move(self, xy): self.steps.append({"op": "pmove", "lx": xy[0], "ly": xy[1]})

    def click(self, xy, ms=4500):
        self.steps.append({"op": "pclick", "lx": xy[0], "ly": xy[1]}); self.wait(ms)

    def shot(self, name, whole=False):
        self.move(PARK); self.wait(900)
        self.steps.append({"op": "shot" if whole else "pshot", "out": str(WORK / f"{name}.png").replace("\\", "/")})

    def texts(self, name):
        self.steps.append({"op": "texts", "out": str(OUT / "texts" / f"{name}.txt").replace("\\", "/")})

    def hover(self, name, x, y):
        self.move((x - 6, y - 4)); self.wait(300); self.move((x, y)); self.wait(2800)
        self.steps.append({"op": "pshot", "out": str(WORK / f"{name}.png").replace("\\", "/")})
        self.move(PARK); self.wait(700)

    def file(self):
        f = WORK / f"steps_{self.name}.json"
        f.write_text(json.dumps(self.steps), encoding="utf-8")
        return str(f)


W1 = ["--w", "1920", "--h", "1180"]
runs = []

r = Run("p1", W1); runs.append(r)
r.shot("01_p1-brand-review"); r.texts("01_p1-brand-review")
r.hover("02_p1-tooltip-f3-oldest-band", 1770, 525)
r.hover("03_p1-tooltip-f4-toronto", 1735, 891)
r.hover("04_p1-tooltip-definitions", 1816, 1058)
r.click((760, 620), 3500); r.shot("23_p1-row-clicked")

r = Run("rec", W1); runs.append(r)
r.click(NEXT, 7000); r.shot("05_p2-recommended-expected"); r.texts("05_p2-recommended-expected")
r.hover("08_p2-recommended-tooltip-year", 1500, 900)
for s, n in (("low", "06"), ("high", "07")):
    r.click(SCEN[s], 5000); r.shot(f"{n}_p2-recommended-{s}"); r.texts(f"{n}_p2-recommended-{s}")

r = Run("alts", W1); runs.append(r)
r.click(NEXT, 7000); r.click(TAB["alts"], 5000)
r.shot("09_p2-what-waits-expected"); r.texts("09_p2-what-waits-expected")
r.hover("12_p2-what-waits-tooltip-a", 188, 345)
r.hover("13_p2-what-waits-tooltip-c", 465, 448)
r.hover("14_p2-what-waits-tooltip-grey-package", 315, 394)
r.hover("15_p2-what-waits-tooltip-year", 1055, 860)
for s, n in (("low", "10"), ("high", "11")):
    r.click(SCEN[s], 5000); r.shot(f"{n}_p2-what-waits-{s}"); r.texts(f"{n}_p2-what-waits-{s}")

r = Run("build", W1); runs.append(r)
r.click(NEXT, 7000); r.click(TAB["build"], 5000)
r.shot("16_p2-build-opening-package-a"); r.texts("16_p2-build-opening-package-a")
for m in ("breakfast", "gatwick", "toronto"):
    r.click(ROW[m])
r.shot("17_p2-build-six-moves"); r.texts("17_p2-build-six-moves")
r.hover("18_p2-build-tooltip-your-plan", 355, 376)  # the dot "You" with these six moves picked
for m in ("kingston", "energy"):
    r.click(ROW[m])
r.shot("19_p2-build-eight-moves"); r.texts("19_p2-build-eight-moves")
for m in ("booking", "revenue", "kiosks", "breakfast", "gatwick", "toronto", "kingston", "boston", "refresh"):
    r.click(ROW[m])
r.shot("20_p2-build-over-budget"); r.texts("20_p2-build-over-budget")
for m in ("energy", "boston", "refresh"):
    r.click(ROW[m])
r.shot("21_p2-build-nothing-picked"); r.texts("21_p2-build-nothing-picked")

r = Run("w1366", ["--w", "1366", "--h", "768"]); runs.append(r)
r.click(NEXT, 7000); r.shot("22_p2-recommended-1366px-window", whole=True)

Z = ["--w", "1920", "--h", "1180", "--dsf", "2"]
r = Run("z1", Z); runs.append(r)
r.shot("z_01_p1-brand-review")
r.click(NEXT, 7000); r.shot("z_05_p2-recommended-expected")
r = Run("z2", Z); runs.append(r)
r.click(NEXT, 7000); r.click(TAB["alts"], 5000); r.shot("z_09_p2-what-waits-expected")
r.click(TAB["build"], 5000); r.shot("z_16_p2-build-opening-package-a")


def go(i, run):
    p = subprocess.run(["node", str(WEB), URL, run.file(), *run.args, "--port", str(9620 + i)],
                       capture_output=True, text=True, encoding="utf-8", timeout=1200)
    (WORK / f"log_{run.name}.txt").write_text(p.stdout + p.stderr, encoding="utf-8")
    return run.name, p.stdout


with ThreadPoolExecutor(4) as ex:
    logs = dict(ex.map(lambda a: go(*a), enumerate(runs)))

metas = {n: next((json.loads(l) for l in o.splitlines() if l.startswith('{"op":"meta"')), None) for n, o in logs.items()}
m = next(v for v in metas.values() if v)
same = all(v and v.get("lastPublished") == m.get("lastPublished") for v in metas.values())
(OUT / "link.txt").write_text(
    f"report: {m.get('report')}\nlast published (UTC): {m.get('lastPublished')}\n"
    f"pages: {', '.join(m.get('pages', []))}\nevery run saw this publish: {'yes' if same else 'NO'}\n", encoding="utf-8")

for f in sorted(WORK.glob("*.png")):
    im = Image.open(f).convert("RGB")
    if f.name.startswith("z_"):
        w, h = im.size
        im.crop((0, 0, w // 2, h)).save(OUT / "zoom" / f"{f.stem[2:]}_left.png", optimize=True)
        im.crop((w // 2, 0, w, h)).save(OUT / "zoom" / f"{f.stem[2:]}_right.png", optimize=True)
    else:
        im.save(OUT / f.name, optimize=True)
    print(f.name, im.size)
print((OUT / "link.txt").read_text(encoding="utf-8"))
