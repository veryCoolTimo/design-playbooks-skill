---
name: sanity
kind: site
style: DT
category: content-platform
website: null
pages: [home, pricing, product (studio), campaign (content-agent)]
palette:
  canvas: "#0b0b0b"
  ink: "#ffffff"
  primary: "#ffffff"
  accents: ["#f36458", "#212121", "#ededed", "#0052ef", "#55beff", "#37cd84", "#afe3ff"]
typography:
  display: "waldenburgNormal (ABC Walden-like humanist sans; Inter fallback) · regular 400 at all display sizes · very tight negative tracking (-4.48px at 112px)"
  body: "waldenburgNormal 16px/1.5; IBM Plex Mono only for eyebrows and small labels"
radius: "buttons pill; marketing cards 12px; app-style inputs and studio windows 3-6px"
---
## Overview
A near-black marketing surface treated like an editorial trade journal: one proprietary humanist sans carries every text role, with headlines scaling to 112px at 400 weight and heavily negative tracking. White type on #0b0b0b is the default voice; a single coral-red (#f36458) is rationed to roughly one CTA or highlight per viewport. Commercial pages (pricing) invert entirely to white, and the dark/light flip is used deliberately as the main structural rhythm.

## Layout
Sticky 64px dark nav: red dot + wordmark left, centered menu, right cluster ending in a white pill CTA. Hero is type-only — the mega headline spans the full ~1640px container with subtitle and CTA stacked below. Sections run at 96px vertical rhythm and alternate polarity (dark / white / #ededed paper) with hard cuts, no dividers or gradients. Pricing is a 4-up tier grid over a dense full-width comparison table; the campaign page breaks symmetry with a ~50% text column plus 2-up cards.

## Components
Primary CTAs are 44px pills: white fill with black text on dark sections, black fill on light ones; the coral pill appears only for peak-priority actions. Secondary buttons drop to 36px with 5px corners and #212121 fill. Cards use 12px radius, 32px padding, tonal step (#212121 on dark, white with #ededed hairline on light); shadows are nearly absent — depth comes from surface stepping. The featured pricing tier is marked purely by inverting to black fill, no badge. Inputs are sharp 3px-radius fields; product screenshots sit in 6px "studio window" frames with macOS-style dots.

## Signature
- Mono eyebrow (IBM Plex Mono, 13px) locked above every oversized editorial headline
- Hard dark-to-light polarity flips between sections as the only divider
- Two corner languages coexisting: pill marketing CTAs vs 3-6px application chrome
- Scarce coral-red accent plus the red brand dot beside the wordmark; everything else monochrome

## Do / Don't
Do:
- Default sections to dark canvas; switch to white only for dense commercial content like pricing tables
- Keep all headings at weight 400 and let size plus tight tracking create hierarchy
- Cap coral-red at one use per viewport (a CTA, a highlight card, or the brand dot)
- Enable the display OpenType alternates (cv01, cv11-cv13, ss07) on headlines above 48px
- Give marketing cards 12px corners and 32px padding; keep app-style elements at 3-6px

Don't:
- Don't flood a section background with the coral accent or add new hues (purple, teal, gradients)
- Don't set body or headline copy in IBM Plex Mono — it is a labeling font only
- Don't mix bold/light weight contrast inside headings
- Don't badge the featured pricing tier; the black-fill inversion is the marker
- Don't separate sections with rules or gradients — use the polarity cut
