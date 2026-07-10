---
name: getapron
kind: site
style: CP
category: fintech-payments
website: https://getapron.com/
pages: [home, product, pricing, audience-accountants, audience-businesses]
palette:
  canvas: "#F8F3E4"
  ink: "#1B1B1B"
  primary: "#FFE223"
  accents: ["#F6EFA6", "#FFFFFF", "#141414"]
typography:
  display: "Chunky rounded grotesque (Gelica/Recoleta-adjacent softness, grotesque bones) · very heavy (800-900) · tight, near-touching"
  body: "Clean geometric grotesque (Aeonik/Graphik-like) · regular · normal spacing"
radius: "pill for buttons; near-none for cards (receipt cards with zigzag perforated edges, photos square-cornered)"
---
## Overview
A receipt-and-Polaroid world on warm paper: cream canvas, butter-yellow hero bands, and near-black type set enormous and heavy. The core metaphor is physical paper — feature cards are thermal receipts with zigzag edges and typewriter mono text, testimonial photos are tilted snapshots with white borders and soft shadows, and hand-drawn ink doodles (a walking receipt character, scribbles) wander around the layout. Feels like a friendly indie brand, not a bank, despite being a payments product.

## Layout
Centered nav: left links (Accountants & Bookkeepers, Businesses), logo dead-center ("apron." lowercase with period), right utilities plus a black pill "Start now" CTA. Hero is fully centered on a pale-yellow (#F6EFA6-ish) band: giant multi-line headline, short subcopy, one or two pill CTAs, sometimes a tilted product screenshot framed by doodles. Below the fold the canvas shifts to cream and sections alternate: centered heading → fanned row of 3-5 rotated receipt cards; two-column photo + quote testimonials; oversized stat numbers (1000s / 10hrs / 5min) stacked vertically; "Every payment tells a story" customer-story carousel with prev/next circle arrows; giant closing CTA headline flanked by two tilted photos. Generous vertical whitespace, almost everything center-axis; comparison tables and pricing use the same receipt styling.

## Components
- Buttons: pill shape. Primary = solid bright yellow (#FFE223) with black text ("Start now"); secondary = white/cream pill with thin black outline ("Book a demo"); nav CTA = solid black pill with white text. No shadows on buttons.
- Receipt cards: white, square-cornered with zigzag/perforated top-bottom edges, mono/typewriter uppercase headers with "## 1 ##" numbering, small mono body text, slight random rotation, soft drop shadow. Used for features AND pricing plans.
- Pricing cards: same receipt treatment, big price figure in the heavy display face, dashed dividers, outline pill CTA inside.
- Text links: mono font with a yellow highlighter background and arrow ("Read more →", "Learn more →").
- Photos: real candid people, white Polaroid-style borders, rotated a few degrees, soft shadows.
- FAQ: plain rows with dotted dividers and circled chevron toggles. Comparison table uses yellow circular check chips.

## Signature
- Thermal-receipt cards with zigzag edges, typewriter mono type, and "## N ##" ticket numbering, fanned at playful angles.
- Ultra-heavy rounded display headlines at poster scale ("Your payments powerhouse", "Ready to roll?") on butter-yellow or cream.
- Hand-drawn ink doodles interacting with UI screenshots and headlines (walking receipt mascot, scribble arrows).
- Yellow-highlighter mono links and a strictly yellow/cream/black/white palette — color arrives only through photography.

## Do / Don't
Do:
- Keep the palette to cream canvas, pale-yellow hero bands, black ink, and one bright yellow reserved for primary CTAs and highlights.
- Style feature/pricing cards as receipts: zigzag edges, mono uppercase text, ticket numbering, slight rotation, soft shadow.
- Center almost everything and let headlines get huge — 3-4 stacked lines in the heavy display face.
- Use candid, warm photography of real people in tilted white-bordered frames.
- Render inline links as monospace text with a yellow highlight and trailing arrow.

Don't:
- Don't introduce blues, gradients, or glassmorphism — the site has zero cool tones or shine.
- Don't round card corners or add heavy borders; only buttons are pills, cards stay paper-square.
- Don't set everything perfectly straight — receipts, photos, and screenshots all sit at small random angles.
- Don't use icon libraries; illustration here is hand-drawn doodles and mono glyphs, not vector icon sets.
- Don't make the display type thin or wide-tracked — it is fat, tight, and rounded everywhere.
