# About Page Playbook
> Coverage: 37 examples from corpus (analyzed 20)

## Anatomy

Ordered skeleton observed across the sample (top to bottom):

1. **Nav** — standard site nav; "About" link usually highlighted as active (cap, common, monad). ~100%
2. **Statement hero** — mission phrased as a bold declarative headline, not "About Us": "Acctual is rethinking B2B payments for a borderless world" (acctual), "The web is what we make it" (astro-build), "Powering the modern security data lake." (monad). ~90% use a statement; only ~25% use a literal label like "About Cap" (cap, flox) or "Our Story" (buymeacoffee). Layouts: centered text ~60%, left-aligned with visual on right ~30% (astro-build, cohere, codex). ~15% add a stat trio directly under the hero — team size / locations / founding date (dope-security) or founded / raised / users / creations-per-day (gamma), team count + countries (morphic).
3. **Story / mission narrative** — ~90%. Three major forms:
   - **Founder letter** with real signature scan and sign-off (~25%): buymeacoffee ("Sip sip hooray. — The BMC team" + drop cap), hatch-fm ("A note from Erik" card with headshot), hellotime ("…so we created Hellotime" card signed by both co-founders), equals ("– Team Equals" essay).
   - **Manifesto** — sequence of large standalone statements (~20%): fabric-so (full-page typographic manifesto, "A digital library of Alexandria"), headroom ("MANIFESTO" badge + belief bullets), common ("Our Common Goal" call-to-action prose).
   - **Sectioned narrative** — alternating headline + short paragraph blocks (~45%): acctual, astro-build, codex, monad ("Our story" with bulleted problem framing), cap (numbered Problem/Solution cards).
   - **Timeline** variant (~10%): genway (vertical dated milestones: Hackathon → Validation → Prototype → Incorporation → Early Adopters), morphic (horizontal interactive timeline in hero).
