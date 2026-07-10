---
name: revolut
kind: site
style: DN
category: fintech
website: null
pages: [home, product, pricing-plans]
palette:
  canvas: "#000000"
  ink: "#ffffff"
  primary: "#ffffff"
  accents: ["#494fdf", "#00a87e", "#e61e49", "#ec7e00", "#007bc2"]
typography:
  display: "Aeonik Pro (subs: Inter Display, General Sans, Söhne) · medium 500 · tight negative tracking, line-height 1.0 at display sizes"
  body: "Inter 400/600 with slight positive tracking on UI labels"
radius: "pill (buttons/chips) / large 20px (cards) / medium 12px (inputs)"
---
## Overview
Fintech marketing site built on a hard two-mode rhythm: true-black full-bleed bands for storytelling and pure-white bands for catalogue content (tables, FAQ, downloads), with no soft transitions between them. Giant Aeonik Pro headlines (80-136px, weight 500, line-height 1.0) dominate; product photography — phones, cards, POS terminals — fills entire dark sections as hero objects. The signature move: the loudest CTA is a plain white pill on black, while the cobalt-violet brand color (#494fdf) is deliberately rationed.

## Layout
64px black nav bar: wordmark left, top-level links center, login plus white pill CTA right; collapses to hamburger under 1024px. Hero is a full-bleed dark band with one massive headline and a white pill button. Sections alternate black/white in whole bands at 88-120px vertical padding; content maxes near 1200px while heroes and mockup bands run edge to edge. Plan cards sit 4-up (2-up tablet, 1-up mobile); feature grids 3-up. Hairline dividers stand in for shadows on both canvases.

## Components
Every button is a 48px-tall pill: white fill with black label on dark canvases, black fill on light ones, plus gray-soft and 1px-outlined variants; pressed state dims the white fill to #c9c9cd. Cards use 20px radius and 32px padding, flat with no drop shadows — dark cards lift via a slightly luminous surface (#16181a) on the black canvas, and the recommended plan tier inverts to a solid cobalt-violet block. Inputs are tall (56px), 12px radius, hairline-bordered on white. Small pill chips serve as sub-nav and tags; a cobalt pill badge marks "Most popular."

## Signature
- Whole-band flips between #000000 and #ffffff — the page reads like alternating magazine spreads
- White-pill-on-black as the primary CTA; brand cobalt reserved for one featured card and badges
- 80-136px medium-weight headlines with line-height 1.0 and steep negative letter-spacing
- Full-bleed device mockups where the photo asset IS the section, no chrome or captions
- Depth from luminance steps and hairlines only — zero drop shadows anywhere

## Do / Don't
Do:
- Alternate full-width black and white bands; keep the black at exactly #000000, not near-black
- Make the hero CTA a white pill with black text; use Aeonik-style type at 500 weight only for headings
- Keep body copy in Inter 400 (or 600 for emphasis), with a small positive tracking on button labels
- Limit dark surfaces to two steps: #000000 canvas and #16181a elevated cards
- Confine the saturated accent set (teal, pink, orange, blues) to illustrations and product imagery

Don't:
- Don't fill buttons with accent colors or cobalt — accents never become interactive surfaces
- Don't add drop shadows to cards; depth comes from band switches and surface luminance
- Don't loosen display line-height above 1.0 or use Inter weight 500 for body text
- Don't let cobalt #494fdf appear more than once per viewport; it is a stamp, not a theme
- Don't overlay captions on product mockup bands or box them in extra chrome
