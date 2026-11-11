import re
from pathlib import Path

d = Path(r"E:\PowerBI_Dataviz_WC27\project\deliverables\screenshots\2026-11-07-desktop")
readme = d / "README.md"
t = readme.read_text(encoding="utf-8")
pngs = {p.stem: p.name for p in d.glob("*.png")}
# table cells like `01_P1_brand-review` -> [01_P1_brand-review](01_P1_brand-review.png)
t = re.sub(r"`([0-9]{2}_[^`]+)`", lambda m: f"[{m.group(1)}]({pngs[m.group(1)]})" if m.group(1) in pngs else m.group(0), t)


# live ranges like `L1a`-`L1c` -> links to each file in the range
def live(m):
    prefix = m.group(1)
    files = sorted(n for s, n in pngs.items() if s.startswith(prefix))
    return " ".join(f"[{n.split('_')[0]}]({n})" for n in files)


t = re.sub(r"`(L[1-4])[a-d]`-`L[1-4][a-d]`", live, t)
t = t.replace("# Desktop screenshots, 7 Nov 2026 (build v2, commit 2a3e6ae)\n",
              "# Desktop screenshots, 7 Nov 2026 (build v2, commit 2a3e6ae)\n\n"
              "**Review of these screenshots: [REVIEW.md](REVIEW.md)** (independent reviewer: 1 blocker, 11 major, "
              "11 minor, 10 polish; the data-dependent findings checked against the model at the top). What the reviewer "
              "was told: [REVIEW-BRIEF.md](REVIEW-BRIEF.md).\n")
readme.write_text(t, encoding="utf-8")
missing = [s for s in pngs if s not in t]
print("links:", t.count(".png)"), "| pngs not linked:", missing)
