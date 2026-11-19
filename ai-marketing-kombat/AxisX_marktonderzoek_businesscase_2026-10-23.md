# AxisX — Marktonderzoek en onderbouwing businesscase

**Datum:** 23 oktober 2026  
**Taal:** Nederlands  
**Bestemming:** overdracht aan Claude (AI Marketing Kombat / AxisX)  
**Status:** onderzoeksnotitie, niet de definitieve case-inzending

## Doel en leeswijzer

Dit bestand bevat de uitkomsten van vijf onderzoeksvragen over de AxisX-casus:

1. Hoeveel gebruikers van gratis health-apps worden betalend?
2. Hoe groot is de doelgroep vrouwen van 40–55 in UK, US en Noord-Europa; hoeveel daarvan zijn vermoedelijk via iPhone bereikbaar; en welke advertentie-CPM's zijn aannemelijk?
3. Welke targeting, meting en optimalisatie laten Meta en Google bij health-apps toe?
4. Is een individuele quizdeelnemer betrouwbaar te volgen tot dag 7, ook via TestFlight?
5. Welke formaten en looptijden zien we bij concurrentieadvertenties?

**Belangrijk bij hergebruik:**
- `BRON / GECONTROLEERD`: gepubliceerde benchmark of officieel platformbeleid, met link.
- `BEREKEND / INDICATIEF`: zelf berekend, afhankelijk van definities en invoerwaarden; geen officieel waargenomen marktaantal.
- `AANNAME / SCENARIO`: alleen bedoeld voor financiële of mediaplanning.
- `TE VALIDEREN`: nog niet afgedekt met direct bewijs of account-specifieke platformcontrole.
- De cijfers uit verschillende datasets mogen niet worden opgeteld of vermenigvuldigd alsof het dezelfde meetpopulatie of hetzelfde conversievenster betreft.

**Werkhypothesen AxisX (afkomstig uit de voorgaande casusbespreking, niet extern geverifieerd):** iOS-bèta via TestFlight; eerste cohort van 500 gebruikers; quiz gevolgd door een app-/begeleidingsprogramma; D7-retentie-doel van 60%; mogelijke jaarprijs £100; doelgroep vrouwen van ongeveer 40–55 jaar. Controleer deze uitgangspunten tegen de laatste AxisX-casebrief.

---

## 1. Economisch anker — gratis naar betaald

### Verifieerbare benchmarks

Bron: **RevenueCat — State of Subscription Apps 2026** (geaggregeerde benchmarks van abonnementsapps; referentiegegevens grotendeels 2025).

| Maatstaf | Benchmark | Populatie en interpretatie |
|---|---:|---|
| Freemium download-to-paid bij dag 35 | **2,1%** | Mediaan alle categorieën, freemium-model |
| Hard paywall download-to-paid bij dag 35 | **10,7%** | Mediaan alle categorieën, ander toegangsmodel; niet direct vergelijkbaar zonder modelkeuze |
| Health & Fitness download-to-paid bij dag 35 | **2,9%** | Mediaan categorie, gecombineerde platformen |
| Health & Fitness op iOS download-to-paid bij dag 35 | **3,5%** | Mediaan iOS-categorie |
| Health & Fitness download-to-trial bij dag 30 | **6,9%** | Conversie naar proefabonnement, andere teller en periode |
| Health & Fitness trial-to-paid | **37,7%** | Mediaan onder gestarte trials; niet vermenigvuldigen met anders gedefinieerde cohortcijfers zonder controle |

**Directe bron:** https://www.revenuecat.com/state-of-subscription-apps

**Interpretatie:** de 2,1% is het meest conservatieve expliciete freemium-anker voor de eerste AxisX-businesscase. De 3,5% geeft een gunstiger **iOS Health & Fitness**-referentie, maar beschrijft niet noodzakelijk dezelfde freemium-subgroep. Het verschil tussen freemium, hard paywall en trial is methodologisch belangrijk.

### Scenario voor 500 installaties

Formule: `verwachte betalers = installaties × conversiepercentage`; `theoretische bruto jaarverkoop = verwachte betalers × £100`.

