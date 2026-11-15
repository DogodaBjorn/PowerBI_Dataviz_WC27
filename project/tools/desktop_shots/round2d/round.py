"""Review round 2, step D: one render round of a whole page in the THROWAWAY copy (never the project; doc 23 rule 6).

  python round.py copy  <copy dir>                           a fresh throwaway copy of project/pbip
  python round.py view  <copy dir> [state] [scenario] [picked]   the generator's report into the copy as it is (no strips);
                                                             state rec | alts | build opens page 2 in that state, the
                                                             scenario (Low | Expected | High) is set in the copy's slicer,
                                                             picked (short names separated by semicolons, "-" = nothing)
                                                             in the move selector
  python round.py shoot <pid> <out dir> <name> [page] [card] reload, capture the page whole at scale 3 (twice: the first
                                                             capture after a reload can miss a visual), cut it to page
                                                             pixels: <name>_2x.png (3840 x 2160) and <name>.png (1920 x 1080)

page: p1-brand-review (default) or p2-investment-strategy; card: the white card page_crop.py finds the page by
(page 2 Recommended: 32,168,1040,488).

Only in a WIDE Desktop window (15 Nov: the session's screen was 2248 px, the canvas 1442 x 546 logical px, the page drawn
whole at 1.41 capture px per page px). In a narrow window use the strips of ..\\step9\\round.py.
"""
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHOTS = HERE.parent
ROOT = HERE.parents[3]
PY = sys.executable


def run(*a, **k):
    r = subprocess.run([str(x) for x in a], capture_output=True, text=True, encoding="utf-8", errors="replace", **k)
    if r.returncode:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise SystemExit(f"failed: {a[:3]}")
    return r.stdout.strip()


cmd = sys.argv[1]
if cmd == "copy":
    print(run(PY, SHOTS / "throwaway_copy.py", ROOT / "project" / "pbip", sys.argv[2]))
elif cmd == "view":
    copy = Path(sys.argv[2])
    state = sys.argv[3] if len(sys.argv) > 3 else "rec"
    scen = sys.argv[4] if len(sys.argv) > 4 else None
    gen = copy.parent / (copy.name + "_gen")
    if gen.exists():
        shutil.rmtree(gen)
    out = run(PY, ROOT / "project" / "tools" / "opzet_report.py", "--out", gen, *([f"--state={state}"] if state != "rec" else []), cwd=ROOT)
    rep = next(gen.glob("*.Report"))
    for part in ("definition", "StaticResources"):
        dst = copy / "THROWAWAY.Report" / part
        shutil.rmtree(dst)
        shutil.copytree(rep / part, dst)
    if scen:  # the scenario slicer's saved selection (the copy only)
        f = copy / "THROWAWAY.Report" / "definition" / "pages" / "p2-investment-strategy" / "visuals" / "sl_scenario" / "visual.json"
        txt = f.read_text(encoding="utf-8")
        cur = [s for s in ("Low", "Expected", "High") if f"'{s}'" in txt]
        assert len(cur) == 1, cur
        f.write_text(txt.replace(f"'{cur[0]}'", f"'{scen}'"), encoding="utf-8")
    picked = sys.argv[5] if len(sys.argv) > 5 else None
    if picked is not None:  # the move selector's saved selection (short names separated by semicolons; "-" = nothing picked)
        f = copy / "THROWAWAY.Report" / "definition" / "pages" / "p2-investment-strategy" / "visuals" / "sl_moves" / "visual.json"
        v = json.loads(f.read_text(encoding="utf-8"))
        names = [] if picked == "-" else [n for n in picked.split(";") if n]
        if names:
            v["visual"]["objects"]["general"][0]["properties"]["filter"]["filter"]["Where"][0]["Condition"]["In"]["Values"] = [[{"Literal": {"Value": f"'{n}'"}}] for n in names]
        else:
            v["visual"]["objects"].pop("general", None)
        f.write_text(json.dumps(v, indent=2, ensure_ascii=False), encoding="utf-8")
    print(out.splitlines()[-1], "| state", state, "| scenario", scen or "as saved", "| picked", "as saved" if picked is None else picked)
elif cmd == "shoot":
    pid, out, name = sys.argv[2], Path(sys.argv[3]), sys.argv[4]
    page = sys.argv[5] if len(sys.argv) > 5 else "p1-brand-review"
    card = sys.argv[6] if len(sys.argv) > 6 else None
    out.mkdir(parents=True, exist_ok=True)
    print(run("powerbi-desktop.cmd", "reload", "--pid", pid)[:120].replace("\n", " "))
    time.sleep(10)
    for rnd in range(2):
        run("node", SHOTS / "cap.mjs", pid, page, "3", out / f"{name}_cap.png")
        time.sleep(3)
    print(run(PY, HERE / "page_crop.py", out / f"{name}_cap.png", out / f"{name}_2x.png", *(["--card", card] if card else [])))
    from PIL import Image
    Image.open(out / f"{name}_2x.png").resize((1920, 1080), Image.LANCZOS).save(out / f"{name}.png")
