---
name: mastercard
kind: site
style: ML
category: fintech-payments
website: null
pages: [home]
palette:
  canvas: "#F3F0EE"
  ink: "#141413"
  primary: "#141413"
  accents: ["#F37338", "#CF4500", "#3860BE", "#FCFBFA"]
typography:
  display: "MarkForMC (Sofia Sans substitute) · medium 500 · tight -2%"
  body: "MarkForMC at the unusual 450 weight (Sofia Sans / Inter fallback)"
radius: "buttons small-medium 20px; media large 40px to full pill/circle — the 8-14px middle is deliberately skipped"
---
## Overview
A warm editorial system built on putty-cream backgrounds instead of white, where nearly every shape is a pill, stadium, or circle. One geometric sans does all the work through weight and tracking shifts. Photography lives inside circular masks connected by thin hand-drawn orange arcs, giving still pages a sense of orbiting motion.

## Layout
The nav is a white pill floating about 24px below the top edge with a whisper-soft shadow — logo left, five links center, circular search button right. The hero is a 40px-radius stadium media frame nearly viewport-wide sitting shadowless on cream. Sections breathe with 96-128px vertical gaps; circular portrait cards are scattered asymmetrically (never gridded) with huge cream-on-cream "ghost" headlines behind them. Content caps around 1280px. The footer flips to warm near-black with a conversational headline and four link columns.

## Components
Primary buttons: solid ink-black pills, 20px radius, cream (not white) text, 1.5px matching border. Secondary: white fill with ink outline, same shape. A burnt-orange pill exists but only for consent/legal flows. The signature element is the "satellite" — a 50-60px white circle with an arrow docked on the rim of each circular photo card. Elevation is rare and diffuse (24-48px blur at ~8% opacity); borders do the functional separating. Search expands from a circle icon into a full-pill input.

## Signature
- Circular image portraits with a white satellite arrow-CTA protruding off the bottom-right edge
- Thin light-orange orbital arcs sketched between cards, implying a constellation of services
- Warm cream canvas everywhere plus body text at weight 450 — half a step softer than normal
- Eyebrow labels: tiny accent dot + 14px bold uppercase with +4% tracking, the only uppercase on the page

## Do
- Default the page background to #F3F0EE cream — never pure white
- Crop feature imagery to perfect circles and dock a white satellite CTA on each
- Keep marketing CTAs as ink-black 20px-radius pills; reserve #CF4500 orange for consent-type actions
- Set headlines at weight 500 with -2% letter-spacing and body at 450
- Float the nav as a detached white pill rather than a flush top bar

## Don't
- Don't use 8-16px radii on media or cards — the system jumps from small chips straight to 40px/full-pill
- Don't add a second typeface; contrast comes only from size, weight, and tracking
- Don't use hard tight shadows — anything elevated gets a large soft halo at low opacity
- Don't arrange the circular portraits on a regular grid; their asymmetric scatter is the point
- Don't uppercase anything larger than the 14px eyebrow, and never drop its leading dot
