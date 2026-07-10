---
name: langbase
kind: site
style: DN
category: ai-infra-saas
website: https://langbase.com/
pages: [home]
palette:
  canvas: "#000000"
  ink: "#909090"
  primary: "#ffffff"
  accents: ["#8979e0", "#e1c33a", "#061164"]
typography:
  display: "Inter-style neo-grotesque · bold to heavy · tight, near-default tracking"
  body: "Inter-style neo-grotesque (regular, gray-on-black)"
radius: "pill buttons; large 16px+ cards"
---
## Overview
Near-total-black canvas with white typography and mid-gray body copy; color is rationed to a deep-blue cosmic hero render, a violet section eyebrow, and one yellow eyebrow. The single white pill CTA is the brightest object on the page, so it always wins attention. Product UI screenshots and diagram cards sit in slightly-lighter charcoal panels with hairline borders, giving a dev-tool, terminal-adjacent feel.

## Layout
No visible persistent nav bar in the hero — the page opens on a full-viewport black-hole/space render with an outlined command (⌘) glyph, one-line title, three-line subhead, and a centered white pill CTA plus a ghost "Video demo" secondary. Sections stack in a strict center-axis rhythm: small colored eyebrow line, huge bold H2 (often two lines), 2-4 line gray paragraph, then a large visual block. Feature area uses an asymmetric bento grid (one narrow + one wide card, then a 2:1:1 row). Social proof is a marquee of pill logo chips and a masonry wall of testimonial cards. Massive vertical whitespace between sections; a scrolling ticker strip ("⌘ Langbase — Composable AI for developers") divides major chapters. Footer repeats the logo + tagline + CTA pair, then a single row of links.

## Components
Buttons: primary is a solid white pill with black label and small ⌘ glyph; secondary is borderless text with icon in gray. In-product buttons (screenshots) are small gray rounded rectangles. Cards: charcoal (#0a0a0a-ish) panels with 16-24px radius and 1px low-contrast borders, no visible shadows; bento feature cards mix text blocks with embedded diagrams. Chips/tags: pill-shaped, hairline-bordered, used for logo marquee and feature-keyword clouds (Versioning, Logs, Streaming...), with an occasional white-filled active chip. Tab row for Studio features uses plain gray text labels with one active item in a subtle pill. Inputs appear only inside product screenshots: dark fields with faint borders.

## Signature
- Pitch-black page where the only saturated color is the deep-blue space render in the hero; everything after is grayscale plus one violet and one yellow eyebrow.
- The ⌘ (command) glyph as a recurring brand mark: outlined hero emblem, inline before the wordmark, inside the CTA pill, even mid-sentence in copy.
- White pill CTA ("⌘ Get started" / "⌘ Start free") repeated top and bottom as the sole high-contrast element.
- Hand-written annotation script with a curved arrow overlaid on the diagram card — a single playful gesture in an otherwise austere layout.

## Do / Don't
- Do keep the canvas true #000 and lean on gray scale (white headings, #909090 body) for nearly all hierarchy.
- Do use one solid white pill CTA per viewport with a black label and the brand glyph; pair it with a plain text secondary link.
- Do introduce each section with a small colored eyebrow (violet by default) over a very large bold centered H2.
- Do frame product screenshots and diagrams in large-radius charcoal cards with 1px faint borders, no drop shadows.
- Do use pill-shaped hairline chips for logos and keyword clouds.
- Don't spread the neon accents around — violet/yellow appear only as eyebrow text, never as button fills or backgrounds.
- Don't add gradients or glow outside the hero's space imagery; mid-page sections stay flat black.
- Don't use colored or outlined primary buttons — the CTA is always solid white.
- Don't left-align section intros; headline/paragraph stacks are center-axis throughout.
- Don't brighten body copy to white — long copy stays mid-gray to keep headings and CTAs dominant.
