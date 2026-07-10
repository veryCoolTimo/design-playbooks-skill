---
name: prismic
kind: site
style: ML
category: dev-tools-cms
website: https://prismic.io/
pages: [home, product, pricing, blog, showcase, developers-landing, agencies-landing]
palette:
  canvas: "#FFFFFF"
  ink: "#151515"
  primary: "#151515"
  accents: ["#8E44EC", "#ED6B22", "#75DCC0", "#F1E1FF", "#FDEEE1", "#F1806E"]
typography:
  display: "geometric grotesque (Gilroy/Aeonik-like) · bold 700 · tight, near-zero tracking"
  body: "same grotesque family, regular 400, small size with generous line-height"
radius: "small 2-6px on buttons; medium 8-12px on cards and image frames"
---
## Overview
A stark black-on-white marketing system energized by playful 3D isometric illustrations of stacked "slices" — colorful outlined blocks in purple, orange, mint, pink, and blue. Chrome is monochrome (black text, black CTAs, thin black borders) so all color lives in the artwork and pastel section fills. Full pages flip polarity: light pages carry heavy near-black (#151515) sections, and the developer/product pages invert to an almost fully dark canvas with the same components.

## Layout
Slim sticky white nav: logo left, centered dropdown links, then Login + a ghost CTA + a solid black "Start Building" button. Heroes are either left-aligned two-column (copy left, isometric illustration right) or centered single-column (pricing, showcase, blog). Sections alternate in wide rounded-corner bands: white → pastel (lavender/peach) → near-black community band → pastel closing CTA band → black footer. Home uses stacked two-column feature rows (bordered text card + illustration card); product pages use a 4-step numbered card row and 2-3 column feature-card grids on dark. Blog is a dense card grid with horizontal topic carousels. Generous vertical padding, content max-width around 1200px.

## Components
Buttons: small-radius (~4px) rectangles; primary is solid #151515 with white text, secondary is white with a 1px black border; on dark sections they invert to white fill/black text. Text links are underlined. Cards: white with 1px black or light-gray borders and ~8-12px radius, flat with no shadows; dark cards (#1E1E1E-ish) on dark pages. Testimonial blocks: lavender (#F1E1FF) or black panels with large italic quote text, avatar, name, and small circular prev/next arrow buttons. Pricing: four bordered plan cards with oversized dollar figures, a black-fill pill Monthly/Annually toggle with purple knob, and a huge comparison table with a sticky black organizations header. Newsletter input: simple white field with black submit button on a black band. Blog category chips: white pills with 1px border and small colored icons.

## Signature
- 3D isometric "slice stack" illustrations everywhere: flat-color blocks with crisp black outlines in purple/orange/mint/pink, sometimes tiling into full-bleed patterns (grayscale when used as a dark background texture).
- Strict monochrome UI chrome — black CTAs, black borders, black footer — with color reserved exclusively for illustration and pastel band fills.
- Alternating full-width rounded bands: white, lavender #F1E1FF, peach #FDEEE1, and near-black, giving pages a striped rhythm.
- Whole-page polarity flips: the same design runs light (home, pricing, blog) and fully dark (developers, product) without changing component shapes.

## Do / Don't
Do:
- Use a solid near-black (#151515) fill for every primary CTA and a 1px-black-border white button for secondary, inverting to white-on-dark sections.
- Keep the interface monochrome and inject color only through illustrations, small category icons, and pastel section backgrounds.
- Frame content in flat 1px-bordered cards with 8-12px radius — no drop shadows anywhere.
- Break long pages into full-width alternating bands (white / lavender / peach / black) with big rounded corners on inset panels.
- Set headlines in a heavy geometric grotesque with tight tracking, left-aligned in heroes with the illustration on the right.

Don't:
- Don't use colored or gradient buttons — brand purple #8E44EC appears in illustrations and toggles, never as a CTA fill.
- Don't add shadows, glassmorphism, or photographic hero backgrounds; imagery is flat outlined 3D vector art (photos appear only for community/testimonial people).
- Don't use pill-shaped or large-radius buttons; corners stay tight (~4px).
- Don't introduce serif or script faces — the entire system is one grotesque family, with italics of it reserved for quotes.
- Don't let dark sections use pure #000; surfaces sit at soft near-blacks (#151515-#1E1E1E) with subtle lighter card layers.
