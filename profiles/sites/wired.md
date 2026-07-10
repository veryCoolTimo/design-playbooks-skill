---
name: wired
kind: site
style: BT
category: media
website: null
pages: [home, article]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#000000"
  accents: ["#057dbc", "#757575", "#e0e0e0", "#f5f5f5"]
typography:
  display: "WiredDisplay (tall narrow high-contrast serif; sub Playfair Display) · regular 400 · tight negative tracking"
  body: "BreveText humanist serif (sub Lora/Source Serif) for articles; Apercu sans (sub Inter) for labels"
radius: "none"
---
## Overview
A print magazine translated to the screen with almost no web-marketing chrome: pure white canvas, pure black ink, and giant serif headlines doing all the work. Identity lives entirely in type — a proprietary condensed didone-style display serif at up to 64px, a humanist serif for reading, a clean sans for structure. Color is deliberately absent; the sole hue is a blue reserved for inline article links.

## Layout
Thin masthead band with the wordmark centered and section links flanking it; hamburger + Subscribe at the edges on mobile/desktop respectively. Home opens with a full-bleed cover story (16:9 image, 64px serif headline), followed by a 2-up secondary grid, then a single-column stack of bylined story rows split by 1px #e0e0e0 hairlines. Wide ~1400px container, 4px spacing base, 48px section padding. Everything sits flat on the white canvas — no bands of alternating background in the main rhythm.

## Components
Buttons are sharp 0px rectangles: solid black with white Apercu 16/700 labels for primary, white with a 1px black border for the outline variant. The only circle in the system is the social-share icon button and avatar crops. Inputs are square with a 1px black border on white. Cards are borderless and shadowless — a photo plus stacked type on bare canvas; story rows get hairline bottom borders. Elevation is done with borders, never shadows (a 2px black border is the "heavy" level). Footer is a full black band with white sans text. Bylines: small circular avatar, gray #757575 bold serif at ~12.7px with very tall line-height.

## Signature
- The tall, narrow, high-contrast display serif at weight 400 — recognizable before you read a word
- Absolute black/white duet; the only color on the page is #057dbc inline links in article body
- Zero border-radius on every interactive element; zero drop-shadows anywhere
- Three-typeface ladder with strict roles: display serif for headlines, text serif for prose, sans for nav/meta/buttons

## Do / Don't
**Do**
- Keep black for everything brand-level: wordmark, CTAs, footer fill, heavy borders
- Set hero headlines at 64px weight 400 in the display serif with negative tracking and sub-1.0 line-height
- Separate story rows with 1px #e0e0e0 hairlines — that is the entire elevation system
- Hold typeface roles strict: serif never on buttons/nav, sans never in article prose
- Use square corners on all buttons, inputs, and cards; circles only for avatars and share icons

**Don't**
- Don't add a chromatic accent — #057dbc belongs only to inline article links, never buttons or nav
- Don't round corners on any interactive element
- Don't apply drop-shadows to cards or modals in the page rhythm; use hairline or 2px black borders
- Don't bold the display face past 400 — its elegance comes from the letterform contrast, not weight
- Don't swap the display serif for a sans headline; the serif voice is the brand
