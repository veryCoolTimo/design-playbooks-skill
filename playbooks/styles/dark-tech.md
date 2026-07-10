# Dark Tech Style Playbook
> Coverage: 85 sites from corpus (analyzed 60)

## Essence
Dark Tech is a near-black marketing language built for developer tools, infrastructure, fintech, and AI products: an unbroken dark canvas (usually #030303–#17191E, often subtly tinted blue, violet, or green rather than pure #000), white or off-white headlines, muted-gray body copy, and a single rationed accent color that does all conversion work. Depth is never rendered — there are no drop shadows; elevation comes exclusively from surfaces stepping one lightness notch above the canvas plus 1px low-contrast hairline borders (linear.app, clickhouse, composio, hashicorp). The product itself is the imagery: dark-mode UI screenshots, syntax-highlighted code windows, and terminal panels sit as first-class content, frequently lit from behind by a soft radial glow in the accent hue (basehub, betterstack, outerbase, jam-dev). The mood is quiet, engineered, and precise — the page persuades through restraint, tonal discipline, and one bright thing, not through decoration.

## Palette formula
The formula is **canvas → surface ladder → muted ink → one loud accent**. Canvas sits in the #000–#1a range, usually tinted (blue-black #010102 linear.app, navy #0E1525 replit, violet-black #0B0714 openserv, green-black #080F11 oxide-computer, plum #1E0714 luroapp, warm charcoal #0E0E0C retool). Cards lift 5–10% lighter than the canvas (#0f0f0f → #161616 → #1e1e28), never lighter. Headings are white/off-white; body ink is deliberately dimmed to mid-gray (#8b8b8e gitness, #A1A1AA betterstack/mintlify/resend, #9B9B9F chroniclehq) — body copy is never pure white. The accent is one saturated hue reserved for CTAs, links, glows, stat numbers, and one highlighted word per headline; when the accent is bright (yellow, lime, mint), button labels flip to dark text, never white (binance, clickhouse, modal, mongodb). Semantic green/red exist only as tiny status signals (binance, checklyhq, modal), never as surfaces.

Concrete example palettes:
1. **Black + electric yellow** — canvas #0a0a0a, cards #1a1a1a, ink #cccccc, accent #faff69, black-on-yellow CTAs (clickhouse); sibling: #0b0e11 / #eaecef / #fcd535 (binance).
2. **Black + single orange** — canvas #030303, panels #161616, body #8F8F8F, accent #FF6D00 for CTAs, glows, and full-width bands (basehub).
3. **Near-black + indigo-violet** — canvas #0C0B0E, ink #A1A1AA, accent #6C63F0 on CTAs, eyebrows, links, screenshot glows (betterstack); sibling: #010102 / #f7f8f8 / #5e6ad2 with a five-step charcoal ladder (linear.app).
4. **Black + acid green/lime** — canvas #0A0A0A, ink #C8CCC8, accent #7FEE64–#D7FF3F (modal); siblings: #0A0A0A / #DFFF2E (codex), #080F11 / #48D597 mint on green-black (oxide-computer), #0a0a0a / #3fe0a1 (pirsch).
5. **Grayscale + white-pill CTA** — canvas #000, cards #111, ink #a1a1aa, primary is off-white #f5f5f5 with green held to status dots only (resend); siblings: gitness (#070709, white pill, color via 3D renders), outerbase (#0e0e0e, off-white pills), react-email (#000 + one cyan #22d3ee).
6. **Near-black + multicolor glow** — canvas #17191E, ink #BFC1C9, violet primary #883AEA with magenta/teal/amber arriving only through blurred aurora artwork and gradient CTAs (astro-build); siblings: framer (#050505, #0055FF, per-section gradient headlines), gitbook (#141519, pastel aurora blooms, soft-yellow #F0E585 pill).

## Typography formula
One neo-grotesque family carries the whole site — Inter-class or a proprietary equivalent (Inter at clickhouse/eraser/dimension, abcDiatype at composio, Linear Display, hashicorpSans, BinanceNova, PP Neue Montreal at modal). Display type is medium-to-bold (500–700) with tight, often aggressively negative tracking (-1 to -3px at hero sizes: linear.app, clickhouse, composio, betterstack, hashicorp); hierarchy is built through size and the display/body weight gap, not through extra typefaces. A minority run display deliberately *light* at very large sizes for a quieter voice (modal, oxide-computer, codex, retool, sandclock). Body copy is small (13–16px), regular weight, muted gray, generous line-height.

The standard second voice is **monospace for micro-labels**: uppercase tracked eyebrows, nav chips, button labels, footer headings, and metadata (astro-build, gitbook, oxide-computer, osmo-supply, retool, cohere, holograph, everlend); code always renders in a real mono face with syntax color (JetBrains Mono at clickhouse/composio). A rarer editorial variant swaps in a serif for a few hero words or headlines (resend, hyperliquid, coinshift, lazy-so, literal-club). Signature headline devices recur across the corpus: exactly one colored or highlighted word/phrase per headline (modal, chroniclehq, clipdrop, mixpanel, jam-dev, openserv), gradient-filled keywords (dimension, framer, height-app), white-then-gray two-tone lines (diagram, morphic, gitbook), and sentence-case headlines that end with a period (betterstack, morphic, capital-xyz).

## Layout & shape
- **Nav**: slim single-row bar (56–64px) sitting directly on the canvas — logo left, sparse text links center, "Log in" text link + one filled CTA right (betterstack, linear.app, basehub, pirsch). Variants: floating pill nav capsule (mintlify, modal, hyperliquid, cohere) or no nav CTA at all (astro-build).
- **Hero**: centered stack — optional eyebrow/badge, 2-line headline, one-line subhead, 1–2 CTAs, then a large product screenshot or code window bleeding into darkness, often on an accent radial glow (basehub, composio, pirsch, outerbase). Left-aligned two-column with code/render right is the developer variant (checklyhq, modal, everlend, resend enterprise).
- **Section rhythm**: small accent eyebrow → large heading → short paragraph → screenshot or 2–3-column card grid, repeated at a 96px-plus vertical cadence (hashicorp, betterstack, composio, mixpanel). Bento grids of mixed-span cards are the default feature layout (diagram, chroniclehq, agentql, outerbase, framer).
- **Container**: ~1100–1280px centered column with wide dark margins; the black void itself is the whitespace — some sites leave screen-height gaps between sections (gitness, lazy-so, morphic).
- **Radius**: two shape camps that don't mix — pill buttons with 8–16px cards (fable, modal, mintlify, pirsch, framer) or compact 4–8px buttons with 8–14px cards (linear.app, clickhouse, composio, betterstack, eraser). Brutalist outliers go fully square with hairline borders (holograph, decideai, paper, oxide-computer).
- **Shadows**: none. Cards are canvas+one-step fills with 1px hairline borders (#23252a linear.app, #2a2a2a clickhouse); glow substitutes for elevation when emphasis is needed (dimension, luroapp, openserv).
- **Page rhythm breaks**: one inverted light band or full-accent band mid-page or pre-footer (basehub orange bands, chroniclehq off-white marquee, betterstack #F4F4F6 section, glideapps white/black alternation); dense multi-column footer, often with a giant cropped/ghosted wordmark bleeding off the bottom (osmo-supply, retool, coinshift, morphic, paper, holograph, capital-xyz).

## Do
- Keep the canvas one continuous near-black (#030303–#18 range, subtly tinted) and build every surface as a lightness step above it — never lighter than ~#242424 (linear.app, clickhouse, composio, gitness).
- Ration the accent to a single hue and spend it only on primary CTAs, links, eyebrows, glows, stat numbers, and one highlighted word per headline (basehub, betterstack, modal, everlend, mongodb).
- Put dark text on bright accents — yellow, lime, mint, and cyan CTAs read black-on-color or not at all (binance, clickhouse, modal, mongodb, jam-dev).
- Separate cards with 1px low-contrast hairline borders and tonal fill steps instead of any drop shadow (linear.app, betterstack, eraser, resend, hashicorp).
- Use real product UI as the hero imagery — dark-themed screenshots, terminal windows, and syntax-highlighted code panels, dimmed to blend with the page and lit by an accent glow (checklyhq, clickhouse, basehub, betterstack, resend).
- Keep body copy small and muted gray (#8b–#a1 range), reserving white strictly for headings and key numbers (gitness, everlend, chroniclehq, jam-dev).
- Give every section a small eyebrow label — uppercase tracked, ideally monospace — before the heading (hashicorp, betterstack, fable, oxide-computer, osmo-supply, gitbook).
- Set display type in one grotesque at 500–700 with tight negative tracking; scale, not extra fonts, carries hierarchy (clickhouse, linear.app, composio, hashicorp).
- Break long dark scrolls exactly once or twice with an inverted moment: a light band, a full-accent CTA band, or an off-white marquee (basehub, betterstack, chroniclehq, glideapps, codex).
- Repeat one identical CTA treatment at every conversion point — hero, mid-page, pre-footer (basehub, replit, awesomic, fable, pirsch).

## Don't
- Don't add drop shadows, glassmorphism, or elevation stacks — depth in this style is tonal steps, hairlines, and glow only (linear.app, clickhouse, resend, hashicorp, eraser).
- Don't introduce a second saturated brand hue in the chrome; extra colors may live only inside artwork, screenshots, and semantic status dots (basehub, composio, betterstack, modal, osmo-supply).
- Don't set body copy in pure white at full contrast — it flattens the hierarchy the gray ink creates (checklyhq, everlend, jam-dev, gitness).
- Don't use pure #000 as the whole canvas by default; the strongest examples tint their black (blue #010102 linear.app, navy #0E1525 replit, violet #0B0714 openserv) — and don't brighten it toward gray either (everlend, replit).
- Don't mix shape grammars: if buttons are pills, keep them pills sitewide; if compact 4–8px rectangles, never pill them (fable vs. linear.app; luroapp explicitly forbids mixing).
- Don't put white text on yellow/lime/mint accent fills (binance, clickhouse, modal, mongodb).
- Don't spread gradients onto body text, card fills, or large surfaces — gradients belong to headline keywords, one CTA, and background glows at most (dimension, framer, height-app, luroapp).
- Don't use stock photography or generic illustration; the imagery vocabulary is product UI, code, schematic linework, and 3D renders (codex, holograph, oxide-computer, eraser, gitness).
- Don't crowd sections or shrink the vertical gaps — the black dead space between blocks is a structural element, not waste (gitness, lazy-so, morphic, chroniclehq).
- Don't ship a light theme as an afterthought inversion; either stay dark end-to-end (hashicorp, morphic, eraser) or mirror the layout deliberately in both themes (mintlify, height-app).

## Canonical examples
- **linear.app** — the reference implementation: #010102 canvas, five-step charcoal ladder, hairlines, one lavender accent, screenshot-led sections.
- **clickhouse** — purest one-accent discipline: black + electric yellow, Inter 700 negative tracking, SQL windows as imagery, zero shadows.
- **basehub** — single orange doing everything (CTA, glow, highlight ring, full-width band) on #030303 grayscale restraint.
- **betterstack** — the section-rhythm template: purple eyebrow → tight sentence-case headline with terminal period → dimmed glowing screenshot.
- **composio** — brightness-ladder elevation codified (#0f0f0f → #181818 → #222222), one deep blue, pure-black code surfaces.
- **modal** — light-weight display type, lime accent, one green phrase per headline, grainy 3D renders, hairline-grid density.
- **resend** — grayscale + white-pill-CTA branch: true black, serif display collision, green as semantic signal only.
- **oxide-computer** — terminal-brutalist wing: uppercase monospace as system voice, mint green, hairline everything, 2–3px radii.
- **hashicorp** — enterprise-scale version: pure black, one family/three weights, per-product accent tokens, surface-lift elevation.
- **astro-build** — multicolor-glow branch: color enters only via blurred aurora artwork and gradient pill CTAs on charcoal.
- **framer** — the maximal end: per-section gradient headlines and neon bento tiles while the canvas stays pure black.
- **gitness** — cinematic minimal end: white pill CTA as the sole high-contrast element, photoreal 3D renders supplying all color.
