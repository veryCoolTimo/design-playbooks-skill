---
name: paper
kind: site
style: DT
category: design-saas
website: https://paper.design/
pages: [home, roadmap, build-log/changelog]
palette:
  canvas: "#050505"
  ink: "#E8E8E6"
  primary: "#F7F6F0"
  accents: ["#4C7DF5", "#F5A83C", "#8E8CF5"]
typography:
  display: "modern neo-grotesque (Söhne/Diatype-like) · regular-to-medium, lowercase-set · near-normal tracking"
  body: "same neo-grotesque at small sizes; muted gray secondary text"
radius: "small 2-6px on buttons; cards and panels near-square (0-2px) with 1px hairline borders"
---
## Overview
Near-black, design-tool-native aesthetic: the marketing site is styled like the canvas of the product itself. Hairline 1px borders, dashed guide lines, crop marks, and selection-handle motifs divide sections instead of color blocks. Type is a lowercase-set neo-grotesque in off-white on black, with color reserved for tiny functional accents (logo blue, comment-pin amber/lavender) and rich gradient artwork inside framed screenshots.

## Layout
Sparse top nav: small logo left, three lowercase text links right ("roadmap", "build log", "open app →"). Hero is left-aligned lowercase headline in two tones (white first line, gray continuation), a single small solid CTA plus a plain text link, then a large app screenshot. Sections are boxed by hairline borders on the black field, forming a visible grid; generous vertical padding between them. Roadmap page uses a two-column card grid of feature entries with status pills; build log is a single-column chronological feed of framed images plus bulleted release notes. Footer repeats nav columns above a giant cropped "Paper" wordmark bleeding off the bottom edge.

## Components
Buttons: small, solid off-white (#F7F6F0) fill with black text, slight 2-4px rounding, no shadow ("get started", "view the roadmap", "try it out"). Secondary actions are bare lowercase text links with a trailing arrow. Cards: square-cornered panels outlined in 1px dark-gray hairlines, dark #0A-0F fills, image on top, small heading + gray body + arrow link below. Status pills on roadmap cards are tiny outlined lowercase chips ("in progress", "planned", "coming soon"). Floating comment bubbles with colored cursor dots (amber, blue, lavender) mimic multiplayer design-tool annotations.

## Signature
- Marketing pages dressed as the design tool: selection handles, dashed guides, rulers, layer panels, and comment pins used as page decoration.
- Pure-black canvas with 1px hairline section framing instead of background color changes.
- Lowercase everywhere — headlines, nav, buttons, pills.
- Giant cut-off "Paper" wordmark filling the footer.
- Color lives in embedded artwork (gradients, CMYK halftone florals) while the chrome stays monochrome.

## Do
- Keep the page chrome strictly monochrome (black, grays, off-white) and let screenshots/artwork carry all saturated color.
- Frame every section and card with 1px hairline borders; use dashed lines, crop marks, and cursor/comment motifs as decoration.
- Set headlines, nav, buttons, and labels in lowercase; use white-vs-gray tone shifts within a headline for emphasis.
- Use one small solid off-white CTA per view, paired with plain arrow text links for secondary actions.
- Show real product UI large and early — hero screenshot directly under the headline.

## Don't
- Don't introduce colored buttons, gradient CTAs, or brand-blue fills — the only solid button color seen is off-white.
- Don't round cards or panels; corners stay square with hairline outlines, and buttons stay at subtle 2-4px.
- Don't add drop shadows, glows, or elevation — separation is done purely with borders on black.
- Don't use title case or bold display weights; the voice is quiet, lowercase, regular-weight.
- Don't fill sections with alternating background colors; the canvas remains near-black end to end.
