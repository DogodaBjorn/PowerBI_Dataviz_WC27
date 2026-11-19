"""Reken performance-KPI's zelf door vanuit ruwe aantallen. Alleen standaardbibliotheek.

Gebruik:
  python -I scripts/kpi_calc.py data.csv [--target-cpa 4.0] [--by Channel,Format]
         [--map spend="Spend, $",conv="First rides"] [--id ID]

Herkent kolommen op naam (hoofdletterongevoelig): spend/cost, impressions, clicks,
installs, conversions/purchases/leads/rides, revenue/value, en een aangeleverde CPA.
Ontbreken conversies maar staat er een CPA, dan conversies = spend / CPA (afgeleid, gemarkeerd).
Schrijft <bestand>-kpis.csv naast de invoer.
"""
import argparse
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path

PATTERNS = {
    "spend": ["spend", "cost", "kosten", "uitgaven"],
    "impr": ["impressions", "impr", "vertoningen"],
    "clicks": ["clicks", "klikken"],
    "installs": ["installs", "install"],
    "conv": ["conversions", "conv", "purchases", "leads", "rides", "orders", "aankopen"],
    "revenue": ["revenue", "value", "omzet", "conv. value"],
    "cpa": ["cpa", "cost per"],
}


def num(v):
    if v is None:
        return None
    s = str(v).strip().replace("$", "").replace("€", "").replace("%", "").replace(" ", "")
    if not s:
        return None
    if s.count(",") and s.count("."):
        s = s.replace(",", "")
    elif s.count(",") == 1 and len(s.split(",")[1]) != 3:
        s = s.replace(",", ".")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        return None


def detect(headers, overrides):
    found = {}
    for key, col in overrides.items():
        found[key] = col
    for key, pats in PATTERNS.items():
        if key in found:
            continue
        for h in headers:
            hl = h.lower()
            if h in found.values():
                continue
            if key == "conv" and ("cpa" in hl or "cvr" in hl or "rate" in hl):
                continue
            if key == "cpa" and not hl.startswith(("cpa", "cost per")):
                continue
            if any(p in hl for p in pats):
                found[key] = h
                break
    return found


def div(a, b, scale=1.0):
    if a is None or b in (None, 0):
        return None
    return a / b * scale


