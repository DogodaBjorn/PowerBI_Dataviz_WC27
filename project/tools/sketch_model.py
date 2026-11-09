"""Writes the shared PillowKey semantic model (TMDL) for the three direction sketches.

Run from the repo root:  python project/tools/sketch_model.py
Output: project/pbip/PillowKey.SemanticModel

The 16 shipped tables keep the organisers' Power Query (DataFile parameter -> public
blob). Added on top: calculated columns on Hotels and InvestmentProjects, the
ProjectCashflow and HotelOutlook calculated tables (rules read from FinanceParameters /
FinanceAssumptions), four small helper tables and the _Measures table.
Every number is re-derived in the model; nothing is typed in from the mission.
"""
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


EXTRA_COLUMNS = {
    "Hotels": "".join([
        calc_col("Hotels", "Hotel Short Name", 'TRIM(SUBSTITUTE(Hotels[HotelName], Hotels[Brand] & " ", ""))', "string",
                 doc="Hotel name without the brand prefix, for dense walls and tables."),
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
        calc_col("InvestmentProjects", "Answers Finding",
                 'SWITCH(InvestmentProjects[ProjectID], "GI-01", "F2", "GI-02", "F3", "GI-03", "F1", "GI-04", "F4", "GI-05", "F4", "GI-06", "F4", "GI-07", "F3", "GI-08", "F4", "GI-09", "F3", "GI-10", "F1")',
                 "string", doc="The Brand Review finding (F1 to F4 on page 1) the initiative answers; Goodnight Inn projects only (opzet 2026-11-06)."),
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


def m(name, dax, fmt, folder, doc):
    # Desktop refuses the whole project on a duplicate ("TMDL objects cannot be merged", 7 Nov); the validators did not
    assert all(x[0] != name for x in MEASURES), f"duplicate measure name: {name}"
    MEASURES.append((name, dax, fmt, folder, doc))


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
MINUS = 'UNICHAR ( 8722 )'


# DAX FORMAT() does not scale by the trailing ",," of USDM1 / SUSDM (it printed "$4,806,360.8M" in Desktop, 7 Nov);
# those strings work only as a measure's formatString. Text measures divide explicitly instead.
def fm(x):
    return f'FORMAT ( ( {x} ) / 1000000, "$#,0.0" ) & "M"'


def sfm(x):
    # sign from the shown (rounded) value, and no sign at zero: "+$0.0M" labelled an invisible bar (REVIEW m6)
    # a word joiner after the sign: wrapped copy broke "−" / "$0.6M" over two lines (render 7 Nov); U+2060 is a
    # default-ignorable character, so it draws nothing in Desktop's and the browser's text engines
    return (f'( VAR __t = ROUND ( ( {x} ) / 100000, 0 ) / 10 RETURN IF ( __t = 0, "$0.0M", IF ( __t < 0, {MINUS}, "+" ) & UNICHAR ( 8288 ) & FORMAT ( ABS ( __t ), "$#,0.0" ) & "M" ) )')


def fmc(x):
    """Capex and budget amounts: up to two decimals, so shown parts add up to shown totals. Every Goodnight Inn capex
    is a multiple of $50K: $24.75M + $4.25M ... = $60.0M, where one decimal printed 24.8 + 4.3 = 60.1 (REVIEW M8)."""
    return f'FORMAT ( ( {x} ) / 1000000, "$#,0.0#" ) & "M"'
# Kit goodnight-inn-wakeup 3.1 (plan 10 D1/D6, plan 11): marks in ACCENT_MARK (Coffee Blue), text and the
# recommended plan in ACCENT (Deep Coffee), signals in SIGNAL_MARK (Tangerine), sisters and context in SLATE (Warm
# Grey, 3.5:1 on white: a mark, never small text), ▲/▼ text in GOOD/BAD.
INK, INK2, GOOD, BAD, ACCENT, ACCENT_MARK, SIGNAL_MARK, SLATE, TINT, TINT2 = (
    "#12233D", "#4B5466", "#1763A8", "#A63F0E", "#1763A8", "#2589D8", "#E05A22", "#8E897D", "#EAF2FB", "#C5DCF3")
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


def shown_parts(expr):
    """DAX VAR lines over `ids` (FIDS): @s per initiative in the package, `expr` rounded to $0.1M by largest
    remainder, so the shown parts add up to the shown package total (REVIEW M8: waterfall B read 3.4 - 1.1 + 0.5
    against a total of 2.7)."""
    return (f"VAR base = ADDCOLUMNS ( ids, \"@v\", VAR p = [@p] RETURN CALCULATE ( {expr}, REMOVEFILTERS ( InvestmentProjects ), InvestmentProjects[ProjectID] = p ) ) "
            "VAR tr = ROUND ( SUMX ( base, [@v] ) / 100000, 0 ) "
            "VAR fl = ADDCOLUMNS ( base, \"@f\", INT ( [@v] / 100000 ) ) "
            "VAR fr = ADDCOLUMNS ( fl, \"@r\", [@v] / 100000 - [@f] + VALUE ( RIGHT ( [@p], 2 ) ) * 0.000000001 ) "
            "VAR k = tr - SUMX ( fr, [@f] ) "
            "VAR adj = ADDCOLUMNS ( fr, \"@s\", ( [@f] + IF ( RANKX ( fr, [@r], , DESC ) <= k, 1, 0 ) ) * 100000 ) ")


m("Focus Project NPV (shown)",
  FIDS + shown_parts("[NPV @ 8%]") + "RETURN SUMX ( FILTER ( adj, [@p] IN VALUES ( InvestmentProjects[ProjectID] ) ), [@s] )", SUSDM, C9,
  "Waterfall: each initiative's NPV in the package in focus, rounded to $0.1M so the bars add up to the shown total.")
for nm, expr in (("NPV", "[NPV @ 8%]"), ("Run-rate", "[2032 Run-rate]")):
    m(f"Initiative {nm} (text)",
      FIDS + shown_parts(expr) + f"VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) VAR v = IF ( me IN ids, MAXX ( FILTER ( adj, [@p] = me ), [@s] ), {expr} ) "
      "RETURN IF ( ISBLANK ( me ), BLANK (), " + sfm("v") + " )",
      TXT, C9, f"Plan table {nm.lower()} as text: inside the package rounded to add up to the package total, outside it as is.")
m("Initiative Capex (text)", 'VAR me = SELECTEDVALUE ( InvestmentProjects[ProjectID] ) RETURN IF ( ISBLANK ( me ), BLANK (), ' + fmc("SUM ( InvestmentProjects[CapexUSD] )") + " )",
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
m("Subtitle P2 (text)",
  f'VAR s = [Selected Scenario] VAR rate = {FP.format("Discount rate")} VAR h = {FP.format("Impact horizon")} '
  'RETURN s & " case  ·  NPV through " & h & " in 2025 dollars at " & FORMAT ( rate, "0%" ) & "  ·  nothing after " & h & " is counted" '
  '& IF ( s <> "Expected", "  ·  the recommendation is set on the Expected case", "" )',
  TXT, C9, "Page-2 subtitle: the scenario in view and the valuation rules, read from FinanceParameters; outside Expected it says where the recommendation was set (REVIEW M3).")
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
m("TT Capex (text)", TT_ID + "RETURN IF ( ISBLANK ( pkg ), BLANK (), " + fmc("LOOKUPVALUE ( Package[CapexUSD], Package[PackageID], pkg )") + " )", TXT, C10, "Tooltip: capex of the hovered package.")
m("TT NPV (text)", TT_ID + TT_NPV + "RETURN IF ( ISBLANK ( pkg ), BLANK (), " + sfm("npv") + " )", TXT, C10, "Tooltip: NPV through 2032 of the hovered package, scenario in view.")
m("TT NPV Label (text)", '"NPV through 2032, " & [Selected Scenario] & " case"', TXT, C10, "Tooltip: label under the NPV.")
m("TT NPV Color", TT_ID + TT_NPV + f'RETURN IF ( ROUND ( npv / 100000, 0 ) >= 0, "{ACCENT}", "{BAD}" )', TXT, C10,
  "Tooltip NPV colour: Deep Coffee when it pays back by 2032 (NPV at least zero), Burnt Tangerine below (08-verbeterplan V2); the sign and the payback line carry it too.")
m("TT Range (text)",
  TT_ID + "VAR lo = LOOKUPVALUE ( Package[NPV Low], Package[PackageID], pkg ) / 1000000 VAR ex = LOOKUPVALUE ( Package[NPV Expected], Package[PackageID], pkg ) / 1000000 "
  "VAR hi = LOOKUPVALUE ( Package[NPV High], Package[PackageID], pkg ) / 1000000 "
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), "Low " & ' + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & "  ·  Expected " & ' + signed("ex", 'FORMAT ( ABS ( ex ), "0.0" )')
  + ' & "  ·  High " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )') + ' & ", $M" )',
  TXT, C10, "Tooltip: NPV of the hovered package in all three cases, $M.")
m("TT Payback Year",
  TT_ID + 'VAR ids = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = pkg ), "@p", PackageProject[ProjectID] ) VAR s = [Selected Scenario] '
  "VAR t = ADDCOLUMNS ( GENERATESERIES ( 2027, 2032, 1 ), \"@c\", VAR y = [Value] RETURN CALCULATE ( SUM ( ProjectCashflow[Benefit] ) - SUM ( ProjectCashflow[Capex] ) - SUM ( ProjectCashflow[Disruption] ), "
  "REMOVEFILTERS ( 'Date' ), 'Date'[Year] <= y, ProjectCashflow[Scenario] = s, TREATAS ( ids, ProjectCashflow[ProjectID] ) ) ) RETURN MINX ( FILTER ( t, [@c] >= 0 ), [Value] )",
  "0", C10, "First year the cumulative net of the hovered package turns positive, scenario in view; blank when not by 2032.")
m("TT Payback (text)",
  # 'pays back by 2032' is the scatter's own line (NPV at least zero); the cash year is said only under it, so the
  # tooltip never claims a payback the line denies, and nothing after 2032 (08-verbeterplan N11)
  TT_ID + TT_NPV + "VAR pb = [TT Payback Year] "
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), IF ( ROUND ( npv / 100000, 0 ) >= 0, "Pays back by 2032" & IF ( ISBLANK ( pb ), "", ": cash positive from " & pb ), "Does not pay back by 2032 in this case" ) )',
  TXT, C10, "Tooltip: whether the hovered package pays back by 2032 in the case in view, and from which year its cumulative cash is positive.")
