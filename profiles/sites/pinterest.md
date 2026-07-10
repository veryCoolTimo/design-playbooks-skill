---
name: pinterest
kind: site
style: PH
category: social-discovery
website: null
pages: [home, search-results, creator-marketing, creator-article, login-modal]
palette:
  canvas: "#ffffff"
  ink: "#33332e"
  primary: "#e60023"
  accents: ["#f6f6f3", "#e5e5e0", "#262622", "#435ee5"]
typography:
  display: "Pin Sans (proprietary; sub with Inter/Manrope) · semibold-to-bold · tight negative tracking (-1.2px at display)"
  body: "Pin Sans, falls back to system-ui stack; ~Inter shape"
radius: "buttons/cards 16px, large cards & modals 32px, chips/search pill"
---
## Overview
A photo-first system where the interface deliberately recedes so pinned imagery does the visual work. Chrome is white and warm cream with black type; the only saturated hue is a single brand red spent almost exclusively on the sign-up CTA and wordmark. Two moods share one skin: a spacious magazine-style marketing layer, and a dense masonry search grid where photos nearly touch.

## Layout
Sticky 64px white top bar: red wordmark left, pill search bar centered, links plus red sign-up button pinned upper right at every breakpoint. Marketing pages alternate text/image two-column feature rows on a ~1280px container with 64px between sections. Discovery pages switch to a masonry column grid (5-6 cols ultrawide down to 1 on mobile) with very tight 8px gutters; each tile keeps its native portrait/square ratio. Footer is a quiet 4-column link grid over a hairline rule.

## Components
Buttons: 40px tall, 16px corner radius (notably rounded but not pill), bold 14px labels; red fill for primary (pressed darkens to #cc001f), gray-cream #e5e5e0 for secondary, transparent ghost for tertiary. Search bar and filter chips are full pills on cream #f6f6f3; active chips invert to solid black. Text inputs: white fill, 16px radius, thin gray border, focus shown as a double ring (black inner plus blue #435ee5 outer). Pin cards have zero padding — the image is the card — with white overlay pills tagging corners; cards carry no borders and no shadows. The only shadow anywhere is under the modal, which floats on a 50% scrim at 32px radius.

## Signature
- One precise red (#e60023) confined to CTAs and the logo; everything else monochrome cream/black
- Zero-padding masonry pin tiles at 16px radius separated by 8px gutters
- Strict three-value shape vocabulary: 16px, 32px, pill — nothing sharp, nothing in between
- 70px display headlines with -1.2px tracking dropping straight to 16px body, no middle tier

## Do / Don't
**Do**
- Keep red scarce — roughly one red CTA per viewport, never as decoration or background
- Let photos fill their tiles edge to edge; put labels in white corner pills over the image
- Build hierarchy with weight (400/600/700) and size while body text stays #33332e everywhere
- Use 64px section spacing on editorial pages but collapse image grids to 8px gutters
- Track display headings tightly (-1.2px); it is part of the voice

**Don't**
- Don't add card shadows or borders — flat tiles only; shadow belongs solely to the modal layer
- Don't pad inside a pin card or stack metadata below the image
- Don't invent a radius between 16 and 32px, or ship any sharp-cornered interactive element
- Don't swap the red for a near-match; the brand tone is exactly #e60023
- Don't tint prose or links with color — inline links use warm near-black #211922, not blue
