---
name: standards-site
kind: site
style: DT
category: design-tools-saas
website: https://standards.site/
pages: [home]
palette:
  canvas: "#000000"
  ink: "#ffffff"
  primary: "#fe2e00"
  accents: ["#101010", "#242424", "#464445", "#e1e1e1"]
typography:
  display: "Söhne-style grotesque (Söhne/Neue Haas) · bold/heavy · tight, near-default tracking"
  body: "Same grotesque, regular weight, generous line height"
radius: "small 2-6px on buttons; medium 8-14px on testimonial/plan cards"
---
## Overview
Pure-black editorial dark theme where the product's colorful brand-guideline artwork does all the decorating. The chrome is strictly monochrome — white grotesque type on #000000 — with a single searing red-orange (#fe2e00) reserved for CTAs and the trademark period that ends every headline. Feels like a printed design manual translated to a screen: typographic, restrained, confident.

## Layout
Slim top nav: lowercase wordmark "standards." left, four plain text links plus a gray Sign in and a red Join waitlist button right. Hero is text-only — a two-line bold headline left-aligned in a wide centered column, small one-line subhead far below it, no hero CTA — followed by a full-bleed edge-to-edge masonry collage of brand-guideline screenshots that bleeds off both viewport edges. Section rhythm repeats: huge amounts of black vertical padding, a big display heading ending in a red period ("Set new standards.", "Branding evolved.", "Plans."), a short left-set paragraph, then a 2-column grid of feature cards (image on top, plain heading + paragraph below, no card container). Testimonials break the black with a mid-gray (#464445) full-width band holding a 3-column masonry of dark #101010 quote cards. Footer is a giant viewport-wide "standards." wordmark.

## Components
Buttons: solid #fe2e00 fill, white bold label, barely-rounded rectangle (2-4px), no shadow, no border; secondary button is flat light gray (#e1e1e1) with dark text. Cards: feature media sits in flat containerless image blocks; testimonial and pricing cards are #101010/#242424 panels with ~10px radius, avatar + name/title header, no borders or shadows. Product-UI screenshots inside features show blue system accents (#2f80ed-ish) that belong to the app, not the marketing chrome. No visible inputs on the page itself beyond those inside screenshots.

## Signature
- The red period: every display heading terminates in a #fe2e00 full stop, echoing the "standards." wordmark.
- True #000000 canvas with only one chromatic accent; all other color arrives via embedded brand artwork collages.
- Full-bleed masonry strips of real customer guideline screenshots used as section dividers.
- Giant lowercase wordmark repeated as the entire footer.

## Do / Don't
- Do keep the marketing chrome strictly black/white and let embedded imagery carry all secondary color.
- Do end display headings with the red period device and left-align them in a wide measure.
- Do use flat, shadowless surfaces — near-black cards (#101010–#242424) on black, separated by tone not borders.
- Do give sections extreme vertical breathing room; one heading + short paragraph can own a full viewport of black.
- Don't introduce gradients, glows, or neon — the dark-tech feel here is matte and editorial, not sci-fi.
- Don't use the red for links, icons, or body emphasis; it is only buttons and terminal periods.
- Don't round buttons past a few pixels or use pill shapes; geometry stays rectangular.
- Don't center hero copy or add a hero CTA — the hero is a quiet left-set statement above a loud collage.
