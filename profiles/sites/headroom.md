---
name: headroom
kind: site
style: BT
category: internal-tools-saas
website: https://headroom.com/
pages: [home, about]
palette:
  canvas: "#FAFAFA"
  ink: "#171717"
  primary: "#213CFF"
  accents: ["#A3A3A3", "#2C50FE", "#FFFFFF"]
typography:
  display: "SF Pro / Helvetica-style neo-grotesque · black to bold · tight, near-default tracking"
  body: "Same neo-grotesque (SF Pro / Inter feel), regular weight"
radius: "buttons medium 8-12px; cards large 16px+"
---
## Overview
A two-tone big-type system: near-white pages punctuated by full-bleed electric-blue (#213CFF) sections, with the about page rendered entirely on blue. Massive all-caps or sentence-case grotesque headlines carry the message; imagery is limited to product screenshots and distinctive scanline/dither pixel illustrations drawn in white or blue horizontal strokes. The effect is loud, flat, and almost brutalist despite soft corner radii.

## Layout
Slim top nav: wordmark left, two text links, Login + blue "Get access now" button right; nav pills sit on whatever background the page uses (white on blue for about). Home hero is centered stacked type ("RUN ON AUTOPILOT") with a pixel-runner figure woven behind the letters, dual CTAs, an inline email field, and a large product screenshot below. Sections alternate white and full-bleed blue bands; mid-page features use a "small heading left, three icon blurbs right" split, followed by floating UI-card collages. A ghost-gray (#A3A3A3) giant all-caps type block ("EVERYTHING YOU NEED...") acts as a mid-page divider. About is a single narrow centered text column (~500px) on solid blue, ending in a scanline landscape illustration. Generous vertical whitespace throughout; footer repeats the page's background color.

## Components
- Primary button: solid #213CFF fill, white label, ~10px radius, no shadow, no border. On blue backgrounds it becomes a white/light-tinted version of the same shape.
- Secondary button: #F0F0F0 light-gray fill with a hairline border, dark label, same radius.
- Email input: full-width, medium radius, on blue it is a translucent lighter-blue (#4061FE) fill with a 1px lighter border and low-contrast placeholder; disabled submit renders as a faint tonal blue block.
- Cards: large-radius (16px+) tonal panels — lighter blue (#2C50FE) on blue, white with hairline gray borders on light sections; flat, shadowless feature-grid cells.
- Small uppercase pill tag ("MANIFESTO") with thin outline used as a section eyebrow.

## Signature
- Single electric blue #213CFF used at full bleed — entire about page and whole home sections are painted with it, no gradients.
- Scanline/dithered pixel illustrations (running figure, landscape, envelope icon) built from horizontal white bars.
- Oversized grotesque display type, including a ghost statement set in flat #A3A3A3 on white.
- Everything flat: no drop shadows, no gradients, hairline borders only.

## Do / Don't
Do:
- Use #213CFF as a surface color for whole sections/pages, not just for buttons and links.
- Keep long copy in a narrow centered column with white text when on blue.
- Build tonal hierarchy on blue with lighter-blue fills (#2C50FE, #4061FE) instead of white cards.
- Render illustrative art as pixel/scanline line-work in a single color.
- Let one giant gray all-caps type block serve as a section in itself.

Don't:
- Add gradients, drop shadows, or glassmorphism — every surface here is flat.
- Introduce a second brand hue; the palette is strictly blue + near-black + grays.
- Use pill-shaped buttons; corners are moderate rounded rects (~10px).
- Put photography anywhere — only UI screenshots and pixel illustrations appear.
- Set headlines in serifs or light weights; display type is heavy grotesque, often all-caps.
