---
name: tableland
kind: site
style: IL
category: web3-dev-infra
website: https://tableland.xyz/
pages: [home]
palette:
  canvas: "#E7C6F3"
  ink: "#1A1A1A"
  primary: "#1A1A1A"
  accents: ["#6465EB", "#895395", "#EA7A80", "#131033"]
typography:
  display: "squared sci-fi techno grotesque (Zen Dots / Trap-like, stencil-cut joints) · bold, extended · normal-to-wide tracking"
  body: "typewriter monospace (IBM Plex Mono / Space Mono feel), also used for nav, buttons, and lists"
radius: "medium 8-14px on buttons; large 16px+ on the terminal card"
---
## Overview
A retro-futurist illustrated landing page: one continuous cyberpunk-desert mural (canyons, rovers, riders, giant moons) flows behind every section, shifting from pale lavender dawn through sunset purples to a dark indigo night footer. All copy is set in monospace with CLI mannerisms ("1>", "2>" numbered lists, a live terminal), while headings use a squared sci-fi display face. Despite the dark-neon metadata tag, most of the page sits on light lavender-to-purple gradients; only the footer goes dark.

## Layout
Sticky-free top nav: wordmark left, three sparse uppercase mono links right, plus one black pill CTA ("RIGS") with coral text. Hero is text-left on a light lavender field with a huge soft moon circle and illustrated cliffs bleeding in from the right edge. Sections are single-column, left-aligned text blocks (heading, mono paragraph or numbered CLI list, one button) separated not by borders or cards but by full-bleed illustration scenes; the background gradient never breaks, so the page reads as one tall scroll-through mural. Final CTA is centered on dark indigo above a single row of mono footer links.

## Components
Buttons: near-black (#1A1A1A) rounded rectangles (~10-14px radius), uppercase letterspaced monospace label with a distinctive "▸|" arrow glyph; the footer variant is filled periwinkle #6465EB. Nav CTA is the same black pill with coral-red (#EA7A80) text. The only card is a large dark rounded terminal (#1A1A1A, ~20px radius) rendering an interactive CLI in white mono. No visible borders, shadows are minimal to none; no traditional inputs shown.

## Signature
- Continuous illustrated desert-cyberpunk backdrop spanning the entire page as one gradient mural
- Everything except display headings set in monospace, including body copy and nav
- Numbered lists written as terminal prompts ("1>", "2>") and a real embedded CLI terminal block
- Squared, stencil-cut sci-fi display face for every heading ("Build web3 with SQL")

## Do
- Keep one uninterrupted background gradient/illustration across sections; let scenes act as section dividers
- Set body, nav, buttons, and lists in monospace with uppercase letterspaced button labels
- Use black (#1A1A1A) as the default button fill on light sections, periwinkle #6465EB on the dark footer
- Lean into terminal idioms: prompt-numbered lists, an embedded CLI card, arrow glyphs on CTAs
- Reserve the squared techno display face for headings only, white on purple, black on lavender

## Don't
- Don't box content into bordered cards or add drop shadows; the page relies on open space over illustration
- Don't use a neutral white/gray canvas — backgrounds are always tinted lavender, purple, or indigo
- Don't introduce a humanist sans or serif for body text; the mono voice is the brand
- Don't center-align section copy (only the final CTA is centered); text blocks hang left with wide right margins
- Don't multiply accent colors per section — one black or periwinkle button per block, coral only as a small nav highlight
