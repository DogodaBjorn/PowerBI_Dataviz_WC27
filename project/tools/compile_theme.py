"""Compile the active brand kit into project/deliverables/theme.json.

Implements the theme-from-brand-kit procedure for this project. Every property
emitted below was checked against Microsoft's report theme schema 2.159
(microsoft/powerbi-desktop-samples, "Report Theme JSON Schema/reportThemeSchema-2.159.json",
matching Desktop Store build 2.159) on 2026-11-06:
  top level: name, $schema, dataColors, accent, good, neutral, bad, minimum,
             center, maximum, null, background, secondaryBackground,
             backgroundLight, backgroundNeutral, foreground,
             foregroundNeutralSecondary, firstLevelElements, secondLevelElements,
             thirdLevelElements, fourthLevelElements, tableAccent, shapeStroke,
             disabledText, hyperlink, visitedHyperlink, textClasses, visualStyles
  textClass: fontFace, fontSize, color   (fontWeight exists but its values are
             not enumerated in the schema, so it is deliberately not emitted)
  commonCards: background{show,color,transparency}, border{show,color,radius,width},
             dropShadow{show}, title{show,fontFamily,fontSize,fontColor,bold},
             subTitle{fontFamily,fontSize,fontColor}, visualHeader{show,foreground,
             background,transparency}, visualTooltip{fontFamily,fontSize,background,
             titleFontColor,valueFontColor}
  page: background{color,transparency}, outspace{color,transparency}
Usage: python project/tools/compile_theme.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import miniyaml  # stdlib-only YAML subset reader shipped with the template

SCHEMA = ("https://raw.githubusercontent.com/microsoft/powerbi-desktop-samples/main/"
          "Report%20Theme%20JSON%20Schema/reportThemeSchema-2.159.json")

project = open(os.path.join(ROOT, "project", "project.yaml"), encoding="utf-8").read()
kit_name = re.search(r"^brand_kit:\s*([A-Za-z0-9_-]+)", project, re.M).group(1)
kit = miniyaml.load(os.path.join(ROOT, "design", "brand-kits", kit_name, "brand.yaml"))
c, t, shape = kit["color"], kit["typography"], kit["shape"]
first = lambda stack: stack.split(",")[0].strip()          # Power BI takes one face
display, body, numeric = first(t["display"]), first(t["body"]), first(t["numeric"])
hero, page_title, section, body_pt, caption = t["scale_pt"]
fill = lambda hex_: {"solid": {"color": hex_}}

def tc(face, size, color):
    return {"fontFace": face, "fontSize": size, "color": color}

theme = {
    "$schema": SCHEMA,
    "name": f"Goodnight Inn ({kit_name})",
    "dataColors": list(c["categorical"]),
    "accent": c["accent"],
    "good": c["good"], "neutral": c["neutral_data"], "bad": c["bad"],
    "minimum": c["diverging"][0], "center": c["diverging"][2], "maximum": c["diverging"][-1],
    "null": c["categorical"][-1],
    "background": c["surface"], "secondaryBackground": c["canvas"],
    "backgroundLight": c["surface"], "backgroundNeutral": c["hairline"],
    "foreground": c["ink"], "foregroundNeutralSecondary": c["ink_secondary"],
    "firstLevelElements": c["ink"], "secondLevelElements": c["ink_secondary"],
    "thirdLevelElements": c["hairline"], "fourthLevelElements": c["neutral_data"],
    "tableAccent": c["accent"], "shapeStroke": c["hairline"], "disabledText": c["neutral_data"],
    "hyperlink": c["accent"], "visitedHyperlink": c["accent"],
    "textClasses": {
        "callout": tc(numeric, hero - 2, c["ink"]),          # card values
        "largeTitle": tc(display, page_title, c["ink"]),
        "title": tc(display, section, c["ink"]),             # visual titles
        "header": tc(body, body_pt, c["ink"]),
        "label": tc(body, body_pt, c["ink"]),
        "semiboldLabel": tc(body, body_pt, c["ink"]),
        "boldLabel": tc(body, body_pt, c["ink"]),
        "largeLabel": tc(body, section, c["ink"]),
        "smallLabel": tc(body, caption, c["ink"]),
        "lightLabel": tc(body, body_pt, c["ink_secondary"]),
        "largeLightLabel": tc(body, section, c["ink_secondary"]),
        "smallLightLabel": tc(body, caption, c["ink_secondary"]),
        "dataTitle": tc(body, caption, c["ink_secondary"]),
        "smallDataLabel": tc(numeric, caption, c["ink"]),
    },
    "visualStyles": {
        "*": {"*": {
            "background": [{"show": True, "color": fill(c["surface"]), "transparency": 0}],
            "border": [{"show": True, "color": fill(c["hairline"]),
                        "radius": shape["radius_px"], "width": shape["hairline_px"]}],
            "dropShadow": [{"show": shape["shadow"] != "none"}],
            "title": [{"show": True, "fontFamily": display, "fontSize": section,
                       "fontColor": fill(c["ink"]), "bold": True}],
            "subTitle": [{"fontFamily": body, "fontSize": caption,
                          "fontColor": fill(c["ink_secondary"])}],
            # kept visible: the header carries "show as a table" and focus mode,
            # accessibility features the contest scores
            "visualHeader": [{"show": True, "foreground": fill(c["ink_secondary"]),
                              "background": fill(c["surface"]), "transparency": 0}],
            "visualTooltip": [{"fontFamily": body, "fontSize": caption,
                               "background": fill(c["surface"]),
                               "titleFontColor": fill(c["ink_secondary"]),
                               "valueFontColor": fill(c["ink"])}],
        }},
        # P-2, one control language (doc 21 section 3; FinalV3 build step 5): the state model of the light surface set
        # once, here. A control that sets nothing gets the secondary look (white, 1 px Dusk outline, Night text) and the
        # Seam hover; a visual sets only its size, its shape, its text and, for a primary or a masthead control, its fill.
        # Checked against reportThemeSchema-2.159 (visual-actionButton fill / text / outline with $id default, hover,
        # selected; actionStates-advancedSlicerVisual for outline and value). The slicer's fill states are not in the
        # theme schema (fillCustom carries no $id), so button_slicer() keeps them per visual. No shape here: a theme
        # shape would turn P2's tabs into pills (they are 8 px rectangles, the large size).
        "actionButton": {"*": {
            "fill": [{"$id": "default", "show": True, "fillColor": fill(c["surface"]), "transparency": 0},
                     {"$id": "hover", "fillColor": fill(c["hairline"]), "transparency": 0},
                     {"$id": "selected", "fillColor": fill(c["hairline"]), "transparency": 0}],
            "text": [{"$id": "default", "show": True, "fontFamily": body, "fontSize": body_pt, "fontColor": fill(c["ink"]), "bold": False},
                     {"$id": "hover", "fontColor": fill(c["ink"])},
                     {"$id": "selected", "fontColor": fill(c["ink"])}],
            "outline": [{"$id": "default", "show": True, "lineColor": fill(c["ink_secondary"]), "weight": 1}],
        }},
        "advancedSlicerVisual": {"*": {
            "outline": [{"$id": "default", "show": True, "lineColor": fill(c["ink_secondary"]), "weight": 1},
                        {"$id": "selection:selected", "lineColor": fill(c["ink"])}],
            "value": [{"$id": "default", "fontFamily": body, "fontSize": body_pt, "fontColor": fill(c["ink"])},
                      {"$id": "selection:selected", "fontColor": fill(c["surface"])}],
        }},
        # FinalV3 build step 7: a data label that asks for a background (the end labels of the cumulative charts, doc 22
        # section 3) gets the card's white, opaque. Set here because Microsoft's CLI validator reads a fill named
        # backgroundColor inside a visual's labels as a misplaced "color" (PBIR_FORMATTING_PROP_NESTED); the shape itself
        # is the theme schema's (reportThemeSchema-2.159, visual-lineChart labels: backgroundColor, backgroundTransparency).
        "lineChart": {"*": {"labels": [{"backgroundColor": fill(c["surface"]), "backgroundTransparency": 0}]}},
        "page": {"*": {
            "background": [{"color": fill(c["canvas"]), "transparency": 0}],
            "outspace": [{"color": fill(c["canvas"]), "transparency": 0}],
        }},
    },
}

out = os.path.join(ROOT, "project", "deliverables", "theme.json")
with open(out, "w", encoding="utf-8", newline="\n") as f:   # UTF-8, no BOM (pbir-style)
    json.dump(theme, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"wrote {os.path.relpath(out, ROOT)} from kit {kit_name}")