m("TT Mix (text)",
  TT_ID + 'VAR ids = FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = pkg ) '
  'RETURN IF ( ISBLANK ( pkg ), BLANK (), COUNTROWS ( ids ) & " moves: " & CONCATENATEX ( ids, ' + "LOOKUPVALUE ( InvestmentProjects[Short Name], InvestmentProjects[ProjectID], PackageProject[ProjectID] )" + ', ", ", PackageProject[ProjectID], ASC ) )',
  TXT, C10, "Tooltip: the initiatives in the hovered package, by name.")
m("TT Chip",
  TT_ID + TT_NPV + 'RETURN IF ( ISBLANK ( pkg ), BLANK (), "data:image/svg+xml;utf8," & IF ( ROUND ( npv / 100000, 0 ) >= 0, ' + CHIP_ON + ", " + CHIP_OFF + " ) )",
  TXT, C10, "Tooltip: the brand's state chip, the funded chip when the package pays back by 2032 and the plain one when it does not; decorative, the payback line says it in words.")
IMAGE_MEASURES.add("TT Chip")
m("Scatter Title (text)",
  'VAR s = [Selected Scenario] VAR t = ADDCOLUMNS ( ALLNOBLANKROW ( Package ), "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
  'VAR n = COUNTROWS ( t ) VAR pos = FILTER ( t, [@v] >= 0 ) VAR k = COUNTROWS ( pos ) + 0 VAR cap = INT ( MAXX ( pos, Package[CapexUSD] ) / 1000000 ) + 1 '
  'RETURN IF ( k = 0, "None of the " & n & " possible packages pays back by 2032 in the " & s & " case", '
  'k & " of " & n & " possible packages " & IF ( k = 1, "pays back by 2032, at under $", "pay back by 2032, all of them under $" ) & cap & "M" )',
  TXT, C9, "Scatter title: how many packages have NPV through 2032 at least zero in the selected scenario, and the capex ceiling they share (the next whole $M above the largest).")
