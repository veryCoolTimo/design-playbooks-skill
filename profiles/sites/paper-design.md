---
name: paper-design
kind: site
style: ML
category: design-tools
website: https://paper.design/
pages: [home, home-dark]
palette:
  canvas: "#FCFDF8"
  ink: "#222220"
  primary: "#181816"
  accents: ["#F05A0D", "#B41A58", "#38A166", "#0D3E80", "#EFEFE3"]
typography:
  display: "neo-grotesque sans (Neue Haas / Helvetica Now feel) · light-to-regular weight · normal-to-slightly-tight tracking"
  body: "same neo-grotesque sans, regular weight"
radius: "small 2-6px on buttons/inputs; medium 8-14px on cards and the app-window frame"
---
## Overview
A quiet, near-monochrome paper-and-ink landing page for a design canvas tool. Big off-white panels float on a warm putty (#EFEFE3) page frame, all copy is lowercase and set in a single restrained grotesque, and color arrives only through the product itself: an embedded app screenshot with bold orange/blue/green/yellow shapes and a confetti-dot "Paper Shaders" card. A full dark-mode twin inverts everything to near-black (#080808) with cream text (#EDEDE1) and a cream CTA, while the accent hues stay identical.

## Layout
Slim single-row nav: logo left, a centered announcement line ("announcing our $4.2M seed, led by Accel →"), and three plain text links right — no nav CTA button. Hero is left-aligned text-only: a three-line lowercase heading (first line ink, rest gray), then an inline email-capture bar (input + dark button fused in one rounded pill-ish field), then a huge full-width product screenshot bleeding off the bottom of its panel. Mid-page: one panel containing nothing but a centered 6-line manifesto paragraph — extreme whitespace. Below, a three-card equal-width row (job posting, seed announcement, shader teaser). Footer is a black band with an oversized viewport-width "make it real" wordmark in gray, cropped by the edges. Sections read as discrete rounded panels separated by thin putty gutters, with a faint dotted/plus grid texture in the page margins.

## Components
- Primary CTA ("get early access"): near-black #181816 fill, white lowercase label, small radius, sits flush inside the email input's bordered container; in dark mode it inverts to cream #FAFAF2 with dark text.
- Secondary CTA ("read the announcement →"): full-card-width dark bar with arrow, same small radius.
- Email input: white fill, hairline border, gray lowercase placeholder.
- Cards: flat, borderless-to-hairline, same off-white as panels — no shadows anywhere; hierarchy comes from spacing and a bold lowercase card title. Job card uses a blueprint-style pen-nib line illustration in light blue.
- Product screenshot framed as a mac-style app window (traffic lights, tabs) with medium radius.

## Signature
- All-lowercase typography everywhere — headings, buttons, nav, even the manifesto.
- One grotesque family at calm weights; scale and gray-value shifts (ink line 1, gray lines 2-3) do the hierarchy work, not boldness.
- Color quarantined to product imagery: the chrome is monochrome cream/black, the canvas content is saturated orange/magenta/green/blue.
- Giant cropped footer wordmark ("make it real") spanning the full viewport on a black band.
- Perfect light/dark mirroring: same layout, same accents, inverted neutrals (cream on #080808).

## Do / Don't
Do:
- Keep every string lowercase, including CTAs and nav links.
- Build hierarchy with size and ink-vs-gray text color, not weight jumps or accent-colored headings.
- Float near-white content panels on the warmer #EFEFE3 frame with visible gutters and a subtle dot/plus grid in the margins.
- Let saturated color appear only inside product artwork, screenshots, and illustrations.
- Ship the dark variant as a true inversion (#080808 canvas, cream text, cream primary button) with unchanged accent hues.

Don't:
- Add drop shadows, gradients, or glassmorphism — the site is entirely flat with hairline separation.
- Use a colored primary button; the CTA is near-black in light mode and cream in dark mode, never orange or blue.
- Introduce a second typeface or heavy bold display weights; the grotesque stays light-to-regular even at footer-wordmark scale.
- Crowd sections — the manifesto panel is one paragraph in a full-height panel; preserve that emptiness.
- Round panels into pills; radii stay small on controls and modest on cards.
