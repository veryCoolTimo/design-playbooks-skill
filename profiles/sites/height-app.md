---
name: height-app
kind: site
style: DT
category: project-management-saas
website: https://height.app/
pages: [home, company, home-light-variant]
palette:
  canvas: "#0E0C15"
  ink: "#E9E7F0"
  primary: "#6A5CF5"
  accents: ["#E44FC4", "#1BB9AC", "#F5793B", "#9D5CF0", "#2BC0E0"]
typography:
  display: "geometric grotesque with soft rounded terminals (Aeonik/Styrene feel) · semibold-bold · tight"
  body: "same geometric sans at small size, Inter-like neutrality"
radius: "small 2-6px on buttons and pill tags; medium 8-14px on cards, large 16px+ on big feature panels"
---
## Overview
Dark-tech SaaS marketing site where a near-black violet-tinted canvas is punched through with saturated candy accents: magenta, teal, orange, and purple. Gradient text spans headline keywords (pink-to-teal on "conversations"), and floating pill badges with avatars animate around a central teal checkmark logo. A full light-mode twin exists with identical layout, swapping the canvas to white with pale lavender/mint section tints while keeping the same accent set. The company page goes even darker (pure black) and quieter, letting one rainbow gradient squiggle carry all the color.

## Layout
Slim top nav: logo left, center links (Product, Pricing, Blog, About us), right-aligned Request demo / Log in / Sign up with the sign-up link in accent color. Hero is centered: gradient-accented H1, one-line subhead, single small CTA, then a playful composition of colored department pills (marketing, engineering, product, design) with circular avatars orbiting the app icon. Section rhythm alternates: two-column benefit cards (text panel + illustration panel side by side), a full-width dark product-screenshot showcase with a tab bar of feature pills (Tasks, Spreadsheet, Kanban, Gantt...), a 3-column masonry testimonial wall, and a gradient-washed "Try it live" embedded product demo. Footer is a dense 5-column sitemap. Generous vertical spacing between sections; content column stays narrow (~1100px).

## Components
Buttons: small, compact, 4-6px radius, solid purple (#6A5CF5) fill with white label and trailing arrow for primary; secondary is a flat dark-gray fill of the same shape. The company page uses a light pill "Request early access" instead. Tags/labels are fully rounded pills with saturated gradient fills. Cards: testimonial cards are dark surfaces with 1px low-contrast borders, ~10px radius, avatar + name + handle header; benefit sections pair a matte text card with a purple/blue gradient illustration card. Product screenshots sit in large rounded frames on subtle purple-to-blue gradient washes. No visible drop shadows in dark mode; light mode uses soft tinted section backgrounds (lavender, periwinkle) instead of borders.

## Signature
- Saturated multi-hue accent system (magenta/teal/orange/purple) as gradient pill badges and gradient headline words on a near-black canvas.
- Teal rounded-square checkmark logo used as a recurring illustration anchor, with chat bubbles and avatars orbiting it.
- Real embedded app screenshots (task list, chat pane, spreadsheet) as hero-scale section content, framed on gradient washes.
- Perfect dark/light parity: the same page recolors from #0E0C15 to white with pastel section tints, accents unchanged.

## Do / Don't
Do:
- Reserve gradients for keywords in headlines and small pill tags; keep body copy plain high-contrast gray/white.
- Keep CTAs small and understated (compact purple button with arrow) — the color system, not button size, carries energy.
- Alternate matte text panels with gradient illustration panels in two-column benefit rows.
- Use 1px low-contrast borders on dark cards instead of shadows; in light mode swap borders for pastel background tints.
- Let product screenshots be large and literal — full app chrome with sidebar, tabs, and task rows.

Don't:
- Don't use one brand color everywhere — this system deliberately spreads magenta, teal, orange, and purple across equal roles.
- Don't add heavy glows, neon outlines, or glassmorphism; surfaces are flat and matte despite the dark-tech palette.
- Don't make hero CTAs large or pill-shaped on the main site (pills are for tags and badges, not primary buttons).
- Don't render headlines in thin or wide-tracked type; display type is chunky, tight, and slightly rounded.
- Don't mix warm off-white canvases into light mode — it stays cool white with lavender/mint washes.