4. **Team section** — ~65%. Forms: uniform headshot grid with names + roles (cakeequity, equals, flox with LinkedIn/GitHub icons per person, dimension, cohere grouped Founders / Technical Leaders / Operating Leaders); founders-only trio with bios (genway, monad, acctual's polaroids); candid photo collage instead of a grid (dope-security scattered photos with `ex-Symantec/Forcepoint` code-style captions, gamma mosaic + personality tags like "Pet snugglers, Pickleballers", cakeequity lifestyle strip, hatch-fm network diagram of avatars); carousel (codex).
5. **Values / beliefs / principles** — ~40%: astro-build ("Our core beliefs" 3 cards), gamma (accordion: "Don't be boring, Stay scrappy…"), genway (numbered 01/02/03), hatch-fm ("We believe" 2×2 grid + one highlighted callout), headroom (belief bullets), cap (feature-style cards).
6. **Investors** — ~50%: logo row (acctual, equals, gamma, monad pairing "Backed by world class investors" with founders side by side, buymeacoffee "Backed by" + Y Combinator/Stripe); expanded angel cards with photos and affiliations (dimension, codex including "MARK CUBAN", "BALAJI SRINIVASAN"). flox weaves investors into story prose instead.
7. **Social proof** — ~30%: press logos (buymeacoffee "As seen on", dope-security "See what the buzz is about", gamma "In the news" article cards), community tweets (astro-build), customer logos (codex), customer testimonials (hatch-fm), employee testimonials (common).
8. **Offices / locations** — ~15%: cakeequity (emoji + city cards), cohere (office photos), morphic (globe + countries stat).
9. **Hiring block** — ~55%: genway ("We're hiring!" mid-page), astro-build ("See Open Roles"), codex (full-width neon "WANT TO WORK ON SOMETHING MEANINGFUL IN WEB3?"), common ("Interested in joining Common?"), morphic (entire page is hiring-oriented: FAQ, benefits grid, tech stack, open positions list), monad ("Work with us" + team photo).
10. **Final CTA banner** — ~85%: product CTA (cap gradient banner, genway dark banner, acctual "Love you, pay me" on green scrapbook board, gamma illustrated scene) or careers CTA (codex, common). ~25% follow with an oversized wordmark footer (equals, common, morphic, gamma).

## Patterns that work

- **Mission-as-headline beats "About Us."** The strongest pages open with the company's thesis as a full-width statement: "The spreadsheet we always wanted" (equals), "Big energy for small business" (headroom), "We build tools for imagination" (gamma). The word "about" appears only in nav/label eyebrows.
- **Founder letters with real signatures create trust.** buymeacoffee, hellotime, hatch-fm, and headroom all close narrative with scanned handwriting and names/roles; hatch-fm and hellotime frame the letter in a raised card so it reads as a document, not body copy.
- **Show humans doing human things, not stock headshots.** acctual uses polaroids with handwritten captions and yearbook photos; gamma tags its mosaic with hobbies; dope-security captions candid shots with previous-employer lineage (`fka Symantec+Forcepoint`) to signal seniority; cakeequity mixes a formal grid with a snowboarding/hiking photo strip.
- **Quantify the company in a stat strip.** dope-security (30+ team members / 3+ locations / May 4 founding day), gamma (2020 / $23M / 50M users / 700K creations per day), morphic (13 full-time / 8 countries). Three to four numbers, giant digits, small labels.
- **Investors are a section, not a footnote.** dimension and codex give each angel a card with photo + affiliation ("Tom Preston-Werner — Founder, GitHub"); monad splits the fold into "Backed by world class investors" | "Founded by security veterans" — social proof and humans on one line.
- **Problem → solution keeps the story scannable.** cap numbers them (1 The Problem / 2 Our Solution); hellotime stages it as "We've been there… / …so we created Hellotime"; monad bullets the three failures of the status quo before introducing the team.
- **Timeline turns a short history into content.** genway's dated vertical timeline gives a 1-year-old startup narrative weight; morphic puts an interactive founding timeline directly in the hero.
- **The page ends with a job, not just a product pitch.** codex, common, astro-build, and monad close with careers CTAs; genway repeats "Join our team" twice. About pages are read by candidates as much as customers.
- **Voice carries the page.** acctual's section headers joke ("Voted 'most likely to start a payments company' in high school"), buymeacoffee signs off "Sip sip hooray," dope-security puns on its own name — the copy does personality work that layout alone can't.

## Variants by style

- **Light minimal** (cap, flox, equals, hellotime, buymeacoffee): centered single column, generous whitespace, restrained accent color. Story is the hero; teams are small uniform grids or absent. Decoration is thematic and quiet — equals scatters dashed spreadsheet cells in the margins; hellotime uses hand-drawn mascot illustrations and emoji-sticker highlights inside the headline.
- **Editorial serif** (monad, buymeacoffee): serif display headlines, cream/paper backgrounds, long-form prose. monad pairs serif heads with monospace body and hairline section rules for a "printed report" feel; buymeacoffee uses a script headline + drop cap like a magazine letter.
- **Dark tech** (astro-build, codex, dimension, dope-security, morphic): near-black backgrounds, one neon accent (astro purple/orbs, codex acid-green cube and CTA block, dimension purple-pink gradient), glow effects. Heavier on investor/angel walls, stats, and hiring content; codex and dope-security use oversized/marquee display type and collage photography.
- **Colorful / playful** (gamma, cakeequity, common, acctual, hatch-fm): illustrated worlds (gamma's sky/clouds), floating avatars in the hero (cakeequity), children's drawings as team art (common), scrapbook props — tape, sticky notes, polaroids (acctual), mascots and blob shapes (hatch-fm). Personality-first copy; culture sections and employee voices appear here most.
- **Manifesto monochrome** (headroom, fabric-so): a single background color (headroom's full-bleed blue) or bare white (fabric-so), no team section, the entire page is typographic conviction plus one signature block or product visual. Works when the product is pre-launch and the argument is the asset.

## Anti-patterns

- **Literal "About Us" headline with nothing behind it** — only cap and flox lead with a plain label, and both immediately back it with substance; no strong page wastes the hero on boilerplate.
- **Wall-of-text biographies.** Nobody writes multi-paragraph bios per person. Name + role + optional one-liner ("Ironman, ex-Googler, and a UWC Alumni" — genway) or ex-employer tag is the ceiling.
- **Team grid without roles or links.** Every grid in the sample carries titles; flox and dimension add LinkedIn/GitHub per person. An unlabeled face wall communicates nothing.
- **Generic corporate stock photography.** Zero examples use it. Even formal pages (monad, cohere) use real office/team photos; playful ones use polaroids, collages, or drawings.
- **Skipping the closing CTA.** Only fabric-so ends without one, and it reads unfinished — the page just stops into the footer. ~85% convert the accumulated goodwill into "try product" or "see open roles."
- **Undifferentiated body copy blocks.** Weakest section observed: acctual repeats the identical paragraph under two different headlines — a sign the alternating headline/paragraph pattern needs distinct content per block or fewer blocks.
- **Values as unstructured prose.** cakeequity's "Creative Healthy Lifestyle, explained" buries its culture framework in three dense paragraphs; the pages that land values use cards, accordions, or numbered items (astro-build, gamma, genway).
- **Employee testimonials that all sound alike.** common's three quotes are near-identical in cadence and length and read as ghost-written; hatch-fm's customer quotes work better because they vary in length and cite specific outcomes.

## Checklist

1. Write the hero as the company's thesis in one sentence — bold statement headline, 1–2 sentence subhead; reserve "About" for the nav state or a small eyebrow label.
2. Pick one story form and commit: founder letter (with signature scan + names/roles), manifesto of large statements, sectioned narrative with distinct headline+paragraph blocks, or a dated timeline.
3. Add a stat strip if the numbers are impressive (team size, countries, funding, usage, founding date) — 3–4 giant digits with small labels.
4. Build the team section to match brand temperature: uniform grid with name + role (+ LinkedIn/GitHub) for professional; polaroids/collage/candid photos with witty captions for playful; founders-only trio with one-line bios if the team is small.
5. Include a values/beliefs section as 3–4 structured items (cards, numbered, or accordion) — never buried prose.
6. Add social proof appropriate to stage: investor logo row (or angel cards with photo + affiliation), press logos, customer logos, or community quotes.
7. Insert a hiring block ("We're hiring" + open-roles CTA) — candidates are a primary audience of this page.
8. Close with a full-width CTA banner (product trial or careers), visually distinct from the body (gradient, dark, or brand-color block).
9. Keep decoration on-theme with the product: spreadsheet cells for a spreadsheet company (equals), scrapbook props for invoicing personality (acctual), ASCII art for dev tooling (headroom).
10. Read all copy aloud — every section header should sound like a person from this specific company wrote it, not a template.

## Best references

- **equals** — letter-essay + team grid + investor logos in flawless minimal execution; on-theme spreadsheet-cell decoration and giant wordmark footer.
- **monad** — editorial serif/monospace system; investors and founders paired in one split section; disciplined hairline-rule structure.
- **gamma** — colorful maximalism done right: stat cards, personality-tagged team mosaic, principles accordion, press cards, illustrated CTA finale.
- **dope-security** — dark-tech team page with stat trio, candid collage with ex-employer captions, and strong voice throughout.
- **buymeacoffee** — the canonical founder-letter about page: script headline, drop cap, signature, backed-by + press row, nothing extra.
- **genway** — best small-startup pattern: founder trio with bios, dated milestone timeline, numbered mission values, dual hiring CTAs.
- **acctual** — personality-driven scrapbook style; polaroid founders, joke section headers, memorable "Love you, pay me" CTA.
- **headroom** — single-color manifesto with founder signatures; proof an about page can work with zero team photos when conviction carries it.
