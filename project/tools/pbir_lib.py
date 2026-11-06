"""Small PBIR authoring helpers for the sketch generator (no third-party code).

Shapes verified against the Microsoft powerbi-report-authoring references and the
previous World Champs builds in E:\\PowerBI Set-up. Every position is a multiple of 8.
"""
import json
import uuid
from pathlib import Path

NS = uuid.UUID("7b1f2a9e-6d3c-4b8e-9f21-3c5d7e8a9b10")
VISUAL_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.11.0/schema.json"
PAGE_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json"
PAGES_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.1.0/schema.json"
REPORT_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.3.0/schema.json"
VERSION_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json"
PBIR_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json"
PBIP_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/pbip/pbipProperties/1.0.0/schema.json"
PLATFORM_SCHEMA = "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json"
MEAS = "_Measures"


def tag(name):
    return str(uuid.uuid5(NS, name))


# ------------------------------------------------------------------ literals
def lit(v):
    return {"expr": {"Literal": {"Value": v}}}


def b(v):
    return lit("true" if v else "false")


def num(v):
    return lit(f"{v}D")


def integer(v):
    return lit(f"{v}L")


def enum(v):
    return lit(f"'{v}'")


def text(v):
    return lit("'" + v.replace("'", "''") + "'")


def color(hexv):
    return {"solid": {"color": {"expr": {"Literal": {"Value": f"'{hexv}'"}}}}}


# ------------------------------------------------------------------ fields
def col(table, name):
    return {"Column": {"Expression": {"SourceRef": {"Entity": table}}, "Property": name}}


def mea(name):
    return {"Measure": {"Expression": {"SourceRef": {"Entity": MEAS}}, "Property": name}}


def proj_col(table, name, active=None, display=None):
    p = {"field": col(table, name), "queryRef": f"{table}.{name}", "nativeQueryRef": name}
    if active is not None:
        p["active"] = active
    if display:
        p["displayName"] = display
    return p


def proj_mea(name, display=None):
    p = {"field": mea(name), "queryRef": f"{MEAS}.{name}", "nativeQueryRef": name}
    if display:
        p["displayName"] = display
    return p


def mref(name):
    return f"{MEAS}.{name}"


# ------------------------------------------------------------------ filters
_FLT = [0]


def filter_in(table, column, values, name=None):
    """Categorical In filter on a column (strings or ints)."""
    _FLT[0] += 1
    name = (name + "_" + str(_FLT[0])) if name else None
    vals = []
    for v in values:
        vals.append([{"Literal": {"Value": f"'{v}'" if isinstance(v, str) else f"{v}L"}}])
    return {
        "name": name or ("flt_" + tag(f"{table}.{column}.{values}")[:12]),
        "field": col(table, column),
        "type": "Categorical",
        "filter": {
            "Version": 2,
            "From": [{"Name": "f", "Entity": table, "Type": 0}],
            "Where": [{"Condition": {"In": {
                "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "f"}}, "Property": column}}],
                "Values": vals}}}],
        },
        "howCreated": "User",
    }


def filter_measure_gt(measure, value, name=None):
    """Advanced filter: measure > value (numeric literal)."""
    _FLT[0] += 1
    return {
        "name": (name or "flt_m") + "_" + str(_FLT[0]),
        "field": mea(measure),
        "type": "Advanced",
        "filter": {
            "Version": 2,
            "From": [{"Name": "m", "Entity": MEAS, "Type": 0}],
            "Where": [{"Condition": {"Comparison": {"ComparisonKind": 1, "Left": {"Measure": {"Expression": {"SourceRef": {"Source": "m"}}, "Property": measure}}, "Right": {"Literal": {"Value": f"{value}L"}}}}}],
        },
        "howCreated": "User",
    }


def filter_topn(table, column, n, by_measure, name=None):
    return {
        "name": name or ("flt_top_" + tag(f"{table}.{column}.{n}")[:10]),
        "field": col(table, column),
        "type": "TopN",
        "filter": {
            "Version": 2,
            "From": [{"Name": "f", "Entity": table, "Type": 0}, {"Name": "m", "Entity": MEAS, "Type": 0}],
            "Where": [{"Condition": {"Top": {
                "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "f"}}, "Property": column}}],
                "OrderBy": [{"Direction": 2, "Expression": {"Measure": {"Expression": {"SourceRef": {"Source": "m"}}, "Property": by_measure}}}],
                "Top": n}}}],
        },
        "howCreated": "User",
    }


