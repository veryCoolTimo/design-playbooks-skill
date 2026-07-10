---
name: three-tools
kind: site
style: DT
category: developer-tools
website: https://three.tools/
pages: [home]
palette:
  canvas: "#000000"
  ink: "#e0e0e0"
  primary: "#ff4505"
  accents: ["#ff6644", "#e8632c", "#ffffff", "#181818"]
typography:
  display: "Inter/SF-style neo-grotesque · bold-to-heavy · tight, slightly negative tracking"
  body: "Same neo-grotesque (Inter/SF Pro feel), regular weight, mid-gray on black"
radius: "pill on buttons and inputs; large 16-24px on cards"
---
## Overview
Pure-black single-page launch site with an Apple-keynote feel: giant 3D-rendered product mascot (glossy red-orange tri-tube logo) floating over #000, heavy grotesque headlines, and one hot orange-gradient CTA. Everything else stays in a narrow grayscale band (#111-#e0), so the red/orange product renders and UI screenshots carry all the color.

## Layout
Minimal sticky-feel top bar: white rounded-square logo + wordmark with a tiny "beta" chip on the left, a single white pill "Get access" button on the right — no nav links at all. Hero is centered: 3D logo with Blender-style selection-handle overlays, two-line headline, two-line subcopy, then a white pill email-capture form. Sections alternate full-bleed product screenshot, a 3-column testimonial strip, a centered 2-line section headline ("Work Smarter, Move Faster."), a 2-column bento grid of six feature cards, a founder-story split (device mockup left, letter-style text right), a beta signup block with a giant gray "Beta" wordmark and dark 3D logo, and a single-column FAQ accordion. Generous vertical whitespace; content column stays narrow and centered.

## Components
- Primary CTA: pill button with vertical orange gradient (#ff6644 → #ff4505), white bold label, embedded inside a white pill input ("Type your email…" in gray placeholder).
- Nav CTA: inverse treatment — white pill, black bold label, small red circular "+" icon.
- Feature cards: near-black (#0d-#11) rounded 16-24px tiles on pure black, hairline-subtle edges, each containing a cropped dark UI screenshot; card headline pattern is bold white lead phrase + gray continuation ("Chrome extension. Use it in any live project.").
- FAQ: full-width dark-gray (#181818) pill rows, bold light-gray question text, circular "+" toggle at right.
- Status chip: small pill with red cloud icon + "Registration closed" bold + gray arrow text.
- Segmented control and selected-row highlight in screenshots use solid orange fills with white text.

## Signature
- Glossy red-orange 3D "tri-tube" mascot recurring in every major section (hero, extension screenshot, dark variant in beta block) — the brand IS the render.
- Two-tone headline device: white bold phrase, then the rest of the sentence in mid-gray at the same size.
- Only two chromatic elements on the whole page: the orange CTA gradient and the red/orange renders; everything else is black-to-gray.
- White pill forms and buttons punched out of a pure #000 canvas for maximum CTA contrast.

## Do / Don't
Do:
- Keep the canvas true #000 (or a barely-visible radial lift to #0d0d0d) and let 3D renders and screenshots supply the color.
- Use the white-bold + gray-continuation pattern for card and section headlines instead of separate title/subtitle blocks.
- Make every interactive element a pill: CTAs, email input, FAQ rows, chips.
- Reserve the orange gradient (#ff6644→#ff4505) exclusively for the one conversion action per section.
- Frame product UI inside dark rounded cards or browser-chrome mockups rather than floating screenshots.

Don't:
- Add nav links, mega-menus, or footers with columns — the chrome is deliberately just logo + one button.
- Introduce blues, greens, or purples; the palette is strictly black/gray/white plus one red-orange family.
- Use borders or drop shadows to separate cards — separation comes from a slight luminance step over black.
- Set headlines in thin or wide-tracked type; the voice is heavy, tight, Apple-grotesque.
- Put long paragraph copy outside the founder-letter section; everywhere else text is two lines max.
