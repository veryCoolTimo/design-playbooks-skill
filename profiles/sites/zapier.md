---
name: zapier
kind: site
style: ML
category: workflow-automation
website: null
pages: [home, pricing]
palette:
  canvas: "#fffefb"
  ink: "#201515"
  primary: "#ff4f00"
  accents: ["#f8f4f0", "#605d52", "#c5c0b1"]
typography:
  display: "Degular Display (Inter 500 as substitute) · medium weight · near-zero tracking, +1px on eyebrows"
  body: "Inter"
radius: "medium 8-14px (12px on buttons and cards; 6px inputs; pill badges only)"
---
## Overview
Everything on this surface is warm: an off-white cream page instead of true white, a coffee-brown near-black instead of true black, and neutrals that drift toward tan rather than gray. One saturated orange (#ff4f00) does all conversion work while the rest of the page stays quiet. The effect is friendly and mature rather than cold-tech, with 12px rounding splitting the difference between playful pills and hard corners.

## Layout
Cream sticky top nav with ink links; dark coffee footer closes the page. Hero splits headline-left / illustration-right on desktop, stacking on mobile, inside a ~1280px centered container. Sections alternate as full-width bands — cream (#fffefb), soft cream (#f8f4f0), and occasional polarity-flipped dark #201515 bands — each with generous 64px vertical padding. Grids run 3-4 columns on desktop, 2 on tablet, 1 on mobile. Sections open with a small uppercase eyebrow (14px, +1px tracking) above a sentence-case display headline.

## Components
- Buttons: 12px-radius rectangles, ~48px tall, Inter semibold 18px labels. Four tiers: orange fill (primary), ink fill (secondary), 1px ink outline on cream (tertiary), and a plain text button. Never pills.
- Cards: 12px radius, 24px padding, mostly borderless — elevation comes from the soft-cream fill sitting on the lighter canvas, not shadows. Dark ink variants flip polarity for featured content and highlighted pricing tiers; pricing cards on canvas get a 1px ink border.
- Inputs: tighter 6px radius, white-cream fill, 1px ink border, 18px Inter.
- Badges: full-pill soft-cream chips with ink text.

## Signature
- Exactly three tonal families: cream surfaces, coffee ink, and one loud orange — no second accent color exists.
- Warm-shifted neutral ladder (#f8f4f0 → #c5c0b1 → #939084 → #605d52); no cool grays anywhere.
- Two-typeface split with strict roles: Degular Display 500 only for heroes and eyebrows, Inter for all other text.
- Depth by surface swap (cream-on-cream, or a flipped dark band) instead of drop shadows.

## Do / Don't
Do:
- Keep #ff4f00 exclusively for primary CTAs; everything else stays in the cream/coffee range.
- Use the 12px radius consistently on buttons and cards; drop to 6px only for inputs.
- Write headlines in sentence case; reserve uppercase for the tiny 14px tracked eyebrow.
- Alternate cream / soft-cream / dark-ink bands to pace the page rather than adding dividers or shadows.
- Convey card elevation via the #f8f4f0-on-#fffefb surface contrast or a 1px ink hairline.

Don't:
- Don't swap the cream canvas for pure #ffffff or the ink for pure #000000 — the warmth is the identity.
- Don't add a blue, green, or any second chromatic accent.
- Don't make CTAs pill-shaped or fully square.
- Don't uppercase display headlines or use heavy 700+ weights at hero scale.
- Don't lean on drop shadows for cards; the system is flat with surface-tint elevation.
