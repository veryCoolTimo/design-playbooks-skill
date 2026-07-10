---
name: theverge
kind: site
style: BT
category: tech-media
website: null
pages: [homepage]
palette:
  canvas: "#131313"
  ink: "#ffffff"
  primary: "#3cffd0"
  accents: ["#5200ff", "#3860be", "#2d2d2d", "#949494", "#3d00bf"]
typography:
  display: "Manuka (Klim) · black 900, condensed · near-zero tracking, 0.80 leading"
  body: "PolySans (mono variant for ALL-CAPS labels; FK Roman Standard for rare serif pulls)"
radius: "pill buttons 24-40px; cards 20-24px; inputs tight 2px"
---
## Overview
A dark-only editorial system built on a near-black canvas where acid-mint and ultraviolet act like warning tape rather than decoration. Headlines are set in an ultra-heavy condensed display face at up to 107px, and stories arrive as saturated color-block pills (yellow, pink, orange, mint, purple) stacked in a vertical timeline. Depth comes entirely from 1px hairline borders and solid color fills — no shadows, no gradients, anywhere.

## Layout
Thin dark nav bar with mono-uppercase category links and a single mint pill CTA on the right; below it the wordmark itself is rendered at hero scale as a page element. Content flows through a ~1280px container: a multi-column feature zone plus the signature "StoryStream" — a single-column feed where each post is a 20px-radius tile hanging off a 1px dashed/solid vertical rail with a mono uppercase timestamp on the left, like a git log for news. Section rhythm alternates stretches of empty near-black with loud full-saturation tiles; spacing is 8px-based with 32-64px between sections and tight 12-16px gaps inside the stream.

## Components
Buttons are full pills: mint fill with black text (primary), dark slate #2d2d2d with off-white text (secondary), and 1px mint- or ultraviolet-outlined transparent pills (tertiary/promo) at 30-40px radius. Button labels are often mono, uppercase, 1.5px tracked. Cards are either dark tiles with a 1px white hairline or solid accent-color blocks with black/white text; hover never lifts or scales — only the headline color shifts to #3860be. Inputs break the pill pattern: 2px radius, 1px white/gray border on dark, focus border turns mint. Nested images get 3-4px corners inside 20-24px tiles with a 1px #313131 frame.

## Signature
- Vertical timeline feed of pill-cornered story tiles on a dashed rail with mono UPPERCASE timestamps
- Whisper-vs-shout typography: 107px black-weight condensed headline paired with a 19-20px weight-300 tracked-out eyebrow
- Elevation by color, not shadow: important stories become fully saturated mint/purple/yellow/pink blocks
- Universal link hover to deep blue #3860be, color-only, no underline

## Do
- Keep every view on the #131313 canvas — this system has no light mode
- Reserve the heavy display face for 60px+ headlines; everything smaller belongs to the grotesque workhorse
- Set all kickers, tags, timestamps, and button labels in UPPERCASE mono with 1.1-1.9px tracking
- Elevate a story with a solid accent fill or a 1px mint/violet border, never a box-shadow
- Hover every link to #3860be regardless of its resting color

## Don't
- Don't add gradients, glows, or soft shadows — the flat hazard-tape look depends on hard edges
- Don't use square corners on any container; even inputs get a token 2px
- Don't let mint or ultraviolet wash across backgrounds — they are accents applied in small doses or full tile blocks only
- Don't set the mono face in lowercase or run the display face at UI sizes
- Don't put #3cffd0 text under 16px on the dark canvas — it vibrates