| Scenario | Conversie | Verwachte betalers van 500 | Theoretische bruto jaarverkoop |
|---|---:|---:|---:|
| Downside (aanname) | 1,0% | 5,0 | £500 |
| Freemium-median (bronbenchmark) | 2,1% | 10,5 | £1.050 |
| iOS H&F-vergelijking (bronbenchmark) | 3,5% | 17,5 | £1.750 |
| Upside (aanname) | 5,0% | 25,0 | £2.500 |

De aantallen 10,5 en 17,5 zijn **verwachtingswaarden**, niet halve klanten. De bedragen veronderstellen dat elke betalende gebruiker het volle jaarabonnement van £100 koopt; ze zijn **geen gerealiseerde omzet, netto-omzet of LTV**. Belasting, Apple-commissie, prijsverdeling, refunds, marketingkosten, churn en timing ontbreken. Een jaarlijkse prijs van £100 kan aanzienlijk hoger zijn dan het gebruikelijke jaarlijkse prijspunt van veel Health & Fitness-apps; neem dus geen categorieconversie zonder prijsgevoeligheid over.

**Conclusie voor de case:** laat de eerste bèta primair waardepropositie, activatie en retentie bewijzen; positioneer betaalconversie als afzonderlijke commerciële validatie ná of buiten TestFlight. Gebruik 1%, 2,1% en 3,5–5% als expliciete scenario's, niet als belofte.

---

## 2. Plafond in getallen — doelgroep, iOS en advertentiekosten

### Definitie

`Noord-Europa` = **Zweden, Denemarken, Noorwegen, Finland en IJsland**; het Verenigd Koninkrijk wordt apart meegeteld. Een andere geografische afbakening verandert de totaalcijfers.

Leeftijd `40 t/m 55 jaar (inclusief)` is in de eerdere berekening benaderd als:

`vrouwen 40–44 + vrouwen 45–49 + vrouwen 50–54 + 20% van vrouwen 55–59`.

Bronkader: UN World Population Prospects 2024, projecties voor 2026. De onderstaande landuitkomsten zijn overgenomen uit de eerdere analyse en **dienen als indicatieve cijfers**: voor een officieel te publiceren TAM moet Claude de exacte leeftijds-/seksegegevens opnieuw uit UN WPP downloaden en de berekening reproduceren.

### Demografische TAM en iPhone-proxy

| Markt | Vrouwen 40–55 (indicatie) | Gebruikte iOS-/iPhone-proxy | Vermenigvuldigde proxy (indicatie) |
|---|---:|---:|---:|
| Verenigde Staten | 33,98 mln | 53,6% | 18,21 mln |
| Verenigd Koninkrijk | 7,18 mln | 52,0% | 3,74 mln |
| Zweden | 1,04 mln | 56,1% | 0,58 mln |
| Denemarken | 0,58 mln | 62,7% | 0,37 mln |
| Noorwegen | 0,57 mln | 58,7% | 0,34 mln |
| Finland | 0,55 mln | 32,5% | 0,18 mln |
| IJsland | 0,04 mln | 60,2% | 0,02 mln |
| **Totaal** | **ca. 43,94 mln** | n.v.t. | **ca. 23,43 mln** |

**Wat deze getallen niet zeggen:**

- De iPhone-kolom is **geen** gemeten aantal unieke iPhone-gebruikende vrouwen van 40–55 jaar. Statcounter meet grotendeels OS-verkeersaandelen, niet het bezit of aantal personen. De UK-bron is een survey onder smartphonegebruikers van 35–54 jaar, eveneens niet exact de AxisX-doelgroep.
- Niet gecorrigeerd voor smartphonepenetratie, type device, gender/age-interacties, geografische verschillen binnen landen, dubbele apparaten, interesse in menopauze, klachtprevalentie, motivatie of betaalbereidheid.
- Het aandeel 55-jarigen is lineair benaderd (1/5 van vijfjaarscohort).
- De precieze percentages variëren per meetmaand en platformfilter. **Gebruik deze 23,4 miljoen niet als SAM of direct advertentiebereik.**

**Bronnen en verificatielinks:**

