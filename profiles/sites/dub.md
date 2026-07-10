---
name: dub
kind: site
style: ML
category: marketing-saas
website: https://dub.co/
pages: [home, pricing, blog, customers, enterprise, resources]
palette:
  canvas: "#FFFFFF"
  ink: "#171717"
  primary: "#171717"
  accents: ["#E8590C", "#2563EB", "#C026D3", "#FDF0E4"]
typography:
  display: "Inter Display / geometric grotesque · medium (500-600), never heavy · slightly tight"
  body: "Inter"
radius: "medium 8-14px (buttons ~8px, cards 10-14px; nav sign-up pill)"
---
## Overview
Near-monochrome minimal-light system on white, with warmth injected only through soft peach-to-cream gradient washes in hero and CTA bands. Black is the primary action color; hue arrives sparingly as functional accents — brand orange for stats and toggles, blue for the featured pricing tier, magenta for Enterprise. Everything else is hairline gray borders, generous whitespace, and restrained medium-weight type.

## Layout
Slim sticky top nav: wordmark left, centered text links, Log in + solid black Sign up button right. Heroes are center-aligned: small pill announcement badge, 2-line headline, one-sentence subhead, paired CTAs (solid black + ghost/outline), then a product screenshot or inline demo widget. Hero sits on a warm gradient panel with a faint grid/dot texture; the rest of the page returns to flat white or #FAFAFA. Sections alternate: 2-up feature cards, full-width analytics screenshot, logo strips of customer wordmarks in bordered tiles, mono-font stat counters, testimonial card grids (2-col with tinted gradient backgrounds per brand), and a closing gradient CTA band that mirrors the hero. Blog/customers use dense uniform card grids (3-col); resources is a classic docs layout with left breadcrumb article + right on-page TOC.

## Components
Buttons: solid black fill, white text, ~8px radius, no shadow; secondary is white with 1px gray border; Enterprise uses a magenta (#C026D3) fill. Cards: white, 1px #E5E5E5 border, 10-14px radius, little-to-no shadow; testimonial cards get soft brand-tinted gradient fills. Inputs: white, 1px border, ~8px radius (link-shortener demo input has an orange submit square). Toggles and switches in brand orange or blue. Pricing table uses colored filled check-dots per tier (black/blue/teal/purple) against hairline row dividers. Docs callouts: pale green tip boxes with rounded corners.

## Signature
- Warm peach/cream gradient hero and footer-CTA panels bracketing an otherwise pure white page
- Monospace orange stat counters (customers, links created, clicks tracked) as a proof section
- Testimonial/customer cards with per-brand pastel gradient tints inside hairline-bordered white grids
- Black-fill primary buttons everywhere; color reserved for meaning (blue = featured plan, magenta = enterprise, orange = brand/data)

## Do
- Use solid near-black (#171717) for every primary CTA; keep hover states subtle
- Bracket the page: warm gradient wash top (hero) and bottom (CTA band), flat white in between
- Keep headings at medium weight with tight-but-not-crushed tracking; let whitespace do the hierarchy
- Render metrics in monospace with the orange accent for an "infrastructure" feel
- Border cards with 1px light gray instead of shadows; reserve tinted gradients for testimonial/brand cards

## Don't
- Don't use orange as a button fill for main CTAs — on this site it only marks data, toggles, and micro-elements
- Don't add heavy drop shadows or dark sections; the darkest large surface is a screenshot, not a band
- Don't use bold/black heading weights or display serifs — everything stays in one grotesque family
- Don't crowd sections; each block gets a single idea with large vertical padding
- Don't mix more than one accent hue per component (blue tier, purple tier, never both on one element)
