---
name: sentry
kind: site
style: DN
category: developer-tools
website: null
pages: [home, product, pricing, contact]
palette:
  canvas: "#1f1633"
  ink: "#1f1633"
  primary: "#150f23"
  accents: ["#c2ef4e", "#fa7faa", "#6a5fc1", "#422082", "#79628c"]
typography:
  display: "Sentry Display (proprietary; substitute Space Grotesk/Archivo) · chunky bold, near-condensed · normal tracking"
  body: "Rubik"
radius: "buttons medium 8px; cards 12-18px"
---
## Overview
A dark-neon developer brand that splits the world in two: violet midnight canvases (#1f1633) for marketing and feature pages, plain white for pricing, contact, and dense reference content. Electric lime (#c2ef4e) is a typographic device — highlight chips wrapping single keywords in giant headlines — while hand-drawn sticker mascots and starfield textures give an observability tool a mischievous streak. The whole thing reads like log output with a personality.

## Layout
Top nav with logo left, dropdown items center, ghost + filled CTA pair right; inverts polarity per page (dark on home, light on pricing), hamburger below 768px. Hero leads with an 88px display headline containing a lime keyword chip, airy 2.0-leading subtext, and a CTA pair. Sections separated by ~96px bands; content maxes near 1152px. Pricing runs a 4-up card row (2-up, then 1-up as it narrows). Dark pages get generous whitespace for mascots and textures; light transactional pages tighten density for scanning.

## Components
Buttons: 8px radius, 12x16px padding, uppercase 14px/700 labels with 0.2px tracking. Primary is near-black violet fill (#150f23) with white text on light pages; on dark pages it flips to a white fill with dark text plus a dark glow halo. Secondary is a translucent white ghost. Pressed states swap polarity toward light gray fills. Cards: 12px radius on pricing tiers (white with #e5e7eb hairline; the featured tier fully inverts to #150f23), 18px on large dark feature cards (#1f1633 with #362d59 hairline) — no shadows on dark canvas. Inputs: white, 6px radius, #cfcfdb hairline, inset-shadow focus plus a translucent blue ring; contact-form selects use a deep violet #422082 fill. Code blocks: #150f23 with Monaco at 16px.

## Signature
- Lime highlight chips (#c2ef4e, 4px radius) wrapping individual words inside hero headlines, like syntax highlighting on prose
- Floating sticker mascots (astronauts, monsters, cones) with hand-drawn outlines, overlapping section boundaries, never boxed in cards
- Hand-drawn lime squiggle divider above the footer instead of a hairline
- Featured pricing tier signaled by full dark inversion rather than an accent border

## Do / Don't
Do:
- Commit each page to one canvas polarity — dark violet for marketing, white for transactional — never mixed on a page
- Set all button labels and eyebrows uppercase with a slight (0.2px) tracking lift
- Keep lime scarce: roughly one lime element per viewport, only as headline chips or the footer squiggle
- Use 2.0 line-height for marketing prose but 1.5 for functional UI text
- Let mascots and UI-mock screenshots tilt and overlap section edges to break the grid

Don't:
- Don't use lime as a button fill or body-text color — it is a chip/decoration color only
- Don't add accents beyond lime and pink; extra hues dilute the violet-lime identity
- Don't drop-shadow cards on the dark canvas — depth comes from texture and illustration
- Don't lighten the primary button toward brand violet; the near-black fill is what makes it read as the top action
- Don't use the 88px display size anywhere but the marketing hero (sub-pages cap at 60px)
