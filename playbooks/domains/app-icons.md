# App Icons Domain Playbook
> Coverage: 93 icons from corpus

## When to use this corpus

- Designing a new app icon (iOS/macOS/Android) and needing proven shape, palette, and finish patterns to anchor the direction.
- Choosing between competing icon strategies — mascot vs. monogram vs. abstract glyph vs. scenic illustration — and wanting real examples of each done well.
- Restyling an existing icon (e.g., flat-to-3D, adding a gradient, simplifying a busy mark) with references for the target style.
- Producing adjacent brand assets (favicon, launcher icon, OG-image badge) that must read at tiny sizes.
- Writing an image-generation prompt for an icon and needing concrete vocabulary: "glossy gel squircle," "soft-embossed mascot," "die-cut sticker outline," "aura-gradient wordmark."

## Craft rules

1. **One idea per icon.** The strongest icons in the corpus are a single centered element on a single-color field: claude.jpg (one starburst on terracotta), cosmos.jpg (six dots on off-white), headspace.jpg (one orange circle-face on white). Resist composing multiple concepts; if the description needs an "and," cut something.

2. **Design the silhouette first, then verify at 60px.** A mark must survive as a shape with the interior detail gone. Duolingo crops to just eyes-and-beak because a full owl body would vanish at homescreen size; limbo.jpg is literally a black head silhouette with two dot eyes. If your mark's outline is ambiguous when filled solid black, rework the shape before touching color.

3. **Crop in, don't shrink down.** The corpus's mascot icons win by extreme close-cropping: duolingo.png fills the frame with the face, ahead.jpg crops a giant winking blob-head, skillsta.jpg crops the octopus at the edges. Whole-body characters floating in the center read as clip art; a face bleeding off the edges reads as a brand.

4. **Hold the palette to 2-3 colors.** Nearly every catalog entry lists two or three hexes: one saturated field, one high-contrast mark, optionally one accent (wise.jpg: green field + dark-green glyph; twitch.jpg: purple + black + white). Full-spectrum color is reserved for icons where the rainbow *is* the concept (google-gemini.jpg, instagram.jpg, sway.jpg) — and even those keep the foreground mark to a single neutral.

5. **Contrast is figure-vs-field, not hue-vs-hue.** The reliable formula is a near-white mark on a saturated mid-to-dark field (ynab.jpg's white Y-tree on periwinkle, claude.jpg's cream star on coral) or a near-black mark on a bright field (linktree.jpg, thru.jpg). Two saturated colors of similar value against each other muddy at small sizes.

6. **Pick a finish deliberately: flat, soft-3D, or full skeuomorph.** The corpus splits into three coherent finish tiers — flat vector (claude, duolingo, twitch), soft-3D/"gel" with gentle embossing and one light source (ynab, aave, xchat, amie), and photoreal skeuomorphism (hipstamatic's leather-and-glass camera, dion's CRT). Each works; mixing tiers within one icon (a flat glyph with one photoreal element) reads as unfinished.

7. **If you gradient, keep it quiet — or make it the whole show.** The dominant gradient move is a subtle vertical or radial shift of one hue on the background (ynab, sleepiest, raycast) that adds depth without stealing attention. The loud alternative is the full-bleed aura/blur field (sway.jpg, instagram.jpg) where the gradient itself is the mark's stage — in that case the foreground must be a single flat white or black element.

8. **Monograms: distort, don't typeset.** Letterform icons in the corpus never use a plain font glyph. They rebuild the letter as an object: ynab's Y becomes a tree trunk, retro.png chromes and slices its R, arc-search draws its A as overlapping sticker strokes, wise.jpg abstracts W into a flag-arrow. If the monogram could be reproduced by typing a character, it is not distinctive enough.

9. **Give mascots a face and an expression, not anatomy.** Corpus mascots are reducible to eyes plus one emotive detail: headspace's closed-eye smile, ditty's winking ring, fabric's smiling folder, tripadvisor's ringed owl eyes. Expression (wink, smirk, sleepiness) carries personality; limbs, textures, and props mostly add noise — dogo.jpg's leash is the rare prop that survives because it is one bold shape.

10. **Treat the background as part of the composition.** Solid saturated fields dominate (roughly the whole flat cohort), with two sanctioned upgrades: a soft same-hue gradient (rule 7) or a textural field that stays low-contrast — linear-mobile's dotted charcoal, bump.png's light-ray glow, orb-social's grainy dot grid. Never white-on-white or a busy pattern that competes with the mark.

11. **Full-bleed scenes are a genre, not a default.** Edge-to-edge illustration (alto-s-adventure, monument-valley, slumber, inside) works for games and mood-driven apps because the scene *is* the product. These still obey silhouette discipline: one large focal shape (a sun, a pedestal, a moon) anchors the frame. Utility apps should stay with glyph/monogram/mascot.

12. **Leave breathing room: mark occupies roughly 50-70% of the frame.** Centered marks in the corpus (claude, cosmos, one-year, perplexity) keep generous margins so the OS corner-rounding never clips them and the shape reads as deliberate. Only mascot close-crops and scenic full-bleeds are allowed to touch the edges — and they must be designed to be cropped.

## How to navigate

- **Catalog:** /Users/timo/.claude/design-library/profiles/icons.md — one bullet per icon: `filename — visual description · style: tags · palette: hexes`. Grep the style tags (`flat`, `3d`, `glassy`, `gradient`, `mascot`, `monogram`, `skeuomorphic`, `sticker`, `wordmark`, `pixel-art`) to shortlist by approach, or grep hex prefixes to shortlist by hue family.
- **Images:** /Users/timo/.claude/design-library/media/app-icons/<filename> — Read the actual file for any shortlisted entry before citing it; descriptions compress a lot (e.g., bump.png's light-ray floor and gel core only fully register in the image).
- **Workflow:** pick 3-5 catalog entries matching the target style tags, Read those images, extract the shared moves (finish tier, mark-to-frame ratio, palette structure), then design against them.

## Best references

- **claude.jpg** — the flat-logomark ideal: one organic-geometric cream starburst on a single coral field, perfect 60px silhouette.
- **duolingo.png** — mascot close-crop masterclass: face fills the frame, three colors, instantly legible.
- **ynab.jpg** — soft-3D monogram-as-object: embossed glassy white Y-tree with a quiet periwinkle gradient background.
- **bump.png** — maximal glossy 3D: gel-core arrow with rim lighting and a glowing ray backdrop; the reference for candy skeuomorphism.
- **hipstamatic.jpg** — full photoreal skeuomorphism: leather texture, glass lens, physical shutter button; the icon as a miniature object.
- **sway.jpg** — gradient-as-stage: blurred aura field carrying a single white italic wordmark; the loud-gradient pattern done with restraint.
- **headspace.jpg** — minimum-viable mascot: an imperfect orange circle plus closed eyes and a smile equals a complete brand character.
- **wise.jpg** — abstract monogram: letterform abstracted into an angular flag-arrow glyph, two-green figure/field contrast.
- **monument-valley.jpg** — scenic full-bleed genre: isometric game scene anchored by one bold focal pedestal, flat gradient palette.
- **linear-mobile.jpg** — textural background pattern: metallic rising-sun mark on a dotted charcoal field that adds depth without noise.
