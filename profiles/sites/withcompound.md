---
name: withcompound
kind: site
style: ML
category: fintech-wealth-management
website: https://withcompound.com/
pages: [home, membership]
palette:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  primary: "#1F1F1F"
  accents: ["#000000", "#EDECEA", "#4E7FE0", "#B06BC9"]
typography:
  display: "neo-grotesque sans (Suisse/Untitled Sans feel) · regular-to-medium weight · tight-to-normal tracking"
  body: "same neo-grotesque sans · small sizes, generous line-height"
radius: "small 2-6px (buttons ~4px; cards and dashboard panels ~4-8px)"
---
## Overview
Austere black-and-white editorial minimalism for a wealth platform. Nearly the entire site is grayscale: white canvas, near-black ink, full-bleed pure-black sections, and warm-gray card panels. Color exists only inside product screenshots (a net-worth dashboard with blue/purple allocation charts), which makes the product UI itself the only "colorful" object on the page. Type does the talking; imagery is limited to abstract monochrome ribbon renders and the dashboard.

## Layout
Sticky-feeling top nav: serif-flavored lowercase "compound" wordmark left, three sparse text links center (Membership, Resources, Company), "Sign in" plus a black pill-less "Get started" button right. Home hero is text-only and left-aligned: a two-line headline where the first line is blurred/faded gray and the second line is crisp black — no hero image, just two buttons below. Membership hero is a split: left-aligned headline, small supporting paragraph on the right, followed by a large embedded product screenshot. Section rhythm alternates full-width white and full-width pure-black bands (black band with 3D ribbon image + white text on home; black statement-headline band on membership). A logo strip (OpenAI, Slack, Ramp, Retool, Lattice, Coinbase) in gray sits under the home hero. Mid-page features use a centered radial/orbit diagram and a 5-column row of flat gray cards. Whitespace is extreme — hero areas are more than half empty. Footer is a black band with 3-column link lists in small gray type and a long block of tiny legal copy.

## Components
- Buttons: primary is a solid near-black (#1F1F1F) rectangle with small (~4px) radius, white 13-14px label, and a right-pointing chevron ">" suffix; on black sections it inverts to a light-gray/white fill with dark text. Secondary is a white button with a thin 1px gray border, same radius, no chevron.
- Cards: flat warm-gray (#EDECEA-ish) panels, no border, no shadow, small radius, small bold-ish title plus small body text (5-up feature row on membership).
- Product screenshot: framed dashboard panel with thin gray borders, small radii, sidebar nav, and colored stacked-area/treemap chart — the only saturated color anywhere.
- Question "chips" on membership: small white pill-ish tags with hairline borders arranged in a loose cloud ("Will I owe AMT?" etc.).
- Pull quote: oversized gray serif-toned quotation filling a warm-gray band, with tiny attribution.
- No visible shadows anywhere; hierarchy comes from value contrast (black/white/gray) and scale.

## Signature
- Blurred-then-sharp two-line hero headline (line 1 defocused gray, line 2 crisp black) — text-only hero.
- Strict grayscale world where only the product dashboard carries color.
- Alternating full-bleed pure-black and white sections with abstract monochrome 3D ribbon renders.
- Small dark rectangular CTAs with a chevron suffix ("Get started >") repeated identically in nav, hero, and mid-page.

## Do / Don't
Do:
- Keep the palette grayscale; reserve saturated color exclusively for in-product UI screenshots.
- Use full-width black bands as rhythm breaks between white sections, inverting text and buttons inside them.
- Set headlines large in a plain neo-grotesque at regular weight and let whitespace (50%+ empty hero) carry the premium feel.
- Use flat warm-gray cards with no borders or shadows for feature grids.
- Append a chevron to primary CTAs and keep them small, dark, and squared-off (~4px radius).

Don't:
- Add drop shadows, gradients on UI chrome, or rounded-pill buttons — everything here is flat and near-square.
- Introduce a brand accent color for links, buttons, or icons; the CTA is black, not colored.
- Use photography of people; imagery stays abstract (3D ribbons) or product screenshots.
- Center the hero or fill it with illustration — heroes are left-aligned, text-first, and sparse.
- Use heavy/bold display weights or decorative type; contrast comes from size and gray-value, not weight.