m("Shortlist Title (text)", '"Three packages, one per criterion (" & [Selected Scenario] & " case)"', TXT, C9, "Shortlist state title.")
# Names instead of codes in everything a board member reads (REVIEW M5); the role of the package is in its name.
# C is the comparator, not a third candidate (08-verbeterplan V1, Björn 7 Nov): it is shown to answer "why not
# renovate?", and every place that names it says so.
ROLE = 'SWITCH ( [Focus Key], "B", "considered, not recommended", "C", "why not renovate?", "our recommendation" )'
m("Plan Title (text)",
  'VAR f = [Focus Package] RETURN IF ( ISBLANK ( f ), BLANK (), "Package " & [Focus Key] & " (" & ' + ROLE + ' & "): " & ' + fmc("[Focus Capex]") + ' & " on " & [Focus Projects] & " initiatives, all live by " & [Focus Live By (text)] )',
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
  'RETURN IF ( ISBLANK ( f ), BLANK (), "In focus: " & SELECTEDVALUE ( PlanSelector[Label], "A · Our recommendation" ) & "  ·  " & ' + fmc("[Focus Capex]") + ' & "  ·  NPV " & ' + sfm("[Focus NPV (sel)]") + ' & " (" & s & ")" )',
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
m("Focus Cumulative Net (sel)",
  'SWITCH ( [Selected Scenario], "Low", [Focus Cumulative Net (Low)], "High", [Focus Cumulative Net (High)], [Focus Cumulative Net (Expected)] )', SUSDM, C9,
  "Cumulative net impact of the package in focus in the selected scenario: the emphasised line (REVIEW M9).")
REC_IDS = 'VAR a = [Recommended Package] VAR aIds = SELECTCOLUMNS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ), "@p", PackageProject[ProjectID] ) '
m("Uncertainty (text)",
  'VAR a = [Recommended Package] VAR k = COUNTROWS ( FILTER ( ALLNOBLANKROW ( Package ), Package[NPV Low] >= 0 ) ) + 0 '
  'VAR lo = CALCULATE ( SUM ( Package[NPV Low] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) '
  'RETURN "Read with care: in the Low case " & IF ( k = 0, "no package pays back by 2032", k & " packages pay back by 2032" ) & ", and A ends at " & ' + sfm("lo") + ' & "."',
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
m("Subtitle P1 Briefing (text)", '"Goodnight Inn in 2025, against the three other Pillow & Key Group brands."', TXT, C8, "Page-1 subtitle (a card, like P2's, so both headers sit on one grid: REVIEW p2).")
m("KPI Occupancy Context (text)",
  rank_words("Occupancy %", 2025, 1) + 'RETURN words & " · the others " & FORMAT ( ' + others("Occupancy %", 2025, "MINX") + ', "0.0%" ) & " to " & FORMAT ( ' + others("Occupancy %", 2025, "MAXX") + ', "0.0%" )',
  TXT, C8, "KPI band: rank among the four brands and the range of the other three, 2025.")
m("KPI Margin after Context (text)",
  # the change from the two shown values (36.5% to 33.7% in F1's title), not from the unrounded ones: -2.8, not -2.7 (REVIEW M8)
  rank_words("GOP Margin after Distribution %", 2025, 1) + "VAR d = ( ROUND ( gn, 3 ) - ROUND ( " + gi_at("GOP Margin after Distribution %", 2023) + ", 3 ) ) * 100 "
  'RETURN words & " · " & ' + signed("d", 'FORMAT ( ABS ( d ), "0.0" )') + ' & " pt since 2023"',
  TXT, C8, "KPI band: rank among the four brands and the change since 2023 in points.")
m("KPI OTA Context (text)",
  rank_words("OTA Share %", 2025, -1, best="lowest", worst="highest") + 'RETURN words & " · " & FORMAT ( ' + gi_at("OTA Share %", 2021) + ', "0.0%" ) & " in 2021"',
  TXT, C8, "KPI band: rank among the four brands (lower is better) and the 2021 share.")
m("KPI NPS Context (text)",
  rank_words("NPS (weighted)", 2025, 1) + "VAR lo = " + others("NPS (weighted)", 2025, "MINX") + " VAR hi = " + others("NPS (weighted)", 2025, "MAXX") + " "
  'RETURN words & " · the others " & ' + signed("lo", 'FORMAT ( ABS ( lo ), "0.0" )') + ' & " to " & ' + signed("hi", 'FORMAT ( ABS ( hi ), "0.0" )'),
  TXT, C8, "KPI band: rank among the four brands and the range of the other three, 2025.")

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
  'RETURN "After commissions, the margin " & IF ( z < a, "fell", "rose" ) & " from " & FORMAT ( a, "0.0%" ) & " to " & FORMAT ( z, "0.0%" )',
  TXT, C8, "F1 title: Goodnight Inn margin after commissions, 2023 to 2025.")
m("F1 Note (text)",
  rank_words("GOP Margin %", 2025, 1) + "VAR pa = ROUND ( " + adr_chg('"Goodnight Inn"') + ", 3 ) VAR plo = ROUND ( " + adr_chg_sisters("MINX") + ", 3 ) VAR phi = ROUND ( " + adr_chg_sisters("MAXX") + ", 3 ) VAR g0 = ( " + gi_at("GOP Margin %", 2021) + " - " + gi_at("GOP Margin after Distribution %", 2021) + " ) * 100 "
  "VAR g1 = ( gn - " + gi_at("GOP Margin after Distribution %", 2025) + " ) * 100 "
  'RETURN "Before commissions Goodnight Inn " & IF ( r = 1, "still has the widest margin of the four", "ranks " & r & " of " & n ) & ". The gap, what the booking channels take, " '
  '& IF ( g1 > g0, "grew", "narrowed" ) & " from " & FORMAT ( g0, "0.0" ) & " to " & FORMAT ( g1, "0.0" ) & " points since 2021. " '
  # plan 09 R1 as applied in plan 11: pricing power (Kantar BrandZ, IPA; CREDITS.md) as room-rate growth since 2023
  # against the sisters. 42_price_index.py showed the 2021 = 100 index measures the recovery, not pricing power.
  '& "Room rates " & IF ( pa < 0, "fell ", "rose " ) & FORMAT ( ABS ( pa ), "0.0%" ) & " since 2023, " '
  '& IF ( pa > phi, "faster than", IF ( pa < plo, "slower than", "in line with" ) ) & " the other brands (" & FORMAT ( plo, "0.0%" ) & " to " & FORMAT ( phi, "0.0%" ) & ")" '
  '& IF ( pa > phi, ".", ": no price premium to absorb the commissions." )',
  TXT, C8, "F1 note: the before-commissions rank, the commission gap 2021 to 2025, and room-rate growth since 2023 against the sisters (plan 09 R1, plan 11).")

# P1 F2 the middleman
m("F2 Title (text)",
  "VAR a = " + gi_at("OTA Share %", 2021) + " VAR z = " + gi_at("OTA Share %", 2025) + " "
  'RETURN "Online agencies now book " & FORMAT ( z, "0%" ) & " of room revenue, " & IF ( z > a, "up", "down" ) & " from " & FORMAT ( a, "0%" )',
  TXT, C8, "F2 title: OTA share of Goodnight Inn room revenue, 2021 to 2025.")
m("F2 Note (text)",
  "VAR o = " + gi_at("Channel Room Revenue", 2025, 'BookingChannels[Channel] = "Online Travel Agencies"') + " / " + gi_at("Channel Room Nights", 2025, 'BookingChannels[Channel] = "Online Travel Agencies"') + " "
  "VAR d = " + gi_at("Channel Room Revenue", 2025, 'BookingChannels[Channel] = "Direct Website & App"') + " / " + gi_at("Channel Room Nights", 2025, 'BookingChannels[Channel] = "Direct Website & App"') + " "
  f"VAR x = CALCULATE ( [Distribution Cost above 2021 Mix 2025], {gi} ) "
  # plan 09 R5 (Double Jeopardy, Ehrenberg-Bass; CREDITS.md): reach over loyalty, only as a labelled reading of the
  # data ("Our reading:" marks an interpretation, not a fact); the hotel count and the occupancy rank come from the model
  f"VAR nh = CALCULATE ( COUNTROWS ( Hotels ), {gi} ) "
  + rank_words("Occupancy %", 2025, 1) +
  'RETURN IF ( ABS ( d - o ) <= 0.05 * o, "The guest pays about the same either way. ", "" ) & "At the 2021 channel mix, 2025 commissions would have been " & ' + fm("x") + ' & " lower. " '
  '& "Our reading: with " & nh & " hotels" & IF ( r = 1, " and the highest occupancy of the four", "" ) & ", Goodnight Inn grows by reaching more guests and winning their next booking direct, not through a loyalty scheme."',
  TXT, C8, "F2 note under the folio: the rate gap between channels (said only when within 5 percent), the 2021-mix counterfactual, and the reach-over-loyalty reading, labelled as interpretation (plan 09 R5).")

# P1 F3 the fading welcome (Hotels[Renovation Age Sort]: dated hotels only)
m("NPS 2025 (signed)", "[NPS (weighted) 2025]", SIGNED1, C8, "Response-weighted NPS 2025 with a true minus, for chart labels.")
m("Age Band Color", f'IF ( SELECTEDVALUE ( Hotels[Renovation Age Sort] ) = 3, "{ACCENT_MARK}", "{SLATE}" )', TXT, C8, "Coffee Blue for the oldest band (the story), Warm Grey for the others; the axis label and the signed value carry it too.")
m("F3 Title (text)",
  "VAR v = " + gi_at("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 3") + ' RETURN "Hotels last renovated 10 years or more ago score NPS " & ' + signed("v", 'FORMAT ( ABS ( v ), "0.0" )'),
  TXT, C8, "F3 title: NPS 2025 of the Goodnight Inn hotels last renovated 10 or more years ago.")
m("F3 Note (text)",
  "VAR o1 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 1") + " VAR o2 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 2") + " VAR o3 = " + gi_at("Occupancy %", 2025, "Hotels[Renovation Age Sort] = 3") + " "
  "VAR lo = MIN ( MIN ( o1, o2 ), o3 ) VAR hi = MAX ( MAX ( o1, o2 ), o3 ) "
  f"VAR n1 = CALCULATE ( COUNTROWS ( Hotels ), {gi}, Hotels[Renovation Age Sort] = 1 ) VAR n2 = CALCULATE ( COUNTROWS ( Hotels ), {gi}, Hotels[Renovation Age Sort] = 2 ) "
  f"VAR n3 = CALCULATE ( COUNTROWS ( Hotels ), {gi}, Hotels[Renovation Age Sort] = 3 ) VAR full = CALCULATE ( COUNTROWS ( Hotels ), {gi} ) "
  'RETURN "Bands of " & n1 & ", " & n2 & " and " & n3 & " hotels" & IF ( n1 + n2 + n3 < full, "; " & full - n1 - n2 - n3 & " of the " & full & " were never renovated", "" ) & ". " '
  '& IF ( hi - lo <= 0.02, "Occupancy is the same in every band (" & FORMAT ( lo, "0%" ) & " to " & FORMAT ( hi, "0%" ) & "): age costs loyalty, not yet rooms. ", "" ) & "An association, not proof of cause."',
  TXT, C8, "F3 note: occupancy across the age bands (the 'not yet rooms' clause only when they sit within 2 points), the causality caveat (05 caveat A2) and how many hotels the bands cover (REVIEW m8: 44 of 50).")

