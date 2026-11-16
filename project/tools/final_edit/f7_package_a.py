"""Edit on the hand-finished report (16 Nov 2026 evening, doc 36): package A reads at a glance, one colour per decision,
and a tranche is called a step.

  python f7_package_a.py <.Report dir> <.SemanticModel dir> [--card outline|tint|none]

Bjorn, 16 Nov: "it's not clear within one single glance what is the selected package A. The right plan A is connected
to the top 3 actions on the left and the first part of the bar chart, but it's not clear." And: everything of tranche 3
one colour, the three parts of the plan distinguishable, and not the word tranche. This script edits the saved report in
place and can be run again (it sets, it does not add). What it sets:

  tbl_hero      the three rows of package A on a light blue ground in every column (measure Move Row Tint), so the
                recommendation is one block in the table. The Status column 16 px wider and the Move column 16 px
                narrower (the bar columns stay where they are): the status now reads "package A", "step 2 · 2028",
                "step 3 · 2028" (model).
  z_card_decision   the card "Our recommendation: package A" in the same blue: an outline in Coffee Blue (--card outline,
                the default) or the light blue ground (--card tint).
  c_rec_head    the words "package A" in Deep Coffee.
  c_plan_t1     the label over the plan bar's first segment in Deep Coffee: "Step 1 · package A".
  ch_plan_bar   the series are named Step 1, Step 2, Step 3.
  c_waits_head, ttg_list2   "two later steps", "Step", "the next step".
  the model     every measure that differs from the repository's generated model is set to it, and a missing one is
                added after its neighbour (Move Status Color and Ink by step, Move Status (text), Move Row Tint, the plan
                labels, the gate rule, two alt texts); the two titles of WaitOption that said Tranche.
"""
import json
import re
import sys
from pathlib import Path

REPORT, MODEL = Path(sys.argv[1]), Path(sys.argv[2])
CARD = sys.argv[sys.argv.index("--card") + 1] if "--card" in sys.argv else "outline"
SOURCE_MODEL = Path(__file__).resolve().parents[2] / "pbip" / "PillowKey.SemanticModel"  # the generator's
P2 = REPORT / "definition" / "pages" / "p2-investment-strategy" / "visuals"
GLOSSARY = REPORT / "definition" / "pages" / "tt-glossary" / "visuals"

COFFEE_BLUE, DEEP_COFFEE, NIGHT, TINT, WHITE = "#2589D8", "#1763A8", "#12233D", "#EAF2FB", "#FFFFFF"
WIDTHS = {"InvestmentProjects.Move Name": 264, "_Measures.Move Status (text)": 112}  # were 280 and 96: the sum stays
WILD = {"data": [{"dataViewWildcard": {"matchingOption": 1}}]}


def lit(s):
    return {"expr": {"Literal": {"Value": s}}}


def solid(hexv):
    return {"solid": {"color": lit(f"'{hexv}'")}}


def by_measure(name):
    return {"solid": {"color": {"expr": {"Measure": {"Expression": {"SourceRef": {"Entity": "_Measures"}}, "Property": name}}}}}


def edit(path, fn):
    raw = path.read_bytes()
    bom = raw.startswith(b"\xef\xbb\xbf")
    txt = raw.decode("utf-8-sig")
    nl = "\r\n" if "\r\n" in txt else "\n"
    v = json.loads(txt)
    fn(v)
    out = json.dumps(v, indent=2, ensure_ascii=False).replace("\n", nl) + (nl if txt.endswith("\n") else "")
    path.write_bytes((b"\xef\xbb\xbf" if bom else b"") + out.encode("utf-8"))


# ---- the report
def hero(v):
    o = v["visual"]["objects"]
    refs = [p["queryRef"] for p in v["visual"]["query"]["queryState"]["Values"]["projections"]]
    for r in refs:
        e = next((e for e in o["values"] if e.get("selector", {}).get("metadata") == r), None)
        if e is None:
            e = {"properties": {}, "selector": {**WILD, "metadata": r}}
            o["values"].append(e)
        e["properties"]["backColor"] = by_measure("Move Row Tint")
    for e in o["columnWidth"]:
        if e["selector"]["metadata"] in WIDTHS:
            e["properties"]["value"] = lit(f"{WIDTHS[e['selector']['metadata']]}D")
    assert sum(float(e["properties"]["value"]["expr"]["Literal"]["Value"][:-1]) for e in o["columnWidth"][:3]) == 480, "the bar columns moved"


def decision_card(v):
    c = v["visual"]["visualContainerObjects"]
    border, ground = c["border"][0]["properties"], c["background"][0]["properties"]
    border.update({"show": lit("true"), "color": solid(COFFEE_BLUE if CARD == "outline" else TINT if CARD == "tint" else WHITE),
                   "width": lit("2D" if CARD == "outline" else "1D")})
    ground["color"] = solid(TINT if CARD == "tint" else WHITE)


