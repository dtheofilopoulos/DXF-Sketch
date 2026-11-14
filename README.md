# DXF Sketch Companion Tool

![version](https://img.shields.io/badge/version-1.1.0-0696d7)

Measure rooms on site with a laser meter, type the readings in on a tablet, phone or computer step by step, and open the result in AutoCAD:
a DXF (AutoCAD 2018 format, millimetres, 1:1) on your layers, with hatched walls, real dimensions in your
`STYLE[inch]` dimension style, the Area label block, doors and windows, pillars and shafts, services (electrical and network
outlets, water, drain and air) and furniture and equipment as your own blocks. The plan's bottom-left corner sits on 0,0,0.

**Open on any device:** https://dtheofilopoulos.github.io/DXF-Sketch/
then add it to the Home Screen (Safari: Share › Add to Home Screen; Chrome: Install app). After the first visit it works with no signal and keeps everything on that device.

## What it does

| Step | What you do |
|---|---|
| 1 Room | Name (and in another language if you like), Room#, room height, wall thickness and fill |
| 2 Walls | Sketch with Apple Pencil, start from a rectangle or an L, or walk the room wall by wall. Tap any length or corner angle to change it; rooms always stay closed |
| 3 Openings | Doors, windows and passages: tap the wall, drag to place, tap a distance to set it |
| 4 Pillars & shafts | Anywhere in the room; they snap to walls, corners and each other |
| 5 Services | Electrical outlets 1P, 1P UPS and 3P UPS, network outlets (RJ45), water supply, drain and air supply: tap the wall, a pillar or a shaft. Exported as your blocks on layer Room, each in its own colour (electrical outlets yellow, network outlets cyan, water blue, drain red, air orange) |
| 6 Furniture | Benches at any size, bench cabinets, bench drawers, wall cabinets, chairs, stools, bins. On layer Room in colour 125 |
| 7 Equipment | PCs, printers, sinks, racks, centrifuges, reverse osmosis and named equipment. On layer Room in colour 125 |
| 8 Export | DXF, a printable site report (plan, room schedule, notes, photos), a plan picture and a room schedule (CSV) |

Also:

- **New, Open, Save, Save as** buttons in the header (a File menu on phones, also with open a project file, save to a file and recent projects); ⌘/Ctrl+S, ⌘/Ctrl+Shift+S, ⌘/Ctrl+O.
- **Units** in Settings: metric (whole millimetres, m²) by default, or feet and inches.
- **Share** (header): send by email a link that always opens the latest version, either a person's own link or one for anyone; see who you shared with and who has it open now (green dot). Kept in secret GitHub Gists; needs a GitHub token with the gist scope in Settings › Live links.
- **Backups** to a private GitHub Gist as you work, a storage meter in Settings, and **Plan to scale** (1:50 on A4/A3) for printing or PDF.
- **Photos and notes** per room, kept on the device and carried in the project file and site report.
- Light and dark themes, undo and redo, several projects per device, screen stays on while you work.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app, including the DXF template with your blocks and dimension style |
| `sw.js` | Offline cache: its `VERSION` must match `APP_VERSION` in `index.html` |
| `manifest.webmanifest`, `icons/` | Home-screen app |
| `laptop/DXF-Sketch.py` + `laptop/DXF-Sketch.html` | Optional laptop helper: serves the app on the local network and saves DXFs straight into a `Sketches` folder (`python DXF-Sketch.py`, opens http://dxf-sketch.localhost:8125) |
| `VERSION`, `CHANGELOG.md` | Release number and history (important changes only) |
| `tests/smoke.py` | Automatic checks run before every release: the app opens, every step and 3D draw, the DXF is valid (`pip install playwright ezdxf`, `python -m playwright install chromium`, `python tests/smoke.py`) |

## Releasing a new version

1. Change the version in `VERSION`, `index.html` (`APP_VERSION`), `sw.js` (`VERSION`) and `laptop/DXF-Sketch.py` (`VERSION`).
2. Copy the same page to `laptop/DXF-Sketch.html`.
3. Add a section for the new version at the top of `CHANGELOG.md`.
4. Commit and push. GitHub Pages publishes the app within a minute (open apps show a dot on About; About › Check for updates installs it), and the Release workflow publishes a GitHub Release with the notes and two zips.

Author: Dionysios Theofilopoulos · d.theofilopoulos@gmail.com

Sora font: SIL Open Font License 1.1.

## License

Copyright © 2026 Dionysios Theofilopoulos. All rights reserved. You may use the published app and freely use everything you
make with it; copying, changing or redistributing the code, the AutoCAD blocks or the template needs permission.
See [LICENSE](LICENSE).