# P1 F4 where we are full
for t in ("Airport", "City", "Highway"):
    m(f"Occupancy {t} GI", gi_at("Occupancy %", 2025, f'Hotels[LocationType] = "{t}"'), PCT, C8, f"Goodnight Inn occupancy 2025 in {t.lower()} hotels.")
    m(f"Occupancy {t} GI (text)", f'FORMAT ( [Occupancy {t} GI], "0.0%" )', TXT, C8, f"Goodnight Inn occupancy 2025 in {t.lower()} hotels, as text (one formatter with the titles).")
m("F4 Title (text)",
  'VAR air = [Occupancy Airport GI] VAR best = MAX ( [Occupancy City GI], [Occupancy Highway GI] ) '
  f"VAR hs = CALCULATETABLE ( VALUES ( Hotels[HotelID] ), {gi} ) "
  "VAR t7 = TOPN ( 7, hs, CALCULATE ( [Occupancy %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ) ) "
  'VAR na = COUNTROWS ( FILTER ( t7, CALCULATE ( SELECTEDVALUE ( Hotels[LocationType] ) ) = "Airport" ) ) '
  'RETURN IF ( air >= best, "The airports are the fullest at ", "The airports run at " ) & FORMAT ( air, "0.0%" ) & ", and " & na & " of the 7 fullest hotels are airports"',
  TXT, C8, "F4 title: airport occupancy and how many of the seven fullest Goodnight Inn hotels are airports, 2025.")

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
  'RETURN "Each move answers a page-1 finding: " & CONCATENATEX ( aIds, LOWER ( ' + NAME_OF.format("[@p]") + ' ) & " " & LOOKUPVALUE ( InvestmentProjects[Answers Finding], InvestmentProjects[ProjectID], [@p] ), ", ", [@p], ASC ) & ". " '
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
  # (Expected), -$2.7M (Low), -$0.1M (High), recounted from project/analysis/output/packages.csv.
  'VAR s = [Selected Scenario] VAR nA = COUNTROWS ( aIds ) '
  'VAR sup = FILTER ( ALLNOBLANKROW ( Package ), Package[Projects] > nA && COUNTROWS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = Package[PackageID] && PackageProject[ProjectID] IN aIds ) ) = nA ) '
  'VAR t = ADDCOLUMNS ( sup, "@v", SWITCH ( s, "Low", Package[NPV Low], "High", Package[NPV High], Package[NPV Expected] ) ) '
  'VAR best = TOPN ( 1, t, [@v], DESC, Package[CapexUSD], ASC ) VAR bid = MAXX ( best, Package[PackageID] ) VAR bv = MAXX ( best, [@v] ) VAR bc = MAXX ( best, Package[CapexUSD] ) '
  'VAR av = CALCULATE ( [Package NPV (sel)], REMOVEFILTERS ( Package ), Package[PackageID] = a ) '
  'VAR added = CONCATENATEX ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = bid && NOT ( PackageProject[ProjectID] IN aIds ) ), LOWER ( ' + NAME_OF.format("PackageProject[ProjectID]") + ' ), " and ", PackageProject[ProjectID], ASC ) '
  'VAR margin = IF ( NOT ISBLANK ( bid ) && ROUND ( ( bv - av ) / 100000, 0 ) < 0, " The best way to spend more, A plus the " & added & ", costs " & ' + fmc("bc - cap") + ' & " more and lowers the NPV by " & ' + fm("av - bv") + ' & ".", "" ) '
  'RETURN "The other " & ' + fmc("budget - cap") + ' & " is held back, to be decided again once " & word & " moves are live, by " & live & ": " '
  '& IF ( hiPos = 0, "no other initiative pays back by 2032, even in the High case.", hiPos & " other initiatives pay back by 2032 only in the High case." ) & margin',
  TXT, C9, "The budget held back: until when, why nothing else is funded now, and the marginal test: the best package with all of A and more lowers the NPV (plan 09 R3).")
