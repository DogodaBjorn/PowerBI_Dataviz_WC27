"""Writes the shared PillowKey semantic model (TMDL) for the three direction sketches.

Run from the repo root:  python project/tools/sketch_model.py
Output: project/pbip/PillowKey.SemanticModel

The 16 shipped tables keep the organisers' Power Query (DataFile parameter -> public
blob). Added on top: calculated columns on Hotels and InvestmentProjects, the
ProjectCashflow and HotelOutlook calculated tables (rules read from FinanceParameters /
FinanceAssumptions), four small helper tables and the _Measures table.
Every number is re-derived in the model; nothing is typed in from the mission.
"""
import json
import os
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODEL = ROOT / "project" / "pbip" / "PillowKey.SemanticModel"
NS = uuid.UUID("5d3c1d2e-7c4f-4d2a-9b1e-9a0f6f1e2c01")


def tag(name):
    return str(uuid.uuid5(NS, name))


def w(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------- shipped tables
# (name, [(column, type, hidden)], M typed-columns clause)
T = "type text"
N = "type number"
I = "Int64.Type"
D = "type date"

SHIPPED = {
    "Date": [("Date", D), ("Year", I), ("Quarter", T), ("MonthNumber", I), ("Month", T), ("YearMonth", T), ("Period", T)],
    "Region": [("Region", T)],
    "Scenario": [("Scenario", T), ("ScenarioOrder", I)],
    "Brands": [("Brand", T), ("Segment", T), ("Properties", I), ("Positioning", T), ("InvestmentBudgetUSD", I)],
    "Hotels": [("HotelID", T), ("HotelName", T), ("Brand", T), ("City", T), ("Country", T), ("Region", T), ("Latitude", N), ("Longitude", N), ("LocationType", T), ("Rooms", I), ("OpeningDate", D), ("LastRenovationDate", D)],
    "Renovations": [("RenovationID", T), ("HotelID", T), ("StartDate", D), ("EndDate", D), ("RenovationType", T), ("RoomsOutOfServicePct", N), ("CostUSD", I)],
    "MonthlyPerformance": [("HotelID", T), ("Month", D), ("RoomsAvailable", I), ("RoomsSold", I), ("RoomRevenue", I), ("FoodBeverageRevenue", I), ("OtherRevenue", I), ("TotalRevenue", I), ("StaffCost", I), ("EnergyCost", I), ("MaintenanceCost", I), ("FoodBeverageCost", I), ("OtherOperatingCost", I), ("TotalOperatingExpenses", I)],
    "GuestSegments": [("HotelID", T), ("Month", D), ("Segment", T), ("Bookings", I), ("RoomNights", I), ("RoomRevenue", I)],
    "BookingChannels": [("HotelID", T), ("Month", D), ("Channel", T), ("Bookings", I), ("RoomNights", I), ("RoomRevenue", I), ("DistributionCost", I)],
    "GuestExperience": [("HotelID", T), ("Month", D), ("SurveyResponses", I), ("OverallScore", N), ("CleanlinessScore", N), ("ServiceScore", N), ("RoomComfortScore", N), ("AmenitiesScore", N), ("ValueForMoneyScore", N), ("NetPromoterScore", N)],
    "GuestComplaints": [("HotelID", T), ("Month", D), ("Category", T), ("Complaints", I)],
    "InvestmentProjects": [("ProjectID", T), ("Brand", T), ("ProjectName", T), ("Category", T), ("Scope", T), ("GrowthInitiative", T), ("CapexUSD", I), ("EarliestStart", D), ("DurationMonths", I), ("RoomsOutOfServicePct", N), ("AddedRooms", I), ("AnnualRunningCostUSD", I), ("DependsOn", T), ("ExclusiveWith", T), ("Description", T)],
    "InvestmentProjectProperties": [("ProjectID", T), ("HotelID", T)],
    "InvestmentScenarios": [("ProjectID", T), ("Scenario", T), ("OccupancyChangePts", N), ("ADRChangePct", N), ("AddedRoomsOccupancy", N), ("FoodBeverageRevenueChangePct", N), ("OtherRevenueChangePct", N), ("OperatingExpenseChangePct", N), ("DistributionCostChangePts", N), ("SatisfactionChangePts", N), ("NewPropertyOccupancy", N), ("NewPropertyADR", N), ("AnnualRevenueImpactUSD", I), ("AnnualOperatingProfitImpactUSD", I)],
    "FinanceAssumptions": [("Year", I), ("Region", T), ("MarketDemandGrowthPct", N), ("ADRInflationPct", N), ("CostInflationPct", N)],
    "FinanceParameters": [("Parameter", T), ("Value", N), ("Unit", T), ("Notes", T)],
}
FACTS = {"MonthlyPerformance", "GuestSegments", "BookingChannels", "GuestExperience", "GuestComplaints", "Renovations", "InvestmentScenarios", "InvestmentProjectProperties"}
HIDDEN_KEYS = {"HotelID", "Month", "ProjectID"}
DOCS = {
    "Date": "Daily calendar 2021-2032 as shipped; Period separates Historical / Planning year / Investment horizon. Marked as the date table.",
    "MonthlyPerformance": "Grain: one row per hotel and month, 2021-01 to 2025-12. Revenue and opex components sum to the totals.",
    "BookingChannels": "Grain: one row per hotel, month and channel. Room revenue and nights reconcile to MonthlyPerformance; DistributionCost sits outside opex.",
    "GuestExperience": "Grain: one row per hotel and month. Scores are averages: every brand-level score is weighted by SurveyResponses in _Measures.",
    "GuestComplaints": "Grain: one row per hotel, month and complaint category.",
    "GuestSegments": "Grain: one row per hotel, month and guest segment.",
    "Renovations": "Grain: one renovation per row (1985-2023). Used for renovation spend per hotel only.",
    "Hotels": "Hotel dimension as shipped, plus refresh-age and capacity flags derived in the model.",
    "InvestmentProjects": "Project dimension as shipped, plus the recommended-plan grouping (Move) used by the plan builder.",
    "InvestmentScenarios": "Grain: one row per project and scenario (Low / Expected / High), organisers' annual impacts in 2025 dollars.",
    "InvestmentProjectProperties": "Bridge: which hotels each project touches. Related to both Hotels and InvestmentProjects.",
    "FinanceParameters": "The organisers' valuation rules (discount rate, ramp-up, horizon). Read by ProjectCashflow, never retyped.",
    "FinanceAssumptions": "Regional demand, ADR and cost inflation 2026-2032. Drives the do-nothing baseline in HotelOutlook.",
    "Brands": "Brand dimension with the investment budget per brand.",
    "Region": "Region dimension.",
    "Scenario": "Scenario dimension (disconnected): drives the Low / Expected / High toggle through TREATAS in the measures.",
}


def tmdl_type(t):
    return {T: "string", N: "double", I: "int64", D: "dateTime"}[t]


def col_block(table, name, t, hidden=False, extra=()):
    lines = [f"\tcolumn {q(name)}", f"\t\tdataType: {tmdl_type(t)}"]
    if hidden:
        lines.append("\t\tisHidden")
    if t == I:
        lines.append("\t\tformatString: 0")
    if t == D:
        lines.append("\t\tformatString: Short Date")
    lines.append(f"\t\tlineageTag: {tag(table + '.' + name)}")
    lines.append("\t\tsummarizeBy: none")
    lines.append(f"\t\tsourceColumn: {name}")
    for e in extra:
        lines.append("\t\t" + e)
    if t == D:
        lines.append("")
        lines.append("\t\tannotation UnderlyingDateTimeDataType = Date")
    return "\n".join(lines) + "\n"


def q(name):
    return f"'{name}'" if (" " in name or "-" in name or "%" in name) else name


def calc_col(table, name, dax, t, fmt=None, doc=None, extra=()):
    lines = []
    if doc:
        lines.append(f"\t/// {doc}")
    lines.append(f"\tcolumn {q(name)} = {dax}")
    lines.append(f"\t\tdataType: {t}")
    if fmt:
        lines.append(f"\t\tformatString: {fmt}")
    lines.append(f"\t\tlineageTag: {tag(table + '.' + name)}")
    lines.append("\t\tsummarizeBy: none")
    lines.append("\t\tisDataTypeInferred")
    for e in extra:
        lines.append("\t\t" + e)
    return "\n".join(lines) + "\n"


def m_partition(table, cols):
    typed = ", ".join(f'{{"{c}", {t}}}' for c, t in cols)
    return (
        f"\tpartition {table} = m\n"
        "\t\tmode: import\n"
        "\t\tsource =\n"
        "\t\t\t\tlet\n"
        "\t\t\t\t    Source = Excel.Workbook(Web.Contents(DataFile), null, true),\n"
        f"\t\t\t\t    Sheet = Source{{[Item=\"{table}\",Kind=\"Sheet\"]}}[Data],\n"
        "\t\t\t\t    Promoted = Table.PromoteHeaders(Sheet, [PromoteAllScalars=true]),\n"
        f"\t\t\t\t    Typed = Table.TransformColumnTypes(Promoted, {{{typed}}})\n"
        "\t\t\t\tin\n"
        "\t\t\t\t    Typed\n"
    )


def shipped_table(name, cols):
    out = []
    if name in DOCS:
        out.append(f"/// {DOCS[name]}")
    out.append(f"table {name}")
    out.append(f"\tlineageTag: {tag('table.' + name)}")
    if name == "Date":
        out.append("\tdataCategory: Time")
    out.append("")
    for c, t in cols:
        hidden = name in FACTS and c in HIDDEN_KEYS
        extra = []
        if name == "Date" and c == "Date":
            extra.append("isKey")
        if name == "Date" and c == "Month":
            extra.append("sortByColumn: MonthNumber")
        if name == "Scenario" and c == "Scenario":
            extra.append("sortByColumn: ScenarioOrder")
        out.append(col_block(name, c, t, hidden, extra))
    out.append(EXTRA_COLUMNS.get(name, ""))
    out.append(m_partition(name, cols))
    out.append("")
    out.append("\tannotation PBI_ResultType = Table")
    return "\n".join(out) + "\n"


# ---- decision data of the FinalV3 rebuild (docs 20 D2 / D4, 21 section 10.1): typed here ONCE, as decisions, not as
# source data. MOVE_FINDING: the Brand Review finding each Goodnight Inn move answers (D4: the kiosks answer F4, the
# queues at the 20 fullest desks; revenue management stays under F1). MOVE_GATE: the tranche of a move that waits for
# the 2028 gate (2 = the airport extensions, 3 = the refresh). Tranche 1 is not typed: it is package A, read from
# Package[Preset] in the MoveDecision table. MOVE_NAMES: the full names of R-P2-3 (the short ones stay in Short Name).
MOVE_NAMES = {"GI-01": "Booking app & member rates", "GI-10": "Revenue management", "GI-02": "Kiosks at the 20 busiest hotels",
              "GI-09": "Breakfast upgrade", "GI-05": "Gatwick +40 rooms", "GI-03": "Energy programme", "GI-04": "Toronto +40 rooms",
              "GI-06": "Kingston +40 rooms", "GI-08": "Boston new hotel", "GI-07": "Refresh, 10 oldest hotels"}
MOVE_FINDING = {"GI-01": "F2", "GI-02": "F4", "GI-03": "F1", "GI-04": "F4", "GI-05": "F4", "GI-06": "F4", "GI-07": "F3", "GI-08": "F4", "GI-09": "F3", "GI-10": "F1"}
MOVE_GATE = {"GI-04": 2, "GI-05": 2, "GI-07": 3}
FINDINGS = [("F2", "The middleman", 1), ("F1", "The margin", 2), ("F4", "Where we are full", 3), ("F3", "The fading welcome", 4)]  # code, name, ledger order (R-P2-5)
WAIT_OPTIONS = [("B", "B · Breakfast instead of kiosks", 1), ("T2", "Tranche 2 · Airport extensions, +80 rooms", 2),
                ("T3", "Tranche 3 · The refresh of the 10 oldest hotels (in package C)", 3)]  # key, title, sort (R-W-2)


HOTEL_COPY_NAMES = {"GI027": "Gatwick"}  # Goodnight Inn London Gatwick Airport


def _switch_hid(mapping, default):
    return "SWITCH ( Hotels[HotelID], " + ", ".join(f'"{k}", "{v}"' for k, v in sorted(mapping.items())) + f", {default} )"


def _switch_pid(mapping, default):
    return "SWITCH ( InvestmentProjects[ProjectID], " + ", ".join(f'"{k}", "{v}"' for k, v in sorted(mapping.items())) + f", {default} )"


# "a year on cost" of one project in the Expected case, from source columns only (no measure, no context transition:
# a calculated column that reads a measure would depend on every column of its table)
_YIELD_EXP = ('DIVIDE ( SUMX ( FILTER ( InvestmentScenarios, InvestmentScenarios[ProjectID] = {p} && InvestmentScenarios[Scenario] = "Expected" ), '
              "InvestmentScenarios[AnnualOperatingProfitImpactUSD] ), {c} )")

EXTRA_COLUMNS = {
    "Date": "".join([
        # round 7: the F4 hotel tooltip's month axis at 496 px: one letter per month (J F M A M J J A S O N D), sorted by month
        calc_col("Date", "Month Letter", "LEFT ( 'Date'[Month], 1 )", "string", doc="First letter of the month name, for narrow month axes (the F4 hotel tooltip).",
                 extra=("sortByColumn: MonthNumber",)),
    ]),
    "Hotels": "".join([
        calc_col("Hotels", "Hotel Short Name", 'TRIM(SUBSTITUTE(Hotels[HotelName], Hotels[Brand] & " ", ""))', "string",
                 doc="Hotel name without the brand prefix, for dense walls and tables."),
        # FinalV3 step 4: the name the copy uses for a hotel (F4 title and note, the gate rule, What waits): the city, except
        # where the city is not what the Brand Review calls the hotel (HOTEL_COPY_NAMES, label data)
        calc_col("Hotels", "Copy Name", _switch_hid(HOTEL_COPY_NAMES, "Hotels[City]"), "string",
                 doc="The hotel's name in running copy: its city, or the airport's name where the copy uses that (London Gatwick: Gatwick)."),
        calc_col("Hotels", "Years Since Refresh", "2025 - YEAR(COALESCE(Hotels[LastRenovationDate], Hotels[OpeningDate]))", "int64", "0",
                 doc="Years between the last refresh (or opening, for the never-renovated) and 2025."),
        calc_col("Hotels", "Refresh Age Band", 'SWITCH(TRUE(), Hotels[Years Since Refresh] <= 5, "0 to 5 y", Hotels[Years Since Refresh] <= 9, "6 to 9 y", "10 y or more")', "string",
                 doc="Refresh-age cohort used by the fading-welcome panel."),
        calc_col("Hotels", "Is Refresh Candidate", 'IF(CALCULATE(COUNTROWS(InvestmentProjectProperties), InvestmentProjectProperties[ProjectID] = "GI-07") > 0, "Yes", "No")', "string",
                 doc="Yes when the hotel is in the organisers' GI-07 room-refresh list."),
        # D1 briefing v2 (06-d1-briefing-opzet.md): the fading welcome on dated hotels only, as in 41_opzet_facts.py
        # (age_bands) and MISSION E10; the six never-renovated hotels stay out rather than borrow their opening date.
        calc_col("Hotels", "Renovation Age Sort",
                 "VAR y = 2025 - YEAR ( Hotels[LastRenovationDate] ) RETURN IF ( ISBLANK ( Hotels[LastRenovationDate] ), BLANK (), SWITCH ( TRUE (), y <= 5, 1, y <= 9, 2, 3 ) )",
                 "int64", "0", doc="1, 2 or 3 for 5 years or less, 6 to 9 and 10 or more years since the last renovation (2025); blank when never renovated."),
        calc_col("Hotels", "Renovation Age Label",
                 'VAR s = Hotels[Renovation Age Sort] VAR br = Hotels[Brand] '
                 # only the three columns it needs: ALLNOBLANKROW ( Hotels ) would depend on every column, including
                 # 'Is Refresh Candidate' (context transition), and close a circular dependency
                 'VAR n = COUNTROWS ( FILTER ( ALLNOBLANKROW ( Hotels[HotelID], Hotels[Brand], Hotels[Renovation Age Sort] ), Hotels[Brand] = br && Hotels[Renovation Age Sort] = s ) ) '
                 # one line per band at 1920: "10 years or more · / 10 hotels" wrapped on its separator (REVIEW m4)
                 # short enough for one line at 1920 (REVIEW m4); the band sizes moved into the F3 note
                 'RETURN IF ( ISBLANK ( s ) || n = 0, BLANK (), SWITCH ( s, 1, "5 years or less", 2, "6 to 9 years", "10 years or more" ) )',
                 "string", doc="Axis label of the fading-welcome chart: the age band and how many of the brand's hotels sit in it.",
                 extra=("sortByColumn: 'Renovation Age Sort'",)),
    ]),
    "InvestmentProjects": "".join([
        calc_col("InvestmentProjects", "Short Name",
                 'SWITCH(InvestmentProjects[ProjectID], "GI-01", "Booking app", "GI-02", "Kiosks at 20 desks", "GI-03", "Energy programme", "GI-04", "Toronto +40 rooms", "GI-05", "Gatwick +40 rooms", "GI-06", "Kingston +40 rooms", "GI-07", "Refresh 10 oldest", "GI-08", "Boston new hotel", "GI-09", "Breakfast upgrade", "GI-10", "Revenue management", InvestmentProjects[ProjectName])',
                 "string", doc="Short label for the plan builder and the departures board (Goodnight Inn projects only)."),
        calc_col("InvestmentProjects", "Move",
                 'SWITCH(InvestmentProjects[ProjectID], "GI-01", "Buy the guest back", "GI-10", "Buy the guest back", "GI-02", "Buy the guest back", "GI-07", "Fix the welcome", "GI-05", "Build where we are full", "GI-04", "Build where we are full", IF(InvestmentProjects[Brand] = "Goodnight Inn", "Not funded", "Other brand"))',
                 "string", doc="The recommended plan grouping from the mission (hypothesis A); the plan builder lets the Board overrule it."),
        calc_col("InvestmentProjects", "Move Sort",
                 'SWITCH(InvestmentProjects[Move], "Buy the guest back", 1, "Fix the welcome", 2, "Build where we are full", 3, "Not funded", 4, 9)',
                 "int64", "0"),
        calc_col("InvestmentProjects", "In Recommended Plan",
                 'IF(InvestmentProjects[Move] IN {"Buy the guest back", "Fix the welcome", "Build where we are full"}, "Yes", "No")',
                 "string", doc="Yes for the six projects of the recommended plan."),
        calc_col("InvestmentProjects", "Planned Start",
                 "VAR dep = InvestmentProjects[DependsOn] VAR own = InvestmentProjects[EarliestStart] RETURN IF ( dep = \"\", own, MAX ( own, EDATE ( LOOKUPVALUE ( InvestmentProjects[EarliestStart], InvestmentProjects[ProjectID], dep ), LOOKUPVALUE ( InvestmentProjects[DurationMonths], InvestmentProjects[ProjectID], dep ) ) ) )",
                 "dateTime", "Short Date",
                 doc="Earliest start, or the month the prerequisite (DependsOn) goes live if that is later: GI-02 kiosks start when the GI-01 app is live."),
        calc_col("InvestmentProjects", "Completion Date", "EDATE(InvestmentProjects[Planned Start], InvestmentProjects[DurationMonths])", "dateTime", "Short Date",
                 doc="Planned start plus duration: the month the project goes live."),
        calc_col("InvestmentProjects", "Answers Finding", _switch_pid(MOVE_FINDING, "BLANK ()"),
                 "string", doc="Decision data, not source data: the Brand Review finding (F1 to F4 on page 1) the initiative answers; Goodnight Inn projects only. "
                               "One mapping with MoveDecision[Finding] (doc 20 D4, 13 Nov: the kiosks answer F4)."),
        # FinalV3 (doc 21 section 10.1): one naming source for the hero table. Sorted by Hero Sort, so a table on Move
        # Name lists the moves by their Expected "a year on cost" in every scenario, with no sort set in the visual.
        calc_col("InvestmentProjects", "Hero Sort",
                 "VAR myp = InvestmentProjects[ProjectID] VAR myc = InvestmentProjects[CapexUSD] VAR myb = InvestmentProjects[Brand] "
                 'VAR gi = FILTER ( ALL ( InvestmentProjects[ProjectID], InvestmentProjects[CapexUSD], InvestmentProjects[Brand] ), InvestmentProjects[Brand] = "Goodnight Inn" ) '
                 "VAR me = " + _YIELD_EXP.format(p="myp", c="myc") + " "
                 'RETURN IF ( myb = "Goodnight Inn", COUNTROWS ( FILTER ( gi, VAR p = InvestmentProjects[ProjectID] VAR c = InvestmentProjects[CapexUSD] RETURN '
                 + _YIELD_EXP.format(p="p", c="c") + " > me ) ) + 1, 99 )",
                 "int64", "0", doc="Rank of the move by its Expected 'a year on cost' (profit a year by 2032 over capex) within Goodnight Inn, 1 = highest; fixed at refresh, so the hero table's order never follows the scenario. 99 for other brands."),
        calc_col("InvestmentProjects", "Move Name", _switch_pid(MOVE_NAMES, "InvestmentProjects[ProjectName]"),
                 "string", doc="The move's full name as the Investment Strategy page says it (R-P2-3); the organisers' project name for other brands. Sorted by Hero Sort.",
                 extra=("sortByColumn: 'Hero Sort'",)),
    ]),
}

# ---------------------------------------------------------------- calculated tables

PROJECT_CASHFLOW = r"""
VAR RampY1 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - first year after completion" )
VAR RampY2 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - second year after completion" )
VAR RampY3 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - third year onwards" )
VAR FirstYear = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Earliest investment date" )
VAR LastYear = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Impact horizon" )
VAR Rate = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Discount rate" )
VAR Origin = DATE ( FirstYear, 1, 1 )
VAR Horizon =
    FILTER ( ALLNOBLANKROW ( 'Date'[Date] ), YEAR ( 'Date'[Date] ) >= FirstYear && YEAR ( 'Date'[Date] ) <= LastYear && DAY ( 'Date'[Date] ) = 1 )
VAR Hotel25 =
    ADDCOLUMNS (
        SELECTCOLUMNS ( ALLNOBLANKROW ( Hotels[HotelID] ), "@Hid", Hotels[HotelID] ),
        "@Brand", LOOKUPVALUE ( Hotels[Brand], Hotels[HotelID], [@Hid] ),
        "@Rev25", VAR vHid = [@Hid] RETURN SUMX ( FILTER ( MonthlyPerformance, MonthlyPerformance[HotelID] = vHid && YEAR ( MonthlyPerformance[Month] ) = 2025 ), MonthlyPerformance[TotalRevenue] )
    )
RETURN
    SELECTCOLUMNS (
        GENERATE (
            InvestmentScenarios,
            VAR vPid = InvestmentScenarios[ProjectID]
            VAR vStart = LOOKUPVALUE ( InvestmentProjects[Planned Start], InvestmentProjects[ProjectID], vPid )
            VAR vDur = LOOKUPVALUE ( InvestmentProjects[DurationMonths], InvestmentProjects[ProjectID], vPid )
            VAR vCapex = LOOKUPVALUE ( InvestmentProjects[CapexUSD], InvestmentProjects[ProjectID], vPid )
            VAR vOos = LOOKUPVALUE ( InvestmentProjects[RoomsOutOfServicePct], InvestmentProjects[ProjectID], vPid )
            VAR vScope = LOOKUPVALUE ( InvestmentProjects[Scope], InvestmentProjects[ProjectID], vPid )
            VAR vBrand = LOOKUPVALUE ( InvestmentProjects[Brand], InvestmentProjects[ProjectID], vPid )
            VAR vDone = EDATE ( vStart, vDur )
            VAR vMappedRev =
                IF (
                    vScope = "Brand-wide",
                    SUMX ( FILTER ( Hotel25, [@Brand] = vBrand ), [@Rev25] ),
                    SUMX ( FILTER ( InvestmentProjectProperties, InvestmentProjectProperties[ProjectID] = vPid ), VAR vHid = InvestmentProjectProperties[HotelID] RETURN MAXX ( FILTER ( Hotel25, [@Hid] = vHid ), [@Rev25] ) )
                )
            VAR vOP = InvestmentScenarios[AnnualOperatingProfitImpactUSD]
            VAR vRev = InvestmentScenarios[AnnualRevenueImpactUSD]
            RETURN
                ADDCOLUMNS (
                    Horizon,
                    "@Capex", IF ( 'Date'[Date] >= vStart && 'Date'[Date] < vDone, DIVIDE ( vCapex, vDur ), 0 ),
                    "@Disruption", IF ( 'Date'[Date] >= vStart && 'Date'[Date] < vDone, vOos * vMappedRev / 12, 0 ),
                    "@Benefit",
                        VAR vM = DATEDIFF ( vDone, 'Date'[Date], MONTH )
                        RETURN IF ( 'Date'[Date] >= vDone, vOP / 12 * SWITCH ( TRUE (), vM < 12, RampY1, vM < 24, RampY2, RampY3 ), 0 ),
                    "@RevenueBenefit",
                        VAR vM = DATEDIFF ( vDone, 'Date'[Date], MONTH )
                        RETURN IF ( 'Date'[Date] >= vDone, vRev / 12 * SWITCH ( TRUE (), vM < 12, RampY1, vM < 24, RampY2, RampY3 ), 0 ),
                    "@Df", DIVIDE ( 1, POWER ( 1 + Rate, DATEDIFF ( Origin, 'Date'[Date], MONTH ) / 12 ) )
                )
        ),
        "ProjectID", InvestmentScenarios[ProjectID],
        "Scenario", InvestmentScenarios[Scenario],
        "Month", 'Date'[Date],
        "Capex", [@Capex],
        "Disruption", [@Disruption],
        "Benefit", [@Benefit],
        "RevenueBenefit", [@RevenueBenefit],
        "DiscountFactor", [@Df]
    )
"""

HOTEL_OUTLOOK = r"""
VAR Cap = 0.97
VAR Base =
    ADDCOLUMNS (
        SELECTCOLUMNS ( ALLNOBLANKROW ( Hotels[HotelID] ), "@Hid", Hotels[HotelID] ),
        "@Region", LOOKUPVALUE ( Hotels[Region], Hotels[HotelID], [@Hid] ),
        "@Avail", VAR vHid = [@Hid] RETURN SUMX ( FILTER ( MonthlyPerformance, MonthlyPerformance[HotelID] = vHid && YEAR ( MonthlyPerformance[Month] ) = 2025 ), MonthlyPerformance[RoomsAvailable] ),
        "@Sold", VAR vHid = [@Hid] RETURN SUMX ( FILTER ( MonthlyPerformance, MonthlyPerformance[HotelID] = vHid && YEAR ( MonthlyPerformance[Month] ) = 2025 ), MonthlyPerformance[RoomsSold] ),
        "@Rev", VAR vHid = [@Hid] RETURN SUMX ( FILTER ( MonthlyPerformance, MonthlyPerformance[HotelID] = vHid && YEAR ( MonthlyPerformance[Month] ) = 2025 ), MonthlyPerformance[TotalRevenue] ),
        "@Opex", VAR vHid = [@Hid] RETURN SUMX ( FILTER ( MonthlyPerformance, MonthlyPerformance[HotelID] = vHid && YEAR ( MonthlyPerformance[Month] ) = 2025 ), MonthlyPerformance[TotalOperatingExpenses] )
    )
VAR Years = SELECTCOLUMNS ( GENERATESERIES ( 2025, 2032, 1 ), "@Yr", [Value] )
RETURN
    SELECTCOLUMNS (
        FILTER (
            GENERATE (
                Base,
                VAR vReg = [@Region]
                VAR vT =
                    ADDCOLUMNS (
                        Years,
                        "@Dem", COALESCE ( PRODUCTX ( FILTER ( FinanceAssumptions, FinanceAssumptions[Region] = vReg && FinanceAssumptions[Year] >= 2026 && FinanceAssumptions[Year] <= [@Yr] ), 1 + FinanceAssumptions[MarketDemandGrowthPct] ), 1 ),
                        "@Adr", COALESCE ( PRODUCTX ( FILTER ( FinanceAssumptions, FinanceAssumptions[Region] = vReg && FinanceAssumptions[Year] >= 2026 && FinanceAssumptions[Year] <= [@Yr] ), 1 + FinanceAssumptions[ADRInflationPct] ), 1 ),
                        "@Cost", COALESCE ( PRODUCTX ( FILTER ( FinanceAssumptions, FinanceAssumptions[Region] = vReg && FinanceAssumptions[Year] >= 2026 && FinanceAssumptions[Year] <= [@Yr] ), 1 + FinanceAssumptions[CostInflationPct] ), 1 )
                    )
                VAR vFc = MINX ( FILTER ( vT, [@Sold] * [@Dem] > [@Avail] * Cap ), [@Yr] )
                RETURN
                    ADDCOLUMNS ( vT, "@FirstCapped", vFc )
            ),
            [@Sold] > 0
        ),
        "HotelID", [@Hid],
        "Year", [@Yr],
        "RoomsAvailable", [@Avail],
        "DemandRoomNights", [@Sold] * [@Dem],
        "RoomsSold", MIN ( [@Sold] * [@Dem], [@Avail] * Cap ),
        "Revenue", MIN ( [@Sold] * [@Dem], [@Avail] * Cap ) * DIVIDE ( [@Rev], [@Sold] ) * [@Adr],
        "Opex", MIN ( [@Sold] * [@Dem], [@Avail] * Cap ) * DIVIDE ( [@Opex], [@Sold] ) * [@Cost],
        "FirstCappedYear", [@FirstCapped],
        "CappedBy2032", IF ( ISBLANK ( [@FirstCapped] ), "No", "Yes" )
    )
"""


def calc_table(name, doc, columns, dax):
    """columns: list of (name, type, format or None)."""
    out = [f"/// {doc}", f"table {name}", f"\tlineageTag: {tag('table.' + name)}", ""]
    for c, t, fmt in columns:
        out.append(f"\tcolumn {q(c)}")
        out.append(f"\t\tdataType: {t}")
        if fmt:
            out.append(f"\t\tformatString: {fmt}")
        out.append(f"\t\tlineageTag: {tag(name + '.' + c)}")
        out.append("\t\tsummarizeBy: none")
        out.append("\t\tisNameInferred")
        out.append("\t\tisDataTypeInferred")
        out.append(f"\t\tsourceColumn: [{c}]")
        out.append("")
    out.append(f"\tpartition {name} = calculated")
    out.append("\t\tmode: import")
    out.append("\t\tsource = ```")
    for line in dax.strip("\n").splitlines():
        out.append("\t\t\t\t" + line if line.strip() else "")
    out.append("\t\t\t\t```")
    out.append("")
    out.append("\tannotation PBI_ResultType = Table")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- measures
MEASURES = []  # (name, dax, format, folder, doc)


FMT_DEFS = {}  # measure name -> DAX of its dynamic format string (formatStringDefinition), doc 21 P-1


def m(name, dax, fmt, folder, doc, fmt_def=None):
    # Desktop refuses the whole project on a duplicate ("TMDL objects cannot be merged", 7 Nov); the validators did not
    assert all(x[0] != name for x in MEASURES), f"duplicate measure name: {name}"
    MEASURES.append((name, dax, fmt, folder, doc))
    if fmt_def:
        FMT_DEFS[name] = fmt_def


def label_safe(name, value_expr, text_expr, folder, doc):
    """P-1 (doc 21): a number for a native data label. The measure keeps its numeric value for the bar or the line;
    its dynamic format string returns the finished text as a quoted literal, so Power BI prints that text and applies
    no locale (a nl-NL Desktop printed "+6,8"). Spike S-1 (13 Nov): the literal goes in all three sections (positive;
    negative; zero), or a negative value gets a second minus ("−−4.9"). Use only where the value axis is hidden or
    where another series comes first: an axis would repeat the literal on every tick. The measure carries NO static
    formatString: the engine refuses a measure that has both ("zowel de eigenschap FormatString als de eigenschap
    FormatStringDefinition", 13 Nov), so scripts/validate_tmdl.py --strict reports one "no formatString" warning per
    label-safe measure; those warnings are expected."""
    m(name, value_expr, None, folder, doc,
      fmt_def=f'VAR __t = {text_expr} RETURN """" & __t & """;""" & __t & """;""" & __t & """"')


def yr(measure, y):
    return f"CALCULATE ( [{measure}], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y} )"


USD = r"\$#,0;(\$#,0)"
USDM = r"\$#,0,,.0\ \M;-\$#,0,,.0\ \M"
PCT = "0.0%"
TXT = '@'
C1 = "01 Core"
C2 = "02 Channels"
C3 = "03 Guest"
C4 = "04 Plan builder"
C5 = "05 Impact"
C6 = "06 Outlook (scenario logic)"
C7 = "07 Display"

m("Rooms Available", "SUM ( MonthlyPerformance[RoomsAvailable] )", "#,0", C1, "Room nights on offer in the period.")
m("Rooms Sold", "SUM ( MonthlyPerformance[RoomsSold] )", "#,0", C1, "Room nights sold in the period.")
m("Occupancy %", "DIVIDE ( [Rooms Sold], [Rooms Available] )", PCT, C1, "Rooms sold over rooms available.")
m("Room Revenue", "SUM ( MonthlyPerformance[RoomRevenue] )", USD, C1, "Room revenue from MonthlyPerformance.")
m("Total Revenue", "SUM ( MonthlyPerformance[TotalRevenue] )", USDM, C1, "Room, food and beverage and other revenue.")
m("ADR", "DIVIDE ( [Room Revenue], [Rooms Sold] )", r"\$#,0.00", C1, "Average daily rate: room revenue per room night sold.")
m("RevPAR", "DIVIDE ( [Room Revenue], [Rooms Available] )", r"\$#,0.00", C1, "Room revenue per available room night.")
m("Operating Expenses", "SUM ( MonthlyPerformance[TotalOperatingExpenses] )", USD, C1, "Total operating expenses; excludes distribution cost (workbook convention).")
m("GOP", "[Total Revenue] - [Operating Expenses]", USDM, C1, "Gross operating profit before distribution cost.")
m("GOP Margin %", "DIVIDE ( [GOP], [Total Revenue] )", PCT, C1, "GOP as a share of total revenue.")
m("Revenue per Occupied Room", "DIVIDE ( [Total Revenue], [Rooms Sold] )", r"\$#,0.00", C1, "Total revenue per room night sold.")
m("Cost per Occupied Room", "DIVIDE ( [Operating Expenses], [Rooms Sold] )", r"\$#,0.00", C1, "Operating expenses per room night sold.")
m("RevPOR Index (2023 = 100)", "DIVIDE ( [Revenue per Occupied Room], " + yr("Revenue per Occupied Room", 2023) + " ) * 100", "0.0", C1, "Revenue per occupied room indexed to 2023 (2021 is a depressed base year).")
m("CPOR Index (2023 = 100)", "DIVIDE ( [Cost per Occupied Room], " + yr("Cost per Occupied Room", 2023) + " ) * 100", "0.0", C1, "Cost per occupied room indexed to 2023.")
m("Hotel Rooms", "SUM ( Hotels[Rooms] )", "#,0", C1, "Rooms in the hotels in context.")
m("Hotels in Context", "DISTINCTCOUNT ( Hotels[HotelID] )", "#,0", C1, "Number of hotels in context.")
m("Refresh Age", "MAX ( Hotels[Years Since Refresh] )", "0", C1, "Years since the last refresh for the hotel in context (scatter axis).")
m("Renovation Spend per Hotel since 2018", "DIVIDE ( CALCULATE ( SUM ( Renovations[CostUSD] ), Renovations[StartDate] >= DATE ( 2018, 1, 1 ) ), [Hotels in Context] )", USDM, C1, "Renovation capex since 2018 divided by the hotels in context.")

m("Channel Room Revenue", "SUM ( BookingChannels[RoomRevenue] )", USD, C2, "Room revenue by booking channel (reconciles to MonthlyPerformance).")
m("Channel Room Nights", "SUM ( BookingChannels[RoomNights] )", "#,0", C2, "Room nights by booking channel.")
m("Distribution Cost", "SUM ( BookingChannels[DistributionCost] )", USDM, C2, "Commissions and fees paid to booking channels; outside operating expenses.")
m("Distribution Cost % of Room Revenue", "DIVIDE ( [Distribution Cost], [Channel Room Revenue] )", PCT, C2, "Distribution cost as a share of room revenue.")
m("Channel Share %", "DIVIDE ( [Channel Room Revenue], CALCULATE ( [Channel Room Revenue], ALL ( BookingChannels[Channel] ) ) )", PCT, C2, "A channel's share of room revenue in context.")
m("OTA Share %", 'CALCULATE ( [Channel Share %], BookingChannels[Channel] = "Online Travel Agencies" )', PCT, C2, "Share of room revenue booked through online travel agencies.")
m("Direct Share %", 'CALCULATE ( [Channel Share %], BookingChannels[Channel] IN { "Direct Website & App", "Direct Phone & Walk-in" } )', PCT, C2, "Share of room revenue booked directly (web, app, phone, walk-in).")
m("GOP after Distribution", "[GOP] - [Distribution Cost]", USD, C2, "GOP after commissions and channel fees.")
m("GOP Margin after Distribution %", "DIVIDE ( [GOP after Distribution], [Total Revenue] )", PCT, C2, "Margin after distribution cost; the like-for-like benchmark across brands.")
m("Distribution Cost at 2021 Mix",
  "SUMX ( VALUES ( BookingChannels[Channel] ), VAR share21 = CALCULATE ( [Channel Share %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2021 ) VAR rate = [Distribution Cost % of Room Revenue] VAR total = CALCULATE ( [Channel Room Revenue], ALL ( BookingChannels[Channel] ) ) RETURN share21 * total * rate )",
  USD, C2, "Counterfactual, labeled as such: this period's room revenue at the 2021 channel mix, at each channel's current cost rate.")
m("Distribution Cost above 2021 Mix", "[Distribution Cost] - [Distribution Cost at 2021 Mix]", USDM, C2, "What the channel drift since 2021 costs per period (counterfactual).")

m("Survey Responses", "SUM ( GuestExperience[SurveyResponses] )", "#,0", C3, "Guest survey responses.")
m("NPS (weighted)", "DIVIDE ( SUMX ( GuestExperience, GuestExperience[NetPromoterScore] * GuestExperience[SurveyResponses] ), [Survey Responses] )", "+0.0;-0.0;0.0", C3, "Net promoter score weighted by survey responses (an unweighted average is a contract violation).")
m("Overall Score (weighted)", "DIVIDE ( SUMX ( GuestExperience, GuestExperience[OverallScore] * GuestExperience[SurveyResponses] ), [Survey Responses] )", "0.00", C3, "Overall guest score weighted by responses.")
m("Room Comfort (weighted)", "DIVIDE ( SUMX ( GuestExperience, GuestExperience[RoomComfortScore] * GuestExperience[SurveyResponses] ), [Survey Responses] )", "0.00", C3, "Room comfort score weighted by responses.")
m("Complaints", "SUM ( GuestComplaints[Complaints] )", "#,0", C3, "Complaints logged.")
m("Complaints per 1k Room Nights", "DIVIDE ( [Complaints], [Rooms Sold] ) * 1000", "0.00", C3, "Complaints normalised per thousand room nights sold.")

for base, yrs in {
    "Occupancy %": (2024, 2025), "RevPAR": (2024, 2025), "ADR": (2025,), "GOP Margin %": (2023, 2024, 2025),
    "GOP Margin after Distribution %": (2025,), "NPS (weighted)": (2021, 2025), "Room Comfort (weighted)": (2025,),
    "Complaints per 1k Room Nights": (2025,), "OTA Share %": (2025,), "Direct Share %": (2025,), "Distribution Cost": (2025,),
    "Distribution Cost % of Room Revenue": (2021, 2025), "Distribution Cost at 2021 Mix": (2025,), "Distribution Cost above 2021 Mix": (2025,),
    "Rooms Sold": (2025,), "Total Revenue": (2025,), "GOP": (2025,), "Revenue per Occupied Room": (2025,),
}.items():
    fmt = next(x[2] for x in MEASURES if x[0] == base)
    folder = next(x[3] for x in MEASURES if x[0] == base)
    for y in yrs:
        m(f"{base} {y}", yr(base, y), fmt, folder, f"{base} fixed to calendar {y}, ignoring the page's date context.")

m("Hotel Status 2025", 'VAR occ = [Occupancy % 2025] VAR nps = [NPS (weighted) 2025] RETURN SWITCH ( TRUE (), occ >= 0.85, "Full", nps < 0, "Tired", occ < 0.65, "Weak", "Fine" )', TXT, C3, "Full (85 percent or more), Tired (negative NPS), Weak (under 65 percent), else Fine; 2025.")

m("Budget", "SUM ( Brands[InvestmentBudgetUSD] )", USDM, C4, "Investment budget of the brand in context.")
m("Capex Selected", "SUM ( InvestmentProjects[CapexUSD] )", USDM, C4, "Capex of the projects currently selected in the plan builder.")
m("Budget Used %", "DIVIDE ( [Capex Selected], [Budget] )", PCT, C4, "Selected capex over the brand budget.")
m("Budget Remaining", "[Budget] - [Capex Selected]", USDM, C4, "Budget left after the selection.")
m("Projects Selected", "COUNTROWS ( InvestmentProjects )", "0", C4, "Projects in the selection.")
m("Growth Initiatives Selected", 'CALCULATE ( COUNTROWS ( InvestmentProjects ), InvestmentProjects[GrowthInitiative] = "Yes" )', "0", C4, "Selected projects flagged as growth initiatives by the organisers.")
m("Plan Valid (text)",
  'VAR n = [Projects Selected] VAR g = [Growth Initiatives Selected] VAR over = [Capex Selected] > [Budget] VAR kiosk = CALCULATE ( COUNTROWS ( InvestmentProjects ), InvestmentProjects[ProjectID] = "GI-02" ) > 0 VAR app = CALCULATE ( COUNTROWS ( InvestmentProjects ), InvestmentProjects[ProjectID] = "GI-01" ) > 0 VAR issues = IF ( n < 3, "fewer than 3 projects; ", "" ) & IF ( g < 1, "no growth initiative; ", "" ) & IF ( over, "over budget; ", "" ) & IF ( kiosk && NOT app, "kiosks need the booking app; ", "" ) RETURN IF ( issues = "", "Plan valid: " & n & " projects, " & g & " growth, within budget, dependencies met", "Not yet valid: " & issues )',
  TXT, C4, "Contest constraints as a lamp: at least 3 projects, at least 1 growth initiative, within budget, GI-02 needs GI-01.")
m("Rooms Added", "SUM ( InvestmentProjects[AddedRooms] )", "#,0", C4, "Rooms added by the selected projects.")
m("Rooms Refreshed", 'CALCULATE ( SUM ( Hotels[Rooms] ), CROSSFILTER ( InvestmentProjectProperties[HotelID], Hotels[HotelID], BOTH ), InvestmentProjects[Category] = "Renovation" )', "#,0", C4, "Rooms in the hotels touched by selected renovation projects.")
m("Kiosk Desks", 'CALCULATE ( COUNTROWS ( InvestmentProjectProperties ), InvestmentProjects[ProjectID] = "GI-02" )', "#,0", C4, "Hotels receiving self check-in kiosks when GI-02 is selected.")
m("Disruption Months", "MAXX ( FILTER ( InvestmentProjects, InvestmentProjects[RoomsOutOfServicePct] > 0 ), InvestmentProjects[DurationMonths] )", "0", C4, "Longest works period with rooms out of service in the selection.")
m("Start (text)", 'FORMAT ( MIN ( InvestmentProjects[EarliestStart] ), "mmm yyyy" )', TXT, C4, "Earliest start of the project in context.")
m("Live (text)", 'FORMAT ( MIN ( InvestmentProjects[Completion Date] ), "mmm yyyy" )', TXT, C4, "Go-live month of the project in context.")
m("Hotels Touched", "DISTINCTCOUNT ( InvestmentProjectProperties[HotelID] )", "#,0", C4, "Hotels mapped to the project in context.")
m("Selected Scenario", 'SELECTEDVALUE ( Scenario[Scenario], "Expected" )', TXT, C4, "Scenario chosen in the toggle; Expected when nothing is selected.")

def cf(col, scn=None):
    s = f'"{scn}"' if scn else "[Selected Scenario]"
    return f"VAR s = {s} RETURN CALCULATE ( SUM ( ProjectCashflow[{col}] ), ProjectCashflow[Scenario] = s )"

m("Capex Phased", cf("Capex"), USDM, C5, "Capex spread evenly over each project's duration (FinanceParameters rule).")
m("Disruption", cf("Disruption"), USDM, C5, "Revenue lost from rooms out of service during works, no cost relief (conservative).")
m("Benefit (ramped)", cf("Benefit"), USDM, C5, "Annual operating-profit impact per month after go-live, ramped 50 / 85 / 100 percent per FinanceParameters.")
for scn in ("Low", "High"):
    m(f"Benefit (ramped, {scn})", cf("Benefit", scn), USDM, C5, f"Benefit at the {scn} scenario regardless of the toggle.")
m("Net Impact", "[Benefit (ramped)] - [Capex Phased] - [Disruption]", USDM, C5, "Benefit minus capex minus disruption, in 2025 dollars.")
m("OP Impact", "[Benefit (ramped)] - [Disruption]", USDM, C5, "Operating-profit effect only (capex is cash, not profit).")
for scn in ("Low", "High"):
    m(f"OP Impact ({scn})", f"[Benefit (ramped, {scn})] - [Disruption]", USDM, C5, f"Operating-profit effect at the {scn} scenario.")
    m(f"Net Impact ({scn})", f'VAR s = "{scn}" RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), ProjectCashflow[Scenario] = s )', USDM, C5, f"Net impact at the {scn} scenario.")
m("Cumulative Net Impact", "VAR d = MAX ( 'Date'[Date] ) RETURN CALCULATE ( [Net Impact], REMOVEFILTERS ( 'Date' ), 'Date'[Date] <= d )", USDM, C5, "Net impact accumulated from January 2027 to the end of the period in context.")
for scn in ("Low", "High"):
    m(f"Cumulative Net Impact ({scn})", f"VAR d = MAX ( 'Date'[Date] ) RETURN CALCULATE ( [Net Impact ({scn})], REMOVEFILTERS ( 'Date' ), 'Date'[Date] <= d )", USDM, C5, f"Cumulative net impact at the {scn} scenario.")
m("2032 Run-rate", "VAR s = [Selected Scenario] RETURN CALCULATE ( SUM ( InvestmentScenarios[AnnualOperatingProfitImpactUSD] ), InvestmentScenarios[Scenario] = s )", USDM, C5, "Full annual operating-profit impact of the selection once ramped (every project is at 100 percent by 2032).")
for scn in ("Low", "High"):
    m(f"2032 Run-rate ({scn})", f'CALCULATE ( SUM ( InvestmentScenarios[AnnualOperatingProfitImpactUSD] ), InvestmentScenarios[Scenario] = "{scn}" )', USDM, C5, f"Run-rate at the {scn} scenario.")
m("Run-rate % of 2025 GOP", "DIVIDE ( [2032 Run-rate], [GOP 2025] )", PCT, C5, "Run-rate relative to 2025 gross operating profit.")
m("NPV @ 8%", "VAR s = [Selected Scenario] RETURN CALCULATE ( SUMX ( FILTER ( ProjectCashflow, ProjectCashflow[Scenario] = s ), ( ProjectCashflow[Benefit] - ProjectCashflow[Capex] - ProjectCashflow[Disruption] ) * ProjectCashflow[DiscountFactor] ), REMOVEFILTERS ( 'Date' ) )", USDM, C5,
  "Net impact through 2032 discounted monthly at the FinanceParameters rate to January 2027 (the close of the 2026 planning year), no terminal value (convention of 04-p2-build-method.md).")
m("Payback Year", "VAR t = ADDCOLUMNS ( FILTER ( ALL ( 'Date'[Year] ), 'Date'[Year] >= 2027 ), \"@cum\", VAR y = 'Date'[Year] RETURN CALCULATE ( [Net Impact], REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y ) ) RETURN MINX ( FILTER ( t, [@cum] >= 0 ), 'Date'[Year] )", "0", C5, "First year the cumulative net impact turns positive; blank when after 2032.")
m("Payback (text)", 'IF ( ISBLANK ( [Payback Year] ), "after 2032", FORMAT ( [Payback Year], "0" ) )', TXT, C5, "Payback year as text, with the horizon trap spelled out.")

m("Baseline Rooms Available", "SUM ( HotelOutlook[RoomsAvailable] )", "#,0", C6, "Rooms available in the do-nothing projection (2025 capacity held).")
m("Baseline Demand Room Nights", "SUM ( HotelOutlook[DemandRoomNights] )", "#,0", C6, "Room nights the market would fill, 2025 sold nights grown by regional demand (scenario logic).")
m("Baseline Rooms Sold", "SUM ( HotelOutlook[RoomsSold] )", "#,0", C6, "Demand capped at 97 percent occupancy (scenario logic).")
m("Baseline Occupancy %", "DIVIDE ( [Baseline Rooms Sold], [Baseline Rooms Available] )", PCT, C6, "Do-nothing occupancy (scenario logic).")
m("Baseline Demand Occupancy %", "DIVIDE ( [Baseline Demand Room Nights], [Baseline Rooms Available] )", PCT, C6, "Uncapped demand over available rooms; above 97 percent means rooms are turned away.")
m("Capacity Cap %", "0.97", PCT, C6, "The occupancy ceiling used by the baseline (highest observed).")
m("Unmet Room Nights", "[Baseline Demand Room Nights] - [Baseline Rooms Sold]", "#,0", C6, "Demand turned away by the capacity cap.")
m("Baseline Revenue", "SUM ( HotelOutlook[Revenue] )", USDM, C6, "Do-nothing revenue: 2025 revenue per occupied room grown by ADR inflation (scenario logic).")
m("Baseline Opex", "SUM ( HotelOutlook[Opex] )", USDM, C6, "Do-nothing opex: 2025 cost per occupied room grown by cost inflation (scenario logic).")
m("Baseline GOP", "[Baseline Revenue] - [Baseline Opex]", USDM, C6, "Do-nothing gross operating profit (scenario logic).")
m("Baseline GOP Margin %", "DIVIDE ( [Baseline GOP], [Baseline Revenue] )", PCT, C6, "Do-nothing margin (scenario logic).")
m("First Capped Year", "MIN ( HotelOutlook[FirstCappedYear] )", "0", C6, "First year the hotel in context runs out of rooms (scenario logic).")
m("Margin Actual (timeline)", "CALCULATE ( [GOP Margin %], TREATAS ( VALUES ( Timeline[Year] ), 'Date'[Year] ) )", PCT, C6, "Actual GOP margin on the 2021-2032 timeline axis (blank after 2025).")
m("Margin Baseline (timeline)", "CALCULATE ( [Baseline GOP Margin %], TREATAS ( VALUES ( Timeline[Year] ), HotelOutlook[Year] ) )", PCT, C6, "Do-nothing margin on the timeline axis, 2025 onward (scenario logic).")
m("GOP Baseline (timeline)", "CALCULATE ( [Baseline GOP], TREATAS ( VALUES ( Timeline[Year] ), HotelOutlook[Year] ) )", USDM, C6, "Do-nothing GOP on the timeline axis (scenario logic).")
m("GOP Plan (timeline)", "[GOP Baseline (timeline)] + CALCULATE ( [OP Impact], TREATAS ( VALUES ( Timeline[Year] ), 'Date'[Year] ) )", USDM, C6, "Baseline GOP plus the selected plan's operating-profit effect (scenario logic).")
for scn in ("Low", "High"):
    m(f"GOP Plan (timeline, {scn})", f"[GOP Baseline (timeline)] + CALCULATE ( [OP Impact ({scn})], TREATAS ( VALUES ( Timeline[Year] ), 'Date'[Year] ) )", USDM, C6, f"Plan GOP at the {scn} scenario.")

m("Bridge Value",
  "VAR s = SELECTEDVALUE ( BridgeStep[Step] ) "
  "VAR sold24 = [Rooms Sold] - 0 + " + yr("Rooms Sold", 2024) + " - [Rooms Sold] "
  "VAR sold25 = " + yr("Rooms Sold", 2025) + " "
  "VAR rev24 = " + yr("Total Revenue", 2024) + " VAR rev25 = " + yr("Total Revenue", 2025) + " "
  "VAR volume = ( sold25 - sold24 ) * DIVIDE ( rev24, sold24 ) "
  "VAR rate = rev25 - rev24 - volume "
  "VAR d = ( c ) => 0 "
  "RETURN 0",
  USD, C7, "placeholder")
MEASURES.pop()  # replaced below with the readable version


def costdelta(col):
    return f"- ( CALCULATE ( SUM ( MonthlyPerformance[{col}] ), REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ) - CALCULATE ( SUM ( MonthlyPerformance[{col}] ), REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2024 ) )"


m("Bridge Value",
  "VAR s = SELECTEDVALUE ( BridgeStep[Step] ) "
  f"VAR sold24 = {yr('Rooms Sold', 2024)} VAR sold25 = {yr('Rooms Sold', 2025)} "
  f"VAR rev24 = {yr('Total Revenue', 2024)} VAR rev25 = {yr('Total Revenue', 2025)} "
  "VAR volume = ( sold25 - sold24 ) * DIVIDE ( rev24, sold24 ) VAR rate = rev25 - rev24 - volume "
  "VAR bsold25 = CALCULATE ( [Baseline Rooms Sold], HotelOutlook[Year] = 2025 ) VAR bsold32 = CALCULATE ( [Baseline Rooms Sold], HotelOutlook[Year] = 2032 ) "
  "VAR brev25 = CALCULATE ( [Baseline Revenue], HotelOutlook[Year] = 2025 ) VAR brev32 = CALCULATE ( [Baseline Revenue], HotelOutlook[Year] = 2032 ) "
  "VAR bopex25 = CALCULATE ( [Baseline Opex], HotelOutlook[Year] = 2025 ) VAR bopex32 = CALCULATE ( [Baseline Opex], HotelOutlook[Year] = 2032 ) "
  "VAR revpor = DIVIDE ( brev25, bsold25 ) VAR cpor = DIVIDE ( bopex25, bsold25 ) "
  "RETURN SWITCH ( s, "
  f"\"GOP 2024\", {yr('GOP', 2024)}, \"Volume\", volume, \"Rate\", rate, "
  f"\"Staff\", {costdelta('StaffCost')}, \"Energy\", {costdelta('EnergyCost')}, \"Maintenance\", {costdelta('MaintenanceCost')}, \"Food and beverage cost\", {costdelta('FoodBeverageCost')}, \"Other cost\", {costdelta('OtherOperatingCost')}, "
  "\"GOP 2025 (baseline)\", brev25 - bopex25, \"Volume the market gives\", ( bsold32 - bsold25 ) * ( revpor - cpor ), \"Price inflation\", brev32 - bsold32 * revpor, \"Cost inflation\", - ( bopex32 - bsold32 * cpor ) )",
  USDM, C7, "One value per bridge step: the 2024 to 2025 GOP bridge (actuals) and the 2025 to 2032 baseline bridge (scenario logic).")


def folio(channel):
    base = f"REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025, BookingChannels[Channel] = \"{channel}\""
    return (
        "VAR line = SELECTEDVALUE ( FolioLine[Line] ) "
        f"VAR rate = CALCULATE ( DIVIDE ( [Channel Room Revenue], [Channel Room Nights] ), {base} ) "
        f"VAR comm = CALCULATE ( DIVIDE ( [Distribution Cost], [Channel Room Nights] ), {base} ) "
        'RETURN SWITCH ( line, "The guest pays", rate, "Commission and fees", - comm, "Goodnight Inn keeps", rate - comm )'
    )


FOLIO_FMT = r"\$#,0.00;" + "−" + r"\$#,0.00"
m("Folio OTA Guest", folio("Online Travel Agencies"), FOLIO_FMT, C7, "The folio: a 2025 OTA room night, what the channel takes and what the hotel keeps (filter the visual to one brand).")
m("Folio Direct Guest", folio("Direct Website & App"), FOLIO_FMT, C7, "The folio: the same room night booked on the brand's own site or app (filter the visual to one brand).")


def folio_text(channel):
    # as text, and 'keeps' from the two shown amounts: $109.31 - $19.68 = $89.63, never $89.64 (REVIEW M8)
    base = f"REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025, BookingChannels[Channel] = \"{channel}\""
    return ("VAR line = SELECTEDVALUE ( FolioLine[Line] ) "
            f"VAR rate = ROUND ( CALCULATE ( DIVIDE ( [Channel Room Revenue], [Channel Room Nights] ), {base} ), 2 ) "
            f"VAR comm = ROUND ( CALCULATE ( DIVIDE ( [Distribution Cost], [Channel Room Nights] ), {base} ), 2 ) "
            'RETURN SWITCH ( line, "The guest pays", FORMAT ( rate, "$#,0.00" ), "Commission and fees", UNICHAR ( 8722 ) & FORMAT ( comm, "$#,0.00" ), "Goodnight Inn keeps", FORMAT ( rate - comm, "$#,0.00" ) )')


m("Folio OTA Guest (text)", folio_text("Online Travel Agencies"), TXT, C7, "The folio's OTA column as text; the kept line is the difference of the two shown amounts.")
m("Folio Direct Guest (text)", folio_text("Direct Website & App"), TXT, C7, "The folio's direct column as text; the kept line is the difference of the two shown amounts.")
m("Benchmark after Distribution (text)",
  'CONCATENATEX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), Brands[Brand] & " " & FORMAT ( CALCULATE ( [GOP Margin after Distribution % 2025], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), TREATAS ( { Brands[Brand] }, Hotels[Brand] ) ), "0.0%" ), ", ", Brands[Brand] )',
  TXT, C7, "Sister-brand margins after distribution in 2025, for the benchmark note.")
m("Benchmark before Distribution (text)",
  'CONCATENATEX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), Brands[Brand] & " " & FORMAT ( CALCULATE ( [GOP Margin % 2025], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), TREATAS ( { Brands[Brand] }, Hotels[Brand] ) ), "0.0%" ), ", ", Brands[Brand] )',
  TXT, C7, "Sister-brand GOP margins before distribution in 2025.")
m("Occupancy vs 2024 (text)", 'FORMAT ( ( [Occupancy % 2025] - [Occupancy % 2024] ) * 100, "+0.0;-0.0;0.0" ) & " pt vs 2024"', TXT, C7, "KPI delta line.")
m("RevPAR vs 2024 (text)", 'FORMAT ( DIVIDE ( [RevPAR 2025], [RevPAR 2024] ) - 1, "+0.0%;-0.0%;0.0%" ) & " vs 2024"', TXT, C7, "KPI delta line.")
m("GOP Margin vs 2023 (text)", 'FORMAT ( ( [GOP Margin % 2025] - [GOP Margin % 2023] ) * 100, "+0.0;-0.0;0.0" ) & " pt vs 2023, " & FORMAT ( [GOP Margin after Distribution % 2025], "0.0%" ) & " after commissions"', TXT, C7, "KPI delta line.")
m("NPS vs 2021 (text)", 'FORMAT ( [NPS (weighted) 2025] - [NPS (weighted) 2021], "+0.0;-0.0;0.0" ) & " vs 2021"', TXT, C7, "KPI delta line.")
m("Counterfactual (text)", 'FORMAT ( [Distribution Cost above 2021 Mix 2025] / 1000000, "$0.0" ) & " M a year above the 2021 channel mix, at today\'s rates per channel (counterfactual)"', TXT, C7, "The $ at the 2021 mix callout.")
m("Headline Plan (text)", 'FORMAT ( [Capex Selected] / 1000000, "$0.0" ) & " M of " & FORMAT ( [Budget] / 1000000, "$0" ) & " M on " & [Projects Selected] & " projects: " & FORMAT ( [2032 Run-rate] / 1000000, "+$0.0;-$0.0" ) & " M a year of operating profit by 2032 (" & [Selected Scenario] & ")"', TXT, C7, "Dynamic page-2 headline from the selection.")
m("Headline Wall (text)", 'VAR full = COUNTROWS ( FILTER ( VALUES ( Hotels[HotelID] ), [Hotel Status 2025] = "Full" ) ) VAR tired = COUNTROWS ( FILTER ( VALUES ( Hotels[HotelID] ), [Hotel Status 2025] = "Tired" ) ) RETURN full & " are full. " & tired & " are tired."', TXT, C7, "Dynamic headline for the wall: counts of Full and Tired hotels.")
m("Wall Light", 'VAR y = SELECTEDVALUE ( PlanYear[Year], 2032 ) VAR n = COUNTROWS ( InvestmentProjectProperties ) VAR done = MAXX ( InvestmentProjects, YEAR ( InvestmentProjects[Completion Date] ) ) RETURN IF ( n > 0, IF ( done <= y, "lit", "planned" ) )', TXT, C7, "The wall: lit once the project is live in the chosen year, planned before that, blank when the hotel is not touched.")
m("Capacity (text)", 'VAR y = [First Capped Year] RETURN IF ( ISBLANK ( [Baseline Rooms Available] ), BLANK (), IF ( ISBLANK ( y ), "room to grow", "full in " & y ) )', TXT, C7, "Capacity wall label per hotel.")


# ================================================================ opzet 2026-11-06 (05-doorlichting-nieuwe-opzet.md)
# P1: the factual four-brand comparison and Goodnight Inn geography. P2: the package matrix
# with the focus swap (04-p2-build-method.md). Offline reference: project/analysis/40_ and 41_.
def _hanger(tile):
    """The faceless door hanger of kit 3.1 (plan 10 D6): a rounded tag with the hole and the slit, no face."""
    mask = "<mask id='h'><rect width='64' height='104' fill='white'/><circle cx='32' cy='24' r='10' fill='black'/><rect x='32' y='22.5' width='40' height='3' fill='black'/></mask>"
    return f"{mask}<rect x='4' y='4' width='56' height='96' rx='14' fill='{tile}' mask='url(%23h)'/>"


def _chip(on):
    """Funded: an Ice pill with a Coffee Blue hanger; not funded: a white pill with a Seam hairline and a Warm Grey
    light hanger. Decorative: the word next to it (Funded / Not funded, Pays back) carries the state."""
    fill, stroke, tile = ("%23EAF2FB", "%23EAF2FB", "%232589D8") if on else ("%23FFFFFF", "%23E3DFD3", "%23C9C4B7")
    svg = (f"<svg xmlns='http://www.w3.org/2000/svg' width='40' height='28' viewBox='0 0 40 28'>"
           f"<rect x='0.5' y='0.5' width='39' height='27' rx='13.5' fill='{fill}' stroke='{stroke}'/>"
           f"<g transform='translate(14.2 3) scale(0.2115)'>{_hanger(tile)}</g></svg>")
    return '"' + svg + '"'


CHIP_ON, CHIP_OFF = _chip(True), _chip(False)
IMAGE_MEASURES = {"Initiative Chip"}


C8 = "08 Brand comparison"
C9 = "09 Package matrix"
# .NET scales by 1,000 per comma only when the commas sit immediately left of the decimal point ("#,0,,.0");
# the earlier "#,0.0,," rendered "$9.400.000,0,,M" in Desktop (7 Nov). USDM above already uses the right form.
SUSDM = r"+\$#,0,,.0\M;" + "−" + r"\$#,0,,.0\M;\$0.0\M"
USDM1 = r"\$#,0,,.0\M"
# whole $M for a value axis: a tick carries no decimal separator in any locale (doc 21 P-1 b); "+$10M", "−$10M", "$0M"
SUSDM0 = r"+\$#,0,,\M;" + "−" + r"\$#,0,,\M;\$0\M"
MINUS = 'UNICHAR ( 8722 )'


# DAX FORMAT() does not scale by the trailing ",," of USDM1 / SUSDM (it printed "$4,806,360.8M" in Desktop, 7 Nov);
# those strings work only as a measure's formatString. Text measures divide explicitly instead.
# The one formatter set of the rebuild (doc 21 P-1, R-G1; the comp's mUSD / fm / sfm / pct1 in rebuild-comp-v10.html):
# money is "$" + one decimal + "M"; two decimals only for a non-zero amount that one decimal would show as 0.0
# ("+$0.03M", the kiosks' NPV in the High case). FORMAT gets "en-US", so no session locale reaches the text.
WJ = "UNICHAR ( 8288 )"
_MUSD = ('VAR __a = ABS ( __v ) + 0 VAR __r1 = ROUND ( __a, 1 ) VAR __r2 = ROUND ( __a, 2 ) '
         'VAR __m = "$" & IF ( __r1 = 0 && __r2 > 0, FORMAT ( __r2, "0.00", "en-US" ), FORMAT ( __r1, "#,0.0", "en-US" ) ) & "M" ')


def fm(x):
    """Money, unsigned: "$9.4M"; a negative amount gets a true minus and the word joiner."""
    return f'( VAR __v = ( {x} ) / 1000000 {_MUSD}RETURN IF ( __v < 0 && __r2 > 0, {MINUS} & {WJ}, "" ) & __m )'


def sfm(x):
    """Money, signed: "+$3.3M", "−$0.6M", "$0.0M"."""
    # sign from the shown (rounded) value, and no sign at zero: "+$0.0M" labelled an invisible bar (REVIEW m6)
    # a word joiner after the sign: wrapped copy broke "−" / "$0.6M" over two lines (render 7 Nov); U+2060 is a
    # default-ignorable character, so it draws nothing in Desktop's and the browser's text engines
    return f'( VAR __v = ( {x} ) / 1000000 {_MUSD}RETURN IF ( __r2 = 0, "$0.0M", IF ( __v < 0, {MINUS}, "+" ) & {WJ} & __m ) )'


def pct1(x):
    """A share with one decimal and a true minus: "47.0%", "−2.6%". FORMAT rounds the unrounded value (20.55 prints
    20.6, as Power BI's own format strings do)."""
    return f'( VAR __p = ( {x} ) * 100 RETURN IF ( ROUND ( __p, 1 ) < 0, {MINUS}, "" ) & FORMAT ( ABS ( __p ), "0.0", "en-US" ) & "%" )'


def pt1(x):
    """A signed number with one decimal, for points and scores: "+6.8", "−4.9", "0.0". The caller adds the unit."""
    return f'( VAR __q = ( {x} ) RETURN IF ( ROUND ( __q, 1 ) = 0, "0.0", IF ( __q < 0, {MINUS}, "+" ) & FORMAT ( ABS ( __q ), "0.0", "en-US" ) ) )'






# Kit goodnight-inn-wakeup 3.1 (plan 10 D1/D6, plan 11): marks in ACCENT_MARK (Coffee Blue), text and the
# recommended plan in ACCENT (Deep Coffee), signals in SIGNAL_MARK (Tangerine), sisters and context in SLATE (Warm
# Grey, 3.5:1 on white: a mark, never small text), ▲/▼ text in GOOD/BAD.
INK, INK2, GOOD, BAD, ACCENT, ACCENT_MARK, SIGNAL_MARK, SLATE, TINT, TINT2 = (
    "#12233D", "#4B5466", "#1763A8", "#A63F0E", "#1763A8", "#2589D8", "#E05A22", "#8E897D", "#EAF2FB", "#C5DCF3")
SURFACE = "#FFFFFF"  # the card surface (the alarm band's resting fill, round 5)
BRANDS = [("GI", "Goodnight Inn"), ("PS", "P&K Select"), ("MO", "Maison d'Or"), ("PP", "Pebble & Pine")]


def signed(expr, body):
    """Text with a true minus or a plus: body is a DAX text expression of ABS(expr)."""
    return f"IF ( {expr} < 0, {MINUS}, \"+\" ) & {body}"


def brand(b):
    return f"REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = \"{b}\""


m("Value for Money (weighted)", "DIVIDE ( SUMX ( GuestExperience, GuestExperience[ValueForMoneyScore] * GuestExperience[SurveyResponses] ), [Survey Responses] )", "0.00", C3, "Value-for-money score weighted by responses.")
m("Room Condition Complaints per 1k", 'DIVIDE ( CALCULATE ( [Complaints], GuestComplaints[Category] = "Room condition" ), [Rooms Sold] ) * 1000', "0.00", C3, "Room-condition complaints per thousand room nights sold.")
m("KPI Value",
  'VAR k = SELECTEDVALUE ( KpiLine[Key] ) RETURN SWITCH ( k, "occ", [Occupancy %], "adr", [ADR], "revpar", [RevPAR], "gop", [GOP Margin %], "gopa", [GOP Margin after Distribution %], '
  '"ota", [OTA Share %], "direct", [Direct Share %], "dist", [Distribution Cost % of Room Revenue], "nps", [NPS (weighted)], "comfort", [Room Comfort (weighted)], '
  '"value", [Value for Money (weighted)], "compl", [Complaints per 1k Room Nights], "roomcond", [Room Condition Complaints per 1k] )',
  "0.0000", C8, "The comparison line in context (KpiLine[Key]) as a number; formatting comes from KpiLine[Format] in the text measures.")
for y in (2023, 2025):
    m(f"KPI {y}", f"CALCULATE ( [KPI Value], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y} )", "0.0000", C8, f"The comparison line in calendar {y}.")
for code, b in BRANDS:
    m(f"KPI {code} 2025", f"CALCULATE ( [KPI 2025], {brand(b)} )", "0.0000", C8, f"{b}, comparison line, 2025.")
    m(f"KPI Text {code}", f"VAR v = [KPI {code} 2025] RETURN IF ( ISBLANK ( v ), BLANK (), FORMAT ( v, SELECTEDVALUE ( KpiLine[Format] ) ) )", TXT, C8, f"{b}: the 2025 value as formatted text for the comparison table.")
m("KPI GI 2023", f"CALCULATE ( [KPI 2023], {brand('Goodnight Inn')} )", "0.0000", C8, "Goodnight Inn, comparison line, 2023 (2021 is a depressed base year).")
m("KPI Rank",
  "VAR dir = SELECTEDVALUE ( KpiLine[Direction] ) VAR gn = [KPI GI 2025] "
  "VAR better = COUNTROWS ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), VAR b = Brands[Brand] RETURN dir * CALCULATE ( [KPI 2025], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = b ) > dir * gn ) ) "
  "RETURN IF ( ISBLANK ( gn ) || dir = 0, BLANK (), better + 1 )",
  "0", C8, "Goodnight Inn's rank among the four brands in the line's good direction (1 = best); blank for segment measures that are not ranked.")
m("KPI Rank (text)",
  "VAR r = [KPI Rank] VAR n = COUNTROWS ( ALLNOBLANKROW ( Brands[Brand] ) ) VAR dir = SELECTEDVALUE ( KpiLine[Direction] ) "
  'RETURN IF ( ISBLANK ( SELECTEDVALUE ( KpiLine[Key] ) ), BLANK (), IF ( dir = 0, "not ranked", SWITCH ( TRUE (), r = 1, UNICHAR ( 9650 ) & " best of " & n, r = n, UNICHAR ( 9660 ) & " last of " & n, r = 2, "2nd of " & n, "3rd of " & n ) ) )',
  TXT, C8, "Rank as words with an arrow (brand-guide section 6: the verdict never rests on color alone); the color repeats it.")
m("KPI Rank Color", f'VAR r = [KPI Rank] VAR n = COUNTROWS ( ALLNOBLANKROW ( Brands[Brand] ) ) RETURN SWITCH ( TRUE (), ISBLANK ( r ), "{INK2}", r = 1, "{GOOD}", r = n, "{BAD}", "{INK2}" )', TXT, C8, "Deep Coffee for best, Burnt Tangerine for last, Dusk otherwise (field-value font color).")
m("KPI Change since 2023 (text)",
  "VAR d = [KPI GI 2025] - [KPI GI 2023] VAR s = SELECTEDVALUE ( KpiLine[DeltaScale] ) VAR u = SELECTEDVALUE ( KpiLine[DeltaUnit] ) "
  "RETURN IF ( ISBLANK ( d ), BLANK (), " + signed("d", 'IF ( u = "$", "$", "" ) & FORMAT ( ABS ( d ) * s, SELECTEDVALUE ( KpiLine[DeltaFormat] ) ) & IF ( u = "pt", " pt", "" )') + " )",
  TXT, C8, "Goodnight Inn's change 2023 to 2025 in the line's unit (points for percentages).")
m("KPI Change Color", f'VAR d = ( [KPI GI 2025] - [KPI GI 2023] ) * SELECTEDVALUE ( KpiLine[Direction] ) RETURN SWITCH ( TRUE (), ISBLANK ( d ) || d = 0, "{INK2}", d > 0, "{GOOD}", "{BAD}" )', TXT, C8, "Direction-aware color of the change: good when it moved the right way.")
m("Occupancy and Hotels (text)", 'VAR o = [Occupancy % 2025] RETURN IF ( ISBLANK ( o ), BLANK (), FORMAT ( o, "0.0%" ) & " · " & [Hotels in Context] )', TXT, C8, "Geography matrix cell: 2025 occupancy and the number of hotels.")
m("Occupancy Heat Color", f'VAR o = [Occupancy % 2025] RETURN SWITCH ( TRUE (), ISBLANK ( o ), "#FFFFFF", o >= 0.85, "{TINT2}", o >= 0.80, "{TINT}", "#FFFFFF" )', TXT, C8, "Three-step tint for the geography matrix: 85 percent and over, 80 percent and over, below.")
m("GN Column Tint", f'"{TINT}"', TXT, C8, "Ice tint behind the Goodnight Inn column of the comparison table (field value, so no literal hex in the visual).")
m("Hotel Bar Color", f'IF ( SELECTEDVALUE ( Hotels[LocationType] ) = "Airport", "{ACCENT_MARK}", "{SLATE}" )', TXT, C8, "Coffee Blue for airport hotels, Warm Grey for the rest; the hotel names say Airport too, so colour is never the only carrier.")
for key, base in (("Margin after", "GOP Margin after Distribution %"), ("OTA", "OTA Share %"), ("NPS", "NPS (weighted)")):
    fmt = next(x[2] for x in MEASURES if x[0] == base)
    for code, b in BRANDS:
        m(f"Trend {key} {code}", f"CALCULATE ( [{base}], {brand(b)} )", fmt, C8, f"{b}: {base} on the trend axis.")
# round 10: the three sister brands as one line for the small F2 chart in the chip tooltip (four names did not fit a 416 px chart)
m("Trend OTA Sisters", 'CALCULATE ( [OTA Share %], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] <> "Goodnight Inn" )', "0.0%", C8,
  "The three sister brands together: OTA share of room revenue on the trend axis (room-revenue weighted), for the compact F2 tooltip chart.")
gi = brand("Goodnight Inn")
m("Subtitle P1 (text)",
  f"VAR occ = CALCULATE ( [Occupancy % 2025], {gi} ) VAR gm = CALCULATE ( [GOP Margin % 2025], {gi} ) VAR ga = CALCULATE ( [GOP Margin after Distribution % 2025], {gi} ) "
  f"VAR last = CALCULATE ( MAX ( Renovations[StartDate] ), {gi} ) "
  'RETURN "Goodnight Inn fills the most rooms (" & FORMAT ( occ, "0.0%" ) & ") and keeps the widest margin before commissions (" & FORMAT ( gm, "0.0%" ) & "); after commissions it is second (" & FORMAT ( ga, "0.0%" ) & "), and on guests, channels and complaints it is last of four. The last renovation started in " & FORMAT ( last, "mmm yyyy" ) & "."',
  TXT, C8, "Page-1 subtitle; the ranks it names are the KPI Rank values of the comparison table (verify on refresh).")
m("Geo Title (text)",
  f'VAR a = CALCULATE ( [Occupancy % 2025], {gi}, Hotels[LocationType] = "Airport" ) VAR h = CALCULATE ( [Occupancy % 2025], {gi}, Hotels[LocationType] = "Highway" ) '
  'RETURN "F4 · The airports are the fullest: " & FORMAT ( a, "0.0%" ) & " occupancy, against " & FORMAT ( h, "0.0%" ) & " on the highway"',
  TXT, C8, "Geography card title.")
m("Trend Title Margin (text)", f'"F1 · After commissions: " & FORMAT ( CALCULATE ( [GOP Margin after Distribution %], {gi}, REMOVEFILTERS ( \'Date\' ), \'Date\'[Year] = 2023 ), "0.0%" ) & " (2023) down to " & FORMAT ( CALCULATE ( [GOP Margin after Distribution % 2025], {gi} ), "0.0%" )', TXT, C8, "Trend title, margin after commissions.")
m("Trend Title OTA (text)", f'"F2 · OTAs book " & FORMAT ( CALCULATE ( [OTA Share % 2025], {gi} ), "0.0%" ) & " of room revenue, up from " & FORMAT ( CALCULATE ( [OTA Share %], {gi}, REMOVEFILTERS ( \'Date\' ), \'Date\'[Year] = 2021 ), "0.0%" )', TXT, C8, "Trend title, OTA share.")
m("Trend Title NPS (text)", f'VAR n = CALCULATE ( [NPS (weighted) 2025], {gi} ) RETURN "F3 · NPS down every year, to " & ' + signed("n", 'FORMAT ( ABS ( n ), "0.0" )') + ' & "; sisters higher"', TXT, C8, "Trend title, NPS (the yearly fall is checked in 41_opzet_facts.py; re-check on refresh).")

# ---------------------------------------------------------------- P2: package matrix
def pkgval(col):
    return f'VAR s = [Selected Scenario] RETURN SWITCH ( s, "Low", SUM ( Package[{col} Low] ), "High", SUM ( Package[{col} High] ), SUM ( Package[{col} Expected] ) )'


m("Package Capex", "SUM ( Package[CapexUSD] )", USDM1, C9, "Capex of the package(s) in context.")
m("Package NPV (sel)", pkgval("NPV"), SUSDM, C9, "Package NPV through 2032 in the selected scenario (scatter Y).")
m("Package Run-rate (sel)", pkgval("RunRate"), SUSDM, C9, "Package operating-profit run-rate in 2032, selected scenario.")
# A, B and C are fixed packages (Package[Preset], chosen on the Expected case; 07-fixgids K1, Björn 7 Nov): the
# scenario switch changes their numbers, never their composition, so no state can be empty (REVIEW B1, M6).
def preset_of(k):
    return f'LOOKUPVALUE ( Package[PackageID], Package[Preset], "{k}" )'


m("Preset A Package", preset_of("A"), TXT, C9, "Package A: the valid package with the highest NPV through 2032 in the Expected case.")
m("Preset B Package", preset_of("B"), TXT, C9, "Package B: most hotels with a dataset guest-score effect among packages with NPV at least zero (Expected case), ties by NPV.")
m("Preset C Package", preset_of("C"), TXT, C9, "Package C: the highest-NPV package that includes the refresh of the ten oldest hotels (Expected case).")
m("Recommended Package", preset_of("A"), TXT, C9,
  "The Board recommendation (06-d1-briefing-opzet.md, Björn 7 Nov): package A, the valid package with the highest NPV through 2032 in the Expected case. Fixed: the scenario switch changes its numbers, never the package.")
m("Focus Key", 'SELECTEDVALUE ( PlanSelector[Key], "A" )', TXT, C9, "A, B or C: the package in focus (dropdown); A when nothing is picked.")
m("Focus Package", 'VAR k = [Focus Key] RETURN SWITCH ( k, "B", [Preset B Package], "C", [Preset C Package], [Recommended Package] )', TXT, C9,
  "The package in focus: A, B or C, each a fixed package. Default A, so the panel is never empty.")
m("Focus Highlight", "IF ( SELECTEDVALUE ( Package[PackageID] ) = [Focus Package], 1, 0 )", "0", C9, "1 for the scatter point in focus.")
m("Package Point Color",
  f'VAR k = SELECTEDVALUE ( Package[Preset] ) RETURN SWITCH ( k, "A", "{ACCENT}", "B", "{INK}", "C", "{INK}", "{SLATE}" )',
  TXT, C9, "Scatter color: Deep Coffee for A (the recommended plan; its white letter 6.2:1), Night for the alternatives B and C, Warm Grey for the other packages (3.5:1 on white; the earlier light lilac was 2.1:1). Plan 10 D6 on the v3 presets.")
m("Named Point Color", f'IF ( SELECTEDVALUE ( Package[Preset] ) = "A", "{ACCENT}", "{INK}" )', TXT, C9,
  "Marker colour of the A/B/C layer only (it draws nothing else): Deep Coffee for A, Night for B and C, so its white letters read at 6.2:1 and 15.8:1 (plan 11).")
m("Package Point Size",
  'VAR k = SELECTEDVALUE ( Package[Preset] ) RETURN SWITCH ( TRUE (), [Focus Highlight] = 1, 6, k = "A", 5, k IN { "B", "C" }, 3, 1 )',
  "0", C9, "Scatter size: the package in focus largest, then A, then B and C, the rest small.")
# Power BI's 'magnitude' bubble scale draws the DIAMETER in proportion to the value (measured 10 Nov: values 5, 3, 1 gave
# 22, 14 and 4 px in the full stack at multiplier -40; the small stack at -22 gives 3.2 px per unit). The letter needs
# about 22 px of dot, so the A/B/C layer gets its own values per stack, A a touch larger than B and C.
m("Named Point Size", 'IF ( SELECTEDVALUE ( Package[Preset] ) = "A", 5.8, 5.3 )', "0", C9,
  "Size of the A/B/C layer's dots in the full-size scatter: about 24 and 22 px, so Power BI centres each letter inside its dot (round 5: at the cloud's "
  "sizes B and C were too small for their letters, which fell beside the dots).")
m("Named Point Size (small)", 'IF ( SELECTEDVALUE ( Package[Preset] ) = "A", 7.2, 6.6 )', "0", C9,
  "Size of the A/B/C layer's dots in the small scatter (alts and build), about 23 px (the stack's cap at its multiplier). Measured 10 Nov: in this smaller "
  "plot Power BI puts the letters UNDER the dots whatever their size, so the small layer draws each letter as a tag in the dot's colour instead.")


def focus(expr, fmt, name, doc):
    m(name, f"VAR f = [Focus Package] RETURN CALCULATE ( {expr}, REMOVEFILTERS ( Package ), Package[PackageID] = f )", fmt, C9, doc)


focus("SUM ( Package[CapexUSD] )", USDM1, "Focus Capex", "Capex of the package in focus.")
focus("[Package NPV (sel)]", SUSDM, "Focus NPV (sel)", "NPV through 2032 of the package in focus, selected scenario.")
focus("SUM ( Package[NPV Low] )", SUSDM, "Focus NPV Low", "NPV of the package in focus, Low scenario.")
focus("SUM ( Package[NPV High] )", SUSDM, "Focus NPV High", "NPV of the package in focus, High scenario.")
focus("[Package Run-rate (sel)]", SUSDM, "Focus Run-rate (sel)", "2032 run-rate of the package in focus.")
focus("SUM ( Package[Projects] )", "0", "Focus Projects", "Initiatives in the package in focus.")
focus("SUM ( Package[Growth] )", "0", "Focus Growth", "Growth initiatives in the package in focus.")
focus("SUM ( Package[RoomsAdded] )", "#,0", "Focus Rooms Added", "Rooms added by the package in focus.")
focus("SUM ( Package[HotelsRated] )", "#,0", "Focus Hotels Rated", "Hotels touched by an initiative with a dataset guest-score effect (Expected), counted once.")
FIDS = 'VAR f = [Focus Package] VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = f ), "@p", PackageProject[ProjectID] ) '
m("Focus Project Flag", FIDS + "RETURN IF ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) IN ids, 1, 0 )", "0", C9, "1 for an initiative inside the package in focus (visual filter for the plan table).")
m("Focus Project NPV (sel)", FIDS + "RETURN SUMX ( FILTER ( VALUES ( InvestmentProjects[ProjectID] ), InvestmentProjects[ProjectID] IN ids ), [NPV @ 8%] )", SUSDM, C9,
  "NPV contribution per initiative in focus; at the total it sums to the package NPV (waterfall; reconciles with Package by construction).")
m("Focus Project Capex", FIDS + "RETURN SUMX ( FILTER ( VALUES ( InvestmentProjects[ProjectID] ), InvestmentProjects[ProjectID] IN ids ), CALCULATE ( SUM ( InvestmentProjects[CapexUSD] ) ) )", USDM1, C9, "Capex per initiative in focus.")
m("Focus Project Run-rate (sel)", FIDS + "RETURN SUMX ( FILTER ( VALUES ( InvestmentProjects[ProjectID] ), InvestmentProjects[ProjectID] IN ids ), [2032 Run-rate] )", SUSDM, C9, "Organisers' annual operating-profit impact per initiative in focus (reached by 2032).")
m("Focus Project Live (text)", "IF ( [Focus Project Flag] = 1, [Live (text)] )", TXT, C9, "Go-live month per initiative in focus.")
m("Focus Project Guest Effect (text)",
  'VAR p = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) VAR s = [Selected Scenario] VAR pts = CALCULATE ( MAX ( InvestmentScenarios[SatisfactionChangePts] ), InvestmentScenarios[Scenario] = s ) '
  'RETURN IF ( [Focus Project Flag] = 1, IF ( pts > 0, "+" & FORMAT ( pts, "0.00" ) & " on " & [Hotels Touched], "·" ) )',
  TXT, C9, "Dataset guest-score effect in points on the touched hotels; per initiative, never summed, never shown as NPS.")
# "Funded" only under the recommendation; under B or C it would read as a decision (REVIEW M5)
m("Initiative Status (text)",
  # 'Not in package' widened the column until 'Guest pts' fell off the table (batch-2 render, 7 Nov)
  'IF ( ISBLANK ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) ), BLANK (), IF ( [Focus Key] = "A", IF ( [Focus Project Flag] = 1, "Funded", "Not funded" ), IF ( [Focus Project Flag] = 1, "Included", "Excluded" ) ) )',
  TXT, C9, "Funded / Not funded under the recommendation A, Included / Excluded under B or C; the word carries the state, the chip and colour repeat it.")
m("Initiative Status Color", f'IF ( [Focus Project Flag] = 1, "{ACCENT}", "{INK2}" )', TXT, C9, "Deep Coffee inside the package, Dusk outside (field-value font color); the word carries the state.")
# The chip column carries the sort: an XML comment with a key before the <svg> (valid SVG, invisible) orders the rows
# package first, then by NPV, high to low, and puts the sort arrow under the blank chip header instead of 'Status'
# (REVIEW m5).
m("Initiative Order",
  'VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) '
  'VAR gi = FILTER ( ALLNOBLANKROW ( InvestmentProjects[ProjectID] ), LEFT ( InvestmentProjects[ProjectID], 3 ) = "GI-" ) '
  # each candidate evaluated on its own id with the table row's filters removed (a context transition alone kept the
  # row's Short Name filter and blanked every other initiative)
  'VAR r = RANKX ( gi, VAR p = InvestmentProjects[ProjectID] RETURN CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ), '
  'CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = me ), DESC, Skip ) '
  'RETURN IF ( ISBLANK ( me ), BLANK (), ( 1 - [Focus Project Flag] ) * 100 + r )',
  "0", C9, "Row order of the plan table: initiatives in the package first, each group by NPV in the selected scenario, high to low.")
m("Initiative Chip", "VAR f = [Focus Project Flag] RETURN IF ( ISBLANK ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) ), BLANK (), \"data:image/svg+xml;utf8,<!--\" & FORMAT ( [Initiative Order], \"000\" ) & \"-->\" & IF ( f = 1, " + CHIP_ON + ", " + CHIP_OFF + " ) )", TXT, C9,
  "The brand's state chip (kit 3.1) as an SVG image: a Coffee Blue hanger on Ice inside the package, a light grey hanger on white outside. Decorative; the Status word is the accessible carrier. Its sort key orders the table.")


def shown_parts(expr, unit=100000):
    """DAX VAR lines over `ids` (FIDS): @s per initiative in the package, `expr` rounded to `unit` ($0.1M; the tooltip
    uses $0.01M) by largest remainder, so the shown parts add up to the shown package total (REVIEW M8: waterfall B
    read 3.4 - 1.1 + 0.5 against a total of 2.7)."""
    return (f"VAR base = ADDCOLUMNS ( ids, \"@v\", VAR p = [@p] RETURN CALCULATE ( {expr}, REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) ) "
            f"VAR tr = ROUND ( SUMX ( base, [@v] ) / {unit}, 0 ) "
            f"VAR fl = ADDCOLUMNS ( base, \"@f\", INT ( [@v] / {unit} ) ) "
            f"VAR fr = ADDCOLUMNS ( fl, \"@r\", [@v] / {unit} - [@f] + VALUE ( RIGHT ( [@p], 2 ) ) * 0.000000001 ) "
            "VAR k = tr - SUMX ( fr, [@f] ) "
            f"VAR adj = ADDCOLUMNS ( fr, \"@s\", ( [@f] + IF ( RANKX ( fr, [@r], , DESC ) <= k, 1, 0 ) ) * {unit} ) ")


m("Focus Project NPV (shown)",
  FIDS + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( FILTER ( adj, [@p] IN VALUES ( InvestmentProjects[ProjectID] ) ), [@s] )", SUSDM, C9,
  "Waterfall: each initiative's NPV in the package in focus, rounded to $0.1M so the bars add up to the shown total.")
# The waterfall's value axis ends (plan 11): its axis is hidden (the bars carry signed labels), so the labels need
# headroom the automatic range does not leave in a 144 px chart. Bounds of the running total: every positive shown
# part stacked, every negative one stacked, plus 30 % and $0.5M for the label; zero always inside.
m("Waterfall Y End", FIDS + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( adj, IF ( [@s] > 0, [@s], 0 ) ) * 1.3 + 500000", "0", C9,
  "Waterfall value axis end: all positive shown parts stacked, plus 30 percent and $0.5M of room for the labels.")
m("Waterfall Y Start", FIDS + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( adj, IF ( [@s] < 0, [@s], 0 ) ) * 1.3 - 500000", "0", C9,
  "Waterfall value axis start: all negative shown parts stacked, plus 30 percent and $0.5M of room for the labels.")
for nm, expr in (("NPV", "[NPV @ 8%]"), ("Run-rate", "[2032 Run-rate]")):
    m(f"Initiative {nm} (text)",
      FIDS + shown_parts(expr) + f"VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) VAR v = IF ( me IN ids, MAXX ( FILTER ( adj, [@p] = me ), [@s] ), {expr} ) "
      "RETURN IF ( ISBLANK ( me ), BLANK (), " + sfm("v") + " )",
      TXT, C9, f"Plan table {nm.lower()} as text: inside the package rounded to add up to the package total, outside it as is.")
m("Initiative Capex (text)", 'VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) RETURN IF ( ISBLANK ( me ), BLANK (), ' + fm("SUM ( InvestmentProjects[CapexUSD] )") + " )",
  TXT, C9, "Plan table capex as text, to the $10K it is set in (24.75, not 24.8).")
m("Initiative Growth (text)", 'VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) RETURN IF ( ISBLANK ( me ), BLANK (), IF ( SELECTEDVALUE ( InvestmentProjects[GrowthInitiative] ) = "Yes", "Growth", "" ) )',
  TXT, C9, "The contest's growth flag per initiative, so the rule can be ticked off without arithmetic (REVIEW M11).")
# Finding and growth flag in one column (08-verbeterplan R4: at 11 pt the nine columns no longer fit 752 px)
m("Initiative Answers (text)",
  'VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) RETURN IF ( ISBLANK ( me ), BLANK (), SELECTEDVALUE ( InvestmentProjects[Answers Finding] ) '
  '& IF ( SELECTEDVALUE ( InvestmentProjects[GrowthInitiative] ) = "Yes", " · growth", "" ) )',
  TXT, C9, "Plan table: the page-1 finding the initiative answers, and the contest's growth flag (REVIEW M11).")
m("Chip Funded", '"data:image/svg+xml;utf8," & ' + CHIP_ON, TXT, C9, "The brand's funded chip (Coffee Blue hanger on Ice) as an image, beside the recommendation's title; decorative.")
IMAGE_MEASURES.add("Chip Funded")
m("Chip Plain", '"data:image/svg+xml;utf8," & ' + CHIP_OFF, TXT, C9, "The brand's plain chip (light grey hanger on white) as an image, beside the titles of B and C: not funded; decorative.")
IMAGE_MEASURES.add("Chip Plain")
m("Initiative Capex", "SUM ( InvestmentProjects[CapexUSD] )", USDM1, C9, "Capex per initiative.")
m("Initiative NPV (sel)", "[NPV @ 8%]", SUSDM, C9, "NPV through 2032 per initiative, selected scenario (same convention as the package matrix).")
m("Initiative Run-rate (sel)", "[2032 Run-rate]", SUSDM, C9, "Organisers' annual operating-profit impact per initiative, reached by 2032.")
m("Initiative Guest Effect (text)",
  'VAR s = [Selected Scenario] VAR pts = CALCULATE ( MAX ( InvestmentScenarios[SatisfactionChangePts] ), InvestmentScenarios[Scenario] = s ) '
  'RETURN IF ( ISBLANK ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) ), BLANK (), IF ( pts > 0, "+" & FORMAT ( pts, "0.00" ) & " on " & [Hotels Touched], "·" ) )',
  TXT, C9, "Dataset guest-score effect in points on the touched hotels; per initiative, never summed, never shown as NPS.")
for scn in ("Low", "Expected", "High"):
    m(f"Focus Cumulative Net ({scn})",
      FIDS + "VAR y = MAX ( 'Date'[Year] ) RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
      f"REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = \"{scn}\", TREATAS ( ids, ProjectCashflow[ProjectID] ) )",
      SUSDM, C9, f"Cumulative net impact of the package in focus, undiscounted 2025 dollars, {scn} scenario.")
m("Focus Payback Year",
  FIDS + "VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), \"@c\", VAR y = [Value] RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
  "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) ) RETURN MINX ( FILTER ( t, [@c] >= 0 ), [Value] )",
  "0", C9, "First year the cumulative net of the package in focus turns positive; blank when after 2032.")
m("Focus Rooms Refreshed",
  FIDS + 'VAR ren = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Category] = "Renovation" && InvestmentProjects[ProjectID] IN ids ), "@r", InvestmentProjects[ProjectID] ) '
  'VAR hs = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] IN ren ), "@h", InvestmentProjectProperties[HotelID] ) '
  "RETURN CALCULATE ( SUM ( Hotels[Rooms] ), REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( Brands ), TREATAS ( hs, Hotels[HotelID] ) ) + 0",
  "#,0", C9, "Rooms in the hotels a renovation initiative in focus touches.")
m("Focus Live By (text)", FIDS + 'RETURN FORMAT ( CALCULATE ( MAX ( InvestmentProjects[Completion Date] ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] IN ids ), "mmm yyyy" )', TXT, C9, "Month the last initiative in focus goes live.")


def preset_set(k):
    pk = f"[Preset {k} Package]"
    for nm, col, fmt in (("Capex", "SUM ( Package[CapexUSD] )", USDM1), ("NPV (sel)", "[Package NPV (sel)]", SUSDM), ("Run-rate (sel)", "[Package Run-rate (sel)]", SUSDM)):
        m(f"Preset {k} {nm}", f"VAR f = {pk} RETURN IF ( ISBLANK ( f ), BLANK (), CALCULATE ( {col}, REMOVEFILTERS ( Package ), Package[PackageID] = f ) )", fmt, C9, f"Preset {k}: {nm.lower()}.")
    m(f"Preset {k} Range (text)",
      f"VAR f = {pk} VAR lo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = f ) / 1000000 VAR hi = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = f ) / 1000000 "
      "RETURN IF ( ISBLANK ( f ), BLANK (), " + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & " to " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )') + " )",
      TXT, C9, f"Preset {k}: NPV from the Low to the High scenario, $M.")
    m(f"Preset {k} Mix (text)",
      f'VAR f = {pk} RETURN IF ( ISBLANK ( f ), "No package qualifies in this case.", f & ": " & CONCATENATEX ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = f ), LOOKUPVALUE ( InvestmentProjects[Short Name], InvestmentProjects[ProjectID], PackageProject[ProjectID] ), " + ", PackageProject[ProjectID], ASC ) )',
      TXT, C9, f"Preset {k}: package id and the initiatives in it.")


for k in "ABC":
    preset_set(k)
FP = 'LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "{}" )'
# The scatter's two views (Björn 7 Nov): every package, or a zoom on the region where A, B and C sit in any scenario.
# A disconnected toggle drives the axis ends through these measures; the scenario switch still never rescales.
VIEW_ZOOM = 'SELECTEDVALUE ( ScatterView[View], "All packages" ) <> "All packages"'
NAMED = 'FILTER ( ALLNOBLANKROW ( Package ), Package[Preset] <> "" )'
def down10(x):  # round down to $10M (INT rounds toward minus infinity, also for negatives)
    return f"INT ( ( {x} ) / 10000000 ) * 10000000"


def up10(x):
    return f"- INT ( - ( {x} ) / 10000000 ) * 10000000"


def down5(x):  # round down to $5M (08-verbeterplan V4: $10M steps left empty bands on every side)
    return f"INT ( ( {x} ) / 5000000 ) * 5000000"


def up5(x):
    return f"- INT ( - ( {x} ) / 5000000 ) * 5000000"


NPV3 = "{ Package[NPV Low], Package[NPV Expected], Package[NPV High] }"
m("Scatter X Start",
  down5('MINX ( ALLNOBLANKROW ( Package ), Package[CapexUSD] )'),
  "0", C9, "Scatter capex axis start: the $5M step below the cheapest package (a scatter needs no zero; 08-verbeterplan V4: the band from $0 to $9.4M was empty).")
m("Scatter X End",
  f"VAR full = {up10('MAXX ( ALLNOBLANKROW ( Package ), Package[CapexUSD] )')} + 2000000 VAR abc = {up5(f'MAXX ( {NAMED}, Package[CapexUSD] )')} + 2000000 "
  f"RETURN IF ( {VIEW_ZOOM}, abc, full )", "0", C9,
  "Scatter capex axis end: $2M beyond the budget for all packages (no half-clipped dots at $60M, REVIEW M2), or $2M beyond the next $5M above A, B and C in the zoom.")
# $1.5M of air beyond the extreme dot before rounding: C at -$34.8M sat on a -$35M edge, half cut (render 7 Nov)
for nm, agg, fn, pad in (("Start", "MINX", down5, " - 1500000"), ("End", "MAXX", up5, " + 1500000")):
    m(f"Scatter Y {nm}",
      f"VAR full = {fn(f'{agg} ( ALLNOBLANKROW ( Package ), {agg} ( {NPV3}, [Value] ) ){pad}')} "
      f"VAR abc = {fn(f'{agg} ( {NAMED}, {agg} ( {NPV3}, [Value] ) ){pad}')} "
      f"RETURN IF ( {VIEW_ZOOM}, abc, full )", "0", C9,
      f"Scatter NPV axis {nm.lower()}: one range for all three scenarios (DC-034), rounded out to $5M, over all packages or over A, B and C in the zoom.")


# ---- the package tooltip (08-verbeterplan V2): one native report-page tooltip for every dot on the scatter, the
# cloud as well as A, B and C. Grain: one Package[PackageID] (the hover layer's category).
C10 = "10 Package tooltip"
TT_ID = "VAR pkg = SELECTEDVALUE ( Package[PackageID] ) "
TT_NPV = "VAR npv = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = pkg ) "
m("TT Title (text)",
  TT_ID + 'VAR k = LOOKUPVALUE ( Package[Preset], Package[PackageID], pkg ) VAR n = LOOKUPVALUE ( Package[Projects], Package[PackageID], pkg ) '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), SWITCH ( k, "", "A package of " & n & " moves", "C", "C · Why not renovate?", LOOKUPVALUE ( PlanSelector[Label], PlanSelector[Key], k ) ) )',
  TXT, C10, "Tooltip header: A, B or C by name and role, any other package by its size.")
m("TT Capex (text)", TT_ID + "RETURN IF ( ISBLANK ( pkg ), BLANK (), " + fm("LOOKUPVALUE ( Package[CapexUSD], Package[PackageID], pkg )") + " )", TXT, C10, "Tooltip: capex of the hovered package, two decimals like the NPV beside it (round 5).")
m("TT NPV (text)", TT_ID + TT_NPV + "RETURN IF ( ISBLANK ( pkg ), BLANK (), " + sfm("npv") + " )", TXT, C10, "Tooltip: NPV through 2032 of the hovered package, scenario in view, two decimals (round 5).")
m("TT NPV Label (text)", '"NPV through 2032, " & [Selected Scenario] & " case"', TXT, C10, "Tooltip: label under the NPV.")
m("TT NPV Color", TT_ID + TT_NPV + f'RETURN IF ( ROUND ( npv / 100000, 0 ) >= 0, "{ACCENT}", "{BAD}" )', TXT, C10,
  "Tooltip NPV colour: Deep Coffee when it pays back by 2032 (NPV at least zero), Burnt Tangerine below (08-verbeterplan V2); the sign and the payback line carry it too.")
m("TT Range (text)",
  TT_ID + "VAR lo = LOOKUPVALUE ( Package[NPV Low], Package[PackageID], pkg ) / 1000000 VAR ex = LOOKUPVALUE ( Package[NPV Expected], Package[PackageID], pkg ) / 1000000 "
  "VAR hi = LOOKUPVALUE ( Package[NPV High], Package[PackageID], pkg ) / 1000000 "
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), "Low " & ' + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & ", Expected " & ' + signed("ex", 'FORMAT ( ABS ( ex ), "0.0" )')
  + ' & ", High " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )') + ' & " ($M; the dark line is break-even)" )',
  TXT, C10, "Tooltip: NPV of the hovered package in all three cases, $M, and the name of the range bar's zero line (round 6).")
m("TT Payback Year",
  TT_ID + 'VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = pkg ), "@p", PackageProject[ProjectID] ) VAR s = [Selected Scenario] '
  "VAR t = ADDCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), \"@c\", VAR y = [Value] RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
  "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) ) RETURN MINX ( FILTER ( t, [@c] >= 0 ), [Value] )",
  "0", C10, "First year the cumulative net of the hovered package turns positive, scenario in view; blank when not by 2032.")
m("TT Payback (text)",
  # 'pays back by 2032' is the scatter's own line (NPV at least zero); the cash year is said only under it, so the
  # tooltip never claims a payback the line denies, and nothing after 2032 (08-verbeterplan N11)
  TT_ID + TT_NPV + "VAR pb = [TT Payback Year] "
  "VAR lo = ROUND ( LOOKUPVALUE ( Package[NPV Low], Package[PackageID], pkg ) / 100000, 0 ) VAR ex = ROUND ( LOOKUPVALUE ( Package[NPV Expected], Package[PackageID], pkg ) / 100000, 0 ) "
  "VAR hi = ROUND ( LOOKUPVALUE ( Package[NPV High], Package[PackageID], pkg ) / 100000, 0 ) "
  'VAR cash = IF ( ROUND ( npv / 100000, 0 ) >= 0 && NOT ISBLANK ( pb ), "; cash positive from " & pb, "" ) '
  # round 6: the verdict reads all three cases, not only the one in view (second opinion: the strongest true sentence)
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), SWITCH ( TRUE (), hi < 0, "Does not pay back by 2032, not even in the High case", lo >= 0, "Pays back by 2032 in every case" & cash, '
  'ex >= 0, "Pays back by 2032 except in Low" & cash, "Pays back by 2032 only in the High case" & cash ) )',
  TXT, C10, "Tooltip verdict: whether the hovered package pays back by 2032 across the three cases (not even in High / only in High / Expected and High / every case), "
            "and the first cash-positive year when the case in view pays back.")
m("Scatter Title (text)",
  'VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( ALLNOBLANKROW ( Package ), "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
  'VAR n = COUNTROWS ( t ) VAR pos = FILTER ( t, [@v] >= 0 ) VAR k = COUNTROWS ( pos ) + 0 VAR cap = INT ( MAXX ( pos, Package[CapexUSD] ) / 1000000 ) + 1 '
  'RETURN IF ( k = 0, "None of the " & n & " possible packages pays back by 2032 in the " & s & " case", '
  '"Only " & k & " of " & n & " packages " & IF ( k = 1, "pays back by 2032, at under $", "pay back by 2032, all under $" ) & cap & "M" )',
  TXT, C9, "Scatter title: how many packages have NPV through 2032 at least zero in the selected scenario, and the capex ceiling they share (the next whole $M above the largest).")
m("Scatter Title Short (text)",
  'VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( ALLNOBLANKROW ( Package ), "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
  'VAR n = COUNTROWS ( t ) VAR k = COUNTROWS ( FILTER ( t, [@v] >= 0 ) ) + 0 '
  'RETURN IF ( k = 0, "No package pays back by 2032 in the " & s & " case", "Only " & k & " of " & n & " packages " & IF ( k = 1, "pays", "pay" ) & " back by 2032" )',
  TXT, C9, "The scatter title for the small card (alts and build states): the count alone, one line at 672 px.")
m("Shortlist Title (text)", '"Three packages, one per criterion (" & [Selected Scenario] & " case)"', TXT, C9, "Shortlist state title.")
# Names instead of codes in everything a board member reads (REVIEW M5); the role of the package is in its name.
# C is the comparator, not a third candidate (08-verbeterplan V1, Björn 7 Nov): it is shown to answer "why not
# renovate?", and every place that names it says so.
ROLE = 'SWITCH ( [Focus Key], "B", "considered, not recommended", "C", "why not renovate?", "our recommendation" )'
m("Plan Title (text)",
  'VAR f = [Focus Package] RETURN IF ( ISBLANK ( f ), BLANK (), "Package " & [Focus Key] & " (" & ' + ROLE + ' & "): " & ' + fm("[Focus Capex]") + ' & " on " & [Focus Projects] & " initiatives, all live by " & [Focus Live By (text)] )',
  TXT, C9, "Plan state title: which package, its role, capex, size and go-live.")
m("Plan Risk (text)",
  # every fragment guarded: with no package there is no NPV ("+M") and no payback year to claim (REVIEW B1).
  # The case in view is "this case" (08-verbeterplan N9: "NPV in the Low case ... (Low)" read twice); nothing is
  # claimed after 2032, the horizon the page itself sets (N11: "turns positive after 2032").
  FIDS + 'VAR s = [Selected Scenario] VAR ren = "GI-07" IN ids VAR pb = [Focus Payback Year] VAR lo = [Focus NPV Low] '
  'VAR oos = LOOKUPVALUE ( InvestmentProjects[RoomsOutOfServicePct], InvestmentProjects[ProjectID], "GI-07" ) VAR dur = LOOKUPVALUE ( InvestmentProjects[DurationMonths], InvestmentProjects[ProjectID], "GI-07" ) '
  'RETURN IF ( ISBLANK ( f ), BLANK (), "Risks: " & IF ( ren, FORMAT ( oos, "0%" ) & " of " & FORMAT ( [Focus Rooms Refreshed], "#,0" ) & " rooms out of service for " & dur & " months; ", "" ) '
  '& IF ( ISBLANK ( lo ) || s = "Low", "", "in the Low case NPV falls to " & ' + sfm("lo") + ' & "; " ) '
  '& IF ( ISBLANK ( pb ), "in this case it does not pay back by 2032.", "in this case the cumulative net turns positive in " & pb & "." ) '
  '& IF ( "GI-02" IN ids, " Kiosks wait for the app: they start when it goes live.", "" ) )',
  TXT, C9, "Plan state: the risks of the package in focus in one sentence; blank when there is no package.")
m("Focus Line (text)",
  'VAR f = [Focus Package] VAR s = [Selected Scenario] '
  'RETURN IF ( ISBLANK ( f ), BLANK (), "In focus: " & SELECTEDVALUE ( PlanSelector[Label], "A · Our recommendation" ) & "  ·  " & ' + fm("[Focus Capex]") + ' & "  ·  NPV " & ' + sfm("[Focus NPV (sel)]") + ' & " (" & s & ")" )',
  TXT, C9, "One line under the dropdown, so changing the focus shows on the landing (REVIEW m2).")
m("Open Plan Label (text)", '"Open the plan for package " & [Focus Key] & "  " & UNICHAR ( 8594 )', TXT, C9, "Button text that names the package in focus (REVIEW m2).")
m("Plan Ops (text)",
  'VAR ra = [Focus Rooms Added] VAR rr = [Focus Rooms Refreshed] VAR hr = [Focus Hotels Rated] '
  'VAR parts = FILTER ( { ( 1, IF ( ra > 0, FORMAT ( ra, "#,0" ) & " rooms added" ) ), ( 2, IF ( rr > 0, FORMAT ( rr, "#,0" ) & " rooms refreshed" ) ), ( 3, IF ( hr > 0, "a guest-score effect in " & hr & " hotels" ) ) }, NOT ISBLANK ( [Value2] ) ) '
  # under C, first the reason it is shown (08-verbeterplan V1), only while the model holds it: below zero in all three
  'VAR f = [Focus Package] VAR lo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = f ) '
  'VAR ex = CALCULATE ( SUM ( Package[NPV Expected] ), REMOVEFILTERS ( Package ), Package[PackageID] = f ) VAR hi = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = f ) '
  'VAR why = IF ( [Focus Key] = "C" && ROUND ( lo / 100000, 0 ) < 0 && ROUND ( ex / 100000, 0 ) < 0 && ROUND ( hi / 100000, 0 ) < 0, '
  '"Shown to answer \'why not renovate?\': it stays below zero through 2032 in every case, High included (" & ' + sfm("hi") + ' & "). ", "" ) '
  'RETURN IF ( COUNTROWS ( parts ) = 0 && why = "", BLANK (), why & IF ( COUNTROWS ( parts ) = 0, "", "In the hotels: " & CONCATENATEX ( parts, [Value2], ", ", [Value1], ASC ) & "." ) )',
  TXT, C9, "What the package changes in the hotels, without zero tiles (REVIEW p9, 07-fixgids S6); under C first why it is shown.")
m("Waterfall Title (text)", '"Where the NPV comes from, $M through 2032 (" & [Selected Scenario] & ")"', TXT, C9, "Waterfall title with the scenario in view (REVIEW m6).")
# The plan chart's three context lines step aside for the case in view: the emphasised line ("This case") would
# otherwise lie on top of its twin and Power BI drops both labels (pass-3 review: the blue line had no label).
for scn in ("Low", "Expected", "High"):
    m(f"Cumulative Line ({scn})", f'IF ( [Selected Scenario] = "{scn}", BLANK (), [Focus Cumulative Net ({scn})] )', SUSDM, C9,
      f"Plan chart: the {scn} case line, blank when {scn} is the case in view (the emphasised line draws it).")
m("Focus Cumulative Net (sel)",
  'SWITCH ( [Selected Scenario], "Low", [Focus Cumulative Net (Low)], "High", [Focus Cumulative Net (High)], [Focus Cumulative Net (Expected)] )', SUSDM, C9,
  "Cumulative net impact of the package in focus in the selected scenario: the emphasised line (REVIEW M9).")
REC_IDS = 'VAR a = [Recommended Package] VAR aIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ), "@p", PackageProject[ProjectID] ) '
m("Uncertainty (text)",
  'VAR a = [Recommended Package] VAR k = COUNTROWS ( FILTER ( ALLNOBLANKROW ( Package ), Package[NPV Low] >= 0 ) ) + 0 '
  'VAR lo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) '
  'RETURN "Low case: " & IF ( k = 0, "no package pays back by 2032", k & " packages pay back by 2032" ) & "; A ends at " & ' + sfm("lo") + ' & "."',
  TXT, C9, "Standing uncertainty line under the recommendation: the Low case, counted from Package.")


# ================================================================ D1 briefing v2 (06-d1-briefing-opzet.md, 7 Nov)
# P1: four benchmarked KPIs, three findings with one chart each, where we are full. P2: one recommendation (A) and
# its alternatives. Every number in a title or note is computed here, so the copy stays true after a refresh;
# connecting words that depend on a direction (fell / rose, grew / narrowed) are guarded the same way.
SIGNED1 = "+0.0;−0.0;0.0"


def gi_at(base, y, *extra):
    more = "".join(", " + e for e in extra)
    return f"CALCULATE ( [{base}], {gi}, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y}{more} )"


def rank_words(base, y, direction, best="best", worst="last"):
    """DAX VAR lines: gn (Goodnight Inn), r (its rank, 1 = best in the direction), n and words (rank with an arrow)."""
    # Goodnight Inn is left out of the count: evaluated along two filter paths its own value differs in the last bit
    # (…903 vs …908), counted itself as better and pushed the NPS rank to 5 of 4 ("3rd of 4" in Desktop, 7 Nov).
    return (f"VAR gn = {gi_at(base, y)} "
            f'VAR better = COUNTROWS ( FILTER ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN {direction} * '
            f"CALCULATE ( [{base}], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = b, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y} ) > {direction} * gn ) ) "
            "VAR r = better + 1 VAR n = COUNTROWS ( ALLNOBLANKROW ( Brands[Brand] ) ) "
            # no arrows: a ▼ beside "highest" read as "down" (REVIEW p8, 07-fixgids S11); the words carry the rank
            f'VAR words = SWITCH ( TRUE (), r = 1, "{best} of " & n, r = n, "{worst} of " & n, r = 2, "2nd of " & n, "3rd of " & n ) ')


def others(base, y, agg):
    return (f'{agg} ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN '
            f"CALCULATE ( [{base}], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = b, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y} ) )")


# P1 KPI band: value plus one comparison each (DC-051)
m("KPI Occupancy GI", gi_at("Occupancy %", 2025), PCT, C8, "Goodnight Inn occupancy, 2025 (KPI band).")
m("KPI Margin after GI", gi_at("GOP Margin after Distribution %", 2025), PCT, C8, "Goodnight Inn operating margin after commissions, 2025 (KPI band).")
m("KPI OTA GI", gi_at("OTA Share %", 2025), PCT, C8, "Share of Goodnight Inn room revenue booked through online travel agencies, 2025 (KPI band).")
m("KPI NPS GI", gi_at("NPS (weighted)", 2025), SIGNED1, C8, "Goodnight Inn net promoter score, response-weighted, 2025 (KPI band).")
# The KPI values as text: value and context line come from one formatter, so they can never show two number
# formats side by side (79,4% over 64.7% in a nl-NL Desktop, REVIEW M7)
for kp in ("Occupancy", "Margin after", "OTA"):
    m(f"KPI {kp} GI (text)", f'FORMAT ( [KPI {kp} GI], "0.0%" )', TXT, C8, f"KPI band value as text: {kp.lower()}.")
m("KPI NPS GI (text)", "VAR v = [KPI NPS GI] RETURN " + signed("v", 'FORMAT ( ABS ( v ), "0.0" )'), TXT, C8, "KPI band value as text: NPS with a true minus or a plus.")
m("Headline P1 (text)", '"Full rooms, a slipping margin: Goodnight Inn pays the middleman, and its welcome is fading."', TXT, C8,
  "Page-1 headline. 'Is losing its guests' overclaimed: occupancy is best of four and F3 says age costs loyalty, not yet rooms (REVIEW M4, 07-fixgids F7).")
m("KPI Occupancy Context (text)",
  rank_words("Occupancy %", 2025, 1) + 'RETURN words & ", the others " & FORMAT ( ' + others("Occupancy %", 2025, "MINX") + ', "0.0%" ) & " to " & FORMAT ( ' + others("Occupancy %", 2025, "MAXX") + ', "0.0%" )',
  TXT, C8, "KPI band: rank among the four brands and the range of the other three, 2025.")
m("KPI Margin after Context (text)",
  # the change from the two shown values (36.5% to 33.7% in F1's title), not from the unrounded ones: -2.8, not -2.7 (REVIEW M8)
  rank_words("GOP Margin after Distribution %", 2025, 1) + "VAR d = ( ROUND ( gn, 3 ) - ROUND ( " + gi_at("GOP Margin after Distribution %", 2023) + ", 3 ) ) * 100 "
  'RETURN words & ", " & ' + signed("d", 'FORMAT ( ABS ( d ), "0.0" )') + ' & " pt since 2023"',
  TXT, C8, "KPI band: rank among the four brands and the change since 2023 in points.")
m("KPI OTA Context (text)",
  rank_words("OTA Share %", 2025, -1, best="lowest", worst="highest") + 'RETURN words & ", " & FORMAT ( ' + gi_at("OTA Share %", 2021) + ', "0.0%" ) & " in 2021"',
  TXT, C8, "KPI band: rank among the four brands (lower is better) and the 2021 share.")
NPS_DROPS = ("VAR drops = COUNTROWS ( FILTER ( GENERATESERIES ( 2022, 2025, 1 ), VAR y = [Value] RETURN CALCULATE ( [NPS (weighted)], " + gi + ", REMOVEFILTERS ( 'Date' ), 'Date'[Year] = y ) "
             "< CALCULATE ( [NPS (weighted)], " + gi + ", REMOVEFILTERS ( 'Date' ), 'Date'[Year] = y - 1 ) ) ) + 0 ")
m("KPI NPS Context (text)",
  # feedback round 4 (Björn 10 Nov): still positive, but falling every year (guarded year by year); the sisters' range
  # moved to the alt text (KPI NPS Sisters)
  rank_words("NPS (weighted)", 2025, 1) + NPS_DROPS + "VAR n21 = " + gi_at("NPS (weighted)", 2021) + " "
  'RETURN IF ( gn > 0, "still positive, but ", "" ) & IF ( drops = 4, "falling every year", IF ( gn < n21, "down since 2021", "up since 2021" ) ) & ", " & words',
  TXT, C8, "KPI band: NPS still positive but falling every year since 2021 (checked year by year), and the rank among the four brands.")
m("KPI NPS Sisters (text)",
  "VAR lo = " + others("NPS (weighted)", 2025, "MINX") + " VAR hi = " + others("NPS (weighted)", 2025, "MAXX") + " VAR n21 = " + gi_at("NPS (weighted)", 2021) + " "
  'RETURN "from " & ' + signed("n21", 'FORMAT ( ABS ( n21 ), "0.0" )') + ' & " in 2021; the others " & ' + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & " to " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )'),
  TXT, C8, "KPI band, read aloud only: the 2021 value and the range of the other three brands, 2025.")
m("KPI NPS Alt Context (text)", '[KPI NPS Context (text)] & ", " & [KPI NPS Sisters (text)]', TXT, C8, "The NPS context line with the sisters' range, for the alt text.")
# feedback round 4, a little more orange: the KPI context lines in Burnt Tangerine where the news is bad (last of four,
# or moving the wrong way), Deep Coffee where it is best of four, Dusk otherwise. The words carry it; the colour repeats it.
m("KPI Occupancy Context Color", rank_words("Occupancy %", 2025, 1) + f'RETURN SWITCH ( TRUE (), r = 1, "{GOOD}", r = n, "{BAD}", "{INK2}" )', TXT, C8, "Field-value colour of the occupancy context line.")
m("KPI Margin after Context Color",
  rank_words("GOP Margin after Distribution %", 2025, 1) + "VAR d = ( ROUND ( gn, 3 ) - ROUND ( " + gi_at("GOP Margin after Distribution %", 2023) + ", 3 ) ) * 100 "
  f'RETURN SWITCH ( TRUE (), d < 0 || r = n, "{BAD}", r = 1, "{GOOD}", "{INK2}" )', TXT, C8, "Field-value colour of the margin context line: Burnt Tangerine when the margin fell since 2023 or is last.")
m("KPI OTA Context Color", rank_words("OTA Share %", 2025, -1, best="lowest", worst="highest") + f'RETURN SWITCH ( TRUE (), r = 1, "{GOOD}", r = n, "{BAD}", "{INK2}" )', TXT, C8, "Field-value colour of the OTA context line (lower is better).")
m("KPI NPS Context Color", rank_words("NPS (weighted)", 2025, 1) + NPS_DROPS + f'RETURN SWITCH ( TRUE (), r = n || drops = 4, "{BAD}", r = 1, "{GOOD}", "{INK2}" )', TXT, C8, "Field-value colour of the NPS context line: Burnt Tangerine when last or falling every year.")

# P1 F1 the margin
def adr_chg(brand_dax):
    """Room-rate (ADR) change 2023 to 2025 as a fraction; brand_dax is a DAX expression: '"Goodnight Inn"' or a VAR."""
    at = lambda y: f"CALCULATE ( [ADR], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = {brand_dax}, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {y} )"
    return f"DIVIDE ( {at(2025)}, {at(2023)} ) - 1"


def adr_chg_sisters(agg):
    return f'{agg} ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN {adr_chg("b")} )'


m("Trend Margin before GI", f"CALCULATE ( [GOP Margin %], {gi} )", PCT, C8, "Goodnight Inn GOP margin before commissions on the trend axis.")
m("F1 Title (text)",
  "VAR a = " + gi_at("GOP Margin after Distribution %", 2023) + " VAR z = " + gi_at("GOP Margin after Distribution %", 2025) + " "
  # FinalV2 (plan 15 S5): the fall is a 2023-2025 story while the chart starts in 2021, so the title says since when, like the KPI line
  # the change from the two shown (rounded) values, like the KPI line: 36.5 to 33.7 is 2.8 points, the unrounded values give 2.7 (REVIEW M8)
  'RETURN "After commissions, the margin " & IF ( z < a, "fell", "rose" ) & " " & FORMAT ( ABS ( ROUND ( z, 3 ) - ROUND ( a, 3 ) ) * 100, "0.0" ) & " points since 2023"',
  TXT, C8, "F1 title: Goodnight Inn margin after commissions, the change in points since 2023.")

# P1 F2 the middleman
m("F2 Title (text)",
  "VAR a = " + gi_at("OTA Share %", 2021) + " VAR z = " + gi_at("OTA Share %", 2025) + " "
  'RETURN "Online agencies now book " & FORMAT ( z, "0%" ) & " of room revenue, " & IF ( z > a, "up", "down" ) & " from " & FORMAT ( a, "0%" )',
  TXT, C8, "F2 title: OTA share of Goodnight Inn room revenue, 2021 to 2025.")

# P1 F3 the fading welcome (Hotels[Renovation Age Sort]: dated hotels only)
m("NPS 2025 (signed)", "[NPS (weighted) 2025]", SIGNED1, C8, "Response-weighted NPS 2025 with a true minus, for chart labels.")
m("Age Band Color", f'IF ( SELECTEDVALUE ( Hotels[Renovation Age Sort] ) = 3, "{SIGNAL_MARK}", "{SLATE}" )', TXT, C8, "Tangerine for the oldest band (a risk signal: the only negative NPS), Warm Grey for the others; the axis label and the signed value carry it too.")
m("F3 Title (text)",
  "VAR v = " + gi_at("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 3") + ' RETURN "Hotels last renovated 10 years or more ago score NPS " & ' + pt1("v"),
  TXT, C8, "F3 title: NPS 2025 of the Goodnight Inn hotels last renovated 10 or more years ago.")

# P1 F4 where we are full
for t in ("Airport", "City", "Highway"):
    m(f"Occupancy {t} GI", gi_at("Occupancy %", 2025, f'Hotels[LocationType] = "{t}"'), PCT, C8, f"Goodnight Inn occupancy 2025 in {t.lower()} hotels.")
    m(f"Occupancy {t} GI (text)", f'FORMAT ( [Occupancy {t} GI], "0.0%" )', TXT, C8, f"Goodnight Inn occupancy 2025 in {t.lower()} hotels, as text (one formatter with the titles).")

# P2 the recommendation (A) and its alternatives
BUDGET_GI = 'CALCULATE ( SUM ( Brands[InvestmentBudgetUSD] ), REMOVEFILTERS ( Brands ), Brands[Brand] = "Goodnight Inn" )'


def rec(expr):
    return f"VAR a = [Recommended Package] RETURN CALCULATE ( {expr}, REMOVEFILTERS ( Package ), Package[PackageID] = a )"


m("Rec Capex", rec("SUM ( Package[CapexUSD] )"), USDM1, C9, "Capex of the recommendation.")
m("Rec NPV (sel)", rec("[Package NPV (sel)]"), SUSDM, C9, "NPV through 2032 of the recommendation, selected scenario.")
m("Rec Run-rate (sel)", rec("[Package Run-rate (sel)]"), SUSDM, C9, "Operating-profit run-rate in 2032 of the recommendation, selected scenario.")
m("Rec Range (text)",
  "VAR a = [Recommended Package] VAR lo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) / 1000000 "
  "VAR hi = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) / 1000000 "
  "RETURN " + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & " to " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )'),
  TXT, C9, "NPV of the recommendation from the Low to the High scenario, $M.")
NAME_OF = "LOOKUPVALUE ( InvestmentProjects[Short Name], InvestmentProjects[ProjectID], {} )"
m("Rec Mix (text)",
  'VAR a = [Recommended Package] RETURN CONCATENATEX ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ), ' + NAME_OF.format("PackageProject[ProjectID]") + ', " + ", PackageProject[ProjectID], ASC )',
  TXT, C9, "The initiatives in the recommendation.")
m("Rec Answers (text)",
  # the one move that does not pay on its own is said out loud, with the reason it stays (REVIEW M3, 07-fixgids F2)
  REC_IDS + f"VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR budget = {BUDGET_GI} "
  # the weakest move is chosen once, on the Expected case (in Low all three are negative and the sentence named the
  # booking app); its value is then said in the scenario in view
  'VAR npvs = ADDCOLUMNS ( aIds, "@e", VAR p = [@p] RETURN CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p, Scenario[Scenario] = "Expected" ), '
  '"@n", VAR p = [@p] RETURN CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) ) '
  'VAR wp = MAXX ( TOPN ( 1, npvs, [@e], ASC ), [@p] ) VAR we = MAXX ( FILTER ( npvs, [@p] = wp ), [@e] ) VAR wn = MAXX ( FILTER ( npvs, [@p] = wp ), [@n] ) '
  'VAR wf = LOOKUPVALUE ( InvestmentProjects[Answers Finding], InvestmentProjects[ProjectID], wp ) VAR wc = LOOKUPVALUE ( InvestmentProjects[CapexUSD], InvestmentProjects[ProjectID], wp ) '
  'VAR cheapest = wc <= MINX ( FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" && InvestmentProjects[Answers Finding] = wf ), InvestmentProjects[CapexUSD] ) '
  # where the weakest move goes (08-verbeterplan S10: "which 20 hotels get kiosks?"): its hotels, named as the n
  # fullest when they are exactly the n Goodnight Inn hotels with the highest 2025 occupancy, and by location type
  'VAR hs = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] = wp ), "@h", InvestmentProjectProperties[HotelID] ) '
  'VAR nh = COUNTROWS ( hs ) '
  'VAR occ = ADDCOLUMNS ( FILTER ( ALLNOBLANKROW ( Hotels ), Hotels[Brand] = "Goodnight Inn" ), "@o", CALCULATE ( [Occupancy % 2025] ) ) '
  'VAR fullest = COUNTROWS ( FILTER ( TOPN ( nh, occ, [@o], DESC ), Hotels[HotelID] IN hs ) ) = nh '
  'VAR ht = ADDCOLUMNS ( hs, "@t", LOOKUPVALUE ( Hotels[LocationType], Hotels[HotelID], [@h] ) ) '
  'VAR tt = GROUPBY ( ht, [@t], "@n", COUNTX ( CURRENTGROUP (), 1 ) ) '
  'VAR dest = IF ( nh > 1, " go to the " & nh & IF ( fullest, " fullest hotels", " hotels" ) & " (" & CONCATENATEX ( tt, [@n] & " " & LOWER ( [@t] ), ", ", [@n], DESC ) & ")", "" ) '
  'VAR wname = SUBSTITUTE ( LOWER ( ' + NAME_OF.format("wp") + ' ), " at " & nh & " desks", "" ) '
  'VAR neg = ROUND ( we / 100000, 0 ) < 0 && ROUND ( wn / 100000, 0 ) < 0 '
  'RETURN "Each move answers a Brand Review finding: " & CONCATENATEX ( aIds, LOWER ( ' + NAME_OF.format("[@p]") + ' ) & " " & LOOKUPVALUE ( InvestmentProjects[Answers Finding], InvestmentProjects[ProjectID], [@p] ), ", ", [@p], ASC ) & ". " '
  '& IF ( dest <> "" || neg, "The " & wname & dest '
  '& IF ( neg, IF ( dest <> "", "; on their own they", " on their own" ) & " return " & ' + sfm("wn") + ' & " by 2032" & IF ( cheapest, ", but they are the cheapest answer to " & wf, "" ), "" ) & ".", "" )',
  TXT, C9, "Which page-1 finding each move of A answers, where the weakest move goes, and why it stays although it does not pay back on its own.")
m("Rec Held (text)",
  # what the rest of the budget is for and when it comes back (08-verbeterplan S10), with only what the model holds:
  # the go-live of the three moves and whether any other initiative would pay back by 2032 in the High case
  REC_IDS + f"VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR budget = {BUDGET_GI} "
  'VAR k = COUNTROWS ( aIds ) VAR word = SWITCH ( k, 2, "both", 3, "all three", 4, "all four", 5, "all five", "all " & k ) '
  'VAR live = FORMAT ( CALCULATE ( MAX ( InvestmentProjects[Completion Date] ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] IN aIds ), "mmm yyyy" ) '
  'VAR others = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" && NOT ( InvestmentProjects[ProjectID] IN aIds ) ), "@p", InvestmentProjects[ProjectID] ) '
  'VAR hiPos = COUNTROWS ( FILTER ( others, VAR p = [@p] RETURN ROUND ( CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p, Scenario[Scenario] = "High" ) / 100000, 0 ) >= 0 ) ) + 0 '
  # plan 09 R3 (Profit Ability 2: show why the next euro is not spent; CREDITS.md): the best package that holds all of
  # A plus at least one more initiative, in the scenario in view. Said only when it lowers the NPV (shown, rounded to
  # $0.1M); otherwise blank, so no false claim in any case. Offline: A + breakfast upgrade, $4.25M more, -$1.1M
  # (Expected), -$2.6M (Low), -$0.1M (High) as shown (offline -$2.65M), recounted from project/analysis/output/packages.csv.
  'VAR s = [Selected Scenario] VAR nA = COUNTROWS ( aIds ) '
  'VAR sup = FILTER ( ALLNOBLANKROW ( Package ), Package[Projects] > nA && COUNTROWS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = Package[PackageID] && PackageProject[ProjectID] IN aIds ) ) = nA ) '
  'VAR t = ADDCOLUMNS ( sup, "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
  'VAR best = TOPN ( 1, t, [@v], DESC, Package[CapexUSD], ASC ) VAR bid = MAXX ( best, Package[PackageID] ) VAR bv = MAXX ( best, [@v] ) VAR bc = MAXX ( best, Package[CapexUSD] ) '
  'VAR av = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = a ) '
  'VAR added = CONCATENATEX ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = bid && NOT ( PackageProject[ProjectID] IN aIds ) ), LOWER ( ' + NAME_OF.format("PackageProject[ProjectID]") + ' ), " and ", PackageProject[ProjectID], ASC ) '
  'VAR margin = IF ( NOT ISBLANK ( bid ) && ROUND ( ( bv - av ) / 100000, 0 ) < 0, " The best way to spend more, A plus the " & added & ", costs " & ' + fm("bc - cap") + ' & " more and lowers the NPV by " & ' + fm("av - bv") + ' & ".", "" ) '
  'RETURN "The other " & ' + fm("budget - cap") + ' & " is held back, to be decided again once " & word & " moves are live, by " & live & ": " '
  '& IF ( hiPos = 0, "no other initiative pays back by 2032, even in the High case.", hiPos & " other initiatives pay back by 2032 only in the High case." ) & margin',
  TXT, C9, "The budget held back: until when, why nothing else is funded now, and the marginal test: the best package with all of A and more lowers the NPV (plan 09 R3).")
m("Rec Rules (text)",
  REC_IDS + f"VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR budget = {BUDGET_GI} VAR h = {FP.format('Impact horizon')} "
  'VAR g = FILTER ( aIds, LOOKUPVALUE ( InvestmentProjects[GrowthInitiative], InvestmentProjects[ProjectID], [@p] ) = "Yes" ) '
  # one line at 12 pt (plan 11): the growth initiatives are named in the plan table ("· growth") and Rec Mix
  'RETURN "Within the rules: " & COUNTROWS ( aIds ) & " initiatives, " & COUNTROWS ( g ) & " of them growth, " '
  '& ' + fm("cap") + ' & " of " & ' + fm("budget") + ' & ", impact through " & h & "."',
  TXT, C9, "The contest rules ticked off for A: initiatives, growth initiatives (dataset flag), budget, horizon (REVIEW M11).")


def alt(k, extra, lead='""'):
    """B or C against A: what it swaps, its capex and NPV in the selected scenario, then `extra` (DAX text, may use
    npvX, capX, npvA, capA, rA, rX, x). `lead` is DAX text before the swap (C's question)."""
    return (REC_IDS + f'VAR x = [Preset {k} Package] '
            'VAR xIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = x ), "@p", PackageProject[ProjectID] ) '
            # the short name 'Refresh 10 oldest' read badly mid-sentence ("the refresh 10 oldest instead of ...")
            'VAR added = CONCATENATEX ( FILTER ( xIds, NOT ( [@p] IN aIds ) ), SUBSTITUTE ( LOWER ( ' + NAME_OF.format("[@p]") + ' ), "refresh 10 oldest", "refresh of the 10 oldest hotels" ), " and ", [@p], ASC ) '
            'VAR dropped = CONCATENATEX ( FILTER ( aIds, NOT ( [@p] IN xIds ) ), LOWER ( ' + NAME_OF.format("[@p]") + ' ), " and ", [@p], ASC ) '
            'VAR capA = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR capX = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
            'VAR npvA = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR npvX = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
            'VAR rA = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR rX = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
            f'RETURN IF ( ISBLANK ( x ), BLANK (), "{k} · " & {lead} & IF ( dropped = "", "A plus the " & added, "The " & added & " instead of the " & dropped ) & ": " & ' + fm("capX") + ' & ", NPV " & ' + sfm("npvX") + f' & ". " & ( {extra} ) )')


m("Alt B (text)",
  alt("B", 'IF ( rX > rA, "A guest-score effect in " & rX & " hotels instead of " & rA & ", for " & ' + fm("capX - capA") + ' & " more and a " & IF ( npvX < npvA, "lower", "higher" ) & " NPV.", "" )'),
  TXT, C9, "Alternative B against the recommendation, selected scenario (B is fixed: 07-fixgids K1).")
# C is shown to answer "why not renovate?" (08-verbeterplan V1): the sentence says so, and that the renovation route
# stays below zero in every case, with the High case as the proof (guarded: the claim only appears when it holds).
m("Alt C (text)",
  alt("C", 'VAR hiX = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
           'VAR allNeg = ROUND ( CALCULATE ( MAX ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) / 100000, 0 ) < 0 '
           '&& ROUND ( CALCULATE ( MAX ( Package[NPV Expected] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) / 100000, 0 ) < 0 && ROUND ( hiX / 100000, 0 ) < 0 '
           'RETURN "It answers F3 most directly, " & IF ( allNeg, "but it stays below zero through 2032 in every case (High " & ' + sfm("hiX") + ' & ").", '
           'IF ( ROUND ( npvX / 100000, 0 ) < 0, "but it does not pay back by 2032 in this case.", "and it pays back by 2032." ) )',
      lead='"Why not renovate? "'),
  TXT, C9, "C against the recommendation, selected scenario: the answer to 'why not renovate?'; 'pays back by 2032' means NPV through 2032 at least zero, as on the scatter.")
m("Not Funded (text)",
  # the reason the selection really applies (A has the highest NPV of all 456 in Expected, so adding any of these
  # lowers it); "each has a negative NPV" was the test the kiosks fail too (REVIEW M3). Names as in the table (m9).
  REC_IDS + 'VAR bp = [Preset B Package] VAR cp = [Preset C Package] '
  'VAR bc = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] IN { bp, cp } ), "@p", PackageProject[ProjectID] ) '
  'VAR t = FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" && NOT ( InvestmentProjects[ProjectID] IN aIds ) && NOT ( InvestmentProjects[ProjectID] IN bc ) ) '
  'VAR names = CONCATENATEX ( t, InvestmentProjects[Short Name], ", ", InvestmentProjects[ProjectID], ASC ) '
  'VAR f4 = COUNTROWS ( FILTER ( t, InvestmentProjects[Answers Finding] = "F4" ) ) '
  'RETURN IF ( ISBLANK ( names ), BLANK (), "Not funded: " & names & IF ( f4 > 0, " (" & f4 & " of them answer F4)", "" ) & ": A has the highest NPV (Expected), so adding any lowers it." )',
  TXT, C9, "The initiatives outside A, B and C, and the reason the selection leaves them out.")
m("Alt Masthead P2 (text)", f'"2027 to 2032, Goodnight Inn budget " & ' + fm(BUDGET_GI), TXT, "11 Accessibility",
  "The P2 masthead read aloud in sentence case (the canvas line is in capitals, which a screen reader may spell out).")
m("Masthead P2 (text)", f'"2027 TO 2032  ·  GOODNIGHT INN BUDGET " & ' + fm(BUDGET_GI), TXT, C9,
  "Page-2 masthead line on the night zone: the horizon and the brand budget, read from Brands (was typed into the report generator).")
# the P2 panel's numbers as text, so a card never mixes a visual-formatted number with DAX text (REVIEW M7)
m("Rec Capex (text)", "VAR a = [Recommended Package] RETURN " + fm("CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a )"), TXT, C9, "Capex of A as text.")
m("Rec NPV (text)", sfm("[Rec NPV (sel)]"), TXT, C9, "NPV through 2032 of A, selected scenario, as text.")
m("Rec Run-rate (text)", sfm("[Rec Run-rate (sel)]"), TXT, C9, "Profit a year by 2032 of A, selected scenario, as text.")

# ================================================================ accessibility (plan 11): alt text from the model
# Alt text that states each visual's message with live values, so it can never drift from the data or from a
# refresh (the static alt texts carried typed numbers and colour names). Bound in the report through
# visualContainerObjects.general.altText as a measure (visualConfiguration 2.6.0: altText takes any expression).
# Practice after Meagan Longoria's Power BI accessibility checklist (CREDITS.md, a11y-studio).
C11 = "11 Accessibility"


def alt_m(name, dax, doc):
    m(f"Alt {name} (text)", dax, TXT, C11, doc)


def semi(measure):
    """A context line read aloud: the separator dot becomes a semicolon."""
    return f'SUBSTITUTE ( [{measure}], " · ", "; " )'


def gi_sgn(base, y, *extra):
    return "( VAR __v = " + gi_at(base, y, *extra) + " RETURN " + signed("__v", 'FORMAT ( ABS ( __v ), "0.0" )') + " )"


for key, label, value, ctx in (
        ("Occupancy", "Goodnight Inn occupancy in 2025", "KPI Occupancy GI (text)", "KPI Occupancy Context (text)"),
        ("Margin after", "Goodnight Inn operating margin after commissions in 2025", "KPI Margin after GI (text)", "KPI Margin after Context (text)"),
        ("OTA", "Share of Goodnight Inn room revenue booked through online agencies in 2025", "KPI OTA GI (text)", "KPI OTA Context (text)"),
        ("NPS", "Guest quality: Goodnight Inn net promoter score in 2025", "KPI NPS GI (text)", "KPI NPS Alt Context (text)")):
    alt_m(f"KPI {key}", f'"{label}: " & [{value}] & ", " & {semi(ctx)} & "."', f"KPI band, read aloud: the label, the value and the comparison ({key}).")

# Pass-3 review (plan 11): lead with the message (Power BI already announces the chart type), stay under 250
# characters (the alt-text limit Desktop enforces on typed text), spell out NPV and capex, and agree with the title.
alt_m("F1 Chart",
      "VAR a1 = " + gi_at("GOP Margin after Distribution %", 2021) + " VAR a3 = " + gi_at("GOP Margin after Distribution %", 2023) + " VAR a5 = " + gi_at("GOP Margin after Distribution %", 2025) + " "
      "VAR b1 = " + gi_at("GOP Margin %", 2021) + " VAR b5 = " + gi_at("GOP Margin %", 2025) + " "
      'RETURN "After commissions, Goodnight Inn\'s operating margin " & IF ( a3 > a1, "rose", "fell" ) & " from " & FORMAT ( a1, "0.0%" ) & " in 2021 to " & FORMAT ( a3, "0.0%" ) & " in 2023 and " '
      '& IF ( a5 < a3, "fell back", "rose" ) & " to " & FORMAT ( a5, "0.0%" ) & " in 2025. The gap to the margin before commissions grew from " '
      '& FORMAT ( ( b1 - a1 ) * 100, "0.0" ) & " to " & FORMAT ( ( b5 - a5 ) * 100, "0.0" ) & " points."',
      "F1 chart read aloud: the after-commissions path 2021, 2023, 2025 (as the title) and the commission gap.")
alt_m("F2 Chart",
      "VAR o1 = " + gi_at("OTA Share %", 2021) + " VAR o5 = " + gi_at("OTA Share %", 2025) + " "
      'RETURN "Online agencies booked " & FORMAT ( o5, "0.0%" ) & " of Goodnight Inn\'s room revenue in 2025, " & IF ( o5 > o1, "up", "down" ) & " from " & FORMAT ( o1, "0.0%" ) & " in 2021. The other brands in 2025: " '
      '& CONCATENATEX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN b & " " & FORMAT ( CALCULATE ( [OTA Share %], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = b, REMOVEFILTERS ( \'Date\' ), \'Date\'[Year] = 2025 ), "0.0%" ), ", ", Brands[Brand], ASC ) & "."',
      "F2 chart read aloud: Goodnight Inn's OTA share 2021 and 2025, and the sisters' 2025 values.")


def folio_pair(channel):
    base = f"{gi}, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025, BookingChannels[Channel] = \"{channel}\""
    return (f"ROUND ( CALCULATE ( DIVIDE ( [Channel Room Revenue], [Channel Room Nights] ), {base} ), 2 )",
            f"ROUND ( CALCULATE ( DIVIDE ( [Distribution Cost], [Channel Room Nights] ), {base} ), 2 )")


(_or, _oc), (_dr, _dc) = folio_pair("Online Travel Agencies"), folio_pair("Direct Website & App")
alt_m("F2 Folio",
      f"VAR orate = {_or} VAR ocomm = {_oc} VAR drate = {_dr} VAR dcomm = {_dc} "
      'RETURN "One Goodnight Inn room night in 2025. Via an online agency the guest pays " & FORMAT ( orate, "$#,0.00" ) & ", fees take " & FORMAT ( ocomm, "$#,0.00" ) '
      '& ", the inn keeps " & FORMAT ( orate - ocomm, "$#,0.00" ) & ". Booked direct: " & FORMAT ( drate, "$#,0.00" ) & ", fees " & FORMAT ( dcomm, "$#,0.00" ) '
      '& ", the inn keeps " & FORMAT ( drate - dcomm, "$#,0.00" ) & "."',
      "F2 folio table read aloud, the same rounding as the table (keeps = the difference of the shown amounts).")
alt_m("F3 Chart",
      '"Goodnight Inn\'s 2025 net promoter score by years since the last renovation: 5 years or less " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 1")
      + ' & ", 6 to 9 years " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 2") + ' & ", 10 years or more " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 3")
      + ' & ". Hovering a bar shows that band\'s occupancy, revenue per room, its NPS since 2021 and its weakest guest scores."',
      "F3 chart: the three bands' NPS 2025 (dated hotels only).")
alt_m("F4 Types",
      '"Goodnight Inn occupancy in 2025 by location type: airport hotels " & [Occupancy Airport GI (text)] & ", city hotels " & [Occupancy City GI (text)] & ", highway hotels " & [Occupancy Highway GI (text)] & "."',
      "F4 numbers card read aloud.")
alt_m("F4 Chart",
      f"VAR hs = CALCULATETABLE ( VALUES ( Hotels[HotelID] ), {gi} ) "
      "VAR t7 = ADDCOLUMNS ( TOPN ( 7, hs, CALCULATE ( [Occupancy %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ) ), \"@o\", CALCULATE ( [Occupancy %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ), "
      "\"@n\", CALCULATE ( SELECTEDVALUE ( Hotels[Hotel Short Name] ) ), \"@t\", CALCULATE ( SELECTEDVALUE ( Hotels[LocationType] ) ) ) "
      'VAR na = COUNTROWS ( FILTER ( t7, [@t] = "Airport" ) ) '
      'RETURN "The 7 fullest Goodnight Inn hotels in 2025, " & na & " of them airports: " & CONCATENATEX ( t7, [@n] & " " & FORMAT ( [@o], "0.0%" ), ", ", [@o], DESC ) & "."',
      "F4 chart read aloud: the seven fullest hotels with their occupancy (one decimal, as the bars), and how many are airports.")
for k, (code, words) in enumerate((("F1", "the margin"), ("F2", "the middleman"), ("F3", "the fading welcome"), ("F4", "where we are full")), 1):
    alt_m(f"{code} Title", f'"{code}, {words}. " & [{code} Title (text)]',
          f"{code} card title read aloud with its kicker (the kicker leaves the tab order; pass-3 review: fewer stops).")
alt_m("Scatter",
      '[Scatter Title (text)] & " (" & [Selected Scenario] & " case). A, our recommendation: capex " & ' + fm("[Preset A Capex]") + ' & ", net present value " & ' + sfm("[Preset A NPV (sel)]")
      + ' & ". B, the alternative: " & ' + fm("[Preset B Capex]") + ' & ", " & ' + sfm("[Preset B NPV (sel)]")
      + ' & ". C, the answer to why not renovate: " & ' + fm("[Preset C Capex]") + ' & ", " & ' + sfm("[Preset C NPV (sel)]") + ' & "."',
      "The A/B/C layer of the scatter read aloud: how many packages pay back, then A, B and C with capex and net present value in the case in view.")
alt_m("Scatter Cloud",
      '"All " & COUNTROWS ( ALLNOBLANKROW ( Package ) ) & " possible packages, each with its capex, net present value through 2032 (" & [Selected Scenario] & " case), range, payback and initiatives. Show as table lists them."',
      "The 456-dot layer read aloud: what its table holds (keyboard users reach the package details there, not in the hover card).")
alt_m("Rec Nums",
      '"Package A, " & [Selected Scenario] & " case: capex " & [Rec Capex (text)] & ", net present value through 2032 " & [Rec NPV (text)] & ", " & [Rec Run-rate (text)] & " a year by 2032, " & [Rec A Year on Cost (text)] & " a year on cost."',
      "The decision card's four numbers read aloud (build step 6: capex, NPV, a year by 2032, a year on cost).")
alt_m("Waterfall",
      FIDS + shown_parts("[NPV @ 8%]") +
      'RETURN IF ( ISBLANK ( f ), BLANK (), "Where the net present value of package " & [Focus Key] & " comes from, " & [Selected Scenario] & " case: " '
      '& CONCATENATEX ( adj, ' + NAME_OF.format("[@p]") + ' & " " & ' + sfm("[@s]") + ', ", ", ' + NAME_OF.format("[@p]") + ', ASC ) & "; together " & ' + sfm("SUMX ( adj, [@s] )") + ' & "." )',
      "The plan waterfall read aloud, in the chart's order (by name): each initiative's shown NPV and the package total.")
alt_m("Plan Table",
      FIDS + 'RETURN IF ( ISBLANK ( f ), BLANK (), "The ten Goodnight Inn initiatives, package " & [Focus Key] & "\'s first: status, finding answered, capex, profit a year by 2032, net present value, guest-score effect. In package " & [Focus Key] & ": " '
      '& CONCATENATEX ( ids, ' + NAME_OF.format("[@p]") + ', ", ", [@p], ASC ) & "." )',
      "The plan table read aloud: what it lists and which initiatives are in the package in focus.")
alt_m("Cumulative",
      'VAR pb = [Focus Payback Year] VAR s = [Selected Scenario] '
      "VAR lo = CALCULATE ( [Focus Cumulative Net (Low)], 'Date'[Year] = 2032 ) VAR ex = CALCULATE ( [Focus Cumulative Net (Expected)], 'Date'[Year] = 2032 ) VAR hi = CALCULATE ( [Focus Cumulative Net (High)], 'Date'[Year] = 2032 ) "
      'RETURN IF ( ISBLANK ( [Focus Package] ), BLANK (), "Package " & [Focus Key] & ", cumulative net impact 2027 to 2032: " '
      '& IF ( ISBLANK ( pb ), "not positive by 2032 in the " & s & " case", "positive from " & pb & " in the " & s & " case" ) '
      '& ". By 2032: Low " & ' + sfm("lo") + ' & ", Expected " & ' + sfm("ex") + ' & ", High " & ' + sfm("hi") + ' & "." )',
      "The cumulative chart read aloud: payback year in the case in view and the 2032 end points of the three cases.")
alt_m("Rec Held", 'SUBSTITUTE ( SUBSTITUTE ( [Rec Held (text)], "The best way to spend more, A plus the ", "Adding the " ), ", costs ", " costs " )',
      "The held-back card read aloud in under 250 characters (with R3 the canvas sentence runs to 261): same facts, shorter lead-in to the marginal test.")
alt_m("Open Plan", '"Open the plan for package " & [Focus Key]',
      "The plan button's accessible name, which contains its visible label (WCAG 2.5.3 Label in Name; the arrow is left out).")
m("Cumulative Title (text)",
  'VAR pb = [Focus Payback Year] VAR s = [Selected Scenario] RETURN "Cumulative net impact of A, $M: " & IF ( ISBLANK ( pb ), "not positive by 2032 in the " & s & " case", "positive from " & pb & " in the " & s & " case" )',
  TXT, C9, "Plan state chart title with the payback year: the year axis does not fit the 88 px chart (pass-3 review: the crossing was unreadable).")

# ================================================================ feedback round 4 (12-feedbackronde-4.md, 10 Nov)
# Björn's review of the 9 Nov renders: title = the finding, one supporting sentence; the P2 panel in three states
# (rec: the recommendation A; alts: B and C, considered and not recommended; build: build your own plan); the
# package tooltip with a table of the moves; a little more orange, within the kit's signal role.
C12 = "12 Build your own"
C13 = "13 Round 4 copy"
CUM32 = lambda k: f"CALCULATE ( [Preset {k} Cumulative Net (sel)], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2032 )"  # noqa: E731

# ---- the recommendation in one sentence (Rec Answers, Rec Held and Rec Rules leave the canvas; their alt texts stay)
m("Rec Note (text)",
  REC_IDS + f"VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR budget = {BUDGET_GI} "
  'VAR fs = CONCATENATEX ( aIds, LOOKUPVALUE ( InvestmentProjects[Answers Finding], InvestmentProjects[ProjectID], [@p] ), ", ", [@p], ASC ) '
  'VAR k = COUNTROWS ( aIds ) VAR word = SWITCH ( k, 2, "both", 3, "all three", 4, "all four", "all " & k ) '
  'VAR live = FORMAT ( CALCULATE ( MAX ( InvestmentProjects[Completion Date] ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] IN aIds ), "mmm yyyy" ) '
  'VAR others = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" && NOT ( InvestmentProjects[ProjectID] IN aIds ) ), "@p", InvestmentProjects[ProjectID] ) '
  'VAR hiPos = COUNTROWS ( FILTER ( others, VAR p = [@p] RETURN ROUND ( CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p, Scenario[Scenario] = "High" ) / 100000, 0 ) >= 0 ) ) + 0 '
  'RETURN "Each move answers a finding on The Brand Review page (" & fs & "). The other " & ' + fm("budget - cap") + ' & " waits until " & word & " are live in " & live & IF ( hiPos = 0, ", because no further move pays back by 2032.", "." )',
  TXT, C13, "The recommendation's one supporting sentence: which findings the moves answer, the budget held back and until when, and why nothing else is funded now.")
m("Guide (text)",
  'VAR n = COUNTROWS ( ALLNOBLANKROW ( Package ) ) VAR k = CALCULATE ( COUNTROWS ( InvestmentProjects ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" ) '
  f'VAR budget = {BUDGET_GI} '
  # round 9: two lines, not three (a communication page; the dots themselves are the explanation)
  'RETURN "Each dot is one of " & n & " possible packages: a mix of the " & k & " moves on offer within the " & ' + fm("budget") + ' & " budget (at least 3 moves, 1 of them growth). '
  'Capex across, NPV through 2032 up; above the line it pays back by 2032."',
  TXT, C13, "The reading guide above the scatter (feedback round 4: 'what am I looking at' before the dots; round 5: say what the 456 are, combinations within the budget; 12 Nov, night: the hover instruction is the tag on the tile).")


# ---- B and C: why considered, why not picked (one sentence each), on the same variables as Alt B / Alt C
def altvars(k):
    return (REC_IDS + f'VAR x = [Preset {k} Package] '
            'VAR xIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = x ), "@p", PackageProject[ProjectID] ) '
            'VAR added = CONCATENATEX ( FILTER ( xIds, NOT ( [@p] IN aIds ) ), SUBSTITUTE ( LOWER ( ' + NAME_OF.format("[@p]") + ' ), "refresh 10 oldest", "refresh of the 10 oldest hotels" ), " and ", [@p], ASC ) '
            'VAR dropped = CONCATENATEX ( FILTER ( aIds, NOT ( [@p] IN xIds ) ), LOWER ( ' + NAME_OF.format("[@p]") + ' ), " and ", [@p], ASC ) '
            'VAR capA = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR capX = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
            'VAR npvA = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR npvX = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
            'VAR rA = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR rX = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) ')


m("Alt B Why (text)",
  altvars("B") + 'RETURN IF ( ISBLANK ( x ), BLANK (), "Considered: it swaps the " & dropped & " for the " & added & IF ( rX > rA, ", a guest-score effect in " & rX & " hotels instead of " & rA, "" ) & "." )',
  TXT, C13, "B, why it was considered: the swap against A and the wider guest-score reach.")
m("Alt B WhyNot (text)",
  altvars("B") + 'VAR pbA = [Preset A Payback Year] VAR pbX = [Preset B Payback Year] '
  'VAR d = ROUND ( npvA / 100000, 0 ) - ROUND ( npvX / 100000, 0 ) '
  'RETURN IF ( ISBLANK ( x ), BLANK (), "Not picked: " & ' + fm("capX - capA") + ' & " more capex than A for " & FORMAT ( ABS ( d ) / 10, "$0.0" ) & "M" '
  '& IF ( d > 0, " less NPV", IF ( d = 0, " no more NPV", " more NPV, but a later payback" ) ) '
  '& IF ( ISBLANK ( pbX ) && NOT ISBLANK ( pbA ), " (B is not cash positive by 2032)", IF ( pbX > pbA, " (cash positive in " & pbX & ", A in " & pbA & ")", "" ) ) & "." )',
  TXT, C13, "B, why it was not picked (round 5, Björn): purely the capex-to-NPV mix, A is simply better; the NPV gap from the shown (rounded) figures, so it matches the cards; scenario in view.")
m("Alt C Why (text)",
  altvars("C") + 'RETURN IF ( ISBLANK ( x ), BLANK (), "Considered: the " & added & " is the one move aimed at NPS (F3)." )',
  TXT, C13, "C, why it is shown (round 5, Björn): a strategic investment aimed at NPS, the answer to 'why not renovate?' (08-verbeterplan V1).")
m("Alt C WhyNot (text)",
  altvars("C") + 'VAR hiX = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) '
  'VAR allNeg = ROUND ( CALCULATE ( MAX ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) / 100000, 0 ) < 0 '
  '&& ROUND ( CALCULATE ( MAX ( Package[NPV Expected] ), REMOVEFILTERS ( Package ), Package[PackageID] = x ) / 100000, 0 ) < 0 && ROUND ( hiX / 100000, 0 ) < 0 '
  'RETURN IF ( ISBLANK ( x ), BLANK (), "Not picked: NPV " & ' + sfm("npvX") + ' & IF ( allNeg, ", below zero in every case, even High (" & ' + sfm("hiX") + ' & ").", '
  'IF ( ROUND ( npvX / 100000, 0 ) < 0, ", not paying back by 2032 in this case.", ", though it pays back by 2032 in this case." ) ) )',
  # FinalV3 step 4 (R-P2-10, P-8 check 4): its old release rule ("... once A has ..., or if NPS falls below 0") is gone;
  # Gate Rule (text) is the only one. The measure retires with its card in step 8.
  TXT, C13, "C, why it was not picked (round 5, Björn): not the financial risk to take now, below zero in every case (guarded).")
for k in "BC":
    m(f"Pkg Label {k} (text)", f'LOOKUPVALUE ( PlanSelector[Label], PlanSelector[Key], "{k}" )', TXT, C13, f"Card title of package {k}: its name and role, from PlanSelector.")


# ---- per preset package: cumulative line, payback, texts, and B's and C's waterfall parts
def pids(k):
    return f'VAR f = [Preset {k} Package] VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = f ), "@p", PackageProject[ProjectID] ) '


CUM_SEL = ("VAR s = [Selected Scenario] VAR y = MAX ( 'Date'[Year] ) RETURN IF ( ISBLANK ( f ), BLANK (), CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
           "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) )")
PAYBACK = ("VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), \"@c\", VAR y = [Value] RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
           "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) ) RETURN IF ( ISBLANK ( f ), BLANK (), MINX ( FILTER ( t, [@c] >= 0 ), [Value] ) )")
for k in "ABC":
    m(f"Preset {k} Cumulative Net (sel)", pids(k) + CUM_SEL, SUSDM, C9, f"Cumulative net impact of package {k}, undiscounted 2025 dollars, scenario in view (the comparer lines).")


    m(f"Preset {k} Payback Year", pids(k) + PAYBACK, "0", C9, f"First year the cumulative net of package {k} turns positive, scenario in view; blank when not by 2032.")
    m(f"Preset {k} Capex (text)", f"VAR f = [Preset {k} Package] RETURN IF ( ISBLANK ( f ), BLANK (), " + fm(f"[Preset {k} Capex]") + " )", TXT, C9, f"Capex of package {k} as text.")
    m(f"Preset {k} NPV (text)", f"VAR f = [Preset {k} Package] RETURN IF ( ISBLANK ( f ), BLANK (), " + sfm(f"[Preset {k} NPV (sel)]") + " )", TXT, C9, f"NPV through 2032 of package {k}, scenario in view, as text.")

# Round 9: the year tooltip (tt-year) the three cumulative charts share: the hovered year's cumulative net impact of A in
# the three cases, then A, B, C and the plan being built in the case in view. The hovered Date[Year] is the page's filter.
def _cum_fixed(scn):
    return ("VAR y = MAX ( 'Date'[Year] ) RETURN IF ( ISBLANK ( f ), BLANK (), CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
            f"REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = \"{scn}\", TREATAS ( ids, ProjectCashflow[ProjectID] ) ) )")


for scn in ("Low", "Expected", "High"):
    m(f"TT Year A ({scn})", pids("A") + _cum_fixed(scn), SUSDM, C9, f"Year tooltip: cumulative net impact of package A to the end of the hovered year, {scn} case.")
    m(f"TT Year A {scn} (text)", sfm(f"[TT Year A ({scn})]"), TXT, C9, f"Year tooltip: package A's cumulative net impact in the {scn} case, as text.")
for k in "ABC":
    m(f"TT Year {k} (text)", sfm(f"[Preset {k} Cumulative Net (sel)]"), TXT, C9, f"Year tooltip: package {k}'s cumulative net impact to the end of the hovered year, case in view, as text.")
m("TT Year Plan (text)", 'IF ( [Build Count] = 0, "none yet", ' + sfm("[Build Cumulative Net (sel)]") + " )", TXT, C9,
  "Year tooltip: the plan being built, cumulative net impact to the end of the hovered year, case in view; 'none yet' before a move is picked.")
m("TT Year Title (text)", "VAR y = MAX ( 'Date'[Year] ) RETURN \"At the end of \" & y", TXT, C9, "Year tooltip title: the hovered year.")
m("TT Year All Title (text)", 'VAR s = [Selected Scenario] RETURN "A, B, C and your plan in the " & s & " case"', TXT, C9, "Year tooltip, second card's title: the case in view.")
alt_m("TT Year A", 'VAR y = MAX ( \'Date\'[Year] ) RETURN "Package A, cumulative net impact to the end of " & y & ": Low " & [TT Year A Low (text)] & ", Expected " & [TT Year A Expected (text)] & ", High " & [TT Year A High (text)] & "."',
      "The year tooltip's first card read aloud.")
alt_m("TT Year All", 'VAR y = MAX ( \'Date\'[Year] ) VAR s = [Selected Scenario] RETURN "Cumulative net impact to the end of " & y & ", " & s & " case: A " & [TT Year A (text)] & ", B " & [TT Year B (text)] & ", C " & [TT Year C (text)] & ", your plan " & [TT Year Plan (text)] & "."',
      "The year tooltip's second card read aloud.")
for k in "BC":
    m(f"Preset {k} Payback (text)", f'VAR f = [Preset {k} Package] VAR pb = [Preset {k} Payback Year] RETURN IF ( ISBLANK ( f ), BLANK (), IF ( ISBLANK ( pb ), "Not cash positive by 2032 in the ", "Cash positive from " & pb & " in the " ) & [Selected Scenario] & " case" )',
      TXT, C13, f"Package {k}'s payback line on its card (undiscounted cumulative), scenario in view.")
    m(f"Preset {k} Project Flag", pids(k) + "RETURN IF ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) IN ids, 1, 0 )", "0", C9, f"1 for an initiative inside package {k} (visual filter of its waterfall).")
    m(f"Preset {k} Project NPV (shown)", pids(k) + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( FILTER ( adj, [@p] IN VALUES ( InvestmentProjects[ProjectID] ) ), [@s] )", SUSDM, C9,
      f"Waterfall of package {k}: each initiative's NPV, rounded to $0.1M so the bars add up to the shown total.")
    m(f"Preset {k} WF Y End", pids(k) + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( adj, IF ( [@s] > 0, [@s], 0 ) ) * 1.3 + 500000", "0", C9, f"Value axis end of package {k}'s waterfall.")
    m(f"Preset {k} WF Y Start", pids(k) + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( adj, IF ( [@s] < 0, [@s], 0 ) ) * 1.3 - 500000", "0", C9, f"Value axis start of package {k}'s waterfall.")

# ---- build your own plan (C12): the selection lives on the disconnected BuildMove table. Every Build measure reads it
# through ALLSELECTED, so a row of the waterfall (grouped by BuildMove) still sees the whole selection, and an
# unfiltered table (nothing picked) counts as empty, not as all ten.
BACT = "VAR act = CALCULATE ( ISFILTERED ( BuildMove[ProjectID] ) || ISFILTERED ( BuildMove[Short Name] ) || ISFILTERED ( BuildMove[Sort] ), ALLSELECTED ( BuildMove ) ) "
BIDS = BACT + 'VAR ids = SELECTCOLUMNS ( FILTER ( CALCULATETABLE ( VALUES ( BuildMove[ProjectID] ), ALLSELECTED ( BuildMove ) ), act ), "@p", BuildMove[ProjectID] ) VAR n = COUNTROWS ( ids ) + 0 '
BTREAT = "REMOVEFILTERS ( InvestmentProjects ), TREATAS ( ids, InvestmentProjects[ProjectID] )"
m("Build Count", BIDS + "RETURN n", "0", C12, "Moves in the plan being built (0 when nothing is picked).")
m("Build Capex", BIDS + f"RETURN IF ( n = 0, BLANK (), CALCULATE ( SUM ( InvestmentProjects[CapexUSD] ), {BTREAT} ) )", USDM1, C12, "Capex of the plan being built.")
m("Build Growth", BIDS + f'RETURN IF ( n = 0, BLANK (), CALCULATE ( COUNTROWS ( InvestmentProjects ), {BTREAT}, InvestmentProjects[GrowthInitiative] = "Yes" ) + 0 )', "0", C12, "Growth initiatives in the plan being built (dataset flag).")
m("Build NPV (sel)", BIDS + f"RETURN IF ( n = 0, BLANK (), CALCULATE ( [NPV @ 8%], {BTREAT} ) )", SUSDM, C12, "NPV through 2032 of the plan being built, scenario in view (sum of its moves: the dataset gives no interaction effects).")
for scn in ("Low", "High"):
    m(f"Build NPV {scn}", BIDS + f'RETURN IF ( n = 0, BLANK (), CALCULATE ( [NPV @ 8%], {BTREAT}, Scenario[Scenario] = "{scn}" ) )', SUSDM, C12, f"NPV of the plan being built, {scn} scenario.")
m("Build Live (text)", BIDS + "RETURN IF ( n = 0, BLANK (), FORMAT ( CALCULATE ( MAX ( InvestmentProjects[Completion Date] ), " + BTREAT + ' ), "mmm yyyy", "en-US" ) )', TXT, C12, "Month the last move of the plan being built goes live.")
BOVER = BIDS + f"VAR cap = COALESCE ( [Build Capex], 0 ) VAR budget = {BUDGET_GI} VAR over = n > 0 && cap > budget "
# FinalV2 (plan 15 S2): the build waterfall's muted title: a waiting note while nothing is picked (the $0 rest bar then reads
# as a waiting place, not a fault), the rec waterfall's wording once moves are in
m("Build WF Note (text)", BOVER + 'RETURN IF ( n = 0, "Pick moves on the left; your plan appears here.", "Where your NPV comes from, $M through 2032 (" & [Selected Scenario] & ")" )',
  TXT, C12, "Build waterfall title: the waiting note of the empty state, else where the plan's NPV comes from, scenario in view.")
m("Build Title (text)", BOVER + 'RETURN IF ( n = 0, "Nothing picked yet", IF ( over, "Over the " & ' + fm("budget") + ' & " budget by " & ' + fm("cap - budget") + ', '
  '"Your plan: " & n & IF ( n = 1, " move", " moves" ) & ", live by " & [Build Live (text)] ) )', TXT, C12,
  "Title of the your-plan tile; its empty state asks for a first move; over the budget it becomes the alarm (round 5, Björn: a big alarm when the selection passes the budget).")
m("Build Title Fill", BOVER + f'RETURN IF ( over, "{SIGNAL_MARK}", "{SURFACE}" )', TXT, C12, "Fill of the your-plan title row: Tangerine while the picked capex passes the budget (the alarm band), white otherwise. Paired with Build Title Ink, branch for branch.")
m("Build Title Ink", BOVER + f'RETURN IF ( over, "{SURFACE}", "{INK}" )', TXT, C12, "Text of the your-plan title row: white on the Tangerine alarm band (18 pt: 4.2:1, WCAG large text), Night otherwise.")
m("Build Capex (text)", fm("COALESCE ( [Build Capex], 0 )"), TXT, C12, "Capex of the plan being built as text ($0.0M when empty).")
m("Build NPV (text)", sfm("COALESCE ( [Build NPV (sel)], 0 )"), TXT, C12, "NPV of the plan being built as text.")
m("Build Range (text)", "VAR lo = COALESCE ( [Build NPV Low], 0 ) VAR hi = COALESCE ( [Build NPV High], 0 ) RETURN " + sfm("lo") + ' & " to " & ' + sfm("hi"),
  TXT, C12, "NPV of the plan being built from the Low to the High scenario, the unit on both ends (R-G1).")
BRULES = (BIDS + f"VAR g = COALESCE ( [Build Growth], 0 ) VAR cap = COALESCE ( [Build Capex], 0 ) VAR budget = {BUDGET_GI} "
          'VAR kiosk = "GI-02" IN ids VAR app = "GI-01" IN ids VAR broken = n > 0 && ( n < 3 || g < 1 || cap > budget || ( kiosk && NOT app ) ) ')
m("Build Valid (text)",
  BRULES + 'VAR issues = IF ( n < 3, "at least 3 moves; ", "" ) & IF ( g < 1, "at least 1 growth move; ", "" ) & IF ( cap > budget, "over the budget; ", "" ) & IF ( kiosk && NOT app, "the kiosks need the booking app; ", "" ) '
  # the empty state (R-B-2, doc 22 section 4): the rules and what appears here, one sentence in one place
  'RETURN IF ( n = 0, "Pick at least three moves, one of them growth, within " & ' + fm("budget") + ' & ". Your plan appears here and is compared with A below.", IF ( NOT broken, "Within the rules: " & n & " moves, " & g & " growth, " & ' + fm("cap") + ' & " of " & ' + fm("budget") + ' & ".", '
  '"Not yet within the rules: " & LEFT ( issues, LEN ( issues ) - 2 ) & "." ) )',
  TXT, C12, "The contest rules against the plan being built: at least 3 moves, 1 growth, within budget, kiosks need the app.")
m("Build Valid Color", BRULES + f'RETURN IF ( broken, "{BAD}", "{INK2}" )', TXT, C12, "Burnt Tangerine while a rule is broken, Dusk otherwise (the sentence says which).")
m("Build Cumulative Net (sel)",
  BIDS + "VAR s = [Selected Scenario] VAR y = MAX ( 'Date'[Year] ) RETURN IF ( n = 0, BLANK (), CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
  "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) )",
  SUSDM, C12, "Cumulative net impact of the plan being built, undiscounted 2025 dollars, scenario in view.")
m("Build Payback Year",
  BIDS + "VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), \"@c\", VAR y = [Value] RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
  "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) ) RETURN IF ( n = 0, BLANK (), MINX ( FILTER ( t, [@c] >= 0 ), [Value] ) )",
  "0", C12, "First year the cumulative net of the plan being built turns positive; blank when not by 2032 or when empty.")
m("Build Row Flag", BIDS + "VAR me = SELECTEDVALUE ( BuildMove[ProjectID] ) RETURN IF ( me IN ids, 1, 0 )", "0", C12, "1 for a move in the plan being built (visual filter of its waterfall).")
m("Build Project NPV (shown)", BIDS + shown_parts("[NPV @ 8%]") + "VAR me = SELECTEDVALUE ( BuildMove[ProjectID] ) RETURN IF ( n = 0, BLANK (), SUMX ( FILTER ( adj, [@p] = me ), [@s] ) )", SUSDM, C12,
  "Waterfall of the plan being built: each move's NPV, rounded to $0.1M so the bars add up to the shown total.")
m("Build WF Y End", BIDS + shown_parts("[NPV @ 8%]") + "RETURN IF ( n = 0, 1000000, SUMX ( adj, IF ( [@s] > 0, [@s], 0 ) ) * 1.6 + 1000000 )", "0", C12, "Value axis end of the build waterfall (FinalV2: 1.6 and $1M headroom, the 160 px chart carries a title row and the labels sit outside the bars).")
m("Build WF Y Start", BIDS + shown_parts("[NPV @ 8%]") + "RETURN IF ( n = 0, -1000000, SUMX ( adj, IF ( [@s] < 0, [@s], 0 ) ) * 1.6 - 1000000 )", "0", C12, "Value axis start of the build waterfall (FinalV2: 1.6 and $1M headroom).")
m("Build Point Size", "IF ( ISBLANK ( [Build NPV (sel)] ), BLANK (), 7 )", "0", C12, "Marker size of the your-plan dot on the small scatter; blank (no dot) while nothing is picked.")
m("Cmp Build Title (text)",
  BIDS + f"VAR s = [Selected Scenario] VAR a32 = {CUM32('A')} VAR y32 = CALCULATE ( [Build Cumulative Net (sel)], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2032 ) VAR pb = [Build Payback Year] "
  'RETURN IF ( n = 0, "Your plan against A, $M (" & s & " case)", "Your plan against A, $M (" & s & " case): yours ends " & IF ( ROUND ( ( y32 - a32 ) / 100000, 0 ) = 0, "level with A", IF ( y32 > a32, "ahead of A by ", "behind A by " ) & ' + fm("ABS ( y32 - a32 )") + ' )'
  + ' & " in 2032" & IF ( ISBLANK ( pb ), " and is not cash positive by 2032", ", cash positive from " & pb ) )',
  TXT, C12, "Title of the comparer in the build state: your plan against A by 2032 and its payback, scenario in view.")
# the selector's dataset: one row per BuildMove, never filtered by its own selection
# FinalV3 step 4: the same row measures serve the hero table (rows on InvestmentProjects) and the selector table (rows on
# BuildMove); the hero's row wins, the selector's table filters no project, so there the BuildMove row is read
MOVE_P = "VAR p = COALESCE ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ), SELECTEDVALUE ( BuildMove[ProjectID] ) ) "
# FinalV2 (plan 15 N1): one decimal in the selector ($4.25M prints $4.3M), one format down the column; fmc stays where parts must add up
m("Move Capex (text)", MOVE_P + 'RETURN IF ( ISBLANK ( p ), BLANK (), ' + fm("LOOKUPVALUE ( InvestmentProjects[CapexUSD], InvestmentProjects[ProjectID], p )") + ' )', TXT, C12, "Selector row: capex of the move, one decimal (fm).")
m("Move NPV (num)", MOVE_P + "RETURN IF ( ISBLANK ( p ), BLANK (), CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) )", SUSDM, C12, "Selector row: NPV through 2032 of the move alone, scenario in view.")
m("Move NPV (text)", "VAR v = [Move NPV (num)] RETURN IF ( ISBLANK ( v ), BLANK (), " + sfm("v") + " )", TXT, C12, "Selector row: the move's NPV as text.")
m("Move Answers (text)", MOVE_P + 'RETURN IF ( ISBLANK ( p ), BLANK (), LOOKUPVALUE ( MoveDecision[Finding], MoveDecision[ProjectID], p ) & IF ( LOOKUPVALUE ( InvestmentProjects[GrowthInitiative], InvestmentProjects[ProjectID], p ) = "Yes", " · growth", "" ) )',
  TXT, C12, "Hero and selector row: the page-1 finding the move answers (MoveDecision, doc 21 10.3) and the growth flag.")
m("Move Case (text)", "[Selected Scenario]", TXT, C12, "Selector header: the scenario in view.")
m("Move Capex (num)", MOVE_P + "RETURN IF ( ISBLANK ( p ), BLANK (), LOOKUPVALUE ( InvestmentProjects[CapexUSD], InvestmentProjects[ProjectID], p ) )", "0", C12, "Selector row: capex of the move as a number (the footer sums the picked rows).")
m("Move Budget (num)", BUDGET_GI, "0", C12, "Selector: the Goodnight Inn budget, repeated on every row (the footer's cap).")

# ---- the package tooltip: the moves table and the case tag
TT_IDS = TT_ID + 'VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = pkg ), "@p", PackageProject[ProjectID] ) '
m("TT Moves Label (text)", TT_IDS + 'RETURN IF ( ISBLANK ( pkg ), BLANK (), "In this package: " & COUNTROWS ( ids ) & " moves" )', TXT, C10, "Tooltip: the line above the moves list.")
m("TT Not Included (text)",
  TT_IDS + 'VAR t = FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" && NOT ( InvestmentProjects[ProjectID] IN ids ) ) '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), IF ( COUNTROWS ( t ) = 0, "Every move is in it.", "Not in it: " & CONCATENATEX ( t, InvestmentProjects[Short Name], ", ", InvestmentProjects[ProjectID], ASC ) & "." ) )',
  TXT, C10, "Tooltip (alt text only since round 6): the moves the hovered package leaves out.")
m("TT Kicker (text)",
  TT_ID + 'VAR k = LOOKUPVALUE ( Package[Preset], Package[PackageID], pkg ) '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), "PACKAGE" & IF ( k <> "", "  " & k, "" ) & "  ·  " & UPPER ( [Selected Scenario] ) & " CASE" )',
  TXT, C10, "Tooltip kicker on the night banner (round 7): the package's letter when it has one and the case in view, in the page's eyebrow style.")

# ---- the package tooltip as an evidence card (round 6, second opinion of 10 Nov): the three numeric claims drawn as
# small SVGs in image visuals, the pattern of the chips above. Conventions (Kerry Kolosko's SVG-in-DAX notes,
# CREDITS.md): '%23' for '#', single quotes inside the SVG, 'data:image/svg+xml;utf8,' in front, coordinates through
# FORMAT ( x, "0.0", "en-US" ) so a comma locale never breaks one. Every label 16 px (the floor). A tableEx was tried
# for the moves with an image column: it squares the image cell to the column width and ignored the hidden sort key,
# so the list is one SVG too (render 10 Nov). Each SVG is decorative and has a text twin.
HAIR = "#E3DFD3"  # Seam, the hairline of the hollow grid chips
SVG_FONT = "font-family='Segoe UI, Arial, sans-serif' font-size='16'"
NUM = lambda x: f'FORMAT ( {x}, "0.0", "en-US" )'  # noqa: E731
SVG_OPEN = lambda w, h: f"\"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}'>\""  # noqa: E731
HX = lambda hexv: hexv.replace("#", "%23")  # noqa: E731  (the SVG colour form of a hex; PCT stays the percent format string)
TTW = 416  # the inner width of a tooltip card (480 - 2 x 32), round 10
TTL = 416  # the moves list, the same width

# the range bar, 416 x 72 (FinalV2, plan 15 M1; round 10: 416 wide): one fixed axis for every package (min Low .. max High
# over all 456, rounded out to $5M), the A/B/C ticks with their letters, the hovered package's Low-High band with its Expected
# dot, the break-even line in Night, the Low and High numbers under everything. Collision rules (review 12 Nov, M1: on A the
# letters A and B, their ticks and "High +12.7" were one clump):
#   1. the Low and High labels have a row of their own (baseline 66, 5 px under B's letter) under the ticks, the band, the dot, so
#      nothing can stand on them; Low ends at the band start, High begins at the band end and swaps to the right
#      edge when it does not fit; neither is ever clamped under a tick (the round-10 clamp did exactly that);
#   2. letters stand 24 px apart or not side by side: A and B within 24 px puts A above the band and B under it, each with
#      its own tick: A's from its letter down to the band's top edge, B's from the band's bottom edge down to its letter
#      (baseline 50, clear of the labels' row), so the two ticks never overlap even 2 px apart;
#   3. C is drawn only 24 px or more from the break-even tick and from A and B.
# TT Range (text) is its text twin and names the line.
RANGE_H = 72
RANGE_AXIS = ("VAR dMin = FLOOR ( MINX ( ALL ( Package ), Package[NPV Low] ) / 5000000, 1 ) * 5000000 "
              "VAR dMax = CEILING ( MAXX ( ALL ( Package ), Package[NPV High] ) / 5000000, 1 ) * 5000000 "
              f"VAR k = {TTW - 16} / ( dMax - dMin ) ")
_tick_up = lambda xv, letter, col: ('"<line x1=\'" & ' + NUM(xv) + ' & "\' x2=\'" & ' + NUM(xv) + ' & "\' y1=\'15\' y2=\'26\' stroke=\'' + col + '\' stroke-width=\'2\'/>'  # noqa: E731
                                    '<text x=\'" & ' + NUM(xv) + ' & "\' y=\'13\' text-anchor=\'middle\' ' + SVG_FONT + ' font-weight=\'600\' fill=\'' + col + '\'>' + letter + '</text>"')
_tick_down = lambda xv, letter, col: ('"<line x1=\'" & ' + NUM(xv) + ' & "\' x2=\'" & ' + NUM(xv) + ' & "\' y1=\'34\' y2=\'38\' stroke=\'' + col + '\' stroke-width=\'2\'/>'  # noqa: E731
                                      '<text x=\'" & ' + NUM(xv) + ' & "\' y=\'50\' text-anchor=\'middle\' ' + SVG_FONT + ' font-weight=\'600\' fill=\'' + col + '\'>' + letter + '</text>"')
m("TT Range SVG",
  TT_ID + RANGE_AXIS +
  "VAR lo = LOOKUPVALUE ( Package[NPV Low], Package[PackageID], pkg ) VAR ex = LOOKUPVALUE ( Package[NPV Expected], Package[PackageID], pkg ) VAR hi = LOOKUPVALUE ( Package[NPV High], Package[PackageID], pkg ) "
  "VAR x0 = 8 + ( 0 - dMin ) * k VAR xL = 8 + ( lo - dMin ) * k VAR xE = 8 + ( ex - dMin ) * k VAR xH = 8 + ( hi - dMin ) * k "
  'VAR xA = 8 + ( LOOKUPVALUE ( Package[NPV Expected], Package[Preset], "A" ) - dMin ) * k VAR xB = 8 + ( LOOKUPVALUE ( Package[NPV Expected], Package[Preset], "B" ) - dMin ) * k '
  'VAR xC = 8 + ( LOOKUPVALUE ( Package[NPV Expected], Package[Preset], "C" ) - dMin ) * k '
  "VAR bDown = ABS ( xA - xB ) < 24 "
  "VAR cShown = ABS ( xC - x0 ) >= 24 && ABS ( xC - xA ) >= 24 && ABS ( xC - xB ) >= 24 "
  'VAR dotc = IF ( ROUND ( ex / 100000, 0 ) >= 0, "' + HX(ACCENT) + '", "' + HX(BAD) + '" ) '
  # the labels: Low ends at the band start (or starts at the left edge when the band starts within 80 px of it); High
  # starts 4 px after the band end, or ends at the right edge when 88 px do not remain
  'VAR lowAnchor = IF ( xL < 80, "start", "end" ) VAR xLo = IF ( xL < 80, 0, xL ) '
  'VAR highAnchor = IF ( xH + 88 > ' + str(TTW) + ', "end", "start" ) VAR xHi = IF ( xH + 88 > ' + str(TTW) + ', ' + str(TTW) + ', xH + 4 ) '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), "data:image/svg+xml;utf8," & ' + SVG_OPEN(TTW, RANGE_H) + ' '
  '& "<line x1=\'1\' x2=\'1\' y1=\'2\' y2=\'14\' stroke=\'' + HX(INK) + '\' stroke-width=\'1.5\'/><text x=\'6\' y=\'13\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>break-even</text>" '
  '& ' + _tick_up("xA", "A", HX(ACCENT)) + ' & IF ( bDown, ' + _tick_down("xB", "B", HX(INK)) + ', ' + _tick_up("xB", "B", HX(INK)) + ' ) & IF ( cShown, ' + _tick_up("xC", "C", HX(INK)) + ', "" ) '
  '& "<rect x=\'" & ' + NUM("xL") + ' & "\' y=\'26\' width=\'" & ' + NUM("xH - xL") + ' & "\' height=\'8\' rx=\'4\' fill=\'' + HX(SLATE) + '\' fill-opacity=\'0.45\'/>" '
  '& "<line x1=\'" & ' + NUM("x0") + ' & "\' x2=\'" & ' + NUM("x0") + ' & "\' y1=\'15\' y2=\'37\' stroke=\'' + HX(INK) + '\' stroke-width=\'1.5\'/>" '
  '& "<circle cx=\'" & ' + NUM("xE") + ' & "\' cy=\'30\' r=\'5\' fill=\'" & dotc & "\' stroke=\'' + HX(SURFACE) + '\' stroke-width=\'2\'/>" '
  '& "<text x=\'" & ' + NUM("xLo") + ' & "\' y=\'66\' text-anchor=\'" & lowAnchor & "\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>Low " & ' + signed("lo", 'FORMAT ( ABS ( lo ) / 1000000, "0.0", "en-US" )') + ' & "</text>" '
  '& "<text x=\'" & ' + NUM("xHi") + ' & "\' y=\'66\' text-anchor=\'" & highAnchor & "\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>High " & ' + signed("hi", 'FORMAT ( ABS ( hi ) / 1000000, "0.0", "en-US" )') + ' & "</text></svg>" )',
  TXT, C10, "Tooltip: the hovered package's Low-High band and Expected dot on one fixed NPV axis shared by every package, "
            "the A/B/C ticks (B under the band when it stands within 24 px of A; C only when clear of break-even, A and B), the break-even line and the Low and High "
            "numbers on their own row; decorative, TT Range (text) is its text twin (keyboard tooltip, alt text).")
IMAGE_MEASURES.add("TT Range SVG")

# the moves list, 376 x 180 (round 10: 440 px tooltips, row pitch 18; round 7, Björn: leaner): a header row, one row per move (positives first, the sinker
# last), a totals row; columns Move | Capex | NPV, the NPV in Burnt Tangerine below zero. The waterfall bars and the
# Answers column of round 6 left with the move grid: the numbers add up without them.
TT_RUN = (TT_IDS + shown_parts("[NPV @ 8%]", 10000) +
          "VAR tot = SUMX ( adj, [@s] ) VAR cap = LOOKUPVALUE ( Package[CapexUSD], Package[PackageID], pkg ) VAR nrows = COUNTROWS ( adj ) ")
_cell = lambda x, anchor, fill, inner, extra="", yv="y": ('"<text x=\'' + str(x) + '\' y=\'" & ( ' + yv + ' + 14 ) & "\' text-anchor=\'' + anchor + '\' ' + SVG_FONT + extra + ' fill=\'' + fill + '\'>" & ' + inner + ' & "</text>"')  # noqa: E731
_npv_fill = lambda expr: "fill='\" & IF ( " + expr + " < 0, \"" + HX(BAD) + "\", \"" + HX(INK) + "\" ) & \"'"  # noqa: E731
_capex = 'LOOKUPVALUE ( InvestmentProjects[CapexUSD], InvestmentProjects[ProjectID], [@p] )'
m("TT Moves SVG",
  TT_RUN +
  # one row per move: y from its rank (positives first); 'rows' is a reserved word in DAX, hence moveRows
  'VAR moveRows = CONCATENATEX ( adj, VAR y = 18 * RANKX ( adj, [@s] + VALUE ( RIGHT ( [@p], 2 ) ) * 0.0000001, , DESC ) RETURN '
  + _cell(0, "start", HX(INK), NAME_OF.format("[@p]")) + ' & ' + _cell(TTL - 96, "end", HX(INK), fm(_capex))
  + ' & ' + _cell(TTL, "end", 'PLACEHOLDER_NPV_COLOUR', sfm("[@s]")).replace("fill='PLACEHOLDER_NPV_COLOUR'", _npv_fill("[@s]")) + ', "" ) '
  # the totals row under the moves (its own VAR name: DAX forbids shadowing the rows' y)
  "VAR yT = 18 * ( nrows + 1 ) "
  'VAR total = ' + _cell(0, "start", HX(INK), '"Total"', " font-weight='600'", "yT") + ' & ' + _cell(TTL - 96, "end", HX(INK), fm("cap"), " font-weight='600'", "yT")
  + ' & ' + _cell(TTL, "end", 'PLACEHOLDER_NPV_COLOUR', sfm("tot"), " font-weight='600'", "yT").replace("fill='PLACEHOLDER_NPV_COLOUR'", _npv_fill("tot")) + ' '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), "data:image/svg+xml;utf8," & ' + SVG_OPEN(TTL, 184) + ' '
  # the header row and its hairline, the hairline over the totals row
  '& "<text x=\'0\' y=\'14\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>Move</text><text x=\'' + str(TTL - 96) + '\' y=\'14\' text-anchor=\'end\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>Capex</text><text x=\'' + str(TTL) + '\' y=\'14\' text-anchor=\'end\' ' + SVG_FONT + ' fill=\'' + HX(INK2) + '\'>NPV</text>" '
  '& "<line x1=\'0\' x2=\'' + str(TTL) + '\' y1=\'17.5\' y2=\'17.5\' stroke=\'' + HX(HAIR) + '\'/>" '
  '& "<line x1=\'0\' x2=\'' + str(TTL) + '\' y1=\'" & ( 18 * ( nrows + 1 ) + 0.5 ) & "\' y2=\'" & ( 18 * ( nrows + 1 ) + 0.5 ) & "\' stroke=\'' + HX(HAIR) + '\'/>" '
  '& moveRows & total & "</svg>" )',
  TXT, C10, "Tooltip: the moves of the hovered package as a list with capex and NPV each (positives first, the sinker last) and a totals row; "
            "the move NPVs are rounded so they add up to the package. Decorative: TT Moves (text) and Alt TT Moves say the same in words.")
IMAGE_MEASURES.add("TT Moves SVG")
m("TT Moves (text)",
  TT_IDS + shown_parts("[NPV @ 8%]", 10000) + 'RETURN IF ( ISBLANK ( pkg ), BLANK (), CONCATENATEX ( adj, ' + NAME_OF.format("[@p]") + ' & " " & ' + sfm("[@s]") + ', "; ", [@s], DESC ) )',
  TXT, C10, "Tooltip text twin of the moves list: each move with its NPV inside the package, positives first (the keyboard layer's tooltip and the alt text).")



# ---- round 6: the findings as a reference on page 2 (chips with a page tooltip each) and hover detail on F3 and F4
C14 = "14 Findings reference and hover detail"
# (12 Nov, night: the F1 to F4 words in the header and their 'Finding Chip' measures left; the moves of A carry the findings, below)

# the F3 band page: grain Hotels[Renovation Age Label] (the hovered bar) within Goodnight Inn (page filter)
BRAND_ALL = f"REMOVEFILTERS ( Hotels ), {gi}"
_w = lambda col: f"CALCULATE ( DIVIDE ( SUMX ( GuestExperience, GuestExperience[{col}] * GuestExperience[SurveyResponses] ), SUM ( GuestExperience[SurveyResponses] ) ), REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 )"  # noqa: E731
m("Band Header (text)",
  'VAR bnd = SELECTEDVALUE ( Hotels[Renovation Age Label] ) RETURN IF ( ISBLANK ( bnd ), BLANK (), bnd & ": " & COUNTROWS ( Hotels ) & " hotels, " & FORMAT ( SUM ( Hotels[Rooms] ), "#,0" ) & " rooms" )',
  TXT, C14, "Header of the F3 band tooltip: the band, its hotels and rooms.")
m("Band vs Brand (text)",
  f'"Goodnight Inn, all hotels, 2025: NPS " & ' + signed(f"CALCULATE ( [NPS (weighted) 2025], {BRAND_ALL} )", f'FORMAT ( ABS ( CALCULATE ( [NPS (weighted) 2025], {BRAND_ALL} ) ), "0.0" )')
  + f' & ", occupancy " & FORMAT ( CALCULATE ( [Occupancy % 2025], {BRAND_ALL} ), "0.0%" ) & ", RevPAR " & FORMAT ( CALCULATE ( [RevPAR 2025], {BRAND_ALL} ), "$#,0.00" )',  # FinalV2 N2: the KPI's decimals
  TXT, C14, "F3 band tooltip: the brand's own 2025 figures under the band's three, the same formatters.")
m("NPS Band (line)", "[NPS (weighted)]", "+0.0;-0.0;0.0", C14, "F3 band tooltip, line: the band's response-weighted NPS by year.")
m("NPS Brand (line)", f"CALCULATE ( [NPS (weighted)], {BRAND_ALL} )", "+0.0;-0.0;0.0", C14, "F3 band tooltip, line: Goodnight Inn's response-weighted NPS by year, every hotel.")
m("Weakest Scores (text)",
  'VAR t = UNION ( ROW ( "@n", "cleanliness", "@v", ' + _w("CleanlinessScore") + ' ), ROW ( "@n", "service", "@v", ' + _w("ServiceScore") + ' ), ROW ( "@n", "room comfort", "@v", ' + _w("RoomComfortScore") + ' ), '
  'ROW ( "@n", "amenities", "@v", ' + _w("AmenitiesScore") + ' ), ROW ( "@n", "value for money", "@v", ' + _w("ValueForMoneyScore") + ' ) ) '
  'RETURN IF ( ISBLANK ( SELECTEDVALUE ( Hotels[Renovation Age Label] ) ), BLANK (), "Weakest guest scores 2025: " & CONCATENATEX ( TOPN ( 2, t, [@v], ASC ), [@n] & " " & FORMAT ( [@v], "0.0" ), ", ", [@v], ASC ) & " (of 10)" )',
  TXT, C14, "F3 band tooltip: the two lowest of the five guest-score dimensions in 2025, response-weighted (what a refresh would have to fix).")
alt_m("Band Nums", '"This band in 2025: NPS " & [NPS 2025 (signed)] & ", occupancy " & FORMAT ( [Occupancy % 2025], "0.0%" ) & ", revenue per available room " & FORMAT ( [RevPAR 2025], "$#,0" ) & "."',
      "The F3 band tooltip's three figures read aloud.")
alt_m("NPS Band Line", f'"Net promoter score by year, 2021 to 2025, this band against the whole brand: the band from " & FORMAT ( [NPS (weighted) 2021], "+0.0;-0.0;0.0" ) & " to " & FORMAT ( [NPS (weighted) 2025], "+0.0;-0.0;0.0" ) '
      f'& ", the brand from " & FORMAT ( CALCULATE ( [NPS (weighted) 2021], {BRAND_ALL} ), "+0.0;-0.0;0.0" ) & " to " & FORMAT ( CALCULATE ( [NPS (weighted) 2025], {BRAND_ALL} ), "+0.0;-0.0;0.0" ) & "."',
      "The F3 band tooltip's line chart read aloud.")

# the F4 hotel page: grain Hotels[Hotel Short Name] (the hovered bar) within Goodnight Inn (page filter)
m("Hotel Header (text)",
  'VAR h = SELECTEDVALUE ( Hotels[Hotel Short Name] ) RETURN IF ( ISBLANK ( h ), BLANK (), h & ", " & LOWER ( SELECTEDVALUE ( Hotels[LocationType] ) ) & ", " & FORMAT ( SUM ( Hotels[Rooms] ), "#,0" ) & " rooms" )',
  TXT, C14, "Header of the F4 hotel tooltip: the hotel, its location type and rooms.")
m("Hotel vs Brand (text)",
  f'"Goodnight Inn, all hotels, 2025: occupancy " & FORMAT ( CALCULATE ( [Occupancy % 2025], {BRAND_ALL} ), "0.0%" ) & ", ADR " & FORMAT ( CALCULATE ( [ADR 2025], {BRAND_ALL} ), "$#,0.00" ) & ", RevPAR " & FORMAT ( CALCULATE ( [RevPAR 2025], {BRAND_ALL} ), "$#,0.00" )',  # FinalV2 N2
  TXT, C14, "F4 hotel tooltip: the brand's own 2025 figures under the hotel's three.")
m("Occupancy Hotel (line)", "[Occupancy %]", PCT, C14, "F4 hotel tooltip, line: the hotel's occupancy by month.")
m("Occupancy Brand (line)", f"CALCULATE ( [Occupancy %], {BRAND_ALL} )", PCT, C14, "F4 hotel tooltip, line: Goodnight Inn's occupancy by month, every hotel.")
m("Segments 2025 (text)",
  'VAR t = ADDCOLUMNS ( VALUES ( GuestSegments[Segment] ), "@s", CALCULATE ( SUM ( GuestSegments[RoomNights] ), REMOVEFILTERS ( \'Date\' ), \'Date\'[Year] = 2025 ) ) VAR tot = SUMX ( t, [@s] ) VAR top3 = TOPN ( 3, t, [@s], DESC ) '  # top is a reserved word in DAX, like rows
  'RETURN IF ( ISBLANK ( SELECTEDVALUE ( Hotels[Hotel Short Name] ) ) || ISBLANK ( tot ), BLANK (), "Room nights 2025: " & CONCATENATEX ( top3, LOWER ( GuestSegments[Segment] ) & " " & FORMAT ( DIVIDE ( [@s], tot ), "0%" ), ", ", [@s], DESC ) '
  '& ", other " & FORMAT ( 1 - DIVIDE ( SUMX ( top3, [@s] ), tot ), "0%" ) )',
  TXT, C14, "F4 hotel tooltip: who fills the hotel, the three largest guest segments by 2025 room nights and the rest.")
alt_m("Hotel Nums", '"This hotel in 2025: occupancy " & FORMAT ( [Occupancy % 2025], "0.0%" ) & ", average daily rate " & FORMAT ( [ADR 2025], "$#,0" ) & ", revenue per available room " & FORMAT ( [RevPAR 2025], "$#,0" ) & "."',
      "The F4 hotel tooltip's three figures read aloud.")
alt_m("Occupancy Hotel Line", f'"Occupancy by month in 2025, this hotel against the whole brand: the hotel averages " & FORMAT ( [Occupancy % 2025], "0.0%" ) & ", the brand " & FORMAT ( CALCULATE ( [Occupancy % 2025], {BRAND_ALL} ), "0.0%" ) & "."',
      "The F4 hotel tooltip's line chart read aloud.")

# ---- FinalV2 follow-up (12 Nov, evening; Björn): the hover signifier and the definitions tooltip. Power BI never changes the
# cursor over a visual that opens a report-page tooltip, so the page itself says where a hover pays: one small ring-i badge in
# Tangerine (a signifier in Don Norman's sense, CREDITS.md) at the same spot on every hover target and nowhere else, a hint in
# the footer row that names it once ('hover for more'), and a Definitions chip in that row whose tooltip page (tt-glossary)
# lists the short words of both pages. The badge is drawn without text, so it renders the same under Publish to Web; the
# hint's words are at the 16 px floor. Its alt text carries the glossary in one breath (Desktop's 250-character limit).
# 12 Nov, night (Björn on the FinalV2 renders: the 16 px ring-i was too small everywhere, its legend 'hover for more' sat far away
# in the header's top-right corner, and the header line was off brand, clumsy and easy to miss). The signifier stays (Don
# Norman's term, CREDITS.md) but it now carries its own label, so no legend is needed: a hover tag, 28 px high, a pill in
# the signal tint with a filled Tangerine disc and a white i, and the instruction in Night ('Hover a bar'), on the card it
# serves. Label the icon instead of explaining it elsewhere: Nielsen's recognition-rather-than-recall heuristic (CREDITS.md).
# The colours are the tooltips' own (orange surface, Night text), so the tag previews what the hover opens. The same pill,
# without words, sits under the two kinds of hover chips (Definitions in the footer row, the moves of A in the
# recommendation tile), whose words are a card on top, so the words are real text and the card takes the hover.
HOVER_TINT = "#FCE6DB"  # kit signal_tint (Burnt Tangerine on it 5.2:1, Night 13.1:1)
TAG_H = 28


def _pill(w):
    """The pill and the disc with the i, the shared ground of every hover tag and chip (shapes only, no text)."""
    return ("<rect width='" + str(w) + "' height='" + str(TAG_H) + "' rx='14' fill='" + HX(HOVER_TINT) + "'/>"
            "<circle cx='14' cy='14' r='10' fill='" + HX(SIGNAL_MARK) + "'/>"
            "<circle cx='14' cy='9.4' r='1.6' fill='%23FFFFFF'/>"
            "<rect x='12.8' y='12.2' width='2.4' height='7.4' rx='1.2' fill='%23FFFFFF'/>")


def _tag_text(x, s, colour=INK, anchor="start"):
    return "<text x='" + str(x) + "' y='19.5' text-anchor='" + anchor + "' " + SVG_FONT + " font-weight='600' fill='" + HX(colour) + "'>" + s + "</text>"


def _svg(w, body):
    return '"data:image/svg+xml;utf8," & ' + SVG_OPEN(w, TAG_H) + ' & "' + body + '</svg>"'


# label, width: the width is the slot's width in opzet-layout.json: 32 px for the disc and the gap, the label as wide as Arial Bold
# sets it (the Mac fallback under Publish to Web; Segoe UI Semibold is narrower), at least 24 px to spare, rounded up to 8.
HOVER_TAGS = (("Bar", "Hover a bar", 144), ("Hotel", "Hover a hotel", 160), ("Dot", "Hover a dot", 144), ("Year", "Hover a year", 152))
for key, label, tw in HOVER_TAGS:
    m(f"Hover Tag {key} SVG", _svg(tw, _pill(tw) + _tag_text(32, label)), TXT, C14,
      f"The hover tag '{label}' ({tw} x {TAG_H} px) on every visual whose {key.lower()}s open a report-page tooltip; decorative, the words say what to hover.")
    IMAGE_MEASURES.add(f"Hover Tag {key} SVG")
m("Definitions Pill SVG", _svg(144, _pill(144)), TXT, C14,
  "The ground of the Definitions chip in the footer row (144 x 28 px): the pill and the disc; the word is the card on top, which takes the hover.")
IMAGE_MEASURES.add("Definitions Pill SVG")
m("Definitions Chip (text)", '"Definitions"', TXT, C14, "The word Definitions on the chip at the right of the footer row of both pages; hovering it opens the definitions tooltip page.")
# 'Revisit the facts' (Björn, 12 Nov, night, on the preview: the three move chips in the recommendation tile were too busy,
# and F4 must stay reachable from page 2): ONE pill in P2's footer row, the disc once, the label, and the four findings as
# hover zones inside it: the code in Burnt Tangerine (as on the P1 kickers) drawn here, the name a transparent card on top
# per zone, which takes the hover and opens tt-f1 to tt-f4. Zone = (finding, x in the pill, width); the code sits at the
# zone's x, the name 26 px further (the card's left padding); widths from Arial Bold metrics with at least 10 px to spare,
# a Warm Grey dot in each 16 px gap. The pill's width and the zones are the slots in opzet-layout.json (z_pill_facts, chip_f1..4).
FINDING_NAMES = (("1", "The margin"), ("2", "The middleman"), ("3", "The fading welcome"), ("4", "Where we are full"))
FACTS_W = 856
FACTS_ZONES = (("1", 160, 124), ("2", 300, 156), ("3", 472, 192), ("4", 680, 168))
_facts = _pill(FACTS_W) + "<text x='32' y='19.5' " + SVG_FONT + " fill='" + HX(INK2) + "'>Revisit the facts</text>"
for j, (k, x, zw) in enumerate(FACTS_ZONES):
    _facts += _tag_text(x, f"F{k}", BAD)
    if j < len(FACTS_ZONES) - 1:
        _facts += "<circle cx='" + str(x + zw + 8) + "' cy='14' r='1.75' fill='" + HX(SLATE) + "'/>"
m("Facts Bar SVG", _svg(FACTS_W, _facts), TXT, C14,
  f"The 'Revisit the facts' pill in P2's footer row ({FACTS_W} x {TAG_H} px): the disc, the label and the codes F1 to F4; the finding names are cards on top, one per zone, which open the finding's tooltip page.")
IMAGE_MEASURES.add("Facts Bar SVG")
for k, nm in FINDING_NAMES:
    m(f"Facts Chip F{k} (text)", f'"{nm}"', TXT, C14, f"The name of finding F{k} in the 'Revisit the facts' pill on page 2; hovering it opens tt-f{k}.")

alt_m("Definitions",
      '"The short words on these pages. NPV: net present value to 2032. Capex: the investment. Run-rate: profit a year by 2032. NPS: promoters minus detractors. ADR: revenue per room sold. RevPAR: revenue per room available. OTA: an online booking site."',
      "The Definitions chip read aloud: the glossary in one breath, so a keyboard or screen-reader user gets the terms the hover shows.")

# ---- alt texts of the new visuals (plan 11 practice: the message with live values, from the model)
alt_m("Guide", '"How to read the chart. " & [Guide (text)] & " A is our recommendation; B and C were considered and not recommended."', "The reading guide read aloud.")
alt_m("TT Moves", TT_ID + 'RETURN IF ( ISBLANK ( pkg ), BLANK (), "The moves in the hovered package with their net present value: " & [TT Moves (text)] & ". " & [TT Not Included (text)] )',
      "The tooltip's moves table read aloud.")
for k in "BC":
    alt_m(f"{k} Nums", f'"Package {k}, " & [Selected Scenario] & " case: capex " & [Preset {k} Capex (text)] & ", net present value through 2032 " & [Preset {k} NPV (text)] & ", from " & [Preset {k} Range (text)] & " $M between the Low and High cases."',
          f"Package {k}'s numbers card read aloud.")
    alt_m(f"{k} Waterfall", pids(k) + shown_parts("[NPV @ 8%]") +
          f'RETURN IF ( ISBLANK ( f ), BLANK (), "Where the net present value of package {k} comes from, " & [Selected Scenario] & " case: " '
          '& CONCATENATEX ( adj, ' + NAME_OF.format("[@p]") + ' & " " & ' + sfm("[@s]") + ', ", ", ' + NAME_OF.format("[@p]") + ', ASC ) & "; together " & ' + sfm("SUMX ( adj, [@s] )") + ' & "." )',
          f"Package {k}'s waterfall read aloud.")
alt_m("Cmp Alts",
      f"VAR s = [Selected Scenario] VAR a32 = {CUM32('A')} VAR b32 = {CUM32('B')} VAR c32 = {CUM32('C')} "
      'RETURN "Cumulative net impact 2027 to 2032 against A, " & s & " case, by 2032: A " & ' + sfm("a32") + ' & ", B " & ' + sfm("b32") + ' & ", C " & ' + sfm("c32") + ' & "."',
      "The alts comparer read aloud: the three 2032 end points.")
alt_m("You Nums", '"Your plan, " & [Selected Scenario] & " case: capex " & [Build Capex (text)] & ", net present value through 2032 " & [Build NPV (text)] & ", from " & [Build Range (text)] & " $M between the Low and High cases. " & [Build Valid (text)]',
      "The your-plan numbers card read aloud, with the rules check.")
alt_m("Build Waterfall", BIDS + shown_parts("[NPV @ 8%]") +
      'RETURN IF ( n = 0, "No moves picked yet.", "Where the net present value of your plan comes from, " & [Selected Scenario] & " case: " '
      '& CONCATENATEX ( adj, ' + NAME_OF.format("[@p]") + ' & " " & ' + sfm("[@s]") + ', ", ", ' + NAME_OF.format("[@p]") + ', ASC ) & "; together " & ' + sfm("SUMX ( adj, [@s] )") + ' & "." )',
      "The build waterfall read aloud.")
alt_m("Cmp Build",
      BIDS + f"VAR s = [Selected Scenario] VAR a32 = {CUM32('A')} VAR y32 = CALCULATE ( [Build Cumulative Net (sel)], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2032 ) "
      'RETURN IF ( n = 0, "Cumulative net impact of A 2027 to 2032, " & s & " case, ends at " & ' + sfm("a32") + ' & "; pick moves to add your plan.", '
      '"Cumulative net impact 2027 to 2032, " & s & " case, by 2032: your plan " & ' + sfm("y32") + ' & ", A " & ' + sfm("a32") + ' & "." )',
      "The build comparer read aloud.")

# ================================================================ FinalV3 storytelling rebuild: model foundations
# Build step 3 of doc 23 (docs 20, 21 section 10, 22 section 3; 13 Nov 2026). Number measures only: the text measures
# that read them are step 4, the visuals steps 5 to 9. Every value is re-derived here and asserted against
# analysis/output/storytelling_checks.txt by project/tools/number_checks.py (E9, E10, E11 in Low, Expected, High).
C15 = "15 Storytelling rebuild"
HORIZON = FP.format("Impact horizon")

# ---- "a year on cost" (metric contract M-101): what a move adds to operating profit a year by 2032 over its capex.
# A derived ratio next to NPV, not a valuation: no discounting, no ramp, no disruption. Every Goodnight Inn move is
# live for 34 months or more in January 2032, so the organisers' annual impact is also the profit booked in 2032.
m("A Year on Cost", "DIVIDE ( [2032 Run-rate], SUM ( InvestmentProjects[CapexUSD] ) )", PCT, C15,
  "A year on cost: the annual operating-profit impact by 2032 of the moves in context over their capex, scenario in view. A derived ratio, not a valuation (no discounting, no ramp-up, no disruption).")
m("Package A Year on Cost (sel)", "DIVIDE ( [Package Run-rate (sel)], [Package Capex] )", PCT, C15,
  "A year on cost of the package(s) in context: 2032 run-rate over capex, scenario in view.")
m("Rec A Year on Cost (sel)", rec("[Package A Year on Cost (sel)]"), PCT, C15, "A year on cost of the recommendation (package A), scenario in view.")
m("Rec NPV Low", rec("SUM ( Package[NPV Low] )"), SUSDM, C15, "NPV through 2032 of the recommendation in the Low case, whatever the toggle says (the worst-case line).")
m("Rec Run-rate Low", rec("SUM ( Package[RunRate Low] )"), SUSDM, C15, "Profit a year by 2032 of the recommendation in the Low case, whatever the toggle says (the worst-case line).")
m("Build Run-rate (sel)", BIDS + f"RETURN IF ( n = 0, BLANK (), CALCULATE ( [2032 Run-rate], {BTREAT} ) )", SUSDM, C15,
  "Profit a year by 2032 of the plan being built, scenario in view; blank while nothing is picked.")
m("Build A Year on Cost (sel)", "DIVIDE ( [Build Run-rate (sel)], [Build Capex] )", PCT, C15, "A year on cost of the plan being built, scenario in view; blank while nothing is picked.")
m("Move Run-rate (num)", MOVE_P + "RETURN IF ( ISBLANK ( p ), BLANK (), CALCULATE ( [2032 Run-rate], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) )", SUSDM, C15,
  "Selector row (BuildMove): profit a year by 2032 of the move alone, scenario in view.")

# ---- status (doc 21 P-6): one source, the MoveDecision table. The word is step 4's text measure; this is the mark colour.
MOVE_ST = "LOOKUPVALUE ( MoveDecision[Status], MoveDecision[ProjectID], SELECTEDVALUE ( InvestmentProjects[ProjectID] ) )"
m("Move Status Color", f'VAR st = {MOVE_ST} RETURN IF ( ISBLANK ( st ), BLANK (), SWITCH ( st, "A", "{ACCENT_MARK}", "2028 gate", "{INK}", "{SLATE}" ) )', TXT, C15,
  "Mark colour of a move by its decision status (MoveDecision): Coffee Blue for package A, Night for the 2028 gate, Warm Grey for not now. A mark colour (3.5:1 at the lightest): the status word carries the state.")

# ---- the hero table's bar cells (doc 21 P-4, spike S-2 of 13 Nov). Geometry and domains come from the build spec the
# comp exported; opzet_report.py places lbl_hero_8 / lbl_hero_0 with hero_ref_x() from the same constants.
_HERO = json.loads((ROOT / "project" / "design-prototypes" / "rebuild-v10-spec.json").read_text(encoding="utf-8"))["construction"]["tables"]["tbl_hero"]
HERO_SPEC_COLS = list(_HERO["cols"])              # the comp's widths: the bar geometry stays on these
HERO_COLS = [280, 104, 96, 196, 64, 184, 74]      # as built (S-2): an image column is the image + 11 px, "−$27.3M" needs 74
HERO_X, HERO_ROW_H = 56, _HERO["row_h"]
HERO_INSET, HERO_BAR_Y, HERO_BAR_H = _HERO["bar_cell"]["inset_px"], _HERO["bar_cell"]["bar_y"], _HERO["bar_cell"]["bar_h"]
HERO_IMG_PAD = 7                                   # Desktop draws an image 7 px into its cell (measured in S-2, not a setting)
HERO_IMG_W = HERO_SPEC_COLS[5] - HERO_IMG_PAD      # grid.imageWidth is one value per table: the narrow bar column minus the padding
HERO_YDOM, HERO_YREF = tuple(float(v) for v in _HERO["yield_domain"]), float(_HERO["yield_ref"])
HERO_NDOM, HERO_NREF = tuple(float(v) for v in _HERO["npv_domain_usd"]), float(_HERO["npv_ref"])


def bar_x(v, dom, w):
    """The comp's barX(): the x of a value inside a bar cell of width w."""
    return HERO_INSET + (v - dom[0]) / (dom[1] - dom[0]) * (w - 2 * HERO_INSET)


def hero_ref_x():
    """Page x of the two reference lines of tbl_hero (8 % and NPV 0), for the labels above the table."""
    return (HERO_X + sum(HERO_COLS[:3]) + bar_x(HERO_YREF, HERO_YDOM, HERO_SPEC_COLS[3]),
            HERO_X + sum(HERO_COLS[:5]) + bar_x(HERO_NREF, HERO_NDOM, HERO_SPEC_COLS[5]))


def bar_cell(name, value_expr, dom, ref, fill_expr, w, doc):
    """P-4: a measure that returns an SVG data URI with one bar from zero and one full-height reference line.
    Fixed pixel width and a fixed domain, so the reference line has the same x in every row and every scenario and
    reads as one line down the table (row padding 0, image height = row height). The value is not in the SVG: it sits
    in its own text column. Numbers go through FORMAT ( x, "0.0", "en-US" ), '#' is written as %23 (Kerry Kolosko's
    SVG-in-DAX conventions, CREDITS.md). Every x is the comp's cell x minus the 7 px Desktop pads an image with."""
    span, inner = dom[1] - dom[0], w - 2 * HERO_INSET
    x0 = bar_x(max(dom[0], min(dom[1], 0.0)), dom, w) - HERO_IMG_PAD
    xr = bar_x(ref, dom, w) - HERO_IMG_PAD
    f = 'FORMAT ( {0}, "0.0", "en-US" )'
    m(name,
      f"VAR v = {value_expr} "
      f"VAR c = MIN ( MAX ( v, {dom[0]!r} ), {dom[1]!r} ) "
      f"VAR xv = {float(HERO_INSET - HERO_IMG_PAD)!r} + ( c - ( {dom[0]!r} ) ) / {span!r} * {inner} "
      f"VAR x0 = {x0!r} "
      f'VAR fill = SUBSTITUTE ( {fill_expr}, "#", "%23" ) '
      "RETURN IF ( ISBLANK ( SELECTEDVALUE ( InvestmentProjects[ProjectID] ) ) || ISBLANK ( v ), BLANK (), "
      f"\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='{HERO_IMG_W}' height='{HERO_ROW_H}' viewBox='0 0 {HERO_IMG_W} {HERO_ROW_H}'>"
      f"<rect x='\" & {f.format('MIN ( x0, xv )')} & \"' y='{HERO_BAR_Y}' width='\" & {f.format('ABS ( xv - x0 )')} & \"' height='{HERO_BAR_H}' fill='\" & fill & \"'/>"
      f"<rect x='{xr - 0.5:.2f}' y='0' width='1' height='{HERO_ROW_H}' fill='%2312233D' shape-rendering='crispEdges'/></svg>\" )",
      TXT, C15, doc)
    IMAGE_MEASURES.add(name)


bar_cell("Hero Yield Bar SVG", "[A Year on Cost]", HERO_YDOM, HERO_YREF, "[Move Status Color]", HERO_SPEC_COLS[3],
         "Hero table, bar cell of 'a year on cost' for the move in the row (scenario in view): a bar from 0 in the move's status colour and the 8 % line (our cost of money). "
         "Fixed domain -10 % to 90 %. Decorative: the value stands in the column beside it.")
bar_cell("Hero NPV Bar SVG", "[NPV @ 8%]", HERO_NDOM, HERO_NREF, "[Move Status Color]", HERO_SPEC_COLS[5],
         "Hero table, bar cell of the NPV through 2032 for the move in the row (scenario in view): a bar from 0 in the move's status colour and the zero line (pays back by 2032 to its right). "
         "Fixed domain -$32M to +$12M. Decorative: the value stands in the column beside it.")
# the domains re-derived from the data (P-4: minimum and maximum over the ten moves and the three scenarios, rounded
# outward: to 10 points for the yield, to $4M for the NPV, as the comp does). number_checks.py asserts they equal
# the constants the bar cells are drawn with, so a data change that leaves the domain cannot pass unseen.
_GI_X_SCN = ('VAR t = CROSSJOIN ( CALCULATETABLE ( VALUES ( InvestmentProjects[ProjectID] ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" ), ALLNOBLANKROW ( Scenario[Scenario] ) ) '
             'VAR v = ADDCOLUMNS ( t, "@v", VAR p = InvestmentProjects[ProjectID] VAR s = Scenario[Scenario] RETURN CALCULATE ( {0}, REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p, REMOVEFILTERS ( Scenario ), Scenario[Scenario] = s ) ) ')
m("Hero Yield Domain Min", _GI_X_SCN.format("[A Year on Cost]") + "RETURN INT ( MIN ( MINX ( v, [@v] ), 0 ) * 10 ) / 10", PCT, C15,
  "Hero table: the lowest 'a year on cost' of the ten moves over the three scenarios, rounded down to 10 points (never above 0). Guards the fixed domain of the bar cells.")
m("Hero Yield Domain Max", _GI_X_SCN.format("[A Year on Cost]") + "RETURN - INT ( - MAXX ( v, [@v] ) * 10 ) / 10", PCT, C15,
  "Hero table: the highest 'a year on cost' of the ten moves over the three scenarios, rounded up to 10 points. Guards the fixed domain of the bar cells.")
m("Hero NPV Domain Min", _GI_X_SCN.format("[NPV @ 8%]") + "RETURN INT ( MINX ( v, [@v] ) / 4000000 ) * 4000000", USDM1, C15,
  "Hero table: the lowest NPV of the ten moves over the three scenarios, rounded down to $4M. Guards the fixed domain of the bar cells.")
m("Hero NPV Domain Max", _GI_X_SCN.format("[NPV @ 8%]") + "RETURN - INT ( - MAXX ( v, [@v] ) / 4000000 ) * 4000000", USDM1, C15,
  "Hero table: the highest NPV of the ten moves over the three scenarios, rounded up to $4M. Guards the fixed domain of the bar cells.")


# ---- the $60M plan in tranches (R-P2-7): sums over MoveDecision[Tranche]; the budget from Brands. Capex does not
# follow the scenario, the run-rates do. Tranche 2 and 3 show no NPV (doc 20).
def tranche(k):
    return f'VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Tranche] = {k} ), "@p", MoveDecision[ProjectID] ) '


TTREAT = "REMOVEFILTERS ( InvestmentProjects ), TREATAS ( ids, InvestmentProjects[ProjectID] )"
for k, what in ((1, "package A, funded now"), (2, "the airport extensions, decided at the 2028 gate"), (3, "the refresh, decided at the 2028 gate")):
    m(f"Tranche {k} Capex", tranche(k) + f"RETURN CALCULATE ( SUM ( InvestmentProjects[CapexUSD] ), {TTREAT} )", USDM1, C15, f"Capex of tranche {k} ({what}); a segment of the plan bar.")
    m(f"Tranche {k} Run-rate", tranche(k) + f"RETURN CALCULATE ( [2032 Run-rate], {TTREAT} )", SUSDM, C15, f"Profit a year once live of tranche {k} ({what}), scenario in view.")
    m(f"Tranche {k} Year on Cost", f"DIVIDE ( [Tranche {k} Run-rate], [Tranche {k} Capex] )", PCT, C15, f"A year on cost of tranche {k} ({what}), scenario in view.")
m("Not Needed Capex", f"{BUDGET_GI} - [Tranche 1 Capex] - [Tranche 2 Capex] - [Tranche 3 Capex]", USDM1, C15,
  "The part of the Goodnight Inn budget no tranche asks for; the last segment of the plan bar (the four segments add up to the budget by construction).")


# ---- the 2032 ledger (R-P2-5, metric contracts M-102 and M-103): the 2025 brand plus package A at full yearly
# effect, in 2025 dollars. Port of analysis/50_storytelling_checks.py section 6 (E11).
def a_sum(col):
    return f"CALCULATE ( SUM ( InvestmentScenarios[{col}] ), REMOVEFILTERS ( InvestmentProjects ), TREATAS ( aIds, InvestmentProjects[ProjectID] ), InvestmentScenarios[Scenario] = s )"


m("Dist Cost % 2025 GI", gi_at("Distribution Cost % of Room Revenue", 2025), PCT, C15, "Goodnight Inn distribution cost as a share of room revenue, 2025 (the ledger's F2 start).")
m("Dist Cost % 2032 with A (sel)", REC_IDS + "VAR s = [Selected Scenario] RETURN [Dist Cost % 2025 GI] + " + a_sum("DistributionCostChangePts"), PCT, C15,
  "Ledger F2: the 2025 distribution cost share of room revenue plus the organisers' change in points for the moves of package A, scenario in view. 2025 brand, A at full effect; not a forecast of 2032.")
m("Margin after 2032 with A (sel)",
  REC_IDS + "VAR s = [Selected Scenario] VAR tot = " + gi_at("Total Revenue", 2025) + " VAR gopa = " + gi_at("GOP after Distribution", 2025) + " "
  "RETURN DIVIDE ( gopa + " + a_sum("AnnualOperatingProfitImpactUSD") + ", tot + " + a_sum("AnnualRevenueImpactUSD") + " )", PCT, C15,
  "Ledger F1: operating margin after commissions of the 2025 brand with package A's full yearly profit and revenue impact added, scenario in view. In 2025 dollars; not a forecast of 2032.")
m("Dist Cost Rise Undone % (sel)",
  "VAR d21 = " + gi_at("Distribution Cost % of Room Revenue", 2021) + " VAR d25 = [Dist Cost % 2025 GI] RETURN DIVIDE ( d25 - [Dist Cost % 2032 with A (sel)], d25 - d21 )", "0%", C15,
  "Ledger F2 status: the share of the 2021 to 2025 rise in distribution cost (points of room revenue) that package A undoes, scenario in view.")
m("Margin Fall Recovered % (sel)",
  "VAR m23 = " + gi_at("GOP Margin after Distribution %", 2023) + " VAR m25 = [KPI Margin after GI] RETURN DIVIDE ( [Margin after 2032 with A (sel)] - m25, m23 - m25 )", "0%", C15,
  "Ledger F1 status: the share of the 2023 to 2025 fall in the margin after commissions that package A recovers, scenario in view.")
# "the app" = the move of package A that answers F2 (the middleman), read from MoveDecision
APP_IDS = 'VAR appIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Status] = "A" && MoveDecision[Finding] = "F2" ), "@p", MoveDecision[ProjectID] ) '
APP_T = "REMOVEFILTERS ( InvestmentProjects ), TREATAS ( appIds, InvestmentProjects[ProjectID] )"
m("App Commission Saving (sel)",
  APP_IDS + "VAR s = [Selected Scenario] VAR rr = " + gi_at("Channel Room Revenue", 2025) + f" RETURN - CALCULATE ( SUM ( InvestmentScenarios[DistributionCostChangePts] ), {APP_T}, InvestmentScenarios[Scenario] = s ) * rr", USDM1, C15,
  "What the booking app saves in commissions a year: its change in distribution cost (points of room revenue, scenario in view) on 2025 room revenue. Also what every year without it leaves with the agencies.")
m("App NPV (sel)", APP_IDS + f"RETURN CALCULATE ( [NPV @ 8%], {APP_T} )", SUSDM, C15, "NPV through 2032 of the booking app alone (the move of A that answers F2), scenario in view.")
m("App Run-rate (sel)", APP_IDS + f"RETURN CALCULATE ( [2032 Run-rate], {APP_T} )", SUSDM, C15, "Profit a year by 2032 of the booking app alone, scenario in view.")

# ---- cumulative charts (doc 21 P-5 as amended by doc 22 section 3): one data label per line, on the last year,
# carrying the name and the value ("A +$6.8M"). Each line gets an end series: the value on the horizon year only,
# label-safe (P-1). In the chart the end series come AFTER the line series, so the value axis keeps a line's format.
_YEND = f"VAR __y = MAX ( 'Date'[Year] ) VAR __h = {HORIZON} RETURN IF ( __y = __h, {{0}} )"
for scn in ("Low", "Expected", "High"):
    m(f"A Cumulative Line ({scn})", f'IF ( [Selected Scenario] = "{scn}", BLANK (), [TT Year A ({scn})] )', SUSDM0, C15,
      f"Capital plan chart: package A's cumulative net impact in the {scn} case; blank when {scn} is the case in view (the emphasised line draws it). "
      "Whole $M: the first of these is the chart's first series, and a value axis prints its first series' format on every tick (build step 7).")
    label_safe(f"A Cumulative End {scn} (label-safe)", _YEND.format(f"[A Cumulative Line ({scn})]"), f'"{scn} " & ' + sfm(f"[A Cumulative Line ({scn})]"), C15,
               f"Capital plan chart, end label of the {scn} line: its value on the horizon year only, printed as '{scn}' and the amount.")
label_safe("A Cumulative End Sel (label-safe)", _YEND.format("[Preset A Cumulative Net (sel)]"), '[Selected Scenario] & " " & ' + sfm("[Preset A Cumulative Net (sel)]"), C15,
           "Capital plan chart, end label of the emphasised line (the case in view): its value on the horizon year only, printed as the case name and the amount.")
for k in "ABC":
    label_safe(f"Preset {k} Cumulative End (label-safe)", _YEND.format(f"[Preset {k} Cumulative Net (sel)]"), f'"{k} " & ' + sfm(f"[Preset {k} Cumulative Net (sel)]"), C15,
               f"Comparison chart, end label of package {k}: its cumulative net impact on the horizon year only, printed as '{k}' and the amount, scenario in view.")
label_safe("A Cumulative End Name (label-safe)", _YEND.format("[Preset A Cumulative Net (sel)]"), '"A"', C15,
           "Build comparison chart, end label of package A: the value on the horizon year only, printed as 'A' (the title carries the amounts; You equals A when the state opens).")
label_safe("Build Cumulative End Name (label-safe)", _YEND.format("[Build Cumulative Net (sel)]"), '"You"', C15,
           "Build comparison chart, end label of the plan being built: the value on the horizon year only, printed as 'You'; blank while nothing is picked.")

# ---- label-safe twins for bars (P-1)
label_safe("NPS 2025 (label-safe)", "[NPS (weighted) 2025]", pt1("[NPS (weighted) 2025]"), C15,
           "F3 bars: response-weighted NPS 2025 with its label as finished text ('+6.8', a true minus), so no session locale prints a decimal comma.")
m("Build Bar NPV", BIDS + "VAR me = SELECTEDVALUE ( BuildMove[ProjectID] ) RETURN IF ( n > 0 && me IN ids, CALCULATE ( [NPV @ 8%], REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = me ) )", SUSDM, C15,
  "Build bar chart (BuildMove): the NPV through 2032 of a picked move alone, scenario in view; blank for a move that is not picked, so the chart lists the plan only.")
label_safe("Build Bar NPV (label-safe)", "[Build Bar NPV]", sfm("[Build Bar NPV]"), C15, "Build bar chart: the picked move's NPV with its label as finished text ('+$3.4M', '−$0.6M').")
m("Build Bar Color", f'VAR v = [Build Bar NPV] RETURN IF ( ISBLANK ( v ), BLANK (), IF ( ROUND ( v / 1000000, 2 ) < 0, "{SIGNAL_MARK}", "{INK}" ) )', TXT, C15,
  "Build bar chart: Night for a move that adds NPV (Night is 'your plan'), Tangerine for one that costs NPV; the signed label carries it too (R-G3).")

# ---- page 1 numbers (doc 21 sections 4.2 to 4.5, doc 22 section 3)
m("Trend Commission Take GI", "[Trend Margin before GI] - [Trend Margin after GI]", PCT, C15,
  "F1 stacked area, the band on top of the margin after commissions: what the booking channels take, in points of revenue (margin before minus margin after commissions).")
_ENDS = ("VAR __y = SELECTEDVALUE ( 'Date'[Year] ) VAR __y0 = YEAR ( CALCULATE ( MIN ( MonthlyPerformance[Month] ), REMOVEFILTERS () ) ) "
         "VAR __y1 = YEAR ( CALCULATE ( MAX ( MonthlyPerformance[Month] ), REMOVEFILTERS () ) ) ")
m("Trend OTA GI (ends)", _ENDS + "RETURN IF ( __y = __y0 || __y = __y1, [Trend OTA GI] )", "0%", C15,
  "F2 chart, end labels of the Goodnight Inn line: the OTA share in the first and the last year of the data only. Whole percent, so it needs no label-safe twin.")
m("Trend OTA Sisters (end)", _ENDS + "RETURN IF ( __y = __y1, [Trend OTA Sisters] )", "0%", C15,
  "F2 chart, end label of the sister brands' line: the OTA share in the last year of the data only. Whole percent.")
_F4_ROW = 'SWITCH ( SELECTEDVALUE ( Hotels[LocationType] ), "Airport", 3, "City", 2, "Highway", 1 )'
_F4_OCC = "VAR hid = Hotels[HotelID] RETURN CALCULATE ( [Occupancy % 2025], REMOVEFILTERS ( Hotels ), Hotels[HotelID] = hid )"
m("F4 Row Y",
  f"VAR base = {_F4_ROW} VAR me = SELECTEDVALUE ( Hotels[HotelID] ) VAR t = SELECTEDVALUE ( Hotels[LocationType] ) VAR br = SELECTEDVALUE ( Hotels[Brand] ) "
  "RETURN IF ( ISBLANK ( me ), base, "
  # the hotel's row: every hotel of its brand and location type with its 2025 occupancy
  f'VAR rw = ADDCOLUMNS ( CALCULATETABLE ( VALUES ( Hotels[HotelID] ), REMOVEFILTERS ( Hotels ), Hotels[LocationType] = t, Hotels[Brand] = br ), "@o", {_F4_OCC} ) '
  # near: another hotel of the row sits within one point of occupancy
  "VAR near = FILTER ( rw, VAR o = [@o] VAR hid = Hotels[HotelID] RETURN COUNTROWS ( FILTER ( rw, Hotels[HotelID] <> hid && ABS ( [@o] - o ) < 0.01 ) ) > 0 ) "
  "VAR myo = MAXX ( FILTER ( rw, Hotels[HotelID] = me ), [@o] ) "
  "VAR k = COUNTROWS ( FILTER ( near, [@o] >= myo ) ) "
  "RETURN base + IF ( COUNTROWS ( FILTER ( near, Hotels[HotelID] = me ) ) > 0, IF ( MOD ( k, 2 ) = 1, -0.3, 0.3 ), 0 ) )",
  "0.0", C15,
  "F4 dot plot, the hotel's row: Airport 3, City 2, Highway 1. A hotel within one point of occupancy of another in its row steps 0.3 off the row, alternately below and above "
  "in order of 2025 occupancy (Gatwick below, Montréal above), so close dots stay apart. For a location type (the average markers) the row itself. A layout value, not a metric.")
m("F4 Dot Color",
  "VAR me = SELECTEDVALUE ( Hotels[HotelID] ) VAR br = SELECTEDVALUE ( Hotels[Brand] ) "
  f'VAR t7 = TOPN ( 7, ADDCOLUMNS ( CALCULATETABLE ( VALUES ( Hotels[HotelID] ), REMOVEFILTERS ( Hotels ), Hotels[Brand] = br ), "@o", {_F4_OCC} ), [@o], DESC ) '
  f'RETURN IF ( ISBLANK ( me ), BLANK (), IF ( COUNTROWS ( FILTER ( t7, Hotels[HotelID] = me ) ) > 0, "{INK}", "{SLATE}" ) )', TXT, C15,
  "F4 dot plot: Night for the seven fullest hotels of the brand in 2025, Warm Grey for the rest (R-G3: no blue on page 1's marks). The seven are named beside their dots.")
m("F4 Type Avg", "[Occupancy % 2025]", PCT, C15, "F4 dot plot, the average markers: 2025 occupancy of the location type in context (rooms sold over rooms available, not an average of hotel percentages).")
m("Months Topped 90% (last 24)",
  "VAR d1 = CALCULATE ( MAX ( MonthlyPerformance[Month] ), REMOVEFILTERS () ) VAR d0 = EDATE ( d1, -23 ) "
  "VAR mths = CALCULATETABLE ( VALUES ( MonthlyPerformance[Month] ), REMOVEFILTERS ( 'Date' ), MonthlyPerformance[Month] >= d0 ) "
  "RETURN COUNTROWS ( FILTER ( mths, CALCULATE ( DIVIDE ( SUM ( MonthlyPerformance[RoomsSold] ), SUM ( MonthlyPerformance[RoomsAvailable] ) ), REMOVEFILTERS ( 'Date' ) ) >= 0.9 ) ) + 0", "0", C15,
  "Months, of the last 24 in the data, in which the hotels in context sold 90 percent or more of their available room nights ('topped 90%': the month's occupancy at or above 90%).")
# P-7 (doc 21 section 3, S-8 passed in step 1): the Definitions chip is one card on this measure, the ring-i (U+24D8) in front
m("Chip Definitions (text)", 'UNICHAR ( 9432 ) & " Definitions"', TXT, C15,
  "The words on the Definitions chip of the rebuilt pages, 'ⓘ Definitions'; hovering the chip opens the definitions tooltip page.")

# ================================================================ FinalV3 storytelling rebuild: text measures
# Build step 4 of doc 23 (docs 20, 21 sections 3 P-8 and 10.2 / 10.3, 22 sections 4 and 6; 13 Nov 2026). Every sentence of the
# rebuilt canvas comes from one measure, with its scenario branches, as rebuild-v10-spec.json -> text has it. The numbers
# come from folder 15 (step 3), printed by the one formatter set fm / sfm / pct1 / pt1 (R-G1); the words follow R-G2.
# Connecting words that depend on the data (rose / fell, more / less, neither / both) are guarded, as in the copy of
# 7 Nov. TEXT_SLOTS (end of this block) maps every slot of the spec to the measure(s) that print it; build_checks.py
# evaluates them in Low, Expected and High and diffs the result against the spec.
LF = "UNICHAR ( 10 )"
RATE, BASE_YEAR = FP.format("Discount rate"), FP.format("Base year")
GATE_YEAR = 2028  # the year of the one Board decision (D2 of doc 20): a decision, typed once
# label data, like MOVE_NAMES: how the copy names a move inside a sentence, and its short label in mixes and milestones
MOVE_SENTENCE = {"GI-01": "booking app", "GI-02": "kiosks", "GI-03": "energy programme", "GI-04": "Toronto extension", "GI-05": "Gatwick extension",
                 "GI-06": "Kingston extension", "GI-07": "refresh", "GI-08": "Boston hotel", "GI-09": "breakfast upgrade", "GI-10": "revenue management system"}
MOVE_PLURAL = {"GI-02"}
MOVE_LABEL = {"GI-01": "App", "GI-02": "Kiosks", "GI-03": "Energy", "GI-04": "Toronto +40", "GI-05": "Gatwick +40", "GI-06": "Kingston +40",
              "GI-07": "refresh", "GI-08": "Boston", "GI-09": "Breakfast", "GI-10": "RMS"}
# the second line of the ledger's F2 and F1 rows: the moves of A that act on the finding (static, like the mix line:
# A's composition never changes with the scenario, decision of 7 Nov)
LEDGER_MOVES = {"F2": "booking app with member rates", "F1": "app + revenue management + kiosks"}


def pid_switch(var, mapping, default='""'):
    return f"SWITCH ( {var}, " + ", ".join(f'"{k}", "{v}"' for k, v in sorted(mapping.items())) + f", {default} )"


def is_plural(var):
    return f"( {var} IN {{ " + ", ".join(f'"{p}"' for p in sorted(MOVE_PLURAL)) + " } )"


def cap1(x):
    """Text with its first letter in upper case."""
    return f"( VAR __w = {x} RETURN UPPER ( LEFT ( __w, 1 ) ) & MID ( __w, 2, 500 ) )"


def words(n):
    """A count as a word ("three"); from 11 on the figure."""
    return (f'( VAR __n = {n} RETURN SWITCH ( __n, 0, "no", 1, "one", 2, "two", 3, "three", 4, "four", 5, "five", 6, "six", 7, "seven", '
            '8, "eight", 9, "nine", 10, "ten", FORMAT ( __n, "0", "en-US" ) ) )')


def ordinal(n):
    return f'( VAR __n = {n} RETURN SWITCH ( __n, 1, "first", 2, "second", 3, "third", 4, "fourth", 5, "fifth", FORMAT ( __n, "0", "en-US" ) & "th" ) )'


def share_words(x):
    """The ledger's status words for the share of a change that A undoes (R-P2-5): a quarter of, half, most of ..."""
    return ('( VAR __x = ' + x + ' RETURN SWITCH ( TRUE (), __x <= 0, "none of", __x < 0.2, "a little of", __x < 0.3, "a quarter of", '
            '__x < 0.4, "a third of", __x < 0.6, "half", __x < 0.7, "two thirds of", __x < 0.85, "three quarters of", __x < 1, "most of", "all of" ) )')


def month(d):
    return f'FORMAT ( {d}, "mmm yyyy", "en-US" )'


def sint(x):
    """A signed whole number: "+6", "−3"."""
    return f'( VAR __i = ROUND ( {x}, 0 ) RETURN IF ( __i < 0, {MINUS}, IF ( __i > 0, "+", "" ) ) & FORMAT ( ABS ( __i ), "0", "en-US" ) )'


HOTEL_OF = "MAXX ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] = {} ), InvestmentProjectProperties[HotelID] )"
AT_HOTEL = "CALCULATE ( {0}, REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( Brands ), Hotels[HotelID] = {1} )"
COPY_NAME = "LOOKUPVALUE ( Hotels[Copy Name], Hotels[HotelID], {} )"
AT_MOVE = "CALCULATE ( {0}, REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = {1} )"
# the Goodnight Inn hotels with their months topped 90 % (last 24) and 2025 occupancy
GI_HOTEL_T = ('VAR hs = ADDCOLUMNS ( CALCULATETABLE ( VALUES ( Hotels[HotelID] ), REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( Brands ), Hotels[Brand] = "Goodnight Inn" ), '
              '"@m", VAR h = Hotels[HotelID] RETURN ' + AT_HOTEL.format("[Months Topped 90% (last 24)]", "h") + ', '
              '"@o", VAR h = Hotels[HotelID] RETURN ' + AT_HOTEL.format("[Occupancy % 2025]", "h") + " ) ")


def tranche_t(k):
    """VAR th: the moves of tranche k with their hero order, rooms, hotel, its copy name, months topped 90 % and NPV."""
    return (f'VAR th0 = ADDCOLUMNS ( SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Tranche] = {k} ), "@p", MoveDecision[ProjectID] ), '
            '"@o", LOOKUPVALUE ( InvestmentProjects[Hero Sort], InvestmentProjects[ProjectID], [@p] ), '
            '"@r", LOOKUPVALUE ( InvestmentProjects[AddedRooms], InvestmentProjects[ProjectID], [@p] ), '
            '"@h", VAR p = [@p] RETURN ' + HOTEL_OF.format("p") + " ) "
            'VAR th = ADDCOLUMNS ( th0, "@n", ' + COPY_NAME.format("[@h]") + ', '
            '"@m", VAR h = [@h] RETURN ' + AT_HOTEL.format("[Months Topped 90% (last 24)]", "h") + ', '
            '"@v", VAR p = [@p] RETURN ' + AT_MOVE.format("[NPV @ 8%]", "p") + " ) ")


T2_NAMES = 'CONCATENATEX ( th, [@n], " and ", [@o], ASC )'  # "Gatwick and Toronto", in hero order
# the extensions on offer: the organisers' Expansion projects of Goodnight Inn
_EXT = ('SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects[ProjectID], InvestmentProjects[Category], InvestmentProjects[Brand] ), '
        'InvestmentProjects[Category] = "Expansion" && InvestmentProjects[Brand] = "Goodnight Inn" ), "@p", InvestmentProjects[ProjectID] ) ')

# ---- page 1 (R-P1-1 to R-P1-6)
m("Staff Cost", "SUM ( MonthlyPerformance[StaffCost] )", USDM, C15, "Staff cost in the period (part of operating expenses).")
m("Staff Cost % of Revenue", "DIVIDE ( [Staff Cost], [Total Revenue] )", PCT, C15, "Staff cost as a share of total revenue (F1 note: running costs).")
m("Subtitle P1 Briefing (text)",
  'VAR n = COUNTROWS ( ALLNOBLANKROW ( Brands[Brand] ) ) - 1 '
  'RETURN "Goodnight Inn in " & ' + BASE_YEAR + ' & ", against the " & ' + words("n") + ' & " other Pillow & Key Group brands. For the Board: what is wrong, before page 2 says what to fund."',
  TXT, C15, "Page-1 subtitle (R-P1-1): the year, the comparison and the audience.")
m("F1 Note (text)",
  # N-2 (doc 21, approved 13 Nov): the fall of 2.8 points split honestly. Commissions = the margin before minus the
  # margin after commissions; running costs = the fall of the margin before commissions. Each part rounded to one
  # decimal (1.0 and 1.8; exact 0.97 and 1.77, 2.72 in all), the title keeps 2.8 from the two shown margins.
  rank_words("GOP Margin %", 2025, 1)
  + "VAR c23 = " + gi_at("GOP Margin %", 2023) + " - " + gi_at("GOP Margin after Distribution %", 2023) + " "
  + "VAR c25 = gn - " + gi_at("GOP Margin after Distribution %", 2025) + " "
  + "VAR comm = ROUND ( ( c25 - c23 ) * 100, 1 ) VAR ops = ROUND ( ( " + gi_at("GOP Margin %", 2023) + " - gn ) * 100, 1 ) "
  + "VAR s23 = " + gi_at("Staff Cost % of Revenue", 2023) + " VAR s25 = " + gi_at("Staff Cost % of Revenue", 2025) + " "
  + "VAR pa = ROUND ( " + adr_chg('"Goodnight Inn"') + ", 3 ) VAR plo = ROUND ( " + adr_chg_sisters("MINX") + ", 3 ) VAR phi = ROUND ( " + adr_chg_sisters("MAXX") + ", 3 ) "
  'RETURN IF ( comm > 0 && ops > 0, "Commissions took " & FORMAT ( comm, "0.0", "en-US" ) & " of those points and running costs " & FORMAT ( ops, "0.0", "en-US" ) '
  '& " (staff " & IF ( s25 >= s23, "rose", "fell" ) & " from " & ' + pct1("s23") + ' & " to " & ' + pct1("s25") + ' & " of revenue). ", "" ) '
  '& "Room rates " & IF ( pa < 0, "fell ", "rose " ) & ' + pct1("ABS ( pa )") + ' & ", " '
  '& IF ( pa > phi, "faster than the other brands.", IF ( pa < plo, "slower than the other brands.", "in line with the other brands, so no price premium absorbs it." ) )',
  TXT, C15, "F1 note (R-P1-3, N-2): the 2023-2025 fall of the margin after commissions split into commissions and running costs, the staff share as the main running cost, "
            "and room-rate growth since 2023 against the sister brands (plan 09 R1).")
_OTA, _DIR = 'BookingChannels[Channel] = "Online Travel Agencies"', 'BookingChannels[Channel] = "Direct Website & App"'
m("F2 Note (text)",
  # the folio's own (rounded) amounts, so the differences equal the ones a reader works out from the table above
  "VAR o = ROUND ( DIVIDE ( " + gi_at("Channel Room Revenue", 2025, _OTA) + ", " + gi_at("Channel Room Nights", 2025, _OTA) + " ), 2 ) "
  "VAR oc = ROUND ( DIVIDE ( " + gi_at("Distribution Cost", 2025, _OTA) + ", " + gi_at("Channel Room Nights", 2025, _OTA) + " ), 2 ) "
  "VAR d = ROUND ( DIVIDE ( " + gi_at("Channel Room Revenue", 2025, _DIR) + ", " + gi_at("Channel Room Nights", 2025, _DIR) + " ), 2 ) "
  "VAR dc = ROUND ( DIVIDE ( " + gi_at("Distribution Cost", 2025, _DIR) + ", " + gi_at("Channel Room Nights", 2025, _DIR) + " ), 2 ) "
  f"VAR dp = d - o VAR dk = ( d - dc ) - ( o - oc ) VAR x = CALCULATE ( [Distribution Cost above 2021 Mix 2025], {gi} ) "
  # per-night dollars with cents: the folio's unit, the one named exception to one decimal (R-G1 is about $M)
  'RETURN "Booked direct, the guest pays " & FORMAT ( ABS ( dp ), "$#,0.00", "en-US" ) & IF ( dp >= 0, " more", " less" ) '
  '& " and we keep " & FORMAT ( ABS ( dk ), "$#,0.00", "en-US" ) & IF ( dk >= 0, " more", " less" ) & ". " '
  '& IF ( dp >= 0, "Nothing rewards the guest for booking direct; member rates change that. ", "" ) '
  '& "At the 2021 channel mix, 2025 commissions would be " & ' + fm("ABS ( x )") + ' & IF ( x >= 0, " lower.", " higher." )',
  TXT, C15, "F2 note (R-P1-4): what booking direct changes for one room night (from the folio's shown amounts), the bridge to member rates, and the 2021-mix counterfactual.")
m("F3 Count (text)",
  f"VAR nAll = CALCULATE ( COUNTROWS ( Hotels ), {gi} ) VAR dated = CALCULATE ( COUNTROWS ( Hotels ), {gi}, NOT ISBLANK ( Hotels[Renovation Age Sort] ) ) VAR u = nAll - dated "
  'RETURN dated & " of " & nAll & " hotels" & IF ( u = 0, ".", "; " & u & IF ( u = 1, " has", " have" ) & " no renovation date." )',
  TXT, C15, "F3 count line (R-P1-5): how many hotels the three age bands hold, counted from the model (hotels with and without a renovation date).")
_SPEND = "CALCULATE ( [Renovation Spend per Hotel since 2018], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), Brands[Brand] = {}, REMOVEFILTERS ( 'Date' ) )"
m("F3 Note (text)",
  "VAR sp = " + _SPEND.format('"Goodnight Inn"') + " "
  'VAR lo = MINX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN ' + _SPEND.format("b") + " ) "
  'VAR hi = MAXX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), VAR b = Brands[Brand] RETURN ' + _SPEND.format("b") + " ) "
  f"VAR last = YEAR ( CALCULATE ( MAX ( Renovations[StartDate] ), {gi}, REMOVEFILTERS ( 'Date' ) ) ) "
  "VAR o1 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 1") + " VAR o2 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 2") + " VAR o3 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 3") + " "
  "VAR olo = MIN ( MIN ( o1, o2 ), o3 ) VAR ohi = MAX ( MAX ( o1, o2 ), o3 ) "
  'RETURN "Since 2018 Goodnight Inn spent " & ' + fm("sp") + ' & " per hotel on renovation; the other brands spent " & ' + fm("lo") + ' & " to " & ' + fm("hi") + ' & ". "'
  ' & "None has started since " & last & ". "'
  # the 'not yet rooms' clause only while the bands sit within 2 points of occupancy (as since 7 Nov); the caveat always
  ' & IF ( ohi - olo <= 0.02, "Older hotels lose guest loyalty before they lose rooms: an association, not proof of cause.", "An association, not proof of cause." )',
  TXT, C15, "F3 note (R-P1-5): renovation spend per hotel since 2018 against the sister brands, the last start, and the causality caveat (05 caveat A2).")
m("F4 Title (text)",
  GI_HOTEL_T + "VAR th = MAXX ( TOPN ( 1, hs, [@m], DESC, [@o], DESC ), Hotels[HotelID] ) VAR tm = MAXX ( FILTER ( hs, Hotels[HotelID] = th ), [@m] ) "
  "VAR air = [Occupancy Airport GI] VAR best = MAX ( [Occupancy City GI], [Occupancy Highway GI] ) "
  'RETURN IF ( air >= best && LOOKUPVALUE ( Hotels[LocationType], Hotels[HotelID], th ) = "Airport", "Our airports run full: ", "" ) & ' + COPY_NAME.format("th")
  + ' & " topped 90% occupancy in " & tm & " of the last 24 months"',
  TXT, C15, "F4 title (R-P1-6): the hotel that topped 90 % occupancy in the most of the last 24 months; 'our airports run full' while the airports are the fullest location type and it is one.")
m("F4 Note (text)",
  GI_HOTEL_T + "VAR t3 = TOPN ( 3, hs, [@m], DESC, [@o], DESC ) VAR h1 = MAXX ( TOPN ( 1, t3, [@m], DESC, [@o], DESC ), Hotels[HotelID] ) "
  "VAR r2 = FILTER ( t3, Hotels[HotelID] <> h1 ) VAR h2 = MAXX ( TOPN ( 1, r2, [@m], DESC, [@o], DESC ), Hotels[HotelID] ) VAR h3 = MAXX ( FILTER ( r2, Hotels[HotelID] <> h2 ), Hotels[HotelID] ) "
  # the extensions on offer (the organisers' Expansion projects) whose hotel is not one of the three just named
  "VAR ext = " + _EXT +
  'VAR eh =ADDCOLUMNS ( ext, "@h", VAR p = [@p] RETURN ' + HOTEL_OF.format("p") + " ) "
  "VAR other = FILTER ( eh, NOT ( [@h] IN { h1, h2, h3 } ) ) VAR kh = MAXX ( other, [@h] ) VAR km = MAXX ( FILTER ( hs, Hotels[HotelID] = kh ), [@m] ) "
  'RETURN ' + COPY_NAME.format("h2") + ' & " did in " & MAXX ( FILTER ( hs, Hotels[HotelID] = h2 ), [@m] ) & ", " & ' + COPY_NAME.format("h3") + ' & " in " & MAXX ( FILTER ( hs, Hotels[HotelID] = h3 ), [@m] ) '
  '& IF ( COUNTROWS ( other ) = 1, "; " & ' + COPY_NAME.format("kh") + ' & ", the " & ' + ordinal("COUNTROWS ( ext )") + ' & " extension on offer, in " & IF ( km = 0, "none", FORMAT ( km, "0", "en-US" ) ), "" ) & "."',
  TXT, C15, "F4 note: the next two hotels by months topped 90 %, and the one extension on offer outside them (Kingston) with its count.")
m("Link F4 (text)",
  'VAR n = COUNTROWS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] = "GI-02" ) ) '
  'RETURN UNICHAR ( 8594 ) & " Page 2: kiosks at the " & FORMAT ( n, "0", "en-US" ) & " busiest hotels; extensions decided at the 2028 gate."',
  TXT, C15, "F4 forward link (R-P1-7): the move on page 2 that answers F4, with the number of hotels the kiosk move covers read from the organisers' project properties.")

# ---- page 2, the shared frame (R-P2-1, R-P2-12)
m("Headline P2 (text)",
  "\"Fix the middleman first: \" & " + fm("[Rec Capex]") + " & \" now earns \" & " + fm("[Rec Run-rate (sel)]") + f" & \" a year by \" & {HORIZON} & \".\"",
  TXT, C15, "Page-2 headline (D6, doc 22 section 4): what A costs now and what it earns a year by 2032, scenario in view.")
m("Subtitle P2 (text)",
  f"VAR budget = {BUDGET_GI} VAR h = {HORIZON} "
  'RETURN "The other " & ' + fm("budget - [Rec Capex]") + f' & " waits for one Board decision in mid-{GATE_YEAR}. " & [Selected Scenario] & " case. NPV through " & h & " at " & FORMAT ( {RATE}, "0%", "en-US" ) '
  f'& " in " & {BASE_YEAR} & " dollars is the contest\'s rule and counts nothing after " & h & ", so we also show what each move earns a year once it is live."',
  TXT, C15, "Page-2 subtitle (R-P2-1): the budget that waits for the gate, the case in view, and the valuation rule with why the yearly figure is shown too.")
m("Footer P2 (text)",
  f'"Source: Pillow & Key Group dataset and finance parameters (" & FORMAT ( {RATE}, "0%", "en-US" ) & " discount rate, " & {BASE_YEAR} & " dollars, horizon " & {HORIZON} & "). Parts are rounded to add up."',
  TXT, C15, "Page-2 source line (R-P2-12): the source and the three valuation parameters, read from FinanceParameters.")

# ---- Recommended: the hero (R-P2-3), the decision card (R-P2-6), the ledger (R-P2-5)
m("Move Yield (text)", MOVE_P + "RETURN IF ( ISBLANK ( p ), BLANK (), VAR y = " + AT_MOVE.format("[A Year on Cost]", "p") + " RETURN " + pct1("y") + " )", TXT, C15,
  "Hero and selector row: the move's 'a year on cost', scenario in view.")
m("Move Status (text)", MOVE_P + "RETURN IF ( ISBLANK ( p ), BLANK (), LOOKUPVALUE ( MoveDecision[Status], MoveDecision[ProjectID], p ) )", TXT, C15,
  "Hero row: the move's decision status as a word (A, 2028 gate, not now): status is a word first, a colour second (P-6).")
m("Move Run-rate (text)", "VAR v = [Move Run-rate (num)] RETURN IF ( ISBLANK ( v ), BLANK (), " + sfm("v") + " )", TXT, C15, "Selector row: the move's profit a year by 2032 as text.")
_HERO_T = ('VAR t = ADDCOLUMNS ( SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects[ProjectID], InvestmentProjects[Brand], InvestmentProjects[Hero Sort] ), InvestmentProjects[Brand] = "Goodnight Inn" ), '
           '"@p", InvestmentProjects[ProjectID], "@o", InvestmentProjects[Hero Sort] ), '
           '"@y", VAR p = [@p] RETURN ' + AT_MOVE.format("[A Year on Cost]", "p") + ', "@v", VAR p = [@p] RETURN ' + AT_MOVE.format("[NPV @ 8%]", "p") + " ) ")
# the two tests on the shown values: 'a year on cost' at or above our cost of money, NPV through 2032 at least zero
_PASS_Y, _PASS_N = f"ROUND ( [@y], 3 ) >= {RATE}", "ROUND ( [@v] / 1000000, 2 ) >= 0"
m("Hero Title (text)",
  _HERO_T + f"VAR k = COUNTROWS ( FILTER ( t, {_PASS_Y} && {_PASS_N} ) ) + 0 "
  f"VAR f = TOPN ( 1, FILTER ( t, {_PASS_Y} && NOT ( {_PASS_N} ) ), [@o], ASC ) VAR fp = MAXX ( f, [@p] ) VAR fy = MAXX ( f, [@y] ) VAR pl = {is_plural('fp')} "
  'RETURN ' + cap1(words("k")) + ' & IF ( k = 1, " move passes", " moves pass" ) & " both tests" '
  '& IF ( ISBLANK ( fp ), "", "; the " & ' + pid_switch("fp", MOVE_SENTENCE) + ' & IF ( pl, " earn ", " earns " ) & ' + pct1("fy")
  + f' & " a year on cost but " & IF ( pl, "pay", "pays" ) & " back after " & {HORIZON} )',
  TXT, C15, "Hero title (R-P2-3): how many moves pass both tests (a year on cost at or above our cost of money, NPV through 2032 at least zero), "
            "then the first move in hero order that passes the first test only. Scenario in view; the order never moves.")
m("Rec A Year on Cost (text)", pct1("[Rec A Year on Cost (sel)]"), TXT, C15, "Decision card: A's 'a year on cost', scenario in view.")
m("Rec Line 1 (text)",
  f'VAR rr = [Rec Run-rate Low] RETURN "Worst case (Low): " & ' + sfm("[Rec NPV Low]") + f' & " through " & {HORIZON} & ", and " & IF ( rr > 0, "still ", "" ) & ' + sfm("rr")
  + f' & " a year by " & {HORIZON} & "."',
  TXT, C15, "Decision card, line 1 (R-P2-6): the downside, always the Low case.")
m("Rec Line 2 (text)",
  # doc 22 section 6, question 1: when A does not pay back by 2032 in the case in view (only Low), the app is weighed on
  # the yearly figure line 1 has just given ("of that"), not on a loss it would 'carry'
  'VAR npv = [Rec NPV (sel)] '
  'RETURN "The app carries it: " & IF ( ROUND ( npv / 100000, 0 ) < 0, ' + sfm("[App Run-rate (sel)]") + ' & " of that " & ' + sfm("[Rec Run-rate (sel)]") + ', '
  + sfm("[App NPV (sel)]") + ' & " of the " & ' + sfm("npv") + ' ) & ". Every year without it leaves about " & ' + fm("[App Commission Saving (sel)]") + ' & " with the agencies."',
  TXT, C15, "Decision card, line 2 (R-P2-6, E13): how much of A the booking app carries (NPV, or the yearly figure when A does not pay back by 2032), and what each year without it leaves with the agencies.")
m("Rec Lines (text)", f"[Rec Line 1 (text)] & {LF} & [Rec Line 2 (text)]", TXT, C15, "Decision card, both lines with a line break (alt text and tables; on the canvas two cards, spike S-7).")
# build step 6: the ink of the card's two signed numbers (the comp's .neg: Burnt Tangerine below zero, on the shown value) and
# the spoken texts of the head and the ledger
m("Rec NPV Ink", f'IF ( ROUND ( [Rec NPV (sel)] / 100000, 0 ) < 0, "{BAD}", "{INK}" )', TXT, C15,
  "Decision card: the ink of A's NPV, Burnt Tangerine when the shown value is below zero (the sign carries it too), Night otherwise.")
m("Rec Run-rate Ink", f'IF ( ROUND ( [Rec Run-rate (sel)] / 100000, 0 ) < 0, "{BAD}", "{INK}" )', TXT, C15,
  "Decision card: the ink of A's profit a year by 2032, Burnt Tangerine when the shown value is below zero, Night otherwise.")
alt_m("Rec Head",
      'VAR a = [Recommended Package] RETURN "Our recommendation: package A. " & CONCATENATEX ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ), '
      'LOOKUPVALUE ( InvestmentProjects[Move Name], InvestmentProjects[ProjectID], PackageProject[ProjectID] ), " + ", '
      'LOOKUPVALUE ( InvestmentProjects[Hero Sort], InvestmentProjects[ProjectID], PackageProject[ProjectID] ), ASC ) & "."',
      "The decision card's head read aloud: the recommendation and its moves, named as the hero table names them, read from the package.")
alt_m("Ledger",
      f'"What package A changes for each of the four findings, " & [Selected Scenario] & " case. " & CONCATENATEX ( ALLNOBLANKROW ( Finding ), '
      f'Finding[Label] & ": " & SUBSTITUTE ( [Ledger Measure (text)], {LF}, ", " ) & "; " & [Ledger 2025 (text)] & " in " & {BASE_YEAR} & ", " & [Ledger 2032 (text)] & " in " & {HORIZON} '
      '& " with A; " & [Ledger Status (text)], ". ", Finding[Ledger Sort], ASC ) & "."',
      "The ledger read aloud, row by row in its own order: the finding, what we track, the two values and the status words.")
_KIOSK = 'VAR kp = MAXX ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Status] = "A" && MoveDecision[Finding] = "F4" ), MoveDecision[ProjectID] ) '
_KHOTELS = "COUNTROWS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] = kp ) )"
_REFRESH = 'VAR rp = MAXX ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Finding] = "F3" && MoveDecision[Tranche] = 3 ), MoveDecision[ProjectID] ) '
_CODE = "VAR c = SELECTEDVALUE ( Finding[Code] ) "
_LM2, _LM1 = LEDGER_MOVES["F2"], LEDGER_MOVES["F1"]
m("Ledger Measure (text)",
  _CODE + REC_IDS + _KIOSK + _REFRESH + "VAR s = [Selected Scenario] "
  "VAR gs = CALCULATE ( SUM ( InvestmentScenarios[SatisfactionChangePts] ), REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = kp, InvestmentScenarios[Scenario] = s ) "
  f'RETURN SWITCH ( c, "F2", "distribution cost, % of room revenue" & {LF} & "{_LM2}", "F1", "operating margin after commissions" & {LF} & "{_LM1}", '
  f'"F4", "self check-in hotels · rooms added" & {LF} & "kiosks live " & ' + month("LOOKUPVALUE ( InvestmentProjects[Completion Date], InvestmentProjects[ProjectID], kp )")
  + ' & "; guest score " & IF ( gs < 0, ' + MINUS + ', "+" ) & FORMAT ( ABS ( gs ), "0.00", "en-US" ) & " there (dataset units)", '
  f'"F3", "refresh of the " & COUNTROWS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] = rp ) ) & " oldest hotels" & {LF} & "why: see What waits, and why" )',
  TXT, C15, "Ledger, 'What we track' (R-P2-5, doc 22 section 4): the measure, a line break, the move(s) that act on it. The kiosks' guest-score change stays in dataset units, never summed, never NPS.")
m("Ledger 2025 (text)",
  _CODE + _KIOSK + 'RETURN SWITCH ( c, "F2", ' + pct1("[Dist Cost % 2025 GI]") + ', "F1", ' + pct1("[KPI Margin after GI]") + ', "F4", "0 of " & ' + _KHOTELS + ' & " · 0", "F3", "not started" )',
  TXT, C15, "Ledger, 2025: distribution cost and the margin after commissions as they were; no kiosk and no added room yet; the refresh not started.")
m("Ledger 2032 (text)",
  _CODE + REC_IDS + _KIOSK + _REFRESH
  + "VAR rooms = SUMX ( FILTER ( ALLNOBLANKROW ( InvestmentProjects[ProjectID], InvestmentProjects[AddedRooms] ), InvestmentProjects[ProjectID] IN aIds ), InvestmentProjects[AddedRooms] ) + 0 "
  'RETURN SWITCH ( c, "F2", ' + pct1("[Dist Cost % 2032 with A (sel)]") + ', "F1", ' + pct1("[Margin after 2032 with A (sel)]") + ', '
  '"F4", IF ( kp IN aIds, ' + _KHOTELS + ', 0 ) & " of " & ' + _KHOTELS + ' & " · " & rooms, "F3", IF ( rp IN aIds, "started", "not started" ) )',
  TXT, C15, "Ledger, 2032 with A (metric contracts M-102, M-103): the 2025 brand plus A's full yearly effect, in 2025 dollars, scenario in view.")
m("Ledger Status (text)",
  _CODE + 'RETURN SWITCH ( c, "F2", ' + share_words("[Dist Cost Rise Undone % (sel)]") + ' & " the rise since 2021 undone", '
  '"F1", ' + share_words("[Margin Fall Recovered % (sel)]") + ' & " the fall since 2023 recovered", '
  f'"F4", "rooms decided at the {GATE_YEAR} gate", "F3", "deferred to the {GATE_YEAR} gate" )',
  TXT, C15, "Ledger status words (P-6): the share of the 2021-2025 rise in distribution cost that A undoes and of the 2023-2025 fall in the margin it recovers, in words; F4 and F3 wait for the gate.")

# ---- Recommended: the capital plan (R-P2-7, N-5) and the one release rule (P-8 check 4)
m("Capital Plan Title (text)",
  f'VAR k = COUNTROWS ( FILTER ( {{ [Tranche 2 Capex], [Tranche 3 Capex] }}, [Value] > 0 ) ) '
  f'RETURN "The $" & FORMAT ( {BUDGET_GI} / 1000000, "#,0", "en-US" ) & "M plan: " & ' + fm("[Tranche 1 Capex]") + f' & " now, " & ' + words("k") + f' & " decisions in {GATE_YEAR}"',
  TXT, C15, "Capital plan title (R-P2-7): the budget, tranche 1 now and the decisions at the gate.")
_T1_YEAR = REC_IDS + "VAR y1 = YEAR ( CALCULATE ( MIN ( InvestmentProjects[Planned Start] ), REMOVEFILTERS ( InvestmentProjects ), TREATAS ( aIds, InvestmentProjects[ProjectID] ) ) ) "
PLAN_LINES = {
    1: ['"Tranche 1 · package A"', _T1_YEAR + "RETURN " + fm("[Tranche 1 Capex]") + ' & " · " & y1'],
    2: [tranche_t(2) + 'RETURN "Tranche 2 · " & ' + T2_NAMES + ' & " +" & MAXX ( th, [@r] ) & " rooms"',
        fm("[Tranche 2 Capex]") + f' & " · {GATE_YEAR} gate"',
        sfm("[Tranche 2 Run-rate]") + ' & " a year once live · " & ' + pct1("[Tranche 2 Year on Cost]") + ' & " a year on cost"'],
    3: [tranche_t(3) + 'RETURN "Tranche 3 · the " & ' + pid_switch("MAXX ( th, [@p] )", MOVE_SENTENCE),
        fm("[Tranche 3 Capex]") + f' & " · {GATE_YEAR} gate"',
        sfm("[Tranche 3 Run-rate]") + ' & " a year once live · " & ' + pct1("[Tranche 3 Year on Cost]") + ' & " a year on cost"'],
    4: ['"Not needed · " & ' + fm("[Not Needed Capex]")],
}
for k, lines in PLAN_LINES.items():
    for i, dax in enumerate(lines, 1):
        m(f"Plan T{k} L{i} (text)", dax, TXT, C15, f"Capital plan, the label of segment {k}, line {i} (one card callout per line: a card value never breaks a line, spike S-7).")
    m(f"Plan T{k} (text)", f" & {LF} & ".join(f"[Plan T{k} L{i} (text)]" for i in range(1, len(lines) + 1)), TXT, C15, f"Capital plan, the label of segment {k}, all lines with line breaks.")
m("Gate Rule (text)",
  # the ONLY release rule in the model (R-P2-7, R-P2-10, P-8 check 4); R-W-2 and R-W-3 quote it, nothing else states one
  REC_IDS + APP_IDS + tranche_t(2)
  + f'VAR pts = - CALCULATE ( SUM ( InvestmentScenarios[DistributionCostChangePts] ), {APP_T}, InvestmentScenarios[Scenario] = "Low" ) * 100 '
  f'RETURN "The {GATE_YEAR} gate, once all " & ' + words("COUNTROWS ( aIds )") + ' & " moves are live: the Board releases tranche 2 if distribution cost has fallen at least " & FORMAT ( pts, "0.0", "en-US" ) '
  '& " points (the app\'s Low case) and " & ' + T2_NAMES + f' & " still topped 90% in 6 of the last 12 months. The refresh comes back to the same meeting with a case that looks beyond " & {HORIZON} & ". A decision rule, not a forecast."',
  TXT, C15, "The gate rule (R-P2-7), the one release rule of the report: when the Board releases tranche 2 and when the refresh comes back. The 0.6 points are the app's Low-case change in distribution cost.")
m("Gate Rule Short (text)", f'"At the {GATE_YEAR} gate, if the app delivers and the airports stay full."', TXT, C15,
  "The gate in one line for the What-waits table (When we decide); the full rule is Gate Rule (text).")
m("Milestones (text)",
  REC_IDS + 'VAR t = ADDCOLUMNS ( aIds, "@d", LOOKUPVALUE ( InvestmentProjects[Completion Date], InvestmentProjects[ProjectID], [@p] ), "@dep", LOOKUPVALUE ( InvestmentProjects[DependsOn], InvestmentProjects[ProjectID], [@p] ) ) '
  "VAR pb = [Preset A Payback Year] "
  'RETURN CONCATENATEX ( t, ' + pid_switch("[@p]", MOVE_LABEL) + ' & " live " & ' + month("[@d]")
  + ' & IF ( [@dep] <> "", " (" & IF ( ' + is_plural("[@p]") + ', "they need", "it needs" ) & " the " & LOWER ( ' + pid_switch("[@dep]", MOVE_LABEL) + ' ) & ")", "" ), " · ", [@d], ASC ) '
  f'& " · " & IF ( ISBLANK ( pb ), "Not cash positive by " & {HORIZON}, "Cash positive " & pb ) & " (" & [Selected Scenario] & ")"',
  TXT, C15, "Capital plan milestone strip: the go-live of A's moves in order, the dependency, and the year A turns cash positive (undiscounted cumulative), scenario in view.")

# ---- build step 7 (doc 23): what the hero table and the capital plan need beside the numbers and the text
# the inks of two hero columns (doc 22 section 3): the status word in a text colour (Warm Grey is 3.5:1 as text), the NPV
# in Burnt Tangerine below zero, on the shown value
m("Move Status Ink", f'VAR st = {MOVE_ST} RETURN IF ( ISBLANK ( st ), BLANK (), SWITCH ( st, "A", "{ACCENT}", "2028 gate", "{INK}", "{INK2}" ) )', TXT, C15,
  "Hero row: the text colour of the status word (Deep Coffee for package A, Night for the 2028 gate, Dusk for not now). The bars keep the mark colours (Move Status Color).")
m("Move NPV Ink", f'VAR v = [Move NPV (num)] RETURN IF ( ROUND ( v / 10000, 0 ) < 0, "{BAD}", "{INK}" )', TXT, C15,
  "Hero row: the ink of the move's NPV, Burnt Tangerine when the shown value is below zero (the sign carries it too), Night otherwise.")
_A32 = "CALCULATE ( [TT Year A ({0})], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = " + HORIZON + " )"
alt_m("Hero",
      _HERO_T + 'VAR s = [Selected Scenario] '
      'RETURN "The ten moves ranked by what each earns a year on its cost, with the finding each answers, its status and its NPV through " & ' + HORIZON + ' & ", " & s & " case. " '
      '& [Hero Title (text)] & ". Highest: " & CONCATENATEX ( TOPN ( 3, t, [@o], ASC ), LOOKUPVALUE ( InvestmentProjects[Move Name], InvestmentProjects[ProjectID], [@p] ) & " " & '
      + pct1("[@y]") + ' & " a year on cost, NPV " & ' + sfm("[@v]") + ', "; ", [@o], ASC ) & ". The two marked lines are our " & FORMAT ( ' + RATE + ', "0%", "en-US" ) & " cost of money and NPV zero."',
      "The hero table read aloud: what it ranks, the title's verdict, the three highest moves with both numbers, and what the two reference lines mean.")
alt_m("Plan Bar",
      '"How the $" & FORMAT ( ' + BUDGET_GI + ' / 1000000, "#,0", "en-US" ) & "M budget is planned, in four parts. " & '
      + ' & ". " & '.join(f'SUBSTITUTE ( [Plan T{k} (text)], {LF}, ", " )' for k in (1, 2, 3, 4)) + ' & "."',
      "The capital plan bar read aloud: the four segments with their labels, in order.")
alt_m("Plan Cum",
      "VAR pb = [Preset A Payback Year] VAR s = [Selected Scenario] "
      'RETURN "Package A, cumulative net impact by year to " & ' + HORIZON + ' & " in the three cases. By " & ' + HORIZON + ' & ": Low " & ' + sfm(_A32.format("Low"))
      + ' & ", Expected " & ' + sfm(_A32.format("Expected")) + ' & ", High " & ' + sfm(_A32.format("High"))
      + ' & ". In the " & s & " case " & IF ( ISBLANK ( pb ), "A is not cash positive by " & ' + HORIZON + ', "A is cash positive from " & pb ) & '
      + f'". The Board decides on the rest at the {GATE_YEAR} gate."',
      "The capital plan's cumulative chart read aloud: the three end points, the cash-positive year in the case in view, and the gate.")

# ---- What waits, and why (R-W-1 to R-W-3)
_NPV_SEL = 'VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( ALLNOBLANKROW ( Package ), "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
m("Proof Title (text)",
  _NPV_SEL + "VAR av = [Rec NPV (sel)] VAR beat = COUNTROWS ( FILTER ( t, [@v] > av ) ) + 0 "
  f'RETURN "We checked all " & COUNTROWS ( t ) & " packages the rules allow: " & IF ( beat = 0, "none beats A", beat & IF ( beat = 1, " beats A", " beat A" ) ) & " through " & {HORIZON}',
  TXT, C15, "Proof chart title (R-W-1): every package the contest rules allow, and how many beat A's NPV through 2032 in the case in view (none, in all three).")
m("Proof Subtitle (text)",
  _NPV_SEL + "VAR pos = FILTER ( t, [@v] >= 0 ) VAR k = COUNTROWS ( pos ) + 0 VAR cap = ( INT ( MAXX ( pos, Package[CapexUSD] ) / 5000000 ) + 1 ) * 5 "
  f'RETURN IF ( k = 0, "None pays back by " & {HORIZON} & ".", "Only " & k & IF ( k = 1, " pays", " pay" ) & " back by " & {HORIZON} & IF ( k = 1, ", under $", ", all under $" ) & cap & "M." ) & " Each dot is a package."',
  TXT, C15, "Proof chart subtitle: how many packages pay back by 2032 in the case in view and the $5M step above the largest of them.")
_WK = "VAR k = SELECTEDVALUE ( WaitOption[Key] ) "
_BV = (REC_IDS + 'VAR b = [Preset B Package] VAR bIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = b ), "@p", PackageProject[ProjectID] ) '
       "VAR capA = [Rec Capex] VAR capB = [Preset B Capex] VAR npvA = [Rec NPV (sel)] VAR npvB = [Preset B NPV (sel)] ")
_CV = ('VAR cP = [Preset C Package] VAR cIds = ADDCOLUMNS ( SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = cP ), "@p", PackageProject[ProjectID] ), '
       '"@o", LOOKUPVALUE ( InvestmentProjects[Hero Sort], InvestmentProjects[ProjectID], [@p] ) ) ')
m("Wait Numbers (text)",
  _WK + _BV + _CV
  + "VAR bLo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = b ) VAR bHi = CALCULATE ( SUM ( Package[NPV High] ), REMOVEFILTERS ( Package ), Package[PackageID] = b ) "
  'RETURN SWITCH ( k, '
  f'"B", ' + fm("capB") + f' & " capex" & {LF} & ' + sfm("npvB") + f' & " NPV through " & {HORIZON} & {LF} & ' + sfm("[Preset B Run-rate (sel)]") + f' & " a year by " & {HORIZON} & {LF} & ' + sfm("bLo") + ' & " to " & ' + sfm("bHi") + ', '
  f'"T2", ' + fm("[Tranche 2 Capex]") + f' & " capex" & {LF} & ' + sfm("[Tranche 2 Run-rate]") + f' & " a year once live" & {LF} & ' + pct1("[Tranche 2 Year on Cost]") + f' & " a year on cost" & {LF} & "no NPV shown", '
  f'"T3", ' + fm("[Tranche 3 Capex]") + f' & " capex" & {LF} & ' + sfm("[Tranche 3 Run-rate]") + f' & " a year once live" & {LF} & ' + pct1("[Tranche 3 Year on Cost]") + f' & " a year on cost" & {LF} '
  '& "package C (" & CONCATENATEX ( cIds, ' + pid_switch("[@p]", MOVE_LABEL) + ', " + ", [@o], ASC ) & ") " & ' + sfm("[Preset C NPV (sel)]") + f' & " through " & {HORIZON} )',
  TXT, C15, "What waits, 'The numbers' (R-W-2): four lines per option, scenario in view; the tranches show no NPV (a gated start is not modelled), the refresh its package C for reference.")
_RENO = ('VAR gh = CALCULATETABLE ( VALUES ( Hotels[HotelID] ), REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( Brands ), Hotels[Brand] = "Goodnight Inn" ) '
         'VAR ly = MAXX ( gh, YEAR ( LOOKUPVALUE ( Hotels[LastRenovationDate], Hotels[HotelID], Hotels[HotelID] ) ) ) '
         'VAR grp = FILTER ( gh, YEAR ( LOOKUPVALUE ( Hotels[LastRenovationDate], Hotels[HotelID], Hotels[HotelID] ) ) = ly ) VAR rest = EXCEPT ( gh, grp ) ')
_NPS_AT = "CALCULATE ( [NPS (weighted)], REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( Brands ), TREATAS ( {0}, Hotels[HotelID] ), REMOVEFILTERS ( 'Date' ), 'Date'[Year] = {1} )"
m("Wait Why (text)",
  _WK + _BV + tranche_t(2) + _RENO
  + f'VAR nh = COUNTROWS ( gh ) VAR rA = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR rB = CALCULATE ( SUM ( Package[HotelsRated] ), REMOVEFILTERS ( Package ), Package[PackageID] = b ) '
  "VAR g21 = " + _NPS_AT.format("grp", 2021) + " VAR g25 = " + _NPS_AT.format("grp", 2025) + " VAR r21 = " + _NPS_AT.format("rest", 2021) + " VAR r25 = " + _NPS_AT.format("rest", 2025) + " "
  'RETURN SWITCH ( k, '
  '"B", "Lifts guest scores in " & IF ( rB = nh, "all ", "" ) & rB & " hotels instead of " & rA & ".", '
  '"T2", CONCATENATEX ( th, [@n], " and ", [@m], DESC, [@o], ASC ) & " topped 90% in " & CONCATENATEX ( th, [@m], " and ", [@m], DESC, [@o], ASC ) & " of the last 24 months.", '
  '"T3", "Renovation works here: the " & ' + words("COUNTROWS ( grp )") + ' & " hotels renovated in " & ly & IF ( ROUND ( g25, 0 ) = ROUND ( g21, 0 ), " held their NPS near ", " moved their NPS to " ) & ' + sint("g25")
  + ' & " while the rest of the brand " & IF ( r25 < r21, "fell", "rose" ) & " to " & ' + pt1("r25") + ' & "." )',
  TXT, C15, "What waits, 'Why it's on the table' (R-W-2): B's wider guest-score reach, the airports' months above 90 %, and the hotels renovated last against the rest of the brand (NPS 2021 to 2025).")
m("Wait WhyNot (text)",
  _WK + _BV + _KIOSK + tranche_t(2)
  + "VAR dc = capB - capA VAR dn = ( ROUND ( npvA / 100000, 0 ) - ROUND ( npvB / 100000, 0 ) ) * 100000 VAR nNeg = COUNTROWS ( FILTER ( th, ROUND ( [@v] / 100000, 0 ) < 0 ) ) "
  + f"VAR t3y = [Tranche 3 Year on Cost] VAR rate = {RATE} "
  "RETURN SWITCH ( k, "
  '"B", ' + fm("ABS ( dc )") + ' & IF ( dc >= 0, " more", " less" ) & " than A for " & ' + fm("ABS ( dn )") + ' & IF ( dn >= 0, " less", " more" ) & " through " & ' + HORIZON
  + ' & IF ( kp IN aIds && NOT ( kp IN bIds ), ", and it leaves the queues at the " & ' + _KHOTELS + ' & " busiest desks", "" ) & ".", '
  '"T2", SWITCH ( nNeg, COUNTROWS ( th ), "Neither pays back by ", 0, "Both pay back by ", "Only one pays back by " ) & ' + HORIZON + ' & " (" & CONCATENATEX ( th, ' + sfm("[@v]") + ', " and ", [@m], DESC, [@o], ASC ) & ").", '
  '"T3", "It earns " & ' + pct1("t3y") + ' & " a year on cost" & IF ( ROUND ( t3y, 3 ) >= rate, '
  '" but does not pay back by " & ' + HORIZON + ' & " (" & ' + sfm("[Tranche 3 NPV]") + ' & ")", '
  'IF ( rate - t3y < 0.005, ", just under our ", ", under our " ) & FORMAT ( rate, "0%", "en-US" ) & " cost of money" ) '
  '& ". The data does not price the cost of waiting, so this case is understated." )',
  TXT, C15, "What waits, 'Why not now' (R-W-2; doc 22 section 6, question 2): B against A, the airports' NPV through 2032, and the refresh against our cost of money "
            "(at or above 8 %, only High, it says that it still does not pay back by 2032).")
m("Tranche 3 NPV", tranche(3) + f"RETURN CALCULATE ( [NPV @ 8%], {TTREAT} )", SUSDM, C15, "NPV through 2032 of tranche 3 (the refresh) alone, scenario in view; said only where 'a year on cost' alone would mislead (What waits, High).")
m("Wait When (text)",
  _WK + "VAR ext = " + _EXT +
  'VAR t2 = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( MoveDecision ), MoveDecision[Tranche] = 2 ), "@p", MoveDecision[ProjectID] ) '
  "VAR kx = MAXX ( EXCEPT ( ext, t2 ), [@p] ) VAR kh = " + HOTEL_OF.format("kx") + " "
  'RETURN SWITCH ( k, "B", "Not planned.", '
  f'"T2", [Gate Rule Short (text)] & IF ( COUNTROWS ( EXCEPT ( ext, t2 ) ) = 1, {LF} & ' + COPY_NAME.format("kh") + ' & " (" & FORMAT ( ' + AT_HOTEL.format("[Occupancy % 2025]", "kh") + ', "0%", "en-US" ) & " full) is not on the list.", "" ), '
  f'"T3", "Back at the {GATE_YEAR} gate, with a case that looks beyond " & {HORIZON} & "." )',
  TXT, C15, "What waits, 'When we decide' (R-W-2): B is not planned; the tranches come back at the gate (the short rule), with the extension that is not on the list.")
m("Cmp Alts Title (text)",
  f"VAR a32 = {CUM32('A')} VAR b32 = {CUM32('B')} VAR pbC = [Preset C Payback Year] "
  'RETURN "Cumulative net impact, $M: B " & IF ( ABS ( a32 - b32 ) < 1000000, "ends within $1M of A", IF ( b32 < a32, "trails A by ", "ends ahead of A by " ) & ' + fm("ABS ( a32 - b32 )") + f' ) & " by " & {HORIZON} '
  f'& "; C " & IF ( ISBLANK ( pbC ), "is not cash positive by " & {HORIZON}, "is cash positive from " & pbC )',
  TXT, C15, "Title of the comparison chart in What waits (R-W-3, R-G2): B against A by 2032, and whether C turns cash positive by 2032, scenario in view.")

# ---- Build your own (R-B-1, R-B-2)
m("Build Picked (text)", BIDS + f'RETURN "Picked: " & n & IF ( n = 1, " move, ", " moves, " ) & ' + fm("COALESCE ( [Build Capex], 0 )") + ' & " of " & ' + fm(BUDGET_GI),
  TXT, C15, "Selector footer: how many moves are picked and their capex against the budget.")
m("Build Run-rate (text)", BIDS + "RETURN IF ( n = 0, BLANK (), " + sfm("[Build Run-rate (sel)]") + " )", TXT, C15, "Your plan: profit a year by 2032, scenario in view; blank while nothing is picked.")
m("Build A Year on Cost (text)", BIDS + "RETURN IF ( n = 0, BLANK (), " + pct1("[Build A Year on Cost (sel)]") + " )", TXT, C15, "Your plan: a year on cost, scenario in view; blank while nothing is picked.")
m("TT Payback Color", f'"{INK}"', TXT, C10,
  "Font colour of the package tooltip's verdict line: Night (the words carry the verdict). Defined in step 4 of doc 23: the report bound this measure while the model had none (doc 21 PB defect).")

# ---- the slot map of the text (doc 21 P-8): every slot of rebuild-v10-spec.json -> text that a measure prints.
# A slot is a measure name, or a list of lines (joined by a line break), each line a measure or a list of parts joined
# without a separator. A part that starts with "=" is literal text on the canvas (a card label, a text-box run).
# Tables: rows, sort, and one entry per spec column (None = an image column, empty in the spec).
# TEXT_STATIC: the slots that are typed in opzet_report.py (text boxes, buttons, slicer items, hover tags), with the
# step that builds them; build_checks.py reports them as not checked here.


def _kpi(code, label, kp):
    return [f"={code} · {label}", f"KPI {kp} GI (text)", f"KPI {kp} Context (text)"]


_P2_FRAME = {"z_headline2": "Headline P2 (text)", "c_subtitle2": "Subtitle P2 (text)", "z_footer2": "Footer P2 (text)"}
TEXT_SLOTS = {
    "P1": {
        "z_headline": "Headline P1 (text)", "c_subtitle": "Subtitle P1 Briefing (text)",
        "kpi_occ": _kpi("F4", "Occupancy", "Occupancy"), "kpi_margin": _kpi("F1", "Operating margin after commissions", "Margin after"),
        "kpi_ota": _kpi("F2", "Room revenue booked through online agencies", "OTA"), "kpi_nps": _kpi("F3", "Guest quality: net promoter score (−100 to +100)", "NPS"),
        "c_f1_title": "F1 Title (text)", "c_f1_note": "F1 Note (text)",
        "c_f2_title": "F2 Title (text)", "c_f2_note": "F2 Note (text)",
        "tbl_f2_folio": {"rows": "FolioLine[Line]", "sort": "FolioLine[Sort]", "cols": ["FolioLine[Line]", "Folio OTA Guest (text)", "Folio Direct Guest (text)"]},
        "c_f3_title": "F3 Title (text)", "c_f3_count": "F3 Count (text)", "c_f3_note": "F3 Note (text)",
        "c_f4_title": "F4 Title (text)", "c_f4_note": "F4 Note (text)", "lnk_f4": "Link F4 (text)",
        "c_f4_rows": [["=Airport ", "Occupancy Airport GI (text)"], ["=City ", "Occupancy City GI (text)"], ["=Highway ", "Occupancy Highway GI (text)"]],
        "chip_def": "Chip Definitions (text)",
    },
    "rec": dict(_P2_FRAME, **{
        "c_hero_title": "Hero Title (text)",
        "tbl_hero": {"rows": "InvestmentProjects[Move Name]", "sort": "InvestmentProjects[Hero Sort]", "filter": 'TREATAS ( { "Goodnight Inn" }, InvestmentProjects[Brand] )',
                     "cols": ["InvestmentProjects[Move Name]", "Move Answers (text)", "Move Status (text)", None, "Move Yield (text)", None, "Move NPV (text)"]},
        "c_rec_nums": ["Rec Capex (text)", "=capex", "Rec NPV (text)", "=NPV through 2032", "Rec Run-rate (text)", "=a year by 2032", "Rec A Year on Cost (text)", "=a year on cost"],
        "c_rec_lines": ["Rec Line 1 (text)", "Rec Line 2 (text)"],
        "tbl_ledger": {"rows": "Finding[Label]", "sort": "Finding[Ledger Sort]",
                       "cols": ["Finding[Label]", "Ledger Measure (text)", "Ledger 2025 (text)", "Ledger 2032 (text)", "Ledger Status (text)"]},
        "c_plan_title": "Capital Plan Title (text)",
        "c_plan_t1": ["Plan T1 L1 (text)", "Plan T1 L2 (text)"], "c_plan_t2": ["Plan T2 L1 (text)", "Plan T2 L2 (text)", "Plan T2 L3 (text)"],
        "c_plan_t3": ["Plan T3 L1 (text)", "Plan T3 L2 (text)", "Plan T3 L3 (text)"], "c_plan_t4": "Plan T4 L1 (text)",
        "c_plan_gate": "Gate Rule (text)", "c_plan_milestones": "Milestones (text)",
    }),
    "alts": dict(_P2_FRAME, **{
        "c_scatter_title_s": "Proof Title (text)", "c_scatter_sub": "Proof Subtitle (text)",
        "tbl_waits": {"rows": "WaitOption[Title]", "sort": "WaitOption[Sort]",
                      "cols": ["WaitOption[Title]", "Wait Numbers (text)", "Wait Why (text)", "Wait WhyNot (text)", "Wait When (text)"]},
        "ch_cmp_alts.title": "Cmp Alts Title (text)",
    }),
    "build": dict(_P2_FRAME, **{
        "c_scatter_title_s": "Proof Title (text)", "c_scatter_sub": "Proof Subtitle (text)",
        # the selector table is not filtered by the selector (doc 21 section 8): all ten rows in every state
        "tbl_moves": {"rows": "BuildMove[Short Name]", "sort": "BuildMove[Sort]", "unfiltered": True,
                      "cols": ["Move Answers (text)", "Move Capex (text)", "Move NPV (text)", "Move Run-rate (text)"]},
        "c_sel_footer": "Build Picked (text)", "c_you_title": "Build Title (text)",
        "c_you_nums": ["Build Capex (text)", "=capex", "Build NPV (text)", "=NPV through 2032", "Build Run-rate (text)", "=a year by 2032", "Build A Year on Cost (text)", "=a year on cost"],
        "c_you_range": "Build Range (text)", "c_you_rules": "Build Valid (text)",
        "ch_cmp_build.title": "Cmp Build Title (text)",
    }),
}
TEXT_STATIC = {  # slot -> where the text is typed (checked against the spec by the report steps, rule 7 of doc 23)
    **{s: "opzet_report.py, step 5" for s in ("z_eyebrow", "c_f1_kicker", "c_f2_kicker", "c_f3_kicker", "c_f4_kicker", "lnk_f1", "lnk_f2", "lnk_f3",
                                              "tag_f3", "tag_f4", "z_footer", "btn_next", "lbl_f4_kingston", "lbl_f4_orlando", "lbl_f4_kuala_lumpur",
                                              "lbl_f4_kansas_city", "lbl_f4_phoenix", "lbl_f4_gatwick_montreal", "lbl_f4_toronto")},
    **{s: "opzet_report.py, step 6" for s in ("z_eyebrow2", "btn_back", "tab_rec_on", "tab_rec_off", "tab_alts_on", "tab_alts_off", "tab_build_on", "tab_build_off",
                                              "lbl_scenario", "sl_scenario", "chip_def2", "c_rec_head", "c_ledger_caption", "btn_build_invite")},
    **{s: "opzet_report.py, step 7" for s in ("lbl_hero_8", "lbl_hero_0", "c_hero_caption", "tag_plan_cum")},
    **{s: "opzet_report.py, step 8" for s in ("tag_scatter_s", "c_waits_head", "tag_cmp_alts")},
    **{s: "opzet_report.py, step 9" for s in ("c_build_head", "sl_moves", "tag_cmp_build")},
}


# MoveDecision: decision data (D2, D4), not source data. Finding and the gate tranche are typed above (MOVE_FINDING,
# MOVE_GATE); status "A" and tranche 1 are read from Package[Preset], so the table follows package A.
MOVE_DECISION = (
    'VAR a = LOOKUPVALUE ( Package[PackageID], Package[Preset], "A" )\n'
    'VAR aIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ), "@p", PackageProject[ProjectID] )\n'
    'VAR decided = DATATABLE ( "xPid", STRING, "xFinding", STRING, "xGate", INTEGER, { '
    + ", ".join(f'{{ "{p}", "{f}", {MOVE_GATE.get(p, 0)} }}' for p, f in sorted(MOVE_FINDING.items())) + " } )\n"
    "RETURN\n"
    "    SELECTCOLUMNS (\n"
    "        decided,\n"
    '        "ProjectID", [xPid],\n'
    '        "Finding", [xFinding],\n'
    '        "Status", SWITCH ( TRUE (), [xPid] IN aIds, "A", [xGate] > 0, "2028 gate", "not now" ),\n'
    '        "Tranche", SWITCH ( TRUE (), [xPid] IN aIds, 1, [xGate] > 0, [xGate], BLANK () )\n'
    "    )\n"
)

BUILD_MOVE = r"""
VAR Proj = FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" )
RETURN
    SELECTCOLUMNS (
        Proj,
        "ProjectID", InvestmentProjects[ProjectID],
        "Short Name", InvestmentProjects[Short Name],
        "Waterfall Label", SWITCH ( InvestmentProjects[ProjectID], "GI-01", "App", "GI-02", "Kiosks", "GI-03", "Energy", "GI-04", "Toronto +40", "GI-05", "Gatwick +40", "GI-06", "Kingston +40", "GI-07", "Refresh 10", "GI-08", "Boston", "GI-09", "Breakfast", "GI-10", "Rev. mgmt", InvestmentProjects[Short Name] ),
        "Sort", VAR p = InvestmentProjects[ProjectID]
            RETURN RANKX (
                Proj,
                VAR pp = InvestmentProjects[ProjectID] RETURN SUMX ( FILTER ( ProjectCashflow, ProjectCashflow[ProjectID] = pp && ProjectCashflow[Scenario] = "Expected" ), ( ProjectCashflow[Benefit] - ProjectCashflow[Capex] - ProjectCashflow[Disruption] ) * ProjectCashflow[DiscountFactor] ),
                SUMX ( FILTER ( ProjectCashflow, ProjectCashflow[ProjectID] = p && ProjectCashflow[Scenario] = "Expected" ), ( ProjectCashflow[Benefit] - ProjectCashflow[Capex] - ProjectCashflow[Disruption] ) * ProjectCashflow[DiscountFactor] ),
                DESC, Dense
            ),
        "Growth", InvestmentProjects[GrowthInitiative],
        "Answers", InvestmentProjects[Answers Finding]
    )
"""

KPI_ROWS = [  # Sort, Key, FindingLabel, Measure, Direction, Format, DeltaScale, DeltaUnit, DeltaFormat
    # Read along the brand promise "A good night. A fair price." and Keller's ladder (goodnight-inn-hanger
    # brand-guide.md section 2): salience = booked with us, performance = a good night, judgment = a fair price.
    # NPS is the last line of F3's evidence, a guest-quality signal, not a resonance rung or the brand's one number:
    # it does not predict growth better than satisfaction (plan 09 R2, Keiningham et al. 2007; CREDITS.md).
    # Not on the v3 canvas (BUILD_LOG); kept for the comparison table measures.
    (1, "occ", "F1 · Full, margin slipping", "Occupancy", 1, "0.0%", 100, "pt", "0.0"),
    (2, "adr", "", "Average daily rate (segment)", 0, "$#,0", 1, "$", "0"),
    (3, "revpar", "", "RevPAR (segment)", 0, "$#,0", 1, "$", "0"),
    (4, "gop", "", "GOP margin before commissions", 1, "0.0%", 100, "pt", "0.0"),
    (5, "gopa", "", "GOP margin after commissions", 1, "0.0%", 100, "pt", "0.0"),
    (6, "ota", "F2 · Booked with us?", "OTA share of room revenue", -1, "0.0%", 100, "pt", "0.0"),
    (7, "direct", "", "Direct share (web, app, phone)", 1, "0.0%", 100, "pt", "0.0"),
    (8, "dist", "", "Distribution cost, % of room revenue", -1, "0.0%", 100, "pt", "0.0"),
    (9, "comfort", "F3 · A good night?", "Room comfort score (0 to 10)", 1, "0.00", 1, "", "0.00"),
    (10, "roomcond", "", "Room-condition complaints per 1,000", -1, "0.00", 1, "", "0.00"),
    (11, "compl", "", "All complaints per 1,000 room nights", -1, "0.0", 1, "", "0.0"),
    (12, "value", "F3 · A fair price?", "Value for money score (0 to 10)", 1, "0.00", 1, "", "0.00"),
    (13, "nps", "", "Net promoter score (guest-quality signal)", 1, "+0.0;\u22120.0;0.0", 1, "", "0.0"),
]

PACKAGE = r"""
VAR LastYear = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Impact horizon" )
VAR Budget = LOOKUPVALUE ( Brands[InvestmentBudgetUSD], Brands[Brand], "Goodnight Inn" )
VAR CF =
    SELECTCOLUMNS (
        ProjectCashflow,
        "@CPid", ProjectCashflow[ProjectID], "@CScn", ProjectCashflow[Scenario], "@CYr", YEAR ( ProjectCashflow[Month] ),
        "@CNet", ProjectCashflow[Benefit] - ProjectCashflow[Capex] - ProjectCashflow[Disruption],
        "@CDf", ProjectCashflow[DiscountFactor], "@CBen", ProjectCashflow[Benefit]
    )
VAR Proj =
    ADDCOLUMNS (
        SELECTCOLUMNS (
            FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" ),
            "@Pid", InvestmentProjects[ProjectID],
            "@Capex", InvestmentProjects[CapexUSD],
            "@Growth", IF ( InvestmentProjects[GrowthInitiative] = "Yes", 1, 0 ),
            "@Dep", InvestmentProjects[DependsOn],
            "@Added", InvestmentProjects[AddedRooms],
            "@Refresh", IF ( InvestmentProjects[Category] = "Renovation", 1, 0 )
        ),
        "@Bit", VALUE ( RIGHT ( [@Pid], 2 ) ) - 1,
        "@Rated", VAR p = [@Pid] RETURN IF ( LOOKUPVALUE ( InvestmentScenarios[SatisfactionChangePts], InvestmentScenarios[ProjectID], p, InvestmentScenarios[Scenario], "Expected" ) > 0, 1, 0 ),
        "@NpvL", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "Low" ), [@CNet] * [@CDf] ),
        "@NpvE", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "Expected" ), [@CNet] * [@CDf] ),
        "@NpvH", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "High" ), [@CNet] * [@CDf] ),
        "@RrL", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "Low" && [@CYr] = LastYear ), [@CBen] ),
        "@RrE", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "Expected" && [@CYr] = LastYear ), [@CBen] ),
        "@RrH", VAR p = [@Pid] RETURN SUMX ( FILTER ( CF, [@CPid] = p && [@CScn] = "High" && [@CYr] = LastYear ), [@CBen] )
    )
VAR Masks = SELECTCOLUMNS ( GENERATESERIES ( 0, POWER ( 2, COUNTROWS ( Proj ) ) - 1, 1 ), "@Mask", [Value] )
VAR PkgRows =
    ADDCOLUMNS (
        Masks,
        "@Ids", VAR m = [@Mask] RETURN CONCATENATEX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), RIGHT ( [@Pid], 2 ), "+", [@Bit], ASC ),
        "@N", VAR m = [@Mask] RETURN COUNTROWS ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ) ) + 0,
        "@G", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@Growth] ) + 0,
        "@Capex", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@Capex] ) + 0,
        "@Broken", VAR m = [@Mask] VAR inP = FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ) VAR have = SELECTCOLUMNS ( inP, "@Have", [@Pid] )
            RETURN COUNTROWS ( FILTER ( inP, [@Dep] <> "" && NOT ( [@Dep] IN have ) ) ) + 0,
        "@Added", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@Added] ) + 0,
        "@Refresh", VAR m = [@Mask] RETURN MAXX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@Refresh] ) + 0,
        "@Rated", VAR m = [@Mask] VAR rp = SELECTCOLUMNS ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 && [@Rated] = 1 ), "@Rp", [@Pid] )
            RETURN COUNTROWS ( DISTINCT ( SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjectProperties ), InvestmentProjectProperties[ProjectID] IN rp ), "@H", InvestmentProjectProperties[HotelID] ) ) ) + 0,
        "@NpvL", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@NpvL] ),
        "@NpvE", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@NpvE] ),
        "@NpvH", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@NpvH] ),
        "@RrL", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@RrL] ),
        "@RrE", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@RrE] ),
        "@RrH", VAR m = [@Mask] RETURN SUMX ( FILTER ( Proj, MOD ( INT ( m / POWER ( 2, [@Bit] ) ), 2 ) = 1 ), [@RrH] )
    )
VAR Valid = FILTER ( PkgRows, [@N] >= 3 && [@G] >= 1 && [@Capex] <= Budget && [@Broken] = 0 )
RETURN
    SELECTCOLUMNS (
        Valid,
        "PackageID", [@Ids], "Mask", [@Mask], "Projects", [@N], "Growth", [@G], "CapexUSD", [@Capex],
        "ContainsRefresh", IF ( [@Refresh] = 1, "Yes", "No" ), "RoomsAdded", [@Added], "HotelsRated", [@Rated],
        "NPV Low", [@NpvL], "NPV Expected", [@NpvE], "NPV High", [@NpvH],
        "RunRate Low", [@RrL], "RunRate Expected", [@RrE], "RunRate High", [@RrH]
    )
"""

PACKAGE_PROJECT = r"""
SELECTCOLUMNS (
    GENERATE (
        SELECTCOLUMNS ( ALLNOBLANKROW ( Package ), "@Pkg", Package[PackageID], "@Mask", Package[Mask] ),
        VAR m = [@Mask]
        RETURN
            FILTER (
                SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( InvestmentProjects ), InvestmentProjects[Brand] = "Goodnight Inn" ), "@Pid", InvestmentProjects[ProjectID] ),
                MOD ( INT ( m / POWER ( 2, VALUE ( RIGHT ( [@Pid], 2 ) ) - 1 ) ), 2 ) = 1
            )
    ),
    "PackageID", [@Pkg],
    "ProjectID", [@Pid]
)
"""

# A, B and C only (07-fixgids K1/K2, Björn 7 Nov): fixed packages, each chosen once by its rule on the Expected case
# (Package[Preset]). The 456 coded entries and their duplicates of A and B are gone; the scatter covers the rest.
# The labels name what each package does against A (B and C swap the kiosks for another answer to F3); the
# selection rules are in Package[Preset], the composition is checked in 08-fixes-review-v2.md.
PLAN_SELECTOR = r"""
DATATABLE (
    "Key", STRING, "Label", STRING, "Sort", INTEGER,
    {
        { "A", "A · Our recommendation", 1 },
        { "B", "B · Breakfast instead of kiosks", 2 },
        { "C", "C · Why not renovate?", 3 }
    }
)
"""

# Package[Preset]: the three packages, picked once on the Expected case so the scatter, the panel and the plan show
# the same package in every scenario (REVIEW B1/M6). A: highest NPV. B: most hotels with a dataset guest-score
# effect among packages with NPV at least zero, ties by NPV. C: highest NPV with the refresh of the ten oldest hotels.
# Only the four columns it reads: ALLNOBLANKROW ( Package ) would depend on this column too (circular).
# Keyed on Mask, not PackageID: PackageID is sorted by Draw Rank, which reads this column, and a sort column may not
# depend on the column it sorts.
PRESET_COL = (
    "VAR me = Package[Mask] "
    "VAR t = ALLNOBLANKROW ( Package[Mask], Package[NPV Expected], Package[HotelsRated], Package[ContainsRefresh] ) "
    "VAR a = MAXX ( TOPN ( 1, t, Package[NPV Expected], DESC ), Package[Mask] ) "
    "VAR b = MAXX ( TOPN ( 1, FILTER ( t, Package[NPV Expected] >= 0 ), Package[HotelsRated], DESC, Package[NPV Expected], DESC ), Package[Mask] ) "
    'VAR c = MAXX ( TOPN ( 1, FILTER ( t, Package[ContainsRefresh] = "Yes" ), Package[NPV Expected], DESC ), Package[Mask] ) '
    'RETURN SWITCH ( me, a, "A", b, "B", c, "C", "" )'
)


def measures_table():
    out = ["/// Measure home for the three sketches. Base measures read columns; everything else reads measures.", "table _Measures", f"\tlineageTag: {tag('table._Measures')}", ""]
    for name, dax, fmt, folder, doc in MEASURES:
        out.append(f"\t/// {doc}")
        out.append(f"\tmeasure {q(name)} = {dax}")
        if name not in FMT_DEFS:  # never both: the engine refuses a measure with a static and a dynamic format string
            out.append(f"\t\tformatString: {fmt}")
        out.append(f"\t\tdisplayFolder: {folder}")
        if name in IMAGE_MEASURES:
            out.append("\t\tdataCategory: ImageUrl")
        out.append(f"\t\tlineageTag: {tag('measure.' + name)}")
        out.append("")
        if name in FMT_DEFS:
            # TMDL: formatStringDefinition is a child object, so it comes AFTER the measure's own properties, in a
            # backtick block (spike S-1, 13 Nov: right after the expression Desktop refuses the project, "Invalid indentation")
            out.append("\t\tformatStringDefinition = ```")
            out.append(f"\t\t\t\t{FMT_DEFS[name]}")
            out.append("\t\t\t\t```")
            out.append("")
    out.append("\tcolumn Placeholder")
    out.append("\t\tdataType: string")
    out.append("\t\tisHidden")
    out.append(f"\t\tlineageTag: {tag('_Measures.Placeholder')}")
    out.append("\t\tsummarizeBy: none")
    out.append("\t\tsourceColumn: Placeholder")
    out.append("")
    out.append("\tpartition _Measures = m")
    out.append("\t\tmode: import")
    out.append("\t\tsource =")
    out.append("\t\t\t\tlet")
    out.append('\t\t\t\t    Source = #table({"Placeholder"}, {{"x"}})')
    out.append("\t\t\t\tin")
    out.append("\t\t\t\t    Source")
    out.append("")
    out.append("\tannotation PBI_ResultType = Table")
    return "\n".join(out) + "\n"


def helper_table(name, doc, rows, cols):
    """Small disconnected tables from DATATABLE. rows: list of tuples; cols: [(name, dax type, tmdl type)]."""
    body = ", ".join("{ " + ", ".join(f'"{v}"' if isinstance(v, str) else str(v) for v in r) + " }" for r in rows)
    coldefs = ", ".join(f'"{c}", {t}' for c, t, _ in cols)
    dax = f"DATATABLE ( {coldefs}, {{ {body} }} )"
    columns = [(c, tt, "0" if tt == "int64" else None) for c, _, tt in cols]
    text = calc_table(name, doc, columns, dax)
    return text


def sort_by(text, *pairs):
    """Adds sortByColumn to string columns of a generated table: pairs of (column, sort column as TMDL writes it)."""
    for col, by in pairs:
        head = f"\tcolumn {q(col)}\n\t\tdataType: string\n"
        assert head in text, col
        text = text.replace(head, head + f"\t\tsortByColumn: {by}\n")
    return text


def main():
    global MODEL
    import sys
    if len(sys.argv) > 2 and sys.argv[1] == "--out":  # dry run into another folder (validation outside project/pbip)
        MODEL = Path(sys.argv[2]) / "PillowKey.SemanticModel"
    if MODEL.exists():
        import shutil
        shutil.rmtree(MODEL / "definition", ignore_errors=True)
    d = MODEL / "definition"
    w(MODEL / ".platform", '{\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/gitIntegration/platformProperties/2.0.0/schema.json",\n  "metadata": {\n    "type": "SemanticModel",\n    "displayName": "PillowKey"\n  },\n  "config": {\n    "version": "2.0",\n    "logicalId": "' + tag("platform.model") + '"\n  }\n}\n')
    w(MODEL / "definition.pbism", '{\n  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/semanticModel/definitionProperties/1.0.0/schema.json",\n  "version": "4.2",\n  "settings": {}\n}\n')
    w(d / "database.tmdl", "database\n\tcompatibilityLevel: 1606\n\n")
    w(d / "expressions.tmdl",
      "/// URL of PillowKey_Dataset.xlsx in the organisers' public blob (anonymous). Switch to a\n"
      "/// local copy under project/data/ via Transform data > Edit parameters if the blob is down.\n"
      'expression DataFile = "https://datavizcontests.blob.core.windows.net/worldchamps-atl27/PillowKey_Dataset.xlsx" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]\n'
      f"\tlineageTag: {tag('expr.DataFile')}\n\n"
      "\tannotation PBI_ResultType = Text\n\n"
      "\tannotation PBI_NavigationStepName = Navigation\n")
    tables = list(SHIPPED) + ["_Measures", "ProjectCashflow", "HotelOutlook", "Timeline", "PlanYear", "BridgeStep", "FolioLine", "KpiLine", "Package", "PackageProject", "PlanSelector", "ScatterView", "BuildMove", "BuildPoint", "MoveDecision", "Finding", "WaitOption"]
    model = ["model Model", "\tculture: en-US", "\tdefaultPowerBIDataSourceVersion: powerBI_V3", "\tsourceQueryCulture: en-US", "\tdataAccessOptions", "\t\tlegacyRedirects", "\t\treturnErrorValuesAsNull", "",
             "queryGroup Facts", "", "\tannotation PBI_QueryGroupOrder = 0", "", "queryGroup Dimensions", "", "\tannotation PBI_QueryGroupOrder = 1", "",
             "annotation __PBI_TimeIntelligenceEnabled = 0", "",
             "annotation PBI_QueryOrder = [" + ",".join(f'"{t}"' for t in ["DataFile"] + list(SHIPPED) + ["_Measures"]) + "]", "",
             'annotation PBI_ProTooling = ["DevMode"]', ""]
    model += [f"ref table {q(t)}" for t in tables]
    w(d / "model.tmdl", "\n".join(model) + "\n")

    for name, cols in SHIPPED.items():
        text = shipped_table(name, cols)
        group = "Facts" if name in FACTS else "Dimensions"
        text = text.replace(f"\tpartition {name} = m\n\t\tmode: import\n", f"\tpartition {name} = m\n\t\tmode: import\n\t\tqueryGroup: {group}\n")
        w(d / "tables" / f"{name}.tmdl", text)
    w(d / "tables" / "_Measures.tmdl", measures_table())
    w(d / "tables" / "ProjectCashflow.tmdl", calc_table(
        "ProjectCashflow",
        "Grain: one row per project, scenario and month, January 2027 to December 2032. Capex phased evenly, disruption from rooms out of service against the mapped hotels' 2025 revenue, benefit ramped 50 / 85 / 100 percent after go-live. Rules read from FinanceParameters.",
        [("ProjectID", "string", None), ("Scenario", "string", None), ("Month", "dateTime", "Short Date"), ("Capex", "double", USD), ("Disruption", "double", USD), ("Benefit", "double", USD), ("RevenueBenefit", "double", USD), ("DiscountFactor", "double", "0.0000")],
        PROJECT_CASHFLOW))
    w(d / "tables" / "KpiLine.tmdl", helper_table(
        "KpiLine", "Lines of the page-1 four-brand comparison: finding group, label, good direction (1 higher, -1 lower, 0 not ranked) and number formats. The values come from KPI Value.",
        KPI_ROWS,
        [("Sort", "INTEGER", "int64"), ("Key", "STRING", "string"), ("Finding", "STRING", "string"), ("Measure", "STRING", "string"), ("Direction", "INTEGER", "int64"),
         ("Format", "STRING", "string"), ("DeltaScale", "INTEGER", "int64"), ("DeltaUnit", "STRING", "string"), ("DeltaFormat", "STRING", "string")]).replace(
        "\tcolumn Measure\n\t\tdataType: string\n", "\tcolumn Measure\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))
    w(d / "tables" / "Package.tmdl", calc_table(
        "Package",
        "Grain: one row per valid Goodnight Inn package (456 of the 1,024 subsets of the ten initiatives): capex within the brand budget, three or more initiatives, at least one growth initiative, every DependsOn met. Values are sums of the initiatives' ProjectCashflow (monthly discounting at the FinanceParameters rate to January 2027; 2032 run-rate). Offline reference: project/analysis/40_package_matrix.py.",
        [("PackageID", "string", None), ("Mask", "int64", "0"), ("Projects", "int64", "0"), ("Growth", "int64", "0"), ("CapexUSD", "double", USD), ("ContainsRefresh", "string", None),
         ("RoomsAdded", "int64", "#,0"), ("HotelsRated", "int64", "#,0"), ("NPV Low", "double", USD), ("NPV Expected", "double", USD), ("NPV High", "double", USD),
         ("RunRate Low", "double", USD), ("RunRate Expected", "double", USD), ("RunRate High", "double", USD)],
        # The scatter draws its dots in PackageID order; sorting PackageID by Draw Rank puts B, C and A last, on top of
        # the cloud (REVIEW M2: grey dots were painted over C). A series (legend) would order them too, but Power BI
        # then ignores the per-dot colour measure (seen 7 Nov: the whole cloud took the accent colour, the dots grew).
        PACKAGE).replace("\tcolumn PackageID\n\t\tdataType: string\n", "\tcolumn PackageID\n\t\tdataType: string\n\t\tsortByColumn: 'Draw Rank'\n").replace(
        "\tpartition Package = calculated", "\n".join([
            calc_col("Package", "Preset", PRESET_COL, "string",
                     doc="A, B or C for the three named packages (rules on the Expected case, fixed across scenarios); blank for the rest."),
            calc_col("Package", "Draw Rank", 'IF ( Package[Preset] = "", Package[Mask], 2000 + SWITCH ( Package[Preset], "B", 1, "C", 2, "A", 3 ) )', "int64", "0",
                     doc="Sort order of PackageID, which is the scatter's drawing order: every other package first (by mask), then B, C and A on top."),
            "\tpartition Package = calculated"])))
    w(d / "tables" / "PackageProject.tmdl", calc_table(
        "PackageProject", "Bridge: one row per package and initiative it contains (Package 1-* PackageProject *-1 InvestmentProjects).",
        [("PackageID", "string", None), ("ProjectID", "string", None)], PACKAGE_PROJECT))
    w(d / "tables" / "PlanSelector.tmdl", calc_table(
        "PlanSelector", "Disconnected package selector (no relationships, by design): the three named packages A, B and C (Package[Preset]). The slicer on Label is single-select; DAX reads Key.",
        [("Key", "string", None), ("Label", "string", None), ("Sort", "int64", "0")], PLAN_SELECTOR).replace(
        "\tcolumn Label\n\t\tdataType: string\n", "\tcolumn Label\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))
    # feedback round 4: the build-your-own plan. BuildMove is a disconnected copy of the ten Goodnight Inn moves, so the
    # selector's cross-filter reaches only the Build measures (TREATAS onto InvestmentProjects) and never A's visuals.
    bm = calc_table(
        "BuildMove", "Disconnected copy of the ten Goodnight Inn moves for the build-your-own plan (P2, build state). The Deneb selector cross-filters this table; the Build measures carry the selection onto InvestmentProjects with TREATAS. Sort: by Expected NPV, high to low.",
        [("ProjectID", "string", None), ("Short Name", "string", None), ("Waterfall Label", "string", None), ("Sort", "int64", "0"), ("Growth", "string", None), ("Answers", "string", None)], BUILD_MOVE)
    assert "\tcolumn 'Short Name'\n\t\tdataType: string\n" in bm
    # verification 17 (12 Nov): the build waterfall labels its bars with a shorter name (12 characters at most) so no bar
    # ends in an ellipsis; the selector and the tooltips keep the full Short Name. Both columns sort by the NPV rank.
    bm = bm.replace("\tcolumn 'Waterfall Label'\n\t\tdataType: string\n", "\tcolumn 'Waterfall Label'\n\t\tdataType: string\n\t\tsortByColumn: Sort\n")
    w(d / "tables" / "BuildMove.tmdl", bm.replace("\tcolumn 'Short Name'\n\t\tdataType: string\n", "\tcolumn 'Short Name'\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))
    w(d / "tables" / "BuildPoint.tmdl", helper_table(
        "BuildPoint", "One row, 'Your plan': the category of the scatter layer that marks the plan being built (its X and Y are the Build Capex and Build NPV measures).",
        [("Your plan",)], [("Label", "STRING", "string")]))
    # FinalV3 (doc 21 section 10.1): the decision table and the two row sources of the ledger and the What-waits table
    w(d / "tables" / "MoveDecision.tmdl", calc_table(
        "MoveDecision",
        "Decision data, not source data (docs 20 D2 / D4, 13 Nov 2026): one row per Goodnight Inn move with the Brand Review finding it answers, its status (A, 2028 gate, not now) and its tranche "
        "(1 = package A, 2 = the airport extensions, 3 = the refresh, blank = not in the plan). Finding and the gate tranches are set in sketch_model.py; status A and tranche 1 are read from Package[Preset]. "
        "Disconnected: measures read it with LOOKUPVALUE and TREATAS.",
        [("ProjectID", "string", None), ("Finding", "string", None), ("Status", "string", None), ("Tranche", "int64", "0")], MOVE_DECISION))
    w(d / "tables" / "Finding.tmdl", sort_by(helper_table(
        "Finding", "The four findings of The Brand Review page, in the order of the 2032 ledger (F2, F1, F4, F3). Disconnected row source of the ledger table: its measures switch on Code.",
        [(c, n, f"{c} {n}", s) for c, n, s in FINDINGS],
        [("Code", "STRING", "string"), ("Name", "STRING", "string"), ("Label", "STRING", "string"), ("Ledger Sort", "INTEGER", "int64")]),
        ("Label", "'Ledger Sort'"), ("Code", "'Ledger Sort'")))
    w(d / "tables" / "WaitOption.tmdl", sort_by(helper_table(
        "WaitOption", "The three options that wait (What waits, and why): package B and tranches 2 and 3. Disconnected row source of the What-waits table: its measures switch on Key.",
        WAIT_OPTIONS,
        [("Key", "STRING", "string"), ("Title", "STRING", "string"), ("Sort", "INTEGER", "int64")]), ("Title", "Sort")))
    w(d / "tables" / "ScatterView.tmdl", calc_table(
        "ScatterView", "Disconnected toggle for the P2 scatter (Björn 7 Nov): all packages, or a zoom on A, B and C. Drives the axis ends through Scatter X End / Scatter Y Start / Scatter Y End; filters nothing.",
        [("View", "string", None), ("Sort", "int64", "0")],
        'DATATABLE ( "View", STRING, "Sort", INTEGER, { { "All packages", 1 }, { "Zoom on A, B, C", 2 } } )').replace(
        "\tcolumn View\n\t\tdataType: string\n", "\tcolumn View\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))
    w(d / "tables" / "HotelOutlook.tmdl", calc_table(
        "HotelOutlook",
        "Scenario logic, labeled as such on every visual: the do-nothing projection per hotel and year 2025-2032. 2025 unit economics grown by the organisers' regional demand, ADR and cost assumptions; demand capped at 97 percent occupancy.",
        [("HotelID", "string", None), ("Year", "int64", "0"), ("RoomsAvailable", "double", "#,0"), ("DemandRoomNights", "double", "#,0"), ("RoomsSold", "double", "#,0"), ("Revenue", "double", USD), ("Opex", "double", USD), ("FirstCappedYear", "int64", "0"), ("CappedBy2032", "string", None)],
        HOTEL_OUTLOOK))
    w(d / "tables" / "Timeline.tmdl", calc_table(
        "Timeline", "Axis table 2021-2032 that joins actuals (via Date) and the outlook (via HotelOutlook) on one chart.",
        [("Year", "int64", "0")], 'SELECTCOLUMNS ( GENERATESERIES ( 2021, 2032, 1 ), "Year", [Value] )'))
    w(d / "tables" / "PlanYear.tmdl", calc_table(
        "PlanYear", "Disconnected year stepper 2027-2032 for the wall: it relights the matrix without filtering any fact.",
        [("Year", "int64", "0")], 'SELECTCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), "Year", [Value] )'))
    w(d / "tables" / "BridgeStep.tmdl", helper_table(
        "BridgeStep", "Steps of the two waterfall bridges; the measure Bridge Value supplies the amounts.",
        [("GOP 2024 to 2025", "GOP 2024", 1), ("GOP 2024 to 2025", "Volume", 2), ("GOP 2024 to 2025", "Rate", 3), ("GOP 2024 to 2025", "Staff", 4), ("GOP 2024 to 2025", "Energy", 5), ("GOP 2024 to 2025", "Maintenance", 6), ("GOP 2024 to 2025", "Food and beverage cost", 7), ("GOP 2024 to 2025", "Other cost", 8),
         ("Baseline 2025 to 2032", "GOP 2025 (baseline)", 1), ("Baseline 2025 to 2032", "Volume the market gives", 2), ("Baseline 2025 to 2032", "Price inflation", 3), ("Baseline 2025 to 2032", "Cost inflation", 4)],
        [("Bridge", "STRING", "string"), ("Step", "STRING", "string"), ("Sort", "INTEGER", "int64")]).replace("\tcolumn Step\n\t\tdataType: string\n", "\tcolumn Step\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))
    w(d / "tables" / "FolioLine.tmdl", helper_table(
        "FolioLine", "The three lines of the folio (a hotel bill): rate, what the channel takes, what we keep.",
        [("The guest pays", 1), ("Commission and fees", 2), ("Goodnight Inn keeps", 3)],
        [("Line", "STRING", "string"), ("Sort", "INTEGER", "int64")]).replace("\tcolumn Line\n\t\tdataType: string\n", "\tcolumn Line\n\t\tdataType: string\n\t\tsortByColumn: Sort\n"))

    rels = [
        ("Hotels", "Brand", "Brands", "Brand"), ("Hotels", "Region", "Region", "Region"), ("FinanceAssumptions", "Region", "Region", "Region"),
        ("InvestmentScenarios", "ProjectID", "InvestmentProjects", "ProjectID"),  # InvestmentProjects->Brands dropped: it made IPP->Hotels->Brands ambiguous; pages filter InvestmentProjects[Brand] directly
        ("InvestmentProjectProperties", "ProjectID", "InvestmentProjects", "ProjectID"), ("InvestmentProjectProperties", "HotelID", "Hotels", "HotelID"),
        ("Renovations", "HotelID", "Hotels", "HotelID"),
        ("MonthlyPerformance", "HotelID", "Hotels", "HotelID"), ("MonthlyPerformance", "Month", "Date", "Date"),
        ("GuestSegments", "HotelID", "Hotels", "HotelID"), ("GuestSegments", "Month", "Date", "Date"),
        ("BookingChannels", "HotelID", "Hotels", "HotelID"), ("BookingChannels", "Month", "Date", "Date"),
        ("GuestExperience", "HotelID", "Hotels", "HotelID"), ("GuestExperience", "Month", "Date", "Date"),
        ("GuestComplaints", "HotelID", "Hotels", "HotelID"), ("GuestComplaints", "Month", "Date", "Date"),
        ("ProjectCashflow", "ProjectID", "InvestmentProjects", "ProjectID"), ("ProjectCashflow", "Month", "Date", "Date"),
        ("HotelOutlook", "HotelID", "Hotels", "HotelID"),
        ("PackageProject", "PackageID", "Package", "PackageID"), ("PackageProject", "ProjectID", "InvestmentProjects", "ProjectID"),
    ]
    out = []
    for ft, fc, tt, tc in rels:
        out.append(f"relationship {tag('rel.' + ft + fc + tt + tc)}")
        out.append(f"\tfromColumn: {q(ft)}.{q(fc)}")
        out.append(f"\ttoColumn: {q(tt)}.{q(tc)}")
        out.append("")
    w(d / "relationships.tmdl", "\n".join(out))
    print(f"model written: {len(tables)} tables, {len(MEASURES)} measures, {len(rels)} relationships")


if __name__ == "__main__":
    main()
