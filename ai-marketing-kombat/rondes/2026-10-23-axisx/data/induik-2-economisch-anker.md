# Deep dive 2: Economic anchor (free-to-paid conversion, Health & Fitness)

Researched 23 Oct 2026. Every number below was read on the open source page via WebFetch unless marked "unverified". FX: 1 GBP = 1.32 USD (same rate as cijfers-helder.md, currency-converter.org.uk, 4 Oct 2026).

## Answer first
1. Anchor: Health & Fitness apps convert a median **2.9% of downloads to paid within 35 days** (top quartile above 6.2%); freemium apps across all categories only 2.1%, hard paywall apps 10.7%. Source: RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps
2. At £100/year minus Apple's 15%, a completed onboarding is worth **£1.79 to £5.27 (USD 2.36 to 6.96)** in year-1 revenue at 2.1% to 6.2% conversion, mid case £2.47 (USD 3.25). Adding one annual renewal at 44.1% raises the mid case to £3.55 (USD 4.69).
3. A woman who completes onboarding is a better prospect than a raw download, but on public benchmarks the "1 in 10 pays" in cijfers-helder.md is top-of-market (hard paywall level), not a base case. Paying Meta USD 7.70 to 20.70 per onboarded woman breaks even only at 4.8% to 12.8% conversion with one renewal included.

## Benchmarks table

