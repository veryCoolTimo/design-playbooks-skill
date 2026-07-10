---
name: resend-forward
kind: site
style: ML
category: developer-tools
website: https://resend.com/forward
pages: [home]
palette:
  canvas: "#f0f0f0"
  ink: "#1a1a1a"
  primary: "#0a0a0a"
  accents: ["#ffffff", "#c4c4c4", "#8a8a8a"]
typography:
  display: "Neutral grotesque (Inter-like) · light-to-regular weight at huge sizes, semibold for feature headlines · tight tracking; one italic glyph swapped into the hero wordmark"
  body: "Inter-like grotesque; uppercase monospace for dates and micro-labels"
radius: "pill buttons; medium 8-14px cards"
---
## Overview
An almost entirely grayscale launch-week microsite: warm light-gray canvas, white cards, and near-black type, with the only saturated color living inside a single iridescent 3D hero render. Hierarchy is carried by scale and value contrast, not hue. Monospace uppercase micro-labels (dates, day counters) give it a calendar/schedule feel. The mood is quiet, precise, and deliberately restrained.

## Layout
Top nav is a slim centered bar: wordmark left, small text links center (About, Blog, Customers, Pricing, Enterprise, Changelog, Docs), Sign in plus a black pill "Get Started" CTA right. Hero is centered: tiny mono date range, one giant word ("Forward"), a two-line subhead, then a floating 3D glass object; a mono day-by-day index (MONDAY 15 … FRIDAY 19) sits in the top-right margin. A repeating uppercase "LAUNCH WEEK" ticker strip divides hero from content. Below, announcements run down a vertical center rule as an alternating two-column timeline: media card on one side, mono date label + headline + copy + CTAs on the other, swapping sides each day. Unreleased days are grayed placeholder bars with white lock cards. Footer is centered: dot-separated uppercase contributor names and an oversized "FWD@RESEND.COM" wordline. Hairline vertical rules and generous whitespace structure everything.

## Components
- Buttons: black pill fill with white label and small chevron ("Get Started", "Blog Post"); secondary action is a plain bold text link with chevron, no border.
- Cards: white, medium-rounded (~10-12px), soft diffuse shadow on the light-gray canvas; locked cards show only a centered gray padlock icon; the revealed card holds an embossed 3D UI vignette with a "New" pill badge.
- Labels: uppercase monospace in mid-gray for dates and day indices; skeleton-style gray bars stand in for unrevealed text.
- No visible inputs; ticker strip uses widely spaced uppercase gray text.

## Signature
- One-word oversized hero headline with a single italic/swash character breaking the grotesque set.
- Grayscale-only palette where the lone iridescent 3D render is the entire color budget.
- Vertical center-rule timeline alternating locked white cards and mono-dated announcements, day by day.
- Repeating "LAUNCH WEEK" ticker band and giant email-address footer as typographic set pieces.

## Do / Don't
Do:
- Keep the page grayscale; concentrate all color into one hero 3D/render moment.
- Use uppercase monospace for dates, day counters, and micro-labels throughout.
- Alternate content left/right along a thin vertical center rule for sequential reveals.
- Use black pill CTAs with chevrons; make secondary actions plain bold text links.
- Represent unreleased content as white lock cards plus gray skeleton text bars.

Don't:
- Introduce brand colors into buttons, links, or section backgrounds — CTAs stay black on gray.
- Use heavy borders or dark shadows; cards separate by white-on-gray value plus a soft blur.
- Mix headline styles — hierarchy comes from one huge display word and modest section headlines.
- Fill the layout; whitespace and hairline rules carry the structure, so avoid dense multi-column grids.
- Use sentence-case or colorful badges for metadata where mono uppercase gray is the established voice.