m("Rec Rules (text)",
  REC_IDS + f"VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) VAR budget = {BUDGET_GI} VAR h = {FP.format('Impact horizon')} "
  'VAR g = FILTER ( aIds, LOOKUPVALUE ( InvestmentProjects[GrowthInitiative], InvestmentProjects[ProjectID], [@p] ) = "Yes" ) '
  'RETURN "Within the rules: " & COUNTROWS ( aIds ) & " initiatives, " & COUNTROWS ( g ) & " of them growth (" & CONCATENATEX ( g, LOWER ( ' + NAME_OF.format("[@p]") + ' ), " and ", [@p], ASC ) & "), " '
  '& ' + fmc("cap") + ' & " of the " & ' + fmc("budget") + ' & " budget, impact counted through " & h & "."',
  TXT, C9, "The contest rules ticked off for A: initiatives, growth initiatives (dataset flag), budget, horizon (REVIEW M11).")
m("Headline P2 (text)",
  # "the three moves that pay" was false: the kiosks alone return -$0.6M (REVIEW M3); the package is what pays
  f"VAR a = [Recommended Package] VAR k = COUNTROWS ( FILTER ( ALLNOBLANKROW ( PackageProject ), PackageProject[PackageID] = a ) ) VAR budget = {BUDGET_GI} "
  "VAR cap = CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a ) "
  'VAR word = SWITCH ( k, 3, "three", 4, "four", 5, "five", 6, "six", 7, "seven", FORMAT ( k, "0" ) ) '
  'RETURN "Fund one package of " & word & " moves: " & ' + fmc("cap") + ' & " now, " & ' + fmc("budget - cap") + ' & " held back."',
  TXT, C9, "Page-2 headline: the recommendation in one sentence that holds in every scenario (06-d1-briefing-opzet.md decision 2, revised 7 Nov).")


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
            f'RETURN IF ( ISBLANK ( x ), BLANK (), "{k} · " & {lead} & IF ( dropped = "", "A plus the " & added, "The " & added & " instead of the " & dropped ) & ": " & ' + fmc("capX") + ' & ", NPV " & ' + sfm("npvX") + f' & ". " & ( {extra} ) )')


