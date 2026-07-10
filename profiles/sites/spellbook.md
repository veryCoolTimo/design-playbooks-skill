---
name: spellbook
kind: site
style: DT
category: legaltech-saas
website: https://www.spellbook.legal/
pages: [home, product, company, resources, security]
palette:
  canvas: "#111111"
  ink: "#c9c9c7"
  primary: "#ffffff"
  accents: ["#ff3e17", "#2f8fff", "#0e7a4b", "#8b5cf6", "#f5b800"]
typography:
  display: "transitional serif (Tiempos/Ivar-like) · regular-to-medium weight · tight, slightly condensed"
  body: "geometric grotesque (Inter-like) · normal spacing"
radius: "buttons pill; cards medium 8-14px"
---
## Overview
Near-black editorial dark theme where an elegant serif carries every headline and a small set of saturated primaries (red-orange, blue, green, purple, yellow) does all the color work. Product UI screenshots sit on full-bleed color blocks, so the page alternates between quiet charcoal sections and loud single-hue panels. The overall feel is "law-firm gravitas plus playful modernist geometry" — closer to a design studio than typical SaaS.

## Layout
Sticky top nav on black: left logo, centered text links with chevron dropdowns, single white pill CTA right. Heroes are centered serif headlines (2 lines max) with a short sans subhead and one CTA; product pages pair a split hero with a color-flooded screenshot card. Section rhythm: centered serif section title → 3-column card grid or alternating text/screenshot rows; each product feature gets its own full-width color panel (red, green, blue, yellow) containing an angled or inset app screenshot. Recurring blocks: mono-tone logo strip, testimonial with avatar, 3-up blog card grid, centered "Start your 7-day free trial" inline form, and a footer with a giant ghosted "Spellbook" wordmark plus rainbow diamond logo.

## Components
- Buttons: pill shape throughout; primary is solid white with black label; secondary is dark gray (#2a2a2a-ish) pill with white label; small arrow-suffix subscribe buttons inside input bars.
- Cards: dark #1c1c1c panels, 8-14px radius, no visible border or shadow, colored line-icon + centered heading + muted gray body; blog cards are image-top with plain text below (no card chrome).
- Inputs: dark filled fields with subtle 1px border, small radius, light placeholder; select with chevron; search bar full-width pill-ish field with magnifier icon.
- FAQ accordions: thin divider rows with plus icons.
- Keyboard-key chips ("Ctrl + C") rendered as small bordered tags.

## Signature
- Serif display type on a near-black canvas — headlines never use the sans.
- Full-bleed feature panels in flat saturated brand colors (red-orange, green, blue, yellow, purple) framing product screenshots.
- Doodled ribbon/squiggle strokes in brand colors scattered over dark panels.
- Footer with oversized translucent "Spellbook" wordmark and multicolor diamond logo.
- White pill CTA as the one high-contrast action everywhere.

## Do / Don't
Do:
- Set all headings in the serif at regular weight; reserve the grotesque sans for UI, labels, and body copy.
- Use one flat brand color per feature section as a full-bleed background, with the screenshot inset on it.
- Keep the primary CTA a white pill with black text; use dark gray pills for secondary actions.
- Render logo strips and testimonials in monochrome white/gray so the accent colors stay reserved for panels and icons.
- Use thin hairline dividers and plus-icon accordions for dense info (FAQ, security).

Don't:
- Don't use gradients, glows, or glassmorphism — every surface here is a flat fill.
- Don't color links or CTAs with the accent hues; accents are for backgrounds, icons, and squiggles only.
- Don't add borders or drop shadows to cards; separation comes from the #1c1c1c-on-#111 value step.
- Don't use bold-weight or all-caps display type; the serif stays calm, sentence case, tightly leaded.
- Don't mix multiple accent colors inside one section (outside the deliberate confetti/squiggle motifs).
