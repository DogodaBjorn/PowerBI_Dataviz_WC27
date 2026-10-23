# Deep dive 3: the ceiling for the $50k paid plan

Researched 2026-10-23. Every number below has a URL that was opened and checked with WebFetch on that date. Anything not checked is marked "unverified".

## Answer first
1. Raw iOS pool: about 22.0M women aged 40-54 on iPhone across UK, US, NL, DK, SE, NO and FI (US 16.9M, UK 3.1M, Northern Europe 1.9M). $50k at a $12 to $30 CPM buys 1.7M to 4.2M impressions, which is 0.56M to 1.39M people at frequency 3. That is 2.5% to 6.3% of the pool.
2. The total pool is not the ceiling. The small markets are: at $20 CPM, frequency 3 on 100% of the iOS pool costs about $10k in Finland, $19k in Norway, $21k in Denmark, and $32k each in the Netherlands and Sweden. Northern Europe saturates inside the $50k. The US ($1.0M) and UK ($189k) do not.
3. The real ceiling is the in-market slice (women who recognise perimenopause and want help), creative fatigue and frequency, not the census. No open source sizes that slice, so we have to measure it from the first 500. If 10% of the pool is in-market (an assumption, not data), the UK slice saturates at about $19k and the Northern Europe slice at about $11k.

## 1. Women aged 40-54 per market
We use 40-54 because every source publishes 5-year bands (40-44, 45-49, 50-54). 40-55 inclusive would add roughly one more single-year cohort, about +7%.

| Market | 40-44 | 45-49 | 50-54 | Total 40-54 | Year | Source (open) |
|---|---|---|---|---|---|---|
| UK | 2,363,855 | 2,140,231 | 2,211,381 | 6,715,467 | mid-2025 | ONS mid-year estimates via Nomis API: https://www.nomisweb.co.uk/api/v01/dataset/NM_2002_1.data.csv?geography=2092957697&date=latest&gender=2&c_age=10,11,12&measures=20100&select=date_name,geography_name,gender_name,c_age_name,obs_value (dataset page: https://www.nomisweb.co.uk/datasets/pestsyoala) |
| US | 11,115,417 | 10,164,244 | 10,293,667 | 31,573,328 | 1 July 2024 | US Census Bureau Vintage 2024, single year of age, SEX=2 (female), ages 40-54 summed by us: https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/national/asrh/nc-est2024-agesex-res.csv ; field key (2 = Female): https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2024/NC-EST2024-AGESEX-RES.pdf |
| Netherlands | 536,712 | 530,016 | 625,347 | 1,692,075 | 1 Jan 2024 | Eurostat demo_pjangroup (see URL below) |
| Denmark | 169,443 | 189,003 | 195,716 | 554,162 | 1 Jan 2024 | Eurostat demo_pjangroup |
| Sweden | 319,679 | 316,405 | 326,231 | 962,315 | 1 Jan 2024 | Eurostat demo_pjangroup |
| Norway | 177,417 | 175,099 | 186,706 | 539,222 | 1 Jan 2024 | Eurostat demo_pjangroup |
| Finland | 177,751 | 169,327 | 155,810 | 502,888 | 1 Jan 2024 | Eurostat demo_pjangroup |
| Ireland (optional) | 223,535 | 199,130 | 182,724 | 605,389 | 1 Jan 2024 | Eurostat demo_pjangroup |
| Germany (optional) | 2,674,408 | 2,445,662 | 2,786,185 | 7,906,255 | 1 Jan 2024 | Eurostat demo_pjangroup |

Eurostat URL (JSON, opens without login): https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_pjangroup?format=JSON&sex=F&age=Y40-44&age=Y45-49&age=Y50-54&geo=NL&geo=DK&geo=SE&geo=NO&geo=FI&geo=DE&geo=IE&time=2024&unit=NR . Table view for humans: https://ec.europa.eu/eurostat/databrowser/view/demo_pjangroup/default/table

Scope used: "Northern Europe" = NL, DK, SE, NO, FI (core). IE and DE are shown but kept out of the core total.

## 2. iOS share of mobile OS (StatCounter, September 2026)
This is traffic share (page views from iOS devices), not the share of people who own an iPhone. It is a proxy.