- UN World Population Prospects 2024: https://population.un.org/wpp/
- UN DemoData (leeftijd/geslacht, export): https://population.un.org/demodata/home
- Statcounter mobiele OS-aandelen, VS: https://gs.statcounter.com/os-market-share/mobile/united-states-of-america
- Statcounter mobiele OS-aandelen, VK: https://gs.statcounter.com/os-market-share/mobile/united-kingdom
- Statcounter, Zweden: https://gs.statcounter.com/os-market-share/mobile/sweden
- Statcounter, Denemarken: https://gs.statcounter.com/os-market-share/mobile/denmark
- Statcounter, Noorwegen: https://gs.statcounter.com/os-market-share/mobile/norway
- Statcounter, Finland: https://gs.statcounter.com/os-market-share/mobile/finland
- Statcounter, IJsland: https://gs.statcounter.com/os-market-share/mobile/iceland
- Ofcom, *Online Nation 2025* (figure 15: bij Britse smartphonebezitters van 35–54 is 52% iPhone; niet vrouwen 40–55): https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf

### Media-inkoop: CPM

**BRON / GECONTROLEERD:** Triple Whale rapporteert voor Meta **Health & Wellness een mediane CPM van $21,80**, periode augustus 2025–juli 2026. Dit is een sectorbenchmark, niet een gemeten CPM voor vrouwen 40–55 met een perimenopauze-app.

Bron: https://www.triplewhale.com/blog/facebook-ads-benchmarks

Algemene, minder specifieke Meta-landindicaties genoemd in de eerdere analyse: US circa $16; UK circa $12; verschillende Noordse markten circa $7–9. Deze landcijfers zijn **niet opnieuw onafhankelijk geverifieerd met dezelfde bronmethodiek** en mogen niet als health-specifieke benchmarks worden geciteerd.

**AANNAME / te toetsen bij campagne-inzet:**

| Markt | Conservatieve planningsbandbreedte Meta CPM | Status |
|---|---:|---|
| US | $22–35 | aanname, geen gemeten AxisX-CPM |
| UK | $15–28 | aanname |
| Noordse landen | $12–25 | aanname |

`Kosten = impressies / 1000 × CPM`.

Voorbeeld: bij $22 CPM kosten 1 miljoen **impressies** ongeveer $22.000. Dat zijn geen 1 miljoen unieke bereikte vrouwen, vanwege frequentie. Google Search draait doorgaans op CPC; Google App Campaigns op installaties/in-app-acties en pas na beschikbaarheid van de app in de appstore (zie §3). Een uniforme 'Google health-CPM' is daarom niet betekenisvol.

**Beslissing:** ruim demografisch plafond; de beperking voor de eerste 500 gebruikers zit vooral in vertrouwen, relevantie, activering en kostenefficiënte distributie. Voor een investeerbare forecast: modelleer apart `TAM → relevantie → bereikbaar publiek → bezoek → quiz → registratie → activatie → D7 → betaald` met eigen aannames en gevoeligheidsanalyse.

---

## 3. Meta- en Google-beleid: targeting en optimalisatie

**Kern:** een advertentie mogen tonen betekent **niet** dat alle gebeurtenissen in de health-funnel naar Meta/Google mogen worden doorgestuurd of gebruikt voor retargeting en algoritmische optimalisatie.

### Google Ads — relatief helder beleid

Health is een **Sensitive Interest Category** in het personalisatiebeleid. De volgende **advertiser-curated audiences** zijn bij gevoelige categorieën niet toegestaan: Customer Match, eigen datasegmenten / remarketing, audience expansion en lookalike segments. Bepaalde door Google vooraf gedefinieerde doelgroepen, demografie (met uitzonderingen), geografie en toegestane contextuele methoden kunnen wel.

- Officiële policy: https://support.google.com/adspolicy/answer/16701855?hl=en
- Algemeen beleid restricted targeting: https://support.google.com/adspolicy/answer/143465

Voorbeeld:
- **Veiliger:** brede/contextuele campagne met een neutrale propositie over ondersteuning bij perimenopauze.
- **Niet als uitgangspunt:** remarketing van vrouwen met specifieke aangegeven klachten of audience-upload op basis van symptoomquiz.

**Extra kanaalblokkade:** Google vereist voor normale **App Campaigns** een app die te downloaden is in Apple App Store of Google Play. Alleen TestFlight voldoet niet. Een reguliere Search-campagne die naar een openbare informatie-/quizlandingspagina leidt kan mogelijk wel, mits tekst, landingspagina, data en targeting aan beleid voldoen.