# ------------------------------------------------------------------ chrome
def vco(title=None, title_font=None, title_size=10, title_color=None, alt=None, bg=None, border=None, padding=None, extra=None):
    v = {
        "title": [{"properties": {"show": b(bool(title)), **({"text": text(title), "fontFamily": text(title_font), "fontSize": num(title_size), "fontColor": color(title_color)} if title else {})}}],
        "background": [{"properties": {"show": b(bool(bg)), **({"color": color(bg), "transparency": num(0)} if bg else {})}}],
        "border": [{"properties": {"show": b(bool(border)), **({"color": color(border), "radius": num(0), "width": num(1)} if border else {})}}],
        "dropShadow": [{"properties": {"show": b(False)}}],
        "visualHeader": [{"properties": {"show": b(False)}}],
        "subTitle": [{"properties": {"show": b(False)}}],
    }
    if padding is not None:
        v["padding"] = [{"properties": {k: num(padding) for k in ("top", "bottom", "left", "right")}}]
    if alt:
        v["general"] = [{"properties": {"altText": text(alt)}}]
    if extra:
        v.update(extra)
    return v


def visual(name, vtype, x, y, w, h, z, tab, query=None, objects=None, vcos=None, filters=None, sort=None, drill=False):
    for v in (x, y, w, h):
        assert v % 8 == 0, (name, x, y, w, h)
    vis = {"visualType": vtype}
    if query is not None:
        vis["query"] = {"queryState": query}
        if sort:
            vis["query"]["sortDefinition"] = {"sort": sort, "isDefaultSort": True}
    if objects:
        vis["objects"] = objects
    if vcos:
        vis["visualContainerObjects"] = vcos
    vis["drillFilterOtherVisuals"] = drill
    out = {"$schema": VISUAL_SCHEMA, "name": name, "position": {"x": x, "y": y, "z": z, "width": w, "height": h, "tabOrder": tab}, "visual": vis}
    if filters:
        out["filterConfig"] = {"filters": filters}
    return out


def sort_by_measure(name, desc=True):
    return [{"field": mea(name), "direction": "Descending" if desc else "Ascending"}]


def sort_by_column(table, name, desc=False):
    return [{"field": col(table, name), "direction": "Descending" if desc else "Ascending"}]


# ------------------------------------------------------------------ visuals
def textbox(name, x, y, w, h, z, tab, runs, align="left", alt=None):
    """runs: list of paragraphs; each paragraph = list of (text, font, size_px, color, bold)."""
    paragraphs = []
    for para in runs:
        tr = []
        for t, font, size, c, bold in para:
            style = {"fontFamily": font, "fontSize": f"{size}px", "color": c}
            if bold:
                style["fontWeight"] = "bold"
            tr.append({"value": t, "textStyle": style})
        paragraphs.append({"textRuns": tr, "horizontalTextAlignment": align})
    objects = {"general": [{"properties": {"paragraphs": paragraphs}}]}
    return visual(name, "textbox", x, y, w, h, z, tab, objects=objects, vcos=vco(alt=alt, padding=0))


def card(name, x, y, w, h, z, tab, measures, value_font, value_size, value_color, label_font=None, label_size=9, label_color=None, labels=None, units=None, precision=None, align="left", alt=None, title=None, tf=None, tc=None):
    """cardVisual with one or more measures. labels: list of label texts (same order) or None to hide."""
    projections = [proj_mea(mn) for mn in measures]
    value_props = {"show": b(True), "fontFamily": text(value_font), "fontSize": num(value_size), "fontColor": color(value_color), "horizontalAlignment": enum(align), "textWrap": b(True)}
    value_props["labelDisplayUnits"] = integer(units if units is not None else 1)
    if precision is not None:
        value_props["labelPrecision"] = integer(precision)
    objects = {
        "value": [{"properties": value_props, "selector": {"id": "default"}}],
        "outline": [{"properties": {"show": b(False)}, "selector": {"id": "default"}}],
        "padding": [{"properties": {"paddingUniform": integer(0)}, "selector": {"id": "default"}}],
        "layout": [{"properties": {"paddingUniform": integer(0), "topOuterMargin": integer(0), "bottomOuterMargin": integer(0), "leftOuterMargin": integer(0), "rightOuterMargin": integer(0)}, "selector": {"id": "default"}}],
        "spacing": [{"properties": {"verticalSpacing": num(0)}, "selector": {"id": "default"}}],
        "cardCalloutArea": [{"properties": {"paddingUniform": integer(0)}}],
    }
    if labels:
        label_props = {"show": b(True), "fontFamily": text(label_font or value_font), "fontSize": num(label_size), "fontColor": color(label_color or value_color), "position": enum("belowValue"), "horizontalAlignment": enum(align)}
        if len(measures) == 1:
            label_props["text"] = text(labels[0])
            objects["label"] = [{"properties": label_props, "selector": {"id": "default"}}]
        else:
            objects["label"] = [{"properties": label_props, "selector": {"id": "default"}}]
            # per-measure label text via metadata selector
            for mn, lb in zip(measures, labels):
                objects["label"].append({"properties": {"text": text(lb)}, "selector": {"metadata": mref(mn)}})
    else:
        objects["label"] = [{"properties": {"show": b(False)}, "selector": {"id": "default"}}]
    return visual(name, "cardVisual", x, y, w, h, z, tab, query={"Data": {"projections": projections}}, objects=objects, vcos=vco(title=title, title_font=tf, title_color=tc, alt=alt, padding=0))


