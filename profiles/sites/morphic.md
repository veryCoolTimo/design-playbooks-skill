---
name: morphic
kind: site
style: DT
category: ai-video-studio
website: https://morphic.com/
pages: [home, about, product-feature]
palette:
  canvas: "#050505"
  ink: "#9b9ba1"
  primary: "#2b6bf3"
  accents: ["#f5f5f5", "#1a1a1c", "#8ab060"]
typography:
  display: "Neo-grotesque sans (Inter/Neue Montreal feel) · medium weight · tight, near-zero tracking"
  body: "Same neo-grotesque sans, small size, regular weight"
radius: "buttons small 4-6px; cards medium 8-12px"
---
## Overview
Near-black cinematic canvas where the UI almost disappears and the product's anime-illustrated video frames carry all the color. Headings are white medium-weight grotesque set small relative to the page; body copy is muted gray. A single saturated blue is reserved for CTAs and tiny "coming soon" pill labels. The effect is a dark theater: restrained chrome, glowing illustrated media.

## Layout
Slim top nav: logo left, centered text links (Studio, About, Blog, Manifesto), one blue "Join Beta" button right. Hero is centered stacked text (two-line headline with period, one-line gray subhead, button pair) followed by a full-width glowing media frame. Sections alternate centered headings with a two-tone pattern: white first line, gray second line ("Morphic Studio. / From ideation to final story."). Long single-column rhythm with huge vertical whitespace between sections; media floats center with small thumbnail satellites scattered around it. Footer features a giant cropped "Morphic" wordmark bleeding off the bottom, plus a horizontal timeline/ruler motif (also used on the About hero as a company-history scrubber).

## Components
Buttons: small, compact, slightly rounded (4-6px); primary is solid saturated blue with white text, secondary is dark gray (#1e1e20) with subtle border, both low-height with small labels ("Apply now", "Learn more", "Join Discord" with icon). Cards: charcoal (#141416) panels with 8-12px radius, thin darker border, icon top-left, white title, gray two-line description (About page benefits grid, 3x2). FAQ: borderless accordion rows with chevron toggles. Tag pills: tiny blue-outlined "Coming soon" labels above feature headings. Screenshots of the product sit in dark app-window frames with soft colored glow spilling onto the black background. No visible drop shadows on UI itself — glow comes only from media.

## Signature
- Vivid anime/illustrated video stills glowing against a pure-black page — the media is the palette
- Two-tone centered headings: white sentence, then gray sentence, both ending with periods
- Giant cropped "Morphic" wordmark and a timeline ruler graphic anchoring the footer
- One small saturated-blue button as the only persistent UI color

## Do / Don't
Do:
- Keep the canvas near-black (#050505) and let product imagery supply all saturation
- End headline sentences with periods and split them white/gray across two lines
- Keep buttons small and quiet — compact height, 4-6px radius, single blue primary
- Frame media in dark app windows with a soft glow halo; scatter small floating thumbnails around a central hero shot
- Use thin-bordered charcoal cards with top-left icons for benefit/feature grids

Don't:
- Introduce a second UI accent color — blue is the only interactive hue on the site
- Use large or pill-shaped CTAs; every button here is understated and small
- Add light-mode sections or white backgrounds; the site never leaves dark
- Put borders, heavy shadows, or bright chrome on the UI — depth comes from media glow only
- Left-align hero or section headings; the layout is consistently center-axis
