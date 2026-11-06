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
        calc_col("InvestmentProjects", "Completion Date", "EDATE(InvestmentProjects[EarliestStart], InvestmentProjects[DurationMonths])", "dateTime", "Short Date",
                 doc="Earliest start plus duration: the month the project goes live."),
    ]),
}

# ---------------------------------------------------------------- calculated tables

PROJECT_CASHFLOW = r"""
VAR RampY1 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - first year after completion" )
VAR RampY2 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - second year after completion" )
VAR RampY3 = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Ramp-up - third year onwards" )
VAR FirstYear = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Earliest investment date" )
VAR LastYear = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Impact horizon" )
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
            VAR vStart = LOOKUPVALUE ( InvestmentProjects[EarliestStart], InvestmentProjects[ProjectID], vPid )
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
                        RETURN IF ( 'Date'[Date] >= vDone, vRev / 12 * SWITCH ( TRUE (), vM < 12, RampY1, vM < 24, RampY2, RampY3 ), 0 )
                )
        ),
        "ProjectID", InvestmentScenarios[ProjectID],
        "Scenario", InvestmentScenarios[Scenario],
        "Month", 'Date'[Date],
        "Capex", [@Capex],
        "Disruption", [@Disruption],
        "Benefit", [@Benefit],
        "RevenueBenefit", [@RevenueBenefit]
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
m("NPV @ 8%", 'VAR r = LOOKUPVALUE ( FinanceParameters[Value], FinanceParameters[Parameter], "Discount rate" ) RETURN SUMX ( FILTER ( ALL ( \'Date\'[Year] ), \'Date\'[Year] >= 2027 ), CALCULATE ( [Net Impact] ) / ( 1 + r ) ^ ( \'Date\'[Year] - 2026 ) )', USDM, C5, "Net impact discounted to 2026 at the FinanceParameters rate, through 2032, no terminal value.")
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
        'RETURN SWITCH ( line, "Room night, average rate", rate, "Paid to the channel", - comm, "What we keep", rate - comm )'
    )


m("Folio OTA Guest", folio("Online Travel Agencies"), r"\$#,0.00;(\$#,0.00)", C7, "The folio: a 2025 OTA room night, what the channel takes and what the hotel keeps.")
m("Folio Direct Guest", folio("Direct Website & App"), r"\$#,0.00;(\$#,0.00)", C7, "The folio: the same room night booked on the brand's own site or app.")
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


def measures_table():
    out = ["/// Measure home for the three sketches. Base measures read columns; everything else reads measures.", "table _Measures", f"\tlineageTag: {tag('table._Measures')}", ""]
    for name, dax, fmt, folder, doc in MEASURES:
        out.append(f"\t/// {doc}")
        out.append(f"\tmeasure {q(name)} = {dax}")
        out.append(f"\t\tformatString: {fmt}")
        out.append(f"\t\tdisplayFolder: {folder}")
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
    tables = list(SHIPPED) + ["_Measures", "ProjectCashflow", "HotelOutlook", "Timeline", "PlanYear", "BridgeStep", "FolioLine"]
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
        [("ProjectID", "string", None), ("Scenario", "string", None), ("Month", "dateTime", "Short Date"), ("Capex", "double", USD), ("Disruption", "double", USD), ("Benefit", "double", USD), ("RevenueBenefit", "double", USD)],
        PROJECT_CASHFLOW))
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
        [("Room night, average rate", 1), ("Paid to the channel", 2), ("What we keep", 3)],
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