def axis(font, size, colour, show=True, title=False, gridlines=False, grid_color=None, units=None, start=None, end=None, extra=None):
    p = {"show": b(show), "fontFamily": text(font), "fontSize": num(size), "labelColor": color(colour), "showAxisTitle": b(title)}
    if gridlines is not None:
        p["gridlineShow"] = b(gridlines)
    if gridlines and grid_color:
        p["gridlineColor"] = color(grid_color)
        p["gridlineThickness"] = num(1)
    if units is not None:
        p["labelDisplayUnits"] = integer(units)
    if start is not None:
        p["start"] = num(start)
    if end is not None:
        p["end"] = num(end)
    if extra:
        p.update(extra)
    return [{"properties": p}]


def legend(show, font=None, size=9, colour=None, position="Bottom"):
    p = {"show": b(show)}
    if show:
        p.update({"position": enum(position), "fontFamily": text(font), "fontSize": num(size), "labelColor": color(colour), "showTitle": b(False)})
    return [{"properties": p}]


def labels(show, font=None, size=9, colour=None, units=None, precision=None, position=None):
    p = {"show": b(show)}
    if show:
        p.update({"fontFamily": text(font), "fontSize": num(size), "color": color(colour)})
        if units is not None:
            p["labelDisplayUnits"] = integer(units)
        if precision is not None and units != 1:
            p["labelPrecision"] = integer(precision)
        if position:
            p["labelPosition"] = enum(position)
    return [{"properties": p}]


def series_colors(mapping, default=None):
    """dataPoint entries: mapping of queryRef -> hex; optional default."""
    out = []
    if default:
        out.append({"properties": {"defaultColor": color(default)}})
    for qref, hexv in mapping.items():
        out.append({"properties": {"fill": color(hexv)}, "selector": {"metadata": qref}})
    return out


def line_styles(mapping, default_width=2, dashed=(), markers=False):
    out = [{"properties": {"strokeWidth": num(default_width), "showMarker": b(markers), "lineChartType": enum("linear")}}]
    for qref, width in mapping.items():
        p = {"strokeWidth": num(width)}
        if qref in dashed:
            p["lineStyle"] = enum("dashed")
        out.append({"properties": p, "selector": {"metadata": qref}})
    return out


def table_objects(font, size, ink, bg_odd, bg_even, header_bg, header_ink, hairline, row_padding=2, header_size=None, extra_values=None, column_formatting=None, totals=False):
    objects = {
        "columnHeaders": [{"properties": {"fontFamily": text(font), "fontSize": num(header_size or size), "fontColor": color(header_ink), "backColor": color(header_bg), "outlineStyle": enum("None"), "autoSizeColumnWidth": b(True), "columnAdjustment": enum("growToFit"), "bold": b(False)}}],
        "values": [{"properties": {"fontFamily": text(font), "fontSize": num(size), "fontColorPrimary": color(ink), "fontColorSecondary": color(ink), "backColorPrimary": color(bg_odd), "backColorSecondary": color(bg_even), "outlineStyle": enum("None")}}] + (extra_values or []),
        "grid": [{"properties": {"gridVertical": b(False), "gridHorizontal": b(True), "gridHorizontalColor": color(hairline), "gridHorizontalWeight": num(1), "rowPadding": num(row_padding), "outlineStyle": enum("None")}}],
        "total": [{"properties": {"totals": b(totals)}}],
    }
    if column_formatting:
        objects["columnFormatting"] = column_formatting
    return objects


def data_bars(qref, positive, axis_color):
    return {"properties": {"dataBars": {"positiveColor": color(positive), "negativeColor": color(positive), "axisColor": color(axis_color), "reverseDirection": b(False), "hideText": b(False)}}, "selector": {"metadata": qref}}


