---
name: binance
kind: site
style: DT
category: crypto-exchange
website: null
pages: [homepage, buy-crypto, deposit, markets, smart-money, futures-arena]
palette:
  canvas: "#0b0e11"
  ink: "#eaecef"
  primary: "#fcd535"
  accents: ["#f0b90b", "#0ecb81", "#f6465d", "#1e2329", "#2dbdb6"]
typography:
  display: "BinanceNova (Inter substitute) · bold 600-700 · tight negative tracking at large sizes"
  body: "BinanceNova (Inter substitute); BinancePlex / IBM Plex Sans for all numerals"
radius: "small-medium: buttons 6px, cards 8-12px, pill 9999px for top-tier CTAs"
---
## Overview
A near-black exchange interface where one yellow (#FCD535) shoulders the entire brand: every primary button, wordmark, giant stat number, and value-claim headline. Surfaces are flat color blocks — no shadows, no gradients — with depth read from the lightness step between canvas (#0b0e11) and card (#1e2329). Marketing pages run dark; buy/deposit flows flip to white while keeping the identical yellow CTA. Green (#0ecb81) and red (#f6465d) exist purely as price-direction text signals.

## Layout
64px flat top nav (yellow wordmark left, dense product menu, "Log In" text link plus yellow "Sign Up" button right). Homepage hero is a dark full-width band with a 64px/700 numeric headline and a card-style markets table in the right rail. Long-scroll pages stack bands at a uniform 80px vertical rhythm — denser than typical marketing sites, relying on color contrast rather than whitespace to separate sections. Content caps at ~1280px (marketing) to ~1440px (data tables); product views split 8/4 main-plus-rail. Every page, even dark ones, closes with a light #fafafa footer holding six link columns.

## Components
Primary button: yellow fill, black text, 14px/600 label, 6px radius, 40px tall; press state darkens to #f0b90b; a pill (9999px) variant is reserved for the single top-of-page action. Secondary buttons are #1e2329 blocks on dark or white with a 1px #eaecef border on light. Compact green/red 4px-radius buttons are Buy/Sell only. Cards: #1e2329 at 12px radius for containers (markets table, QR promo), 8px for smaller badges and light-mode transactional cards — shadowless, separated by hairlines (#2b3139 dark / #eaecef light). Inputs are 40px, 6-8px radius, hairline-bordered, with a blue (#3b82f6) focus ring. Table rows use hairline dividers, BinancePlex numerals, and direction-colored change cells with triangle arrows.

## Signature
- Black-on-yellow CTA rendered identically across dark and light modes — the one non-negotiable brand mark.
- Two-typeface split by function: BinanceNova for words, BinancePlex for every price, percentage, and stat counter.
- Huge yellow BinancePlex stat numbers ("316,258,026 USERS") doing hero duty on bare dark canvas, no card behind them.
- Light gray footer capping dark pages — an intentional inversion that closes the scroll.
- Green-up / red-down as text color only, never as surface fill.

## Do / Don't
**Do**
- Hold yellow to CTAs, brand-claim headlines, and stat callouts; its scarcity on dark is the whole identity.
- Set every numeral in the tabular face (BinancePlex or a Plex/mono substitute), even mid-paragraph.
- Keep displays at weight 600-700 with slight negative tracking; headlines must outshout dense data tables.
- Separate surfaces with hairlines and the canvas-to-card lightness step, not shadows.
- Flip to the white theme for transactional forms while reusing the same yellow button and hairline tones.

**Don't**
- Add a second brand color; the Smart Money turquoise is a one-off, not a system token.
- Fill cards or buttons with the trading green/red, or reuse them as generic success/error states.
- Put white text on yellow — the CTA reads black-on-yellow or not at all.
- Lay mesh gradients, glows, or glass over the canvas; the system is flat color blocks (the one yellow-to-dark hero gradient is event-page-only).
- Loosen the 80px band rhythm into airy marketing spacing or thin display weights down to 400.
