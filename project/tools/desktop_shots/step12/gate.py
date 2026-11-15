"""Build step 12 of doc 23: the whole Publish to Web gate in one run, against a published link.

usage: python gate.py <url> <out dir> [--ref <dir of an earlier gate run>] [--only hit,clicks,...]

Runs web.mjs with the plans of plan.py (four browsers at a time, each signed out with a fresh profile) and prints one
summary: which report the link shows, the mouse hit test at 1920 and 1366 px (hit_test.js), what a click changes
outside the visual that was clicked, the Dutch and German captures against the English ones, the Tab order, and,
with --ref, every page capture against the same capture of an earlier run (a render repeats to the pixel).
The captures stay in <out dir>; the judgement of the tooltips' and the pages' look is by eye, on those files.
"""
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from PIL import Image, ImageChops

HERE = Path(__file__).resolve().parent
URL, OUT = sys.argv[1], Path(sys.argv[2]).resolve()
REF = Path(sys.argv[sys.argv.index("--ref") + 1]).resolve() if "--ref" in sys.argv else None
ONLY = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
REPORT = HERE.parents[2] / "pbip" / "GoodnightInn-opzet.Report"
OUT.mkdir(parents=True, exist_ok=True)
P = lambda n: str(OUT / n).replace("\\", "/")


def hit_steps(tag):
    h = lambda n: {"op": "evalfile", "file": str(HERE / "hit_test.js").replace("\\", "/"), "out": P(f"{tag}_{n}.json")}
    c = lambda x, y, ms=5000: [{"op": "pclick", "lx": x, "ly": y}, {"op": "wait", "ms": ms}]
    s = [{"op": "ready"}, {"op": "meta"}, {"op": "wait", "ms": 3000}, h("p1")]
    s += c(1552, 1058, 8000) + [h("p2_rec")] + c(1556, 76) + [h("p2_alts")] + c(1780, 76) + [h("p2_build")]
    f = OUT / f"{tag}.json"; f.write_text(json.dumps(s), encoding="utf-8")
    return str(f)


def plan(run, tag):
    return subprocess.run([sys.executable, str(HERE / "plan.py"), str(OUT), run, tag], capture_output=True, text=True).stdout.strip()


JOBS = [  # name, steps file, web.mjs arguments
    ("hit", lambda: hit_steps("hit"), ["--w", "1920", "--h", "1180"]),
    ("hit1366", lambda: hit_steps("hit1366"), ["--w", "1366", "--h", "768"]),
    ("clicks", lambda: plan("clicks", "en"), ["--w", "1920", "--h", "1180"]),
    ("en_p1", lambda: plan("p1", "en"), ["--w", "1920", "--h", "1180"]),
    ("en_p2", lambda: plan("p2", "en"), ["--w", "1920", "--h", "1180"]),
    ("en_states", lambda: plan("states", "en"), ["--w", "1920", "--h", "1180"]),
    ("en_more", lambda: plan("more", "en"), ["--w", "1920", "--h", "1180"]),
    ("keys", lambda: plan("keys", "en"), ["--w", "1920", "--h", "1180"]),
    ("keys2", lambda: plan("keys2", "en"), ["--w", "1920", "--h", "1180"]),
    ("nl_p1", lambda: plan("p1", "nl"), ["--lang", "nl-NL", "--w", "1920", "--h", "1180"]),
    ("nl_p2", lambda: plan("p2", "nl"), ["--lang", "nl-NL", "--w", "1920", "--h", "1180"]),
    ("nl_more", lambda: plan("more", "nl"), ["--lang", "nl-NL", "--w", "1920", "--h", "1180"]),
    ("de_p1", lambda: plan("p1", "de"), ["--lang", "de-DE", "--w", "1920", "--h", "1180"]),
    ("de_p2", lambda: plan("p2", "de"), ["--lang", "de-DE", "--w", "1920", "--h", "1180"]),
    ("de_more", lambda: plan("more", "de"), ["--lang", "de-DE", "--w", "1920", "--h", "1180"]),
    ("w1366", lambda: plan("tips", "w1366"), ["--w", "1366", "--h", "768"]),
    ("touch", lambda: plan("touch", "touch"), ["--w", "1366", "--h", "768", "--touch"]),
]


