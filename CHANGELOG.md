# Changelog

## 1.7.1 — 13 Nov 2026
- A graphic scale bar on the drawing shows what 500 mm, 1 m or 2 m look like; it adapts as you zoom.
- Removed the drawing-scale option: AutoCAD stays 1:1 in millimetres. Text height (100) and hatch scale (14) are fixed defaults you can change on Export.

## 1.7.0 — 13 Nov 2026
- The six steps now sit in a floating dock on the drawing: icons with a count or a tick, the current step expanded with its name. Keys 1–6 jump between steps.
- Fit leaves room for the title block and the dock, so the plan is never hidden under them.

## 1.6.0 — 13 Nov 2026
- Apple Pencil draws markup on the plan; fingers still pan and zoom. A pen button lets a finger or mouse draw too. Markup goes to the DXF on a new **Markup** layer (colour 1).
- Rooms can start as a rectangle or an L with typed sizes; a rectangle stays rectangular when you change one side.
- Tap a wall in the drawing to drop a door, window, pillar or socket where you tapped, then drag it along the wall with live distances to both corners.
- Quick turn buttons (90°, 45°, straight) and common sizes for doors, windows and pillars; number fields accept sums such as 1200+850.
- Drawing scale (1:20 to 1:200) and room height set at the start; text height and hatch size follow the scale; the room height is written under the room label.
- Projects kept on the device: save, save as copy, open, delete; one-tap room delete with Undo; **Close DXF Sketch** stops the laptop helper.
- Notes per room and for the whole project.
- Settings: where it runs, offline status and updates, export with the share sheet or as a download.
- Laptop helper restyled, lists every address the iPad can try, explains what to do when the page keeps loading, and can add the Windows Firewall rule (`--firewall`).

## 1.1.0 — 13 Nov 2026
- First github.io release: works offline on the iPad, Sora font, dark and light AutoCAD-like themes.
