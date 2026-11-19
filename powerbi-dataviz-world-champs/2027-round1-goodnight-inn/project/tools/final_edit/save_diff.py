"""Read a Desktop save of the final copy against the repository's report, value by value, and take it in untouched.

  python project/tools/final_edit/save_diff.py                 what differs
  python project/tools/final_edit/save_diff.py --take          the same, then copy the save into the repository

Bjorn saves in Desktop between the agent's rounds. Before any edit: this first, and if it differs, `--take` and a commit
"The report as Bjorn saved it ..., untouched", then the edit on top (docs 32 to 39 of 16 Nov 2026 all start this way).
Desktop rewrites files it did not change (line ends, number forms, layer numbers), so a byte comparison says little:
this compares the JSON values, names what differs per file, and sets apart files in which only the layer or the tab
number changed while the order of the visuals on their page stayed the same. The model is compared measure for measure.
"""
import filecmp
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SAVE = ROOT / "Goodnight Inn - Room to Invest"  # Bjorn's own copy, in the entry folder since 18 Nov 2026
SAVE_REPORT, SAVE_MODEL = SAVE / "Goodnight Inn - Room to Invest.Report", SAVE / "PillowKey.SemanticModel"
REPO_REPORT, REPO_MODEL = ROOT / "project" / "pbip" / "GoodnightInn-final.Report", ROOT / "project" / "pbip" / "PillowKey.SemanticModel"
ORDER_ONLY = ("/position/z", "/position/tabOrder")


def walk(x, y, path, out):
    if type(x) is not type(y) and not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        out.append((path, x, y))
    elif isinstance(x, dict):
        for k in sorted(set(x) | set(y)):
            if k not in x:
                out.append((path + "/" + k, "<absent>", y[k]))
            elif k not in y:
                out.append((path + "/" + k, x[k], "<absent>"))
            else:
                walk(x[k], y[k], path + "/" + k, out)
    elif isinstance(x, list):
        if len(x) != len(y):
            out.append((path, f"list of {len(x)}", f"list of {len(y)}"))
        else:
            for i, (p, q) in enumerate(zip(x, y)):
                walk(p, q, f"{path}[{i}]", out)
    elif x != y:
        out.append((path, x, y))


def files(root):
    return {f.relative_to(root) for f in root.rglob("*") if f.is_file() and ".pbi" not in f.relative_to(root).parts}


def page_order(root, page, key):
    o = []
    for d in (root / "definition" / "pages" / page / "visuals").iterdir():
        p = json.loads((d / "visual.json").read_text(encoding="utf-8-sig"))["position"]
        if key in p:
            o.append((p[key], d.name))
    return [n for _, n in sorted(o)]


def measures(root):
    out = {}
    for f in root.rglob("*.tmdl"):
        for m in re.finditer(r"^\tmeasure (?:'((?:[^']|'')+)'|(\S+)) =(.*)$", f.read_text(encoding="utf-8"), re.M):
            out[m.group(1) or m.group(2)] = re.sub(r"\s+", "", m.group(3))
    return out


a, b = files(SAVE_REPORT), files(REPO_REPORT)
for f in sorted(a - b):
    print("only in the save:", f)
for f in sorted(b - a):
    print("only in the repository:", f)
real, order_only = 0, 0
for f in sorted(a & b):
    if f.suffix != ".json":
        if not filecmp.cmp(SAVE_REPORT / f, REPO_REPORT / f, shallow=False):
            real += 1
            print("differs (not JSON):", f)
        continue
    out = []
    walk(json.loads((SAVE_REPORT / f).read_text(encoding="utf-8-sig")), json.loads((REPO_REPORT / f).read_text(encoding="utf-8-sig")), "", out)
    if not out:
        continue
    if all(p in ORDER_ONLY for p, _, _ in out):
        order_only += 1
        continue
    real += 1
    print("==", f)
    for p, u, v in out[:12]:
        print("   ", p[-110:], "| save:", str(u)[:90], "| repository:", str(v)[:90])
    if len(out) > 12:
        print("    ...", len(out), "differences")
print(f"{real} file(s) differ in content; {order_only} file(s) differ in a layer or tab number only")
if order_only:
    for page in sorted(p.name for p in (SAVE_REPORT / "definition" / "pages").iterdir() if p.is_dir()):
        for key in ("z", "tabOrder"):
            s, r = page_order(SAVE_REPORT, page, key), page_order(REPO_REPORT, page, key) if (REPO_REPORT / "definition" / "pages" / page).exists() else []
            if s != r:
                print(f"  {page}: the {key} ORDER differs:", [n for n in s if n in r and s.index(n) != r.index(n)][:10])
ma, mb = measures(SAVE_MODEL), measures(REPO_MODEL)
print(f"model: {len(ma)} measures in the save, {len(mb)} in the repository; names that differ: {sorted(set(ma) ^ set(mb))[:8]}; "
      f"expressions that differ: {[k for k in ma if k in mb and ma[k] != mb[k]][:8]}")

if "--take" in sys.argv:
    n = 0
    for f in sorted(a):
        if f not in b or not filecmp.cmp(SAVE_REPORT / f, REPO_REPORT / f, shallow=False):
            (REPO_REPORT / f).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(SAVE_REPORT / f, REPO_REPORT / f)
            n += 1
    for f in sorted(b - a):
        (REPO_REPORT / f).unlink()
        n += 1
    for d in sorted((d for d in REPO_REPORT.rglob("*") if d.is_dir()), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()
    print(f"taken: {n} file(s) copied or removed; commit it before editing")