- Google App Campaigns requirements: https://support.google.com/google-ads/answer/6247380?hl=en

### Meta — ad approval versus datadeling

Meta verbiedt het via de Business Tools doorgeven van informatie die gevoelige gezondheidsinformatie bevat of daaruit kan worden afgeleid. Bij websites/apps in health & wellness kunnen afhankelijk van de classificatie datadeling en bepaalde standaardevents beperkt worden. In de eerdere analyse werden restrictieklassen beschreven (Core Setup, Standard Event Restrictions, Full Restrictions); **controleer de huidige exacte restrictie en toegestane events in AxisX Events Manager vóór kanaalkeuze.** Niet iedere health-app krijgt automatisch een volledige blokkade.

- Meta Business Tools Terms: https://www.facebook.com/legal/technology_terms
- Meta help, data-sharing restrictions: https://www.facebook.com/business/help/511197658391698

### Kanalenmatrix voor besluitvorming

| Gebruik | Meta | Google | AxisX-advies |
|---|---|---|---|
| Informatieve campagne op basis van toegestane brede targeting | In beginsel mogelijk | In beginsel mogelijk | Eerst advertentie-/beleidstoets |
| Demografie/geografie | Mogelijk, onder actuele delivery-/audience-instellingen | Mogelijk, met uitzonderingen | Niet gelijkstellen aan exact bereik |
| Segment gebaseerd op ingevulde health-quiz | Niet gebruiken | Niet gebruiken | Geen symptom-based advertentieaudiences |
| `QuizCompleted` / `Day7Active` als advertentie-event | Kan beperkt of verboden zijn door gegevensinhoud en databronrestricties | Niet zonder passende policy-/privacytoets | First-party intern vastleggen; niet standaard doorsturen |
| Purchase-/registratie-optimalisatie | Afhankelijk van Meta-databronrestricties | Afhankelijk van beleidskader / toegestane data | Per event feitelijk toetsen, geen automatisme |
| App-installs naar TestFlight via App Campaigns | Eigen test-/linkstrategie vereist | **Geen normale App Campaigns zolang app niet live in store staat** | Begin niet met Google App Campaigns |

**Waarschuwing:** gezondheidstargeting, AVG/GDPR, Apple ATT, cookie-/SDK-consent en advertentieverificatie zijn **verschillende** eisen. Een pseudoniem of gehashte identifier maakt gevoelige informatie niet automatisch advertentiegeschikt. Onderzoek ook eventuele healthcare-/medical claims in teksten en US/UK-specifieke gezondheidsadvertentieregels.

**Aanbeveling:** het acquisitieplan voor het bèta-cohort mag niet afhankelijk zijn van het terugsturen van gezondheids- of symptoomgebaseerde events naar Meta/Google. Gebruik eigen first-party cohortmetrics en publieke/brede content, community's, partnerships en andere privacyconforme kanalen.

---

## 4. Eén user-ID van quiz tot D7, inclusief TestFlight

### Kort antwoord

**Ja, technisch kan dit**, mits AxisX een **eigen, pseudonieme en persistent account-ID** uitgeeft vóór of tijdens de quiz en diezelfde identiteit koppelt wanneer de tester voor het eerst inlogt in de iOS-app. TestFlight maakt die accountkoppeling niet vanzelf.

### Aanbevolen first-party architectuur

```text
[Website / quiz]
   → interne user_id (random UUID; niet e-mail of advertentie-ID)
   → consentstatus en quizdata in afzonderlijke, beveiligde opslag
   → uitnodiging / onboarding met eenmalige token
   → TestFlight-installatie
   → app-login of token redemption
   → koppeling aan dezelfde user_id
   → eventstore: QuizCompleted, AccountCreated, AppActivated,
                 Day1Active, Day3Active, Day7Active
   → cohortanalyse in eigen BI / backend
```

**Minimale eventschema (concept, geen gevoelige parameters):**

| Veld | Doel |
|---|---|
| `event_id` | unieke deduplicatiesleutel |
| `user_id` | first-party pseudonieme user identifier |
| `event_name` | gestandaardiseerde gebeurtenis |
| `occurred_at_utc` | tijdstip in UTC |
| `cohort_start_at_utc` | start van cohort, bv. appactivatie |
| `app_version` / `platform` | technische segmentatie |
| `consent_version` | relevante toestemmingsversie / audit trail |
| `source_category` | privacyvriendelijke herkomstgroepering, zonder health-targeting-data |

