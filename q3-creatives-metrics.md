# Q3 creatives: doorgerekend (21 okt 2026)

Bron: `nigeria-q3-creatives.csv`. CPI = spend/installs, IPM = installs per 1.000 impressies, eerste ritten = spend/CPA (afgeleid, niet in dataset).
Benchmarks (Appendix D): CPI Google 0,80 / Meta 1,20 / TikTok 1,50; IPM 1,5 / 3,0 / 0,5; CPA eerste rit overal $4,00.

| ID | Hypothese | Fmt | Kanaal | Spend | Installs | CPI | IPM | CPA | Ritten* | Oordeel |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| NG-01 | Split screen | Static | Google | 2356 | 6742 | 0.35 | 10.24 | 0.97 | 2429 | WINNAAR (33% van alle ritten) |
| NG-02 | Split screen | Motion 9:16 | Google | 467 | 721 | 0.65 | 1.50 | 1.70 | 274 | win |
| NG-03 | Split screen | Motion 1200x628 | Google | 521 | 284 | 1.83 | 0.12 | 8.44 | 62 | stop |
| NG-04 | Ride fails | UGC | TikTok | 2266 | 1283 | 1.77 | 0.25 | 4.22 | 537 | net boven target |
| NG-05 | Ride fails | UGC | TikTok | 3765 | 1242 | 3.03 | 0.43 | 7.32 | 514 | stop (grootste spend, 2x CPI-bench) |
| NG-06 | City Hustler (pcm) | Motion 1200x628 | Google | 782 | 976 | 0.80 | 0.30 | 2.14 | 365 | win |
| NG-07 | City Hustler (pcm) | Motion 9:16 | Google | 137 | 307 | 0.45 | 4.16 | 1.58 | 87 | win, klein volume: opschalen |
| NG-08 | City Hustler | Static | Meta | 444 | 291 | 1.53 | 3.62 | 42.05 | 11 | stop (CTR 6%, geen ritten) |
| NG-09 | Plans changed | AI video | TikTok | 1868 | 1154 | 1.62 | 1.52 | 20.22 | 92 | stop (klik-magneet, geen ritten) |
| NG-10 | Late night | AI video | TikTok | 1293 | 780 | 1.66 | 0.28 | 3.45 | 375 | win (beste TikTok) |
| NG-11 | Your choice | AI video | TikTok | 903 | 355 | 2.54 | 0.22 | 4.58 | 197 | net boven target |
| NG-12 | Family first | AI video | TikTok | 602 | 287 | 2.10 | 0.69 | 15.08 | 40 | stop |
| NG-13 | Rush hour | AI video | TikTok | 513 | 258 | 1.99 | 0.22 | 3.79 | 135 | win (krap) |
| NG-14 | Romantic | Static | Meta | 1649 | 838 | 1.97 | 1.41 | 3.86 | 427 | win (krap), CTR 11% |
| NG-15 | Special project | Motion | Meta | 627 | 476 | 0.49 | 0.61 | 0.49 | 1281 | ONMOGELIJK: 1281 ritten uit 476 installs. Niet gebruiken. |
| NG-16 | Rainy season | Motion 6 s | Google | 635 | 331 | 1.92 | 0.17 | 3.43 | 185 | win (krap) |
| NG-17 | Always on | Static 1:1 | Meta+Google | 498 | 380 | 1.31 | 4.12 | 19.64 | 25 | stop |
| NG-18 | Creator concept 2 | UGC 30 s | TikTok | 646 | 298 | 2.17 | 0.46 | 12.82 | 50 | stop |
| NG-19 | Creator concept 4 | UGC 33 s | TikTok | 1280 | 757 | 1.69 | 0.29 | 7.31 | 175 | stop |
| NG-20 | Creator concept 8 | UGC | TikTok | 2311 | 1085 | 2.13 | 0.27 | 81.01 | 29 | stop (2e grootste spend, slechtste CPA) |

*Ritten = spend/CPA, afgeleid. Totaal spend $23.563, afgeleide ritten 7.291 (excl. NG-15: 6.010), blended CPA $3,23 (excl. NG-15: $3,82).

## Patronen (ruwe eerste lezing, nog te checken op beeld)
1. Google motion/static met expliciet fare-moment (split screen, City Hustler) is de enige structurele winnaar: 5 van 6 Google-creatives onder $2,20 CPA. NG-03 (landscape 1200x628 motion) is de uitzondering.
2. Hoge CTR voorspelt niets: NG-08 (6,2%), NG-09 (4,1%), NG-14 (11,3%), NG-15 (11,8%) hebben de slechtste of onmogelijke CPA's. Beoordeel op CPA eerste rit.
3. TikTok UGC/creator-concepten (NG-04/05/18/19/20) kosten $10,3k = 44% van de spend en leveren 1.305 ritten tegen gemiddeld $7,87. Lange creator-video's (30 s+) zijn het slechtst.
4. Pidgin (NG-06/07) werkt: beide onder $2,20 en NG-07 heeft IPM 4,2 op Google (bench 1,5). Enige non-Engelse creatives.
5. Situationele AI-video's op TikTok (NG-10 late night, NG-13 rush hour) halen target; emotionele/familie-verhalen (NG-09, NG-12) niet.

## Loudbox MCP (`loudbox-demo`, read-only demo)
Tools: `describe_demo_data`, `query_demo_data(resource,input)`, `get_creative_preview(mediaAssetId|keyframeId)`.
Resources: `brands.list`, `creativeLibrary.list`, `creativeLibrary.detail`, `brandAssets.list`, `voiceOfCustomer.dashboard`.
- Workspace bevat de 20 NG-creatives (brandId inDrive `1de77255fe601a9d214156c1ba78e32b`); `creativeLibrary.detail` geeft `caseId` (NG-xx) terug.
- Concurrenten: Bolt (22 paid ads, boodschap "Pay up to 40% less for your first 3 rides", "Make your life easier"), Uber, Lagride (6 organic LinkedIn-posts). Bolt brandId `e079e20ff704b82df002e6237cdae010`.
- Voice of customer inDrive (App Store): passagiers waarderen zelf de prijs afspreken ("I enjoy the fact I get to negotiate price with the drivers"), klagen over prijsstijging Lekki-mainland en bestemmingsfouten; chauffeurs klagen over lage biedingen.
- Voice of customer Bolt: "quoted fares differ from what passengers are asked to pay" (bargaining na boeking, hogere prijs bij drop-off). Dat is precies het inDrive-voordeel: prijs vooraf afgesproken.
- Brand assets: inDrive modulaire set (dollar-bubbles, avatar met rating, prijs-slider) aanwezig.

## AI-fouten gevangen (bijhouden voor "how you worked")
- (nog leeg)
