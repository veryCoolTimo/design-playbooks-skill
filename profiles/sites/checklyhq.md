---
name: checklyhq
kind: site
style: DT
category: dev-monitoring
website: https://www.checklyhq.com/
pages: [home, product, blog]
palette:
  canvas: "#0A192E"
  ink: "#9FB1C7"
  primary: "#F5F8FC"
  accents: ["#3B82F6", "#16233B", "#22C55E", "#EF4444"]
typography:
  display: "Inter-style neo-grotesque · semibold-to-bold · tight, near-neutral tracking"
  body: "Inter-style neo-grotesque, regular"
radius: "small 2-6px on buttons; medium 8-14px on cards"
---
## Overview
A deep navy, code-first developer aesthetic: near-black blue canvases carry white headlines, muted slate body text, and embedded terminal/code panels with syntax-highlighted green and red output. Bright blue is the accent thread (logo check, numbered step badges, links), while the main CTA flips to a light/white fill for contrast on dark. The blog inverts to a clean white canvas with navy ink, keeping the same type and component language.

## Layout
Slim single-row top nav: logo left, center link cluster with dropdown carets, Login plus a solid pill-ish CTA right. Home hero is centered stacked text over a dark radial "network" illustration with floating product icons converging on the mascot; product hero is left-aligned two-column with a code snippet panel right. Sections alternate long dark bands with occasional white/light bands (integrations, testimonials, newsletter) creating strong value contrast rhythm. Content rides a narrow centered column (~1100px); features appear in 3-column icon-plus-blurb grids; a vertical connector line threads numbered Code/Test/Deploy steps down the page. Blog uses a large featured post (image left, text right) above a 3-column card grid on alternating white/gray bands. Footer is a dense multi-column navy block. Signature waveform: rows of thin vertical blue bars form an audio-waveform texture as section transitions.

## Components
Buttons: compact, small-radius (4-6px) rectangles; primary is light/white fill with dark navy text on dark canvases and solid dark navy fill with white text on light canvases (nav "Start for free", "Subscribe"); secondary is transparent with a thin muted border ("Read the docs"). Cards: 8-12px radius, white fill with hairline light-gray borders and little to no shadow on light bands; on dark bands, slightly lighter navy fills with faint blue hairline borders. Code/terminal panels: darker-than-canvas fills, rounded corners, syntax highlighting in green/red/blue, small window chrome. Tag chips: small gray pills with lowercase labels on blog cards. Inputs: white rounded fields with subtle border, paired inline with a dark submit button. Numbered step badges: small solid blue circles with white digits.

## Signature
- Deep navy near-black canvas with a thin-vertical-bar blue waveform texture bridging sections
- Real syntax-highlighted terminal/code panels as first-class hero and feature content
- Blue raccoon mascot icon recurring in illustrations, diagrams, and card art
- Light CTA on dark ground / navy CTA on light ground — the button always maximally contrasts the band
- Vertical connector line stitching numbered Code → Test → Deploy steps down the page

## Do
- Keep marketing canvases deep navy (#0A192E range) and reserve pure white for the blog/docs surfaces and inverted content bands
- Show actual CLI output and code snippets with green/red status coloring instead of abstract product shots
- Use small blue numbered badges and a thin connector line to sequence workflow steps
- Keep buttons compact with small radii and flip button fill (light-on-dark, dark-on-light) per band
- Use hairline borders on cards; keep shadows minimal or absent

## Don't
- Don't use large-radius or pill buttons — corners stay tight (4-6px)
- Don't put saturated blue fills on the primary CTA; blue is for accents, links, and badges
- Don't add heavy drop shadows or glassmorphism — depth comes from band color shifts and hairlines
- Don't use gradients beyond the subtle radial glow behind heroes and the soft blue-to-white card washes
- Don't set long body copy in white at full opacity on dark — body text is muted slate (#9FB1C7 range)
