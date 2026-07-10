---
name: gitness
kind: site
style: DT
category: developer-tools
website: https://gitness.com/
pages: [home]
palette:
  canvas: "#070709"
  ink: "#8b8b8e"
  primary: "#ffffff"
  accents: ["#75d9c7", "#958ac2", "#8bb2b3"]
typography:
  display: "Inter-like neo-grotesque · semibold to bold · tight, near-default tracking"
  body: "Same neo-grotesque sans, regular weight, small sizes (~14-16px)"
radius: "pill buttons; medium 12-16px cards"
---
## Overview
Near-black cinematic dark-tech. The page is one continuous #070709 void punctuated by photographic 3D renders — a light-streaked road, iridescent glass primitives, a chromed "4x" — that glow out of the darkness. UI chrome is minimal and monochrome; color arrives only through render lighting (violet, mint, amber) and tiny status accents. Headings are crisp white; everything else recedes into gray.

## Layout
Slim single-row nav: logo left, sparse links + white pill CTA right, sitting directly on the black canvas with no bar background. Hero is left-aligned text (3-line heading, pill CTA) with floating terminal-command pills at right and a full-bleed 3D "road" render bleeding behind the fold. Sections alternate between left-aligned eyebrow-label + heading blocks and center-aligned statement sections ("Your Code / Your Language / Your Platform", "Up to 4x faster"). Rhythm: big feature card full-width, then a 2-up card row beneath it — repeated for both the Code Hosting and Pipelines sections. Feature-pill chip rows and a 3-column template-card grid break up the card blocks. Generous vertical whitespace (screen-height gaps) between sections; content column stays narrow against the wide black field.

## Components
Buttons: white pill fill with dark text and a "›" chevron ("Get started"), plus a ghost/outlined pill variant ("Try it now") — both small and quiet. Cards: very dark gray fills (#15191f–#1f212c) a step above the canvas, 12-16px radius, no visible borders or shadows — separation comes purely from the fill lightening. Large feature cards embed either giant duotone display text ("Commit. Branch. Merge." in sage, "Build. Test. Deploy." in steel blue) next to mock UI panels, or full-bleed renders. Chips/pills: thin-bordered dark capsules with small icons (feature lists, terminal commands). Commit-list mock rows use mint #75d9c7 status checks. Eyebrow labels are tiny colored/gray caps above headings.

## Signature
- Photoreal 3D renders as the only real color: iridescent glass cones/tori/cubes, a chrome "4x", a lit road at night — floating on pure black.
- Giant muted-color display words inside cards ("Commit. Branch. Merge.") acting as illustration, not copy.
- White pill CTA as the single high-contrast interactive element on the page.
- Borderless near-black cards that separate from the #070709 canvas by a barely lighter fill.

## Do / Don't
**Do**
- Keep the canvas one continuous near-black (#070709) and let card fills lighten only 5-10% to define surfaces.
- Use a solid white pill with dark text for every primary CTA; repeat it per section rather than inventing variants.
- Bring color through imagery — glowing 3D renders and duotone display type — not through UI chrome.
- Pair a tiny colored eyebrow label ("Code Hosting", "Pipelines") with a two-line white heading for each section.
- Reserve saturated mint (#75d9c7) for status/success micro-elements inside product mockups.

**Don't**
- Don't add borders, drop shadows, or gradient strokes to cards — the design relies on flat fill steps.
- Don't use a colored/gradient CTA button; nothing on this page uses a chromatic button fill.
- Don't brighten body text past mid-gray — copy sits around #8b8b8e and deliberately recedes.
- Don't fill the whitespace between sections; screen-height black gaps are part of the rhythm.
- Don't render illustrations flat/vector — the language is photographic, lit, and dimensional.
