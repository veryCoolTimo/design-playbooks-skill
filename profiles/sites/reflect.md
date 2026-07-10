---
name: reflect
kind: site
style: DN
category: productivity
website: https://reflect.app/
pages: [home]
palette:
  canvas: "#030014"
  ink: "#aca4c4"
  primary: "#1e0b45"
  accents: ["#6c35f0", "#736995", "#c9bdf5"]
typography:
  display: "Roobert-like geometric grotesque · medium weight · slightly tight"
  body: "same geometric grotesque, regular weight"
radius: "medium 8-14px (buttons ~10px, cards/app frame 12-16px); pill on announcement badges"
---
## Overview
Near-black indigo void (#030014) lit almost entirely by one recurring motif: a glowing violet celestial body. The hero is a black-hole/eclipse render, later sections reuse orbital rings, radar circles, a locked globe, and a luminous planet under pricing. Chrome is minimal — thin translucent borders, lavender-gray text — so the neon glow carries all the drama. Typography stays calm and mid-weight; the light show does the branding.

## Layout
Centered pill nav bar at top (logo left, links center, Login + bordered CTA right). Hero: pill announcement badge, one-line H1, one-line subhead, then a huge product screenshot that intersects the glowing eclipse. Sections follow a strict rhythm: tiny eyebrow pill/label, centered 1-2 line heading, short subhead, then either a 4-column icon feature grid, a 2-3 column benefit row, or a full-width illustration. Enormous vertical whitespace between sections (illustrations get 800px+ of breathing room). Pricing is a single centered plan sitting on a glowing planet. Everything is center-axis symmetric.

## Components
- Primary CTA ("Start free trial", "Start your 14-day trial"): deep violet fill (~#1e0b45) with a 1px lighter violet border (~#736995), white label, ~10px radius, subtle inner glow gradient.
- Announcement/eyebrow badges: pill shape, faint translucent fill, thin border, sparkle icon.
- Feature items: mostly borderless — small line icon, bold white label, dim lavender description; separated by whitespace, not card boxes.
- App screenshot framed in a rounded dark panel with a faint 1px border; sidebar/calendar UI inside uses the same violet accents.
- Testimonial cards: dark translucent panels, thin borders, avatar + name + handle, muted gray-lavender body text.

## Signature
- One purple glow object per section (black hole, beam, radar rings, encrypted lock field, planet) as the sole imagery system — no photos, no flat illustration.
- Ultra-dark blue-violet canvas that is never pure black (#030014), so glows bloom smoothly into it.
- CTAs are dark violet with a light border — the brightest thing on the page is always the artwork, not the button.
- Center-aligned everything with cinematic vertical spacing; sections feel like slides in space.

## Do / Don't
Do:
- Keep the canvas #030014 everywhere; create hierarchy with glow intensity, not background shifts.
- Give each section exactly one luminous violet focal graphic and let text stay small and centered around it.
- Use lavender-gray (#aca4c4) for subheads/body and reserve pure white for headings and button labels.
- Border interactive elements with thin light-violet strokes over dark fills.
- Use pill badges as section eyebrows ("Get access", "New: ...").

Don't:
- Use bright/solid filled buttons — the primary CTA here is dark with a glowing edge, not a saturated block.
- Box features into visible cards; the feature grids rely on whitespace and icons only.
- Introduce a second hue — everything from icons to glows stays in the violet #6c35f0 family.
- Left-align hero or section headers; the whole page is symmetric about the center axis.
- Crowd sections vertically — the glow art needs hundreds of pixels of empty dark space to read.
