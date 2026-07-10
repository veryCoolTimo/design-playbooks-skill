---
name: dirt
kind: site
style: ML
category: creative-studio
website: https://dirtverse.co/
pages: [home, work-grid, news, contact-form, footer]
palette:
  canvas: "#F5F5F2"
  ink: "#111111"
  primary: "#111111"
  accents: ["#D8E22E", "#5A46E8", "#FF4A1F", "#C9B4F2"]
typography:
  display: "custom blocky stencil wordmark + neo-grotesque (Helvetica Now / Neue Haas feel) · bold · tight, near-zero tracking"
  body: "neo-grotesque sans (Helvetica Now / Inter-like); monospace uppercase for section eyebrows"
radius: "pill (buttons/nav chips); medium 8-14px (image and news cards)"
---
## Overview
A near-white, air-heavy studio site where all chrome is monochrome and every drop of color comes from imagery: a hero row of circular 3D renders (chrome rose, acid-green sphere, violet plasma, marbled orange orb) and portfolio photography. UI is reduced to gray pill chips and one black pill CTA. The footer is the loudest moment — a viewport-filling glass/chrome 3D "dirt" wordmark with chromatic-aberration edges on white.

## Layout
Three-zone sticky nav: left pill group (About / Work / News), centered blocky "dirt" logomark, right solitary black Contact pill. Hero is a horizontal band of five circular media windows floating in huge white space, with a small two-line intro caption pinned bottom-left ("Welcome to the dirtverse." in gray, bold black tagline under it). Work section is an asymmetric masonry-ish grid of edge-to-edge image cards in mixed widths; a right-aligned "See All Work" pill closes it. News is a strict 3-column card row under a thin hairline rule and a monospace uppercase eyebrow ("IN THE NEWS"). Footer: 3-column link lists (FOLLOW / CONTACT / LEGAL, monospace headers, pill links) above the giant 3D wordmark. Whitespace is extreme — full empty viewport bands between sections.

## Components
- Buttons: pills only. Secondary/nav = light warm-gray fill (#EBEBE7), no border, dark gray label. Primary CTA (Contact) = solid black pill, white label. No shadows anywhere.
- Cards: rounded ~10-12px image blocks with zero chrome — no border, no shadow, no padding frame; the image is the card. News cards add a translucent gray pill source-tag overlaid top-right of the image, then bold black title and gray 2-line excerpt below.
- Form: contact textarea is a large flat light-gray rounded field with pale placeholder; Submit is a full-width light-gray rounded bar with bold black label.
- Labels: monospace, uppercase, letterspaced eyebrows over hairline rules.

## Signature
- Circular "porthole" hero: 3D renders masked into large circles, half-cropped at the viewport edges, floating on white.
- One-color UI system: everything interactive is a gray or black pill; content imagery supplies 100% of the color.
- Giant footer wordmark rendered as transparent glass/chrome 3D type with RGB-split edge fringing.
- Monospace uppercase section eyebrows against otherwise pure grotesque typography.

## Do / Don't
Do:
- Keep the interface strictly grayscale (white canvas, #EBEBE7 pills, black CTA) and let photos/3D renders carry saturated color.
- Use pill shape for every button, chip, tag, and link-button, including footer link lists.
- Leave oversized empty bands between sections; captions sit small and bottom-left, not centered.
- Crop hero media into circles and let outer ones bleed off the viewport edges.
- Set section labels in uppercase monospace above a 1px hairline rule.

Don't:
- Don't add borders, drop shadows, or gradients to buttons or cards — everything is flat fills.
- Don't introduce a colored brand accent into UI chrome; the only emphasis color is black.
- Don't center or enlarge body copy — text stays small, left-aligned, and sparse against huge visuals.
- Don't frame images in padded card containers; images run edge-to-edge within their rounded mask.
- Don't use more than one solid-black CTA per view (Contact in nav; everything else stays gray).
