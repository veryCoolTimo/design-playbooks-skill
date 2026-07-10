---
name: coinbase
kind: site
style: ML
category: crypto-exchange
website: null
pages: [home, explore, wealth, pricing, developer-platform]
palette:
  canvas: "#ffffff"
  ink: "#5b616e"
  primary: "#0052ff"
  accents: ["#0a0b0d", "#eef0f3", "#05b169", "#cf202f", "#f4b000"]
typography:
  display: "Coinbase Display (sub: Inter) · light-feeling weight 400 · tight negative tracking (-1 to -2px)"
  body: "Coinbase Sans (sub: Inter); Coinbase Mono for all numbers"
radius: "pill (100px) on buttons; large 24px on cards"
---
## Overview
A crypto exchange styled like a restrained financial-services house: white canvas, near-black ink, and one blue used sparingly. Headlines run at regular weight rather than bold, which gives the whole system a calm, editorial tone instead of trading-app aggression. Sections alternate between white, soft gray, and full-bleed near-black bands.

## Layout
Slim 64px top nav (wordmark left, menu center, sign-in/sign-up pills right) that inverts to white-on-dark over dark heroes. Signature hero: full-bleed #0a0b0d band, 80px weight-400 headline on the left, and 2-3 layered product-UI mockup cards floating at slight rotation on the right. Content caps at ~1200px on a 12-column grid; feature grids run 2-up or 3-up; every major band gets 96px vertical padding. A dark CTA band precedes a white 6-column footer.

## Components
Buttons are always pills: blue #0052ff primary (44px tall, 56px for hero CTAs), soft-gray #eef0f3 secondary, dark-elevated or white-outline variants on dark bands; press state darkens blue to #003ecc. Cards use 24px radius with 32px padding, either flat or with a 1px #dee1e6 hairline; only one shadow tier exists (a faint 4/12 blur on hover). Text inputs are 48px with 12px radius, gaining a 2px blue border on focus; search fields are gray pills. Asset rows pair 32px circular icon plates with mono-font prices and green/red change text.

## Signature
- Weight-400 display headlines with tight negative tracking — the calm-institution voice.
- One blue (#0052ff) doing all action work, rationed to a couple of moments per band.
- Dark #0a0b0d hero bands carrying stacked, slightly-rotated product-UI mockup cards.
- Pill everything interactive, 24px-radius everything containing, circle everything iconic.

## Do / Don't
**Do**
- Keep #0052ff exclusive to primary CTAs, the wordmark, and inline brand links.
- Set headlines in the display face at weight 400 with -1px to -2px tracking.
- Alternate white, soft-gray, and dark bands to build page rhythm.
- Render every price and percentage in the mono face; color change values green #05b169 / red #cf202f as text only.
- Mark the featured pricing tier by inverting it to the dark palette, not with ribbons or color.

**Don't**
- Don't add a second action color or use trading green/red as button fills.
- Don't bold display copy — heavy headlines break the brand voice.
- Don't square off CTAs; pills are non-negotiable.
- Don't stack shadow tiers — depth comes from card-on-card layering, not elevation.
- Don't mix the display and body families within one headline.
