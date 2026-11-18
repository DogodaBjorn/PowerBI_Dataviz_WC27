"""Build step 10: what a screen reader hears on a report page, in the order of the page's elements, from a dump of
a11y_pass.ps1 -Do names. The visuals of the page are the elements one level under the canvas (the level of the logo,
'Goodnight Inn'): each is listed with its role as Desktop names it and its spoken name; --cells adds the cells inside
tables and the tiles inside slicers (the level a reader reaches with Enter; the 456 points of the scatter are left out).

  python spoken.py <dump.txt> [--cells] [--width N]
"""
import re
import sys

lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
cells = "--cells" in sys.argv
width = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 400
pat = re.compile(r"^\s*(\d+) \[(\w+)/([^\]]*)\] '(.*)'(.*)$")
rows = []
for ln in lines:
    m = pat.match(ln)
    if m:
        rows.append((int(m.group(1)), m.group(2), m.group(3), m.group(4), m.group(5)))
start = next(i for i, r in enumerate(rows) if r[3].strip() == "Goodnight Inn" and r[1] in ("Image", "Group"))
depth = rows[start][0]
n = 0
inside = ""
for d, ctype, local, name, rest in rows[start:]:
    if d < depth:
        break
    name = name.replace("⁠", "").strip()
    if d == depth:
        n += 1
        inside = local
        # Desktop's edit mode marks every visual focusable, so the dump cannot tell a tab stop from a decorative
        # visual: an element without a name is one the generator took out of the tab order (a11y_check.py holds that)
        print(f"{n:>3} {local:<24} {len(name):>4}  {name[:width] if name else '(no name: decorative)'}")
    elif cells and name and ("abel" in inside or "licer" in inside) and "schuiven" not in name and "scrollen" not in name and ctype in ("DataItem", "Button", "ListItem", "Header", "HeaderItem", "Text", "CheckBox") and d <= depth + 6:
        state = "".join(x for x in re.findall(r" (?:toggle|selected)=\w+", rest))
        print(f"      {'  ' * (d - depth - 1)}{local} '{name[:width]}'{state}")