m("Alt B (text)",
  alt("B", 'IF ( rX > rA, "A guest-score effect in " & rX & " hotels instead of " & rA & ", for " & ' + fmc("capX - capA") + ' & " more and a " & IF ( npvX < npvA, "lower", "higher" ) & " NPV.", "" )'),
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
  'RETURN IF ( ISBLANK ( names ), BLANK (), "Not funded · " & names & IF ( f4 > 0, " (" & f4 & " of them answer F4)", "" ) & ": A has the highest NPV of all packages in the Expected case, so adding any of them lowers it." )',
  TXT, C9, "The initiatives outside A, B and C, and the reason the selection leaves them out.")
m("Masthead P2 (text)", f'"2027 TO 2032  ·  GOODNIGHT INN BUDGET " & ' + fmc(BUDGET_GI), TXT, C9,
  "Page-2 masthead line on the night zone: the horizon and the brand budget, read from Brands (was typed into the report generator).")
m("Footer P2 (text)",
  f'VAR rate = {FP.format("Discount rate")} VAR h = {FP.format("Impact horizon")} '
  'RETURN "Source: Pillow & Key Group dataset and its finance parameters (ramp-up, " & FORMAT ( rate, "0%" ) & " discount rate, impact horizon " & h & "). Low, Expected and High are the dataset\'s scenarios. In the plan, parts are rounded so they add up to the package total. Deliberately not shown: impressions, likes, and NPS as a growth measure; effectiveness research does not support them."',
  TXT, C9, "Page-2 source line with the valuation parameters (REVIEW p7).")