| # | Metric | Value | Segment | Year (data) | Exact quote on page | URL | Status |
|---|---|---|---|---|---|---|---|
| 1 | Download-to-paid, D35 | median 2.9%, top quartile >6.2% | Health & Fitness | Report 2026 (2025 data) | "Health & Fitness median: 2.9% (top quartile above 6.2%)." | https://www.revenuecat.com/state-of-subscription-apps | Verified |
| 2 | Download-to-paid, D35 | median 2.0% | All categories, global | Report 2026 | "Globally, median lands at 2.0%." | https://www.revenuecat.com/state-of-subscription-apps | Verified |
| 3 | Download-to-paid, freemium vs hard paywall | 2.1% freemium vs 10.7% hard paywall | All categories | Report 2026 | "Apps that ask for money upfront convert 5x better than freemium (10.7% vs. 2.1%)." | https://www.revenuecat.com/state-of-subscription-apps | Verified |
| 4 | Download-to-trial, D30 | 6.9%; top performers >23% | Health & Fitness | Report 2026 | "Health & Fitness (6.9%)"; "Health & Fitness top performers convert over 23%." | https://www.revenuecat.com/state-of-subscription-apps | Verified |
| 5 | Trial-to-paid | median 37.7%, top quartile >51.4% | Health & Fitness | Report 2026 | "Health & Fitness median: 37.7% (top quartile above 51.4%)." | https://www.revenuecat.com/state-of-subscription-apps | Verified |
| 6 | Trial-to-paid | median 39.9%, top 10% 68.3% | Health & Fitness | Report 2025 (2024 data) | "While Health & Fitness apps have a median of 39.9%, the top 10% convert at 68.3%" | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 7 | Download-to-paid, D35 | P90 12.1% | Health & Fitness | Report 2025 | "Health & Fitness is hitting 12.1% at P90" | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 8 | Download-to-paid, D35, freemium vs hard paywall | 2.18% vs 12.11% | All categories | Report 2025 | "we see 12.11% median conversion versus just 2.18% for freemium" | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 9 | 12-month retention, yearly plans | 44.1% (was 47.1%) | All categories | Report 2025 | "retention has slightly declined from 47.1% in the previous period to 44.1% in this period" | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 10 | 12-month retention, yearly plans, upper quartile | 60-75% | All categories | Report 2025 | "the upper quartile retain 60-75% on yearly plans" | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 11 | Refund rate | 4.71% | Health & Fitness | Report 2025 | "Education and health & fitness apps have the highest refund rates, at 4.86% and 4.71% respectively." | https://www.revenuecat.com/state-of-subscription-apps-2025/ | Verified |
| 12 | Trial-to-paid | 35.0% | Health & Fitness | Adapty report 2026 | "Health & Fitness leads trial-to-paid at 35.0%" | https://adapty.io/state-of-in-app-subscriptions/ | Verified |
| 13 | Install-to-trial / trial-to-paid, global average | 10.9% / 25.6% | All categories | Adapty report 2026 | "For trial funnels, the global average is 10.9% install-to-trial and 25.6% trial-to-paid." | https://adapty.io/state-of-in-app-subscriptions/ | Verified |
| 14 | First-renewal retention | 30.3% (lowest category; plan type not stated) | Health & Fitness | Adapty report 2026 | "Utilities leads with 58.1% first-renewal retention while Health & Fitness is last at 30.3%." | https://adapty.io/state-of-in-app-subscriptions/ | Verified, but plan type unclear |
| 15 | Install-to-trial / trial-to-paid / first renewal | 9.5% / 42.2% / 67.7% | Health & Fitness, WEEKLY plans with trial | Adapty blog, 27 Mar 2026 | funnel chart figures | https://adapty.io/blog/health-fitness-app-subscription-benchmarks/ | Verified, weekly plans only, not comparable to annual |
| 16 | Paid share of active users (stock ratio, not a conversion rate) | ~5M paid / ~70M MAU = ~7.1% | Flo (women's health) | June 2024 | "serves nearly 70 million monthly active users and close to 5 million paid subscribers." | https://hlth.com/insights/news/flo-health-achieves-unicorn-status-with-200-million-series-c-funding-2024-07-31 | Verified |
| 17 | Flo 7% conversion, 77M MAU (2026) | 7% | Flo | 2026 | third-party Notion teardown | (Notion page, not a primary source) | Unverified, not used |
| 18 | Menopause apps (Balance, Peppy, Midday, Stella, Clue) conversion | none found | Menopause / femtech | n/a | no public conversion figures found | n/a | Not available |

Metric definitions, so nobody mixes them:
- Download-to-trial: share of installs that start a free trial (RevenueCat D30).
- Trial-to-paid: share of started trials that become a paid subscription. Only applies to the trial path.
- Download-to-paid (D35): share of ALL installs that pay within 35 days, any path. This is the one closest to our question.
- Freemium free-to-paid: download-to-paid for apps without an upfront paywall (row 3 and 8). AxisX beta is free, so this is the closest structural match.

## Break-even calc

Question: what may one completed onboarding cost, if a share c of onboarded women later pay £100/year?

Formula: break-even cost per completed onboarding = net revenue per payer x c.

Assumptions:
- Price £100/year, annual plan only.
- Apple fee 15% (App Store Small Business Program, under USD 1M revenue). Net £85 per payer per year. At 30% fee net would be £70.
- Base case counts year 1 only. Renewal case adds one renewal at 44.1% (row 9, all categories). Sensitivity: 30.3% (row 14).
- c is taken from download-to-paid benchmarks and applied to completed onboardings (see caveats: this is conservative).
- Low 2.1% (freemium, row 3), mid 2.9% (H&F median, row 1), high 6.2% (H&F top quartile, row 1), stretch 10.7% (hard paywall, row 3).
- FX 1 GBP = 1.32 USD.

| Case | c | Gross £100 x c | Net £85 x c (year 1) | Net in USD | Net + 1 renewal at 44.1%: £85 x 1.441 x c | in USD | Net + 1 renewal at 30.3% |
|---|---|---|---|---|---|---|---|
| Low | 2.1% | £2.10 | £1.79 | $2.36 | £2.57 | $3.40 | £2.33 |
| Mid | 2.9% | £2.90 | £2.47 | $3.25 | £3.55 | $4.69 | £3.21 |
| High | 6.2% | £6.20 | £5.27 | $6.96 | £7.59 | $10.02 | £6.87 |
| Stretch | 10.7% | £10.70 | £9.10 | $12.01 | £13.11 | $17.30 | £11.85 |

Worked example (mid): £85 x 0.029 = £2.465, x 1.32 = $3.25. With renewal: £85 x 1.441 = £122.49 per payer over two years, x 0.029 = £3.55, x 1.32 = $4.69.

UK VAT variant: if £100 is the consumer price including 20% VAT, Apple proceeds are £100 / 1.2 x 0.85 = £70.83. Mid case then becomes £70.83 x 0.029 = £2.05.

Reverse check against cijfers-helder.md (Meta USD 7.70 to 20.70 per onboarded woman):
- Year 1 net per payer = £85 x 1.32 = $112.20. Needed conversion = 7.70 / 112.20 = 6.9% up to 20.70 / 112.20 = 18.4%.
- With one renewal at 44.1%: $161.68 per payer. Needed conversion = 7.70 / 161.68 = 4.8% up to 20.70 / 161.68 = 12.8%.
- So cheap Meta onboardings (around $8) need top-quartile H&F conversion; expensive ones ($20) need better than hard paywall medians.

## Caveats
- Denominator mismatch. Benchmarks are per download; our KPI is per completed onboarding. Onboarding completers are a filtered, more motivated group, so their conversion should be higher than download-to-paid. No public benchmark gives conversion per completed onboarding. Measure it on the first 500 (founding price "yes" rate as proxy, then real payment at launch).
- Paywall model matters more than category. Hard paywall converts about 5x freemium (10.7% vs 2.1%), yet RevenueCat 2026 says after one year retention is nearly identical. AxisX's beta is free; the paid model at launch decides which row applies.
- Time window. D35 means payment within 35 days of install. Free beta users who get asked to pay months later are a different situation, with no public benchmark.
- Retention row 9 (44.1%) is all categories, not Health & Fitness. Adapty's H&F first-renewal 30.3% is lower and its plan type is not stated, so treat 30% to 44% as the realistic band for a year-1 renewal.
- Plan mix conflict on the RevenueCat 2026 page itself: "Health & Fitness captures 68% from annual plans" versus "Health & Fitness is monthly-heavy (68%)". Do not cite either as a plan-mix fact.
- Flo's ~7% (5M paid of 70M MAU) is a stock ratio of active users, from a 15+ year mass-market app. It is not a conversion rate and not menopause-specific. No public conversion data exists for Balance, Peppy, Midday, Stella or Clue.
- Refund rate H&F 4.71% (2025) would trim net revenue slightly; not included in the table.
- Rejected as anchor: secondary write-ups (athletechnews, saastr, rocketshiphq, voxbooster, Notion teardown) and any number not visible on the RevenueCat, Adapty or HLTH page. Adapty's 4.2% H&F download-to-paid seen in a search summary could not be found on an open page: unverified, not used.
- Fierce Healthcare and MobiHealthNews returned 403; Flo figures verified via HLTH instead.
