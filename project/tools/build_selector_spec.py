"""Writes the Deneb (Vega) spec of the move selector, dn_build_selector (feedback round 4, 12-feedbackronde-4.md).

    python project/tools/build_selector_spec.py      # writes project/deliverables/deneb-specs/dn_build_selector.json

The spec is the source (deneb-studio convention: one file per visual, versioned); opzet_report.py pastes it into the
visual's jsonSpec. A Python builder, not a hand-written JSON: the cross-filter expression nests three levels of
quotes, and this keeps them straight.

What it draws: the ten Goodnight Inn moves as a list, one row each (check, move, the finding it answers, capex, NPV in
the case in view). A plain click toggles a row in or out of the plan: Deneb's ADVANCED cross-filtering
(pbiCrossFilterApply(event, filter, options), deneb.guide/docs/interactivity-selection-advanced) takes any Vega filter
expression as the new set of cross-filtered rows, so the handler rebuilds the whole set from the rows Power BI reports
as selected (`__selected__` = 'on') plus or minus the clicked one. No Ctrl, no modifier keys, no internal state that
could drift from the host's. Removing the last row calls pbiCrossFilterClear(). Credit: Deneb by Daniel
Marsh-Patrick (CREDITS.md). Kit 3.1 tokens only.

Round 5 (Björn, 10 Nov): a footer line keeps the running total under the hand that clicks: "Picked: 3 moves, $9.4M of
$60.0M", and "Over budget by $4.5M: $64.5M picked, the cap is $60.0M" in Burnt Tangerine, bold, once the picked capex
passes the budget (the big alarm is the your-plan title band on the canvas; this is the one at the point of action).
The dataset carries CapexNum and Budget for it.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "project" / "deliverables" / "deneb-specs" / "dn_build_selector.json"

INK, INK2, HAIR, TINT, ACCENT, ACCENT_MARK, BAD, SLATE, SURFACE = "#12233D", "#4B5466", "#E3DFD3", "#EAF2FB", "#1763A8", "#2589D8", "#A63F0E", "#8E897D", "#FFFFFF"
FONT = "Segoe UI, wf_segoe-ui_normal, Arial, sans-serif"
FONT_B = "Segoe UI Semibold, wf_segoe-ui_semibold, Arial, sans-serif"
PX = 16  # 12 pt
ON = "datum['__selected__'] == 'on'"
# $ millions like the canvas's fmc(): one decimal, a second only when it is not zero ($9.4M, $11.65M, $60.0M)
FMT = "replace(format(({v}) / 1e6, '$.2f'), regexp('0$'), '') + 'M'"
OVER = "nOn > 0 && capOn > budget"
FOOTER = ("nOn == 0 ? 'Nothing picked yet' : (" + OVER + " ? 'Over budget by ' + " + FMT.format(v="capOn - budget") + " + ': ' + " + FMT.format(v="capOn")
          + " + ' picked, the cap is ' + " + FMT.format(v="budget") + " : 'Picked: ' + nOn + (nOn == 1 ? ' move, ' : ' moves, ') + " + FMT.format(v="capOn")
          + " + ' of ' + " + FMT.format(v="budget") + ")")

# The filter expression Deneb evaluates against every dataset row (its own `datum`), built as a string at click time:
# the ids currently on, as one '|id|id|' string (onIds), plus or minus the clicked row's id.
_in_set = "indexof('\" + onIds + \"', '|' + datum['ProjectID'] + '|') >= 0"
_remove = "\"" + _in_set + " && datum['ProjectID'] != '\" + datum['ProjectID'] + \"'\""
_add = "\"" + _in_set + " || datum['ProjectID'] == '\" + datum['ProjectID'] + \"'\""
TOGGLE = f"{ON} && nOn == 1 ? pbiCrossFilterClear() : pbiCrossFilterApply(event, {ON} ? {_remove} : {_add}, {{limit: 50}})"


def txt(name, x, field=None, signal=None, align="left", fill=INK, font=FONT, header=False, weight=None, test=None):
    enc = {"x": {"value": x}, "align": {"value": align}, "baseline": {"value": "middle"}, "fontSize": {"value": PX}, "font": {"value": font}}
    if header:
        enc["y"] = {"signal": "headerH / 2"}
        enc["fill"] = {"value": INK2}
    else:
        enc["y"] = {"signal": "datum.y0 + rowH / 2"}
        enc["fill"] = {"signal": fill} if fill.startswith("datum") else {"value": fill}
    if field:
        enc["text"] = {"field": field}
    if signal:
        enc["text"] = {"signal": signal}
    if weight:
        enc["fontWeight"] = {"signal": weight}
    m = {"type": "text", "name": name, "interactive": False, "encode": {"update": enc}}
    if not header:
        m["from"] = {"data": "rows"}
    return m


spec = {
    "description": ("dn_build_selector (opzet P2, build state): the ten Goodnight Inn moves as a tappable list. Dataset fields, by display "
                    "name: ProjectID, Move, Sort, Answers, Capex, NPV, NPVnum, Case, CapexNum, Budget. Advanced cross-filtering: a plain click toggles the row; "
                    "the handler rebuilds the selected set from __selected__ and applies it with pbiCrossFilterApply. Tokens: Night, Dusk, "
                    "Seam, Ice, Coffee Blue, Burnt Tangerine (kit goodnight-inn-wakeup 3.1). Source: project/tools/build_selector_spec.py."),
    "autosize": {"type": "none", "contains": "padding"},
    "padding": 0,
    "background": SURFACE,
    "signals": [
        {"name": "width", "init": "containerSize()[0]", "on": [{"events": "window:resize", "update": "containerSize()[0]"}]},
        {"name": "height", "init": "containerSize()[1]", "on": [{"events": "window:resize", "update": "containerSize()[1]"}]},
        {"name": "headerH", "value": 32},
        {"name": "footerH", "value": 28},
        {"name": "nRows", "update": "max(1, length(data('dataset')))"},
        {"name": "rowH", "update": "(height - headerH - footerH) / nRows"},
        {"name": "nOn", "update": "length(data('onrows'))"},
        {"name": "capOn", "update": "length(data('ontotal')) > 0 ? data('ontotal')[0]['cap'] : 0"},
        {"name": "budget", "update": "length(data('dataset')) > 0 ? data('dataset')[0]['Budget'] : 0"},
        {"name": "onIds", "update": "'|' + join(pluck(data('onrows'), 'ProjectID'), '|') + '|'"},
        {"name": "caseLabel", "update": "length(data('dataset')) > 0 ? data('dataset')[0]['Case'] : ''"},
        # Deneb's advanced cross-filter signal: the host applies what pbiCrossFilterApply / pbiCrossFilterClear return
        {"name": "pbiCrossFilterSelection", "value": [],
         "on": [{"events": {"source": "scope", "type": "mouseup", "markname": "rowhit"}, "update": TOGGLE}]},
    ],
    "data": [
        {"name": "dataset"},
        {"name": "rows", "source": "dataset", "transform": [
            {"type": "collect", "sort": {"field": "Sort"}},
            {"type": "window", "ops": ["row_number"], "as": ["r"]},
            {"type": "formula", "as": "y0", "expr": "headerH + (datum.r - 1) * rowH"},
        ]},
        {"name": "onrows", "source": "dataset", "transform": [{"type": "filter", "expr": ON}]},
        {"name": "ontotal", "source": "onrows", "transform": [{"type": "aggregate", "ops": ["sum"], "fields": ["CapexNum"], "as": ["cap"]}]},
    ],
    "marks": [
        # header row
        txt("h_move", 40, signal="'Move'", header=True),
        txt("h_answers", 236, signal="'Answers'", header=True),
        txt("h_capex", 400, signal="'Capex'", align="right", header=True),
        txt("h_npv", 548, signal="'NPV, ' + caseLabel", align="right", header=True),
        {"type": "rule", "interactive": False, "encode": {"update": {"x": {"value": 0}, "x2": {"signal": "width"}, "y": {"signal": "headerH - 1"}, "stroke": {"value": HAIR}}}},
        # the rows: one hit rectangle each (the only interactive mark), Ice when the move is in the plan
        {"type": "rect", "name": "rowhit", "from": {"data": "rows"},
         "encode": {"update": {"x": {"value": 0}, "x2": {"signal": "width"}, "y": {"signal": "datum.y0 + 1"}, "height": {"signal": "rowH - 2"},
                               "fill": {"signal": f"{ON} ? '{TINT}' : '{SURFACE}'"}, "stroke": {"value": HAIR}, "strokeWidth": {"value": 1},
                               "cornerRadius": {"value": 6}, "cursor": {"value": "pointer"}},
                    "hover": {"stroke": {"value": ACCENT_MARK}, "strokeWidth": {"value": 1.5}}}},
        # the check: a Coffee Blue disc with a white tick when on, a Warm Grey ring when off (the row's fill repeats it)
        {"type": "symbol", "interactive": False, "from": {"data": "rows"},
         "encode": {"update": {"x": {"value": 20}, "y": {"signal": "datum.y0 + rowH / 2"}, "size": {"value": 230}, "shape": {"value": "circle"},
                               "fill": {"signal": f"{ON} ? '{ACCENT_MARK}' : '{SURFACE}'"}, "stroke": {"signal": f"{ON} ? '{ACCENT_MARK}' : '{SLATE}'"},
                               "strokeWidth": {"value": 1.5}}}},
        {"type": "text", "interactive": False, "from": {"data": "rows"},
         "encode": {"update": {"x": {"value": 20}, "y": {"signal": "datum.y0 + rowH / 2 + 1"}, "align": {"value": "center"}, "baseline": {"value": "middle"},
                               "text": {"signal": f"{ON} ? '✓' : ''"}, "fill": {"value": SURFACE}, "fontSize": {"value": 13}, "fontWeight": {"value": "bold"}}}},
        txt("t_move", 40, field="Move", fill=f"{ON} ? '{INK}' : '{INK2}'", weight=f"{ON} ? 600 : 400"),
        txt("t_answers", 236, field="Answers", fill=INK2),
        txt("t_capex", 400, field="Capex", align="right", fill=f"{ON} ? '{INK}' : '{INK2}'"),
        txt("t_npv", 548, field="NPV", align="right", fill=f"datum['NPVnum'] < 0 ? '{BAD}' : ({ON} ? '{INK}' : '{INK2}')"),
        # the footer (round 5): the running total, the alarm in Burnt Tangerine once the picked capex passes the budget
        {"type": "rule", "interactive": False, "encode": {"update": {"x": {"value": 0}, "x2": {"signal": "width"}, "y": {"signal": "height - footerH + 0.5"}, "stroke": {"value": HAIR}}}},
        {"type": "text", "name": "t_footer", "interactive": False,
         "encode": {"update": {"x": {"value": 40}, "y": {"signal": "height - footerH / 2 + 1"}, "align": {"value": "left"}, "baseline": {"value": "middle"},
                               "fontSize": {"value": PX}, "font": {"signal": f"{OVER} ? '{FONT_B}' : '{FONT}'"}, "fontWeight": {"signal": f"{OVER} ? 600 : 400"},
                               "fill": {"signal": f"{OVER} ? '{BAD}' : '{INK2}'"}, "text": {"signal": FOOTER}}}},
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
print("deneb spec written:", OUT)
