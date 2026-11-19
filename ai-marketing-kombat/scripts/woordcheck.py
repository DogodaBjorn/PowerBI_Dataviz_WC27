"""Zoek verboden woorden en frasen in een inlevering. Alleen standaardbibliotheek.

Gebruik:
  python -I scripts/woordcheck.py inlevering.md --regels regels.md
  python -I scripts/woordcheck.py inlevering.md --woorden "taxi,commission,cheap rides"

In regels.md: een kop "## Verboden woorden" met daaronder één woord of frase per regel
(opsommingstekens mogen). Het blok eindigt bij de volgende kop.
Let op: een treffer in een "Must not appear"-lijst kan bedoeld zijn; het script meldt hem toch.
"""
import argparse
import re
import sys
from pathlib import Path


def lees_regels(pad):
    woorden, actief = [], False
    for regel in Path(pad).read_text(encoding="utf-8").splitlines():
        if regel.startswith("#"):
            actief = "verboden" in regel.lower() or "forbidden" in regel.lower()
            continue
        if actief:
            w = regel.strip().lstrip("-*").strip().strip('"').strip()
            if w:
                woorden.append(w)
    return woorden


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("bestand")
    ap.add_argument("--regels")
    ap.add_argument("--woorden", default="")
    a = ap.parse_args()

    woorden = [w.strip() for w in a.woorden.split(",") if w.strip()]
    if a.regels:
        woorden += lees_regels(a.regels)
    if not woorden:
        sys.exit("Geen verboden woorden opgegeven")

    tekst = Path(a.bestand).read_text(encoding="utf-8").splitlines()
    treffers = 0
    for w in woorden:
        patroon = re.compile(r"\b" + re.escape(w) + r"\w*", re.IGNORECASE)
        for nr, regel in enumerate(tekst, 1):
            for m in patroon.finditer(regel):
                treffers += 1
                ctx = regel[max(0, m.start() - 40): m.end() + 40].strip()
                must_not = "must not" in regel.lower() or "not appear" in regel.lower()
                label = " (in must-not-lijst, waarschijnlijk bedoeld)" if must_not else ""
                print(f"r{nr}: '{m.group(0)}'{label} ... {ctx} ...")
    print(f"\n{treffers} treffer(s) voor {len(woorden)} woorden/frasen.")


if __name__ == "__main__":
    main()
