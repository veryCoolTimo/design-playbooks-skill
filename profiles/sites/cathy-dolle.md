---
name: cathy-dolle
kind: site
style: ML
category: portfolio-photography
website: https://www.cathydolle.com/
pages: [home-gallery]
palette:
  canvas: "#ffffff"
  ink: "#0a0a0a"
  primary: "#0a0a0a"
  accents: ["#c7c7c7", "#8ea4b8"]
typography:
  display: "Helvetica Now / grotesque sans · regular weight · uppercase, slightly tight"
  body: "Same grotesque sans, ~11px uppercase labels"
radius: "none"
---
## Overview
A stark white index-page portfolio where a single narrow vertical filmstrip of monochrome imagery runs down the exact center of the viewport, flanked by a numbered project list on both sides. Type is tiny, uppercase, and utilitarian; the images carry all the visual weight. The entire interface behaves like a contact sheet: no panels, no color blocks, no chrome.

## Layout
- Fixed top bar spanning full width: site name top-left ("CATHY DOLLE"), view toggle ("LIST / SLIDER") left-center, "ABOUT", a small logo mark + "SHOP", and "PLAYGROUND" spread across the right half. "CONTACT" pinned bottom-right.
- Center column (~350px wide) holds a continuous vertical stack of portrait-ratio images with thin white gaps between them, scrolling like a filmstrip. A tiny square outline cursor/marker sits at viewport center over the images.
- Project index split into two symmetric columns left and right of the filmstrip: numbers ("01/", "02/"...) inner-aligned, project names outer-aligned, items 01-06 on the left, 07-12 on the right, evenly spaced down the full viewport height.
- The active/hovered item turns solid black while all others stay pale gray (~#c7c7c7), and the filmstrip scrolls to the matching image.
- Massive symmetric whitespace; the page is roughly 60% empty canvas.

## Components
- No conventional buttons: every action is a bare uppercase text label (~10-11px), no underline, no border, no background. Active state = black ink, inactive = light gray.
- No cards, no borders, no shadows, no dividers anywhere; images sit flush on white with square corners.
- The only non-text UI element is a small black square outline centered on the current image (acts as a cursor/viewfinder motif) and a tiny logo glyph next to "SHOP".
- Imagery is uniformly desaturated: black sculptural objects, B/W portraits, near-monochrome scenes; the muted slate blue of one image is the only hue on the page.

## Signature
- Single centered vertical filmstrip of monochrome images bisecting a white page.
- Mirrored two-column numbered index ("01/ ... 12/") with gray-to-black hover/active states as the sole navigation feedback.
- Tiny uppercase grotesque labels pinned to the four corners of the viewport instead of a nav bar.
- Square viewfinder mark hovering at page center, referencing a camera frame.

## Do / Don't
**Do**
- Keep all UI text uppercase, ~10-11px, in one grotesque sans; let scale contrast come from images, not type.
- Use opacity/gray-value shifts (light gray to black) as the only hover and active state.
- Center imagery in a narrow fixed column and let both flanks stay empty white.
- Pin navigation items to viewport corners/edges rather than grouping them in a bar or menu.
- Keep imagery desaturated or monochrome so the white canvas and black ink stay the palette.

**Don't**
- Add buttons with fills, borders, or rounded corners — there are none on this site.
- Introduce saturated brand colors, gradients, or background tints.
- Frame images with cards, shadows, captions, or borders; they must sit flush on white.
- Use mixed-case or large display headlines; the identity depends on uniformly tiny caps.
- Fill the side whitespace with content — the empty symmetry is the layout.
