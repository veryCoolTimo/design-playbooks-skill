---
name: literal-club
kind: site
style: DT
category: social-reading-platform
website: https://literal.club/
pages: [home]
palette:
  canvas: "#000000"
  ink: "#FFFFFF"
  primary: "#25C575"
  accents: ["#161616", "#9B9B9B", "#F5F0E8"]
typography:
  display: "transitional serif (Lyon/Freight-like) · regular weight · normal tracking"
  body: "neutral grotesque (Inter/Helvetica-like), 13-15px, muted gray for secondary text"
radius: "small 2-6px (buttons ~4px, cards and chips ~6px); pill only on small tag chips"
---
## Overview
A near-pure-black canvas with white serif headlines and a single saturated green reserved for actions. The product itself (dark-mode phone mockups) blends seamlessly into the page, so UI and marketing feel like one surface. Restraint everywhere: tiny type, thin hairlines, small line icons in dark gray squares, and book covers plus testimonial avatars supplying the only bursts of color.

## Layout
Top bar: logo left, full-width inline search field, then Features / Sign in / a green "Join →" block flush to the top-right corner (square, no margin). Hero is centered text-only — serif headline over two lines, small sans subcopy, one green CTA — followed by a horizontal row of four phone mockups that bleed off both edges. Feature section uses a 2-column grid of icon-plus-text rows (icon in a dark rounded square, title plus one line). Mid-page "Help writing the story" is a 3-column card row (product UI snippet, code snippet, b/w illustration). Social proof is a masonry-like scatter of small testimonial cards at varied offsets, also bleeding off the edges. Footer: 4 sparse link columns in small gray text. Generous vertical breathing room between sections; hairline dividers used sparingly.

## Components
- Buttons: solid green (#25C575) fill, black or dark text, small ~4px radius, compact padding, no shadow, no border. The nav "Join" is a hard-cornered green block with an arrow.
- Secondary buttons: "Explore features" is a ghost button — transparent fill, 1px gray border, white text, small radius.
- Cards: very dark gray (#141414-#1A1A1A) on black, small radius, no visible border or shadow — separation comes from the slight luminance step.
- Chips/tags: dark gray pills with white text (review mood tags "Addictive", "Haunting"); status chips with checkmark/book icons.
- Inputs: nav search is borderless dark field with magnifier icon and gray placeholder.
- Links: underlined white text inline in body copy (e.g. "our open API").

## Signature
- True-black page where dark-mode app screenshots dissolve into the background — the phones read as floating UI, not framed devices.
- Serif display type against black with a lone kelly-green action color; nothing else is tinted.
- Square-cornered green "Join →" block welded into the top-right corner of the nav.
- Scattered, edge-bleeding testimonial cards quoting tweets/IG handles instead of a neat grid.

## Do / Don't
Do:
- Keep the background at or near #000 and let dark UI screenshots merge into it without device chrome or drop shadows.
- Reserve the green strictly for CTAs and success/action states; render everything else in white-to-gray steps.
- Set headlines in a serif at modest sizes; keep body and UI text small (13-15px) in a plain grotesque.
- Separate cards from the canvas with a small luminance lift (#141414-ish), not borders or shadows.
- Let horizontal content rows (phones, testimonials) bleed past the viewport edges.

Don't:
- Don't introduce a second accent color or gradients — the palette is green plus grayscale only.
- Don't use large radii or pill buttons on primary CTAs; corners stay tight (0-6px).
- Don't add drop shadows, glows, or outlines around cards or mockups.
- Don't oversize the typography; the hero headline is restrained (~40px serif), not a giant display face.
- Don't align testimonials into a rigid symmetric grid — the scatter/offset rhythm is part of the look.
