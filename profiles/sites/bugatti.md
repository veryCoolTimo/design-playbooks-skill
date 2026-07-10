---
name: bugatti
kind: site
style: EL
category: luxury-automotive
website: null
pages: [home, model-detail, newsroom, careers]
palette:
  canvas: "#000000"
  ink: "#cccccc"
  primary: "#ffffff"
  accents: ["#c3d9f3", "#141414", "#999999", "#262626"]
typography:
  display: "Bugatti Display (sub: Saira Condensed) · regular 400, never bold · very wide (2-4px, wordmark 6px), always uppercase"
  body: "Bugatti Text Regular, a serif text face (sub: Cormorant/EB Garamond); Bugatti Monospace (sub: JetBrains Mono) for buttons, nav, captions"
radius: "none on cards/photos/inputs (0px); buttons are pill (9999px) — a strict binary"
---
## Overview
The most stripped-down surface in luxury automotive: pure black everywhere, white uppercase display type with generous tracking, and edge-to-edge car photography carrying all the visual energy. There is no accent hue, no gradient, no shadow, no decorative mark beyond the wordmark itself. A rigid three-font system — condensed display, serif body, monospace UI labels — replaces every conventional branding device.

## Layout
A 56px transparent nav overlays the hero photo: "MENU" left, centered 14px wordmark at 6px tracking, "STORE" right. Heroes are full-bleed photo bands with a centered 64px uppercase h1, a small mono caption, and one outlined pill CTA. Content sits in a ~1280px container while photography always bleeds full width. Major bands sit 120px apart — deliberately airier than typical marketing pages, since sections are mostly image plus a sentence. Newsroom runs a 2-up grid (1-up mobile); careers and spec tables are hairline-divided single-column rows.

## Components
Primary button: transparent fill, 1px white outline, pill shape, 44px tall, monospace uppercase label at 2.5px tracking — the transparent pill is the entire button language. Icon buttons are 40px outlined circles. Cards are 0px-radius and nearly indistinguishable from the canvas (#141414 at most), with no shadow; depth comes only from photography. Inputs are borderless except a bottom hairline (#3a3a3a) that turns white on focus. Tags and dates are bare muted monospace text — no chips, no fills. Links use the lone chromatic token, ice-blue #c3d9f3, underlined.

## Signature
- Transparent outlined pill CTA on pure black — no filled button exists anywhere
- Three-typeface trinity with strict roles: display headlines, serif paragraphs, monospace buttons/nav/captions
- Zero bold weight; hierarchy built entirely from size, tracking, case, and family contrast
- Only one non-monochrome color in the whole system (ice-blue inline links)

## Do / Don't
**Do**
- Lead every section with full-bleed automotive photography; let the black void around it do the framing
- Set all headlines uppercase at weight 400 with 2-4px letter-spacing (wordmark at 6px)
- Keep the font trinity intact: monospace for any button/nav/caption, serif only for running prose
- Hold 120px between editorial bands even when it feels excessive
- Keep primary CTAs as transparent 1px-outlined pills

**Don't**
- Don't add any color beyond black/white/grays and the #c3d9f3 link blue
- Don't use bold anywhere — 400 is the only weight in the system
- Don't fill a button or round a card; radius is strictly 0px except button pills
- Don't tighten headline tracking or drop the uppercase treatment
- Don't add shadows, gradients, or card chrome — photography is the sole depth device
