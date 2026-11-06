"""Writes the three direction sketches (D1 Wake-up call, D2 Fifty keys, D3 Two futures)
as separate PBIP reports on the shared PillowKey semantic model.

Run from the repo root after sketch_model.py:  python project/tools/sketch_reports.py
Output: project/pbip/D1-wake-up-call.pbip, D2-fifty-keys.pbip, D3-two-futures.pbip

Sketch-level: layout, bindings and copy follow project/PITCH-goodnight-inn-directions.md;
every number comes from the model. Stage-5 comps and the fidelity loop still follow.
"""
from pathlib import Path
from pbir_lib import *  # noqa: F401,F403
from pbir_lib import (visual, textbox, card, slicer, page, write_report, theme, vco, axis, legend, labels, series_colors, line_styles,
                      table_objects, data_bars, rule_backcolor, rule_fontcolor, proj_col, proj_mea, mref, filter_in, sort_by_measure,
                      sort_by_column, b, num, integer, enum, text, color, mea, col, filter_measure_gt)

ROOT = Path(__file__).resolve().parents[2]
PBIP = ROOT / "project" / "pbip"
FOOTER = "Data: Pillow & Key Group dataset, Power BI Dataviz World Champs 2027. Guest scores response-weighted. 2021 is a depressed base year. Projections are scenario logic from the organisers' FinanceAssumptions and FinanceParameters."
def GI():
    return [filter_in("Brands", "Brand", ["Goodnight Inn"], "flt_page_brand"), filter_in("InvestmentProjects", "Brand", ["Goodnight Inn"], "flt_page_projects")]
def YEARS_2125():
    return filter_in("Date", "Year", [2021, 2022, 2023, 2024, 2025], "flt_years_hist")
PLAN = ["Booking app", "Revenue management", "Kiosks at 20 desks", "Refresh 10 oldest", "Gatwick +40 rooms", "Toronto +40 rooms"]


def chart(name, vtype, x, y, w, h, z, tab, query, pal, F, title=None, objects=None, filters=None, sort=None, alt=None, title_size=10):
    objs = objects or {}
    return visual(name, vtype, x, y, w, h, z, tab, query=query, objects=objs, filters=filters, sort=sort,
                  vcos=vco(title=title, title_font=F["body"], title_size=title_size, title_color=pal["ink2"], alt=alt, padding=0))


def kicker(name, x, y, w, h, z, tab, t, pal, F):
    return textbox(name, x, y, w, h, z, tab, [[(t, F["mono"], 10, pal["ink2"], False)]])


def headline(name, x, y, w, h, z, tab, t, pal, F, size=22):
    return textbox(name, x, y, w, h, z, tab, [[(t, F["hero"], size, pal["ink"], False)]])


def footer(pal, F, z=900):
    return textbox("z_footer", 24, 696, 1232, 24, z, 9000, [[(FOOTER, F["body"], 8, pal["ink2"], False)]])


def note(name, x, y, w, h, z, tab, paras, pal, F, size=10):
    """paras: list of (kicker, body)."""
    runs = []
    for k, body in paras:
        if k:
            runs.append([(k, F["mono"], 9, pal["ink2"], False)])
        runs.append([(body, F["body"], size, pal["ink"], False)])
    return textbox(name, x, y, w, h, z, tab, runs)


def cumulative_chart(name, x, y, w, h, z, tab, pal, F, title):
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]},
         "Y": {"projections": [proj_mea("Cumulative Net Impact"), proj_mea("Cumulative Net Impact (Low)"), proj_mea("Cumulative Net Impact (High)")]}}
    objs = {"categoryAxis": axis(F["body"], 9, pal["ink2"]), "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=True, grid_color=pal["hair"], units=1),
            "legend": legend(True, F["body"], 9, pal["ink2"], "Top"),
            "dataPoint": series_colors({mref("Cumulative Net Impact"): pal["accent"], mref("Cumulative Net Impact (Low)"): pal["neutral"], mref("Cumulative Net Impact (High)"): pal["neutral"]}),
            "lineStyles": line_styles({mref("Cumulative Net Impact"): 3, mref("Cumulative Net Impact (Low)"): 1, mref("Cumulative Net Impact (High)"): 1}, dashed=(mref("Cumulative Net Impact (Low)"), mref("Cumulative Net Impact (High)")))}
    return chart(name, "lineChart", x, y, w, h, z, tab, q, pal, F, title=title, objects=objs,
                 filters=[filter_in("Date", "Year", [2027, 2028, 2029, 2030, 2031, 2032], "flt_horizon")], alt="Cumulative net impact of the selected plan 2027 to 2032, Expected line with Low and High dashed")


def plan_slicer(name, x, y, w, h, z, tab, pal, F, mode="Basic"):
    return slicer(name, x, y, w, h, z, tab, "InvestmentProjects", "Short Name", "PLAN BUILDER: tick the projects", F["body"], pal["ink"], pal["ink2"], pal["surface"], pal["accent"],
                  mode=mode, selected=PLAN, alt="Plan builder: select the investment projects to fund")


def scenario_slicer(name, x, y, w, h, z, tab, pal, F):
    return slicer(name, x, y, w, h, z, tab, "Scenario", "Scenario", "SCENARIO", F["body"], pal["ink"], pal["ink2"], pal["surface"], pal["accent"],
                  single=True, horizontal=True, selected=["Expected"], alt="Scenario toggle: Low, Expected or High")


