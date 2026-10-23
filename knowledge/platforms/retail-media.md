# Retail Media (Amazon Ads and other retail media networks)

Status: reference for 2-hour case rounds. Written 2026-10-23. [CHECK] = verify before relying on it. The case's own numbers beat everything below.

## 1. What it is good for
- Funnel role: bottom-funnel capture at the point of purchase, plus upper-funnel reach using retailer first-party shopper data (Amazon DSP, Walmart Connect, etc.).
- Intent: very high (shoppers searching or browsing inside a marketplace/retailer). Closed-loop sales attribution on the retailer's own transactions.
- Audience: shoppers on the retailer (Amazon, Walmart, Target, Instacart, Zalando, bol.com, Mercado Libre, Jumia, Noon, Flipkart, Shopee/Lazada, etc.). Demographics follow the retailer's customer base.
- Best for: CPG/FMCG, consumer electronics, beauty, household, books/media, private-label sellers, brands with marketplace listings, launches needing ranking velocity.
- Weak for: brands without retail distribution, services, apps, B2B, categories that do not sell via the retailer. Not relevant to app-install or ride-hailing cases unless the case says so.

## 2. Campaign structure & objectives (Amazon first, then others)
- Amazon Ads sponsored formats (self-serve, CPC):
  - Sponsored Products (SP): product ads in search results and on product pages; keyword (broad/phrase/exact), product targeting (ASIN), auto targeting (close match, loose match, substitutes, complements).
  - Sponsored Brands (SB): headline banner with logo + multiple products, video, store spotlight; top-of-search placement; requires Brand Registry [CHECK].
  - Sponsored Display (SD): audience and product targeting on and off Amazon; retargeting.
  - Sponsored TV [CHECK]: self-serve streaming TV in Amazon Ads console.
- Amazon DSP: programmatic display, video, audio, Prime Video/Streaming TV ads, Twitch, third-party supply; uses Amazon shopper signals (in-market, lifestyle, remarketing, lookalikes).
- Amazon Marketing Cloud (AMC): clean-room analytics for path to purchase, custom audiences.
- Amazon Attribution: measure non-Amazon traffic (Meta, Google, email) that converts on Amazon.
- Brand tools: Stores, A+ Content, Posts, Live, Brand Analytics, Brand Referral Bonus (earn % on off-Amazon traffic) [CHECK].
- AI-assisted: Rufus (shopping assistant) and sponsored prompts / ads in conversational shopping surface [CHECK status].
- Recommended structure (SP):
  - Auto campaign (discovery) > harvest converting search terms into exact/phrase manual campaigns > add negative exact in auto/broad to avoid overlap.
  - Separate campaigns for brand, competitor, category/generic, product targeting.
  - Group by product themes; avoid hundreds of micro-campaigns.
- Other networks: Walmart Connect (sponsored search/display/on-site/off-site), Instacart Ads, Target Roundel, Kroger Precision Marketing, Criteo Retail Media (retail-agnostic), Zalando ZMS, bol.com Advertising (Netherlands), Albert Heijn/Ahold Delhaize retail media [CHECK], Mercado Ads (LatAm), Jumia/Noon/Flipkart/Shopee/Lazada ad products, TikTok Shop (GMV Max).

## 3. Bidding & budget
- Amazon SP/SB/SD bidding: Dynamic bids - down only, up and down, fixed; placement modifiers (top of search first page, rest of search, product pages). Manual CPC bids per keyword/target; auto-bidding rules via Ads console.
- Budget: daily budget per campaign; budget rules for events (Prime Day, Q4). Rule of thumb: budget >= ~10x target CPC and enough clicks/day to get data (30-50 clicks to judge a keyword) [rule of thumb].
- Key metrics: ACOS (ad spend / ad sales), ROAS (sales / spend), TACoS (ad spend / total sales, including organic), CPC, CVR, CTR, detail page views, new-to-brand orders.
- Target ACOS = gross margin or breakeven ACOS; set bids by max CPC = AOV x CVR x target ACOS.
- Scale: raise bids/budgets on exact winners; expand keyword harvest; watch TACoS (healthy ads lift organic rank, TACoS falls over time).
- Seasonality: raise budget ahead of peak events; inventory in stock matters (ads pause or waste when out of stock).

## 4. Targeting & signals
- Keywords (customer search terms), ASIN/product targeting, category targeting, interests/audiences (DSP/SD), Amazon shopper segments, remarketing (viewed detail pages, ASIN purchasers), lookalikes.
- Negative keywords/ASINs to control waste; search term reports are the key optimisation source.
- First-party: brand CRM lists via AMC/DSP; Amazon Attribution tags.
- Listing signals matter more than targeting: relevance, price competitiveness, ratings/reviews, Buy Box ownership, delivery speed (Prime), stock, title/bullets/images/A+.

