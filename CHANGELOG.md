# Changelog

## 2.0.0 — 13 Nov 2026
- Pillars and shafts snap: near a wall they sit against it, near a corner they sit in the corner, and while dragging they line up with other pillars (column grids) with a red guide line and a tag saying what they snapped to.
- A pillar or shaft touching a wall runs through it to the outer wall line and the wall stops at its sides; in a corner it cuts both walls and fills the outer corner. Same in the DXF, hatches included.
- Doors, windows and points snap to the centre of their wall while you drag them, with a guide and a CENTRED tag.
- Site keypad: on the iPad the measurement bubble has its own big number pad instead of the iPad keyboard, with + and − to add up part lengths and Next → to go wall to wall. It flips below the number when there is no room above. Settings › Number keypad: Auto, Always or Off.
- Duplicate room (Room step): copies a room with all its doors, windows, pillars and points and places it beside the original, for identical labs side by side.
- Everything since 1.12: walls locked after the Walls step, tap-to-change doors and windows, pillars anywhere, Ortho 90°, tappable corner angles, rooms that always close, and reliable updates.

## 1.14.1 — 13 Nov 2026
- Fixed: tapping Update could reload the same old version. Updates now always download fresh files from GitHub, bypassing the browser's and GitHub's caches.
- If an update still does not take, the app clears its offline copy and reloads the newest version by itself; your projects stay. A message confirms the new version.

## 1.14.0 — 13 Nov 2026
- Rooms never keep a gap: change a length, an angle, insert or delete a wall in a closed room and it closes again on its own. The walls that change least are adjusted (e.g. lengthen one side and the opposite side follows), and the message names them. Undo puts them back.
- If an adjustment would distort the room, the last wall is turned and stretched to meet corner A instead.
- Walking a room wall by wall: when the end lands within 150 mm (or 2% of the perimeter) of corner A, the last wall snaps shut and the message says by how much.

## 1.13.0 — 13 Nov 2026
- Corner angles in the Walls step: every corner shows its angle on the drawing; tap it (or the ∠ buttons on a selected wall) and type any angle, e.g. 108° or 120° for polygon rooms.
- A closed room stays closed when you change an angle: two of the walls after it stretch to fit, every angle you set is kept, and the message names the walls that changed. Undo puts them back.
- The selected wall's bar shows its length and both corner angles as buttons, so a wall can be extended or angled in one tap.

## 1.12.0 — 13 Nov 2026
- Walls are locked once you leave the Walls step: in Openings, Pillars and Sockets the wall lengths can no longer be changed by a stray tap; only doors, windows and passages cut them.
- Tap a door or window to select it: a bar on the drawing switches Single/Double, opens In/Out and flips the hinge side, with Delete and Done. Changes apply at once and Undo takes them back.
- Pillars and shafts go anywhere in a room: tap the floor or sketch the outline, drag them freely, and set their distance from the nearest wall by tapping the number.
- A pillar or shaft against a wall runs through to the outer wall line; the wall hatch stops at its sides.
- Ortho 90° is on by default: sketched walls square up and a sketched room closes with square corners; typed turns go back to 90° after each wall. Turn Ortho off in Walls for angled walls.
- Closed rooms label their last wall D–A (not D–E).

## 1.11.0 — 13 Nov 2026
- Room Height defaults to 2700 mm for new projects.
- Share plan picture: a clean PNG of the whole plan (no grid or helper marks) with the hospital or laboratory name, date and a scale bar, ready for email or WhatsApp.
- Rotate a free room by 90° and mirror any closed room from the Walls step.
- Export warns when two openings overlap on a wall, or an opening starts inside a corner.
- The drawing shows the Greek room name and Room# with each room.

## 1.10.0 — 13 Nov 2026
- Sketch on the grid and it becomes the real thing: in Walls a line becomes walls (straightened, square corners snapped, closed if you end near the start; drawn away from the room it starts a new room); in Openings a line along a wall becomes a door, window or passage of that width; in Pillars an outline becomes a pillar or shaft (round if you draw a circle); in Sockets a mark becomes the point. Then tap the numbers to set exact sizes.
- Apple Pencil sketches by default; the new sketch button lets a finger or mouse do the same; the highlighter button keeps lines as markup.
- Side panel narrower and denser, and it can be hidden for a full-width drawing.
- Projects are named after the hospital or laboratory; exported files end with the date, e.g. Gen._Hosp._Kavala_20261113.dxf.
- "Room Height" used throughout.

## 1.9.0 — 13 Nov 2026
- Every step reworked to be shorter and tap-first: one line of guidance, the fields that matter on top, typed positions folded away under "Or type the position", and a list of what is already in the room.
- Room: project name and usual height in one compact line once set; names, Room#, height and walls side by side; the position of a second room folded away.
- Export: a checklist of rooms (closed or not, area, height, contents) above one Export DXF button; drawing options folded away.
- An orange **Update** button appears in the header when a newer release is on GitHub; one tap updates the app and keeps your projects.
- New About page (tap the version in the header, or Settings › About) with how it works and this changelog.
- Author shown in the About page, the laptop window and the README.

## 1.8.0 — 13 Nov 2026
- Tap any wall length on the drawing to change it in place; Enter saves and moves on to the next wall, so a whole room can be corrected without leaving the plan.
- Doors, windows, pillars and points show their distances to both corners on the drawing; tap either number to set it exactly.

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
