---
name: index-app
kind: site
style: ML
category: analytics-bi-saas
website: https://index.app/
pages: [home, pricing, blog]
palette:
  canvas: "#F5F3EF"
  ink: "#25221E"
  primary: "#2B2723"
  accents: ["#E8552B", "#6B7CF0", "#EDE9E2", "#1C1916"]
typography:
  display: "neo-grotesque sans (Inter/Neue Haas feel) · medium-semibold · normal-to-slightly-tight"
  body: "same neo-grotesque sans, regular weight, quiet gray-brown tone"
radius: "buttons small-medium 6-10px; cards medium 12-16px; section wrappers and footer band large 24px+"
---
## Overview
Warm minimal-light system built on a cream/eggshell canvas with near-black charcoal ink — no pure white, no pure black. Color is rationed: one orange accent word or badge per view, plus multicolor chart fills (orange, blue, purple) that live only inside product/dashboard mockups. Large dark charcoal bands (hero mockup surround, pre-footer CTA, Enterprise pricing column) invert the scheme for emphasis. Faint circuit-board line illustrations texture backgrounds at very low contrast.

## Layout
Slim top nav: small logo mark + wordmark left, centered text links (Features, Pricing, Blog, Changelog, Careers, Support), lone "Log in" right — no nav CTA button. Heroes are centered: small pill "eyebrow" badge with icon, large 2-line headline, 1-2 line muted subcopy, single dark CTA. Home stacks alternating sections: full-width dashboard screenshot, monospace-flavored logo wall, then feature sections each framed as a rounded card or a 2-3 column grid of small bordered tiles with icon + caption pairs. Pricing uses a 4-column plan row (Enterprise column inverted dark) above a long comparison table with dark section-divider bars. Every page ends with the same dark rounded-corner CTA block ("Analyze. Visualize. Collaborate.") flowing into a dark footer with 3-column link lists. Generous vertical whitespace between sections; content column is narrow and centered.

## Components
Buttons: charcoal (#2B2723) fill with white label, small radius (~6-10px), compact padding; on dark surfaces the CTA inverts to white fill with dark text; secondary/tab buttons are white with a hairline warm-gray border. Pill eyebrow badges: white or beige fill, 1px border, tiny icon + label. Cards: white or slightly-lighter-than-canvas fill, 1px warm hairline border, 12-16px radius, essentially shadowless (at most a whisper of soft shadow on blog cards). Segmented tab control (All Posts / Announcements / Changelog) as joined pill group with active white segment. Comparison table rows use checkmarks and full-width dark rounded category header bars. Inputs/toggles (Monthly/Annually) follow the same pill-with-hairline pattern. Small orange "Popular"/"New" pill tags.

## Signature
- Cream #F5F3EF canvas + charcoal ink, with big dark rounded blocks (pre-footer CTA, Enterprise plan) as the only heavy contrast moves
- Faint tone-on-tone circuit-trace illustrations behind heroes, dark blocks, and card headers
- One orange (#E8552B) highlight per screen: a colored headline word, a "Popular" badge, a "New" tag
- Monospace seasoning: fake-brand logo wall and code/SQL snippets in mono against the otherwise single grotesque family
- Hairline-bordered, near-shadowless white cards on beige — depth via tone shifts, not shadows

## Do / Don't
Do:
- Keep the entire page in the warm beige-charcoal duotone; introduce chart colors (orange, blue, purple) only inside product screenshots and data-viz mockups
- Use exactly one solid charcoal CTA per hero/section, inverting to white-on-dark inside dark blocks
- Frame sections and the pre-footer CTA as large-radius (24px+) dark or beige slabs with subtle circuit-line texture
- Start each section with a bordered pill eyebrow (icon + short label) above a centered headline
- Separate cards with 1px warm-gray hairlines and tone changes instead of drop shadows

Don't:
- Use pure white (#FFFFFF) page backgrounds or pure black text — everything is warmed
- Add gradients, glows, or heavy shadows; the deepest elevation seen is a faint blur under blog cards
- Color links or buttons orange — orange is reserved for accent words and small status tags; CTAs stay charcoal
- Put a signup button in the top nav or crowd it; nav stays text-only with a single quiet "Log in"
- Use large border radii on buttons (they stay 6-10px) or sharp 0px corners on cards
