---
name: spotify
kind: site
style: CP
category: music-streaming
website: null
pages: [app-shell, browse, search]
palette:
  canvas: "#121212"
  ink: "#ffffff"
  primary: "#1ed760"
  accents: ["#b3b3b3", "#181818", "#1f1f1f", "#f3727f", "#ffa42b", "#539df5"]
typography:
  display: "SpotifyMixUITitle (customized Circular grotesque) · bold 700 · normal tracking"
  body: "SpotifyMixUI (Circular-family sans, huge global-script fallback stack)"
radius: "pill (500px-9999px) on buttons and inputs, 50% circles for play controls; medium 6-8px on cards"
---
## Overview
A near-black theater where the interface deliberately fades out so album artwork supplies almost all color. Every surface is a slightly different charcoal (#121212 base, #181818/#1f1f1f layers), and the single brand green appears only where something is playable, active, or clickable. Type is compact and weight-driven; geometry is relentlessly rounded — pills and circles everywhere.

## Layout
App shell, not marketing page: fixed dark sidebar for navigation, a scrollable main area of grid-based album/playlist cards, and a persistent now-playing bar pinned to the bottom. Spacing runs on an 8px base but stays dense — track lists and card grids are tightly packed, with the dark ground itself doing the separating work instead of whitespace. Card grid collapses 5 → 3 → 2 → 1 columns; sidebar becomes a bottom bar on mobile.

## Components
Buttons are pills in every variant: #1f1f1f dark pills, #eeeeee light pills for rare light-context CTAs, transparent pills with a 1px #7c7c7c outline for follow actions, and perfect circles (50%) for play/pause. Labels are 14px, uppercase, 600-700 weight with 1.4-2px letter-spacing. Cards sit on #181818/#1f1f1f at 6-8px radius with no visible border, lightening slightly on hover and lifting with rgba(0,0,0,0.3) 8px shadows. Search input is a full 500px pill with icon-aware padding and a distinctive inset ring shadow (rgb(124,124,124) 0 0 0 1px inset) instead of a plain border. Dialogs float on heavy rgba(0,0,0,0.5) 24px-blur shadows.

## Signature
- One functional green (#1ed760) against an otherwise achromatic charcoal UI — never used as decoration
- Pill-and-circle geometry on every interactive element; no square buttons anywhere
- Uppercase, wide-tracked button labels that read as system "chrome" distinct from content
- Unusually heavy shadows for a dark theme, making panels feel like they float in darkness

## Do / Don't
Do:
- Build depth from charcoal steps (#121212 → #181818 → #1f1f1f → #252525), not from borders
- Reserve #1ed760 strictly for play controls, active states, and primary CTAs
- Round everything: 500-9999px pills for buttons/inputs, 50% for icon controls, 6-8px for cards
- Keep type in the 10-24px band and lean on the 700-vs-400 weight contrast for hierarchy
- Use strong shadows (0.3-0.5 alpha, 8-24px blur) — faint ones vanish on near-black

Don't:
- Don't paint backgrounds or decorative elements green; the palette is grays plus one accent
- Don't switch primary surfaces to light mode — the dark immersion is the identity
- Don't draw plain gray borders; prefer inset ring shadows or shade contrast
- Don't loosen line-height or scale headlines up like an editorial site; density is intentional
- Don't introduce extra brand hues — reds/oranges/blues exist only as semantic status colors