def rule_backcolor(qref, measure, cases, default):
    """cases: list of (comparisonKind, literal, hex)."""
    return {"properties": {"backColor": {"solid": {"color": {"expr": {"Conditional": {"Cases": [
        {"Condition": {"Comparison": {"ComparisonKind": kind, "Left": mea(measure), "Right": {"Literal": {"Value": litv}}}}, "Value": {"Literal": {"Value": f"'{hexv}'"}}} for kind, litv, hexv in cases
    ], "DefaultValue": {"Literal": {"Value": f"'{default}'"}}}}}}}}, "selector": {"data": [{"dataViewWildcard": {"matchingOption": 1}}], "metadata": qref}}


def rule_fontcolor(qref, measure, cases, default):
    r = rule_backcolor(qref, measure, cases, default)
    r["properties"] = {"fontColor": r["properties"]["backColor"]}
    return r


def slicer(name, x, y, w, h, z, tab, table, column, header, font, ink, ink2, bg, accent, mode="Basic", single=False, horizontal=False, selected=None, search=False, alt=None, size=9):
    objects = {
        "data": [{"properties": {"mode": enum(mode)}}],
        "header": [{"properties": {"show": b(True), "text": text(header), "fontFamily": text(font), "textSize": num(size), "fontColor": color(ink2), "outlineStyle": enum("None")}}],
        "items": [{"properties": {"fontFamily": text(font), "textSize": num(size), "fontColor": color(ink), "background": color(bg), "outlineStyle": enum("None"), "padding": num(2)}}],
        "selection": [{"properties": {"singleSelect": b(single), "strictSingleSelect": b(single), "selectAllCheckboxEnabled": b(False)}}],
    }
    general = {"orientation": num(1 if horizontal else 0)}
    if selected:
        general["filter"] = {"filter": {
            "Version": 2,
            "From": [{"Name": "s", "Entity": table, "Type": 0}],
            "Where": [{"Condition": {"In": {
                "Expressions": [{"Column": {"Expression": {"SourceRef": {"Source": "s"}}, "Property": column}}],
                "Values": [[{"Literal": {"Value": f"'{v}'" if isinstance(v, str) else f"{v}L"}}] for v in selected]}}}],
        }}
    objects["general"] = [{"properties": general}]
    return visual(name, "slicer", x, y, w, h, z, tab, query={"Values": {"projections": [proj_col(table, column)]}}, objects=objects, vcos=vco(alt=alt, padding=0))


# ------------------------------------------------------------------ pages and report
def page(name, display, visuals, bg, filters=None, hidden=False):
    p = {"$schema": PAGE_SCHEMA, "name": name, "displayName": display, "displayOption": "FitToPage", "height": 720, "width": 1280,
         "objects": {"background": [{"properties": {"color": color(bg), "transparency": num(0)}}]}}
    if filters:
        p["filterConfig"] = {"filters": filters}
    if hidden:
        p["visibility"] = "HiddenInViewMode"
    return p, visuals


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def write_report(root, name, display, pages, theme, theme_name, model_folder="PillowKey.SemanticModel"):
    rep = root / f"{name}.Report"
    import shutil
    if rep.exists():
        shutil.rmtree(rep)
    write_json(root / f"{name}.pbip", {"$schema": PBIP_SCHEMA, "version": "1.0", "artifacts": [{"report": {"path": f"{name}.Report"}}], "settings": {"enableAutoRecovery": True}})
    write_json(rep / ".platform", {"$schema": PLATFORM_SCHEMA, "metadata": {"type": "Report", "displayName": display}, "config": {"version": "2.0", "logicalId": tag("platform." + name)}})
    write_json(rep / "definition.pbir", {"$schema": PBIR_SCHEMA, "version": "4.0", "datasetReference": {"byPath": {"path": f"../{model_folder}"}}})
    write_json(rep / "definition" / "version.json", {"$schema": VERSION_SCHEMA, "version": "2.0.0"})
    write_json(rep / "definition" / "report.json", {
        "$schema": REPORT_SCHEMA,
        "themeCollection": {
            "baseTheme": {"name": "Fluent2-CY26SU05", "reportVersionAtImport": {"visual": "2.9.0", "report": "3.3.0", "page": "2.3.1"}, "type": "SharedResources"},
            "customTheme": {"name": theme_name, "reportVersionAtImport": {"visual": "2.10.0", "report": "3.4.0", "page": "2.3.1"}, "type": "RegisteredResources"},
        },
        "objects": {"outspacePane": [{"properties": {"expanded": b(False), "visible": b(False)}}]},
        "resourcePackages": [
            {"name": "SharedResources", "type": "SharedResources", "items": [{"name": "Fluent2-CY26SU05", "path": "BaseThemes/Fluent2-CY26SU05.json", "type": "BaseTheme"}]},
            {"name": "RegisteredResources", "type": "RegisteredResources", "items": [{"name": theme_name, "path": theme_name, "type": "CustomTheme"}]},
        ],
    })
    write_json(rep / "StaticResources" / "RegisteredResources" / theme_name, theme)
    order = []
    for pg, visuals in pages:
        order.append(pg["name"])
        write_json(rep / "definition" / "pages" / pg["name"] / "page.json", pg)
        for v in visuals:
            write_json(rep / "definition" / "pages" / pg["name"] / "visuals" / v["name"] / "visual.json", v)
    write_json(rep / "definition" / "pages" / "pages.json", {"$schema": PAGES_SCHEMA, "pageOrder": order, "activePageName": order[0]})
    return rep


