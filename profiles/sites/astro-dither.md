---
name: astro-dither
kind: site
style: DN
category: experimental-audiovisual
website: https://astrodither.robertborghesi.is/
pages: [entry-gate]
palette:
  canvas: "#070707"
  ink: "#f2f2f2"
  primary: "#0a0a0a"
  accents: ["#f767ae", "#8b6bc7", "#5a4b8a", "#c9c9c9"]
typography:
  display: "bitmap-style monospace (VT323 / pixel mono feel) · bold · normal-to-wide tracking, uppercase"
  body: "same bitmap monospace, no separate body face observed"
radius: "none"
---
## Overview
A near-total black void where the only content is a tiny animated cluster of pixel glyphs — filled squares, outlined squares, circles, and plus signs in hot pink, violet, and gray — that reforms frame to frame like a dithered particle system. A single monospace terminal-style caption, "[:: CLICK TO ENTER + ENABLE AUDIO ::]", floats over the cluster on a black strip. The aesthetic is retro-terminal meets generative art: no chrome, no navigation, no imagery beyond the reactive glyph swarm.

## Layout
No nav, no header, no footer — the entire viewport is empty black canvas with one dead-center focal point. The pixel-glyph cluster sits at exact horizontal center, slightly below vertical center, roughly 60px wide against a 1440px viewport, making negative space itself the composition (~99% of the page is void). The CTA text bar overlaps the cluster horizontally, terminal-prompt style. Across frames the cluster mutates (glyphs swap between square/circle/plus, colors shift pink↔purple↔gray), signaling audio-reactive motion.

## Components
Only one interactive element observed: the enter prompt — uppercase bold monospace white text on a solid near-black (#0a0a0a) strip with square corners, framed by "[::" and "::]" ASCII brackets instead of borders. No conventional buttons, cards, or inputs; the whole screen is the click target. The glyph cluster acts as a living component: a grid of ~10px cells rendered as pixel-perfect squares (filled and 1px-outlined), circles, and crosses with zero border-radius and no shadows anywhere.

## Signature
- A single tiny neon pixel-glyph swarm (pink/violet/gray squares, circles, plus signs) animating on an otherwise empty black screen
- ASCII-bracket terminal caption "[:: ... ::]" as the sole UI text, uppercase bitmap monospace
- Extreme negative space: content occupies well under 1% of the viewport
- Glitch/dither motion — the figure never holds a stable shape between frames

## Do / Don't
Do:
- Keep the canvas pure near-black (#070707) with zero texture, gradient, or vignette
- Render all graphics on a strict pixel grid: hard-edged squares, outlined squares, circles, and crosses, no anti-aliased curves
- Limit color to hot pink (#f767ae), violet (#8b6bc7), and desaturated grays over black
- Use one bitmap monospace face, uppercase, wrapped in ASCII brackets like "[:: LABEL ::]"
- Make elements animate/mutate continuously — static compositions break the language

Don't:
- Add navigation bars, footers, cards, or any conventional page chrome
- Use border-radius, drop shadows, or gradients on any element
- Introduce photography, illustration, or smooth vector art — glyphs only
- Fill the viewport with content; the void is the design
- Mix in serif or humanist sans type, or lowercase headings
