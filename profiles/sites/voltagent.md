---
name: voltagent
kind: site
style: DT
category: developer-tools
website: null
pages: [landing]
palette:
  canvas: "#101010"
  ink: "#f2f2f2"
  primary: "#00d992"
  accents: ["#2fd6a1", "#10b981", "#1a1a1a", "#3d3a39", "#bdbdbd"]
typography:
  display: "Inter · regular (400) at hero scale, bolder only at card level · tight negative tracking (-0.65px at 60px)"
  body: "Inter; SF Mono (JetBrains/Geist Mono as substitutes) for code, snippets, and numeric counters"
radius: "small 2-6px (buttons/inputs 6px, cards 8px; 9999px pills only for inline status tags)"
---
## Overview
A dark-only developer marketing surface: one near-black background (#101010) end to end, with a lone electric green (#00d992) doing all the accent work — CTAs, status dots, the lightning logo. Chrome is built from 1px hairline borders rather than fills or shadows, and code-editor mockups with copy buttons sit in the hero. The overall effect is a docs site that happens to be a homepage — engineered, quiet, and terminal-flavored.

## Layout
Sticky dark top nav with small (14px) muted-gray links and a green CTA; mobile collapses to a hamburger that keeps the green button pinned. Hero is a 48px-padded band with an uppercase tracked eyebrow, a 60px regular-weight Inter headline in pure white, and a code mockup card beside or below it. Sections repeat as identical dark bands (48px vertical padding, ~1200-1400px container) hosting 2-3-up grids of hairline-bordered cards; a 1px dashed slate divider or an occasional 2px green border band marks section breaks. No photography anywhere.

## Components
Primary button: solid #00d992 fill with near-black (#101010) text, 6px radius, 600-weight 16px label, ~44px tall. Secondary: same shape, canvas fill with 1px #3d3a39 hairline border; tertiary is a borderless green-text ghost. Cards: canvas-colored with 1px hairline border, 8px radius, 24px padding — no shadows; hover gets a faint gray glow, and "featured" state swaps to a 2px green or 3px hairline border. Inputs and code blocks use a slightly lighter #1a1a1a fill inside the same hairline frame. Inline status tags are the only full pills.

## Signature
- One accent color total: electric green #00d992 owns every CTA, live indicator, and the logo — nothing else gets color.
- Hero headline at 60px in Inter weight 400 with tight tracking — deliberately calm, doc-H1 energy instead of billboard shouting.
- Hairline-bordered rectangles on near-black as the entire elevation system; the sole ornament is a 1px dashed divider between bands.
- Inter/SF Mono pairing where anything typeable at a terminal — commands, chips, metrics — switches to mono.

## Do / Don't
Do:
- Keep #101010 as the sole page surface; there is no light mode and no alternating band colors.
- Express card and button structure with 1px #3d3a39 hairlines; signal hover with a subtle glow, emphasis with a green or thicker border.
- Reserve green strictly for primary CTAs, live/status pills, and the logo mark.
- Set uppercase eyebrows in Inter 600 with wide (+2.5px) tracking above section headlines.
- Put commands and metrics in SF Mono (13px), with the lighter #1a1a1a fill for code chips and inputs.

Don't:
- Don't add a light theme or lighten section backgrounds for rhythm.
- Don't use green as body-text or paragraph link decoration beyond the deep #10b981 inline link.
- Don't apply material drop shadows to cards — hairlines and glow only.
- Don't push the hero headline to 700+ weight; the display voice stays at regular weight.
- Don't make buttons pill-shaped — pills belong only to inline "Live"/"Beta" tags.
