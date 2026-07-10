---
name: expo
kind: site
style: ML
category: developer-tools
website: null
pages: [home, pricing, docs]
palette:
  canvas: "#ffffff"
  ink: "#171717"
  primary: "#000000"
  accents: ["#0d74ce", "#cfe7ff", "#a8c8e8", "#60646c", "#f0f0f3"]
typography:
  display: "Inter · semibold (600) · tight negative tracking (-0.5 to -1.9px)"
  body: "Inter"
radius: "medium 8-14px (buttons 8px, cards 12px; device mockups 16px; pills only on badges)"
---
## Overview
A white-canvas developer-platform look where restraint does the branding: near-black text on pure white, black-filled CTAs, and one soft sky-blue gradient wash confined to the hero. Inter handles all text at just two weights (600 display, 400 body), with JetBrains Mono on every code surface. Depth comes from hairline borders and a single faint shadow tier rather than color or decoration.

## Layout
Slim 64px white top bar: wordmark left, horizontal menu, Sign In plus a black CTA right; collapses to hamburger under 768px. Hero is centered — 64px headline over the gradient sky, one CTA, then a MacBook + iPhone screenshot composite that acts as the page's chrome. Content caps around 1200px on a 12-column grid; sections breathe at 96px vertical rhythm while card clusters stay tight (16-24px gaps). Grids run 3-up for features, 8-up for ecosystem logo tiles, 5 columns in the footer.

## Components
- Primary button: solid #000000 fill, white 14px/500 label, 40px tall, 8px radius; press state lightens to #1a1a1a. Never a pill, never blue.
- Secondary button: white fill with a 1px #dcdee0 border, ink text, same 8px/40px geometry.
- Cards: white, 12px radius, 1px hairline border, hover gets one soft shadow (0 4px 12px rgba(0,0,0,.04)). Dark inversions (#171717) mark feature cards, code blocks, IDE mockups, and the featured pricing tier.
- Inputs: 44px tall, 8px radius, hairline border thickening to 2px ink on focus.
- Badges: tiny uppercase pills (11px/600, +0.88px tracking) on #f0f0f3 — the only pill shape on the site.

## Signature
- MacBook + iPhone device composite showing real product screens, floating over a sky-blue gradient — the hero IS the product demo.
- Black as the sole CTA color; blue (#0d74ce) exists only as inline text links.
- Dark #171717 panels used as inversion accents: code blocks, IDE mockups, featured pricing.
- Inter locked to two weights (600/400) with strongly negative display tracking.

## Do / Don't
**Do**
- Fill primary CTAs with pure black at 8px radius, 40px height.
- Keep display type at Inter 600 with tight negative letter-spacing; body at 400.
- Set all code in JetBrains Mono, white-on-#171717 dark blocks.
- Lead the hero with a device-mockup composite over the sky-blue wash.
- Use dark #171717 card inversions to spotlight one item (featured tier, code demo).

**Don't**
- Don't add a saturated brand color — black is the only action fill.
- Don't put blue on buttons; #0d74ce stays inside running text.
- Don't use pill-shaped CTAs — pills belong to badges alone.
- Don't repeat the sky gradient outside the hero band.
- Don't push display weight past 600-700 or below 600.
