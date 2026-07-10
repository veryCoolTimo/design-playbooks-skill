---
name: nothing-to-watch
kind: site
style: DN
category: entertainment-media
website: https://nothing-to-watch.port80.ch/
pages: [onboarding]
palette:
  canvas: "#0A0A0A"
  ink: "#F2F2F2"
  primary: "#F5F5F5"
  accents: ["#1A1A1A", "#FFFFFF"]
typography:
  display: "geometric grotesque (Poppins-like) · extra-bold italic · normal tracking"
  body: "geometric grotesque, medium weight · slightly wide tracking on labels"
radius: "small 2-6px on the Continue CTA; medium 8-10px on choice chips"
---
## Overview
A near-black, cinema-dark canvas with almost nothing on it: one oversized italic quote centered in a sea of empty space, and a compact control cluster pushed to the bottom third. The metadata says minimal-light, but the evidence is minimal-dark — white-on-black, monochrome, zero decorative chrome. Emoji serve as the only "iconography" and the only color.

## Layout
No nav at all. The hero is a single centered display line ("There's nothing to watch".) floating at vertical center with huge margins on every side. All interaction sits in a narrow left-anchored column in the lower third: a small labeled group ("Your device" with a tiny device glyph), a horizontal row of three equal-width choice chips, a full-column-width Continue button, and a fine-print attribution line beneath. Whitespace-to-content ratio is extreme; the page reads as a full-screen intermission card.

## Components
- Choice chips: dark fill (#141414-ish) with 1px subtle gray borders, ~8-10px radius, emoji + bold label. Selected state = brighter white border, a white "Estimated" pill tag overlapping the top edge, and a circular checkmark badge on the corner.
- Primary CTA: solid white/off-white bar (#F5F5F5) with dark text, small radius, full width of the control column — the only high-contrast solid on the page.
- Tag/pill: tiny white rounded pill with dark uppercase-ish label ("Estimated").
- No visible shadows; hierarchy is done entirely with border brightness and fill contrast.

## Signature
- One giant bold-italic quoted sentence as the entire hero, punctuation included ("...").
- Inverted-contrast CTA: white solid button on a near-black page, everything else outlined and dark.
- Emoji as functional icons inside selectable chips (potato / neutral face / flexed bicep as device tiers).
- Overlapping pill + check badge on the selected option, breaking the chip's bounding box.

## Do
- Keep the canvas near-black (#0A0A0A) and let a single white solid element (the CTA) carry all the visual weight.
- Set display copy in heavy italic geometric sans, wrapped in literal quotation marks for the conversational tone.
- Use 1px low-contrast borders on dark fills for secondary controls; brighten the border to show selection.
- Leave aggressive empty space — center one message, push controls to the bottom.
- Use playful emoji as option icons instead of a custom icon set.

## Don't
- Don't add chromatic accent colors — the palette is strictly monochrome; emoji provide the only hue.
- Don't introduce a top nav, logo lockup, or header; the page is deliberately chromeless.
- Don't use drop shadows or gradients on controls — depth comes from border/fill contrast only.
- Don't make secondary buttons solid; only the primary action gets a filled white treatment.
- Don't enlarge the fine print — attribution stays as a single sub-caption line under the CTA.