| Market | iOS | Android | URL |
|---|---|---|---|
| UK | 46.88% | 53.11% | https://gs.statcounter.com/os-market-share/mobile/united-kingdom |
| US | 53.59% | 46.39% | https://gs.statcounter.com/os-market-share/mobile/united-states-of-america |
| Netherlands | 31.82% | 68.16% | https://gs.statcounter.com/os-market-share/mobile/netherlands |
| Denmark | 62.70% | 37.29% | https://gs.statcounter.com/os-market-share/mobile/denmark |
| Sweden | 56.12% | 43.88% | https://gs.statcounter.com/os-market-share/mobile/sweden |
| Norway | 58.69% | 41.30% | https://gs.statcounter.com/os-market-share/mobile/norway |
| Finland | 32.49% | 67.48% | https://gs.statcounter.com/os-market-share/mobile/finland |
| Ireland | 47.37% | 52.62% | https://gs.statcounter.com/os-market-share/mobile/ireland |
| Germany | 27.63% | 72.37% | https://gs.statcounter.com/os-market-share/mobile/germany |

iPhone share among women or among the 40-55 age group: no open, current source found. Statista has UK iPhone ownership by age, but it is paywalled (https://de.statista.com/forecasts/1284304/iphone-user-share-in-the-united-kingdom-by-age), so not used. Old claims that women skew to iPhone (AdMob, around 2010) are too old to use. We apply the all-adult StatCounter share. Direction of error: unverified.

## 3. Addressable iOS pool (women 40-54 x iOS share)

| Market | Women 40-54 | x iOS share | = iOS pool |
|---|---|---|---|
| US | 31,573,328 | 53.59% | 16,920,146 |
| UK | 6,715,467 | 46.88% | 3,148,211 |
| Netherlands | 1,692,075 | 31.82% | 538,418 |
| Sweden | 962,315 | 56.12% | 540,051 |
| Denmark | 554,162 | 62.70% | 347,460 |
| Norway | 539,222 | 58.69% | 316,469 |
| Finland | 502,888 | 32.49% | 163,388 |
| **Northern Europe core (NL, DK, SE, NO, FI)** | 4,250,662 | | **1,905,787** |
| **Core total (UK + US + N. Europe)** | 42,539,457 | | **21,974,144** |
| Ireland (optional) | 605,389 | 47.37% | 286,773 |
| Germany (optional) | 7,906,255 | 27.63% | 2,184,498 |
| Extended total (core + IE + DE) | | | 24,445,415 |

The pool counts people, not reachable Meta users. Meta's audience size for women 40-54 on iOS per country was not checked (it needs an ad account, through the Meta Ads Manager reach estimate). Unverified.

## 4. CPM benchmarks

### Meta (Facebook and Instagram), all industries, by country
Source: Superads Facebook Ads benchmarks. Median-based, more than $3B in spend, directional. The page header says Oct 2025 to Sep 2026, while the body text describes a July 2025 to July 2026 window. Currency is shown as "$" but not stated.

| Market | Window average CPM | Latest month in text | URL |
|---|---|---|---|
| Global | $20.59 | $16.47 (Jul 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille |
| US | $23.42 | $20.24 (Jul 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/united-states |
| UK | about $17.38 | $18.39 (Jul 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/united-kingdom |
| Netherlands | about $14.2 | $29.5 (Jul 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/netherlands |
| Denmark | $16.02 | $34.03 (May 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/denmark |
| Sweden | about $13.48 | about $12.50 | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/sweden |
| Norway | about $11.1 | $6.85 (Jul 2026) | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/norway |
| Finland | not checked | | unverified |

The Nordic monthly figures swing hard (Norway $6.85 to $17.7, NL up to $29.5), which points to small samples. Use the averages, not single months.

### Meta, health-specific (no country split)
| Category | CPM | Period | Basis | URL |
|---|---|---|---|---|
| Healthcare (Superads) | about $30.3 average, peak $42.53 (Apr 2026), low $8.04 (Jul 2026) | Jul 2025 to Jul 2026 | Superads accounts, global, above the global baseline in 12 of 13 months | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/healthcare |
| Health & Wellness (Triple Whale, via Influee) | $20.70 (+38% YoY), vs $14.19 for the platform overall | Full year 2025 | about 35,000 accounts, mostly e-commerce, so not app-specific | https://influee.co/blog/facebook-ads-benchmarks |

Note: the Superads country filter does not work on the healthcare page (the UK and US URLs show "all countries"), so there is no health x country CPM.

### Other channels (directional, not health app or country-specific unless stated)
| Channel | CPM | Period | URL |
|---|---|---|---|
| TikTok, Tier 1 (US, UK, CA) | $10 to $15 | 2026 (TikAdSuite, cited) | https://influee.co/blog/tiktok-cpm |
| TikTok, Health & Fitness | $6.50 | 2026 (TikAdSuite, cited) | https://influee.co/blog/tiktok-cpm |
| TikTok, in-feed conversion | $9.16 | 2026 (DigitalApplied, cited) | https://influee.co/blog/tiktok-cpm |
| YouTube / Google | no open US/UK source checked | | unverified |

### CPM for women 45+
No current, open source found that gives Meta CPM by age x gender. The only findings were a 2014 Nanigans study (via MarketingCharts, which returned 403 so we could not check it) and a blog claim that women's CPM is $6.01 vs $4.92 for men (unverified, the original source was not found). Practitioners widely expect higher CPMs for women 45+, but that is unverified here. Measure it in the first test (Ads Manager breakdown by age and gender).

## 5. What $50k buys, and where saturation starts

Scenario CPMs, chosen from the tables above:
- Low $12: Nordic all-industry averages ($11 to $14)
- Mid $20: global all-industry average ($20.59) and Health & Wellness 2025 ($20.70)
- High $30: Healthcare average ($30.3), above the US all-industry average ($23.42)

| CPM | Impressions ($50,000 / CPM x 1,000) | Reach at frequency 3 (impressions / 3) | Share of core iOS pool (21,974,144) |
|---|---|---|---|
| $12 | 4,166,667 | 1,388,889 | 6.3% |
| $20 | 2,500,000 | 833,333 | 3.8% |
| $30 | 1,666,667 | 555,556 | 2.5% |

Spend needed to reach 100% of each market's iOS pool at frequency 3 (pool x 3 / 1,000 x CPM):

| Market | iOS pool | At local avg CPM | At $20 | At $30 | Saturates within $50k? |
|---|---|---|---|---|---|
| US | 16,920,146 | $1,188,809 (at $23.42) | $1,015,209 | $1,522,813 | No |
| UK | 3,148,211 | $164,148 (at $17.38) | $188,893 | $283,339 | No, but only 3.3x headroom |
| Netherlands | 538,418 | $22,937 (at $14.2) | $32,305 | $48,458 | Yes |
| Sweden | 540,051 | $21,840 (at $13.48) | $32,403 | $48,605 | Yes |
| Denmark | 347,460 | $16,699 (at $16.02) | $20,848 | $31,271 | Yes |
| Norway | 316,469 | $10,538 (at $11.1) | $18,988 | $28,482 | Yes |
| Finland | 163,388 | n/a | $9,803 | $14,705 | Yes |
| N. Europe core | 1,905,787 | | $114,347 | $171,521 | Yes, per country |

The census pool is the upper bound. Saturation shows up sooner, from four sources:
1. **In-market slice.** The brief targets women who recognise perimenopause, not those in denial. No open source sizes this. Illustrative only (an assumption, not data): if 10% of the pool is in-market, the slices are US 1.69M, UK 315k and Northern Europe 191k. At $20 CPM and frequency 3, those saturate at about $101k, $19k and $11k. Northern Europe and the UK would then hit their ceiling inside $50k.
2. **Meta reachable audience is smaller than the population**, and there is ATT signal loss on iOS. Unverified; check with Ads Manager reach estimates.
3. **Frequency and creative.** Once frequency passes about 3 per week in a small market, CPM and CPA rise. This is a practitioner rule of thumb, not sourced here (unverified).
4. **Seasonality.** CPMs rise into Q4. Global Superads median CPM is $16.47 in Jul 2026 against a $20.59 average, and the healthcare series shows the same kind of swings. A plan that starts in Nov/Dec (public release is about 4 to 6 weeks from mid-October) pays peak CPMs.

Implication for the plan: put the Nordic countries on fixed caps (roughly $5k to $10k each, where frequency climbs fast) and use the US and UK as the scale markets. Treat the in-market share as the number to measure on the first 500, for example the share of reached women who complete onboarding per 1,000 reached, by country.

## Caveats
- StatCounter = share of web traffic, not device ownership or ownership by gender/age.
- Population years differ: US 2024, Eurostat 1 Jan 2024, UK mid-2025.
- Superads: dates in header and text conflict, currency not stated, Nordic samples look small and volatile. Healthcare is a broad category (clinics, pharma, services), not health apps.
- Triple Whale and Influee figures are mostly e-commerce, not app installs.
- No health app x country x age CPM source exists in the open; the CPM scenarios are a range, not a forecast.
- The Meta Ads MCP benchmark tool (ads_insights_industry_benchmark) was not used. It needs an ad account with spend, which AxisX does not have.
