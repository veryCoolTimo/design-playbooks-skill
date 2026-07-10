---
name: replicate
kind: site
style: ML
category: ai-ml-platform
website: null
pages: [home, pricing, model-collections, enterprise]
palette:
  canvas: "#f9f7f3"
  ink: "#202020"
  primary: "#ea2804"
  accents: ["#ff6a3d", "#f4a8a0", "#f3f0e8", "#2b9a66"]
typography:
  display: "rb-freigeist-neue (fallback: Bricolage Grotesque) · heavy 700 · very tight, negative tracking scaling with size"
  body: "basier-square (fallback: Geist/Inter); jetbrains-mono for all code"
radius: "pill on all interactive elements (buttons, inputs, badges); medium 10-16px on cards and code wells"
---
## Overview
A developer-tools site that borrows the feel of a print zine: warm cream backgrounds instead of white, ink-dark text, and one hot orange that only shows up where it matters most. Giant condensed display type (up to 128px, line-height 1.0) does the decorating; dark monospace code panels sit in the cream page like printed pull-quotes. Depth comes from color-blocking (cream, bone, dark, black) rather than shadows.

## Layout
60px cream nav bar with a hairline bottom border — wordmark left, page links center, GitHub icon plus pill CTA right. Home opens with a full-bleed orange hero (radial mesh from #ea2804 through #ff6a3d to pink #f4a8a0) topped by a 128px headline; interior pages open on cream with 72px headers. Sections alternate cream, orange band, dark code-story band, then a pure-black footer, with 96-160px of vertical breathing room. Content maxes around 1280px; model grids run 4-up on desktop, code-story sections split copy-left / code-right until 1024px.

## Components
- Buttons: fully pill-shaped, 44px tall, semibold 16px labels. Variants stack cleanly — orange fill (primary, darkens to #c01f00 pressed), near-black fill, white with 1px dark outline, borderless ghost, 36px circular icon buttons.
- Cards: white on cream, 10px radius, hairline border instead of shadow; pricing tiers step up to 16px radius, with the recommended tier inverted to dark #202020. Collection tiles are cream-on-bone.
- Inputs: pill-shaped, white fill, hairline border, blue focus ring.
- Code wells: dark #202020 panels with 10px radius, black tab strip on top; active tab gets an orange underline. Always JetBrains Mono.
- Badges: pill-shaped — green (#2b9a66) status pills, outlined cream capability tags.

## Signature
- Cream (#f9f7f3) as page canvas with white reserved strictly for cards and inputs — the warmth is the brand temperature.
- One orange (#ea2804) doing exactly three jobs: primary CTA, home hero band, inline links — treated like a rubber stamp, roughly one per viewport.
- Massive freigeist display headlines at line-height 1.0 with tracking that tightens as size grows (-3px at 128px).
- Every interactive element is a pill; every content container is a soft rectangle — the split never blurs.

## Do
- Keep the page background cream and let white appear only on discrete cards, inputs, and thumbnails.
- Hold orange to CTA + hero + links; if two orange elements share a viewport, demote one to dark.
- Set display type at line-height 1.0 with negative tracking; clamp hero sizes down the breakpoint ladder (128 → 96 → 64 → 48).
- Render all code in dark wells with JetBrains Mono, tab strip in near-black on top.
- Elevate with color shifts (cream → bone → dark) and hairline borders, not shadows.

## Don't
- Don't swap the cream canvas for pure white — it flattens the whole identity.
- Don't add a second accent color; green and focus-blue are functional only.
- Don't bold body copy to 500 for emphasis — switch to the display family instead.
- Don't make content cards pill-shaped or leave them sharp-cornered; they live at 10-16px.
- Don't drop code into light grey boxes or paint large surfaces orange.
