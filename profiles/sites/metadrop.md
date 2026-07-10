---
name: metadrop
kind: site
style: DN
category: crypto-launchpad
website: https://metadrop.com/
pages: [home, activity]
palette:
  canvas: "#1A1A1A"
  ink: "#E8E8E6"
  primary: "#F5F5F2"
  accents: ["#C9F45B", "#FF54A6", "#3EE0DC", "#FF4B3E", "#3DDC6A"]
typography:
  display: "transitional serif (Tiempos-like) for hero, plus huge outlined-stroke grotesque page titles · regular-to-medium · normal tracking"
  body: "monospace (JetBrains/IBM Plex Mono feel) for all UI labels, tables, buttons; neutral sans for paragraph copy"
radius: "pill on buttons and chips; large 16px+ on cards"
---
## Overview
Near-black charcoal canvas where almost all UI chrome — nav, buttons, table headers, prices — is set in uppercase monospace, giving a terminal/trading-desk feel. Against that, warm editorial serif headlines ("Where coins launch.") and saturated rainbow gradients (a racetrack loop in the hero, orb-gradient coin avatars) inject playful meme-coin energy. CTAs are stark white pills; chartreuse lime is the signal color for points, links, and positive data.

## Layout
Sticky top nav: logo left, Products dropdown, centered pill search field, right-aligned white CONNECT pill and lime POINTS pill; a scrolling ticker strip of coin-price chips sits directly under the nav. Home hero is centered text inside a giant rounded rainbow "racetrack" outline. Sections alternate: a "Recently launched" row list, a horizontal strip of gradient coin cards, a top-10 data table, a 3-column feature card row, a product-screenshot walkthrough, then a bento-grid collage (logo tile, photo tiles, lime graphic tiles) before the footer. Activity page is a single full-width data table under a giant outlined title, with a right-aligned 1H/4H/24H segmented control. Generous vertical breathing room between sections; tables run edge-to-edge within a wide container.

## Components
Buttons: pill-shaped, white fill with black mono uppercase label (LAUNCH A COIN, VIEW MORE, CONNECT); lime pill variant for POINTS; some pills carry a small circular icon chip inside. Segmented control: dark pill group, active segment white. Ticker chips: dark rounded rectangles with mono coin symbol + red/green change arrows. Tables: hairline 1px row and column dividers on dark, mono uppercase column headers, lime coin symbols, green/red deltas, em-dashes for empty cells. Cards: large-radius dark or gradient-filled tiles with folder-tab cutout corners on coin cards; feature cards pair illustration panels with mono caption footnotes. Search input: dark pill with subtle border.

## Signature
- Rainbow gradient "racetrack" loop framing the hero, echoed by rainbow-orb coin avatars everywhere
- Uppercase monospace as the default UI voice (nav, buttons, tables, tickers) on near-black
- Giant outline-stroke display titles in pale lime ("Activity") vs. serif marketing headlines on home
- White pill CTAs + chartreuse lime accent (#C9F45B) as the only bright solids amid rainbow gradients
- Bento-grid collage sections mixing logo tiles, photography, and lime graphic tiles

## Do / Don't
- Do set all functional UI text (buttons, labels, table headers, tickers) in uppercase monospace
- Do keep primary CTAs as white pills with black text; reserve lime for points, links, and positive values
- Do use hairline 1px dividers for data tables and render gains green / losses red with triangle glyphs
- Do use rainbow/multicolor gradients for decorative elements (avatars, hero loop, card fills), not for text or buttons
- Do give cards large 16px+ radii and let sections breathe with big vertical gaps
- Don't use lime as a button fill for the main CTA — it marks the POINTS badge and accents, not primary actions
- Don't introduce blue/corporate SaaS palettes; the scheme is charcoal + white + lime + rainbow gradients
- Don't set headlines in the mono font — marketing headlines are serif (or outlined grotesque for page titles)
- Don't add drop shadows or glassmorphism; depth comes from borders, fills, and gradients on flat dark panels
- Don't round table containers into pills; only buttons, chips, and inputs are fully pill-shaped
