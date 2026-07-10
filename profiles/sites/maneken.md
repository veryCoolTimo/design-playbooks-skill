---
name: maneken
kind: site
style: BT
category: design-tools
website: https://maneken.app/
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#000000"
  primary: "#0251B8"
  accents: ["#0F151A", "#F6F6F6"]
typography:
  display: "Neue Haas Grotesk / Helvetica Now feel · bold-to-black · tight, slightly negative tracking"
  body: "Same grotesque family, regular weight, generous size"
radius: "medium 8-14px on buttons and image cards; large 16px+ on full-bleed section blocks"
---
## Overview
Swiss-modernist, type-first landing page: enormous black grotesque headlines on white, alternated with full-bleed flat cobalt (#0251B8) and near-black (#0F151A) section blocks with rounded corners. Photography does the product storytelling — real-world street photos of murals, posters, and signage serve as live mockup examples. Almost no decoration: no gradients, no illustrations, no shadows; contrast and scale carry everything. Note: despite EL metadata, the screenshot shows zero serifs — this is bold-grotesque territory.

## Layout
Sparse top nav: wordmark left ("MANEKEN" + blue dot), only "Log in" text link and a blue "Sign up" button right. Hero is centered stacked type — two-line H1 at roughly 120px, one-line subhead, single blue CTA — followed by a full-width photo, then a dark app-UI screenshot of the editor itself. Section rhythm alternates canvas color per block: white → light gray (#F6F6F6) → cobalt blue → white masonry photo grid → near-black → white → black footer. Inside colored blocks, headlines sit huge and left-aligned at the top; feature rows pair left-aligned copy with right-offset photo cards. Masonry/collage grids of user photos ("We got you covered", "Our creators") act as proof sections. Footer is black with three small link columns and a repeat of the wordmark.

## Components
Buttons: solid #0251B8 fill, white label, medium radius (~10px), compact padding, arrow glyph after CTA labels ("Join the waitlist →"); no visible outline or shadow. Only two button treatments seen: blue solid and plain text link ("Log in"). Cards are borderless photos with medium rounded corners — no chrome, no shadow, no caption bars. The editor screenshot is presented as a dark rounded panel with its real toolbar UI. Small circular avatar/color dots appear as inline accents. No form inputs visible on the page; signup section is a black block with heading, blue CTA, and social icons.

## Signature
- Massive tight-set grotesque headlines (hero and section titles fill most of the viewport width) with sentence case.
- Full-bleed rounded-corner color-block sections in exactly one saturated cobalt blue plus near-black — no secondary hues anywhere.
- Street-photography mockup collages (the recurring blue "JIN" figure poster) doubling as product demo and portfolio.
- On the blue block, subheads drop to a lighter tint of the background blue instead of gray ("And yet so simple").

## Do / Don't
Do:
- Set headlines huge (site-title scale) in a bold grotesque with tight tracking, black on white or white on blue.
- Keep one primary color: #0251B8 for every CTA and the blue accent dot in the wordmark.
- Alternate full-width section backgrounds (white / #F6F6F6 / #0251B8 / #0F151A) with visible rounded corners between blocks.
- Let real photographs carry visual interest; place them as borderless rounded rectangles or masonry grids.
- Keep nav to a bare minimum: logo, one text link, one button.

Don't:
- Introduce serifs, script faces, or a second accent color — the palette is strictly blue/black/white/gray.
- Add shadows, gradients, borders, or glassmorphism; every surface is flat.
- Use icon-heavy feature grids; features are told with short copy blocks next to photos.
- Center-align body copy inside colored sections — inside blocks everything is left-aligned (only the hero and small section intros are centered).
- Shrink CTAs into ghost/outline variants; buttons are always solid blue.
