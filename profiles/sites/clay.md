---
name: clay
kind: site
style: CP
category: gtm-data-platform
website: null
pages: [home, pricing, experts, feature-pages]
palette:
  canvas: "#fffaf0"
  ink: "#0a0a0a"
  primary: "#0a0a0a"
  accents: ["#ff4d8b", "#1a3a3a", "#b8a4ed", "#ffb084", "#e8b94a", "#f5f0e0"]
typography:
  display: "Plain Black (custom rounded display; sub Inter 500) · medium, never bold · tight (-1 to -2.5px)"
  body: "Inter"
radius: "medium 8-14px (buttons/inputs 12px); large 16px+ (content cards 16px, feature cards 24px); pill for tabs/badges"
---
## Overview
A warm, toy-like B2B site: cream-tinted canvas, near-black ink, and hand-modeled 3D claymation scenes (mountains, mascot figures) doing the heavy branding work. Rotating blocks of one flat saturated color — pink, teal, lavender, peach, ochre — carry the feature story, each framing a miniature screenshot of the real product. Display type is a soft rounded face kept at weight 500 with strong negative tracking, so the friendliness comes from letterform shape rather than boldness.

## Layout
Cream top bar (64px) with logo left, menu center, "Sign in" text link plus dark "Try free" button right; collapses to hamburger under 768px. Hero splits roughly 7/5 — giant 72px headline and button row on the left, a rounded illustration panel on the right. Bands stack on a 96px vertical rhythm inside a ~1280px container. Feature cards run 3-up on desktop, 2-up tablet, 1-up mobile; pricing collapses 4→2→1. Pre-footer is a rounded cream CTA band, and the footer itself stays cream (often with a horizon mountain illustration) — no dark closer.

## Components
- Primary button: near-black #0a0a0a fill, white Inter 600 label, 12px radius, 44px tall; active darkens slightly, disabled goes light gray. Secondary is cream with a 1px hairline; on colored cards the button inverts to white-with-ink.
- Feature cards: 24px radius, 32px padding, flat single-color fills with no shadow; text flips white on pink/teal, dark on lavender/peach/ochre. Each embeds a small product-UI fragment or mascot.
- Content/testimonial/pricing cards: 16px radius, cream or canvas fill with hairline border; featured pricing tier signals itself by switching to the deep teal fill.
- Inputs: 44px, 12px radius, hairline border that thickens to ink on focus. Tabs and badges are pills on cream fills.
- Depth is color-driven: no heavy shadows anywhere, only hairlines and the contrast between cream and saturated fills.

## Signature
- 3D claymation renders (mountains, recurring mascots) as hero and footer artifacts — the single most identifiable brand asset.
- A strict six-color card rotation (pink/teal/lavender/peach/ochre/cream) that never repeats a color back-to-back.
- Cream-everything pacing: even the footer stays warm light, bucking the dark-footer SaaS default.
- Rounded display face at weight 500 with tight negative tracking — warmth via shape, not weight.

## Do / Don't
**Do**
- Keep the whole page on the #fffaf0 cream floor, footer included.
- Cycle the six card colors in sequence and match color to feature theme (pink=outbound, teal=featured/enterprise, lavender=AI agents).
- Put real product screenshots inside the colored cards — the pitch is product-first, not abstract shapes.
- Hold display headlines at weight 500 with -1 to -2.5px tracking; if Plain Black is unavailable, Inter 500 tightened is the stand-in.
- Rely on flat color contrast and hairlines for depth; keep shadows out.

**Don't**
- Don't swap cream for cool gray or white-white — the warm tint is the differentiator.
- Don't add a seventh card color or repeat one twice in a row.
- Don't push headlines to 700; the rounded face turns shouty.
- Don't replace the 3D clay illustrations with flat vector art.
- Don't close pages with a dark footer band.
