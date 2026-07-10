---
name: x-advertising
kind: site
style: ML
category: advertising-platform
website: https://business.x.com/en/advertising
pages: [landing]
palette:
  canvas: "#ffffff"
  ink: "#3d3d3d"
  primary: "#000000"
  accents: ["#f2f2f0", "#8a8a8a", "#e5e5e5"]
typography:
  display: "Chirp (X house grotesque, close to Helvetica Now/Inter) · regular-to-medium weight, oversized · tight, near-zero letter-spacing"
  body: "Chirp / neo-grotesque sans, regular weight, gray #536471-ish"
radius: "pill buttons; none on cards/panels (sharp 0px corners)"
---
## Overview
A monochrome, near-brutalist minimal-light system: pure white canvas, black type, and thin-line geometric schematics (circles, dashed orbits, plotted nodes) standing in for all imagery. Headlines use a two-line pattern — first line black, second line gray — at large regular weight. The only color contrast in the entire page is black vs. gray vs. one dark testimonial panel; zero brand hues.

## Layout
Fixed left sidebar nav (thin gray text links, active item bold, chevrons for expandable groups) with the X glyph top-left and stacked pill buttons (black "Create Ad", outlined "Sign In") pinned bottom-left. Content column starts around 1/5 of viewport width. Sections are tall and airy with huge vertical gaps; hairline 1px gray rules separate sections and top each feature column. Features sit in a 3-4 column grid with staggered/offset placement — text blocks and line-art diagrams alternate rows rather than aligning uniformly. Stats appear as staggered gray tiles at varying vertical offsets, masonry-like. A numbered stepper (01–04) with underline-active state drives a campaign walkthrough carousel with bare chevron arrows.

## Components
- Buttons: solid black pill with white text for primary CTAs ("Get started", "Claim Credits", "Create your Ad"); secondary is light gray (#efefef) pill with black text ("Talk to an Ads expert"); Sign In is a white pill with 1px gray border. No shadows, no gradients.
- Cards: flat light-gray (#f2f2f0) rectangles with zero radius and no border or shadow; stat cards lead with a huge black figure (85%, 4.74x) over small gray copy. One inverted card: near-black panel with white quote text and faint watermark logo.
- Diagrams: 1px black/gray stroke line art — intersecting circles, dashed ellipses, node-and-square plots — with small bordered white label chips ("Where ideas move forward.").
- Stepper tabs: number + label over a hairline; active tab gets a black underline and black text, inactive stay gray.

## Signature
- Technical-drawing line art (circles on an axis, dashed orbits, plotted nodes) instead of photos or color illustration.
- Two-tone headline device: black first line, mid-gray second line, both large and regular weight.
- Everything grayscale — the "palette" is literally white, grays, and black; the black pill CTA is the loudest element on the page.
- Sharp-cornered flat gray panels against pill-shaped buttons: the only two radius values in the system.

## Do / Don't
Do:
- Keep the canvas pure white and reserve solid black exclusively for CTAs, headline first-lines, and big stat figures.
- Use the black-line/gray-line two-row headline pattern for every section title.
- Draw supporting visuals as 1px monochrome schematics (circles, dashed paths, nodes) inside flat #f2f2f0 rectangles.
- Separate sections with hairline gray rules and generous (150px+) vertical whitespace; let grid items stagger vertically.
- Use pill shape for all buttons and 0px radius for all containers.

Don't:
- Introduce any hue — no blue links, no colored icons; the system is strictly grayscale.
- Add shadows, gradients, or borders to cards; panels are flat fills only.
- Round card or panel corners; radius belongs to buttons alone.
- Use bold/heavy display weights; headlines stay regular-to-medium and get presence from size, not weight.
- Fill layouts edge-to-edge; the design depends on large empty zones and offset, non-uniform column starts.
