# DXF Sketch Companion Tool

![version](https://img.shields.io/badge/version-2.9.0-0696d7)

Measure rooms on site with a laser meter, type the readings in on the iPad step by step, and open the result in AutoCAD:
a DXF (AutoCAD 2018 format, millimetres, 1:1) on your layers, with hatched walls, real dimensions in your
`STYLE[inch]` dimension style, the Area label block, doors and windows, pillars and shafts, sockets, water and
drain points, and furniture as your own blocks.

**Open on the iPad:** https://dtheofilopoulos.github.io/DXF-Sketch/
then Share › Add to Home Screen. After the first visit it works with no signal and keeps everything on the iPad.

## What it does

| Step | What you do |
|---|---|
| 1 Room | Name (English, Greek), Room#, room height, wall thickness and fill |
| 2 Walls | Sketch with Apple Pencil, start from a rectangle or an L, or walk the room wall by wall. Tap any length or corner angle to change it; rooms always stay closed |
| 3 Openings | Doors, windows and passages: tap the wall, drag to place, tap a distance to set it |
| 4 Pillars & shafts | Anywhere in the room; they snap to walls, corners and each other |
| 5 Sockets & water | Socket 1P, 1P UPS, 3P UPS, RJ45, water and drain, exported as your blocks |
| 6 Furniture | Benches at any size, cabinets, drawers, sinks, PCs, printers, chairs and named equipment |
| 7 Export | DXF, a printable site report (plan, room schedule, notes, photos), a plan picture and a room schedule (CSV) |

Also:

- **Units** in Settings: metric (whole millimetres, m²) by default, or feet and inches.
- **Photos and notes** per room, kept on the device and carried in the project file and site report.
- Light and dark themes, undo and redo, several projects per device, screen stays on while you work.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app, including the DXF template with your blocks and dimension style |
| `sw.js` | Offline cache: its `VERSION` must match `APP_VERSION` in `index.html` |
| `manifest.webmanifest`, `icons/` | Home-screen app |
| `laptop/DXF-Sketch.py` + `laptop/DXF-Sketch.html` | Optional laptop helper: serves the app on the local network and saves DXFs straight into a `Sketches` folder (`python DXF-Sketch.py`, opens http://dxf-sketch.localhost:8125) |
| `VERSION`, `CHANGELOG.md` | Release number and history |

## Releasing a new version

1. Change the version in `VERSION`, `index.html` (`APP_VERSION`), `sw.js` (`VERSION`) and `laptop/DXF-Sketch.py` (`VERSION`).
2. Copy the same page to `laptop/DXF-Sketch.html`.
3. Add a section for the new version at the top of `CHANGELOG.md`.
4. Commit and push. GitHub Pages publishes the app within a minute (iPads offer *Reload to update* in Settings), and the Release workflow publishes a GitHub Release with the notes and two zips.

Author: Dionysios Theofilopoulos · d.theofilopoulos@gmail.com

Sora font: SIL Open Font License 1.1.