def theme(name, pal, fonts):
    name = name  # must equal the registered file name (validator rule)
    """pal: dict canvas, surface, ink, ink2, hair, accent, good, bad, neutral, extra(list). fonts: hero, body, mono."""
    data_colors = [pal["accent"], pal["ink"], pal["neutral"], pal["good"], pal["bad"], pal["ink2"], pal["hair"], pal["surface"]] + pal.get("extra", [])
    return {
        "name": name,
        "dataColors": data_colors,
        "good": pal["good"], "neutral": pal["neutral"], "bad": pal["bad"],
        "maximum": pal["accent"], "center": pal["neutral"], "minimum": pal["ink2"], "null": pal["hair"],
        "background": pal["canvas"], "secondaryBackground": pal["surface"],
        "foreground": pal["ink"], "foregroundNeutralSecondary": pal["ink2"], "foregroundNeutralTertiary": pal["hair"],
        "firstLevelElements": pal["ink"], "secondLevelElements": pal["ink2"], "thirdLevelElements": pal["hair"], "fourthLevelElements": pal["neutral"],
        "backgroundLight": pal["surface"], "backgroundNeutral": pal["hair"], "tableAccent": pal["accent"],
        "shapeStroke": pal["hair"], "disabledText": pal["neutral"], "hyperlink": pal["accent"], "visitedHyperlink": pal["accent"],
        "textClasses": {
            "callout": {"fontFace": fonts["hero"], "fontSize": 24, "color": pal["ink"]},
            "title": {"fontFace": fonts["body"], "fontSize": 10, "color": pal["ink2"]},
            "largeTitle": {"fontFace": fonts["hero"], "fontSize": 20, "color": pal["ink"]},
            "header": {"fontFace": fonts["body"], "fontSize": 12, "color": pal["ink"]},
            "label": {"fontFace": fonts["body"], "fontSize": 9, "color": pal["ink"]},
            "semiboldLabel": {"fontFace": fonts["body"], "fontSize": 9, "color": pal["ink"]},
            "boldLabel": {"fontFace": fonts["body"], "fontSize": 9, "color": pal["ink"]},
            "largeLabel": {"fontFace": fonts["body"], "fontSize": 11, "color": pal["ink"]},
            "smallLabel": {"fontFace": fonts["body"], "fontSize": 8, "color": pal["ink"]},
            "lightLabel": {"fontFace": fonts["body"], "fontSize": 9, "color": pal["ink2"]},
            "largeLightLabel": {"fontFace": fonts["body"], "fontSize": 11, "color": pal["ink2"]},
            "smallLightLabel": {"fontFace": fonts["body"], "fontSize": 8, "color": pal["ink2"]},
            "dataTitle": {"fontFace": fonts["mono"], "fontSize": 9, "color": pal["ink2"]},
        },
        "visualStyles": {
            "*": {"*": {
                "background": [{"show": False}],
                "border": [{"show": False}],
                "dropShadow": [{"show": False}],
                "visualHeader": [{"show": False}],
                "padding": [{"top": 0, "bottom": 0, "left": 0, "right": 0}],
                "title": [{"show": False}],
                "subTitle": [{"show": False}],
            }},
            "page": {"*": {"background": [{"color": {"solid": {"color": pal["canvas"]}}, "transparency": 0}], "outspace": [{"color": {"solid": {"color": pal["canvas"]}}, "transparency": 0}]}},
            "tableEx": {"*": {"columnHeaders": [{"autoSizeColumnWidth": True, "columnAdjustment": "growToFit"}]}},
            "pivotTable": {"*": {"columnHeaders": [{"autoSizeColumnWidth": True, "columnAdjustment": "growToFit"}]}},
        },
    }
