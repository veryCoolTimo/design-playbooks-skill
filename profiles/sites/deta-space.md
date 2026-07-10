---
name: deta-space
kind: site
style: GR
category: cloud-platform
website: https://deta.space/
pages: [home]
palette:
  canvas: "#fdf6eb"
  ink: "#746d61"
  primary: "#ee72a8"
  accents: ["#95a8eb", "#6787a7", "#131215"]
typography:
  display: "high-contrast bold condensed serif (Abril/Playfair feel) · heavy · tight; eyebrows in a retro connected script"
  body: "IBM Plex Mono-like monospace"
radius: "medium 8-14px buttons; large 16px+ cards and icon tiles"
---
## Overview
A storybook take on a cloud platform: hand-painted Ghibli-style sky gradients (indigo night fading to pink dawn, cumulus clouds, a red prop plane) sit on a warm cream paper canvas. Near-black condensed serif headlines pair with monospace body copy and cursive script eyebrows, so the page reads like an illustrated manual crossed with a terminal. One candy-pink button color carries every CTA.

## Layout
Minimal transparent nav over the hero sky: small logo left, only "Login / Sign up" (mono) right — no menu links. Hero is a full-bleed painted gradient sky with sparkle stars, script kicker ("The Personal"), giant serif title, short mono paragraph, single pink CTA. Sections alternate between cream text blocks and full-width painted illustration bands (clouds, machinery, plane) that act as dividers. Every text section repeats the same centered rhythm: script eyebrow → serif headline → narrow mono paragraph → optional CTA. A 5-column app-card grid mid-page; one near-black (#131215) section for developers breaks the cream before a final cloud illustration and a plain multi-column mono footer.

## Components
Primary buttons: solid pink (#ee72a8) rounded rectangles (~10-12px) with a slightly darker pink border/edge giving a faint raised look, white monospace label; used identically at every scale. App cards: off-white (#fffaf0) rounded cards (~16px) with hairline warm border and very soft shadow, holding a large rounded-square gradient icon tile, bold mono title, muted mono description. One pill-shaped mono input ("Post actions...") with soft inset look. Chat/UI mockups are flat cream panels with thin borders, no heavy elevation.

## Signature
- Painted anime-style sky and cloud illustrations used as full-width section dividers, blending into the cream canvas
- Three-voice type system: cursive script eyebrows (pink or dusty blue), heavy condensed serif headlines, monospace everything else (body, buttons, nav, footer)
- Single candy-pink CTA color repeated verbatim across the whole page
- Warm cream paper background (#fdf6eb) with subtle grain instead of white

## Do / Don't
Do:
- Keep the section formula rigid: script eyebrow, centered serif headline, narrow centered mono paragraph
- Set all UI chrome (nav, buttons, labels, footer) in the monospace, reserving the serif for headlines only
- Use full-width illustrations as transitions between sections rather than boxed inline images
- Feather illustration edges into the cream canvas with gradient fades, never hard crops
- Stick to one pink for every CTA and let painted art supply the rest of the color

Don't:
- Use pure white backgrounds or cool grays — everything sits on warm cream
- Add nav menus, mega-menus, or secondary link rows; the header carries only auth links
- Introduce ghost/outline or secondary button styles — only the solid pink button appears
- Use sans-serif headlines or photographic imagery; the identity depends on serif + script + painted art
- Pile on shadows or glassmorphism; elevation stays at hairline borders and whisper-soft card shadows
