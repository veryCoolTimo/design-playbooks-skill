---
name: planetscale
kind: site
style: ML
category: database-saas
website: https://planetscale.com/
pages: [home]
palette:
  canvas: "#ffffff"
  ink: "#1a1a1a"
  primary: "#f35815"
  accents: ["#0a0a0a", "#2b6bdb", "#e8434f", "#f6c750"]
typography:
  display: "Inter-like neo-grotesque · semibold · slightly tight"
  body: "Same neo-grotesque, regular; JetBrains-style monospace for CLI/code blocks"
radius: "pill buttons; medium 8-14px cards and dashboard panels"
---
## Overview
Stark white engineering minimalism punctured by two counterweights: a signature orange (#f35815) used almost exclusively as outline and arrow color, and full-bleed near-black (#000-#111) sections that showcase product UI in cinematic dark. A rainbow gradient band (blue → purple → pink → orange → yellow) peeks from behind the hero dashboard screenshot, the one moment of saturated color on an otherwise monochrome canvas. The product itself — dashboard, terminal, query charts — is the imagery; there is no decorative illustration.

## Layout
Slim single-line nav: logo left, four text links, "Sign in" plus one outlined pill CTA right. Hero is left-aligned text (two-line headline, no subhead visible) over a huge centered dashboard screenshot in a rounded, softly shadowed frame, with the rainbow gradient bleeding out from behind it. Page alternates long white sections (#fff/#fafafa) with long black sections (#000/#111), each running multiple viewport heights. Feature storytelling uses small app-icon tiles paired with UI screenshots in a repeating icon-left / screenshot-right rhythm. Section labels use a small orange vertical bar beside short intro text. Very generous vertical whitespace; content sits in a wide centered container.

## Components
Buttons: pill-shaped, outlined-only — primary CTA is white/transparent fill with 1px #f35815 border, dark label, and an orange chevron; secondary actions are bare text links with orange chevron. On dark sections the same orange-outlined pill appears on black. Inside product screenshots, buttons are rectangular small-radius (Connect = white w/ gray border, New branch = solid black). Cards: dark announcement cards (#111) with ~12px radius, green "New" pill badge, white title, gray body, chevron link. Dashboard frame has large radius (~16px) and diffuse drop shadow. Small outlined chip toggles (MacOS / Windows / Manual) in mono type on terminal cards. Progress bars in blue; charts in light blue/green bars.

## Signature
- Orange used only as a line: pill outlines, chevrons, section-marker bars — never as a filled button
- Long full-bleed black product-cinema sections alternating with clinical white ones
- Rainbow gradient escaping from behind a giant dashboard screenshot in the hero
- Isometric grid of colorful customer app-icon tiles as the social-proof section
- Real terminal output and mono type as first-class visual content

## Do / Don't
Do:
- Keep CTAs as outlined pills with #f35815 border and chevron on white or black; label stays dark/white, never orange
- Alternate multi-screen white and pure-black sections; showcase real product UI at large scale in both
- Confine saturated color to the hero gradient, customer icons, and chart marks; keep chrome monochrome
- Use monospace terminal blocks and CLI snippets as content, styled on dark panels
- Mark section intros with a thin orange vertical bar next to short gray text

Don't:
- Fill buttons with the brand orange or use it for body links (in-product links are blue/purple)
- Add drop shadows or borders to white-section cards beyond the single hero screenshot frame
- Center the hero headline — it sits left-aligned above the screenshot
- Introduce illustration or photography outside grayscale customer portraits and product shots
- Use square or small-radius marketing buttons; pills only outside product screenshots