def pearson(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(pairs)
    if n < 4:
        return None, n
    mx = sum(p[0] for p in pairs) / n
    my = sum(p[1] for p in pairs) / n
    sxy = sum((x - mx) * (y - my) for x, y in pairs)
    sxx = sum((x - mx) ** 2 for x, _ in pairs)
    syy = sum((y - my) ** 2 for _, y in pairs)
    if sxx == 0 or syy == 0:
        return None, n
    return sxy / math.sqrt(sxx * syy), n


def fmt(v, d=2):
    return "" if v is None else f"{v:,.{d}f}"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--target-cpa", type=float)
    ap.add_argument("--by", help="kolommen om op te groeperen, komma-gescheiden")
    ap.add_argument("--map", default="", help='key=kolom,... keys: spend,impr,clicks,installs,conv,revenue,cpa')
    ap.add_argument("--id", help="ID-kolom (default: eerste kolom)")
    a = ap.parse_args()

    src = Path(a.csv)
    with open(src, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t")
        rows = list(csv.DictReader(f, dialect=dialect))
    if not rows:
        sys.exit("Leeg bestand")
    headers = list(rows[0].keys())
    overrides = dict(kv.split("=", 1) for kv in a.map.split(",") if "=" in kv)
    cols = detect(headers, overrides)
    idcol = a.id or headers[0]
    print("Kolommen:", ", ".join(f"{k}={v}" for k, v in cols.items()))

    out, flags = [], []
    for r in rows:
        g = {k: num(r.get(c)) for k, c in cols.items()}
        derived = False
        if g.get("conv") is None and g.get("cpa") and g.get("spend") is not None:
            g["conv"] = g["spend"] / g["cpa"]
            derived = True
        rid = r.get(idcol, "")
        m = {
            "id": rid,
            "spend": g.get("spend"), "impr": g.get("impr"), "clicks": g.get("clicks"),
            "installs": g.get("installs"), "conv": g.get("conv"), "revenue": g.get("revenue"),
            "CPM": div(g.get("spend"), g.get("impr"), 1000),
            "CTR%": div(g.get("clicks"), g.get("impr"), 100),
            "CPC": div(g.get("spend"), g.get("clicks")),
            "CVR%": div(g.get("installs") or g.get("conv"), g.get("clicks"), 100),
            "CPI": div(g.get("spend"), g.get("installs")),
            "IPM": div(g.get("installs"), g.get("impr"), 1000),
            "CPA": div(g.get("spend"), g.get("conv")),
            "act%": div(g.get("conv"), g.get("installs"), 100),
            "ROAS": div(g.get("revenue"), g.get("spend")),
            "_row": r, "_derived": derived,
        }
        if g.get("installs") and g.get("conv") and g["conv"] > g["installs"]:
            flags.append(f"{rid}: meer conversies ({g['conv']:.0f}) dan installs ({g['installs']:.0f}) -> onmogelijk, uitsluiten")
        if g.get("clicks") and g.get("impr") and g["clicks"] > g["impr"]:
            flags.append(f"{rid}: meer klikken dan impressies")
        if g.get("installs") and g.get("clicks") and g["installs"] > g["clicks"] * 1.5:
            flags.append(f"{rid}: installs > 1,5x klikken (view-through of datafout?)")
        out.append(m)

    bad = {f.split(":")[0] for f in flags if "onmogelijk" in f}
    valid = [m for m in out if m["id"] not in bad]

    keys = ["spend", "impr", "clicks", "installs", "conv", "CPM", "CTR%", "CPC", "CVR%", "CPI", "IPM", "CPA", "act%", "ROAS"]
    keys = [k for k in keys if any(m[k] is not None for m in out)]
    print("\n== Per rij, gerangschikt op CPA (laag = beter) ==")
    print("id".ljust(10) + "".join(k.rjust(11) for k in keys))
    for m in sorted(out, key=lambda m: (m["CPA"] is None, m["CPA"] or 0)):
        mark = " !" if m["id"] in bad else (" *" if m["_derived"] else "")
        print((m["id"] + mark).ljust(10) + "".join(fmt(m[k], 0 if k in ("spend", "impr", "clicks", "installs", "conv") else 2).rjust(11) for k in keys))
    if any(m["_derived"] for m in out):
        print("* conversies afgeleid als spend / CPA")
    if bad:
        print("! uitgesloten uit totalen")

    def tot(ms):
        s = sum(m["spend"] or 0 for m in ms)
        c = sum(m["conv"] or 0 for m in ms)
        return s, c, (s / c if c else None)

    s, c, cpa = tot(valid)
    print(f"\n== Totaal (geldige rijen: {len(valid)}) ==\nspend {fmt(s)} | conversies {fmt(c, 0)} | blended CPA {fmt(cpa)}")
    ranked = sorted([m for m in valid if m["conv"]], key=lambda m: -(m["conv"]))
    if ranked:
        top = ranked[0]
        rest = [m for m in valid if m is not top]
        s2, c2, cpa2 = tot(rest)
        print(f"Concentratie: {top['id']} levert {top['conv'] / c * 100:.0f}% van de conversies; blended CPA zonder {top['id']}: {fmt(cpa2)}")
        top3 = sum(m["conv"] for m in ranked[:3])
        print(f"Top 3 leveren {top3 / c * 100:.0f}% van de conversies")
    if a.target_cpa:
        over = [m for m in valid if m["CPA"] and m["CPA"] > a.target_cpa]
        so = sum(m["spend"] or 0 for m in over)
        print(f"Spend boven doel-CPA {a.target_cpa}: {fmt(so)} ({so / s * 100:.0f}% van spend), {len(over)} rijen")
        on = [m["id"] for m in valid if m["CPA"] and m["CPA"] <= a.target_cpa]
        print("Op of onder doel:", ", ".join(on) or "geen")

    print("\n== Correlatie met CPA en activatieratio (geldige rijen) ==")
    for up in ["CTR%", "CPI", "IPM", "CVR%", "CPM"]:
        for down in ["CPA", "act%"]:
            r, n = pearson([m[up] for m in valid], [m[down] for m in valid])
            if r is not None:
                print(f"{up:>5} vs {down:<5} r = {r:+.2f} (n={n})")

    if a.by:
        for col in [c.strip() for c in a.by.split(",")]:
            groups = defaultdict(list)
            for m in valid:
                groups[m["_row"].get(col, "")].append(m)
            print(f"\n== Per {col} ==")
            for k, ms in sorted(groups.items(), key=lambda kv: (tot(kv[1])[2] is None, tot(kv[1])[2] or 0)):
                gs, gc, gcpa = tot(ms)
                inst = sum(m["installs"] or 0 for m in ms)
                print(f"{k or '(leeg)':<16} n={len(ms):<3} spend {fmt(gs):>12} conv {fmt(gc, 0):>8} CPA {fmt(gcpa):>8} CPI {fmt(div(gs, inst)):>7}")

    if flags:
        print("\n== Datavlaggen ==")
        for f in flags:
            print("-", f)

    dst = src.with_name(src.stem + "-kpis.csv")
    with open(dst, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id"] + keys + ["excluded", "conv_derived"])
        for m in out:
            w.writerow([m["id"]] + [("" if m[k] is None else round(m[k], 4)) for k in keys] + [m["id"] in bad, m["_derived"]])
    print(f"\nGeschreven: {dst}")


if __name__ == "__main__":
    main()
