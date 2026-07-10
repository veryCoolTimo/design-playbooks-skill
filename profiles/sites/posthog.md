---
name: posthog
kind: site
style: CP
category: developer-tools
website: null
pages: [home, pricing, docs, product-feature]
palette:
  canvas: "#eeefe9"
  ink: "#4d4f46"
  primary: "#f7a501"
  accents: ["#23251d", "#2c84e0", "#2c8c66", "#cd4239", "#7c44a6", "#1078a3"]
typography:
  display: "IBM Plex Sans Variable · bold-to-extrabold (700/800) · slightly tight (-0.5 to -0.6px) on larger sizes"
  body: "IBM Plex Sans Variable (400); Source Code Pro / ui-monospace for code"
radius: "small 2-6px (buttons and cards both ~6px; pill only for nav CTA and chips)"
---
## Overview
A cheerful dev-tools brand that swaps the genre's dark-tech gloom for a warm cream sheet covered in cartoon hedgehog mascots. One typeface (IBM Plex Sans) does all the work through weight steps 400-800, ink is olive-tinted rather than true black, and exactly one loud color exists: the yellow-orange CTA. The overall feel is a friendly engineering textbook with doodles in the margins.

## Layout
Cream 56px nav (logo + hedgehog left, yellow "Get started" pill far right), sometimes with a 40px soft-gray sub-nav strip beneath. Content caps near 1280px; sections stack on an 80px rhythm with the cream running edge-to-edge — no alternating background bands, no dividers. Marketing pages use 4/3/2/1-up white-card grids with 16px gutters; docs add a sticky 240px sidebar (icon-labeled sections, "Ask PostHog AI" search on top) beside a ~720px article column. Footer is a 6-column link grid over the same cream.

## Components
Buttons: 40px tall, 6px radius, bold 14px labels — yellow #f7a501 fill with dark olive text for primary, soft gray #e5e7e0 for secondary, ghost for tertiary; pressed darkens the yellow to #dd9001. Cards are white (docs use warm-white #fcfcfa) with 1px olive hairline borders (#bfc1b7), 24px padding, 6px corners, and zero drop shadow. Inputs are 36px white fields with hairline borders that switch to a 2px blue border plus translucent focus ring. Active tabs signal by flipping surface: product tabs turn white against cream, pill filters invert to dark ink. Docs get emoji-prefixed pastel callout banners (blue/green/red/purple) and dark olive code blocks floating inside white cards.

## Signature
- Hand-drawn hedgehog characters (lab coats, hammocks, terminals) as the entire decorative system — no photos, gradients, or mesh backgrounds
- Warm cream #eeefe9 page background with true-white cards outlined in thin olive hairlines, everything flat
- A single saturated hue: the yellow-orange CTA pill, kept scarce (roughly one per fold)
- Olive-charcoal #23251d pulls double duty as headline ink and inverted code-block surface

## Do
- Keep the page background cream #eeefe9 end to end; place white bordered cards on top of it
- Reserve #f7a501 strictly for primary CTAs, with dark olive (not white) label text
- Build hierarchy from Plex Sans weight jumps (400 body, 600/700 emphasis, 800 display) instead of extra colors
- Space major sections 80px apart and let cards separate content — skip rules and shaded bands
- Anchor a mascot illustration in card margins where personality is wanted; pair code with dark olive blocks

## Don't
- Don't put shadows under cards or introduce gradient/atmospheric backgrounds — depth comes from borders and illustration
- Don't add a second saturated CTA color or splash the doc-callout pastels onto marketing surfaces
- Don't swap the cream canvas for pure white or a full-bleed dark hero
- Don't uppercase text outside eyebrows, tiny badges, and footer column headers
- Don't replace hedgehog characters with a generic icon set — the mascot is the identity
