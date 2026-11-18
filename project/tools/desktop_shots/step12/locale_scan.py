"""Build step 12 of doc 23: read the visible texts of the published report (web.mjs, op "texts") for locale leaks.

usage: python locale_scan.py <texts.txt> [<texts.txt> ...]

R-G1: no decimal comma and no Dutch or German word on any visual, whatever the browser's locale. A number with a
comma followed by one or two digits and no third ("3,3", "79,4%", "$9,4M") is a decimal comma; "1,250" is a
thousands separator and passes. The service's own chrome (share buttons, page navigator) is the browser's language
by design and is listed apart: lines that start with "aria: " or that the report does not print.
"""
import re
import sys
from pathlib import Path

DECIMAL_COMMA = re.compile(r"(?<![\d,.])\d{1,3},\d{1,2}(?![\d,])")
WORDS = ("Totaal", "Gesamt", "Summe", "Overige", "Sonstige", "Leeg", "Leer", "(Blanco)", "(Leer)", "Geen", "Keine",
         "mln", "Mio", "mld", "Mrd", "jan.", "mrt", "mei", "okt", "Mär", "Dez")
WORD_RE = re.compile(r"(?<![A-Za-z])(" + "|".join(re.escape(w) for w in WORDS) + r")(?![A-Za-z])")

bad = 0
for name in sys.argv[1:]:
    lines = Path(name).read_text(encoding="utf-8").splitlines()
    canvas = [l for l in lines if not l.startswith("aria: ")]
    aria = [l[6:] for l in lines if l.startswith("aria: ")]
    hits = [(kind, l) for kind, group in (("text", canvas), ("aria", aria)) for l in group
            if DECIMAL_COMMA.search(l) or WORD_RE.search(l)]
    print(f"{name}: {len(canvas)} texts, {len(aria)} aria labels, {len(hits)} to read")
    for kind, l in hits:
        print(f"  {kind}: {l[:160]}")
    bad += len(hits)
print("locale_scan:", "nothing to read" if not bad else f"{bad} line(s) to read by eye (chrome of the service is the browser's language by design)")
