---
name: hp
kind: site
style: ML
category: consumer-electronics
website: null
pages: [homepage, laptop-shop, printer-pricing, faq]
palette:
  canvas: "#ffffff"
  ink: "#1a1a1a"
  primary: "#024ad8"
  accents: ["#296ef9", "#0e3191", "#c9e0fc", "#f7f7f7", "#e8e8e8", "#ff5050", "#356373"]
typography:
  display: "Forma DJR Micro (geometric grotesque; sub: Manrope/Inter) · medium 500 even at hero scale · zero tracking, line-height 1.0"
  body: "Forma DJR Micro · 400, ~1.4 line-height; uppercase 600/700 with 0.7px tracking on buttons only"
radius: "buttons small 4px; cards large 16px (two-tier split); pill tabs"
---
## Overview
A white-paper catalog system that serves consumer and enterprise audiences from one page. Pure white ground, near-black ink, and a single electric blue that fires only on CTAs, links, and the wordmark-derived chevron slashes. One font family everywhere; headlines never go heavier than 500, which keeps 72px heroes feeling approachable rather than shouty.

## Layout
Stack: 36px dark utility strip → 64px white top nav (wordmark left, category links center, search/sign-in/cart right, hairline bottom border) → white body → alternating #f7f7f7/#e8e8e8 gray bands → dark ink slab ("How can we help?") → dark 5-column footer. Content maxes at 1366px with full-bleed band backgrounds. 80px vertical gap between every major section (~48px mobile). Hero is a single white card with photo on one half, copy on the other, flanked outside its box by two giant blue parallelogram slashes. Product grids run 4→3→2→1 columns; 24px gutters.

## Components
Buttons: 44px tall, 4px radius, uppercase 14px labels with 0.7px tracking; blue fill primary (pressed → #0e3191, disabled → #c2c2c2 gray), black ink fill variant, blue- or ink-outlined secondaries, plain blue text links. Cards: white, 16px radius, 16-24px padding, soft `0 2px 8px rgba(26,26,26,.08)` lift — the only shadow tier besides rare modals; feature cards sit on #f7f7f7. Featured pricing tier gets a thin blue top border and blue price text, never an inverted background. Inputs: 44px, 4px radius, 1px #c2c2c2 border that turns ink on focus — no halo. Pill tabs for sub-nav filters (active = ink fill, white text). Sale tags are small coral #ff5050 chips. FAQ accordions on 8px-rounded rows with hairline dividers.

## Signature
- Two angular blue chevron slashes (0 radius, ~60° cut) flanking hero cards — an architectural-scale echo of the HP wordmark; hero-only, gone on mobile
- Sharp/soft radius split: near-square 4px buttons against 16px-rounded cards and photo frames
- Weight-500 display type at every size including 72px heroes; letter-spacing exists only in uppercase button labels
- Page rhythm always closes on dark ink slabs: testimonial band, help band, footer

## Do / Don't
Do:
- Cap the blue at roughly two elements per viewport (one CTA + one chevron); it works because it is scarce
- Alternate white with #f7f7f7/#e8e8e8 bands for section rhythm and let color contrast, not shadows, carry depth
- Keep display weight at 500 with line-height 1.0 even for the biggest headline
- End the page with an ink-colored help band and footer
- Frame product photos in 16px-rounded rectangles; avatars are 4px-rounded squares, never circles

Don't:
- Round buttons past 4px — soft pill CTAs break the brand's sharp/soft split
- Add saturated colors beyond the blue family, coral sale tags, and teal storm infographic tones
- Fade ink opacity for hierarchy — step to #3d3d3d or #636363 instead
- Use the chevron motif inside cards or as scattered decoration
- Pile on heavy material shadows; only product/pricing cards get the one soft lift
