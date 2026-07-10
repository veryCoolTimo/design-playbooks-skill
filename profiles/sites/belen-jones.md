---
name: belen-jones
kind: site
style: ML
category: portfolio
website: https://www.belenjones.com/
pages: [home]
palette:
  canvas: "#C6CCEC"
  ink: "#111111"
  primary: "#FFFFFF"
  accents: ["#F3D8DE", "#E4D6C4", "#CBCEC2", "#14362A", "#3A3322"]
typography:
  display: "extended grotesque (Monument Extended / Druk Wide feel) · heavy black weight · slightly tight, all caps"
  body: "monospaced grotesque (Space Mono feel) for metadata; nav uses wide-tracked caps grotesque"
radius: "pill (nav/CTA buttons); none elsewhere — the 3D showcase shape is hard-edged"
---
## Overview
A single-screen typographic index: a full-viewport stack of oversized all-caps project names rendered as thin outlines, with a giant hard-edged black 3D polygon (a rotating slab) floating over the list. The page background is a flat pastel that swaps per project state — lavender-blue, blush pink, warm beige, sage gray — while the type and slab stay near-black. Hovering a project fills its outline solid, with the leading letters tinted a deep green.

## Layout
No traditional nav bar: just two floating white pill buttons pinned top-right ("BELEN JONES" wordmark and "CONTACT"). The hero IS the site — an edge-to-edge list of 8-9 project names set in ~120px outline caps, left-aligned, stacked with almost no leading, overflowing the right edge. The black 3D slab occupies the center-right two-thirds and overlaps the type. Bottom-right corner holds tiny monospace metadata ("BERLIN, GERMANY / CET 05:01"). Zero conventional sections, zero scroll rhythm visible; whitespace comes only from the flat pastel field around the type.

## Components
- Buttons: white pill capsules, no border, very soft drop shadow, dark letter-spaced caps label; the only "UI chrome" on the page.
- Project links: text-only. Default state is 1px-outline hollow type in the ink color; hover/active state fills the word solid black with the first 2-3 letters filled deep green (#14362A).
- Cards/inputs: none. The 3D black polygon acts as the project showcase surface (likely a video/render canvas), sharp-cornered, no border or shadow.

## Signature
- Viewport-filling list of outline display type used as the entire navigation and content.
- Whole-page background color swap (pastel lavender, pink, beige, sage) as the state change between projects.
- One monolithic matte-black 3D polygon overlapping the type, breaking the flat layout with depth.
- Partial-word color fill on hover: solid black word with dark-green leading letters.

## Do / Don't
Do:
- Set project names in a single extended heavy grotesque, all caps, at 100px+ with cramped line-height so the list fills the viewport.
- Use outline (stroke-only) type for resting state and solid fill for the active item.
- Swap the entire canvas color per active project, keeping ink and the 3D element constant near-black.
- Keep chrome to two white pill buttons top-right and one monospace caption bottom-right.
- Let type run off the right edge instead of shrinking it to fit.

Don't:
- Add nav menus, section headers, cards, or grids — the type list is the only structure.
- Use rounded corners, borders, or gradients on the showcase surface; the slab is flat black and hard-edged.
- Introduce saturated brights; every canvas is a desaturated pastel and every foreground is near-black.
- Use more than one display family or mix weights within the list.
- Add drop shadows anywhere except the two pill buttons.
