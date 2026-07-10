---
name: bmw-m
kind: site
style: BT
category: automotive
website: null
pages: [home, model-detail, magazine, motorsport, topics]
palette:
  canvas: "#000000"
  ink: "#bbbbbb"
  primary: "#000000"
  accents: ["#0066b1", "#1c69d4", "#e22718", "#0653b6"]
typography:
  display: "BMW Type Next Latin (Inter substitute) · heavy 700, all-caps · zero tracking on display, 1.5px on labels"
  body: "BMW Type Next Latin Light (300)"
radius: "none (buttons and cards 0px; circular icon buttons are the sole exception)"
---
## Overview
True-black pages where the only real energy source is edge-to-edge car photography — track shots, cockpit views, carbon-fiber closeups. White uppercase headlines at weight 700 sit against feather-light 300 body copy; that weight gap is the whole editorial voice. The M tricolor (light blue / dark blue / red) shows up only as a thin stripe on brand moments, never as UI color. Everything else is hairlines, black surfaces, and restraint.

## Layout
Fixed 64px black top nav with logo left and sentence-case menu links. Heroes are full-bleed photo bands with an 80px uppercase h1 laid over the image, no card frame. Content sits in a ~1440px container while photography breaks out to the viewport edge. Major bands are separated by a strict 96px rhythm, alternating photo band → spec/text band → photo band so two text-only sections never touch. Card grids run 3-up on desktop, collapsing to 2 then 1; footer is a 4-column black link block.

## Components
Buttons are sharp 0px rectangles, 48px tall, uppercase 14px labels tracked 1.5px — either white-outlined on transparent (over photos) or canvas-filled with white text. The lone round shapes are 48px circular icon buttons (carousel arrows, chat launcher). Cards have zero radius: some sit on a #1a1a1a surface with 24px padding, others are just a photo on bare black with a title and an uppercase chevron text-link. Spec cells use near-black #0d0d0d with a 32px stat on top and a small caps label under it. Inputs are 48px square-cornered fields on #1a1a1a with a hairline border that turns white on focus. Category tabs are bare caps text; the active one goes white with a 2px underline. No drop shadows anywhere — depth comes from photo lighting and one-step surface lifts.

## Signature
- The 4px M tricolor stripe (#0066b1 → #1c69d4 → #e22718) as a rare divider/badge accent — strictly identity, never an action color.
- 700-weight uppercase display versus 300-weight body — an extreme, deliberate weight pairing.
- Binary geometry: everything is a hard rectangle except perfectly circular icon buttons.
- Photography carries all depth and drama; UI chrome is monochrome and nearly invisible.

## Do / Don't
**Do**
- Lead every band with full-bleed automotive photography and let type sit on or under it.
- Set h1/h2 in UPPERCASE at 700; keep body at Light 300, sentence case.
- Track all-caps buttons and labels at 1.5px for the machined feel.
- Keep 0px corners on buttons, cards, inputs, and images; circles only for icon buttons.
- Hold a uniform 96px gap between major sections.

**Don't**
- Don't fill buttons or backgrounds with the M tricolor — it lives only in the stripe, wordmark, and badges.
- Don't bold body copy; anything above 300 kills the engineered restraint.
- Don't round button or card corners — soft shapes read as consumer tech, not motorsport.
- Don't add gradients, shadows, or decorative backdrops behind hero type; the floor stays pure black.
- Don't stack two text-only sections back to back — alternate photo and content bands.
