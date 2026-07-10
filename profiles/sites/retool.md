---
name: retool
kind: site
style: DT
category: low-code-platform
website: https://retool.com/
pages: [home, product (apps, ai-apps, database, mobile, external-apps), solutions (enterprise), pricing]
palette:
  canvas: "#0E0E0C"
  ink: "#E9E6DC"
  primary: "#EFECE1"
  accents: ["#2B4EDD", "#B77CE4", "#E4593B", "#F2CB4E", "#33654E", "#E5E7D8"]
typography:
  display: "Custom neo-grotesque (Neue Haas / Helvetica Now feel) · regular-to-medium, never heavy · tight, slightly negative tracking"
  body: "Same grotesque at small sizes; monospace for eyebrow labels, tags, and metadata"
radius: "pill buttons; small 2-6px on cards and panels (some fully square)"
---
## Overview
A dual-theme editorial-technical language: most product pages sit on a near-black warm charcoal canvas with cream type, while home, enterprise, and pricing flip to a pale cream/sage canvas with near-black type. Every page pairs restrained grotesque headlines with lavish painterly illustration (isometric block cities, bookshelves, anime-style interiors) and thin blueprint grid linework. Each product page owns one accent hue — cobalt blue (apps), violet (AI), red-orange (mobile), green (enterprise) — applied to large flat panels framing UI screenshots.

## Layout
Sticky top nav: logo left, plain text links with dropdown carets center-left, right-aligned "Sign in" ghost + "Book a demo" outline + "Start for free" filled pill; on the light home variant the nav links sit inside a white pill capsule. Heroes are text-first: a small breadcrumb/eyebrow label, a 2-3 line grotesque headline (sentence case, sometimes with inline pictogram glyphs embedded in the headline), two pill CTAs, then a full-bleed illustration band with a floating product screenshot overlapping it. A monochrome logo strip follows every hero. Body rhythm alternates: sticky two-column feature sections (numbered accordion list left, framed screenshot on a colored panel right), long scroll-linked use-case rails where inactive items dim to near-invisible, an oversized-quote testimonial block with customer logo tiles, then a final CTA section beside an illustration. Footer is dense multi-column links capped by a giant wordmark spanning nearly full page width. Thin 1px blueprint grids and isometric line drawings fill negative space.

## Components
Buttons: full pills, small text; filled (cream on dark pages, black on light pages), thin 1px outline secondary, both compact. Eyebrow tags: tiny bordered pill chips with monospace uppercase text ("FEATURES", "USE CASES", "HOW IT WORKS"). Cards: flat, square-to-slightly-rounded, hairline 1px borders, no drop shadows anywhere; pricing plan cards are thin-bordered rectangles with flat pastel header bands (pink, sage) and checkmark lists. Feature grids use small line icons above a bold one-line title and muted body copy, separated by hairline rules rather than card boxes. Screenshots sit on flat solid-color panels (cobalt, violet, red-orange) with subtle rounded corners. Accordion/numbered lists with 01-04 indices and hairline dividers. Pricing toggle: small dark pill switch (Monthly/Annually, Cloud/Self-host).

## Signature
- Dual cream/near-black canvases with the same grotesque type system; page section inverts rather than tints.
- One flat accent color per product page framing UI screenshots (cobalt, violet, red-orange, green, yellow).
- Thin blueprint/isometric line-art grids as background texture, plus painterly illustration heroes.
- Giant footer wordmark ("Retool" at near viewport width) and monospace pill eyebrow labels.
- Scroll-dimmed content: inactive list items and use-case blocks fade to barely-legible until active.

## Do / Don't
Do:
- Keep headlines regular-to-medium weight, sentence case, tightly tracked; scale, not boldness, carries hierarchy.
- Use hairline 1px borders and flat fills for all cards and chips; separate features with rules instead of boxes.
- Assign each major page/section a single flat accent panel color behind screenshots; keep everything else near-monochrome.
- Use monospace uppercase micro-labels in bordered pill chips as section eyebrows.
- Let illustration and blueprint linework fill whitespace instead of gradients or photos of UI.

Don't:
- Don't use drop shadows, glassmorphism, or glow effects — every surface here is flat.
- Don't use saturated blue/purple gradients or neon; accents are single flat hues on matte canvases.
- Don't bold or uppercase headlines; the type voice is calm and editorial.
- Don't round cards beyond ~6px — only buttons are pills.
- Don't mix multiple accent hues within one section; one hue per context.