def folio_table(name, x, y, w, h, z, tab, pal, F, title="THE FOLIO: one room night in 2025, by channel"):
    q = {"Values": {"projections": [proj_col("FolioLine", "Line", display="Folio"), proj_mea("Folio OTA Guest", "OTA guest"), proj_mea("Folio Direct Guest", "Direct guest")]}}
    objs = table_objects(F["mono"], 10, pal["ink"], pal["surface"], pal["surface"], pal["surface"], pal["ink2"], pal["hair"], row_padding=4)
    return chart(name, "tableEx", x, y, w, h, z, tab, q, pal, F, title=title, objects=objs, sort=sort_by_column("FolioLine", "Sort"),
                 alt="The folio: average room rate, commission paid and what the hotel keeps for an OTA guest and a direct guest")


def kpi_band(pal, F, y=96):
    out = []
    specs = [("kpi_occupancy", "Occupancy % 2025", "Occupancy 2025", "Occupancy vs 2024 (text)"),
             ("kpi_revpar", "RevPAR 2025", "RevPAR 2025", "RevPAR vs 2024 (text)"),
             ("kpi_gop_margin", "GOP Margin % 2025", "GOP margin 2025, before commissions", "GOP Margin vs 2023 (text)"),
             ("kpi_nps", "NPS (weighted) 2025", "NPS 2025, response-weighted", "NPS vs 2021 (text)")]
    for i, (n, mval, lab, mdelta) in enumerate(specs):
        x = 24 + i * 248
        out.append(card(n, x, y, 232, 56, 100 + i, 100 + i, [mval], F["hero"], 22, pal["ink"], F["body"], 9, pal["ink2"], labels=[lab], alt=lab))
        out.append(card("dlt_" + n[4:], x, y + 56, 232, 40, 110 + i, 110 + i, [mdelta], F["body"], 10, pal["ink2"], alt=lab + " change"))
    out.append(card("c_benchmark", 1016, y, 240, 96, 120, 120, ["Benchmark after Distribution (text)"], F["body"], 9, pal["ink2"], labels=["Sister brands, margin after commissions 2025"], alt="Sister-brand benchmark of margin after distribution"))
    return out


