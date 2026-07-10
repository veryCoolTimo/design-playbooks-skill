---
name: runwayml
kind: site
style: PH
category: ai-creative-tools
website: null
pages: [home, pricing, research, studios, contact]
palette:
  canvas: "#ffffff"
  ink: "#030303"
  primary: "#000000"
  accents: ["#676f7b", "#e7eaf0", "#1a1a1a", "#d0d4d4"]
typography:
  display: "abcNormal (ABC Diatype-like grotesque; Inter substitute) · regular 400 · tight negative tracking (-0.9 to -1.2px)"
  body: "abcNormal · 400 · line-height 1.5"
radius: "buttons pill; cards mixed — 0px pricing/form cells, 8px media tiles, 16px hero panels"
---
## Overview
A monochrome, editorial marketing system that feels like a film-festival catalog rather than a SaaS site. Cinematic photography on near-black scrims alternates with pure white reading bands; every accent job is handled by a ladder of grays, and one proprietary sans covers the entire hierarchy at regular weight. No gradients, no shadows, no color signal anywhere — restraint is the brand.

## Layout
White top bar (~64px): lowercase wordmark left, five centered menu items, then text links plus a black pill CTA on the right; no bottom hairline. Sections cycle dark photo hero → white reading band → research grid → full-width photo interlude → dark CTA → black footer. Content caps around 1280px with big gutters; section verticals run 64–96px. Pricing is a five-column continuous slab split by 1px hairlines instead of gapped cards; research rows use a 5/7 image-left/text-right split on a 12-column grid; studios pages break rank with an irregular mixed-aspect masonry of poster tiles.

## Components
Buttons: one 40px black pill (white text, 14px/600) for every primary action, an inverted white pill on dark photo surfaces, and a white pill with 1px black border for secondary — no size variants. Cards are flat: zero shadow, zero border, separated by hairlines (#e7eaf0 / #c9ccd1); the featured pricing tier gets only a pale-gray infill, no badge or colored border. Inputs are borderless with a 1px bottom rule that darkens from hairline to ink on focus — no glow. Thumbnails sit at 16:9 with 8px corners over a cool gray placeholder; footer is near-black with gray small-caps column heads.

## Signature
- Every CTA on the site is the exact same black pill — zero accent color competing with photography
- Uppercase eyebrow → tight-tracked 36–48px regular-weight headline → gray lead paragraph, repeated as a fixed lockup
- Five-tier pricing slab where "featured" means a subtle gray surface step, nothing louder
- Full-bleed atmospheric stills (dusk forest, night sky) used as pacing breaks between white bands

## Do / Don't
Do:
- Keep pure black scarce: primary pills and the footer only; if two pills share a viewport, demote one to the bordered ghost variant
- Set all headings at weight 400 with -0.9 to -1.2px tracking; differentiate hierarchy by size, never by a second typeface
- Use body copy in graphite #404040 on white, saving near-black #030303 for headings and emphasis
- Mark a featured comparison item with a #e7eaf0 fill, and divide grids with 1px hairlines rather than gaps
- Run photos full-bleed at page edges; give them 16px corners only when contained mid-page

Don't:
- Don't add any hue — no blue links, no green checks, no red errors; validation relies on rules and copy
- Don't put shadows, glows, or gradients on cards or buttons; depth comes from photos and tonal steps
- Don't mix bold and light weights within a headline or set body/button text in uppercase
- Don't round pricing cells or form fields — pills are for buttons, square edges for tables and inputs
- Don't center multi-sentence paragraphs; reading bands stay left-aligned
