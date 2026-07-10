---
name: podscan
kind: site
style: ML
category: media-monitoring-saas
website: https://podscan.fm/
pages: [home]
palette:
  canvas: "#ffffff"
  ink: "#1a1a1a"
  primary: "#111111"
  accents: ["#0a0a0a", "#f4f4f5", "#e4e4e7"]
typography:
  display: "Inter-style neo-grotesque · bold 700 · tight, near-default tracking"
  body: "Inter-style neo-grotesque, regular, gray-muted for secondary copy"
radius: "small 2-6px on buttons; medium 8-14px on cards and pricing panels"
---
## Overview
A strictly monochrome minimal-light site: white canvas, near-black ink, and black-fill CTAs with zero brand color anywhere on the page. Contrast comes from value, not hue — a full-bleed near-black section mid-page inverts the scheme, and an embedded product screenshot supplies the only color. Type does the branding work: a large bold grotesque headline with a single italicized word ("immediately") as the emotional accent.

## Layout
Top nav is a slim centered bar: pill-outlined logo left, plain text links center-right, ghost "Log in" plus solid black "Register" button. Hero is fully center-aligned on a faint gray-to-white gradient: three-line headline, one-line subhead, dark CTA button paired with an inline "or search 7,509,369+ past episodes" alternative, then a stacked/fanned alert-card mockup as the hero visual. A 4-column stat strip (10K+, 50min, 4,000+ words, 100%) sits below on light gray. Section rhythm alternates white → white with gray feature cards → inverted near-black block (left text column, right product screenshot, then a 2x4 grid of small icon-led feature blurbs) → white pricing (3 cards, middle one inverted black as the highlighted tier) → FAQ accordion → centered dark closing CTA → multi-column footer. Content sits in a narrow centered container (~1000px) with generous vertical padding.

## Components
Buttons: solid black fill, white text, small radius (~4-6px), compact padding; no gradients or shadows. Secondary actions are plain text or ghost links. Feature cards: flat light-gray (#f4f4f5) fills, no borders, small radius; one card in the row carries a hairline border to mark emphasis. Pricing cards: hairline-bordered white cards with checkmark lists; the featured Premium tier flips to black fill with white text and its CTA inverts to a light button. FAQ: full-width gray rows with plus-icon toggles. In the dark section, feature bullets sit on slightly lighter panels (#161616-ish) with thin icons. Inline keyword highlights in the alert mockup use a marker-style background chip.

## Signature
- Pure black-and-white system where the "highlighted" pricing tier and an entire mid-page section are achieved by inverting to near-black rather than adding color.
- Center-aligned hero with one italicized word in the headline and a hand-drawn-style underline flourish.
- Layered/fanned alert-card mockup as the hero image instead of a full app screenshot; the real dashboard screenshot is saved for the dark section.
- Big-number stat strip (10K+ / 50min / 4,000+ words / 100%) with tiny caption text directly under the hero.

## Do / Don't
Do:
- Keep every CTA solid black on light sections and invert (white/light button) inside dark sections.
- Use flat #f4f4f5 gray fills instead of borders or shadows to define cards on white.
- Invert an entire section to near-black for the product-depth story and for the featured pricing tier.
- Set headlines in heavy grotesque and reserve italics for exactly one emphasized word.
- Anchor claims with an oversized-number stat row and small muted captions.

Don't:
- Introduce a hue-based brand color; the only color allowed is inside embedded product screenshots.
- Add drop shadows, gradients (beyond the faint hero wash), or outlined/ghost primary buttons.
- Use large or pill radii on buttons; corners stay tight (~4-6px) even though cards are softer.
- Left-align the hero; hero and closing CTA sections are strictly center-stacked.
- Decorate section transitions — sections butt together as flat full-width bands of white, gray, or black.
