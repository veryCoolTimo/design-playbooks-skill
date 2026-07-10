---
name: aninix
kind: site
style: ML
category: design-tools-saas
website: https://www.aninix.com/
pages: [home]
palette:
  canvas: "#F0F0F2"
  ink: "#17171B"
  primary: "#17171B"
  accents: ["#3D4FE0", "#FFE014", "#FCFCFD"]
typography:
  display: "geometric grotesque with techy cut terminals (Space Grotesk-like) · bold · tight"
  body: "neutral grotesque (Inter/Graphik-like)"
radius: "buttons small 4-6px; cards medium 8-14px"
---
## Overview
A stripped-down, near-monochrome landing page on a cool light-gray canvas where the product's own output does all the visual work. Huge black centered headlines alternate with masonry-style grids of animation preview cards, each card carrying its own internal color world (dark fintech UI, yellow illustration, cream editorial). Chrome is minimal: one dark pill of a nav CTA, tiny link labels, no decorative shapes or gradients on the page itself.

## Layout
Slim top nav: logo left, three text links (Features, Pricing, Wiki) plus a solid black "Install plugin" button right, on a white bar over the gray body. Hero is fully centered: two-line display headline, one-sentence subhead, single black CTA button with a "19k installs and counting" microcopy line under it. Sections follow a strict rhythm: oversized centered H2 (often 2-3 lines) -> irregular grid of showcase cards in mixed aspect ratios and widths, generous vertical gaps between sections. Closing section repeats the headline + CTA pattern. Footer is a single sparse row of small links left, social icons right.

## Components
- Buttons: solid near-black fill, white label, small radius (~4-6px), often prefixed with the Figma logo mark; no visible border or shadow. Same button reused in nav, hero, and closing CTA.
- Showcase cards: medium-rounded rectangles containing full-bleed animation stills; no border, no drop shadow — they sit flat on the gray canvas and read via their own contrasting fills.
- Attribution badges: tiny blue (#3D4FE0) rounded tags ("by Aninix") pinned to the bottom-left inside cards; third-party works get neutral text credits below the card instead.
- No inputs, no icon rows, no testimonial widgets visible.

## Signature
- Editorial-scale centered headlines written as conversational sentences ("Hard to believe these animations were actually made in Figma?" ... "They were. With Aninix. Excited?") that carry the narrative across sections.
- Grayscale page shell with all color delegated to the showcase cards — the vivid yellow illustration tile and dark dashboard tile pop precisely because the frame is neutral.
- Blue "by Aninix" badge as a recurring provenance stamp on the work samples.
- One CTA, repeated verbatim ("Install plugin" with Figma mark), always as a black button.

## Do / Don't
Do:
- Keep the page shell to gray canvas + black ink and let embedded work samples supply every accent color.
- Set headlines huge, bold, centered, and phrased as a question-answer dialogue between sections.
- Use a single black small-radius CTA with the platform logo inline, and repeat it top, hero, and bottom.
- Vary showcase card widths and aspect ratios in a loose grid rather than a uniform 3-up.
- Stamp product-made samples with a small colored attribution badge inside the card corner.

Don't:
- Add drop shadows, borders, or gradients to cards or buttons — everything sits flat.
- Introduce a colored primary button or link-styled CTAs; the CTA is always solid black.
- Fill the space between sections with feature grids, icons, or testimonial blocks — the rhythm is headline, proof, headline.
- Use large pill radii; corners stay modest (buttons ~4-6px, cards under ~14px).
- Left-align hero copy or headlines — the whole narrative column is centered.