**Niet opnemen in generieke marketingevents:** individuele quizantwoorden, symptoomlabels, diagnosevermoedens, e-mailadressen, echte namen en andere gezondheidsinformatie. Leg medisch/gezondheidsinhoudelijke gegevens apart vast met passende rechtsgrond, privacyverklaring en autorisaties.

### Definitie D7-retentie (expliciet kiezen)

Voorstel: `D7 retained = gebruiker met minstens één geldige actieve gebeurtenis op kalenderdag 7 na de gekozen cohortstart`, waarbij kalenderdag en tijdzone consistent zijn. Voor een 24-uursvenster of 'return on or after day 7' ontstaat een **andere** metric; zet dit vóór meten vast.

Voorbeeld:

`D7-retentie = aantal geactiveerde gebruikers met qualifying D7-event / aantal geactiveerde gebruikers in een volledig uitgemeten cohort`.

Rapporteer apart `quiz → uitnodiging`, `uitnodiging → installatie`, `installatie → activatie`, `D1`, `D3`, `D7`. Niet alle 500 uitgenodigde vrouwen zullen activatie bereiken; wees expliciet over de noemer.

### TestFlight-grenzen

| Kenmerk | Beperking / eigenschap |
|---|---|
| Interne testers | maximaal **100** teamleden met passende App Store Connect-rollen |
| Externe testers | maximaal **10.000** |
| Eerste externe build | vereist goedkeuring via TestFlight App Review |
| Uitnodigen | e-mail of openbare link |
| Looptijd build | **90 dagen** geldig; daarna nieuwe build nodig |
| In-app purchases | sandbox: transacties gratis voor testers; geen werkelijke betaalomzet |
| Identiteit bij publieke link | TestFlight levert geen betrouwbare quiz→persoonskoppeling; eigen login nodig |

- Officieel Apple TestFlight: https://developer.apple.com/testflight/
- Apple over sandbox aankopen: https://developer.apple.com/in-app-purchase/
- Apple over 90 dagen: https://developer.apple.com/videos/play/tech-talks/110343/

**Juridische/privacygrenzen:** symptomtracking betreft doorgaans bijzondere gezondheidsgegevens onder EU/UK GDPR. Controleer een passende grondslag én uitzondering voor bijzondere persoonsgegevens, doelbinding, transparantie, dataminimalisatie, bewaartermijn, beveiliging, eventuele DPIA en toestemming voor afzonderlijke doeleinden. Ook Apple's App Tracking Transparency (ATT) kan gelden als gegevens worden gebruikt om een persoon over apps/sites van andere bedrijven te volgen voor advertenties.

**Besluit:** gebruik een first-party `user_id` en eigen eventstore als source of truth. Meet D7 primair op cohortniveau. TestFlight is geschikt om productgedrag en interesse in een betaalpropositie te observeren, niet om echte App Store-betaalconversie te claimen.

---

## 5. Concurrenten: Ad Library-formaten en looptijd

### Datakwaliteit

Voor de oorspronkelijk besproken merken **thePause, Play Health, Waves Women en balance** waren niet voor alle vier individuele, verifieerbare Meta Ad Library-records met startdatum én format beschikbaar. Het zou onjuist zijn om ontbrekende records te verzinnen.

Wel beschikbaar zijn **derdepartij-snapshots** van twee aanvullende merken in dezelfde gezondheid-/menopauzemarkt: **Midi Health** en **Alloy**. Deze zijn nuttig voor creatieve referenties, maar ze zijn geen bewijs van bereik, CPA, ROAS of winstgevendheid. Een langdurig live advertentie kan om tal van redenen live zijn.

### Gevonden creatieve steekproeven (peildatum 5 oktober 2026)

| Merk | Steekproef | Formaten | Mediane looptijd | Voorbeelden | Bron |
|---|---:|---|---:|---|---|
| Midi Health | 31 advertenties | 97% single image; 3% video | **48 dagen** | “Get answers at Midi” (statisch, 34 dagen); “Relief Starts With Being Heard” (video, 49 dagen) | https://www.sprites.ai/midi-health-ads |
| Alloy | 30 advertenties | 80% single image; 17% video; 3% carrousel | **9 dagen** | “Estrogen-Powered Skincare” (statisch, <1 dag); “Treatment, Without The Pharmacy” (statisch, 9 dagen) | https://www.sprites.ai/alloy-ads |

