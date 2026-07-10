---
name: endlesstools
kind: site
style: DN
category: creative-saas
website: https://endlesstools.io/
pages: [home]
palette:
  canvas: "#1e1e1e"
  ink: "#bbbbbb"
  primary: "#efefef"
  accents: ["#fe80ba", "#1780fe", "#98c647"]
typography:
  display: "Inter-like neutral grotesque · regular-to-medium weight · tight, near-default tracking"
  body: "Same neutral grotesque (Inter/Helvetica family), small sizes in mid-gray"
radius: "pill on buttons; medium 10-14px on inputs; large 16px+ on media tiles and feature panels"
---
## Overview
A near-monochrome charcoal interface that acts as a gallery frame: the UI itself is grayscale (#1e1e1e canvas, white headings, gray copy, off-white pill buttons) while all color arrives through dense, hyper-saturated 3D renders — hot pink, electric blue, acid green, iridescent chrome. The chrome-vs-content contrast is the whole idea: quiet type, loud imagery. Headings are set at regular weight rather than bold, giving an understated, tool-like tone.

## Layout
Minimal top bar: small two-line wordmark top-left, a single "Log in / Sign in" pill top-right — no visible nav links. Hero is centered text (heading, two-line subcopy, one pill CTA) followed by a full-width rounded media banner. Section rhythm repeats: tiny uppercase eyebrow label, centered regular-weight heading, short gray subcopy, optional pill button, then imagery. Imagery blocks alternate between a masonry/mosaic gallery of mixed-size tiles, a 4-up card row of tool categories, and zig-zag feature rows (rounded image panel on one side, heading + copy + button on the other). Page closes with an oversized left-aligned display heading ("Stay tuned...") beside a stacked waitlist form, then a sparse one-line footer. Generous vertical whitespace between sections; content held in a fairly narrow centered column.

## Components
Buttons: off-white (#efefef) pill with dark text for every CTA at every level — hero, section, feature rows, form submit; small and unassuming rather than oversized. No colored or gradient buttons anywhere. Cards: media tiles with large (~16px+) radius, no borders, no shadows — the artwork is the card. Tool-category cards are tall rounded image panels with overlaid icon + label and caption text below. Inputs: dark fields matching the canvas with a subtle 1px lighter border, medium radius, gray placeholder text; select uses a chevron; circular checkbox with underlined Privacy Policy link. Small floating dark tooltip/control panels (Softness, Scale, Roughness sliders) appear on top of imagery to suggest the editor UI.

## Signature
- Grayscale UI shell where 100% of the color comes from saturated 3D artwork (pinks #fe80ba, blues #1780fe, acid greens)
- Every CTA is the same small off-white pill — one button style, repeated, never colored
- Regular-weight (not bold) display headings, mostly centered, with tiny uppercase eyebrow labels
- Mosaic gallery of mixed-size rounded tiles as the main proof-of-product section
- Floating mini control panels (sliders) overlaid on renders to hint at the tool

## Do / Don't
Do:
- Keep the UI strictly grayscale (#1e1e1e / white / grays) and let imagery carry all saturation
- Use one off-white pill button style for every CTA, sized modestly
- Set display headings in regular weight with tight tracking; pair with small mid-gray subcopy
- Round all media containers generously (16px+) with no borders or shadows
- Precede each section heading with a tiny uppercase gray eyebrow label

Don't:
- Add colored, gradient, or glowing buttons — the site never uses accent color in UI chrome
- Bold or uppercase the main headings; the voice is quiet, weight comes from imagery
- Put borders, shadows, or glass effects on cards; tiles are flat cutouts of artwork
- Fill the header with nav links or mega-menus; the top bar stays nearly empty
- Use pure black (#000) or pure-white body copy; canvas is soft charcoal and copy is muted gray
