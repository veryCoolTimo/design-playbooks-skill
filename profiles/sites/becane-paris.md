---
name: becane-paris
kind: site
style: ML
category: fashion-ecommerce
website: https://www.becaneparis.com/
pages: [shop-collection, editorial-manifesto, footer]
palette:
  canvas: "#f4f4f4"
  ink: "#111111"
  primary: "#ffffff"
  accents: ["#b8b8b8", "#595959"]
typography:
  display: "wide extended grotesque (Monument Extended / Druk Wide feel) · heavy black · slightly tight, all-caps"
  body: "compact grotesque (Helvetica/Univers condensed feel) · regular · all-caps micro labels"
radius: "small 2-6px (cards and pill labels share a subtle ~2-3px corner)"
---
## Overview
A stark monochrome shop that reads like a technical spec sheet. Everything lives on an off-white canvas with floating white utility cards; the only "color" is the value scale from near-black ink through mid-grays. Personality comes entirely from an ultra-wide, heavyweight all-caps display face used for headings and full-screen manifesto text, set against tiny all-caps interface labels with numeric counters.

## Layout
- Nav is a small floating white card pinned top-left: italic BECANE wordmark above a one-line menu (ALL 27 · STORIES 04 · CART 00) with gray counts next to black labels. A mirrored card top-right shows contextual state (COLLECTION 01 / 01) plus a thumbnail.
- Page header is sparse: a tiny eyebrow label (COLLECTION 01 / 01), then a massive extended-caps H1, then a keyed data row (PRODUCTS — 14). Enormous empty whitespace below before content.
- A persistent status bar card bottom-left ("14 PRODUCTS" left, gray "DISCOVER" right) acts as scroll/section indicator.
- Mid-page: a full-width editorial block where a long brand manifesto is set centered in giant extended caps on the light canvas; a dark gray image band separates sections.
- Footer is a row of small white pill/tab links bottom-left (TERMS OF SERVICE, SHIPPING POLICY, SIZE GUIDE) and bottom-right (HELLO@BECANEPARIS.COM, INSTAGRAM) — same card language as the nav.

## Components
- Buttons/links: small white rectangles with barely-rounded corners, black all-caps ~10-11px labels, no borders, no visible shadow depth — flat tabs. Secondary/inactive state is mid-gray text (#b8b8b8) on the same white fill.
- Cards: white panels floating on the off-white canvas, distinguished by value contrast alone (no strokes, no drop shadows of note).
- Counters: two-digit zero-padded numbers (27, 04, 00, 01 / 01) in gray beside their labels — a recurring data-readout motif.
- No conventional hero imagery in these shots; imagery appears as full-bleed gray/photographic bands between text sections.

## Signature
- Ultra-wide heavy extended grotesque set in all caps at poster scale — even paragraphs of manifesto copy are display type.
- Floating white utility cards (nav, status bar, footer pills) on an off-white field instead of a traditional header/footer chrome.
- Zero-padded numeric counters (00, 01 / 01, 27) paired with every label, giving a technical/odometer feel.
- Strict grayscale palette; hierarchy built only from black vs. mid-gray text and white vs. off-white surfaces.

## Do / Don't
Do:
- Set all headings and hero copy in a heavy extended sans, all caps, and let it be the loudest element on the page.
- Keep chrome as small detached white cards anchored to corners, leaving the center of the viewport mostly empty.
- Pair every nav label and data point with a gray zero-padded counter (CART 00, STORIES 04).
- Use whitespace aggressively — one H1 and a data row can own an entire viewport.
- Differentiate states with gray text (#b8b8b8) rather than color or underline.

Don't:
- Introduce accent colors, gradients, or tinted buttons — the system is strictly grayscale.
- Add borders, drop shadows, or heavy rounding to cards; surfaces separate by value contrast only.
- Use lowercase or mixed-case anywhere; every string on the site is uppercase.
- Center a traditional full-width nav bar or fill the header edge-to-edge.
- Use a normal-width or humanist typeface for headings — the extended width is the brand.