def rec_head(v):
    para = v["visual"]["objects"]["general"][0]["properties"]["paragraphs"][0]
    text = "".join(r["value"] for r in para["textRuns"])
    assert text == "Our recommendation: package A", text
    style = dict(para["textRuns"][0]["textStyle"])
    para["textRuns"] = [{"value": "Our recommendation: ", "textStyle": {**style, "color": NIGHT}}, {"value": "package A", "textStyle": {**style, "color": DEEP_COFFEE}}]


def plan_t1(v):
    v["visual"]["objects"]["value"][0]["properties"]["fontColor"] = solid(DEEP_COFFEE)


def plan_bar(v):
    for p in v["visual"]["query"]["queryState"]["Y"]["projections"]:
        m = re.fullmatch(r"_Measures\.Tranche (\d) Capex", p["queryRef"])
        if m:
            p["displayName"] = f"Step {m.group(1)}"


def reword(pairs):
    def fn(v):
        for para in v["visual"]["objects"]["general"][0]["properties"]["paragraphs"]:
            for run in para["textRuns"]:
                for a, b in pairs:
                    if run["value"] == a or (len(a) > 12 and a in run["value"]):
                        run["value"] = run["value"].replace(a, b)
    return fn


edit(P2 / "tbl_hero" / "visual.json", hero)
edit(P2 / "z_card_decision" / "visual.json", decision_card)
edit(P2 / "c_rec_head" / "visual.json", rec_head)
edit(P2 / "c_plan_t1" / "visual.json", plan_t1)
edit(P2 / "ch_plan_bar" / "visual.json", plan_bar)
edit(P2 / "c_waits_head" / "visual.json", reword([("One alternative and two tranches, each weighed against A.", "One alternative and two later steps, each weighed against A.")]))
edit(GLOSSARY / "ttg_list2" / "visual.json", reword([("Tranche", "Step"), ("decides on the next tranche, by the rule", "decides on the next step, by the rule")]))
left = [str(f.relative_to(REPORT)) for f in REPORT.rglob("*.json") if ".pbi" not in f.parts and re.search(r"[Tt]ranche(?! \d Capex)", f.read_text(encoding="utf-8-sig"))]
assert not left, f"the word is still in {left}"

# ---- the model: every measure as the generator's model has it
MEASURE = re.compile(r"^\tmeasure (?:'((?:[^']|'')+)'|(\S+)) = (.*)$")


def measures(text):
    """name -> (line index of the measure, index of its /// line or None, index after its block)"""
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


def norm(s):
    return re.sub(r"\s+", " ", s.rstrip("\r")).strip()


tgt_file, src_file = MODEL / "definition" / "tables" / "_Measures.tmdl", SOURCE_MODEL / "definition" / "tables" / "_Measures.tmdl"
changed, added = [], []
if tgt_file.resolve() != src_file.resolve():
    s_lines, s_idx, s_order = measures(src_file.read_text(encoding="utf-8"))
    raw = tgt_file.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    t_lines, t_idx, _ = measures(raw)
    eol = "\r" if nl == "\r\n" else ""
    for name in s_order:  # set what differs
        if name in t_idx:
            si, sd, _ = s_idx[name]
            ti, td, _ = t_idx[name]
            if norm(s_lines[si]) != norm(t_lines[ti]):
                t_lines[ti] = s_lines[si].rstrip("\r") + eol
                changed.append(name)
            if sd is not None and td is not None and norm(s_lines[sd]) != norm(t_lines[td]):
                t_lines[td] = s_lines[sd].rstrip("\r") + eol
    for k, name in enumerate(s_order):  # add what is missing, after the measure it follows in the generator's model
        if name not in t_idx:
            si, sd, sj = s_idx[name]
            block = [l.rstrip("\r") + eol for l in s_lines[(sd if sd is not None else si):sj]] + [eol]
            _, t_idx_now, _ = measures("\n".join(t_lines))
            at = t_idx_now[s_order[k - 1]][2]
            while at < len(t_lines) and t_lines[at].strip() == "":
                at += 1
            t_lines[at:at] = block
            added.append(name)
    tgt_file.write_text("\n".join(t_lines), encoding="utf-8", newline="")
    extra = set(measures("\n".join(t_lines))[1]) - set(s_idx)
    assert not extra, f"measures the generator's model does not have: {sorted(extra)}"
    w = MODEL / "definition" / "tables" / "WaitOption.tmdl"
    txt = w.read_text(encoding="utf-8")
    new = txt.replace('"Tranche 2 · Airport extensions, +80 rooms"', '"Step 2 · Airport extensions, +80 rooms"').replace('"Tranche 3 · Refresh, 10 oldest hotels"', '"Step 3 · Refresh, 10 oldest hotels"')
    assert '"Step 2 · Airport extensions, +80 rooms"' in new and '"Step 3 · Refresh, 10 oldest hotels"' in new
    if new != txt:
        w.write_text(new, encoding="utf-8", newline="")
        changed.append("WaitOption (table)")
print(f"f7_package_a: package A's rows tinted, the decision card {CARD}, steps for tranches; model: {len(changed)} set {changed}, {len(added)} added {added}")
