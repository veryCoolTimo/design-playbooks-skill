---
name: eclipse
kind: site
style: BT
category: crypto-infrastructure
website: https://www.eclipse.builders/
pages: [home, how-it-works, careers, news, resources]
palette:
  canvas: "#EDECE8"
  ink: "#111111"
  primary: "#0E0E0E"
  accents: ["#FF4B00", "#E4FC54", "#151B3B", "#6B74B2", "#7EA189", "#EFC9CB", "#D9D6BB", "#F2A93B"]
typography:
  display: "Neue Haas Grotesk / Helvetica Now style neo-grotesque · medium-bold · tight, slightly negative tracking"
  body: "Same neo-grotesque family, regular weight, small size, normal tracking"
radius: "mixed — pill buttons/inputs (fully rounded); cards and sections have no radius (hard 90° edges); diagram nodes large 16px+"
---
## Overview
Eclipse is a big-type, color-blocked Swiss-grotesque site where each page runs its own two-to-three-color theme (orange/black/cream on home; navy/chartreuse on careers; periwinkle/khaki on resources; khaki/sage/black/amber on news). Full-bleed rectangular color bands stack vertically with zero gaps, no shadows, no gradients. The signature move is the wordmark "eclipse" set so large it bleeds off both edges of the viewport in the hero and footer.

## Layout
Top nav is a minimal 3x2 grid of small text links at top-right, each with a thin rule above it; a dotted-circle "eclipse" logomark sits top-left. Heroes are either a viewport-cropped giant wordmark/page-title (home, news, resources) or a plain statement headline on a colored band (careers, how-it-works). Sections are alternating full-width color slabs, frequently split into a 50/50 two-column grid: big heading left, supporting copy or a list right. Rhythm comes from color changes, not whitespace; blocks butt directly against each other. A repeated "Sign up for our testnet" email-capture band appears mid-page and pre-footer on every page. Footer = giant clipped wordmark over a color band with a row of small social links.

## Components
Buttons: fully rounded pill "Submit," solid fill (black most often; recolored per page theme — periwinkle on resources, sage on news), white or light label, no border, no shadow. Inputs: white pill email field with placeholder "name@company.xyz," paired inline with the Submit pill. Cards: none in the traditional sense — content sits in flat color rectangles; benefit items on careers use a thin top rule + bold title + small gray body. FAQ accordions on resources are black rows with chevrons and thin dividers. Diagram nodes (how-it-works) are large-radius rounded rectangles / pills stacked with arrows. Links are small text with an outward ↗ arrow glyph; list items use ↗ or • bullets.

## Signature
- Wordmark set at viewport-overflowing scale, cropped by the screen edges, in hero and footer of every page.
- Per-page color theme swap: same layout system, entirely different 2–3 color palette per page.
- Thin horizontal rules above nav links and section list items; grid feels like a printed spec sheet.
- Dotted-circle logomark (ring of dots) and a rotating "think of the possibilities" circular-text badge.

## Do / Don't
**Do**
- Compose pages as stacked full-bleed color slabs; change background color to mark a new section instead of adding vertical whitespace.
- Set the brand wordmark or page title so large it clips off the left and right viewport edges.
- Keep exactly one recurring CTA pattern: white pill email input + solid pill Submit button, restyled to the section's theme.
- Use 50/50 split sections: oversized grotesque heading on one side, small dense body copy or ruled list on the other.
- Recolor the whole theme per page (orange, navy/chartreuse, periwinkle, khaki/sage) while keeping black and off-white as anchors.

**Don't**
- Don't add shadows, gradients, glassmorphism, or glows — every surface is flat solid color.
- Don't round cards or section containers; radius belongs only to pills (buttons, inputs, diagram nodes).
- Don't use more than one type family or decorative/serif display type — everything is the same neo-grotesque at different sizes.
- Don't center-align hero copy; headings sit hard left (or hard right) against generous asymmetric space.
- Don't box content in bordered cards — separate items with thin 1px rules and background-color changes instead.