# ====================================================================== D1
def build_d1():
    pal = {"canvas": "#FBF8F1", "surface": "#FFFFFF", "ink": "#1C2B3A", "ink2": "#5A6B7B", "hair": "#E6E0D4", "accent": "#D9960A", "good": "#2E7D4F", "bad": "#B23A2E", "neutral": "#A7B0B8"}
    F = {"hero": "Georgia", "body": "Segoe UI", "mono": "Consolas"}
    th = theme("D1-wake-up-call.json", pal, F)

    # ---- page 1
    v = [kicker("z_masthead", 24, 16, 1232, 24, 1, 1, "GOODNIGHT INN  ·  BRAND REVIEW 2021 TO 2025  ·  FOR THE BOARD OF PILLOW & KEY GROUP", pal, F),
         headline("z_headline", 24, 40, 1232, 48, 2, 2, "Full, flat, and paying the middleman: the group's best margin is slipping.", pal, F)]
    v += kpi_band(pal, F)
    # column 1: the plateau
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea("RevPOR Index (2023 = 100)"), proj_mea("CPOR Index (2023 = 100)")]}}
    v.append(chart("ch_plateau_index", "lineChart", 24, 200, 392, 200, 200, 200, q, pal, F, title="THE PLATEAU: revenue vs cost per occupied room, index 2023 = 100",
                   objects={"categoryAxis": axis(F["body"], 9, pal["ink2"]), "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=True, grid_color=pal["hair"], start=90),
                            "legend": legend(True, F["body"], 9, pal["ink2"], "Top"),
                            "dataPoint": series_colors({mref("RevPOR Index (2023 = 100)"): pal["neutral"], mref("CPOR Index (2023 = 100)"): pal["accent"]}),
                            "lineStyles": line_styles({mref("CPOR Index (2023 = 100)"): 3, mref("RevPOR Index (2023 = 100)"): 2}, markers=True)},
                   filters=[YEARS_2125()], alt="Revenue per occupied room and cost per occupied room indexed to 2023; cost rises faster"))
    q = {"Category": {"projections": [proj_col("BridgeStep", "Step", active=True)]}, "Y": {"projections": [proj_mea("Bridge Value")]}}
    v.append(chart("hero_gop_bridge", "waterfallChart", 24, 408, 392, 152, 201, 201, q, pal, F, title="GOP BRIDGE 2024 TO 2025, $",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"], gridlines=None), "valueAxis": axis(F["mono"], 8, pal["ink2"], gridlines=False, units=1),
                            "sentimentColors": [{"properties": {"increaseFill": color(pal["good"]), "decreaseFill": color(pal["bad"]), "totalFill": color(pal["ink"]), "otherFill": color(pal["neutral"])}}],
                            "labels": labels(True, F["mono"], 8, pal["ink"]), "legend": legend(False)},
                   filters=[filter_in("BridgeStep", "Bridge", ["GOP 2024 to 2025"], "flt_bridge")], sort=sort_by_column("BridgeStep", "Sort"),
                   alt="Waterfall from 2024 gross operating profit to 2025: volume, rate, staff, energy, maintenance, food and beverage cost, other cost"))
    # column 2: the middleman
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Series": {"projections": [proj_col("BookingChannels", "Channel")]}, "Y": {"projections": [proj_mea("Channel Room Revenue")]}}
    v.append(chart("ch_channel_mix", "hundredPercentStackedAreaChart", 432, 200, 392, 184, 210, 210, q, pal, F, title="THE MIDDLEMAN: share of room revenue by channel",
                   objects={"categoryAxis": axis(F["body"], 9, pal["ink2"]), "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=False),
                            "legend": legend(True, F["body"], 8, pal["ink2"], "Bottom"),
                            "dataPoint": [{"properties": {"fill": color(pal["accent"])}, "selector": {"data": [{"scopeId": {"Comparison": {"ComparisonKind": 0, "Left": col("BookingChannels", "Channel"), "Right": {"Literal": {"Value": "'Online Travel Agencies'"}}}}}]}}]},
                   filters=[YEARS_2125()], alt="Stacked area of channel share of room revenue 2021 to 2025; online travel agencies grow"))
    v.append(folio_table("tbl_folio", 432, 392, 392, 128, 211, 211, pal, F))
    v.append(card("c_counterfactual", 432, 528, 392, 40, 212, 212, ["Counterfactual (text)"], F["body"], 10, pal["ink"], alt="Distribution cost above the 2021 channel mix"))
    # column 3: the fading welcome
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "X": {"projections": [proj_mea("Refresh Age")]}, "Y": {"projections": [proj_mea("Room Comfort (weighted) 2025")]}, "Size": {"projections": [proj_mea("Hotel Rooms")]}}
    v.append(chart("ch_comfort_vs_age", "scatterChart", 840, 200, 416, 200, 220, 220, q, pal, F, title="THE FADING WELCOME: room comfort 2025 vs years since refresh, one dot per hotel",
                   objects={"categoryAxis": axis(F["mono"], 9, pal["ink2"], title=True, extra={"titleText": text("years since refresh"), "titleFontFamily": text(F["body"]), "titleFontSize": num(8), "titleColor": color(pal["ink2"])}),
                            "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=True, grid_color=pal["hair"]),
                            "dataPoint": series_colors({}, default=pal["accent"]), "bubbles": [{"properties": {"bubbleSize": integer(-20)}}], "legend": legend(False), "categoryLabels": [{"properties": {"show": b(False)}}]},
                   alt="Scatter of 50 hotels: room comfort score falls as years since refresh rise"))
    q = {"Category": {"projections": [proj_col("GuestComplaints", "Category", active=True)]}, "Y": {"projections": [proj_mea("Complaints per 1k Room Nights 2025")]}}
    v.append(chart("ch_complaints", "clusteredBarChart", 840, 408, 416, 152, 221, 221, q, pal, F, title="COMPLAINTS PER 1,000 ROOM NIGHTS, 2025",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], show=False),
                            "dataPoint": [{"properties": {"fill": {"solid": {"color": {"expr": {"Conditional": {"Cases": [
                                {"Condition": {"Comparison": {"ComparisonKind": 0, "Left": {"Aggregation": {"Expression": col("GuestComplaints", "Category"), "Function": 3}}, "Right": {"Literal": {"Value": "'Room condition'"}}}}, "Value": {"Literal": {"Value": f"'{pal['accent']}'"}}},
                                {"Condition": {"Comparison": {"ComparisonKind": 0, "Left": {"Aggregation": {"Expression": col("GuestComplaints", "Category"), "Function": 3}}, "Right": {"Literal": {"Value": "'Check-in & waiting times'"}}}}, "Value": {"Literal": {"Value": f"'{pal['accent']}'"}}}],
                                "DefaultValue": {"Literal": {"Value": f"'{pal['neutral']}'"}}}}}}}}}],
                            "labels": labels(True, F["mono"], 8, pal["ink"], precision=1), "legend": legend(False)},
                   sort=sort_by_measure("Complaints per 1k Room Nights 2025"), alt="Bar chart of complaint categories per thousand room nights; room condition and check-in in accent"))
    # bottom strip
    q = {"Category": {"projections": [proj_col("Hotels", "LocationType", active=True)]}, "Y": {"projections": [proj_mea("Occupancy % 2025")]}}
    v.append(chart("ch_occ_by_location", "clusteredBarChart", 24, 568, 392, 120, 230, 230, q, pal, F, title="WHERE WE'RE FULL: occupancy 2025 by location type",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], show=False), "dataPoint": series_colors({}, default=pal["neutral"]),
                            "labels": labels(True, F["mono"], 8, pal["ink"], precision=1), "legend": legend(False)},
                   sort=sort_by_measure("Occupancy % 2025"), alt="Occupancy by location type: airport, highway, city"))
    q = {"Category": {"projections": [proj_col("Date", "Month", active=True)]}, "Series": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Occupancy %")]}}
    v.append(chart("ch_full_sparklines", "lineChart", 432, 568, 824, 120, 231, 231, q, pal, F, title="MONTHLY OCCUPANCY 2025: Gatwick and Toronto are full, Kingston is not",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], show=False), "legend": legend(True, F["body"], 8, pal["ink2"], "Right"),
                            "dataPoint": series_colors({}, default=pal["neutral"]), "lineStyles": line_styles({}, default_width=2)},
                   filters=[filter_in("Date", "Year", [2025], "flt_2025"), filter_in("Hotels", "Hotel Short Name", ["London Gatwick Airport", "Toronto Pearson Airport", "Kingston"], "flt_three_hotels")],
                   alt="Monthly occupancy lines for Gatwick, Toronto and Kingston in 2025"))
    v.append(footer(pal, F))
    p1 = page("p1-wake-up-call", "Wake-up call", v, pal["canvas"], GI())

    # ---- page 2
    v = [kicker("z_masthead2", 24, 16, 1232, 24, 1, 1, "THE MORNING PLAN  ·  2027 TO 2032  ·  GOODNIGHT INN INVESTMENT STRATEGY", pal, F),
         card("z_headline2", 24, 40, 1232, 48, 2, 2, ["Headline Plan (text)"], F["hero"], 20, pal["ink"], alt="Dynamic headline: capex, projects and run-rate of the selected plan")]
    v.append(plan_slicer("sl_plan_builder", 24, 96, 368, 304, 10, 10, pal, F))
    v.append(card("kpi_budget", 24, 408, 368, 64, 11, 11, ["Capex Selected", "Budget Used %", "Projects Selected", "Growth Initiatives Selected"], F["hero"], 18, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["capex selected", "of budget", "projects", "growth"], alt="Capex selected, share of budget, project count and growth initiatives"))
    q = {"Category": {"projections": [proj_col("Brands", "Brand", active=True)]}, "Y": {"projections": [proj_mea("Capex Selected"), proj_mea("Budget Remaining")]}}
    v.append(chart("ch_budget_bar", "barChart", 24, 480, 368, 72, 12, 12, q, pal, F, title="BUDGET: $ used of $60 M",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"], show=False), "valueAxis": axis(F["mono"], 8, pal["ink2"], show=False), "legend": legend(False),
                            "dataPoint": series_colors({mref("Capex Selected"): pal["accent"], mref("Budget Remaining"): pal["hair"]}), "labels": labels(True, F["mono"], 8, pal["ink"])},
                   alt="Stacked bar of capex selected against the remaining budget"))
    v.append(card("kpi_plan_valid", 24, 560, 368, 32, 13, 13, ["Plan Valid (text)"], F["body"], 9, pal["ink"], alt="Constraint lamp: at least three projects, one growth initiative, within budget, dependencies met"))
    v.append(scenario_slicer("sl_scenario", 408, 96, 464, 48, 20, 20, pal, F))
    v.append(card("kpi_impact", 408, 152, 464, 80, 21, 21, ["2032 Run-rate", "Run-rate % of 2025 GOP", "NPV @ 8%", "Payback (text)"], F["hero"], 18, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["run-rate by 2032", "of 2025 GOP", "NPV at 8 pct", "payback"], alt="Impact of the selected plan: run-rate, share of GOP, NPV and payback"))
    v.append(cumulative_chart("hero_cumulative", 408, 240, 464, 232, 22, 22, pal, F, "CUMULATIVE NET IMPACT 2027 TO 2032, $ (Expected; Low and High dashed)"))
    v.append(card("kpi_ops", 408, 480, 464, 80, 23, 23, ["Rooms Added", "Rooms Refreshed", "Kiosk Desks", "Disruption Months"], F["hero"], 18, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["rooms added", "rooms refreshed", "kiosk desks", "months of works"], alt="Operational impact of the selection"))
    q = {"Values": {"projections": [proj_col("InvestmentProjects", "Short Name", display="Initiative"), proj_mea("Hotels Touched", "Hotels"), proj_mea("Start (text)", "Departs"), proj_mea("Live (text)", "Arrives"),
                                     proj_mea("Capex Selected", "Capex"), proj_mea("2032 Run-rate", "Run-rate"), proj_mea("Payback (text)", "Payback")]}}
    v.append(chart("tbl_departures", "tableEx", 888, 96, 368, 376, 30, 30, q, pal, F, title="DEPARTURES: the selected initiatives",
                   objects=table_objects(F["mono"], 9, pal["ink"], pal["surface"], pal["surface"], pal["surface"], pal["ink2"], pal["hair"], row_padding=3),
                   sort=sort_by_column("InvestmentProjects", "Short Name"), alt="Departures board: initiative, hotels, start, go-live, capex, run-rate and payback"))
    v.append(note("c_not_funded", 408, 568, 464, 120, 40, 40, [("NOT FUNDED, AND WHY", "Boston Logan: 41 percent of the budget for one hotel that opens in 2029. Kingston extension: 61 percent occupancy today, the Low case loses money. Energy programme: pays back after the horizon. Breakfast upgrade: held as the alternative to the contingency.")], pal, F))
    v.append(note("c_risks", 888, 480, 368, 208, 41, 41, [("RISKS AND TRADE-OFFS", "Rooms versus kilowatts: the refresh beats the energy programme on guest scores, not on in-horizon cash. The refresh takes 15 percent of 1,180 rooms out for 14 months. App adoption is the swing between Low and High. Horizon honesty: capital projects pay back after 2032; read the run-rate.")], pal, F))
    v.append(footer(pal, F))
    p2 = page("p2-morning-plan", "The morning plan", v, pal["canvas"], GI())
    write_report(PBIP, "D1-wake-up-call", "D1 Wake-up call", [p1, p2], th, "D1-wake-up-call.json")