# the P2 panel's numbers as text, so a card never mixes a visual-formatted number with DAX text (REVIEW M7)
m("Rec Capex (text)", "VAR a = [Recommended Package] RETURN " + fmc("CALCULATE ( SUM ( Package[CapexUSD] ), REMOVEFILTERS ( Package ), Package[PackageID] = a )"), TXT, C9, "Capex of A as text.")
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
        ("NPS", "Guest quality: Goodnight Inn net promoter score in 2025", "KPI NPS GI (text)", "KPI NPS Context (text)")):
    alt_m(f"KPI {key}", f'"{label}: " & [{value}] & ", " & {semi(ctx)} & "."', f"KPI band, read aloud: the label, the value and the comparison ({key}).")

alt_m("F1 Chart",
      '"Line chart, 2021 to 2025, of Goodnight Inn\'s operating margin before commissions, from " & FORMAT ( ' + gi_at("GOP Margin %", 2021) + ', "0.0%" ) & " to " & FORMAT ( ' + gi_at("GOP Margin %", 2025) + ', "0.0%" ) '
      '& ", and after commissions, from " & FORMAT ( ' + gi_at("GOP Margin after Distribution %", 2021) + ', "0.0%" ) & " to " & FORMAT ( ' + gi_at("GOP Margin after Distribution %", 2025) + ', "0.0%" ) '
      '& ". The gap between the lines is what the booking channels take."',
      "F1 chart: both margin lines at their ends, 2021 and 2025.")
alt_m("F2 Chart",
      '"Line chart, 2021 to 2025, of the share of room revenue booked through online agencies. Goodnight Inn went from " & FORMAT ( ' + gi_at("OTA Share %", 2021) + ', "0.0%" ) & " to " & FORMAT ( ' + gi_at("OTA Share %", 2025) + ', "0.0%" ) '
      '& "; the other brands in 2025: " & CONCATENATEX ( FILTER ( ALLNOBLANKROW ( Brands[Brand] ), Brands[Brand] <> "Goodnight Inn" ), Brands[Brand] & " " & FORMAT ( CALCULATE ( [OTA Share %], REMOVEFILTERS ( Brands ), REMOVEFILTERS ( Hotels ), REMOVEFILTERS ( \'Date\' ), \'Date\'[Year] = 2025 ), "0.0%" ), ", ", Brands[Brand], ASC ) & "."',
      "F2 chart: Goodnight Inn's OTA share 2021 and 2025, and the sisters' 2025 values.")


def folio_pair(channel):
    base = f"{gi}, REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025, BookingChannels[Channel] = \"{channel}\""
    return (f"ROUND ( CALCULATE ( DIVIDE ( [Channel Room Revenue], [Channel Room Nights] ), {base} ), 2 )",
            f"ROUND ( CALCULATE ( DIVIDE ( [Distribution Cost], [Channel Room Nights] ), {base} ), 2 )")


(_or, _oc), (_dr, _dc) = folio_pair("Online Travel Agencies"), folio_pair("Direct Website & App")
alt_m("F2 Folio",
      f"VAR orate = {_or} VAR ocomm = {_oc} VAR drate = {_dr} VAR dcomm = {_dc} "
      'RETURN "Table, the folio of one Goodnight Inn room night in 2025. Via an online agency the guest pays " & FORMAT ( orate, "$#,0.00" ) & ", commission and fees take " & FORMAT ( ocomm, "$#,0.00" ) '
      '& " and the inn keeps " & FORMAT ( orate - ocomm, "$#,0.00" ) & ". Booked direct, on the web or in the app, the guest pays " & FORMAT ( drate, "$#,0.00" ) & ", fees take " & FORMAT ( dcomm, "$#,0.00" ) '
      '& " and the inn keeps " & FORMAT ( drate - dcomm, "$#,0.00" ) & "."',
      "F2 folio table read aloud, the same rounding as the table (keeps = the difference of the shown amounts).")
alt_m("F3 Chart",
      '"Column chart of Goodnight Inn\'s 2025 net promoter score by years since the last renovation: 5 years or less " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 1")
      + ' & ", 6 to 9 years " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 2") + ' & ", 10 years or more " & ' + gi_sgn("NPS (weighted)", 2025, "Hotels[Renovation Age Sort] = 3") + ' & "."',
      "F3 chart: the three bands' NPS 2025 (dated hotels only).")
alt_m("F4 Types",
      '"Goodnight Inn occupancy in 2025 by location type: airport hotels " & [Occupancy Airport GI (text)] & ", city hotels " & [Occupancy City GI (text)] & ", highway hotels " & [Occupancy Highway GI (text)] & "."',
      "F4 numbers card read aloud.")
