---
name: tuple
kind: site
style: ML
category: dev-collab-saas
website: https://tuple.app/
pages: [home, blog, integrations, pricing]
palette:
  canvas: "#ffffff"
  ink: "#18181b"
  primary: "#4f46e5"
  accents: ["#e0e7ff", "#dc2626", "#2563eb", "#f5f5f5", "#0a0a0a"]
typography:
  display: "Neutral neo-grotesque (Inter-like) · semibold-to-bold · tight, near-default tracking"
  body: "Same neo-grotesque family · regular · gray-toned (#52525b-ish) for secondary copy"
radius: "medium 8-14px (buttons ~8px, cards ~10-14px)"
---
## Overview
A restrained, engineering-first minimal-light system: white canvas, near-black headlines, one indigo CTA color, and lots of air. Product truth carries the design — real macOS app screenshots, real Slack UI mockups, and terminal-flavored details (monospace `/tuple` command chips) replace decorative illustration. Sections alternate white / faint gray / near-black to create rhythm without adding color.

## Layout
Slim single-row nav: logo left, text links (Pricing, Learn, Integrations with chevrons), right-aligned Download / Log in and an outlined Sign up pill-ish button. Heroes are centered: tiny uppercase tracked eyebrow label in an accent color (indigo "PRICING", red "TESTIMONIALS"), a large 2-line headline, one-sentence gray subhead, single indigo CTA, then a large product screenshot floating on soft shadow. Section rhythm: white hero → gray-tinted logo strip → feature grid on faint gray cards → white testimonial wall → full-bleed near-black "Built for developers" section → white closer CTA. Blog and integrations use a 3-column card grid inside a generous max-width container; integrations page mixes centered copy with alternating 2-column text/screenshot rows and hand-drawn arrow doodles pointing at the CTA.

## Components
- Buttons: solid indigo (#4f46e5) fill, white text, ~8px radius, no visible border or heavy shadow; secondary is pale lavender (#e0e7ff) fill with indigo text; tertiary is white with 1px gray border (Sign up, Add to Slack).
- Cards: white fill, 1px very light gray border, ~10-14px radius, whisper-soft shadow; blog cards stack title / gray excerpt / avatar + author + date + read-time meta row.
- Testimonials: bordered white cards with small circular avatars, bold name, gray role line; key phrases bolded inside quote text.
- Pricing: one elevated white card with big price ("$30 / per user per month"), green check-circle feature list with hairline dividers; enterprise column is borderless text beside it. Dashed-border boxes for offer callouts (startup discount, OSS free).
- FAQ: two-column rows (bold question left, gray answer right) separated by hairlines; inline links are blue/indigo underlined.
- Monospace code chips (`/tuple`, `/tuple ls`) with light border and tint for command references.

## Signature
- One indigo, used only for CTAs and links — everything else is grayscale, so the buttons pop hard.
- Real app/OS screenshots (macOS window chrome, Slack UI) as hero art, floated on soft shadows over flat backgrounds.
- Tiny uppercase letter-spaced eyebrow labels in shifting accent colors (indigo, red) above every section headline.
- A full near-black inverted section mid-page ("Built for developers, by developers") breaking the white rhythm.
- Green check-circle bullet lists and hairline dividers doing the structural work instead of boxes and fills.

## Do / Don't
**Do**
- Keep the palette to white, near-black, gray tints, and a single indigo reserved for CTAs and links.
- Lead sections with a small uppercase tracked eyebrow, then a large centered grotesque headline and one gray sentence.
- Use real product screenshots with OS chrome and soft diffuse shadows as the primary visual asset.
- Border cards with 1px light gray and keep shadows barely perceptible; alternate white and #f5f5f5 section backgrounds.
- Set commands and technical tokens in monospace chips; use green check-circles for feature lists.

**Don't**
- Don't add gradients, colored section backgrounds, or decorative illustration — the only non-neutral surfaces are the indigo button and pale lavender secondary.
- Don't use more than one primary CTA per section; secondary actions get the lavender or outlined treatment.
- Don't round corners past ~14px or make pill buttons; the system sits at modest medium radii.
- Don't left-align hero copy — heroes and section intros are consistently centered.
- Don't crowd sections: whitespace between blocks is very generous, and the dark inverted section is used once, not repeatedly.
