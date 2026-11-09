# 09 - Research based rebuild: toepassing van het KPI-onderzoek

**Datum:** 2026-11-09 · **Gevraagd door:** Bjorn (WhatsApp, 9 november 09:43: "Kan je dit dan toevoegen in de repository en heel specifiek duiden hoe wat en waar de gekozen elementen geïmplementeerd kunnen worden? Dus data inhoudelijk en technisch. Noem het maar research based rebuild") · **Stage:** 0 (plan, geen build-wijziging).

**Bron:** `research/2026-11-09-brand-kpis-wat-echt-telt.md` (PR #9): het onderzoek "Brand report & investment plan: welke KPI's echt tellen (en welke niet)". Dit document legt per gekozen element vast **wat** er verandert (inhoud), **met welke data** het kan (velden uit de PillowKey-dataset, met haalbaarheidscheck) en **waar** het landt (generator, functie, measure, visual). Implementatie volgt pas na Bjorns go-ahead en loopt altijd via de generators - nooit handmatig in Desktop (fixgids 07 paragraaf 2).

**Relatie met bestaande plannen:** dit is geen vervanging van `07-fixgids-review-v2.md` en `08-verbeterplan-ronde-3.md`. Waar een punt overlapt (R3 hier vs. F2/K1/V1 daar), staat dat erbij. Volgorde van implementatie blijft die van 08 paragraaf 4, met deze punten als toevoeging aan de copy- en framingstap.

**Geldende randvoorwaarden (ongewijzigd):**

- *Do-not-fabricate:* elk cijfer dat op een canvas landt wordt opnieuw uit het model afgeleid (stage 4/6). Onderzoeksgetallen (bijvoorbeeld de £1,87/£4,11 uit Profit Ability 2) komen nergens als getal op het canvas; ze zijn alleen argument voor de vorm.
- *Alleen aangeleverde data:* geen externe reeksen in het model (wedstrijdregel, MISSION paragraaf 1.6).
- *Accessibility:* verdicts nooit alleen in kleur (brand-guide sectie 6; het onderzoek bevestigt de harde accessibility-drempel van de jury), contrast >= 4.5:1, Key Takeaway zichtbaar op de landingspagina (in de huidige build: `z_headline` + `c_subtitle` op P1).
- *Horizon-framing:* NPV tot 2032 én 2032-run-rate plus payback-jaar tonen (SCOUT "horizon trap"); het onderzoek sluit hierop aan met de kort/lang-rendementlogica.

---

## R1 - Prijskracht op P1: ADR- en RevPAR-index naast absolute waarden

**Inhoudelijk.** Het onderzoek noemt prijspremie/pricing power een must-have KPI (Kantar: pricing power als sterkste winstdriver van brand; IPA). De huidige hero-tabel (`hero_brand_compare`) toont ADR en RevPAR als absolute bedragen met `Direction = 0` (niet gerankt), omdat een budgetmerk geen zinnige absolute prijsvergelijking heeft met Maison d'Or ($527,9 ADR). De subtekst (`c_compare_sub`) zegt dat al. Wat mist is de *beweging*: wie wint of verliest prijskracht. Een index (2021 = 100 per merk) maakt die vergelijking segment-schoon mogelijk en past bij de "waarde"-as die de pagina nu niet heeft.

**Data.** Volledig aanwezig, geen nieuwe bronnen: `MonthlyPerformance[RoomRevenue]`, `[RoomsSold]`, `[RoomsAvailable]` per hotel per maand 2021-2025. De basissmaten bestaan al: `[ADR]` = `DIVIDE ( [Room Revenue], [Rooms Sold] )` en `[RevPAR]` = `DIVIDE ( [Room Revenue], [Rooms Available] )` in `project/tools/sketch_model.py` (regel ~359-360). Per-merkberekening loopt via het bestaande `brand()`-patroon (regel ~570). **Haalbaarheidscheck eerst:** bereken de vier indexen 2021-2025 offline (zelfde route als `project/analysis/`) en kijk of GN's indexlijn het verhaal draagt voordat de rij op het canvas komt - het onderzoek geeft zelf aan dat hotel-KPI's niet specifiek aan brand-equity-onderzoek gekoppeld zijn (caveat c).

**Technisch.**

- `sketch_model.py`: twee nieuwe measures in folder C1 naast ADR/RevPAR, patroon van `[RevPAR vs 2024 (text)]` (regel ~523): bijvoorbeeld `ADR Index (2021 = 100)` en `RevPAR Index (2021 = 100)` via de bestaande `yr()`-helper; tekstvarianten voor de tabel zoals `KPI Text {code}` ze verwachten.
- `sketch_model.py` `KPI_ROWS` (regel ~735): twee nieuwe rijen direct onder de bestaande `adr`/`revpar` (sort 2a/3a): key `"adrix"` / `"revparix"`, Finding-label leeg (vallen onder F1), Measure "ADR index (2021 = 100)" / "RevPAR index (2021 = 100)", Direction 1 (hoger = beter), format `"0"`, delta in punten. De `SWITCH` in `[KPI Value]` (regel ~577) krijgt de twee nieuwe keys.
- Optioneel (als de index sterk genoeg is): een vierde trend-slot in `p1_visuals()` naast `ch_trend_margin` / `ch_trend_ota` / `ch_trend_nps` - zelfde patroon (lineChart, GN in raspberry/ACCENT, zusters in SLATE), eigen titelmeasure `Trend Title RevPAR Index (text)`. Alleen doen als het canvas het toelaat (V4-canvasruimte uit 08 geldt ook hier); anders blijft het bij de tabelrijen.
- Copy: `c_compare_sub` in `opzet_report.py` aanpassen: absolute tarieven niet gerankt, index wél - dat is dan precies waarom de index er staat.

**Acceptatiecheck.** Een jurylid ziet in de hero-tabel dat GN's prijskracht-beweging (index) vergelijkbaar is met de drie zusters, zonder dat er een absoluut budget-vs-luxe-vergelijk op het canvas staat; natelbaar uit MonthlyPerformance; rang-pijltje en kleur dragen het verdict dubbel (sectie 6).

---

## R2 - NPS herframen: van merk-KPI naar operationeel kwaliteitssignaal

**Inhoudelijk.** Het onderzoek is helder: NPS is geen groeivoorspeller (Keiningham et al., 2007; IJMR 2024: kritiek "unresolved") en hoort niet als "the one number" op een executive-pagina. Onze NPS-daling (+8.5 naar +3.3) blijft een echt feit uit de data, maar de rol verandert: symptoom van eroderende gastkwaliteit, naast comfort (7.17, laagste van vier) en stijgende room-condition complaints - niet dé merkuitkomst. Dit is een copy-aanpassing, geen herbouw.

**Data.** Ongewijzigd: `GuestExperience` (survey responses, 6 scores 0-10, NPS) - measures `[NPS (weighted)]`, `[Room Comfort (weighted)]`, `[Value for Money (weighted)]` bestaan (folder C3). Geen nieuwe berekening nodig.

**Technisch.**

- `sketch_model.py` `KPI_ROWS` rij 13 (key `"nps"`): het Finding-label `"F3 · Recommend us?"` herformuleren zodat NPS als kwaliteitssignaal onder F3 leest (bijvoorbeeld `"F3 · A good night?"` al bij comfort laten en NPS als laatste bewijsregel van F3, niet als eigen ladder-trede "resonance"). Let op: de Keller-ladder-comment boven KPI_ROWS (salience/performance/judgment/resonance) moet meebewegen zodat de redenering in de code klopt met het canvas.
- `sketch_model.py` trend-titelmeasures: `Trend Title NPS (text)` (gebruikt door `ch_trend_nps` in `p1_visuals()`) zodanig dat de titel NPS als operationeel signaal kadert, niet als merkgezondheid.
- `sketch_model.py` `Subtitle P1 (text)` en `Headline Wall (text)`: check dat de koppen de NPS niet als hoofdbewijs noemen; de "goodwill"-formulering uit fixgids F7 blijft leidend.
- Tooltip/methodologie: één zin dat NPS als groeimaatstaf bewust niet centraal staat (Keiningham 2007), kan in de voetnoot van R4 meeliften.

**Acceptatiecheck.** Nergens op P1 wordt NPS gepresenteerd als dé merk-KPI of groeivoorspeller; de daling staat er nog wel, als onderdeel van het kwaliteitsverhaal F3; cijfers ongewijzigd natelbaar.

---

## R3 - P2 scherper op marginale ROI: waarom het volgende pakket níet gefinancierd wordt

**Inhoudelijk.** Het onderzoek (Profit Ability 2): CFO's kiezen op incrementeel rendement, payback en risico - en de sterkste investeringspagina laat zien waarom de volgende euro níet wordt uitgegeven. Dat hebben we deels al: de scatter toont alle 456 pakketten, C is geframed als antwoord op "waarom niet alles renoveren" (verbeterplan V1) en de not-funded-reden wordt "each would lower the package NPV" (fixgids F2). Wat erbij komt: één expliciete regel die de marginale toets benoemt - het beste pakket dat net boven A ligt verdient minder dan het kost, dus blijft $50.6M bewust in kas. Koppelt ook aan de horizon-framing: run-rate 2032 ("exit velocity") naast NPV, zoals SCOUT dat al voorschrijft.

**Data.** Volledig aanwezig in de eigen modeltabellen: `Package` (456 rijen, NPV Low/Expected/High), `PackageProject` (pakket -> initiatief), `InvestmentProjects` (capex, running cost), measures `[Focus NPV (sel)]`, `[Focus NPV Low]`/`[Focus NPV High]`, `[2032 Run-rate]`, `[Focus Payback Year]` (folder C6/C9). De rangorde komt uit `project/analysis/output/packages.csv` (offline herberekend, reconcilieert exact).

**Technisch.**

- `sketch_model.py`: nieuwe tekstmeasure (folder C9), bijvoorbeeld `Plan Margin (text)`: zoekt het beste pakket dat strikt meer initiatieven bevat dan het focuspakket (of simpelweg de #2 op NPV boven A) en formuleert: "The next package costs $X.XM more and adds -$Y.YM of NPV - that is why $50.6M stays in the bank." Implementatie als `CALCULATE` over `Package` met filter op `Package[NPV Expected] < [Focus NPV (sel)]`, TOPN 1, zelfde patroon als `Scatter Title (text)` (regel ~715). Bewaken: als de focus niet A is, valt de regel weg (BLANK) - geen valse claims bij B of C.
- `sketch_model.py` `Plan Risk (text)` (regel ~720): behoud de risicozin; de marginale toets hoort op de *landing/shortlist*, niet in de risicoregel. `Uncertainty (text)` (regel ~726) blijft de disclaimer dragen.
- `opzet_report.py`: `c_plan_risk` bestaat al als dyn op de planstate; voor de landing een nieuwe `dyn(..., "Plan Margin (text)")` in `p2_visuals()` op een bestaand leeg slot in `opzet-layout.json` (volg V4: geen loze banden creeren). Font >= het R4-minimum (circa 16 px op 1920).
- Randvoorwaarde: dit punt gaat ervan uit dat A, B en C bevroren sets zijn (kans K1 uit fixgids 07). Met dynamische regels kan "het volgende pakket" per scenario verschillen en wordt de zin onbetrouwbaar - K1 eerst.

**Acceptatiecheck.** Een jurylid dat alleen de landing ziet kan zeggen waarom niet méér wordt gefinancierd; de bedragen in de zin zijn natelbaar uit `packages.csv`; bij focus B of C verdwijnt de regel schoon (geen lege of valse tekst, zelfde bewaking als F1).

---

## R4 - Voetnoot "bewust niet getoond"

**Inhoudelijk.** Het onderzoek adviseert vanity metrics te vermijden en stelt dat een expliciete voetnoot ("bewust niet getoond: impressies, likes, NPS als groeimaat") de inhoudelijke positie juist versterkt. Goedkoop en past bij Analytical Quality.

**Data.** Geen - pure copy.

**Technisch.** `opzet_report.py` constante `FOOTER` (regel ~45) wordt op beide pagina's gebruikt (`z_footer`, `z_footer2`): één zin toevoegen, bijvoorbeeld "Deliberately not shown: impressions, likes, and NPS as a growth measure - effectiveness research does not support them (see research/2026-11-09)." Fontgrootte van de footer checken tegen het R4-minimum; zo nodig als losse `tb` op P1 alleen.

**Acceptatiecheck.** De zin staat leesbaar op beide pagina's op 1366 breed; geen verwijzing naar cijfers die niet in de dataset zitten.

---

## R5 - Double Jeopardy / penetratie: alleen als interpretatie-lens

**Inhoudelijk.** Het onderzoek zet penetratie boven loyaliteit (Ehrenberg-Bass) en stelt een Double Jeopardy-diagnose voor. De dataset kan dat niet dragen: `GuestSegments` (49,050 rijen) telt boekingen per segment per maand, zonder gast-ID over tijd, dus unieke-gastpenetratie en koopfrequentie per gast zijn niet berekenbaar. Wat rest is de *gedachte* als lens: GN is het budgetmerk met de grootste fysieke beschikbaarheid (50 hotels, 6,485 kamers, 79% bezetting, beste bezetting van de vier) - groei komt hier uit bereik/herhaalverkeer via directe kanalen, niet uit loyaliteitsverzwarende programma's. Dat legitimeert de voorkeur voor direct-boekingsinitiatieven (GI-01/GI-10/GI-02) boven het loyalty-spoor, maar alleen als interpretatie, gelabeld.

**Data.** Geen nieuwe berekening. De interpretatie rust op bestaande feiten: `[Occupancy %]` (best-of-4), `[OTA Share %]` / `[Direct Share %]`, `Brands[Segment]`/`[Positioning]`.

**Technisch.** Hooguit één zin in de bestaande subtekst bij F2 ("Booked with us?") via `c_compare_sub` of een KpiLine-finding label in `sketch_model.py`, met de FEIT/INSCHATTING-conventie: deze zin is INSCHATTING (interpretatie), geen FEIT uit de data. Geen Double Jeopardy-scatter bouwen - die zou verzonnen assen vereisen.

**Acceptatiecheck.** De penetratie-gedachte staat nergens als getal of grafiek op het canvas; waar hij in tekst voorkomt, is hij als interpretatie herkenbaar.

---

## Uitgesloten (gemotiveerd, niet meenemen)

- **Share of search (+ ESOS):** geen zoekvolume-data in de PillowKey-dataset; externe data is verboden (MISSION 1.6). Ook als contextzin op het canvas riskeert het een onverifieerbare claim.
- **SOV / ESOV en de 10:0.5-regel:** er is geen mediaspend per merk in de data; de $60M is capex over 10 gedefinieerde initiatieven, geen mediabudget. De ESOV-redenering past niet op deze beslissingssoort.
- **60/40 brand-activation:** zelfde reden - geen mediabudget om te verdelen; Profit Ability 2 noemt de indeling zelf "at best unhelpful".
- **Salience / consideration / awareness als KPI:** geen brand tracker in de dataset. De KpiLine leunt al op Keller's ladder met wat de data wél heeft (bezetting als "booked with us", comfort als "a good night", value-for-money als "a fair price", NPS als "recommend us") - dat is de verdedigbare proxy en blijft zo.
- **Budgetbenchmarks (Gartner/CMO Survey):** niet relevant voor deze capex-case; hooguit kennis voor de jury-Q&A, niet op het canvas.
- **MMM / attributie / attentiemetrics:** niet van toepassing op de aangeleverde data en beslissing.

---

## Implementatievolgorde (indien goedgekeurd)

1. R3 samen met K1/V1 (bevroren pakketten + C-framing) - één rebuild van `sketch_model.py`.
2. R2 (NPS-copy) en R4 (voetnoot) - zelfde rebuild; puur measures/copy.
3. R1 na de offline haalbaarheidscheck van de indexlijnen; eventueel trend-slot alleen als het canvas het toelaat (V4).
4. R5 als zinnetje in dezelfde copy-rebuild.
5. Daarna de vaste cyclus: `schema_check.py`, rebuild, renders op 1920 en 1366, eigen-ogen review (K6), en de Publish-to-Web-gate bij Bjorn (R6/N10 uit 08).
