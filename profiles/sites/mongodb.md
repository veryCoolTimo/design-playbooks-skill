---
name: mongodb
kind: site
style: DT
category: developer-tools
website: null
pages: [homepage, product, pricing, course-catalog, use-case, community-edition]
palette:
  canvas: "#ffffff"
  ink: "#001e2b"
  primary: "#00ed64"
  accents: ["#001e2b", "#00684a", "#c3f0d2", "#7b3ff2", "#fa6e39", "#3d4f9f"]
typography:
  display: "Euclid Circular A · medium (500), never heavier for headlines · tight negative tracking (-1.5px at 72px)"
  body: "Euclid Circular A (geometric sans); Source Code Pro for code only"
radius: "buttons pill (9999px); cards medium-large 12px"
---
## Overview
A two-register system: near-black teal (#001e2b) bands for heroes, CTA banners, and the footer, alternating with plain white content sections. The single loudest element is the electric-green pill button, which reads against both registers with dark-navy label text. Everything else stays quiet — hairline-bordered white cards, muted gray text tiers, geometric sans at medium weight.

## Layout
Sticky white nav (~64px, hairline bottom border) with a dark promo strip above it and a green "Try Free" pill at the right. Heroes are deep-teal full-bleed bands with ~120px padding, a centered 72px headline, subtitle, button pair, and often a dark terminal-style code mockup card floating below. Sections run at 96px rhythm on marketing pages, tightening to 64px on pricing/catalog. Container is 1280px; catalogs use 3-up card grids, certifications 4-up, pricing a 3-tier card row over a dense hairline comparison table. Pages close with a dark rounded CTA banner and a dark 6-column footer.

## Components
Buttons: all pill-shaped, 14px/600 labels, 10x22px padding. Primary is #00ed64 fill with #001e2b text (pressed darkens to #008c34); secondaries are transparent with a 1px hairline outline in either register. Cards: white, 12px radius, 1px #e1e5e8 border, essentially flat — shadows appear only on hover tiles and floating code mockups. Featured pricing tier flips to pale mint (#e3fcef) with a 2px bright-green border. Inputs: 44px tall, 8px radius, 1px border that becomes 2px dark-green (#00684a) on focus. Small square-ish badges (4-6px radius) carry category colors on course tiles; status badges are pills. Tabs come in two flavors: outlined pills (active = solid ink) and underline tabs (active = dark-green 2px underline).

## Signature
- Bright green (#00ed64) pill CTA with dark-navy text, identical on white and dark-teal surfaces
- Deep-teal (#001e2b) hero/footer/CTA bands sandwiching stark white content
- Dark terminal-style code mockup cards embedded right in the hero
- Saturated purple/orange/pink/blue appears only as course category tags — nowhere else

## Do
- Reserve #00ed64 strictly for CTA pills and small badges; label them in #001e2b, not white
- Open and close pages with #001e2b bands; keep mid-page content on white with hairline-bordered flat cards
- Keep every button and status badge fully pill-shaped, cards at 12px
- Use dark-green #00684a (not the bright green) for text links and focus rings
- Set headlines at weight 500 with negative tracking; save 600 for buttons and small labels

## Don't
- Don't fill backgrounds or set text in the bright green — it functions only at button/badge scale
- Don't give flat documentation/pricing cards drop shadows; elevation belongs to code mockups and modals
- Don't square off buttons or swap the dark hero for a white one
- Don't let the category accents (purple/orange/pink/blue) leak beyond course tags
- Don't push headline weight to bold; the system tops out at 500 for display sizes
