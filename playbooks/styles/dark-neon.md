# Dark Neon Style Playbook
> Coverage: 28 sites from corpus (analyzed 28)

## Essence

Dark Neon is a near-black stage where light is rationed, not sprayed. The canvas is a very dark neutral or tinted void (#000–#1f1633 range), typography stays quiet — white headings, muted gray body — and nearly all color arrives through one controlled channel: soft gradient glows (evervault, reflect, idle-finance), saturated 3D renders or product screenshots (endlesstools, coinflect, risecalendar), or a single reserved accent (madewithgsap's lime, tome's magenta, super's magenta). The signature paradox of the style is that the loudest CTA is usually a plain white pill on black (revolut, langbase, graphy, liveblocks, aave), not a neon button. Depth comes from luminance steps and hairline borders, never drop shadows; glow is atmospheric, living behind or inside content, not on the UI chrome itself. The result reads as premium, engineered, and cinematic — a dark room where each section gets exactly one light source.

## Palette formula

**Canvas** is near-black but rarely pure #000 — most sites tint it: navy (aave #14161F, evervault #0A0A12, galileo-ft #02081A, idle-finance #071233), violet (reflect #030014, threads #0E0B17, sentry #1f1633, super #16021B), or neutral charcoal (endlesstools #1e1e1e, metadrop #1A1A1A, madewithgsap #0D0D0D). True #000 appears only in the boldest cases (revolut, beeper, tome, langbase). **Ink** for body copy is deliberately muted gray (#909090–#C9CBD4), never full white — white is reserved for headings and CTA labels (langbase, risecalendar, unicorn). **Primary action** is most often white/off-white (aave, graphy, idle-finance, revolut, liveblocks, langbase, metadrop), occasionally one saturated solid (tome #FF00BF, risecalendar #6D68E9, uizard #2E6FF2, super #E90D74). **Accents** are neon-adjacent hues — violet, magenta, cyan, lime, coral — confined to glows, imagery, eyebrows, and per-feature color coding; they almost never fill buttons or backgrounds. Elevated surfaces sit one luminance step above canvas (#141414–#1C1F2B) with optional 1px hairline borders.

Example palettes (all from corpus):
- **Violet-bloom infra** (evervault): canvas #0A0A12 · ink #C9CBD4 · primary #FFFFFF · accents #7B5CFF, #5B2EEA, #B9A6FF
- **Navy + aurora gradient** (aave): canvas #14161F · ink #CFD2DC · primary #FFFFFF · accents #2EBAC6, #B6509E, #38D275
- **True black + gradient spectrum** (raycast): canvas #07070a · ink #a6a6ad · primary #e8e8ec · accents #ff6363, #b968ff, #56c2ff, #59d499
- **Charcoal + single lime signal** (madewithgsap): canvas #0D0D0D · ink #F2F0EA · primary #CDF546 · accents #F2542D, #F5B821, #8FE0B4
- **Indigo void + one violet family** (reflect): canvas #030014 · ink #aca4c4 · primary #1e0b45 · accents #6c35f0, #736995, #c9bdf5
- **Black + magenta stamp** (tome): canvas #000000 · ink #E7E7E7 · primary #FF00BF · accents #8A5CF6, #5B7CFA, #2FD05E

## Typography formula

The default is a single neutral-to-geometric grotesque family at every level — Inter/Aeonik/Graphik-like — at medium-to-bold weight with slightly tight tracking (aave, evervault, raycast, liveblocks, idle-finance, index-inc, graphy, uizard, threads, galileo-ft). Two weight philosophies coexist: heavy display (beeper, raycast bold-to-extrabold; revolut runs Aeonik Pro 500 at 80–136px with line-height 1.0) versus deliberately quiet regular-weight headings where imagery carries drama (endlesstools, coinflect, graphy medium). Body copy is small (14–16px), regular weight, muted gray, generous line-height — universally.

Three recurring departures, each intentional: (1) **serif-led voices** — clay-earth sets even body copy in a Tiempos-like serif; super pairs a GT Super-style bold serif headline with a tiny geometric sans body; metadrop and tome drop serif set-pieces into sans systems. (2) **monospace as UI voice** — metadrop sets all functional chrome (nav, buttons, tables) in uppercase mono; madewithgsap uses 10–12px uppercase mono for every label and button against 100px+ grotesque display; liveblocks uses mono uppercase letterspaced eyebrows; astro-dither is bitmap mono only. (3) **micro-eyebrows** — tiny wide-tracked uppercase kickers above headlines are near-universal (clay-earth, langbase, liveblocks, endlesstools, safepal, galileo-ft).

## Layout & shape

Slim single-row top nav — wordmark left, sparse links, one high-contrast pill CTA right (aave, coinflect, graphy, tome, index-inc); a floating capsule/pill nav is a common variant (evervault, reflect, threads, whimsical). Heroes are usually center-axis: badge/eyebrow, 1–2 line headline, one CTA, then a large product screenshot or glow artwork (reflect, langbase, threads, index-inc, uizard). Sections breathe with extreme vertical whitespace — 150px+ gaps of empty dark canvas replace dividers (evervault, idle-finance, clay-earth, tome, coinflect). Rhythm devices: alternating black/charcoal or dark/light full-bleed bands (beeper, revolut, graphy, sentry, uizard, safepal), bento grids with shared 1px hairline borders (liveblocks, unicorn, langbase), and glowing horizon/planet arcs before the final CTA (liveblocks, reflect, risecalendar, index-inc).

Shape: buttons are most commonly pills (aave, evervault, graphy, revolut, metadrop, safepal, clay-earth); a boxy minority runs 2–8px (tome, madewithgsap, unicorn, idle-finance). Cards run larger radii than buttons — 10–20px — filled one step lighter than canvas with hairline 1px borders and **zero drop shadows**; depth comes from luminance and internal glow (evervault, liveblocks, graphy, index-inc, revolut, risecalendar). Imagery is 3D renders, gradient blooms, or real dark-mode product UI — almost never stock photography (idle-finance, index-inc, whimsical, coinflect).

## Do

- Tint the dark canvas — lean navy (#0A0A12 evervault, #02081A galileo-ft) or violet (#030014 reflect, #1f1633 sentry) rather than defaulting to flat gray; reserve pure #000 for hard-edged brands (revolut, tome, langbase).
- Make the primary CTA the brightest object on the page: a solid white/off-white pill with dark label, repeated identically everywhere (langbase, graphy, idle-finance, revolut, metadrop, liveblocks).
- Set body copy at muted gray (#909090–#C9CBD4), never white — white belongs to headings and button labels only (langbase, risecalendar, unicorn, coinflect).
- Elevate cards with a one-step lighter fill plus an optional 1px low-contrast border; let tone and spacing do all separation (evervault, liveblocks, graphy, idle-finance, revolut).
- Ration accent color to one channel per page: a gradient bloom family (evervault violet), one reserved hue (tome magenta, madewithgsap lime, risecalendar violet), or per-feature color coding kept consistent (liveblocks, threads pricing tiers).
- Keep glows soft, local, and behind/inside content — hero backdrops, card interiors, horizon arcs — never as strokes on UI (evervault, reflect, graphy, index-inc).
- Let imagery carry all saturation: hyper-colored 3D renders (endlesstools, coinflect), real dense product screenshots (risecalendar, index-inc, raycast), or data-viz-as-ornament (graphy) against grayscale chrome.
- Precede headlines with tiny uppercase eyebrow labels, optionally in an accent color or monospace (liveblocks, langbase, clay-earth, safepal, endlesstools).
- Punctuate with oversized stat numerals over tiny muted captions — numbers as hero content (aave's giant TVL, idle-finance stat rows, super's stat-pill marquee).
- Separate chapters with enormous empty vertical gaps or full-band background flips instead of rules and dividers (revolut, beeper, clay-earth, tome).

## Don't

- Don't fill buttons with neon accents or gradients as the default — accent-filled CTAs are the exception (index-inc's lone coral pill, tome's magenta), and even then exactly one hot button per viewport; aave, revolut, graphy, langbase all forbid colored CTAs outright.
- Don't add drop shadows or bevels to dark cards — every profile in the corpus replaces elevation with luminance steps, hairlines, or internal glow (revolut, liveblocks, evervault, raycast, coinflect).
- Don't flood sections with gradient backgrounds; glow blooms stay local to heroes, footers, and card interiors while mid-page stays flat dark (beeper, graphy, langbase, index-inc).
- Don't brighten body copy to pure white or tint it with accents — long copy stays mid-gray even next to full-spectrum gradients (raycast, langbase, threads, risecalendar).
- Don't scatter multiple accent hues within one section or one component system — each block commits to one hue (aave, coinflect's orange-phrase rule, sentry's one-lime-per-viewport rule).
- Don't use stock photography or generic illustration — the style's imagery is 3D renders, gradient artwork, and real product UI (idle-finance, whimsical, index-inc, risecalendar); photos, when they appear, go grayscale (clay-earth).
- Don't give buttons and cards the same radius — buttons pill or small, cards visibly larger (threads, coinflect, clay-earth's deliberate radius mix).
- Don't rely on glassmorphism, neon strokes, or outer glows on interactive chrome — edges stay crisp and matte (aave, galileo-ft, clay-earth, tome).
- Don't crowd the nav — corpus navs carry a wordmark, a handful of links, and one CTA at most (beeper's single link, endlesstools' near-empty bar, index-inc).
- Don't let the whole page glow at uniform intensity — hierarchy comes from giving each section exactly one luminous focal point in a sea of dark (reflect, coinflect, langbase).

## Canonical examples

- **evervault** — the archetypal soft-violet-bloom-on-navy formula: white pill CTA, hairline cards, glow as the only depth cue.
- **raycast** — rainbow gradients rationed to panels and one halo'd climax button while chrome stays colorless.
- **liveblocks** — per-product neon color coding, mono eyebrows, hairline bento grids, and the horizon-arc closing CTA.
- **langbase** — the austere extreme: true black, gray body, one white pill, color budgeted to a single hero render and two eyebrow hues.
- **reflect** — single-hue discipline; one glowing violet celestial object per section on an indigo void.
- **revolut** — hard black/white band flips, 136px display type, white-pill-on-black CTA doctrine, zero shadows.
- **graphy** — charts as neon ornament on a strict black/white base; accents live only in data visuals and highlighted words.
- **index-inc** — the one-warm-accent pattern: a lone glowing coral CTA on a cool violet aurora canvas full of real app UI.
- **madewithgsap** — the brutalist-mono variant: lime as the only chrome color, extreme type-scale contrast, ↳-prefixed CTAs.
- **endlesstools** — grayscale-shell-as-gallery: every CTA the same off-white pill, all saturation delegated to 3D artwork.
- **risecalendar** — light-to-dark gradient fusion and one violet doing all interactive work amid screenshot-driven storytelling.
- **metadrop** — terminal-flavored DN: uppercase monospace chrome, white pill CTAs, lime signal color, rainbow gradients kept decorative.
