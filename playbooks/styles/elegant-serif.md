# Elegant Serif Editorial Style Playbook
> Coverage: 16 sites from corpus (analyzed 16)

## Essence
This style translates the register of a well-set print magazine to the web: large display headlines at light-to-regular weight (300–500, almost never bold), a warm paper-like or cinematic near-black canvas, and exactly one scarce accent color doing all the action work. The defining tension is scale contrast without weight contrast — hierarchy comes from size, tracking, case, and family switches (serif display vs. small grotesque or monospace body), never from 700+ headline weights (claude, elevenlabs, shareio, suno, titan). Depth is built from flat surface swaps and 1px hairlines instead of drop shadows and gradients (intercom, cursor, ferrari, titan). Most sites in the group lead with a high-contrast editorial serif (claude, kindsight, titan, voicenotes, monologue, shareio, suno, mode, evergreen, sublime-manifesto); a minority carry the identical editorial voice in a regular-weight sans with negative tracking (cursor, intercom, ferrari, lamborghini) — the restraint, not the serif itself, is the style's core. Copy behaves editorially too: sentence case, terminal periods on headlines (titan, suno), single italic emphasis words (kindsight), and vast whitespace between statements (sublime, suno, bugatti).

## Palette formula
Two canonical grounds, one shared rule: the canvas is never pure neutral white or cool gray. Light variants sit on warm cream/ivory (#F4EFE6–#FAF9F5 range); dark variants sit on near-black or true black. Ink is warm near-black (light mode) or off-white/warm gray (dark mode). Exactly ONE saturated primary exists — a CTA color used with extreme scarcity — or none at all, with the CTA rendered as an ink-colored pill (elevenlabs, evergreen, suno). Accents are either muted pastels confined to decoration (elevenlabs orbs, cursor timeline pills) or earth-tone section slabs (kindsight, mode). Pure white is reserved for card surfaces lifted off the cream floor (intercom, cursor, titan, kindsight).

Example palettes:
- **claude** — canvas #faf9f5 cream / ink #3d3d3a / primary #cc785c coral / accents #181715 dark panel, #efe9de card cream
- **titan** — canvas #F7F5EF cream / ink #1E1E1C / primary #F2C744 muted gold / accents #DDE4DA sage, #E9E4D4
- **intercom** — canvas #f5f1ec cream / ink #111111 / primary #111111 charcoal CTA / accent #ff5600 product-scoped only
- **elevenlabs** — canvas #f5f5f5 warm stone / ink #0c0a09 / primary #292524 ink pill (zero saturated hues) / pastel orbs #a7e5d3, #f4c5a8, #c8b8e0
- **shareio** — canvas #0A0A0A near-black / ink #D9D9D6 / primary #EFEFEC off-white CTA / iridescent accents #4EC4D9, #DE5FC4 live only in imagery
- **kindsight** — canvas #F4EFE6 cream / ink #1F1E1B / primary #DF8462 terracotta / earth slabs #3C4522 olive, #6B2027 maroon, #D9E64F chartreuse

## Typography formula
- **Display:** high-contrast editorial/transitional serif — Tiempos Headline, GT Super, Copernicus, Freight, Editorial New, Times-style faces (claude, titan, voicenotes, kindsight, monologue, shareio, suno, sublime-manifesto, elevenlabs, mode, evergreen). Weight is the signature: 300 (elevenlabs, monologue), 400 (claude, suno, bugatti, shareio, voicenotes), 400–500 (titan); only evergreen and mode go heavy, and neither goes bold-sans. Tracking is tight-to-negative (-0.3 to -1.9px at elevenlabs, -0.3 to -1.5px at claude, -2px at 72px at intercom). Sizes are poster-scale: 64–120px heroes (elevenlabs 64, cursor 72, ferrari 80, lamborghini 120).
- **Sans-editorial variant:** cursor, intercom, ferrari, lamborghini set display in a proprietary grotesque at 400–500 with the same negative tracking — identical rules, no serif.
- **Body:** small neutral grotesque (Inter, Helvetica, Saans, StyreneB) at 400/500, generous line height, often deliberately tiny against the giant display (shareio, monologue, voicenotes, titan). Serif body appears only where the whole page is prose (suno, sublime manifesto, bugatti).
- **Third voice (optional):** monospace for UI chrome, labels, captions, code (bugatti buttons/nav, monologue body labels, cursor code surfaces) — a precision-instrument counterpoint to the romantic serif.
- Micro-typography: sentence case with terminal periods (titan "Titan in Your Inbox.", suno "Make a song."), one italic emphasis word per headline (kindsight), uppercase reserved for luxury-automotive display (bugatti, ferrari, lamborghini) and tiny tracked labels.

## Layout & shape
- Content caps at ~1000–1280px (voicenotes ~1000, claude/cursor/elevenlabs ~1200, intercom/ferrari/bugatti ~1280) on a 12-column grid; imagery may bleed full width (bugatti, ferrari, shareio).
- Vertical rhythm is generous and named: 80px (cursor), 96px (claude, elevenlabs, intercom, ferrari), 120px (bugatti), up to multiple viewport heights of emptiness (sublime, suno). Cards inside a band cluster tight (16–24px gaps).
- Pacing device: alternate full-width surface bands instead of borders — cream / card-cream / dark / accent slab (claude, titan, kindsight, mode); no two adjacent bands share a tone (claude).
- Depth: NO shadow stacks anywhere in the group. Separation via 1px hairlines (#e6e5e0 cursor, #e7e5e4 elevenlabs, #E5E1D6 titan), white-on-cream lift (intercom), or surface-brightness steps on dark canvases (#000 → #202020 lamborghini, #181818 → #303030 ferrari). At most one faint hover shadow (elevenlabs).
- Radius: two coherent camps. Soft-editorial: pill buttons + 12–24px cards (titan, elevenlabs, voicenotes, evergreen, claude, mode). Sharp-luxury: 0px everything, pills only as tiny badges or the lone outlined CTA (ferrari, lamborghini, bugatti, shareio 2–6px).
- Slim quiet nav (56–64px), wordmark left or centered, one CTA right; sublime and suno shrink nav to a floating pill or near-nothing.

## Do
- Set display type at 300–500 weight with tight negative tracking; let size, not boldness, carry hierarchy (claude, elevenlabs, cursor, ferrari, titan).
- Warm the canvas: cream/ivory for light pages (claude #faf9f5, intercom #f5f1ec, titan #F7F5EF), warm near-black for dark ones (ferrari #181818, monologue #0A0A0A) — never pure white or cool gray as the floor.
- Spend exactly one accent color, and only on primary CTAs and one highlighted data point (titan gold, claude coral, ferrari red, lamborghini gold, cursor orange); or drop color entirely and use an ink/cream pill CTA (elevenlabs, evergreen, suno, monologue).
- Build depth from hairlines and flat surface swaps; alternate full-width color bands as the pacing device (claude, titan, kindsight, mode).
- Pair the giant display face with deliberately small body copy in a neutral grotesque — extreme scale contrast is the intended tension (shareio, voicenotes, monologue, titan).
- Keep white reserved for cards lifted off the cream floor (intercom, cursor, titan, kindsight, voicenotes).
- Hold a strict section cadence (80–120px) and let whitespace, not dividers, structure the page (cursor, claude, bugatti, sublime).
- Use hairline rules to organize dense content — pricing rows, FAQs, listings (titan accordions, bugatti spec tables, suno footer).
- Write headlines editorially: sentence case, terminal periods, occasional single italic word (titan, suno, kindsight).
- Show real product chrome or full-bleed photography as the imagery, not abstract illustration (claude dark code cards, intercom screenshots, ferrari/bugatti photography, voicenotes mini-UI vignettes).

## Don't
- Don't bold the display type or swap it for a heavy geometric sans — the magazine tone collapses instantly (claude, cursor, elevenlabs, titan, shareio all forbid this explicitly).
- Don't use pure #FFFFFF as the page canvas on light variants (cursor, titan, kindsight, evergreen) or drop dark canvases to a soft gray when the identity is black (lamborghini demands true #000, ferrari demands warm #181818 — know which).
- Don't add a second saturated hue or scatter the accent across minor UI (ferrari, titan, cursor, intercom, evergreen).
- Don't stack drop shadows, gradients, or glassmorphism for depth — hairlines and surface contrast only (intercom, cursor, kindsight, titan, mode).
- Don't let decorative pastels leak into functional roles: no orb-gradient buttons (elevenlabs), no timeline-pill status colors elsewhere (cursor), no chart colors on marketing chrome (intercom).
- Don't mix the radius camps: never pill a luxury-automotive CTA (ferrari, lamborghini) and never square off a soft-editorial one (elevenlabs, titan, voicenotes).
- Don't make CTAs loud or oversized — buttons stay small and quiet against the huge type (monologue, suno, sublime).
- Don't use serif for body copy or UI labels when it's a display-only system (voicenotes); don't run body text large against the poster display (shareio).
- Don't fill the page with imagery or 3D illustration where typography is the artwork (suno, sublime, monologue).
- Don't tint the palette cool — no blue/purple "AI" gradients or teal SaaS defaults; warmth is the shared identity (claude, kindsight, voicenotes, evergreen).

## Canonical examples
- **claude** — the reference cream-and-coral editorial AI site: serif 400 display, surface-band pacing, dark product-chrome cards.
- **titan** — print-inspired fintech; serif headlines with periods, one gold accent, rounded full-width slabs, hairline-ruled everything.
- **elevenlabs** — the lightest serif in the corpus (300) with a colorless ink-pill CTA and decorative pastel orbs.
- **intercom** — proof the style survives without a serif: one sans family, cream canvas, charcoal CTA, shadowless white tiles.
- **shareio** — dark-mode extreme: poster-scale condensed serif vs. tiny gray sans, color only in iridescent imagery.
- **monologue** — serif-vs-monospace tension on grainy near-black with a single cyan glow.
- **suno** — typography-as-artwork endpoint: rotated ghosted serif sentences, one orange dot, zero imagery.
- **kindsight** — the warm-earth maximal variant: italic emphasis words, full-bleed olive/maroon/lime slabs, hand-drawn line art.
- **voicenotes** — calm paper-tone AI utility; single-serif-word section headers over flat gray cards.
- **ferrari** — dark cinematic luxury discipline: weight-500 display, 0px corners, one scarce red, photography as chrome.
- **bugatti** — the three-typeface trinity (display/serif/mono), no bold anywhere, transparent outlined pill on pure black.
- **sublime** — whitespace extreme: tweet-width centered column, Times-style manifesto serif, one pale-green chip.
