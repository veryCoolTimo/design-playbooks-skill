---
name: icebug
kind: site
style: ML
category: outdoor-footwear-ecommerce
website: https://www.icebug.com/en-GB
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  primary: "#FFFFFF"
  accents: ["#C0392B", "#5A6B4A"]
typography:
  display: "rounded geometric grotesque (Favorit/Right Grotesk feel) · medium weight · tight tracking"
  body: "monospace grotesque (Space Mono / IBM Plex Mono feel), uppercase for UI labels"
radius: "none"
---
## Overview
An image-first e-commerce homepage where nearly all chrome dissolves into a full-bleed lifestyle photograph. The UI voice is technical and utilitarian: monospaced uppercase labels, hairline borders, square corners, no fills. Contrast comes from one enormous rounded-sans headline set in white over the darkened photo, giving an editorial-poster feel on top of shop plumbing.

## Layout
Top nav is a single slim transparent bar over the hero: left-aligned category links (WOMEN / MEN / IMPACT / SHOE FINDER), centered beetle logo + wordmark, right-aligned utilities (SEARCH, HELP, EN/GBP, LOGIN, CART 0) — all small monospaced uppercase in white. The hero is a full-viewport photograph (product worn in context) with a subtle dark gradient; content anchors to the bottom-left: tiny mono eyebrow (product code "ELI RB9X"), a two-line display headline at very large scale, then a pair of compact ghost buttons. Modals/dialogs are centered white panels with a hairline-divided header row (title left, CLOSE action right). Whitespace inside panels is generous; the photo itself carries the rest of the page.

## Components
- Buttons: small rectangular ghost buttons — transparent fill, 1px white border, white monospaced uppercase label, no radius, no shadow. Primary CTA ("SHOP NOW") is visually identical to secondary ("READ MORE"); hierarchy comes from order, not fill.
- Dialog: flat white card, square corners, no visible drop shadow beyond the photo contrast; header separated by a thin light rule; text actions ("CLOSE") instead of icon buttons.
- Inputs: full-width select with 1px light-gray border, square corners, mono placeholder text, small chevron at right.
- Validation/notice text in muted red mono ("Please select a country…").

## Signature
- Monospaced uppercase micro-typography for every nav item, button, and label — the entire UI reads like technical spec text.
- One oversized rounded geometric-sans headline bottom-left over a full-bleed photo; nothing else competes at display scale.
- Zero border-radius and zero fills: ghost buttons and hairline borders everywhere, even the primary CTA.
- Symmetric nav with a centered insect logomark splitting shop links from utilities.

## Do
- Set all nav, buttons, and metadata in small monospaced uppercase with visible letter-spacing.
- Let a single full-bleed photograph be the background; darken it just enough for white text to pass contrast.
- Anchor hero copy bottom-left: mono eyebrow, huge two-line headline, then small ghost buttons in a row.
- Keep every rectangle sharp-cornered — buttons, inputs, dialogs alike.
- Use flat white panels with hairline dividers for overlays; text-only actions like "CLOSE".

## Don't
- Don't give the primary CTA a solid fill or brand color — CTAs stay outlined and transparent here.
- Don't round corners or add drop shadows to buttons, cards, or inputs.
- Don't mix in a second display face; the mono handles everything below headline scale.
- Don't center the hero headline or shrink it — the poster scale bottom-left is the identity.
- Don't introduce saturated accent colors in chrome; color lives in the photography, with red reserved for warnings.