alt_m("F4 Chart",
      f"VAR hs = CALCULATETABLE ( VALUES ( Hotels[HotelID] ), {gi} ) "
      "VAR t7 = ADDCOLUMNS ( TOPN ( 7, hs, CALCULATE ( [Occupancy %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ) ), \"@o\", CALCULATE ( [Occupancy %], REMOVEFILTERS ( 'Date' ), 'Date'[Year] = 2025 ), "
      "\"@n\", CALCULATE ( SELECTEDVALUE ( Hotels[Hotel Short Name] ) ), \"@t\", CALCULATE ( SELECTEDVALUE ( Hotels[LocationType] ) ) ) "
      'VAR na = COUNTROWS ( FILTER ( t7, [@t] = "Airport" ) ) '
      'RETURN "Column chart of the seven Goodnight Inn hotels with the highest occupancy in 2025, " & na & " of them airport hotels: " & CONCATENATEX ( t7, [@n] & " " & FORMAT ( [@o], "0%" ), ", ", [@o], DESC ) & "."',
      "F4 chart read aloud: the seven fullest hotels with their occupancy, and how many are airports.")
alt_m("Scatter",
      '[Scatter Title (text)] & ", in the " & [Selected Scenario] & " case, out of every combination of the ten initiatives that fits the rules. Capex runs along the horizontal axis, NPV through 2032 up the vertical one. '
      'A, our recommendation: " & ' + fmc("[Preset A Capex]") + ' & ", NPV " & ' + sfm("[Preset A NPV (sel)]") + ' & ". B, the alternative: " & ' + fmc("[Preset B Capex]") + ' & ", NPV " & ' + sfm("[Preset B NPV (sel)]")
      + ' & ". C, the answer to why not renovate: " & ' + fmc("[Preset C Capex]") + ' & ", NPV " & ' + sfm("[Preset C NPV (sel)]") + ' & ". Hover a dot for its package card."',
      "The scatter read aloud (its one tab stop is the A/B/C layer): how many packages pay back, then A, B and C with capex and NPV in the case in view.")
alt_m("Rec Nums",
      '"Package A in numbers, " & [Selected Scenario] & " case: capex " & [Rec Capex (text)] & ", NPV through 2032 " & [Rec NPV (text)] & ", NPV from the Low to the High case " & [Rec Range (text)] & " $M, profit a year by 2032 " & [Rec Run-rate (text)] & "."',
      "The recommendation's numbers card read aloud.")
alt_m("Waterfall",
      FIDS + shown_parts("[NPV @ 8%]") +
      'RETURN IF ( ISBLANK ( f ), BLANK (), "Waterfall, " & [Selected Scenario] & " case: where the NPV through 2032 of package " & [Focus Key] & " comes from. " '
      '& CONCATENATEX ( adj, ' + NAME_OF.format("[@p]") + ' & " " & ' + sfm("[@s]") + ', ", ", [@s], DESC ) & "; together " & ' + sfm("SUMX ( adj, [@s] )") + ' & "." )',
      "The plan waterfall read aloud: each initiative's shown NPV and the package total, in the case in view.")
alt_m("Plan Table",
      FIDS + 'RETURN IF ( ISBLANK ( f ), BLANK (), "Table of the ten Goodnight Inn initiatives, those in package " & [Focus Key] & " first, with their status, the page-1 finding each answers, capex, profit a year by 2032, NPV and the dataset guest-score effect. In package " & [Focus Key] & ": " '
      '& CONCATENATEX ( ids, ' + NAME_OF.format("[@p]") + ', ", ", [@p], ASC ) & "." )',
      "The plan table read aloud: what it lists and which initiatives are in the package in focus.")
alt_m("Cumulative",
      'VAR pb = [Focus Payback Year] VAR s = [Selected Scenario] '
      "VAR lo = CALCULATE ( [Focus Cumulative Net (Low)], 'Date'[Year] = 2032 ) VAR ex = CALCULATE ( [Focus Cumulative Net (Expected)], 'Date'[Year] = 2032 ) VAR hi = CALCULATE ( [Focus Cumulative Net (High)], 'Date'[Year] = 2032 ) "
      'RETURN IF ( ISBLANK ( [Focus Package] ), BLANK (), "Line chart, 2027 to 2032, of the cumulative net impact of package " & [Focus Key] & " in the Low, Expected and High cases. " '
      '& IF ( ISBLANK ( pb ), "In the " & s & " case it does not pay back by 2032", "In the " & s & " case it turns positive in " & pb ) '
      '& ". By 2032: Low " & ' + sfm("lo") + ' & ", Expected " & ' + sfm("ex") + ' & ", High " & ' + sfm("hi") + ' & "." )',
      "The cumulative chart read aloud: payback year in the case in view and the 2032 end points of the three cases.")


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
        { "C", "C · Why not renovate? For comparison", 3 }
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
        out.append(f"\t\tformatString: {fmt}")
        out.append(f"\t\tdisplayFolder: {folder}")
        if name in IMAGE_MEASURES:
            out.append("\t\tdataCategory: ImageUrl")
        out.append(f"\t\tlineageTag: {tag('measure.' + name)}")
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
    tables = list(SHIPPED) + ["_Measures", "ProjectCashflow", "HotelOutlook", "Timeline", "PlanYear", "BridgeStep", "FolioLine", "KpiLine", "Package", "PackageProject", "PlanSelector", "ScatterView"]
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
