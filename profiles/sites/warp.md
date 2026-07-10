---
name: warp
kind: site
style: DT
category: developer-tools
website: null
pages: [home]
palette:
  canvas: "#2b2622"
  ink: "#f7f5f0"
  primary: "#f7f5f0"
  accents: ["#383330", "#c9c0ad", "#3f3a36"]
typography:
  display: "Inter · light-feeling regular 400 · tight negative tracking (-1.6px at 64px)"
  body: "Inter (DM Mono for code, Instrument Serif italic for rare editorial lines)"
radius: "small 2-6px (buttons 3px, cards 4-6px); pill only on icon containers"
---
## Overview
An achromatic dark-tech identity built on a warm brown-tinted charcoal (#2b2622) rather than true black, with a warm off-white (#f7f5f0) serving triple duty as body ink, wordmark, and CTA fill — there is no colored accent anywhere. Typography does the branding: quiet weight-400 Inter headlines with strong negative tracking, DM Mono for terminal content, and a stray Instrument Serif italic for editorial flavor. The whole page reads like a reading-mode editor, not a billboard.

## Layout
One continuous dark band from sticky nav to footer with no section background changes. Hero pairs a 64px headline with a two-column split of terminal screenshots (stacking on mobile), followed by a 5-up partner-logo strip on soft tiles, one testimonial card, hairline-divided press and job rows, and 3-up Mac/Linux/Windows download tiles. Content centers near 1200px; bands carry generous 96px vertical padding while cards stay compact at 24px interior.

## Components
Primary button is an off-white fill with warm-dark text at an unusually tight 3px radius and ~36px height; secondary actions are borderless ghosts on canvas; circular shapes appear only on icon buttons. Cards, inputs, mockups, and tiles all share one recipe: slightly lighter warm surface (#383330) plus a 1px hairline border (#3f3a36) at 4px radius — no drop shadows at any level; elevation is purely surface contrast plus hairlines. List content (press, jobs) uses full-width rows separated by bottom hairlines instead of cards.

## Signature
- Warm brown-charcoal canvas — a deliberate tint away from both pure black and neutral gray
- Zero chromatic accent: one off-white token is text, logo, and CTA simultaneously
- Near-rectangular 3px CTA buttons paired with weight-400, tightly tracked hero type
- Terminal-mockup screenshots as the only decoration — no gradients, illustration, or atmosphere

## Do / Don't
Do:
- Keep every neutral warm-tinted (backgrounds, text tiers, hairlines all carry the brown-beige cast)
- Set display type in Inter 400 with negative tracking scaling from -1.6px down
- Build elevation from canvas-soft fills plus 1px hairlines only
- Use DM Mono strictly for code/terminal content and Inter for everything narrative
- Hold CTA radius at 3-4px — almost rectangular

Don't:
- Introduce any hue-carrying accent color; the off-white on warm-dark is the entire palette
- Swap the canvas for pure black or neutral gray — the warmth is the identity
- Bold the hero (700+) or loosen its tracking
- Round CTAs into pills; reserve full-round shapes for icon containers
- Add drop shadows to cards or modals
