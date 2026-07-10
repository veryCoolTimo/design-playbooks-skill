---
name: shopify-design
kind: site
style: ML
category: design-agency-showcase
website: https://shopify.design/
pages: [home, work-gallery]
palette:
  canvas: "#ffffff"
  ink: "#0a0a0a"
  primary: "#0a0a0a"
  accents: ["#d3e520", "#e8e5e0", "#101010"]
typography:
  display: "SF Pro / Inter-class neo-grotesque · medium-to-regular at huge sizes · tight, near-zero tracking"
  body: "Same neo-grotesque family, regular weight, quiet gray-black"
radius: "large 16px+ on cards and media tiles; pill on small chips/badges (e.g. the Sidekick pill, reply inputs)"
---
## Overview
A stark white portfolio canvas that lets curated work samples carry all the color. The page itself is almost content-free chrome: enormous single words ("Make") and a scrolling masonry of rounded media cards — phone mockups, product shots, motion stills — floating in generous whitespace. Black and warm-gray card fills alternate with punchy artifacts like chartreuse blocks and prismatic glitch/light-leak imagery, so the neutral shell reads deliberate rather than empty.

## Layout
No persistent nav visible in the captured viewports; the experience is a long vertical scroll gallery. Content sits in a loose 3-column masonry grid of large rounded cards with uneven vertical offsets, cards frequently bleeding off the left and right viewport edges. Rhythm alternates dense card clusters with near-empty white stretches and one oversized display word. A small pill-shaped 3D capsule ornament floats in the lower-right corner and persists across scroll like a mascot/scroll companion. A glitchy full-bleed prismatic transition sequence (RGB light-leak, checker fragments, lime blocks) interrupts the calm gallery mid-page.

## Components
Cards: large radius (roughly 16–24px), no visible borders, no drop shadows; fills are flat white, warm gray (#e8e5e0), light gray (#dedcd9), or near-black (#0a0a0a); media sits inside or fills the card. Product cards embed small circular icon buttons (arrow-in-circle, heart) as white/neutral discs. Chips and quick-reply buttons inside phone mockups are pill-shaped with light gray fills. Inputs seen (search, reply) are pill/rounded fields with pale fills and no hard borders. No conventional marketing CTA button appears in these screens — interactive affordances are circular icon buttons and pills; primary defaults to the site's black.
## Signature
- Oversized single-word display type ("Make") set in a plain neo-grotesque at hero scale on bare white.
- Masonry of big, borderless, shadowless rounded cards that bleed off the viewport edges, mixing warm-gray, white, and black fills.
- Chartreuse/lime (#d3e520) used sparingly as the only saturated brand pop against the neutral shell.
- Prismatic glitch/light-leak transition imagery and a floating 3D pill capsule as playful counterweights to the minimal chrome.

## Do / Don't
Do:
- Keep the page shell pure white and let imagery inside cards supply all color.
- Use large-radius cards with flat fills (warm gray, black, white) and zero borders or shadows.
- Set headings as very large, plainly weighted grotesque words with tight tracking — scale, not weight or color, carries hierarchy.
- Vary card heights and let the masonry crop at viewport edges; leave big empty white gaps between clusters.
- Reserve the lime accent for small blocks/artifacts, not for buttons or text.

Don't:
- Add drop shadows, outlines, or gradients to cards — everything is flat.
- Introduce a saturated multi-color palette in the chrome; saturation lives only inside curated work imagery.
- Use decorative serif or display faces — the type voice is one neutral grotesque throughout.
- Center everything into a rigid symmetric grid; the layout depends on offset, asymmetric card placement.
- Crowd the layout — sections with a single word or a single card in a sea of white are the norm, not a bug.
