---
name: displace
kind: site
style: DT
category: agency
website: https://displace.agency/
pages: [home]
palette:
  canvas: "#1a1415"
  ink: "#f5f5f7"
  primary: "#ff4a2c"
  accents: ["#3d9df3", "#8e8a8c", "#221c1d"]
typography:
  display: "SF Pro Display / system sans · bold for numerals, regular elsewhere · tight, with wide-tracked uppercase micro-labels"
  body: "SF Pro Text / Inter-like system sans"
radius: "large 16px+ (widget cards ~16-20px, dock tray ~24px, tooltip pill)"
---
## Overview
A faithful macOS desktop simulation used as an agency homepage: dark warm-charcoal wallpaper with a faint red-orange glow in the lower right, a real menu bar with Finder menus and status icons, desktop widgets standing in for content sections, file icons on the right edge, and a translucent dock of app icons at the bottom. Note: metadata says minimal-light, but the captured screenshots are unmistakably a dark theme. Everything reads as OS chrome rather than web page — content is delivered through widgets, files, and apps.

## Layout
No conventional nav; the top menu bar (logo, Finder, File, Edit, Go, Window, Help, clock, status icons) and the bottom dock replace it. No hero either — a left-aligned column of macOS-style widgets carries the messaging: dual-timezone clock ("The studio runs on two clocks", Madrid/Miami), a calendar widget doubling as the CTA ("Book a 30 min call"), a latest-journal card, two stat widgets (17 projects shipped, 5 open-source apps), and a music player ("Displace FM"). Desktop files (Projects folder, Journal, README.txt) sit top-right. The center is deliberately empty except a ghosted watermark logo, giving enormous negative space. A floating pill tooltip top-center invites interaction: "Everything here works — drag the windows, open Terminal, find the easter eggs."

## Components
Widgets are the core component: dark translucent cards (#221c1d-ish over the wallpaper) with ~16-20px radius, hairline light borders, no visible drop shadows, uppercase letter-spaced micro-labels in muted gray, oversized bold white numerals/values, and small gray captions. The calendar widget uses an orange-red "FRIDAY" label as its only saturated text. Traditional buttons are absent; interactive affordances are OS metaphors — play/skip glyphs in the music widget, dock icons that populate on hover/interaction (shot-02 shows more icons than shot-01), a pill-shaped dark tooltip with light text. Desktop icons pair a colored glyph with a small white label.

## Signature
- Full macOS desktop metaphor as the site: live menu bar, dock, draggable windows, desktop files, easter eggs.
- Content-as-widgets: stats, journal, booking, and music are Notification-Center-style cards, not sections.
- Vast empty desktop center with a ghosted logo watermark and a subtle warm red glow gradient in the wallpaper.
- Near-monochrome dark palette punctuated only by the red-orange brand accent and colorful "real" app/dock icons.

## Do / Don't
**Do**
- Keep the OS illusion consistent: system-font typography, hairline borders, translucent dark surfaces, authentic menu-bar/dock spacing.
- Deliver every content block as a widget or file — uppercase gray micro-label, big bold value, small gray caption.
- Reserve the red-orange accent for one or two touches (date label, logo, dock icon); let icons supply the remaining color.
- Leave the desktop center mostly empty; density lives on the left column and edges.
- Make interactivity discoverable but quiet (a single tooltip pill, hover-revealed dock icons).

**Don't**
- Don't add a conventional website header, nav links, hero headline, or footer — they break the desktop metaphor.
- Don't use large filled CTA buttons; the CTA is a calendar widget, not a button.
- Don't introduce drop shadows, gradients on cards, or bright card backgrounds — surfaces stay flat, dark, translucent.
- Don't spread saturated color across text or borders; accents beyond the red-orange belong only to app-icon artwork.
- Don't crowd the desktop with widgets on both sides; the right edge holds only small file icons.