Dit zijn **momentopnamen / selecties**, geen complete formatdistributies van alle advertenties over de tijd. De provider toont bredere libraries (meer advertenties dan de uitgewerkte steekproef). Controleer actuele advertenties en startdatums rechtstreeks in Meta Ad Library indien de bewijsvoering doorslaggevend is.

Meta Ad Library: https://www.facebook.com/ads/library/

### Oorspronkelijke concurrenten

| Merk | Stand van onderzoek | Gevolg |
|---|---|---|
| thePause / Harmoni | Positionering/productinformatie beschikbaar, maar geen betrouwbaar individueel Ad Library-overzicht met duur en format | Niet kwantitatief rangschikken zonder screenshots/advertentie-ID's |
| Play Health | Officiële website meldt sluiting van app en dienstverlening | **Niet** als actieve app-acquisitieconcurrent presenteren; https://playhealth.com/ |
| Waves Women | Product-/pricinginformatie beschikbaar; geen verifieerbare uitgewerkte advertentiesnapshot in dit onderzoek | Ad Library-capture nodig |
| balance (Dr. Louise Newson) | Niet eenduidig geverifieerde advertenties in deze sessie; meerdere bedrijven heten “Balance” | Verifieer exacte Facebook-pagina en page ID voordat je analyseert |

### Format en looptijd op het juiste niveau vastleggen

Aanbevolen aanleverdataset voor Claude:

```csv
brand,facebook_page_id,ad_id,ad_url,first_seen_date,as_of_date,status,format,primary_hook,cta,landing_domain,source_url,confidence
```

Met `run_days = as_of_date - first_seen_date` bij actieve advertenties; leg bij beëindigde advertenties de **laatste** waargenomen actieve datum vast, anders is het slechts een geschatte ondergrens. Creatieve varianten, individuele ads en campagneclusters niet door elkaar tellen. Sla bewijs/screenshot en peildatum op.

**Creative learning, beperkt ondersteund:** de onderzochte voorbeelden bij Midi Health en Alloy bevatten relatief veel statische advertenties. Dat is een argument om statische creatives **mee te testen**, geen grond om video als minder effectief af te schrijven. De propositie ‘begrip/helderheid/erkenning’ is inhoudelijk bruikbaar als creatieve hypothese, maar de dataset levert geen bewezen creatieve effectiviteit.

---

## Integrale consequenties voor AxisX

| Vraag | Onderbouwde uitkomst | Aanbevolen actie |
|---|---|---|
| 1. Betaalconversie | Freemium mediaan 2,1%; Health & Fitness iOS mediaan 3,5% (niet identieke segmenten) | Gebruik scenario's; betaalgedrag apart na bèta valideren |
| 2. Marktmaximum | 43,94 mln vrouwen 40–55; 23,43 mln berekende iOS-proxy, beide indicatief | Herbereken TAM; maak SAM/SOM met expliciete relevante doelgroep en smartphonebezit |
| 3. Ad policies | Gezondheidsinformatie belemmert remarketing en eventdeling; Google App Campaigns vergen store-publicatie | Niet afhankelijk zijn van health-eventoptimalisatie; privacy-/accountaudit vóór paid launch |
| 4. Quiz → D7 | Met een eigen login en first-party user-ID technisch uitvoerbaar | Instrumenteer events en definieer cohort/noemer; scheid symptomen van marketingevents |
| 5. Concurrenten | Midi en Alloy-formats/looptijden onderbouwd met snapshots; originele set deels onvoldoende gedekt | Verzamel exacte Meta Ad Library-records en datum-/formatbewijs |

### Prioriteit voor de hackathon / productvalidatie

