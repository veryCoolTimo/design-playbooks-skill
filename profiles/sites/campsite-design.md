---
name: campsite-design
kind: site
style: ML
category: design-collab-saas
website: https://www.campsite.design/
pages: [home]
palette:
  canvas: "#FFFFFF"
  ink: "#060606"
  primary: "#F35733"
  accents: ["#EF4D3B", "#F86D1A", "#000000", "#6B6F73"]
typography:
  display: "Geometric grotesque (Roobert/Graphik-like) · bold · tight tracking"
  body: "Inter-like neutral sans"
radius: "pill on buttons; medium 8-14px on cards"
---
## Overview
Ultra-minimal light SaaS landing built almost entirely from white, near-black, and one warm red-to-orange gradient. Content is sparse and declarative — short punchy sentences set in bold black headings with muted gray supporting lines. Product proof comes from embedded UI mockups (browser window, Figma plugin card, Slack notifications) rather than illustration. A full-black inverted section near the footer provides the single dramatic contrast beat.

## Layout
Top nav is skeletal: small logo + wordmark left, a lone pill "Sign in" button right — no menu links. Hero is left-aligned text (headline, two-line gray subhead, gradient CTA) with a hand-drawn arrow + "Your team's WIP" annotation pointing to a large browser-chrome product mockup below. Sections alternate centered and split two-column layouts (text left / mockup right, then flipped), separated by generous whitespace and faint background tint shifts (#FFFFFF vs ~#FAFAFA, plus a subtle grid texture behind the Private & Secure card). Rhythm: hero → centered feature → two-column features → centered trust card → full-bleed black CTA band → thin black footer.

## Components
- Primary CTA: pill button with horizontal red-to-orange gradient (#EF4D3B → #F86D1A), white bold label; repeated in the black section as a white pill with black text.
- Secondary: small light-gray pill ("Sign in"), no border, minimal shadow.
- Cards: white, medium rounded corners, hairline gray borders or very soft diffuse shadows (Slack notification rows, Figma post card, browser mockup with macOS traffic lights).
- File-type chips: solid black circles with tiny white labels (MP4, GIF, PNG) orbiting the logo.
- Small dark pill "Post" button inside the Figma mockup mirrors the pill language at micro scale.
- No visible inputs on the page.

## Signature
- One warm red→orange gradient reserved exclusively for the primary CTA and brand accents on an otherwise black-and-white page.
- Terse, period-ended headline fragments ("Share anything." "Works with Figma." "Stop counting seats.") as the primary section device.
- Realistic in-context product mockups (browser chrome, Figma plugin, Slack messages) instead of abstract art.
- A single full-black section flipping the palette for the closing CTA, with the orange accent line glowing against it.

## Do / Don't
**Do**
- Keep the palette to white, near-black (#060606), gray (#6B6F73), and one red→orange gradient used only on CTAs/brand marks.
- Write headings as short bold declarative sentences ending in periods; pair with 1-3 muted gray lines.
- Use pill buttons everywhere; give cards 8-14px corners with hairline borders or barely-there shadows.
- Show the product via framed, realistic mockups (browser windows, integration cards) with authentic detail.
- End the page with an inverted black band that reuses the accent color for one highlighted line.

**Don't**
- Add nav links, mega-menus, or badges — the header stays logo + one pill button.
- Introduce blues, purples, or a second accent hue; the gradient carries all the color.
- Use large photography, illustration scenes, or decorative gradients on backgrounds — tints stay within #FFFFFF-#FAFAFA plus faint grid texture.
- Set long paragraphs; copy blocks never exceed a few short lines.
- Put sharp-cornered or heavily shadowed elements next to the soft pill/rounded system.
