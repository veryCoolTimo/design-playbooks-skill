# Illustration-Driven Style Playbook
> Coverage: 33 sites from corpus (analyzed 33)

## Essence
Illustration-driven sites hand the entire emotional and chromatic load to custom artwork — painted murals, hand-inked doodles, 3D toy renders, pixel scenery, engraved line art — while the UI chrome underneath stays disciplined, flat, and nearly monochrome. The canvas is almost never pure white or pure black: it is warm cream, paper gray, or tinted charcoal, chosen so the art reads as printed or painted onto a physical surface (clay-com, adaline, tracky, micro). Saturated color lives inside the illustrations and in exactly one reserved CTA hue; buttons, cards, and text stay in ink-and-paper neutrals (kosmik, tally, todoist, kikin). Depth comes from hairline borders, flat color bands, and fill-value steps — essentially never from drop shadows, gradients on chrome, or glassmorphism. The result is a product page that feels hand-crafted, storybook, or zine-like, with real product screenshots acting as crisp "artifacts" placed on top of the illustrated world (cora, deta, operate, shortverse).

## Palette formula
**Canvas:** a warm or cool-tinted off-white in the #F1-F8 range (cream, paper, eggshell) for light sites; a warm near-black (#0F-1A range, never #000 except avara) for dark ones. Pure white canvases are rare and always compensated with heavy illustration (tally, vana, opencollective).
**Ink:** near-black with a temperature cast matching the brand — green-black (kikin #122216, saucelabs #0E2A1F), teal-black (dashlane #0E353D), warm charcoal (clay-com #1A1A1A). Body copy often steps down to mid-gray while headings stay full-ink (krepling, qatchup, todoist).
**Primary:** ONE saturated hue reserved almost exclusively for CTAs and interactive emphasis — the single loudest thing outside the artwork. Several sites go further and make the CTA black/white, pushing all color into illustration (clay-com, qatchup, micro, morflax, trunk).
**Accents:** 3-5 hues that live inside illustrations, badges, icon chips, and section bands — explicitly forbidden from UI controls (kikin, todoist, tracky, morflax).

Concrete examples:
- **adaline** — eggshell #F2F0E7 canvas, forest ink #1C2A21, deep green CTA #2C4A36, lime #D9E8A0 highlight; nature CGI carries all other color.
- **clay-com** — cream #F3EFE7, ink #1A1A1A, black pill CTAs #17150F; jewel bands rotate #2247F5 / #9E1258 / #0E5D38 / #F49E1B.
- **kikin** — cream #F4ECE3 + forest green #122216 used as both canvas and ink; electric #56DC49 strictly for CTAs; #EE6729 / #73D3EC / #EFE04A confined to badges and illustration.
- **hydra** — strict two-color: charcoal #101010, orange #F2731D, off-white #E9E7E2 text; whole sections flip orange-on-dark to dark-on-orange.
- **useportal** — paper #f7f7f7, soft ink #3d3d3d, one blue #297dfa for every actionable element; painterly twilight art (#929bde, #f2a0c0) bookends the page.
- **trunk** (dark) — charcoal #0F0F0E, gray ink #A9A9A6, off-white pill CTA #F5F5F3; one accent per product page (#4ADE80 / #9B5CF6 / #3B82F6 / #F5A31B) only on headline keywords and sketch highlights.

## Typography formula
Three recurring recipes, all pairing an expressive display voice with a quiet grotesque body:
1. **Editorial serif display + neutral grotesque body** — the most common "storybook" move: high-contrast or transitional serif headlines (Tiempos/Reckless/Canela feel), regular weight, sentence case, over Inter-like body. Cited: cora, deta, fly (slab), kosmik (light serif), statamic (italic emphasis words), prevalent-ai, useportal, passionfroot, micro (serif sublines).
2. **Single grotesque family at contrasting weights** — heavy/bold display, regular gray body, no second family: clay-com, tally, todoist, opencollective, shareup, krepling, dashlane; kikin pushes it to all-caps black weight.
3. **Character display face + clean body** — a novelty face carries the brand while body stays plain: obscura (bitmap/pixel), tableland (squared sci-fi techno), switch-lit (stencil-cut letterpress), shortverse (condensed Druk-like), avara (custom crossbar-less wordmark).
Cross-cutting habits: monospace or mono-flavored type for meta layers — micro-labels, stats, section numbers, footers (operate, micro, saucelabs, tableland, trunk, shortverse); one accent-colored or highlighted word per headline (shortverse, prevalent-ai, trunk, obscura, saucelabs, tally); sentence-case headlines that end with a period (vana, hook-xyz, micro "Organized.").

## Layout & shape
- **Full-bleed horizontal bands** are the dominant sectioning device: alternating cream/pastel/jewel or light/dark slabs instead of borders or shadows (clay-com, dashlane, saucelabs, prevalent-ai, reef, kikin, vana, hydra, passionfroot).
- **Continuous scroll murals**: one illustrated environment runs behind the entire page, its color shifts acting as section dividers — sky-to-dusk (cora), day-to-night (deta), desert dawn-to-indigo (tableland), a train track threading every section (trunk).
- **Bookend illustration**: full-bleed art at top and bottom framing a flat, quiet middle (shortverse, useportal, kikin, clay-com's garden footer, deta's sunflower strip).
- **Narrow centered columns with enormous vertical whitespace** — one idea per section, illustration filling the gaps (deta, micro, qatchup, opencollective, hook-xyz).
- **Radius**: pill buttons are the default (about two-thirds of the corpus: adaline, cora, hydra, micro, trunk, reef, statamic, tracky, qatchup, opencollective…); cards run medium-to-large 8-24px. A minority faction keeps corners near-square for a print/zine feel (dashlane, shortverse, kosmik, tally, passionfroot, fly).
- **Shadows**: essentially none. Separation comes from hairlines, tint steps, and color blocks (adaline, clay-com, dashlane, kikin, vana, hydra, prevalent-ai, trunk). Soft diffuse shadows appear only under floating product screenshots staged as collages (kosmik, shortverse, tracky, deta).
- **Handmade connective tissue**: squiggle arrows, dashed paths, torn-paper edges, sticky notes, marker annotations linking sections (tracky, qatchup, operate, passionfroot, opencollective, kosmik, useportal).
- **Screenshots as artifacts**: real product UI in crisp white/rounded frames floating on the illustrated or tinted field — the only "neutral" pixels on the page (cora, operate, deta, krepling, shortverse, todoist).

## Do
- Tint the canvas — warm cream (#F2F0E7 adaline, #F3EFE7 clay-com, #F4ECE3 kikin) or paper gray (#F1F0F6 kosmik, #f7f7f7 useportal) on light pages; warm charcoal (#0F0F0E trunk, #101010 hydra) on dark ones.
- Reserve exactly one saturated hue for primary CTAs and interactive emphasis; keep every other control neutral (kosmik orange, tally blue, todoist red, kikin green, tracky blue-violet, reef violet).
- Let illustration own all remaining color: accents belong to artwork, badges, and icon chips, never to buttons or links (morflax's purple lives only in 3D renders; kikin's orange/cyan/yellow live in badges; todoist's sage/mustard/blush live in gouache scenes).
- Separate sections with full-bleed color bands or the mural's own color shifts, not borders or shadows (clay-com, saucelabs, cora, deta, tableland).
- Keep surfaces flat: hairline 1px borders and fill-value steps for cards; shadows only under staged screenshot collages (adaline, hydra, trunk vs. kosmik, tracky).
- Pair an expressive display face (serif, stencil, pixel, techno, or heavy grotesque) with a quiet Inter-like body, and push meta text (labels, stats, section numbers) into mono or letterspaced small caps (operate, micro, saucelabs, tableland, statamic).
- Highlight one word or phrase per headline in the accent — color shift, marker swipe, or italic (shortverse, prevalent-ai, saucelabs, statamic, adaline, trunk).
- Stage real product screenshots as crisp framed artifacts on top of the illustrated world so the product reads trustworthy against the whimsy (cora, operate, deta, shortverse, krepling).
- Add handmade annotations — doodle arrows, script eyebrows, sticky notes, torn edges — as connective tissue between sections (qatchup, tracky, kosmik, passionfroot, operate, opencollective).
- Give the page a consistent illustrated sign-off: the same closing scene or oversized cropped wordmark on every page (clay-com's garden footer, adaline's aurora lake, vana's cropped "vana", micro's cropped wordmark, saucelabs's robot footer).

## Don't
- Don't use pure white canvas + pure black ink; the paper/ink temperature cast is core to the style (adaline, kikin, tracky, saucelabs, reef all warn against it explicitly).
- Don't put drop shadows, gradients, or glassmorphism on UI chrome — flatness is the near-universal law (clay-com, dashlane, kikin, vana, hydra, prevalent-ai, opencollective, trunk).
- Don't let accent colors leak into buttons, links, or backgrounds; a second saturated UI color breaks the one-CTA-hue discipline (todoist, shortverse, tally, kikin, morflax, obscura).
- Don't replace the custom illustration with stock photography, generic 3D, or flat corporate-vector blobs — the bespoke art style IS the brand (fly, statamic, todoist, vana, trunk, shareup).
- Don't crop hero artwork into small decorative thumbnails; illustration runs full-bleed or frames the page at scale (adaline, useportal, shortverse, tableland).
- Don't box everything into bordered, shadowed cards on a plain grid; content sits openly on bands and murals, with slight rotation/overlap where cards do appear (tableland, avara, kosmik, shortverse).
- Don't mix radius languages loosely — commit to pills everywhere or near-square everywhere; a page with both reads broken (adaline, morflax, tracky vs. dashlane, kikin, kosmik).
- Don't play the copy straight while the visuals are whimsical; the voice must match the art — jokes, periods on headlines, script eyebrows, founder letters (fly, vana, hook-xyz, qatchup, obscura).
- Don't crowd sections; the empty stretches of canvas or painting between blocks are structural, not wasted space (cora, deta, micro, hook-xyz, opencollective).
- Don't set body copy in the display face — serif/stencil/pixel/mono display voices are headline-only; body always returns to the clean grotesque (obscura, micro, switch-lit, tableland is the lone mono-body exception).

## Canonical examples
- **clay-com** — the archetype: cream canvas, black pill CTAs, jewel-tone bands, 3D garden footer sign-off on every page.
- **cora** — one continuous painted mural (sky → hills → dusk) as the whole page, white UI cards floating on it like paper cutouts.
- **deta** — storybook scroll from day sky to starry night; serif headlines, pastel quote cards, single email+Apply CTA repeated verbatim.
- **fly** — watercolor whimsy (balloons, SOC2 goat) + warm slab serif proving illustration-driven works for hard dev infra.
- **kikin** — national-park outfitter kit: all-caps black headlines, scout-patch badges, one electric green on forest/cream bands.
- **hydra** — the two-color extreme: orange/charcoal slabs with Greco-Roman line engravings that invert per background.
- **todoist** — quietest end of the spectrum: white canvas, one brand red, hand-painted gouache scenes in muted sage/mustard/blush.
- **tally** — marginalia mode: black-ink doodles and magenta scribbles animating an otherwise stark Notion-like page.
- **operate** — the "working document" conceit: one green ink for everything, dot-grid paper, numbered sections, marker-drawn arrows.
- **trunk** — dark-mode benchmark: sketched white train tracks threading an all-charcoal page, one accent hue per product, white pill CTA.
- **obscura** — character-face display done right: pixel headlines and 8-bit scenery wrapped around a clean grotesque SaaS body.
- **vana** — pop-art loud end: neon chartreuse blocks, comic-collage illustration in a fixed ink set, headlines that end with a period.