1. **Product proof:** duidelijk gedefinieerde D1/D3/D7-cohorten; verifieer of de beoogde 60% D7-retentie daadwerkelijk gemeten kan worden.
2. **Distribution proof:** voldoende relevante testers, bijvoorbeeld via community's, partnerships en vertrouwenwekkende introducties, zonder verboden health-retargeting.
3. **Economic proof:** scenario rond paid conversion en £100, nadrukkelijk nog geen bewezen LTV/CAC-businesscase.
4. **Operational proof:** TestFlight-review, app-login, consent/privacybeheer en eventinstrumentatie gereed voor een cohort van 500.
5. **Creative proof:** statische en video-adconcepten naast elkaar testen; op basis van echte performance beslissen, niet op advertentieloopduur alleen.

**Samenvattend advies:** beschouw het eerste cohort van 500 gebruikers primair als **product- en retentievalidatie**. Voor een geloofwaardige economische case zijn naast D7-retentie later afzonderlijke betaalconversie, CAC, netto-ARPU/LTV, refundrate en kanaalrestricties noodzakelijk.

---

## Openstaande controles vóór formele externe indiening

- [ ] AxisX-casebrief nalopen: exacte doelgroep, aanbod, prijs, TestFlight-plan, D7-definitie.
- [ ] UN WPP 2026 per land op geslacht/leeftijd downloaden en de 40–55 totalen reproduceerbaar vastleggen.
- [ ] iPhone-bereik vervangen door daadwerkelijk smartphone-/iOS-bezit onder vrouwen 40–55 waar mogelijk; anders duidelijke bandbreedte gebruiken.
- [ ] Meta Events Manager: restrictiestatus voor de AxisX-site/app en elke gewenste optimalisatiegebeurtenis controleren.
- [ ] Google Ads: concrete campagnevorm en toegestane conversies juridisch/technisch toetsen.
- [ ] Consentflow en scheiding tussen health-data en marketingeventdata valideren.
- [ ] App Store Connect / TestFlight, eerste externe build-review, 90-dagenverval en loginflow testen.
- [ ] Concurrerende advertenties per exacte brand/page/ad-ID, format en startdatum vastleggen; geen prestaties afleiden uit looptijd.

## Volledige kernbronnen

1. RevenueCat, *State of Subscription Apps 2026* — https://www.revenuecat.com/state-of-subscription-apps
2. United Nations, *World Population Prospects 2024* — https://population.un.org/wpp/
3. UN Population Division, *DemoData* — https://population.un.org/demodata/home
4. Ofcom, *Online Nation 2025* — https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-research/online-nation/2025/online-nations-report-2025.pdf
5. Statcounter, *Mobile OS Market Share* — https://gs.statcounter.com/os-market-share/mobile
6. Triple Whale, *Facebook Advertising Benchmarks* — https://www.triplewhale.com/blog/facebook-ads-benchmarks
7. Google Ads, *Health in personalised advertising* — https://support.google.com/adspolicy/answer/16701855?hl=en
8. Google Ads, *Restricted targeting in personalised advertising* — https://support.google.com/adspolicy/answer/143465
9. Google Ads, *About App campaigns* — https://support.google.com/google-ads/answer/6247380?hl=en
10. Meta, *Business Tools Terms* — https://www.facebook.com/legal/technology_terms
11. Meta, *Data-sharing restrictions* — https://www.facebook.com/business/help/511197658391698
12. Apple, *TestFlight* — https://developer.apple.com/testflight/
13. Apple, *In-App Purchase / sandbox testing* — https://developer.apple.com/in-app-purchase/
14. Apple, *Get started with TestFlight* — https://developer.apple.com/videos/play/tech-talks/110343/
15. Meta, *Ad Library* — https://www.facebook.com/ads/library/
16. Sprites, *Midi Health Ads (snapshot)* — https://www.sprites.ai/midi-health-ads
17. Sprites, *Alloy Ads (snapshot)* — https://www.sprites.ai/alloy-ads
18. Play Health, *Official shutdown notice* — https://playhealth.com/

---

## Overdrachtsinstructie voor Claude

Behandel dit bestand als een **onderzoeksbijlage** bij de AxisX-casus. Neem brondata, berekende indicaties, aannames en openstaande verificatiepunten **niet zonder onderscheid** over als vaststaande feiten. Gebruik officiële bronnen en reproduceerbare berekeningen voor harde claims, en label de creatieve en economische aanbevelingen als hypotheses. Waar de actuele of officiële casebrief afwijkt, heeft de casebrief voorrang.
