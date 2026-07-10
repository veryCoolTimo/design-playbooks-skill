---
name: flox
kind: site
style: ML
category: dev-platform
website: https://flox.dev/
pages: [home, features, blog, about]
palette:
  canvas: "#FAFAFA"
  ink: "#3F3F46"
  primary: "#C77DF3"
  accents: ["#18181B", "#A855F7", "#F9A86B", "#EDE0F7"]
typography:
  display: "Inter-like grotesque · bold 700 · tight tracking"
  body: "Inter-like grotesque · regular · normal"
radius: "buttons pill; cards medium 8-14px"
---
## Overview
Near-white minimal-light developer landing with near-black text and a signature soft violet-to-peach gradient wash used sparingly as glows and hero art. Content is airy and center-weighted; personality comes from a geometric logo-block motif on a faint blueprint grid and terminal snippets embedded in illustrations. Reads calm and technical, with color reserved for a single purple CTA and gradient keyword highlights.

## Layout
Slim centered top nav: logo left, sparse text links, GitHub star count, pill "Download" button, Login. Home hero is split — bold left-aligned headline with a gradient-purple keyword and a purple pill CTA, geometric gradient shapes on a faint grid to the right. Inner pages (About, Blog, Features) open with a small pill eyebrow tag in purple, then a large centered H1 and short centered paragraph. Sections alternate numbered feature rows (1, 2, 3 with copy left, illustration right inside bordered panels), a 2+3 bento feature grid, and 3-column icon+text rows. Blog is a 3-column card grid with a large featured post row on top. Heavy whitespace between sections; thin hairline dividers; footer is minimal centered logo + link row.

## Components
Buttons: pill shape; primary CTA is solid light purple (#C77DF3) with white label and dropdown caret; secondary is near-black (#18181B) pill with white label; ghost white pill with hairline border in nav. Cards: white fills, 1px light gray borders, 8-14px radius, virtually no shadow (occasional whisper-soft blur on floating UI mocks). Bento cells share hairline dividers rather than gaps. Blog cards: image top (medium radius), tiny purple-tinted pill category tag + date, bold title, gray excerpt. Team cards: small rounded-square photos, name, muted role, tiny social icons. Eyebrow tags: small pill, pale lavender fill, purple text. Terminal blocks: white/near-white panels with monospace type and colored tokens (purple, green) instead of dark terminals.

## Signature
- Violet-to-peach aurora gradient used as thin horizontal glows between sections and as fills for geometric hero shapes.
- Flox logo blocks (parallelogram/chevron shapes) enlarged into abstract section art on a faint blueprint grid with dotted guides.
- Gradient purple highlight on one keyword per big headline ("Environments", "everywhere", "Developers") plus a small sparkle glyph.
- Purple pill CTA paired with a black pill secondary — the only saturated UI elements on an otherwise near-white page.

## Do / Don't
Do:
- Keep the page near-white and let the violet/peach gradient appear only as glows, hero shapes, and one highlighted headline word.
- Use pill buttons everywhere: purple primary, near-black secondary, hairline-bordered white tertiary.
- Introduce sections with a small lavender pill eyebrow tag above a large centered heading.
- Render terminal/code mocks as light panels with monospace colored tokens, keeping the dev flavor without dark blocks.
- Separate cards with 1px hairline borders and shared dividers; rely on whitespace, not shadows.

Don't:
- Don't use heavy drop shadows or dark section backgrounds — the whole site stays light with hairline structure.
- Don't apply the gradient to buttons or large text blocks; CTAs are flat purple, gradients live in decoration and single keywords.
- Don't use rounded-corner-heavy or glassmorphic cards; radii stay modest (8-14px) except pill buttons/tags.
- Don't add more than one accent hue per section — orange appears only inside gradient art, never as UI color.
- Don't crowd sections; every block gets generous vertical padding and a centered, narrow measure for body copy.
