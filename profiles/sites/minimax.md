---
name: minimax
kind: site
style: ML
category: ai-models
website: null
pages: [homepage, product-showcase, documentation, pricing]
palette:
  canvas: "#ffffff"
  ink: "#0a0a0a"
  primary: "#0a0a0a"
  accents: ["#ff5530", "#ea5ec1", "#1456f0", "#a855f7", "#3daeff"]
typography:
  display: "DM Sans · semibold 600 · tight negative tracking (-2px at 80px)"
  body: "DM Sans"
radius: "pill buttons/tabs/badges; cards 16px (quiet white) vs 32px (gradient product)"
---
## Overview
A two-mode identity: austere black-on-white editorial marketing chrome, punctured by saturated color-block product cards where each model line owns a distinct hue (coral for M2.7, magenta for Music, blue for Hailuo video, purple for Speech). One typeface (DM Sans) covers everything from an 80px hero down to 12px microcopy, with weight — never a second face or italics — carrying all emphasis. The overall feel is a magazine spread of album covers sitting on a clean spec sheet.

## Layout
Sticky white top nav (~64px, hairline bottom border) with wordmark, link row, and paired CTAs: black pill + outlined pill; an optional black promo strip sits above the nav. Hero is centered: huge tight-leaded headline, steel subtitle, dual pill CTAs, with roughly 96px of air above the fold. Content runs in a 1280px container: a 4-column strip of 32px-radius gradient cards, then a 4-column grid of bordered white tiles, a 4-cell stat row, and a dense black multi-column footer. Docs shift to a 3-column frame (220px sidebar / ~720px prose / 180px TOC) with much tighter 32-64px section gaps versus 80-96px on marketing pages.

## Components
Buttons are always full pills at ~40px height: black fill with white label (primary), transparent with 1px ink outline (secondary), white fill with hairline border (tertiary); pressed lifts black to charcoal, disabled goes hairline-gray. Cards split into two families — vivid full-bleed color cards at 32px radius with white text and internal gradients (no shadows; color supplies depth), and flat white cards at 16-24px radius with a 1px #e5e7eb border. Inputs are 40px, 8px radius, hairline border, switching to a 2px deep-blue border on focus. Tabs come in two flavors: ink-underline segmented tabs and pill tabs whose active state inverts to black fill. Badges are small pills — coral NEW, pale-blue BETA, pale-green success. Tables stay rectangular with gray header rows and soft hairline row dividers. Elevation is mostly level-0 flat; shadows appear only on dropdowns, modals, and the occasional featured card.

## Signature
- Black pill CTA on pure white — the single most repeated interactive element
- Per-product color coding: each model release gets its own saturated card hue, used nowhere else
- Deliberate radius contrast in one viewport: 32px gradient showcases next to 16px bordered white tiles
- 80px / weight-600 / -2px-tracking hero type with 1.10 leading, all in DM Sans

## Do / Don't
**Do**
- Make the black pill the default action everywhere; invert active pill tabs to black fill too
- Assign each product line one fixed brand color (coral, magenta, blue, purple) and keep the mapping stable
- Keep white cards flat with 1px hairline borders; let gradient cards carry depth through color alone
- Push display type large and tight (-1 to -2px tracking, 1.10 leading) while body stays 1.5 line-height
- Place a full-width black promo banner above the nav for time-limited announcements

**Don't**
- Don't spill coral/magenta/blue/purple onto generic buttons, body text, or backgrounds — they only mark product identity
- Don't use any radius short of full-pill on buttons, tabs, or badges
- Don't add a second typeface or italics; emphasis is weight only (400/500/600/700, nothing heavier)
- Don't put gradients or heavy shadows on standard white cards or buttons
- Don't loosen the hero's tight leading and negative tracking when scaling it down
