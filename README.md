# DXF Sketch Companion Tool

![version](https://img.shields.io/badge/version-1.10.0-0696d7)

Measure rooms on site, enter them on the iPad step by step, and export an AutoCAD DXF
(AutoCAD 2018 format, millimetres, 1:1) with your layers, hatched walls, the Area label block,
sockets, water and drain points.

**Open on the iPad:** https://dtheofilopoulos.github.io/DXF-Sketch/
then Share › Add to Home Screen. After the first visit it works with no signal and keeps
everything on the iPad.

## Files

| File | What it is |
|---|---|
| `index.html` | The whole app |
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
