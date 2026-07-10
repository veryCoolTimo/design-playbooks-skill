---
name: intercom
kind: site
style: EL
category: customer-service-saas
website: https://www.intercom.com
pages: [home, pricing, product, customers]
palette:
  canvas: "#f5f1ec"
  ink: "#111111"
  primary: "#111111"
  accents: ["#ff5600", "#0007cb", "#d3cec6", "#ebe7e1"]
typography:
  display: "Saans (proprietary geometric sans; Inter 500 closest free stand-in) · medium 500, never bold · strongly negative tracking that scales with size (-2px at 72px, 0 at body)"
  body: "Saans 400 (Inter/Geist as substitutes); SaansMono only inside product-UI code snippets"
radius: "buttons small-medium 8px; cards medium 12px, product-mockup tiles 16px; pills only on tab toggles, never on CTAs"
---
## Overview
A quiet, publication-like SaaS marketing surface where a warm cream background (#f5f1ec, never pure white) does the brand work. Everything else is restraint: charcoal #111111 type and CTAs, white cards separated from the cream by hairlines rather than shadows, and one deliberate jolt of Fin Orange #ff5600 reserved exclusively for the Fin AI product. High-fidelity product screenshots, not illustration, carry every section.

## Layout
Sticky 56px cream nav (wordmark left, links center, login/signup right; hamburger below 768px). Content maxes around 1280px with 96px vertical gaps between sections. Hero leads with a 72px medium-weight headline, then each section is built around a full-width white tile holding a product screenshot. Card grids run 3-up on desktop, stepping to 2-up at 1024px and 1-up under 768px. Depth is expressed as white-on-cream surface changes, never drop shadows.

## Components
- Buttons: 8px radius, 10x18px padding, 15px/500 label. Primary is charcoal fill with white text; secondary is white with a 1px #d3cec6 hairline; the orange fill exists only as a Fin-product variant. No pill CTAs.
- Cards: white tiles at 12px radius (pricing, features, testimonials) or 16px for screenshot frames; featured pricing tier inverts to charcoal. Borders are 1px warm-gray hairlines; shadowless.
- Inputs: white fill, 8px radius, 10x14px padding.
- Tabs: pill toggles where the selected state lifts onto white; FAQ accordions sit flat on cream with soft hairline rules.
- Testimonial strip is the one true-black moment on the page.

## Signature
- Warm cream canvas instead of white — the single most identifying trait.
- One family (Saans) for the whole hierarchy: size, 500/400 weight split, and proportional negative tracking do all the work.
- Product screenshots as the hero content of every section; marketing chrome deliberately mute.
- Fin Orange as a scarce, product-scoped accent — never a system primary or background.

## Do / Don't
Do:
- Keep #f5f1ec as the page ground and create hierarchy by lifting cards to pure white.
- Set display type at weight 500 with negative tracking proportional to size; body at 400 with zero tracking.
- Make charcoal the default CTA fill; hold #ff5600 back for Fin-branded buttons and badges only.
- Lead each section with a screenshot inside a 16px-radius white tile.
- Use sentence-case 14px/500 eyebrows.

Don't:
- Don't swap the cream canvas for pure white or add drop shadows to cards.
- Don't pill-round buttons or write all-caps tracked eyebrows.
- Don't put charcoal and orange CTAs in the same viewport, or use orange as a section background.
- Don't introduce a second display typeface or promote the in-product chart colors (blue/pink/lime/cyan) to marketing surfaces.
