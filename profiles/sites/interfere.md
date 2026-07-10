---
name: interfere
kind: site
style: ML
category: developer-tools
website: https://interfere.com/
pages: [landing]
palette:
  canvas: "#FFFFFF"
  ink: "#3A3A3F"
  primary: "#111113"
  accents: ["#F3C6C6", "#C9C4E8", "#BFE3F0", "#E8734A"]
typography:
  display: "Neue Haas / Helvetica-class grotesque · medium-to-semibold · tight, with italic serif inflections"
  body: "Same grotesque family · regular · normal tracking"
radius: "buttons small 4-6px; product-mockup cards medium 8-12px; pill badges on nav CTA keyboard hints"
---
## Overview
A near-white, typography-led SaaS landing page where the interface itself does the selling: oversized product UI mockups bleed off the right edge of the viewport on a soft pink-lavender-blue gradient wash. Chrome is minimal — thin hairline dividers, gray-scale text, one near-black CTA — so the pastel gradients and colorful issue-type icons inside the mockups carry all the color. Headlines mix a clean grotesque with a single italic serif word ("breaks") for editorial contrast.

## Layout
Fixed top nav on white: dithered pixel-glyph logo left, center-aligned text links (Product, Careers, Changelog, Docs, Contact), Login plus a dark "Request a demo" button right — both annotated with tiny keyboard-shortcut chips (L, D). Hero is a two-column split: giant left-aligned headline on the left, small right-aligned supporting paragraph plus two buttons on the right, then a full-width product screenshot rising from a pink gradient below. Sections follow a numbered 01/02/03 system: a three-up feature card row up top, then long alternating sections with text in the left third (numeral, heading, paragraph, "capability list" of hairline-ruled two-column links) and a large cropped app mockup filling the right two-thirds, bleeding off-screen. A grayscale logo marquee ("Trusted and funded by") sits between hero and features. A giant gradient testimonial card uses ghosted low-contrast serif quote text. Whitespace is generous, almost airy; hairline horizontal rules mark section boundaries.

## Components
- Buttons: near-black (#111113) fill, white text, small 4-6px radius for the primary CTA; secondary is white with a faint gray border and subtle shadow ("Get Early Access"). Nav demo button carries an inline "D" key chip.
- Cards: white product-mockup panels with medium radius, faint border, very soft diffuse shadow, floating over gradient backdrops; feature preview tiles are flat with light borders.
- Product UI mockups: Linear-style app with left icon rail, breadcrumb header, tab pills (Activity / Sessions / Findings — active tab is a light gray pill), metadata key-value tables, kanban columns, and inline code-diff blocks with red/green change gutters.
- Badges/chips: rounded-full light gray keyboard hints; status chips ("Investigating…", "Medium priority") are outlined pills with tiny icons.
- Icons: small pastel-tinted rounded-square issue icons (key, invoice, mail) providing color pops.

## Signature
- Off-canvas product mockups: large app screenshots cropped by the viewport edge, floating on pink→lavender→blue gradient washes.
- One italic serif word inside an otherwise grotesque headline ("Ship software that never *breaks*").
- Numbered section system (01, 02, 03) in small monospace-style labels, plus hairline-ruled capability link lists.
- Keyboard-shortcut chips (L, D) attached to nav actions — dev-tool credibility signaling.
- Near-monochrome page shell; all saturation lives in gradients and in-mockup icons.

## Do / Don't
**Do**
- Keep the page shell white/gray-only and let soft pink-lavender gradient fields plus in-mockup pastel icons supply all color.
- Crop large, realistic product screenshots off the right viewport edge instead of framing them fully in view.
- Use the 01/02/03 numeral labels and thin hairline rules to structure long feature sections.
- Set one emphasized word per headline in an italic serif; keep everything else in the grotesque.
- Pair the dark primary button with a bordered white secondary; add small keyboard-hint chips to nav actions.

**Don't**
- Don't use saturated brand color on buttons or links — CTAs are near-black, links are plain gray text.
- Don't add heavy shadows, thick borders, or large radii; corners stay tight (4-12px) and shadows barely visible.
- Don't center hero copy — headline is hard-left, supporting text right-aligned in the opposite column.
- Don't fill sections edge to edge; preserve the wide left text column vs. right mockup asymmetry with generous whitespace.
- Don't decorate with illustrations or stock imagery; the only visuals are product UI, code diffs, and gradients.
