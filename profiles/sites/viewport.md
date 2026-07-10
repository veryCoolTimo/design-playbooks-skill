---
name: viewport
kind: site
style: ML
category: portfolio-saas
website: https://viewport.co/
pages: [home, feature-landing, product-tool, changelog, use-cases]
palette:
  canvas: "#FFFFFF"
  ink: "#5F6470"
  primary: "#1B9AFF"
  accents: ["#4F46E5", "#EEEDFB", "#8FEBC0", "#F4F5F7"]
typography:
  display: "Inter-like geometric grotesque · semibold · tight, near-default tracking"
  body: "Inter-like geometric grotesque, regular, gray rather than black"
radius: "buttons pill; cards medium 8-14px; screenshot frames large 16px+"
---
## Overview
A bright, airy minimal-light SaaS language built almost entirely from white space, gray UI screenshots, and two blues: an azure CTA blue and an indigo accent used for icons, links, and eyebrow labels. Headlines are near-black semibold grotesque; everything else recedes into mid-gray. Product screenshots do the visual heavy lifting inside softly rounded, lightly bordered frames, with occasional playful touches (an italicized word in a headline, chat-bubble callouts, scattered tilted cards).

## Layout
Slim white sticky nav: logo left, four centered text links, ghost "Sign in" + filled pill "Sign up" right. Heroes are centered: H1 (sometimes with one italic phrase or a blue-highlighted phrase), 2-line gray subhead, one or two pill buttons, then a large product visual. Sections alternate white and very light gray (#F4F5F7) full-width bands; content sits in a narrow centered column (~700-1000px) with generous vertical padding. Feature rows use 3-up icon cards; the updates page is a single-column changelog with date in the left gutter, image card, title + colored tag pill, and paragraph. Every page ends with a light-gray footer of 3 link columns above a decorative field of scattered, rotated gray rectangles fading downward.

## Components
Buttons: pill-shaped; primary is solid azure blue (#1B9AFF) with white text and a soft blue glow-shadow; secondary is white with a thin gray border and gray text; the nav Sign up pill leans indigo. Cards: white, 1px light-gray border, 8-14px radius, essentially shadowless; use-case cards pair left text with a right screenshot on a tinted (mint, gray, beige) background panel. Eyebrow labels: small indigo caps text or lavender (#EEEDFB) pill tags with indigo text; changelog tags in the same style. Screenshot frames: large radius, thin border or dark-chrome browser mock. Small line icons in indigo atop feature cards. Testimonials: bordered white cards with avatar, quote, and blue-highlighted key sentences.

## Signature
- Scattered, randomly rotated flat gray rectangles ("floating screenshots") as a decorative field below the footer on every page
- Two-blue system: azure fill for CTAs, indigo for icons, tags, links, and the logo
- One italicized or blue-colored phrase inside an otherwise plain black headline
- Real product screenshots framed in rounded, thin-bordered cards, sometimes with before/after slider or chat-bubble annotations
- Lavender pill eyebrow/tag labels (indigo text on #EEEDFB) marking sections and changelog entries

## Do / Don't
Do:
- Keep the page white with light-gray (#F4F5F7) alternating bands and let screenshots carry the color
- Use pill buttons: solid azure with soft glow for the single primary action, thin-gray-bordered white for secondary
- Reserve indigo for small elements — icons, tag pills, eyebrow caps, inline links — never large fills
- Set body copy in mid-gray, noticeably lighter than the near-black headings
- Add one playful accent per hero (italic word, blue phrase, or callout bubbles) and stop there

Don't:
- Don't add drop shadows to cards — the system relies on 1px borders and whitespace
- Don't use dark backgrounds except inside screenshot chrome/mockups
- Don't introduce warm accent colors into UI chrome; mint/beige appear only as screenshot backdrop panels
- Don't crowd sections — each section holds one idea with large vertical padding
- Don't square off buttons or mix radii wildly; pills for actions, ~12px for cards, 16px+ for media frames
