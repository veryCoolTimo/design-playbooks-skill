---
name: mural
kind: site
style: CP
category: collaboration-saas
website: https://www.mural.co/
pages: [home]
palette:
  canvas: "#ffffff"
  ink: "#0d0d0d"
  primary: "#ff4b4d"
  accents: ["#fecee0", "#5a88f6", "#00c27a", "#bf53fe", "#fc83ff", "#ffe245", "#edeedb", "#000000"]
typography:
  display: "high-contrast editorial serif (Tiempos/Value Serif-like) · regular weight at very large sizes · tight, slightly negative tracking"
  body: "neutral grotesque sans (Graphik/Inter-like)"
radius: "small 2-6px on buttons; cards split between square-edged full-bleed color blocks and medium 8-12px app mockups"
---
## Overview
A poster-like page built from stacked full-bleed color bands: white hero, pure black interlude, saturated cornflower blue, kelly green, violet, beige, and hot magenta, each carrying one idea. Oversized editorial serif headlines sit on flat, ungradiented color with hand-drawn illustrations and product mockups as counterweights. It reads as a playful print campaign more than a typical SaaS template.

## Layout
Slim white nav: multicolor wordmark left, four text items with chevrons, "Sign in" text link plus a dark near-black (#424242) pill-ish button right. Hero is a 50/50 split — giant two-line serif headline and short sans subhead left, whiteboard product mockup bleeding off the right edge. Below, the page proceeds as edge-to-edge color sections with no visible container borders; rhythm comes from abrupt background swaps (white → black → blue → green → white → beige...). The green section uses an accordion-style list of huge serif headlines separated by thin black rules ("Connect as a team", "Make a plan"...). Logo wall is a plain 2-column grid of monochrome marks beside a violet testimonial block. Footer CTA is a magenta band with a giant yellow marker-shaped "Get started" block, then a beige multi-column sitemap footer.

## Components
Primary CTA is a distinctive two-part button: a red (#ff4b4d) square chip holding a black chevron, fused to a pale pink (#fecee0) label field with black text, corners ~4-6px — repeated in hero, blue section, and enterprise section (label field turns lavender/blue on colored bands). Secondary nav button is a solid dark gray/near-black rectangle with white text. A green chip + white-label variant ("Learn more about LUNA") and yellow chip variant ("Explore all templates") reuse the same chip+label anatomy. Cards are flat and borderless: the black "Come up with ideas" panel is sharp-cornered with a white close X; the embedded whiteboard mockups get soft medium radius and faint shadow. Feature rows use thin 1px black rules as separators instead of card containers. No gradients, no glassmorphism, almost no drop shadows.

## Signature
- Stacked full-bleed flat color bands (black, #5a88f6 blue, #00c27a green, #bf53fe violet, #fc83ff magenta) with no transitions between them
- Compound chip+label CTA: red arrow square welded to a pastel pink text field
- Enormous editorial serif headlines (often lowercase-led) over flat color, paired with a small grotesque sans for everything else
- Hand-drawn, chunky multicolor illustrations (tangled figures, hands, trees) and the multicolor wordmark echoing sticky-note colors

## Do / Don't
**Do**
- Give each section one flat, fully saturated background color and let it run edge to edge
- Set headlines in a large high-contrast serif at 3-5x body size; keep body copy small, sans, and black
- Build CTAs as the two-part chip+label unit; recolor the label field per section but keep the chip/arrow anatomy
- Use thin 1px black rules and typography, not boxed cards, to separate list content
- Drop in playful hand-drawn illustration or real whiteboard UI (sticky notes, cursors with name tags) as the imagery

**Don't**
- Add gradients, glass blur, or heavy drop shadows — every surface here is flat
- Use large corner radii or pill buttons; corners stay square to barely-rounded
- Tint or desaturate the section colors — the palette works because it is at full chroma against black text
- Set headlines in a bold geometric sans; the serif/sans contrast is the core typographic move
- Wrap content in bordered white cards floating on the colored bands
