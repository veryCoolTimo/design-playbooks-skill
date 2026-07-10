---
name: react-email
kind: site
style: DT
category: dev-tools
website: https://react.email/
pages: [home, components-gallery, templates-gallery]
palette:
  canvas: "#000000"
  ink: "#a1a1aa"
  primary: "#ffffff"
  accents: ["#22d3ee", "#0891b2", "#18181b"]
typography:
  display: "Inter-style neo-grotesque · medium-to-semibold · tight tracking"
  body: "Inter-style neo-grotesque"
radius: "pill buttons; medium 8-12px cards"
---
## Overview
Pure-black developer aesthetic where nearly everything is monochrome and one electric cyan does all the accent work. Content lives inside hairline-bordered dark cards on a #000 canvas; the hero adds a single glowing cyan 3D render for atmosphere. Real email screenshots (white) are the only bright surfaces, so light-mode content reads as the "product" floating on a dark stage.

## Layout
Slim top nav: logo left, three text links (Components, Templates, Docs) plus a GitHub star count right; active nav item gets a subtle dark pill highlight. Hero is left-aligned text (large heading, short gray paragraph, two CTAs) with a cyan blueprint-style 3D ribbon bleeding off the top-right edge. Below, sections alternate centered headings with generous vertical dead space between them — the page breathes through darkness, not dividers. Galleries use a tight 3-column (components) or 2-column (templates) card grid with thin gutters and faint full-height column rules framing the content area. Footer is a single centered "Brought to you by Resend" line.

## Components
Primary CTA is a white pill button with black text ("Explore components →", "Get Started"); the secondary CTA is a dark pill styled as a copyable terminal command (`npx create-email@latest`) with a 1px gray border. Small segmented toggles (Tailwind / CSS) use tiny dark pills with hairline borders. Cards are near-black (#0a0a0a–#111) panels with 1px low-contrast borders, ~8-12px radius, no shadows; component cards contain abstract wireframe previews built from gray blocks plus one cyan element, over a faint dot-grid texture. Template cards embed real white email screenshots with a dark caption bar (name + author avatar). A mock code editor window with traffic-light dots and syntax-highlighted code sits beside a live email preview.

## Signature
- True #000 background with hairline vertical rules bounding the content column, like a technical drawing.
- One cyan accent (#22d3ee family) reused everywhere: hero 3D render, card wireframe highlights, cursor callouts — never a second brand color.
- Abstract skeleton/wireframe illustrations (gray bars + one cyan bar) standing in for component previews, on dot-grid card backgrounds.
- White pill CTAs as the sole high-emphasis element; all other chrome stays within 2-3 steps of black.

## Do / Don't
Do:
- Keep the canvas true black and build hierarchy with #0a-#1a panel steps and 1px borders instead of shadows.
- Reserve cyan for tiny functional highlights (one bar, one button, one cursor) inside otherwise gray compositions.
- Use white pill buttons with black text for the primary action; style secondary actions as bordered dark pills or terminal commands.
- Let real product output (white email screenshots) provide the only large bright areas.
- Add texture sparingly: dot grids inside cards, hairline column rules, a single glowing 3D hero object.

Don't:
- Don't introduce gradients, colored section backgrounds, or a second accent color — the system is mono + cyan.
- Don't use drop shadows or heavy card elevation; separation comes from border and fill deltas.
- Don't fill cards with literal screenshots in the components gallery — previews are abstracted wireframes.
- Don't center the hero; it is left-aligned text with art bleeding off the right edge.
- Don't use large border radii on cards or square corners on buttons — cards stay ~8-12px, buttons stay pill.