def run(i, job):
    name, steps, args = job
    r = subprocess.run(["node", str(HERE / "web.mjs"), URL, steps(), *args, "--port", str(9500 + i)], capture_output=True, text=True, encoding="utf-8", timeout=900)
    (OUT / f"log_{name}.txt").write_text(r.stdout + r.stderr, encoding="utf-8")
    return name, r.stdout


jobs = [j for j in JOBS if not ONLY or j[0] in ONLY]
with ThreadPoolExecutor(4) as ex:
    logs = dict(ex.map(lambda a: run(*a), enumerate(jobs)))


def page_of(name):
    im = Image.open(OUT / name).convert("RGB")
    return im.crop((0, 30, 1920, 1110)) if im.size == (1920, 1180) else im


def changed(a, b):
    d = ImageChops.difference(a, b)
    bb = d.getbbox()
    n = sum(d.convert("L").point(lambda v: 1 if v > 24 else 0).histogram()[1:2]) if bb else 0
    return bb, n


print("== the link")
for name, out in logs.items():
    meta = next((json.loads(l) for l in out.splitlines() if l.startswith('{"op":"meta"')), None)
    if meta:
        print(f"  report {meta.get('report')!r}, last published {meta.get('lastPublished')} UTC, {len(meta.get('pages', []))} pages"); break

