# Incrementality and MMM

Core question: how many conversions would NOT have happened without the ads? Attribution cannot answer this; experiments and MMM can.
Incremental = test group result - what the control group would have done anyway.

## 1. Methods overview

| Method | What it does | When to use | Needs | Weakness |
|---|---|---|---|---|
| Conversion lift (platform user-level RCT) | Randomly withholds ads from a control (or uses ghost ads/PSA); measures incremental conversions | Single platform, enough volume, want causal CPA/iROAS | Platform tool (Meta Conversion Lift, Google Conversion Lift, TikTok lift), budget threshold [CHECK], signal (CAPI/MMP events) | Platform-run, one platform at a time, requires logged-in users; privacy limits |
| Geo experiment / GeoLift | Treat some regions, hold out others; synthetic control compares outcome | Cross-channel, offline outcomes, privacy-safe, no user IDs | 15-40 comparable geos, 4-8 weeks, geo-level outcome data | Spillover, few geos = low power, region events (holidays) |
| Holdout (own audience) | Withhold ads from a random slice of CRM/audience | Retargeting/CRM/lifecycle incrementality | A reliable random split, own data | Contamination via other channels |
| On/off or budget pulse test | Pause or change spend, compare to baseline | Quick sanity check when nothing else | Stable baseline | Confounded by seasonality; low rigor |
| PSA / ghost ads | Control sees a neutral ad | Auction-level cleanliness | Platform support | Complexity |
| MMM (marketing mix modelling) | Regression on aggregate time series (spend by channel, price, seasonality, promos, macro) -> contribution, saturation, adstock, ROI curve | Annual/quarterly budget split across channels incl. offline; long-run effects | 2-3 years weekly (or daily) data, spend variation, many channels | Correlational; needs calibration with experiments; slow |

## 2. Tools

| Tool | Owner | Notes |
|---|---|---|
| Meridian | Google, open source | Bayesian MMM; supports geo-level hierarchical models; ROI priors can be set from experiments; reach & frequency inputs; [CHECK] current release and availability |
| Robyn | Meta, open source (R, also Python) | Ridge regression + evolutionary hyperparameter optimization (Nevergrad), calibration with lift tests, Pareto-optimal models |
| GeoLift | Meta, open source (R) | Synthetic control for geo experiments; power analysis and market selection helpers |
| CausalImpact | Google (R) | Bayesian structural time-series for intervention analysis |
| PyMC-Marketing | PyMC Labs | Bayesian MMM in Python |
| Platform lift tools | Meta / Google / TikTok | Conversion Lift, Brand Lift, Search Lift, YouTube |

[CHECK] versions and features as of 2026; these tools evolve quickly.

## 3. Which to use when

| Situation | Choose |
|---|---|
| "Does Meta actually drive installs/rides, or just claim them?" | Conversion lift on Meta, or geo-lift if you can split by city |
| "How should $600k be split across Meta / TikTok / Google?" | MMM if you have history; otherwise a staged geo/budget split test + calibration with attribution |
| New market, no history, 2-week horizon (like a case round) | Launch a structured split with holdout / staggered budget; rely on equal-budget tests per channel and compare CPA of the business event on a deduplicated source |
| Brand awareness effect | Brand lift survey or share-of-search tracking |
| Retargeting effectiveness | Holdout test on the retargeting audience |
| Offline/TV or non-clickable | Geo-lift or MMM |
| Daily optimization | Platform attribution + MER guardrails |

## 4. Triangulation

Three lenses, none perfect:
- Attribution (MMP / platform): fast, granular, biased upward.
- Experiments (lift, geo): causal, narrow, expensive, snapshot.
- MMM: holistic, long run, model-dependent.
Workflow: MMM sets the allocation -> experiments test the biggest assumptions -> attribution runs daily optimization, with calibration factors (incrementality factor = lift-measured conversions / platform-reported conversions).
Compare: if lift says 60% of reported conversions are incremental, scale the platform's CPA by 1/0.6 for budget decisions.

Calibration example: Meta reports CPA $10; lift test shows incremental CPA $18; Google reports $15, incremental $17. Decision based on incremental CPA: Google is cheaper per extra conversion, though Meta looks cheaper in reports.

## 5. Quick design tips

- Conversion lift: need roughly hundreds of incremental conversions [CHECK platform minimums]; run 2-4 weeks; keep other variables stable; pre-register the metric.
- Geo test: match geos on pre-period trend; run 4-8 weeks; hold-out at least 10-20% of the volume; avoid markets with known events; analyze with synthetic control or diff-in-diff; report a confidence interval.
- MMM: weekly data, 2+ years, include price, promo, seasonality, competitor/macro control; use adstock (carryover) and saturation (diminishing returns) curves; report ROI intervals, not a point.
- Always state the minimum detectable effect before the test.

## 6. Explain it to a jury in 3 lines

1. "Attribution tells us who got the credit; incrementality tells us who made the sale happen. We use lift or geo tests to measure real incremental CPA."
2. "MMM then turns those results into a budget split with diminishing-returns curves, so the next dollar goes where the marginal return is highest."
3. "In this round we split budget evenly at first, apply scale/stop rules on deduplicated first-ride CPA, and reserve test budget for a holdout that calibrates the platform numbers."

## 7. Pitfalls

- Treating platform lift as independent of the platform's interests; check design and p-value.
- Underpowered test and reading "no effect" as "zero effect".
- Running a lift test during a promo spike.
- MMM with spend that never varied (no signal) or with collinear channels (all scale together).
- Reporting iROAS without the interval.
- Using last-click CPA as the incremental CPA.
