---
name: eraser
kind: site
style: DT
category: dev-tools
website: https://www.eraser.io/
pages: [home, product-landing, pricing, resources, use-case]
palette:
  canvas: "#0D0D0D"
  ink: "#C7C7C7"
  primary: "#FFFFFF"
  accents: ["#3D9EF5", "#7B5BF5", "#F5C518", "#3DBA5D", "#F04E30"]
typography:
  display: "tight bold grotesque (Inter Display / Helvetica Now feel) · heavy 700-800 · tight, near-negative tracking"
  body: "Inter-style neutral grotesque, 400, light gray on black; monospace for code and small footer labels"
radius: "small 2-6px on buttons; medium 8-14px on cards (highlighted pricing card ~16px)"
---
## Overview
Near-black developer canvas where the product itself provides the color: glowing diagram nodes in blue, purple, orange, pink, and green float on a #0D0D0D field. Chrome is monochrome — white headlines, gray body, white CTA buttons — while playful "multiplayer" garnish (named cursor chips, hand-drawn circles, yellow highlighter strokes) breaks the austerity. The result reads like a dark IDE with sticky notes on it.

## Layout
Slim top nav: logo left, dropdown links center-left, Log in + white "Try Eraser →" button right. Heroes are center-aligned: gradient or two-tone headline (blue-to-cyan on home, blue-to-purple on Eraser AI), one-line subhead, single white CTA, then a full-width product screenshot or embedded diagram card. Section rhythm alternates: colored eyebrow pill badge → centered H2 (often with one word highlighted, circled, or underlined in marker style) → 2-3 sentence intro → screenshot → 3-4 column icon+text feature row. Logo wall ("Trusted by leading engineering teams globally") sits in a thin-bordered box below the hero. Pricing uses a 3-card row with the middle Professional card outlined and tabbed in blue, followed by a long striped comparison table. Resources page is a left filter-rail (search + pill-tag facets) with a 3-column card grid. Decorative sticky-note chips and diamond shapes float in the outer margins on nearly every page.

## Components
Buttons: white fill, black text, small 4-6px radius, usually with a trailing "→"; secondary buttons are dark with a 1px gray border; the highlighted pricing CTA is solid blue (#2E9BF0-ish). Cards: very dark gray (#141414-#1A1A1A) on black with 1px low-contrast borders, 8-14px radius, no visible shadows — separation comes from border + slight fill lift. Eyebrow badges: small colored pill outlines or fills (green, blue, purple, pink, yellow) with icon + label. Filter tags: dark pills with 1px borders. Inputs: dark field with subtle border (resources search). Checkmark lists use small filled circular check icons. Testimonials are bordered dark cards, some with video thumbnails and red play buttons.

## Signature
- Diagram-as-hero: real product canvases with multicolored node boxes and connector lines are the primary imagery on every page, including a white diagram card contrasting the black page on use-case heroes.
- Multiplayer garnish: named cursor chips ("Lauren S.", "Heath D.") in orange/green/yellow scattered beside headlines, plus floating sticky-note chips ("Documents & Diagrams", "Diagram as Code").
- Marker annotations on typography: yellow highlight behind a word, hand-drawn ellipse around "your", italic underlined "better" — one annotated word per H2.
- Color-coded eyebrow pills that assign each section its own accent hue against otherwise monochrome chrome.

## Do / Don't
Do:
- Keep the page shell strictly monochrome (near-black canvas, white type, gray borders) and let diagrams/screenshots carry all saturated color.
- Use white small-radius CTA buttons with trailing arrows; reserve solid blue fills for a single emphasized element (e.g., the featured pricing tier).
- Open each section with a small colored pill badge, then a centered heavy-grotesque H2 with one marker-annotated word.
- Scatter light-hearted collaboration props (cursor name chips, sticky notes, diamond doodles) in margins to soften the dark-tech look.
- Border cards with 1px low-contrast strokes on slightly lifted dark fills; skip drop shadows.

Don't:
- Don't introduce light or colored section backgrounds — every page stays on the same near-black field end to end (only inline diagram cards may be white).
- Don't use gradient-filled or pill-shaped buttons; buttons here are flat, rectangular-ish, 4-6px radius.
- Don't apply the headline gradient to body copy or more than the hero H1.
- Don't over-color the UI chrome: nav, footer, tables, and FAQ are grayscale; accents live only in badges, annotations, and artwork.
- Don't use rounded playful illustration styles — imagery is literal product UI and node-and-wire diagrams, not abstract blobs or 3D renders.
