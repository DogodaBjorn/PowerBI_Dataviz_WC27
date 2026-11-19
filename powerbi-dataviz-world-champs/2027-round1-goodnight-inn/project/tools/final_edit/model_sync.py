"""Bring the measures of a model folder in line with the repository's generated model (the final copy keeps Desktop's own
serialization, so its _Measures.tmdl is edited line by line, never replaced). Used by the edit scripts from f8 on;
f7_package_a.py carries the same logic inline.

    from model_sync import sync_measures
    changed, added = sync_measures(Path(<.SemanticModel dir>))

Every measure whose expression or description differs from the generator's model is set to it; a missing one is added
after the measure it follows there. A measure the generator's model does not have stops the script.
"""
import re
from pathlib import Path

SOURCE_MODEL = Path(__file__).resolve().parents[2] / "pbip" / "PillowKey.SemanticModel"
MEASURE = re.compile(r"^\tmeasure (?:'((?:[^']|'')+)'|(\S+)) = (.*)$")


def _measures(text):
    """lines, name -> (index of the measure line, index of its /// line or None, index after its block), names in order"""
    lines = text.split("\n")
    out, order = {}, []
    for i, l in enumerate(lines):
        m = MEASURE.match(l.rstrip("\r"))
        if m:
            name = m.group(1) or m.group(2)
            j = i + 1
            while j < len(lines) and lines[j].startswith("\t\t"):
                j += 1
            out[name] = (i, i - 1 if i and lines[i - 1].startswith("\t///") else None, j)
            order.append(name)
    return lines, out, order


def _norm(s):
    return re.sub(r"\s+", " ", s.rstrip("\r")).strip()


def sync_measures(model):
    tgt, src = Path(model) / "definition" / "tables" / "_Measures.tmdl", SOURCE_MODEL / "definition" / "tables" / "_Measures.tmdl"
    changed, added = [], []
    if tgt.resolve() == src.resolve():
        return changed, added
    s_lines, s_idx, s_order = _measures(src.read_text(encoding="utf-8"))
    raw = tgt.read_text(encoding="utf-8")
    eol = "\r" if "\r\n" in raw else ""
    t_lines, t_idx, _ = _measures(raw)
    for name in s_order:
        if name in t_idx:
            (si, sd, _), (ti, td, _) = s_idx[name], t_idx[name]
            if _norm(s_lines[si]) != _norm(t_lines[ti]):
                t_lines[ti] = s_lines[si].rstrip("\r") + eol
                changed.append(name)
            if sd is not None and td is not None and _norm(s_lines[sd]) != _norm(t_lines[td]):
                t_lines[td] = s_lines[sd].rstrip("\r") + eol
    for k, name in enumerate(s_order):
        if name not in t_idx:
            si, sd, sj = s_idx[name]
            block = [l.rstrip("\r") + eol for l in s_lines[(sd if sd is not None else si):sj]] + [eol]
            at = _measures("\n".join(t_lines))[1][s_order[k - 1]][2]
            while at < len(t_lines) and t_lines[at].strip() == "":
                at += 1
            t_lines[at:at] = block
            added.append(name)
    extra = set(_measures("\n".join(t_lines))[1]) - set(s_idx)
    assert not extra, f"measures the generator's model does not have: {sorted(extra)}"
    if changed or added:
        tgt.write_text("\n".join(t_lines), encoding="utf-8", newline="")
    return changed, added
