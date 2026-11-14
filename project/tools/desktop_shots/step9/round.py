"""One render round of a page-2 state in the THROWAWAY copy (build step 9 of doc 23; never the project, rule 6).

  python round.py copy  <copy dir>                              a fresh throwaway copy of project/pbip (no cache: open it, then
                                                                refresh_desktop_model.ps1 once, about 25 s after opening)
  python round.py view  <copy dir> <state> <scenario> [picked]  the generator's report in <state> (rec, alts, build) into the
                                                                copy, cut into four strips of 480 x 1080 (tiles/mk_tiles.py
                                                                --rows 1); picked: short names separated by commas, "-" for
                                                                nothing picked, left out for the saved selection
  python round.py shoot <pid> <out dir> [name]                  reload, capture the calibration page and the four strips (each
                                                                twice: the first capture after a reload can miss a visual),
                                                                stitch to <out dir>/<name>.png and <name>_1920.png

A round is: view, shoot, then tiles/slotdiff.py <name>.png <comp png> slot,x,y,w,h ... against step9/comp_shots.py.
"""
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHOTS = HERE.parent
ROOT = HERE.parents[3]
PY = sys.executable
PAGE = "p2-investment-strategy"


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
    copy, state, scen = Path(sys.argv[2]), sys.argv[3], sys.argv[4]
    picked = sys.argv[5] if len(sys.argv) > 5 else None
    gen = copy.parent / (copy.name + "_gen")
    if gen.exists():
        shutil.rmtree(gen)
    out = run(PY, ROOT / "project" / "tools" / "opzet_report.py", "--out", gen, *([f"--state={state}"] if state != "rec" else []), cwd=ROOT)
    rep = next(gen.glob("*.Report"))
    for part in ("definition", "StaticResources"):
        dst = copy / "THROWAWAY.Report" / part
        shutil.rmtree(dst)
        shutil.copytree(rep / part, dst)
    args = [PY, SHOTS / "tiles" / "mk_tiles.py", copy / "THROWAWAY.Report", "--page", PAGE, "--scenario", scen, "--mast", "168", "--rows", "1"]
    if picked is not None:
        args += ["--picked", "" if picked == "-" else picked]
    print(out.splitlines()[-1])
    print(run(*args))
elif cmd == "shoot":
    pid, out = sys.argv[2], Path(sys.argv[3])
    name = sys.argv[4] if len(sys.argv) > 4 else "page"
    out.mkdir(parents=True, exist_ok=True)
    print(run("powerbi-desktop.cmd", "reload", "--pid", pid)[:200])
    time.sleep(10)
    cap = lambda page, f: run("node", SHOTS / "cap.mjs", pid, page, "3", f)  # noqa: E731
    cap("t_cal", out / "t_cal.png")
    print(run(PY, SHOTS / "step7" / "find_cal.py", out / "t_cal.png", out / "t_cal.txt"))
    for rnd in range(2):
        for c in range(4):
            cap(f"t_0_{c}", out / f"t_0_{c}.png")
        time.sleep(2)
    print(run(PY, SHOTS / "tiles" / "stitch.py", out, out / "t_cal.txt", out / f"{name}.png", "--rows", "1"))