for tag, label in (("hit", "1920 px"), ("hit1366", "1366 px")):
    if tag not in logs:
        continue
    print(f"== the mouse at {label} (hit_test.js: live visuals and their marks)")
    for st, pg, bm in (("p1", "p1-brand-review", None), ("p2_rec", "p2-investment-strategy", "bm_p2_rec"), ("p2_alts", "p2-investment-strategy", "bm_p2_alts"), ("p2_build", "p2-investment-strategy", "bm_p2_build")):
        f = OUT / f"{tag}_{st}.json"
        if not f.exists():
            print(f"  {st}: no result"); continue
        r = subprocess.run([sys.executable, str(HERE / "hit_report.py"), str(f), str(REPORT), pg] + (["--state", bm] if bm else []),
                           capture_output=True, text=True, encoding="utf-8", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
        lines = [l for l in r.stdout.splitlines() if l.strip()]
        print(f"  {st}: " + (lines[-1] if lines else r.stderr[-300:]))
        for l in lines[1:-1]:
            print("     " + l.strip()[:190])

if "clicks" in logs:
    print("== a click on a mark or a row: what changes on the page (the whole page, before and after)")
    for b in sorted(OUT.glob("en_ck_*_before.png")):
        a = Path(str(b).replace("_before", "_after"))
        if a.exists():
            bb, n = changed(Image.open(a).convert("RGB"), Image.open(b).convert("RGB"))
            print(f"  {b.name[6:-11]:20} changed box {bb}, {n} pixels")

# The band: a clicked chart or table keeps a light band in its header strip. What stands there must look the same
# before and after the click (page coordinates of the line above each visual, left of the header's two icons).
BANDS = [("p1_folio_row", "the years under F2's chart", (680, 505, 1190, 543)), ("p1_f3_bar", "F3's title", (1304, 347, 1800, 391)),
         ("p1_f4_dot", "F4's title", (56, 835, 1690, 862)), ("rec_hero_row", "the hero's column labels", (574, 216, 925, 240)),
         ("rec_ledger_row", "the lines above the ledger", (1112, 310, 1800, 361)), ("rec_cum_line", "the plan bar", (792, 788, 1800, 820)),
         ("rec_cum_line", "the plan chart's caption", (864, 820, 1380, 846)),  # review round 2, step C
         ("alts_waits_row", "the head of What waits", (792, 184, 1800, 237)), ("build_moves_row", "the head of Build", (792, 184, 1300, 237)),
         ("build_bar", "the rules line above the bars", (1384, 408, 1800, 456))]
if "clicks" in logs:
    print("== the band of a clicked visual: the line above it, before and after the click")
    for name, what, box in BANDS:
        a, b_ = OUT / f"en_ck_{name}_after.png", OUT / f"en_ck_{name}_before.png"
        if a.exists() and b_.exists():
            d = ImageChops.difference(Image.open(a).convert("RGB").crop(box), Image.open(b_).convert("RGB").crop(box)).convert("L").point(lambda v: 255 if v > 24 else 0)
            print(f"  {what:32} " + ("unchanged" if not d.getbbox() else f"CHANGED inside {d.getbbox()} of {box}"))

print("== nl and de against en (the page, pixel for pixel)")
for f in sorted(OUT.glob("en_p*.png")):
    for loc in ("nl", "de"):
        o = OUT / f.name.replace("en_", loc + "_", 1)
        if o.exists():
            bb, n = changed(page_of(f.name), page_of(o.name))
            if bb:
                print(f"  {o.name}: differs in {bb}, {n} pixels")
print("  (every pair not listed is equal)")

if "keys" in logs:
    print("== Tab after Ctrl+Enter")
    stops = [json.loads(l)["value"] for l in logs["keys"].splitlines() if l.startswith('{"op":"focus"')]
    for s in stops[2:9]:
        print("  ", (s or {}).get("role"), "|", ((s or {}).get("name") or "").strip()[:80])

if "keys2" in logs:
    # Review round 2, step E (J-AC-8, J-AC-4). Every stop of the walk has a role and a spoken name; a stop without a name
    # is a visual that should be out of the tab order (the scatter's helper layers, the F4 averages): none may appear.
    print("== the keyboard walk in the published report (keys2: the whole list is in keys2_walk.txt)")
    part, parts = None, {}
    for l in logs["keys2"].splitlines():
        if l.startswith('{"op":"eval"') and '"walk:' in l:
            part = json.loads(l)["value"][5:]; parts[part] = []
        elif part and l.startswith('{"op":"focus"'):
            parts[part].append(json.loads(l)["value"] or {})
        elif part and l.startswith('{"op":"tabto"'):
            t = json.loads(l); parts[part].append({"tabto": t["match"], "presses": t["presses"], **(t["value"] or {"name": None})})
    lines = []
    for part, stops in parts.items():
        names = [((s.get("name") or "").strip(), s.get("role"), s.get("tag")) for s in stops if "tabto" not in s]
        seen = list(dict.fromkeys(names))
        nameless = [n for n in seen if not n[0]]
        reached = next((s for s in stops if "tabto" in s), None)
        head = f"  {part}: {len(names)} key presses, {len(seen)} different stops, {len(nameless)} without a name"
        if reached:
            head += f"; reached after {reached['presses']} Tab: " + (repr((reached.get('name') or '')[:60]) if reached.get("name") else "NOT REACHED")
        print(head + (f"  <-- nameless: {nameless[:4]}" if nameless else ""))
        lines.append(part)
        lines += [f"    {'tabto ' + s['tabto'] + ' -> ' if 'tabto' in s else ''}{s.get('role')} | {s.get('tag')} | {(s.get('name') or '').strip()[:110]}" for s in stops]
    (OUT / "keys2_walk.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")

if REF:
    print(f"== against {REF.name} (page captures of the same view)")
    for f in sorted(OUT.glob("*.png")):
        r = REF / f.name
        if r.exists() and ("_tt_" not in f.name) and ("_ck_" not in f.name):
            A, B = Image.open(f).convert("RGB"), Image.open(r).convert("RGB")
            if A.size != B.size:
                print(f"  {f.name}: size {A.size} against {B.size}"); continue
            bb, n = changed(A, B)
            print(f"  {f.name}: " + ("equal" if not bb else f"differs in {bb}, {n} pixels"))
