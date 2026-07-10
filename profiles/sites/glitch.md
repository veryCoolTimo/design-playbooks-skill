---
name: glitch
kind: site
style: CP
category: dev-tools-community-saas
website: https://glitch.com/
pages: [home, discover, pricing]
palette:
  canvas: "#EAF8EF"
  ink: "#222222"
  primary: "#CDF3E6"
  accents: ["#6C5CE7", "#F857A0", "#14B0C7", "#FBF7B8", "#F8C3DC"]
typography:
  display: "Benton Sans-like humanist grotesque · extra bold · tight"
  body: "Same humanist grotesque, regular weight; monospace (Courier-style) for buttons, code snippets, and pull quotes"
radius: "small 2-6px (buttons ~2-4px, cards ~4-8px)"
---
## Overview
Candy-pastel playground for coders: soft vertical gradients (mint-to-cream on home/discover, hot-pink-to-white on pricing) carry flat, thick-outlined cartoon illustrations of people, browser windows, and stickers. Big bold sans headlines are set in saturated purple, pink, cyan, and gold — often multiple colors within one sentence. Interactive elements go the opposite way: austere white or mint rectangles with 1px black borders and monospace labels, like UI chrome from a code editor dropped into a coloring book.

## Layout
Slim white sticky nav: logo left, three text links center (one with an emoji marker), search icon plus two small bordered Log in / Sign up buttons right. Home hero is a full-width multicolor headline over an oversized illustration, with a numbered, syntax-highlighted feature list beside it. Sections alternate centered intros, two-column starter-template grids with small icon thumbnails, and zig-zag rows (illustration one side, text the other). Community content sits in bordered "playlist" panels holding rows or 3-up cards with a "by Community" footer bar. Pricing uses two bordered plan cards side by side plus a full-width gray Teams band, then a grayscale logo strip, a monospace pull quote, and a two-column FAQ over blurred pastel star shapes. Generous whitespace; content column roughly 1000px.

## Components
Buttons: rectangles with ~2-4px radius, 1px solid black border, monospace labels, no shadow; fills are white ("Remix it!", often with a leading emoji) or pale mint ("Choose Starter", "Choose Pro", "Let's go"). Nav buttons are the same white-bordered style at small size. Cards: white fill, 1px gray-to-black border, small radius, flat or with a faint offset shadow on playlist panels; list-row cards inside panels have their own hairline borders. Links: colored text (pink or purple) with a thick underline in a contrasting color; some arrow-suffixed micro-links ("blank version →"). Inputs: underline-only text field for the GitHub import, monospace placeholder. Checklist items use plain blue-violet checkmarks. Quote marks and diamond illustration on pricing get a neon purple outline glow.

## Signature
- Multicolor headlines: a single sentence cycling through pink, purple, green, and gold with thick contrasting underlines on inline links.
- Monospace, black-bordered, sharp-cornered buttons with emoji prefixes ("🍒 Remix it!") against soft pastel gradients.
- Flat sticker-style illustrations with bold outlines and pink/teal/purple fills scattered through every section.
- "Playlist" panels: bordered containers of community app cards with a "by Community / View all" footer strip.

## Do
- Build backgrounds as soft vertical pastel gradients (mint→cream, pink→white) and keep the nav/footer flat white.
- Set headlines in one heavy sans and let color, not size contrast, do the theatrics — alternate purple/pink/cyan per phrase.
- Use monospace for all button labels, quotes, and anything code-adjacent; pair it with 1px black borders and near-square corners.
- Sprinkle emoji into buttons, nav items, and card titles as functional decoration.
- Frame community/user content inside bordered panels with attribution footers rather than free-floating cards.

## Don't
- Don't use large border radii, pill buttons, or heavy drop shadows — everything here is flat, thin-bordered, and near-square.
- Don't fill CTAs with saturated brand color; the strongest fill on a button is pale mint, and hierarchy comes from borders and placement.
- Don't render illustrations as gradients or 3D — they are flat, outlined, sticker-like shapes.
- Don't set headlines in a single sober color; monochrome type kills the identity.
- Don't darken the palette — ink is near-black on pastel; there is no dark section anywhere.
