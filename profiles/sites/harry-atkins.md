---
name: harry-atkins
kind: site
style: ML
category: personal-portfolio
website: https://harryjatkins.com/
pages: [home/project-index]
palette:
  canvas: "#FFFFFF"
  ink: "#1A1A1A"
  primary: "#1A1A1A"
  accents: ["#F4F4F2", "#A3A3A0"]
typography:
  display: "Neue-grotesque sans (Helvetica Now / Suisse-like) · bold for monogram, regular elsewhere · tight/neutral tracking"
  body: "Same grotesque sans, regular weight, small size (~13-14px)"
radius: "none"
---
## Overview
A single-surface, monochrome project index. Two giant black letters ("H" / "A") anchor the top corners like a typographic logo split across the page, then everything below is a quiet four-column grid of hairline-ruled project entries with muted screenshot thumbnails. Color appears only inside the thumbnails; the chrome of the site itself is strictly black, gray, and white.

## Layout
- No conventional nav bar. The header row is a utility grid: "Independent / Developer" identity text, "Information / Projects" links, mode toggles ("Text mode / Dark mode / Monochrome" each with a "( N )" keyboard hint), and viewport/OS metadata ("1440x900 / macOS") — all set in the same small type, aligned to the four grid columns.
- Hero is purely typographic: the oversized "H" and "A" letters (~130px tall) sit at columns 1 and 3; on scroll they shrink to a small sticky "H  A" header (~40px) that persists above a hairline rule.
- Body is a strict 4-column grid with even gutters. Each cell: hairline top rule, project title (dark) over category label (gray) on the left, a light-gray index number (26, 25, 24... counting down to 01) right-aligned, then a large thumbnail tile.
- Thumbnails sit centered on very light warm-gray tiles (#F4F4F2) with generous padding, like specimens on a mat.
- Rhythm is metronomic: identical row heights, no featured/hero project, no size variation across all 26 entries.

## Components
- No buttons, cards with borders, or inputs anywhere in evidence. Interactive elements are plain text links in body size with no underline or color shift visible at rest.
- Mode toggles are text labels paired with parenthesized keyboard shortcuts "( N )" — the shortcut key rendered slightly darker than its parentheses.
- Project entries function as list-item "cards": separated by 1px hairline rules only, zero background, zero shadow, zero radius.
- Thumbnail tiles: flat light-gray rectangles, square corners, no border, no shadow.

## Signature
- Monogram-as-layout: two huge grotesque capitals occupying the top of the page instead of a logo or hero headline, collapsing on scroll.
- Reverse-numbered index (26 → 01) in pale gray, giving the archive an editorial, catalog feel.
- Keyboard-shortcut hints "( N )" printed inline next to mode toggles — the interface documents itself.
- One type size and one family doing nearly all the work; hierarchy comes from gray value (dark title / mid-gray label / pale number) and hairline rules, not size or weight.

## Do / Don't
**Do**
- Keep the entire UI chrome achromatic; let project imagery be the only color on the page.
- Separate list items with 1px hairline rules and whitespace rather than boxes or shadows.
- Use gray-value steps (near-black, mid-gray, pale gray) as the hierarchy system within a single small type size.
- Set thumbnails on flat light-gray (#F4F4F2) mats with wide, equal padding.
- Expose utility details (viewport size, OS, keyboard shortcuts) as content — they are part of the aesthetic.

**Don't**
- Don't add buttons, pills, or filled CTAs — the site has none; links are bare text.
- Don't round corners or add drop shadows to tiles or images; everything is hard-edged and flat.
- Don't vary grid cell sizes or feature one project larger than others — the rhythm is strictly uniform.
- Don't introduce a brand accent color into text, rules, or backgrounds.
- Don't use decorative or serif display type; the only display gesture is scale applied to the same grotesque sans.
