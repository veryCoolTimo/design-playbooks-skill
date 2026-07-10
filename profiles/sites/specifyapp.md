---
name: specifyapp
kind: site
style: DT
category: design-system-saas
website: https://specifyapp.com/
pages: [home, pricing, blog, solutions]
palette:
  canvas: "#0C0C10"
  ink: "#A6A6B0"
  primary: "#6C51E4"
  accents: ["#F24BB0", "#2E6BF2", "#7FD6D2", "#9E8CFC"]
typography:
  display: "Inter-style geometric grotesque · bold 700 · tight tracking"
  body: "Inter-style grotesque, regular, muted gray"
radius: "pill buttons; medium 10-14px cards"
---
## Overview
Near-black, developer-facing dark UI where violet is the single brand anchor: a purple pill CTA repeats on every page, purple gradient glows wash over section bands, and purple-tinted 3D/abstract renders illustrate features. Headings are crisp white bold grotesque on charcoal; body copy drops to a muted gray. Small doses of magenta, blue, and teal appear only in data-like contexts (pricing tier checkmarks, testimonial card backgrounds, token chips), keeping the base austere and technical.

## Layout
Slim top nav: logo left, dropdown links center-right, "Sign in" ghost + purple "Start for free" pill right. Heroes are centered stacks — small purple eyebrow/pill, 2-3 line bold white headline, short gray subhead, one or two pill CTAs — followed by a grayscale "loved by" logo strip. Sections alternate: centered H2 intro, then either two-column feature rows (text list + product screenshot card) or 2-up rounded feature cards. A horizontally scrolling testimonial carousel with full-bleed colored cards (purple, teal, dark) breaks the rhythm mid-page. Every page closes with the same centered "Start automating your design system today" CTA block above a 5-column dark footer. Generous vertical whitespace between bands; content column stays narrow (~1100px).

## Components
Buttons: pill-shaped, compact; solid purple fill with white text for primary, white fill with black text for secondary, dark ghost with thin border for tertiary; "Discover" links render as white pill buttons with arrow. Cards: 10-14px radius, slightly lighter charcoal (#141418) fill with 1px faint border; the highlighted pricing tier gets a purple border plus a "Most popular" purple tab on top. Pricing feature table uses color-coded circular checkmarks per tier (pink / purple / white). FAQ is a plus-icon accordion with hairline dividers. Blog grid: 3-up cards with image thumb, colored category label, title, excerpt, date. Toggle switch (Yearly) in purple.

## Signature
- One purple (#6C51E4) doing all interactive work — CTAs, toggles, tier highlights, eyebrows — against an otherwise grayscale dark UI
- Per-tier color coding on pricing (pink Essentials, purple Teams, white Enterprise) carried into checkmarks and prices
- Full-bleed testimonial carousel cards in saturated flat colors (teal, purple) that punch through the dark canvas
- Purple-glow gradient bands and dark 3D token/hardware renders as hero and section imagery

## Do / Don't
Do:
- Keep the canvas near-black (#0C0C10) with cards only one step lighter and hairline borders
- Use pill buttons everywhere; reserve solid purple for the primary action and white fill for the secondary
- Center section intros (bold white H2 + short muted-gray subhead) before every content band
- Repeat the same closing CTA band ("Book demo" purple pill) at the bottom of every page
- Render logos and non-interactive chrome in grayscale so purple stays the only accent

Don't:
- Don't introduce warm or light section backgrounds — color arrives only via gradient glows and testimonial cards
- Don't use square or slightly-rounded buttons; the pill shape is consistent site-wide
- Don't set body copy in pure white — it is always muted gray against white headings
- Don't add heavy drop shadows; depth comes from surface lightness steps and glows
- Don't scatter the pink/blue/teal accents into CTAs — they mark categories and testimonials, not actions
