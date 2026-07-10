# Gradient Mesh Style Playbook
> Coverage: 15 sites from corpus (analyzed 15)

## Essence
Gradient mesh is a light-canvas discipline where color arrives as atmosphere, not chrome: soft airbrushed multi-hue blooms, auras, ribbons, and orbs glow behind heroes, card art, and footers while the rest of the page stays strictly monochrome. The canvas is white or warm paper (cream, oat, greige), ink is near-black or deep navy, and exactly one saturated hue owns every CTA — the mesh itself never becomes a functional UI color (stripe, mymind, overflow, monad). Depth comes from blur, hairline borders, and whisper-soft diffuse shadows rather than elevation; heavy drop shadows are absent across the entire corpus. Typography carries the personality that color declines to: either one grotesque pushed to a weight extreme (thin 300 in stripe, ultra-black in kit) or an editorial serif/mono split (mistral.ai, monad, mymind, vetric, deta-space). The overall read is calm, editorial structure hosting one or two contained moments of chromatic energy.

## Palette formula
**Canvas** is never a dark theme and rarely a cool gray: either pure/near white (common, mistral.ai, overflow, portalgaming, replay, stripe, vetric) or a warm paper tint (#fdf6eb deta-space, #F7F5F2 jasper, #F5F3EE kit, #f7f4ed lovable, #F7F2E9 metaview, #F4F0E8 monad, #f2f1f3 mymind, #EBEAF6 genway). **Ink** is near-black but almost never #000 — deep navy #0d253d (stripe), charcoal #1c1c1c (lovable), warm #1E1C18 (monad); lovable builds every gray from one ink at reduced opacity. **Primary** is a single saturated CTA color used verbatim everywhere: electric purple #8624F5 (jasper), candy pink #ee72a8 (deta-space), vermilion #fd4b19 (mymind), indigo #533afd (stripe), mint #7DF0A8 (metaview), sky blue #3BA5F8 (kit) — or simply solid black (common, monad, overflow, portalgaming, vetric). **Accents** are the mesh stops: 3-5 adjacent or complementary pastels-to-saturated hues that live only inside gradients, illustration, frames, and tint blocks, never as buttons or links (stripe: "ruby and magenta never become buttons"; mymind: "blues/pinks live only inside gradients").

Example palettes:
1. **stripe** — canvas #ffffff, ink #0d253d, primary #533afd; mesh stops cream #f5e9d4, ruby #ea2261, magenta #f96bee, navy #1c1e54.
2. **metaview** — canvas #F7F2E9, ink #16161E, primary #7DF0A8; mesh runs cobalt #1F3DFF → teal #4FE3C1 → mint, plus blush #F5E9DE panels.
3. **mymind** — canvas #f2f1f3, ink #1c1b1a, primary #fd4b19; mesh peach #f9c5a8, pink #e9a7c9, periwinkle #a9b6e8.
4. **monad** — canvas #F4F0E8, ink #1E1C18, primary black #161513 pills; gradient auras periwinkle #9FB0F2, green #8ED08F, orange #F0925C.
5. **mistral.ai** — canvas #ffffff, ink #1f1f1f, primary #fa520f; sunset stripe #fa520f → #ffa110 → #ffd900 → #fff8e0.
6. **overflow** — canvas #fafafc, ink #000000, primary black; hero mesh blue #169afb, indigo #6b61f2, amber #fdc023.

## Typography formula
Two viable systems, both with tight display tracking:
- **Single grotesque, weight-differentiated**: one geometric/neo-grotesque family for display and body, distinguished only by weight and size — jasper (Matter-like), kit (ultra-heavy custom grotesque), metaview (Poppins-like), genway (Plus Jakarta-like), overflow and replay (Inter-like), portalgaming (Neue Haas-style, sentence case, quiet). Weight extremes are the flavor knob: stripe runs 300 with -1.4px tracking at 56px; kit runs the heaviest black weight; lovable caps at 600.
- **Editorial serif display + workmanlike body**: serif headlines at large sizes over a small sans or monospace — mistral.ai (PP Editorial Old 400 at 84px over Inter), mymind (Canela-like light serif at 120px+ over a small grotesque), monad and vetric (transitional serif over mono/Inter), deta-space (heavy condensed serif + script eyebrows + all-mono body).
- **Monospace micro-labels** are a recurring third voice: uppercase mono for eyebrows, nav, buttons, and metadata (common, monad, portalgaming, deta-space).
Negative tracking scales with size (lovable: -1.5px at 60px to -0.9px at 36px; stripe: -1.4px at 56px to -0.2px at 20px). Body copy is small, muted, and generously leaded everywhere.

## Layout & shape
Centered hero blocks with the mesh bleeding edge-to-edge behind them (stripe, overflow, genway, mymind, portalgaming), then a snap back to disciplined monochrome sections. Content sits in a ~1200-1280px container (stripe, mistral.ai, lovable) with lavish vertical rhythm — 64-208px gaps do the separating instead of divider lines (lovable, replay, vetric), or full-width 1px hairlines mark sections (monad, common). Long pages alternate light bands with near-black panels or bands for pacing (jasper, kit, metaview, genway) — dark panels are often inset rounded cards rather than full-bleed strips (metaview). A signature closer recurs: a gradient-washed CTA block or band just before the footer (monad's blue wash, mistral.ai's sunset stripe, genway's dark indigo panel, metaview's cobalt ribbon footer, jasper's dark mockup section). Radius splits into two camps: pill buttons (stripe, metaview, monad, mymind, genway, replay, portalgaming) or compact 4-8px near-rectangles (jasper, kit, common, mistral.ai, vetric, lovable) — pick one and hold it. Cards run 12-24px radius with 1px hairline borders and either no shadow or a faint diffuse one (lovable #eceae4 borders, stripe rgba(0,55,112,.08) shadow); illustration and screenshots live inside large rounded containers (portalgaming 20px+, overflow 16-24px thick colored frames).

## Do
- Confine the mesh to a few zones — hero backdrop, section edges, pre-footer CTA — and let the rest of the page run monochrome (overflow, stripe, mymind, vetric).
- Render gradients as soft, organic, blurred blobs/auras — "organic SVG blobs, not flat CSS gradients" (stripe); feather edges into the canvas, never hard crops (deta-space, monad).
- Pick one saturated CTA color and repeat it verbatim at every scale on every page (deta-space pink, jasper purple, metaview mint, replay pink, kit blue).
- Keep all UI chrome monochrome — nav, buttons, labels black-on-light — so color reads as artwork (portalgaming, common, overflow).
- Prefer a warm-tinted canvas (cream/oat/paper) over clinical white when in doubt; eight of fifteen sites do (kit, lovable, metaview, monad, mymind, jasper, deta-space, genway).
- Do containment with 1px hairline borders and tint fills, saving real shadows for floating product mockups (jasper, lovable, mistral.ai, monad).
- Push display type to an extreme — very thin (stripe), very heavy (kit), or a light serif at huge sizes (mymind) — with negative tracking scaled to size.
- Add a monospace or letterspaced-caps micro-label voice for eyebrows, nav, and metadata (monad, common, portalgaming, vetric kickers).
- Close every page with a recurring gradient-touched CTA moment before the footer (monad, mistral.ai, genway, metaview, jasper).
- Keep the mesh hues family-coherent: adjacent stops (genway's all-purple, mistral.ai's sunset range, metaview's blue→mint) or one fixed multi-hue recipe reused everywhere (stripe, mymind).

## Don't
- Don't put gradients on buttons, links, or any control — gradients are backgrounds and art only (monad, common, kit explicitly forbid it).
- Don't run the mesh behind body copy or mid-page reading sections; below the hero, color lives in accents and contained panels (overflow, genway, vetric).
- Don't stack heavy drop shadows or glassmorphism — depth is blur, hairlines, and soft diffusion across all 15 profiles (deta-space, kit, mymind, portalgaming).
- Don't let mesh accent hues become functional UI colors; secondary text stays neutral and links stay in the primary or plain ink (stripe, mymind, replay, genway).
- Don't use pure black ink or dead-gray neutrals — tint the ink (navy, charcoal, warm black) and derive grays from it (stripe, lovable, mistral.ai cream neutrals).
- Don't mix button geometries: either everything is a pill or everything is a compact 4-8px rectangle, never both (mistral.ai "explicitly not pills" vs. metaview "every button is a pill").
- Don't introduce a second competing CTA color or rainbow-colored headlines; emphasis is one hue plus scale (jasper, kit, mymind).
- Don't fill the whole page with the gradient or go full dark-theme — the style is a light page with contained chromatic moments (replay: "the neon lives inside embedded media"; overflow: "one-scene gradient mesh").
- Don't crowd sections; every block gets a full band of whitespace and one idea (portalgaming, overflow, kit, replay).
- Don't use harsh, high-contrast gradient stops with visible banding — stops are pastel-soft and heavily blurred even when the endpoint hues are saturated (mymind, monad, vetric).

## Canonical examples
- **stripe** — the archetype: edge-to-edge organic mesh hero as the entire depth system over a white, thin-type, one-indigo page.
- **mymind** — soft peach-pink-lavender orbs behind a paper canvas with giant light serif headlines; one vermilion doing every job.
- **metaview** — blue→mint 3D ribbons as hero, card, and footer art on warm cream, with a single mint pill CTA.
- **monad** — pastel gradient auras glowing behind thin line-art diagrams; serif + uppercase mono "technical stationery."
- **overflow** — the one-scene discipline: a blue-violet-orange aurora confined to the hero, strict monochrome below.
- **mistral.ai** — the sunset variant: warm orange-to-cream gradient stripe closing every page, serif/Inter editorial split.
- **genway** — monochromatic mesh: an entire site inside one purple family, from lavender canvas to violet orb to indigo panels.
- **portalgaming** — Swiss monochrome chrome hosting lavender mesh banners and rainbow ribbons inside big rounded cards.
- **common** — primary-color radial glow spots floating on pure white, held together by black CTAs and mono labels.
- **vetric** — airbrushed rainbow blooms and halftone ribbons under serif headlines; gradients never behind body text.
- **jasper** — greige canvas with a sunset mesh hero moment, pastel tint chips, and one electric purple CTA.
- **deta-space** — the painterly outlier: hand-painted sky gradients as full-width section dividers on warm cream, one pink CTA.
