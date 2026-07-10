---
name: uber
kind: site
style: BT
category: transportation
website: null
pages: [home, ride-landing, drive-landing, eats-landing]
palette:
  canvas: "#ffffff"
  ink: "#000000"
  primary: "#000000"
  accents: ["#efefef", "#5e5e5e", "#e2e2e2", "#0000ee"]
typography:
  display: "UberMove (geometric grotesque; sub: Inter/Geist) · bold 700 only · neutral tracking, never spaced"
  body: "UberMoveText (sub: Inter 400/500)"
radius: "buttons pill (999px); cards medium-large 16px; inputs small 8px"
---
## Overview
A strict monochrome system: pure black is the only conversion color, white is everything else, and grays fill the gaps between. Two proprietary sans faces split roles cleanly — a bold geometric display cut for headlines, a companion text cut for all copy and labels. Decoration is limited to hard-edged 4:3 editorial illustrations of urban life; no gradients, no accent hues, no atmosphere.

## Layout
Sticky white top nav with medium-weight links and black login/signup pills, collapsing to a hamburger under 1120px. Hero pairs a 52px/700 sentence-case headline with a shadowed ride-request form card (stacked gray input rows plus a black CTA). Page rhythm alternates polarity: white illustrated promo rows, then a full black band with white text, back to white, ending in a solid black footer. ~1200px centered container; cards 2-up on desktop with image/copy sides alternating, stacking on mobile.

## Components
Buttons are a pill hierarchy in one hue: black fill/white text for primary, plain white for secondary, #efefef gray for tertiary chips and category pills; a rare 16px-radius black rectangle appears only inside the large request flow. Cards are 16px-radius, flat by default — shadows (rgba-black ~0.12-0.16, 4px/16px blur) are reserved for the hero form card and floating pills. Inputs are gray-filled (#efefef or #f3f3f3) 8px-radius rows, no visible borders. Pressed white pills darken to #e2e2e2.

## Signature
- One black pill CTA per viewport — the entire conversion language is a single shape in a single color
- Mid-page polarity flips: solid #000 bands with white text act as the depth system instead of shadows
- Hero ride-request card: pickup/destination rows, date chip, black "See prices" pill in one shadowed 16px card
- Sentence-case-only display type at 700; uppercase exists only as tiny section eyebrows

## Do / Don't
**Do**
- Keep #000000 exclusive to primary CTAs, the footer, and dark promo bands — nothing else earns black fill
- Round every interactive element to 999px pill; keep all card chrome at 16px
- Break long white stretches with a full-width black band rather than adding color or shadow
- Anchor promo cards with a flat 4:3 illustration on one side, copy on the other
- Set headlines in the display face at 700, sentence case, default tracking

**Don't**
- Don't add any chromatic accent — the sole non-grayscale value is default link blue #0000ee in fine print
- Don't letter-space the display face in either direction
- Don't shadow cards by default; flat is the baseline, elevation belongs to the form card and floating pill only
- Don't set display headlines in all caps or use the text face for hero type
- Don't square off primary buttons outside the documented large-form exception
