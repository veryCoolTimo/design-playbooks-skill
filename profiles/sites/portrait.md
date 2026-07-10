---
name: portrait
kind: site
style: ML
category: web3-identity
website: https://portrait.so/
pages: [home, about, blog, points]
palette:
  canvas: "#F7F8FA"
  ink: "#5C6470"
  primary: "#26241F"
  accents: ["#1E3A5C", "#F0436E", "#8ECDF5", "#F5C6DC"]
typography:
  display: "rounded geometric grotesque (Hanken Grotesk / Gellix feel) · semibold · normal tracking"
  body: "same grotesque family · regular · muted slate gray"
radius: "pill (buttons, nav container) · large 16px+ (cards, page frame)"
---
## Overview
Ultra-light, airy canvas washed with a faint pastel rainbow gradient (pink, blue, green, peach) that bleeds from the top of every page and fades to near-white. Content sits in a rounded page frame with a floating pill navbar. Deep navy headings over soft gray body text, with occasional italic-serif words spliced into sans headlines for warmth. The whole language reads friendly, personal, and Apple-adjacent minimal.

## Layout
Floating pill nav bar (logo left, center links with a red "NEW!" superscript badge on Points, Login + gradient-ring Sign up pill right). Heroes are centered with a large heading and a short 2-3 line subhead; the home hero adds a domain-claim input and scattered polaroid-style photo cards at the edges. Sections are separated by generous whitespace and vertical dashed hairlines used as rhythm markers (about page is essentially a single centered column of short paragraphs strung along a dashed line). Blog uses a hero-post split (text left, card right) plus a 2-up "More Stories" card grid. Footer is a 4-column link grid above a dashed divider, with a status dot bottom-right.

## Components
- Buttons: fully pill. Primary is near-black fill (#26241F) with white text ("Sign up or login"); the Sign up nav pill is white with an animated rainbow-gradient border ring; secondary ("Read More") is white pill with soft shadow and hairline border.
- Cards: white, large radius (~16-20px), 1px light gray border, very soft shadow; blog cards hold a light-gray rounded image well, date in small gray, bold title, gray excerpt, avatar + author row.
- Tabs/segments: pill segmented control (Dashboard / Leaderboard) — white active segment on light gray track.
- Inputs: pill domain-claim field with inline suffix (".link") and embedded gradient submit pill.
- Decorative: oversized soft-gray 3D coins floating behind content on Points; small rounded-square app icon with rainbow ring.

## Signature
- Pastel rainbow gradient mist at the top of every page, dissolving into near-white — the brand's single strongest cue.
- Rainbow-gradient ring used as the accent everywhere (logo mark, Sign up pill border) instead of one flat brand color.
- Italic serif words dropped into sans headlines ("your *forever* space", "earn *Points*").
- Vertical and horizontal dashed hairlines as section connectors and dividers.
- Everything pill-shaped: nav container, buttons, inputs, segmented controls.

## Do / Don't
Do:
- Start pages with a soft multi-hue pastel gradient that fades to white within the first viewport.
- Reserve color for the gradient wash and rainbow rings; keep all UI chrome white/gray with near-black or navy text.
- Use pill geometry consistently — buttons, nav, inputs, tab segments.
- Emphasize one or two words per headline with an italic serif, keeping the rest in the grotesque.
- Separate sections with dashed hairlines and very generous vertical whitespace.

Don't:
- Use a saturated flat brand color for CTAs — the primary button is near-black; the rainbow appears only as gradient borders/washes.
- Add heavy shadows or dark section backgrounds; elevation stays whisper-soft on a light canvas.
- Use sharp or small corner radii; nothing on the site is squarer than ~16px.
- Crowd sections — the about page averages one short paragraph per viewport-height of space.
- Render body copy in full black; text stays muted slate gray with navy reserved for headings.