## 5. Creative: what wins
- Product detail page quality is the "landing page": strong title with keywords, 7+ images including lifestyle and infographic, video, A+ Content, price/deal badges, reviews 4+ stars.
- Sponsored Brands: custom headline (50 chars), brand logo, 3 products, lifestyle image; video ads (6-45 s, vertical or horizontal) with product demo in first 3 seconds [CHECK].
- Display/DSP: lifestyle + product; benefit-led copy; mobile-first formats.
- Test hero image (main image) for CTR; white-background compliance for main image.
- Coupons, Lightning Deals, Subscribe & Save badges boost CVR.

## 6. Ad specs cheat sheet (Amazon)
| Item | Spec |
|---|---|
| SB headline | 50 chars max |
| SB logo | min 400x400 px |
| SB video | 6-45 s, min 1920x1080 or 1080x1920 (vertical) [CHECK] |
| SP | uses product listing creative (title, image, price, rating) |
| SD | image or product; custom creative min 600x600 [CHECK] |
| Product image | min 1000 px longest side (zoom), white background main image |
| Keywords | match types broad/phrase/exact; negative exact/phrase |
| DSP display sizes | 300x250, 728x90, 160x600, 320x50, 300x600, etc. |

## 7. Measurement & attribution
- Amazon SP attribution window 7 days (click) for on-Amazon sales; SB and SD 14 days; DSP configurable (14-day default) [CHECK].
- Attributed sales include same-brand halo (other products of the brand) in some reports; check "advertised SKU" vs "other SKU".
- New-to-brand metrics; detail page views; Brand Halo; Total ROAS (DSP).
- Incrementality: Amazon Brand Lift, Amazon Marketing Cloud analysis, pre/post and holdout tests; TACoS and organic rank movement.
- Closed-loop attribution is strong for on-retailer sales but ignores store/DTC halo; for multi-channel, use MMM or geo tests.
- Metrics to avoid in isolation: ACOS for brand keywords (low by default), CTR on branded terms.

## 8. DO's
1. Fix the listing first: price, stock, Buy Box, reviews, images, A+ Content.
2. Start with auto + broad, harvest into exact, add negatives.
3. Set targets from margin (breakeven ACOS) and AOV, not arbitrary ROAS.
4. Split brand, generic and competitor campaigns; evaluate each on its own role.
5. Use placement modifiers on Top of search for high-value terms.
6. Track TACoS and organic rank, not only ACOS.
7. Use Amazon Attribution for external traffic sources.
8. Use SB video and SBV for category discovery; DSP for remarketing and reach.
9. Plan inventory for ad-driven demand; pause when low stock.
10. Use Sponsored Display retargeting with exclusions for converters.

## 9. DON'Ts
1. Do not advertise products with poor reviews, no stock or uncompetitive price.
2. Do not run only auto campaigns forever.
3. Do not judge by ACOS only; account for organic lift and lifetime value.
4. Do not bid on brand terms without separating them in reports.
5. Do not scatter hundreds of low-budget campaigns.
6. Do not ignore negative keyword hygiene.
7. Do not compare Amazon ROAS directly with Meta/Google ROAS (different attribution windows and sales logic).
8. Do not forget off-Amazon halo (store/DTC) when judging brand impact.

## 10. Method of success (playbook)
1. Audit listing quality and stock; set margin-based target ACOS.
2. Launch auto + manual (broad/phrase) with moderate bids; SB headline and video for top products.
3. Learn 2-3 weeks; mine search term reports; move winners to exact; negate losers.
4. Optimise bids by placement and by keyword profit; test creative.
5. Scale: raise budgets for winners; add DSP remarketing and awareness; watch TACoS.
6. Refresh: seasonal creative, deal calendar, listing improvements.
7. Validate: AMC, lift studies, total sales trend.

## 11. KPI benchmarks (orders of magnitude; prefer the case's own benchmarks)
- Amazon SP CPC about $0.3-$2 (US, competitive categories $1-$3+; emerging markets lower); CTR ~0.3-0.6%; CVR ~5-15% (Amazon CVR is much higher than website CVR); ACOS commonly 15-40% depending on margin and category; TACoS often 8-15% for mature brands [CHECK]. Walmart/other RMNs usually lower competition and CPC but smaller scale.
- DSP CPM ~$5-$15 (varies; premium audiences higher); Prime Video/Streaming TV CPM higher (~$15-$30+) [CHECK].

## 12. AI features
- Amazon Ads AI: creative generator (image/video from product listing), Video Generator, Audio Generator, Creative Agent, AI-powered campaign suggestions, Performance+ type automation, Rufus conversational shopping ad surfaces [CHECK].
- Walmart Connect, Instacart and Criteo also provide auto-bidding/auto-targeting; policy usually requires truthful AI-generated creative [CHECK].

## 13. Common traps in a case/competition setting
- Using retail media where the case product is not sold through the retailer (e.g. app, service).
- Misreading ACOS: low ACOS on brand terms is not incremental.
- Ignoring that retailer-reported sales are last-touch and heavily attributed to the retailer's own traffic.
- Ignoring stock and listing quality in the recommendation.
- Not separating halo/new-to-brand from existing customer sales.
- Comparing ROAS across channels with different attribution windows (7/14-day on Amazon vs 7-day-click-1-day-view on Meta).
