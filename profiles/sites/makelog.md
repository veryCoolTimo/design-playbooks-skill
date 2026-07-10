---
name: makelog
kind: site
style: CP
category: dev-tools-changelog
website: https://www.makelog.com/
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#666666"
  primary: "#8A47E6"
  accents: ["#2864ED", "#EEAFD4", "#FBE790", "#A8B6FA", "#D3B8FD", "#18181A"]
typography:
  display: "rounded bubble/soft-serif display (Baloo/Fredoka-like, inflated letterforms) · extra bold · slightly tight, all-caps"
  body: "clean geometric sans (Inter/Poppins-like)"
radius: "pill buttons; large 16px+ cards"
---
## Overview
A candy-colored, toy-like SaaS landing page: an intense cobalt-blue hero melts into a giant sunset-rainbow gradient (pink to orange), then drops onto a plain white canvas filled with pastel candy cards. Headlines are set in an inflated bubble typeface, often all-caps and sometimes filled with multicolor gradients, while body copy stays in a quiet gray geometric sans. The mood is playful and confident, closer to a sticker sheet than a typical dev tool.

## Layout
Top nav sits directly on the blue hero: logo left, three text links plus a pill outline "Log in / Sign up" button right. Hero is centered and short — two-line bubble headline, one small subline, single white pill CTA — followed by a ghosted logo strip and a large floating product screenshot framed in a rounded white/blue card that overlaps the gradient. Below, a 3-column feature-blurb row (middle one on a light gray rounded panel), then an asymmetric bento grid of pastel cards (2-col, mixed heights: blue integrations card, periwinkle "done done" card, black pricing card, lavender AI card). Testimonials are a loose, slightly rotated scatter of pastel quote cards around a gradient bubble heading. A pale-pink full-width CTA banner precedes a cobalt footer that mirrors the hero blue. Generous whitespace between sections; content column ~1000px.

## Components
Buttons: pill-shaped everywhere; hero CTA is white fill with blue text on the blue background, footer-banner CTA is purple (#8A47E6) fill with white text, nav login is a transparent pill with thin white border. Black pricing card doubles as a giant button with a circular arrow chip. Cards: large radius (16-24px), flat pastel fills, no visible borders or drop shadows except the hero screenshot card which has a white inner frame and soft glow; testimonial cards get slight rotation for a hand-placed feel. Integration chips are small white pills with icon + label and hairline borders. AI example rows are white pill-shaped inputs inside the lavender card. Stage badges (Dev/Stage/Prod) are gray pills with status dots.

## Signature
- Inflated bubble display type, all-caps, sometimes with animated-looking multicolor gradient fills ("OUR CUSTOMERS", "LET'S SHIP!")
- Full-bleed cobalt-to-sunset rainbow gradient hero with tiny yellow sparkle/star doodles
- Bento grid of flat pastel candy cards (baby blue, periwinkle, lavender, pink, yellow) plus one contrasting solid-black card
- Slightly rotated, scattered pastel testimonial cards with circular avatars

## Do / Don't
Do:
- Reserve the bubble display face for short all-caps headlines; keep everything else in the plain gray sans
- Use flat pastel card fills with large radii and no borders/shadows; let one black card punch through the pastels
- Keep CTAs as pills — white-on-blue in the hero, saturated purple on light sections
- Let the hero gradient bleed behind the product screenshot so the white canvas starts mid-page
- Add small playful touches: sparkle glyphs, slight card rotation, gradient-filled headline text

Don't:
- Don't put long paragraphs in the bubble font — it's used only for 2-6 word headlines
- Don't add drop shadows, outlines, or glassmorphism to the pastel cards; they read flat
- Don't use sharp corners or small radii anywhere — nothing on the page is squarer than ~16px
- Don't desaturate the palette; the look depends on full-strength cobalt and candy pastels against pure white
- Don't align testimonial cards to a strict grid — the scatter/rotation is deliberate
