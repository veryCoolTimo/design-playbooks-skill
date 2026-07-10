---
name: buddy-works
kind: site
style: ML
category: devops-saas
website: https://buddy.works/
pages: [home, pricing, docs, changelog, contact]
palette:
  canvas: "#F4F5F7"
  ink: "#17191C"
  primary: "#A8E82E"
  accents: ["#35D1F5", "#3BE8A0", "#F653A6", "#8B5CF6", "#FF8A3D"]
typography:
  display: "Inter-like neutral grotesque · black/extra-bold · tight tracking"
  body: "Inter-like neutral grotesque"
radius: "pill (buttons/inputs); medium 8-14px (cards, panels)"
---
## Overview
A minimal light "engineering paper" aesthetic: a pale gray canvas overlaid with a faint blueprint grid, near-black text, and hairline-bordered white panels. Color is rationed to a single loud lime-green CTA plus thin rainbow-gradient ribbon squiggles used as garnish. Product screenshots do most of the storytelling; the chrome around them stays monochrome and quiet.

## Layout
Sticky white top bar: logo left, inline search field, small text nav (Changelog / Docs / Pricing / Contact / Sign in), then two pill buttons — outlined "Install Self-Hosted" and lime "Get Started on Cloud". Heroes are centered, huge black type on the grid background with no imagery besides small badges. Pages run as long stacked feature sections: bold section heading, short paragraph, large layered product screenshots, then a 2-3 column row of tiny benefit blurbs with squiggle-underline accents. A full-width dark (near-black) logo-wall/testimonial band breaks up the light home page. Every page ends with the same signature cyan-to-green gradient "Start for free" panel (self-hosted pill buttons left, lime OAuth pills right), a footer with diagonal-hatch section rules, and a giant outlined "Buddy Works" wordmark bleeding off the page bottom. Docs use a horizontal tab bar plus left sidebar over the same grid; changelog uses a center wavy timeline with date pills.

## Components
- Buttons: fully pill-shaped. Primary = solid lime (#A8E82E) with black text; secondary = white with 1px dark border; both flat, at most a whisper of shadow. OAuth pills carry a leading brand icon.
- Cards: white, thin light-gray border, 8-14px radius, nearly shadowless; the highlighted pricing tier gets a soft drop shadow, slight lift, and gradient ribbon corners. Checklist rows use solid black circular check icons.
- Inputs: pill-shaped, light border, inline pill submit button (email subscribe, docs search).
- Decorative set: hatched/striped divider bars, dashed hairlines, date pills, a peeling "SOC 2 Type II" sticker, green "all systems operational" status dot.

## Signature
- Faint grid/graph-paper background across every page, like engineering drafting paper.
- One acid-lime pill CTA repeated everywhere against an otherwise grayscale UI.
- Thin multicolor gradient squiggles and ribbon strips as the only ornament — under headings, on card corners, as timeline threads.
- Cyan-to-green gradient pre-footer CTA panel plus a giant outline-only wordmark cropped at the very bottom of each page.

## Do / Don't
Do:
- Keep the canvas a pale gray grid and reserve saturated color for the primary CTA and small squiggle accents.
- Use extra-bold, tightly tracked near-black headlines at large sizes ("7-in-1 Pricing", "Hey! Let's deploy.") with playful, terse copy.
- Make every button and input a pill; distinguish hierarchy by fill (lime vs. white-outlined) rather than size.
- Repeat the gradient "Start for free" band and outlined giant wordmark as the closing module on every page.
- Border cards with 1px light gray and keep them flat; reserve shadow for the one highlighted element (featured pricing tier).

Don't:
- Don't introduce a blue or multi-color button system — the lime CTA is the only solid-color button besides icon OAuth pills.
- Don't use photography or illustration heroes; product screenshots and type carry the visuals.
- Don't apply heavy drop shadows or glassmorphism to cards — depth stays near zero on this site.
- Don't use the rainbow gradients as large fills; they only appear as thin ribbons, underlines, and the single pre-footer panel.
- Don't round cards to pill extremes or square off buttons — the pill/medium-radius split is consistent sitewide.
