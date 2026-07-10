---
name: liveblocks
kind: site
style: DN
category: dev-platform
website: https://liveblocks.io/
pages: [home, product, feature (comments/notifications/presence/dashboard/infrastructure), pricing, company]
palette:
  canvas: "#0a0a0c"
  ink: "#a3a3ab"
  primary: "#ffffff"
  accents: ["#a78bfa", "#f472b6", "#34d399", "#fbbf24", "#f97316"]
typography:
  display: "geometric grotesque (Inter/Neue Haas feel, slightly rounded terminals) · bold 600-700 · tight, near-negative tracking"
  body: "same grotesque family, regular weight, small sizes (~14-16px)"
radius: "buttons pill; cards medium 8-14px"
---
## Overview
Near-black, almost lightless pages where color is rationed to small neon signals: each product line owns a hue (comments orange, notifications green, text editor blue, realtime APIs pink, dashboard purple) rendered as glassy 3D gradient icons on the void. Headlines are large white bold grotesque; everything else is quiet gray. The mood is precision developer-infra with jewel-like accents, not a glowing cyber aesthetic — glow appears only in controlled moments (hero gradients, the horizon "planet curve" before the final CTA).

## Layout
Slim one-row nav: wordmark left, text links center-left, Sign in + pill Sign up right, on transparent black. Feature-page heroes are centered: 3D product icon, monospace uppercase letterspaced eyebrow (e.g. "N O T I F I C A T I O N S"), 2-line bold headline, one-line subhead, white pill CTA + ghost "Read the docs" link, then a large product screenshot/demo panel. Home hero breaks the pattern with a pink-gradient staggered headline over a dot-matrix motif. Sections alternate centered intros with hairline-divided bento grids (2-3 columns of feature cards sharing 1px borders, no gaps). Every page closes with a glowing white horizon arc under "Add collaboration to your product today" and a single pill CTA, then a dense multi-column footer. Generous vertical whitespace; content column ~1100-1200px.

## Components
Buttons: primary is a white pill with black text and a trailing arrow ("Sign up for free →"); secondary is a dark gray pill or borderless text link with arrow; pricing highlights one plan with a yellow (#f4cf5e-ish) pill. Cards: #101013-ish panels with 1px #26262b borders, 8-14px radius, flat (no drop shadows); bento cells share hairline borders. Embedded UI demos are rendered as realistic dark-app screenshots inside rounded browser/window chrome. Pricing table uses hairline row rules with the featured column elevated on a lighter panel. Eyebrow labels in mono uppercase tinted with the section's accent color. Inputs (in demos) are dark fills with subtle 1px borders, small radius.

## Signature
- Per-product neon color coding via glassy, gradient-lit 3D icons (speech bubble, "T", hexagon, lightning bolt) floating on pure black
- Monospace, uppercase, wide-letterspaced eyebrow labels above every section headline
- White pill CTA with arrow repeated identically across all pages
- Glowing horizon/planet-curve divider before the final CTA section
- Hairline-bordered bento grids of small icon+text feature cards with no cell gaps

## Do
- Keep the canvas near-black (#0a0a0c) and let 90% of the page be white/gray text; use accent colors only for icons, eyebrows, and tiny status dots
- Assign one accent hue per product/feature and keep it consistent everywhere that feature appears
- Use the mono uppercase eyebrow + bold 2-line centered headline + one white pill CTA as the section formula
- Show the product as realistic dark-UI screenshots or live demos inside bordered rounded panels
- Separate feature cards with shared 1px #26262b hairlines instead of gaps and shadows

## Don't
- Don't fill backgrounds with color, gradients, or heavy glow — gradients belong only to icons, the home hero headline, and the horizon arc
- Don't use colored or gradient-filled CTA buttons (except the single yellow featured-plan button on pricing); primary stays white-on-black
- Don't add drop shadows or elevation to cards; the system is flat panels + hairline borders
- Don't use serif or decorative display type; everything is one grotesque family at different weights
- Don't crowd sections — keep large empty vertical bands between centered intros and their card grids