# ====================================================================== D2
def build_d2():
    pal = {"canvas": "#0F1B2D", "surface": "#16243A", "ink": "#F4F1EA", "ink2": "#B7C0CC", "hair": "#2A3A52", "accent": "#F2B134", "good": "#5BC58A", "bad": "#F07D6B", "neutral": "#6F7F93"}
    F = {"hero": "Segoe UI Semibold", "body": "Segoe UI", "mono": "Consolas"}
    th = theme("D2-fifty-keys.json", pal, F)
    Y25 = filter_in("Date", "Year", [2025], "flt_page_2025")

    v = [kicker("z_masthead", 24, 16, 1232, 24, 1, 1, "GOODNIGHT INN  ·  50 HOTELS  ·  6,485 ROOMS  ·  THE WALL TONIGHT (2025)", pal, F),
         card("z_headline", 24, 40, 1232, 48, 2, 2, ["Headline Wall (text)"], F["hero"], 20, pal["ink"], alt="Dynamic headline: how many hotels are full and how many are tired")]
    occ, rev, nps, age = mref("Occupancy % 2025"), mref("RevPAR 2025"), mref("NPS (weighted) 2025"), "Hotels.Years Since Refresh"
    q = {"Values": {"projections": [proj_col("Hotels", "Hotel Short Name", display="Hotel"), proj_col("Hotels", "LocationType", display="Type"), proj_mea("Occupancy % 2025", "Occupancy"), proj_mea("RevPAR 2025", "RevPAR"),
                                     proj_mea("NPS (weighted) 2025", "NPS"), proj_col("Hotels", "Years Since Refresh", display="Yrs since refresh"), proj_mea("Hotel Status 2025", "Tonight")]}}
    objs = table_objects(F["body"], 8, pal["ink"], pal["canvas"], pal["canvas"], pal["canvas"], pal["ink2"], pal["hair"], row_padding=1,
                         extra_values=[rule_backcolor(nps, "NPS (weighted) 2025", [(3, "0D", pal["bad"])], pal["canvas"]),
                                       rule_fontcolor(nps, "NPS (weighted) 2025", [(3, "0D", pal["canvas"])], pal["ink"]),
                                       rule_fontcolor(occ, "Occupancy % 2025", [(2, "0.85D", pal["accent"])], pal["ink"])],
                         column_formatting=[data_bars(occ, pal["hair"], pal["hair"])])
    v.append(chart("hero_wall", "tableEx", 24, 96, 808, 400, 10, 10, q, pal, F, title="THE WALL: one row per hotel, sorted by occupancy; amber = 85 percent or fuller, red chip = negative NPS",
                   objects=objs, sort=sort_by_measure("Occupancy % 2025"), alt="Table of all fifty hotels with occupancy bars, RevPAR, NPS chips, years since refresh and status"))
    q = {"Category": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "X": {"projections": [proj_mea("Occupancy % 2025")]}, "Y": {"projections": [proj_mea("NPS (weighted) 2025")]}, "Size": {"projections": [proj_mea("Hotel Rooms")]}}
    v.append(chart("ch_full_vs_tired", "scatterChart", 848, 96, 408, 192, 20, 20, q, pal, F, title="FULL vs TIRED: occupancy by NPS, bubble = rooms",
                   objects={"categoryAxis": axis(F["mono"], 8, pal["ink2"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], gridlines=True, grid_color=pal["hair"]),
                            "dataPoint": series_colors({}, default=pal["accent"]), "bubbles": [{"properties": {"bubbleSize": integer(-30)}}], "legend": legend(False), "categoryLabels": [{"properties": {"show": b(False)}}],
                            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0), "lineColor": color(pal["ink2"]), "style": enum("dashed")}, "selector": {"id": "zero"}}]},
                   alt="Scatter of hotels by occupancy and NPS with a zero line"))
    v.append(card("kpi_middleman", 848, 296, 408, 56, 21, 21, ["OTA Share % 2025", "Distribution Cost 2025", "Distribution Cost above 2021 Mix 2025"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["of room revenue via OTAs", "paid to channels 2025", "above the 2021 mix"], alt="The middleman in three numbers"))
    q = {"Category": {"projections": [proj_col("Date", "Year", active=True)]}, "Y": {"projections": [proj_mea("OTA Share %"), proj_mea("Direct Share %")]}}
    v.append(chart("ch_ota_trend", "lineChart", 848, 360, 408, 136, 22, 22, q, pal, F, title="OTA share rises, direct share falls, 2021 to 2025",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], gridlines=False), "legend": legend(True, F["body"], 8, pal["ink2"], "Top"),
                            "dataPoint": series_colors({mref("OTA Share %"): pal["accent"], mref("Direct Share %"): pal["neutral"]}), "lineStyles": line_styles({}, markers=True)},
                   filters=[YEARS_2125()], alt="Lines of OTA share and direct share of room revenue by year"))
    q = {"Category": {"projections": [proj_col("HotelOutlook", "Year", active=True)]}, "Series": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Y": {"projections": [proj_mea("Baseline Demand Occupancy %")]}}
    v.append(chart("ch_capacity_wall", "lineChart", 24, 504, 1232, 184, 30, 30, q, pal, F, title="CAPACITY WALL (scenario logic from FinanceAssumptions): projected demand occupancy 2025 to 2032 for the hotels that cross the 97 percent ceiling (dashed)",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], gridlines=False), "legend": legend(True, F["body"], 8, pal["ink2"], "Right"),
                            "dataPoint": series_colors({}, default=pal["accent"]), "lineStyles": line_styles({}, default_width=2),
                            "y1AxisReferenceLine": [{"properties": {"show": b(True), "value": num(0.97), "lineColor": color(pal["ink"]), "style": enum("dashed"), "displayName": text("97 percent ceiling")}, "selector": {"id": "cap"}}]},
                   filters=[filter_measure_gt("First Capped Year", 0, "flt_capped")], alt="Lines per capped hotel: projected demand occupancy against the 97 percent capacity ceiling"))
    v.append(footer(pal, F))
    p1 = page("p1-wall-tonight", "The wall tonight", v, pal["canvas"], GI())

    v = [kicker("z_masthead2", 24, 16, 1232, 24, 1, 1, "THE PLAN ON THE WALL  ·  2027 TO 2032  ·  EVERY LIGHT IS A FUNDED DECISION", pal, F),
         card("z_headline2", 24, 40, 1232, 48, 2, 2, ["Headline Plan (text)"], F["hero"], 20, pal["ink"], alt="Dynamic headline of the selected plan")]
    v.append(slicer("sl_year", 24, 96, 472, 48, 10, 10, "PlanYear", "Year", "YEAR: step the wall through the plan", F["body"], pal["ink"], pal["ink2"], pal["surface"], pal["accent"], single=True, horizontal=True, selected=[2032], alt="Year stepper 2027 to 2032"))
    v.append(card("kpi_budget_compact", 512, 96, 744, 48, 11, 11, ["Capex Selected", "Budget Used %", "2032 Run-rate", "NPV @ 8%"], F["hero"], 14, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["capex selected", "of $60 M", "run-rate by 2032", "NPV at 8 percent"], alt="Budget and impact of the selection"))
    q = {"Rows": {"projections": [proj_col("Hotels", "Hotel Short Name")]}, "Columns": {"projections": [proj_col("InvestmentProjects", "Short Name")]}, "Values": {"projections": [proj_mea("Wall Light")]}}
    objs = {"columnHeaders": [{"properties": {"fontFamily": text(F["body"]), "fontSize": num(8), "fontColor": color(pal["ink2"]), "backColor": color(pal["canvas"]), "outlineStyle": enum("None"), "autoSizeColumnWidth": b(True), "columnAdjustment": enum("growToFit"), "wordWrap": b(True)}}],
            "rowHeaders": [{"properties": {"fontFamily": text(F["body"]), "fontSize": num(8), "fontColor": color(pal["ink"]), "backColor": color(pal["canvas"]), "outlineStyle": enum("None")}}],
            "values": [{"properties": {"fontFamily": text(F["body"]), "fontSize": num(8), "fontColorPrimary": color(pal["ink"]), "fontColorSecondary": color(pal["ink"]), "backColorPrimary": color(pal["canvas"]), "backColorSecondary": color(pal["canvas"]), "outlineStyle": enum("None")}},
                       {"properties": {"backColor": {"solid": {"color": {"expr": {"Conditional": {"Cases": [
                           {"Condition": {"Comparison": {"ComparisonKind": 0, "Left": mea("Wall Light"), "Right": {"Literal": {"Value": "'lit'"}}}}, "Value": {"Literal": {"Value": f"'{pal['accent']}'"}}},
                           {"Condition": {"Comparison": {"ComparisonKind": 0, "Left": mea("Wall Light"), "Right": {"Literal": {"Value": "'planned'"}}}}, "Value": {"Literal": {"Value": f"'{pal['hair']}'"}}}],
                           "DefaultValue": {"Literal": {"Value": f"'{pal['canvas']}'"}}}}}}}}, "selector": {"data": [{"dataViewWildcard": {"matchingOption": 1}}], "metadata": mref("Wall Light")}},
                       {"properties": {"fontColor": {"solid": {"color": {"expr": {"Conditional": {"Cases": [
                           {"Condition": {"Comparison": {"ComparisonKind": 0, "Left": mea("Wall Light"), "Right": {"Literal": {"Value": "'lit'"}}}}, "Value": {"Literal": {"Value": f"'{pal['accent']}'"}}}],
                           "DefaultValue": {"Literal": {"Value": f"'{pal['hair']}'"}}}}}}}}, "selector": {"data": [{"dataViewWildcard": {"matchingOption": 1}}], "metadata": mref("Wall Light")}}],
            "grid": [{"properties": {"gridVertical": b(False), "gridHorizontal": b(True), "gridHorizontalColor": color(pal["hair"]), "gridHorizontalWeight": num(1), "rowPadding": num(1), "outlineStyle": enum("None")}}],
            "rowTotal": [{"properties": {"fontColor": color(pal["ink2"]), "backColor": color(pal["canvas"])}}],
            "columnTotal": [{"properties": {"fontColor": color(pal["ink2"]), "backColor": color(pal["canvas"])}}],
            "subTotals": [{"properties": {"rowSubtotals": b(False), "columnSubtotals": b(False)}}]}
    v.append(visual("hero_wall_relit", "pivotTable", 24, 152, 808, 400, 20, 20, query=q, objects=objs,
                    vcos=vco(title="THE WALL, RE-LIT: amber = live in the chosen year, grey = planned, blank = not touched", title_font=F["body"], title_size=10, title_color=pal["ink2"], alt="Matrix of hotels by selected projects; cells light amber once the project is live in the chosen year", padding=0,
                             extra={"stylePreset": [{"properties": {"name": enum("None")}}]}),
                    sort=sort_by_column("Hotels", "Hotel Short Name")))
    v.append(plan_slicer("sl_plan_builder", 848, 152, 408, 304, 30, 30, pal, F))
    v.append(card("kpi_plan", 848, 464, 408, 88, 31, 31, ["Projects Selected", "Growth Initiatives Selected", "Rooms Added", "Rooms Refreshed"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["projects", "growth", "rooms added", "rooms refreshed"], alt="Plan counts"))
    v.append(card("kpi_plan_valid", 24, 560, 472, 40, 40, 40, ["Plan Valid (text)"], F["body"], 9, pal["ink"], alt="Constraint lamp"))
    v.append(card("kpi_impact_by_hotel", 24, 608, 472, 80, 41, 41, ["Kiosk Desks", "Disruption Months", "Direct Share % 2025", "Payback (text)"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["desks with kiosks", "months with rooms out", "direct share today", "payback year"], alt="Impact by hotel"))
    v.append(cumulative_chart("ch_cumulative", 512, 560, 464, 128, 42, 42, pal, F, "CUMULATIVE NET IMPACT 2027 TO 2032, $"))
    v.append(note("c_why_not", 992, 560, 264, 128, 43, 43, [("WHY NOT", "Boston: 41 percent of the budget, opens 2029. Kingston: 61 percent occupancy, Low case loses. Energy: pays back after the horizon.")], pal, F, size=9))
    v.append(footer(pal, F))
    p2 = page("p2-wall-2032", "The wall in 2032", v, pal["canvas"], GI())
    write_report(PBIP, "D2-fifty-keys", "D2 Fifty keys", [p1, p2], th, "D2-fifty-keys.json")


# ====================================================================== D3
def build_d3():
    pal = {"canvas": "#F6F1E7", "surface": "#FFFDF8", "ink": "#2B2A28", "ink2": "#6B6660", "hair": "#DDD5C6", "accent": "#C9821E", "good": "#2E7D4F", "bad": "#B23A2E", "neutral": "#A39E95"}
    F = {"hero": "Georgia", "body": "Segoe UI", "mono": "Consolas"}
    th = theme("D3-two-futures.json", pal, F)
    v = [kicker("z_masthead", 24, 16, 1232, 24, 1, 1, "GOODNIGHT INN  ·  TWO FUTURES  ·  2025 ACTUAL AND 2032 IF NOTHING IS FUNDED", pal, F),
         headline("z_headline", 24, 40, 1232, 48, 2, 2, "The market will fill our rooms. It will not protect our margin.", pal, F)]
    q = {"Category": {"projections": [proj_col("Timeline", "Year", active=True)]}, "Y": {"projections": [proj_mea("Margin Actual (timeline)"), proj_mea("Margin Baseline (timeline)")]}}
    v.append(chart("hero_margin_fan", "lineChart", 24, 104, 616, 264, 10, 10, q, pal, F, title="GOP MARGIN 2021 TO 2032: actual, then the do-nothing projection (scenario logic, organisers' assumptions)",
                   objects={"categoryAxis": axis(F["mono"], 9, pal["ink2"]), "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=True, grid_color=pal["hair"], start=0.35, end=0.5),
                            "legend": legend(True, F["body"], 9, pal["ink2"], "Top"),
                            "dataPoint": series_colors({mref("Margin Actual (timeline)"): pal["ink"], mref("Margin Baseline (timeline)"): pal["neutral"]}),
                            "lineStyles": line_styles({mref("Margin Actual (timeline)"): 3, mref("Margin Baseline (timeline)"): 2}, dashed=(mref("Margin Baseline (timeline)"),), markers=True),
                            "labels": labels(True, F["mono"], 8, pal["ink2"], precision=1)},
                   alt="Line of actual GOP margin 2021 to 2025 continued by a dashed do-nothing projection to 2032"))
    q = {"Category": {"projections": [proj_col("BridgeStep", "Step", active=True)]}, "Y": {"projections": [proj_mea("Bridge Value")]}}
    v.append(chart("ch_bridge_2032", "waterfallChart", 656, 104, 600, 264, 11, 11, q, pal, F, title="WHAT 2032 IS MADE OF: GOP 2025 to 2032 baseline, $ (scenario logic)",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink2"], gridlines=None), "valueAxis": axis(F["mono"], 8, pal["ink2"], gridlines=False, units=1),
                            "sentimentColors": [{"properties": {"increaseFill": color(pal["good"]), "decreaseFill": color(pal["bad"]), "totalFill": color(pal["ink"]), "otherFill": color(pal["neutral"])}}],
                            "labels": labels(True, F["mono"], 8, pal["ink"]), "legend": legend(False)},
                   filters=[filter_in("BridgeStep", "Bridge", ["Baseline 2025 to 2032"], "flt_bridge32")], sort=sort_by_column("BridgeStep", "Sort"),
                   alt="Waterfall from 2025 GOP to the 2032 baseline: volume the market gives, price inflation, cost inflation"))
    q = {"Values": {"projections": [proj_col("Hotels", "Hotel Short Name", display="Hotel"), proj_col("Hotels", "LocationType", display="Type"), proj_mea("Occupancy % 2025", "Occupancy 2025"), proj_mea("First Capped Year", "Full in"), proj_mea("Capacity (text)", "Reading"), proj_mea("Unmet Room Nights", "Unmet nights 2025 to 2032")]}}
    v.append(chart("tbl_capacity_wall", "tableEx", 24, 384, 616, 208, 20, 20, q, pal, F, title="THE CAPACITY WALL: hotels that run out of rooms before 2032 (scenario logic)",
                   objects=table_objects(F["mono"], 8, pal["ink"], pal["surface"], pal["surface"], pal["surface"], pal["ink2"], pal["hair"], row_padding=2),
                   filters=[filter_measure_gt("First Capped Year", 0, "flt_capped")], sort=sort_by_measure("First Capped Year", desc=False),
                   alt="Table of hotels with the first year demand exceeds capacity and the unmet room nights"))
    v.append(folio_table("tbl_folio", 656, 384, 296, 128, 21, 21, pal, F, title="THE MIDDLEMAN, PRICED: one room night 2025"))
    v.append(card("kpi_dist_pct", 968, 384, 288, 56, 22, 22, ["Distribution Cost % of Room Revenue 2021", "Distribution Cost % of Room Revenue 2025"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["distribution cost 2021", "distribution cost 2025"], alt="Distribution cost as a share of room revenue, 2021 and 2025"))
    v.append(card("kpi_above_mix", 968, 448, 288, 64, 23, 23, ["Distribution Cost above 2021 Mix 2025"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["a year above the 2021 channel mix (counterfactual)"], alt="Distribution cost above the 2021 mix"))
    v.append(note("c_scenario_note", 656, 520, 600, 72, 24, 24, [("SCENARIO LOGIC, STATED", "The do-nothing future holds 2025 unit economics per hotel and applies the organisers' regional demand growth, ADR inflation and cost inflation for 2026 to 2032, with demand capped at 97 percent occupancy. No channel drift is assumed. Impacts stay in 2025 dollars.")], pal, F, size=9))
    v.append(note("c_method", 24, 600, 1232, 88, 25, 25, [("HOW TO READ THIS PAGE", "Every projected mark is scenario logic, not data: it is derived in the model from the FinanceAssumptions table and labeled as such. Actuals end in December 2025. The folio prices a 2025 room night at the average rate per channel and subtracts the channel's cost per night.")], pal, F, size=9))
    v.append(footer(pal, F))
    p1 = page("p1-if-we-do-nothing", "2032, if we do nothing", v, pal["canvas"], GI())

    v = [kicker("z_masthead2", 24, 16, 1232, 24, 1, 1, "THE PLAN AGAINST THE BASELINE  ·  2025 TO 2032  ·  OPERATING PROFIT IN 2025 DOLLARS", pal, F),
         card("z_headline2", 24, 40, 1232, 48, 2, 2, ["Headline Plan (text)"], F["hero"], 20, pal["ink"], alt="Dynamic headline of the selected plan")]
    v.append(scenario_slicer("sl_scenario", 24, 104, 312, 48, 10, 10, pal, F))
    v.append(card("kpi_capex", 352, 104, 288, 48, 11, 11, ["Capex Selected", "Budget Used %"], F["hero"], 14, pal["ink"], F["body"], 8, pal["ink2"], labels=["capex selected", "of $60 M"], alt="Capex selected and budget share"))
    q = {"Category": {"projections": [proj_col("Timeline", "Year", active=True)]}, "Y": {"projections": [proj_mea("GOP Baseline (timeline)"), proj_mea("GOP Plan (timeline)"), proj_mea("GOP Plan (timeline, Low)"), proj_mea("GOP Plan (timeline, High)")]}}
    v.append(chart("hero_op_vs_baseline", "lineChart", 24, 160, 616, 264, 12, 12, q, pal, F, title="OPERATING PROFIT 2025 TO 2032: do-nothing baseline (grey) vs the plan (amber), Low and High dashed. Works dip 2027 to 2028, ramp 50 / 85 / 100 percent",
                   objects={"categoryAxis": axis(F["mono"], 9, pal["ink2"]), "valueAxis": axis(F["mono"], 9, pal["ink2"], gridlines=True, grid_color=pal["hair"], units=1),
                            "legend": legend(True, F["body"], 8, pal["ink2"], "Top"),
                            "dataPoint": series_colors({mref("GOP Baseline (timeline)"): pal["neutral"], mref("GOP Plan (timeline)"): pal["accent"], mref("GOP Plan (timeline, Low)"): pal["accent"], mref("GOP Plan (timeline, High)"): pal["accent"]}),
                            "lineStyles": line_styles({mref("GOP Plan (timeline)"): 3, mref("GOP Baseline (timeline)"): 2, mref("GOP Plan (timeline, Low)"): 1, mref("GOP Plan (timeline, High)"): 1}, dashed=(mref("GOP Plan (timeline, Low)"), mref("GOP Plan (timeline, High)")))},
                   filters=[filter_in("Timeline", "Year", [2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032], "flt_outlook_years")],
                   alt="Lines of baseline GOP and plan GOP 2025 to 2032 with Low and High variants"))
    q = {"Category": {"projections": [proj_col("InvestmentProjects", "Short Name", active=True)]}, "Y": {"projections": [proj_mea("Net Impact")]}}
    v.append(chart("ch_cumulative_per_initiative", "clusteredBarChart", 24, 432, 616, 160, 13, 13, q, pal, F, title="CUMULATIVE NET 2027 TO 2032 PER INITIATIVE, $ (capex counted; payback year in the ledger)",
                   objects={"categoryAxis": axis(F["body"], 8, pal["ink"]), "valueAxis": axis(F["mono"], 8, pal["ink2"], show=False),
                            "dataPoint": series_colors({}, default=pal["accent"]),
                            "labels": labels(True, F["mono"], 8, pal["ink"]), "legend": legend(False)},
                   sort=sort_by_measure("Net Impact"), alt="Diverging bars of cumulative net impact per selected initiative"))
    q = {"Values": {"projections": [proj_col("InvestmentProjects", "Short Name", display="Initiative"), proj_mea("Capex Selected", "Capex"), proj_mea("Start (text)", "Start"), proj_mea("Live (text)", "Live"),
                                     proj_mea("2032 Run-rate", "Run-rate 2032"), proj_mea("Net Impact", "Net through 2032"), proj_mea("Payback (text)", "Payback")]}}
    v.append(chart("tbl_ledger", "tableEx", 656, 104, 600, 320, 20, 20, q, pal, F, title="THE LEDGER: the selected initiatives",
                   objects=table_objects(F["mono"], 9, pal["ink"], pal["surface"], pal["surface"], pal["surface"], pal["ink2"], pal["hair"], row_padding=4, totals=True),
                   sort=sort_by_column("InvestmentProjects", "Short Name"), alt="Ledger of initiatives with capex, start, go-live, run-rate, net through 2032 and payback"))
    v.append(plan_slicer("sl_plan_builder", 656, 432, 600, 80, 21, 21, pal, F, mode="Dropdown"))
    v.append(card("kpi_ledger_totals", 656, 520, 600, 72, 22, 22, ["2032 Run-rate", "NPV @ 8%", "Payback (text)", "Rooms Added"], F["hero"], 16, pal["ink"], F["body"], 8, pal["ink2"],
                  labels=["run-rate by 2032", "NPV at 8 percent through 2032", "payback year", "rooms added"], alt="Totals of the selection"))
    v.append(note("c_horizon_note", 24, 600, 1232, 88, 30, 30, [("THE HORIZON TRAP", "Capital projects pay back after the horizon: the ramp finishes in 2030 and the organisers measure impact through December 2032, so every refresh or extension is cumulative-negative by then. The run-rate is the number to read; the payback year says when the cash turns.")], pal, F, size=9))
    v.append(footer(pal, F))
    p2 = page("p2-with-the-plan", "2032, with the plan", v, pal["canvas"], GI())
    write_report(PBIP, "D3-two-futures", "D3 Two futures", [p1, p2], th, "D3-two-futures.json")


if __name__ == "__main__":
    build_d1()
    build_d2()
    build_d3()
    print("reports written")
