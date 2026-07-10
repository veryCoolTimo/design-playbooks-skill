---
name: basehub
kind: site
style: DT
category: dev-tools-cms
website: https://basehub.com/
pages: [home]
palette:
  canvas: "#030303"
  ink: "#EDEDED"
  primary: "#FF6D00"
  accents: ["#161616", "#8F8F8F", "#F96B02"]
typography:
  display: "neutral grotesque (Inter/Suisse-like) · regular-to-medium, never heavy · tight, slightly negative tracking"
  body: "same neutral grotesque, small sizes; monospace for code snippets and labels"
radius: "buttons pill; cards small-medium 6-12px"
---
## Overview
Near-black (#030303) developer-tool landing page where a single saturated orange (#FF6D00) does all the work: glowing hero gradient, pill CTAs, highlight rings on feature cards, and a full-width orange banner. Everything else is restrained grayscale — #161616 panels, gray body text, white headings at moderate weights. The product itself (a dark CMS UI) is the hero art, shown as large embedded screenshots.

## Layout
Slim one-row dark nav: logo left, text links right, "Log in" ghost + orange pill "Sign up". Hero is centered: small pill badge, two-line headline, short subcopy, logo strip, one orange pill CTA, then a huge product screenshot sitting on an orange radial glow. Sections alternate: centered H2 + subcopy above a large screenshot or a bento-style feature grid (2-3 columns, mixed card sizes). Mid-page manifesto section drops imagery entirely — just two large gray/white paragraphs, left-aligned. Then a masonry testimonial grid (3 columns of tweet cards), a horizontal roadmap timeline with milestone nodes, two centered pricing cards, an FAQ accordion list, and a repeated orange CTA band before a minimal footer. Generous vertical whitespace between sections; content column stays narrow relative to the dark expanse.

## Components
- Buttons: solid #FF6D00 pill with dark/black label for primary; ghost text links for secondary; small white/outline pill inside the orange banner.
- Cards: #161616 fill, 1px subtle darker border, 6-12px radius, no visible drop shadows; the active/featured card gets an orange border ring.
- Testimonial cards: same #161616 tiles with avatar, handle, small gray text, and an X icon top-right.
- Pricing cards: dark panels with checklist rows, big price figure, full-width button at bottom (orange for the paid tier).
- FAQ: full-width hairline-divided accordion rows with chevrons.
- Code blocks: black insets with monospace and syntax coloring inside setup-step cards.

## Signature
- One-color discipline: bright orange #FF6D00 against pure near-black, used for CTAs, glows, and highlight rings — nothing else is colored.
- Orange radial glow bleeding from behind the hero screenshot and again behind the footer CTA.
- Full-width flat-orange CTA bands ("Try BaseHub Today") breaking the black rhythm mid-page and pre-footer.
- Product-UI screenshots as primary imagery, framed in thin-bordered dark cards; roadmap rendered as a literal timeline with labeled nodes.

## Do / Don't
Do:
- Keep the background a uniform #030303 and build depth only with #161616 panels and 1px borders.
- Reserve orange strictly for CTAs, glows, and one highlighted card per grid; let everything else stay grayscale.
- Use pill buttons with dark text on orange; keep headings regular/medium weight, not bold.
- Show the real product UI large and dark so it blends with the page; add an orange glow beneath it.
- Repeat the orange CTA band at least twice (mid-page and pre-footer).

Don't:
- Don't introduce a second accent hue — no blues, greens, or purple gradients.
- Don't use heavy drop shadows or glassmorphism; elevation here is border + fill contrast only.
- Don't set body copy in pure white; it sits at mid-gray (#8F8F8F-ish) with white reserved for headings and key phrases.
- Don't use large radii on cards or screenshots; only buttons and badges are pills.
- Don't fill the page edge-to-edge — content stays in a narrow centered column with wide black margins.
