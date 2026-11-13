# Changelog

## 2.11.0 — 13 Nov 2026
- 2D / 3D: the switch at the top of the zoom buttons shows the laboratory as a 3D model, with doors, windows, pillars, benches, furniture and service points. Drag to turn it, pinch or scroll to zoom, two fingers to move. The walls nearest to you are cut down so you can see in.
- North: the round arrow under the zoom buttons. Tap it and choose Set from the compass (hold the iPad flat with the plan lined up with the room), or drag the arrow to set it by hand. Turn the plan so north is up in one tap. The DXF gets a north arrow next to each laboratory where north is set; rotating the plan turns north with it.
- Clearer screen: the status bar shows only the coordinates, units and one short tip; the colour key opens from the Key button. Shorter step descriptions. Sockets & water is now Services.
- The fitted plan keeps clear of the title block and scale bar.

## 2.10.0 — 13 Nov 2026
- Laboratories and rooms: a project is the hospital, each laboratory or department (Microbiology, ER…) is its own plan, and a laboratory can hold several rooms on the same screen. Switch, add, rename or delete laboratories from the laboratory button at the top; + Room adds a room to the plan you are on. The DXF puts every laboratory side by side; the room schedule and CSV list the laboratory of each room. Existing projects open as one laboratory with their rooms in it.
- Rotate the whole plan 90° either way, from the laboratory menu or by long-pressing the canvas: every room, door, pillar, point and markup line turns with it.
- Share a link from the new share button at the top: whoever opens it gets their own copy of the whole project (photos stay on your device). If the share sheet is unavailable the link is copied.
- Point colours on screen and in the DXF: sockets yellow, RJ45 cyan, Water Supply blue, Drain red, and a new Air Supply point (orange) with your Air Tubing block. Air is counted in the room schedule.
- The Area outline is written first in the DXF, so it always sits behind walls, hatches and everything else.
- The scale bar sits under the title block, so the Lock and the selection bar are never hidden; the tool palette stays on top; the step arrows are icons only; tap a selected element again to deselect it.

## 2.9.1 — 13 Nov 2026
- Sockets, water supply and drain points go on pillars and shafts too: in Sockets & water, tap a pillar or shaft and the point sits on its nearest face, facing out into the room; drag a point near a pillar or shaft and it snaps onto it. It moves with the pillar and exports on it in the DXF.
- A point on a pillar shows its distances to both corners of that face; tap either to set it. Back to the wall on its bar puts it on the wall again.
- Lock is the first button on the bar whenever you tap a wall, pillar or shaft, and it is also in the side panel (wall editor and pillar settings). Tapping a locked pillar or shaft says so.

## 2.9.0 — 13 Nov 2026
- Lock walls, pillars and shafts once you are certain of them: Lock on the selected item's bar, or hold / right-click for the menu. Locked items show a small padlock and keep their size and position.
- Nothing can change a locked item by accident: its numbers do not open for editing, a locked pillar or shaft cannot be dragged, and any change that would move or resize it (keeping a room rectangular, closing a room, deleting) is undone with a message saying which item is locked.
- When a room closes itself after an edit, it never adjusts a locked wall; it picks other walls instead.
- Doors, windows and passages on a locked wall stay editable: tapping a segment moves or resizes them inside the wall, and the wall keeps its length.
- Pillar and shaft sizes on the drawing: the width is centred on the side facing the room and the depth on the side it measures, each turned to read along that side.

## 2.8.3 — 13 Nov 2026
- Removed the Bosch laser meter (Bluetooth) connection: the laser button, its Settings section and the shortcut in the measurement bubble are gone. Type or use the number keypad for readings.

## 2.8.2 — 13 Nov 2026
- Double doors can have unequal leaves: select the door and tap either leaf's width on the drawing, use Leaves on its bar, or type both in the panel. The two always fill the clear width between the frames.
- Each leaf swings at its own size, on screen and in the DXF, and the door's tag reads e.g. D 1600 (1000+500) when the leaves differ.

## 2.8.1 — 13 Nov 2026
- Pillars and shafts show their real, room-side size everywhere: on the selection bar, in the panel and when you tap their numbers, exactly what you measure on site. Snapping to a wall still draws them on to the outer wall line; that part is not counted in their size.
- Every pillar and shaft has its size written on it in the drawing (e.g. 400×400, Ø300), on the part that stands in the room.
- Rotate a pillar or shaft 90° from its bar (⟳ 90°) or the right-click / hold menu: width and depth swap about its centre, and one standing against a wall or in a corner stays there.

## 2.8.0 — 13 Nov 2026
- The Area outline and the room area leave out pillars and shafts: a pillar against a wall or in a corner cuts a notch into the Area polyline, one standing free becomes a separate ring, and the AREA attribute, the drawing, the room schedule and the site report all show the net floor area.
- Tool palette on the drawing: Openings, Pillars & shafts, Sockets & water and Furniture show their choices across the top of the plan (type, common sizes, every furniture item). Pick one and tap where it goes, without going through the side panel.
- One Export: the blue Export DXF button in the header is gone; export from the Export step.
- Cleaner step navigation: back and next arrows sit in the side panel's head next to the step name, and the bar at the foot of the panel is gone.
- Pinch to zoom keeps the spot between your fingers under them and follows them as they move; the page itself no longer zooms in Safari.
- Settings and About: the header stays put while the content scrolls under it, sections are grouped more clearly, and What's new shows the current version open with earlier ones folded away.
- Light theme: toggles, buttons, fields and icons have stronger edges and darker text, so they stand out from the background.
- Projects › Send a copy as a link: the project travels inside the link (photos excepted); whoever opens it gets their own copy.
- Messages appear at the foot of the drawing, clear of the palette and the title block.

## 2.7.0 — 13 Nov 2026
- Numbers-only keypad for every number field on the iPad (lengths, angles, sizes, distances), not only in the measurement bubble: digits, + and − for adding up parts, ′ and ″ in imperial, Next to move to the following field and Done. Settings › Number keypad switches it on, off or automatic.
- Editing a segment of a wall's dimension chain now changes only that segment: the openings, pillars, points and furniture after it move along, the wall-to-wall total grows or shrinks to match, and the other walls adjust so the room stays closed.
- Windows and passages can have a frame too (none unless you set one); doors keep 50 mm unless changed. Frame is on every opening's bar and in the panel.
- Pillars and shafts that run into a wall show and take their size to the outer wall line, so the numbers match what is drawn and exported.
- Bench cabinets, drawers and everything on a bench snap to every edge of the bench: its ends, its back and its front.
- Tap to edit whatever is selected: a piece of furniture shows its distances to both corners, its distance off the wall and its width and depth on the drawing; a pillar shows its width and depth. Tap any number to change it.
- Whatever you place by tapping (opening, pillar, socket or point) is selected straight away, ready to adjust.

## 2.6.0 — 13 Nov 2026
- Walls with doors, windows or passages now show a chain of segment dimensions: corner → door, door width, door → window, window width, … → corner. Tap any segment to change it: a gap moves the next opening, a width resizes that opening, the last gap moves the last opening. Save → jumps to the next segment.
- The wall-to-wall dimension stays as a second row further out, on the drawing and in the DXF; overall room dimensions move one row further still.
- In the DXF the chain and the wall-to-wall row are real dimensions in your STYLE[inch], like the Kavala drawing.
- Door frame: every door has a frame on each side, 50 mm unless you change it. Set it in the Door panel (with the clear width shown), with Frame on the door's bar, or by tapping the frame value next to the selected door. The jambs are drawn and exported, and the leaf and swing fill the clear width between them.
- Fixed: switching between door, window and passage before placing one no longer carries the previous width over.

## 2.5.2 — 13 Nov 2026
- New rooms are called Laboratory 1, Laboratory 2 and so on, and the header button reads + Laboratory.
- In projects you already have, rooms still carrying the old default name (Room 1, Room 2…) become Laboratory 1, Laboratory 2…; names you typed yourself are left alone.

## 2.5.1 — 13 Nov 2026
- Buttons follow the Shui pattern: pill-shaped, with the primary action filled in the app's blue and secondary actions as flat grey pills without an outline.
- Form fields are filled grey with a thin underline that turns blue while you type, instead of outlined boxes.
- Cards, lists, folding sections and summary tiles are flat with small corners on the panel background.
- Colours are unchanged in both themes, and nothing carries third-party branding.

## 2.5.0 — 13 Nov 2026
- New layout: a flat application bar on top, the seven steps as a navigation bar of tabs under it (the active step underlined), the side panel and the drawing flush against each other with thin separators, and a status bar at the bottom with coordinates, legend, grid and units. The floating step dock is gone, so the drawing has more room.
- Squarer, flatter controls throughout: buttons, toggles, fields, cards, menus and sheets share the same small corner radius. Colours are unchanged, in both the dark and the light theme.
- Proper SVG icons everywhere instead of text symbols: rotate, turn round, mirror, duplicate, delete, edit, split, turn left and right, shapes, arrows and the right-click menus.
- Messages appear over the drawing, clear of the bars and the title block.
- Selecting a piece of furniture, a door or a pillar brings its settings to the top of the side panel.
- README brought up to date with everything the app does.

## 2.4.1 — 13 Nov 2026
- Lengths are whole millimetres everywhere: typing, the drawing, the panel, the laser and the DXF (e.g. 5994, not 5994.4).
- Slimmer buttons and pills throughout: less padding, smaller header icons and step dock, so more fits on screen.
- Fixed: the blue glow under selected buttons and room tabs was cut off at the edges of the panel and header. Selected items are now flat blue with a crisp edge.
- Export step: Export DXF is a full-width button with Site report, Plan picture and Room schedule (CSV) neatly below it; the summary tiles no longer wrap or cut off.

## 2.4.0 — 13 Nov 2026
- New step 6, Furniture: benches at any length and depth (presets, or one tap for a bench along a whole wall), bench cabinets and drawers, wall cabinets, sinks, PCs, printers, sample racks, centrifuges, office chairs and stools, biohazard bins, and named equipment (fridge, freezer −80 °C, fume hood, biosafety cabinet, analyzer, water system, or your own name and size). Export is now step 7.
- Pick an item and tap where it goes: against a wall, on the floor or on top of a bench. Keep tapping to add more. Items stand with their back to the nearest wall, snap into corners and line up end to end with their neighbour; chairs and stools go in front of the bench.
- Tap an item to select it: rotate 90°, turn it round, duplicate it next to itself, delete it, or set its size and its distances from the corner and the wall. Drag to move it; hold or right-click for the same menu.
- In the DXF they arrive as your own blocks from the Kavala drawing (Bench Cabinet, Bench Drawer, Wall Cabinet, Sink, PC, Printer, Office Chair, Office Stool, Rack Samples, Centrifuge (M), Bin (Biohazard)) on the Room layer. Benches become one block per size (e.g. Bench 1800x700) on the Benches layer; equipment is an outline with its name on Laboratory Equipment.
- Room schedule and site report list the furniture and equipment in each room, with the total bench length.
- Lengths shown while dragging follow the Units setting.

## 2.3.0 — 13 Nov 2026
- Photos per room: in Notes, Add photo opens the iPad camera (or pick from Photos). Photos are kept on the device, tagged with the selected wall, and travel in the project file and the site report.
- Site report (Export step): one HTML page with the plan, a room schedule (area, perimeter, height, volume, doors, windows, sockets, UPS, RJ45, water, drain), project and room notes, wall lengths and photos. Open it and print to PDF, or send it as is.
- Room schedule (CSV) for Excel: one row per room with the same figures, in your units.
- Export step shows total floor area, rooms closed and volume at a glance.
- Walking a room: a prompt on the drawing shows the next wall, the turn at its corner and the gap back to corner A; with the laser connected, each measurement fills the wall and moves on.
- The screen stays on while you work (Settings › Screen), so the iPad does not lock between measurements.
- The laser reading popup sits lower, clear of the title block.

## 2.2.0 — 13 Nov 2026
- Wall dimensions in the DXF are now real AutoCAD dimensions on the Room Dimensions layer, in your STYLE[inch] dimension style (mm with inches in brackets, e.g. 5830 [229,5"], 70 closed arrows, 50 text), 500 mm outside the wall like your drawings. Rooms that are not a plain rectangle also get overall length and width one row further out.
- Text in the DXF defaults to 50 (was 100), matching your dimension text.
- Units in Settings: Metric (mm, m²) by default, or Imperial (feet and inches, ft²). Type 12'6", 12'-6 1/2" or 150"; sums work too. Drawings are still stored and exported 1:1 in millimetres.
- The drawing shows wall lengths as dimension lines outside the walls, as in AutoCAD, with smaller lettering.
- Bosch laser meter: the new laser button connects a GLM 50 C / 100 C over Bluetooth. Press measure on the meter and the value goes into the measurement bubble, the length field you are in, or the next wall when you walk a room. Works in Chrome (Windows, Android) and in the Bluefy browser on iPad; Safari cannot use Bluetooth, and Settings explains what to do.
- The DXF header now names an existing dimension style (it pointed to ISO-25, which was not in the file).

## 2.1.0 — 13 Nov 2026
- Right-click (or hold a finger on the iPad) anything on the drawing for a menu of what you can do with it:
  - a wall: change its length or corner angle; add a door, window, passage, pillar or socket right where you pressed; split it, insert a wall after it, or delete it;
  - a door or window: double, opens out, flip the hinge, make it a door/window/passage, centre it on the wall, duplicate, delete;
  - a pillar or shaft: round, pillar ⇄ shaft, against the wall, centre on the wall, duplicate, delete; a socket or water point: duplicate, delete;
  - inside a room: add a pillar or shaft there, zoom to the room, rename, duplicate, rotate, mirror, delete; empty space: fit, zoom, add a room, markup pen, share picture, export DXF.
- Double-tap or double-click: a door flips between opening in and out; a wall opens its length in the Walls step (from any step, without adding anything); inside a room zooms to that room; empty space fits the whole plan; a window, pillar or point opens its menu.
- Keyboard: Delete removes the selected door, window, pillar or point; Esc deselects or closes the menu; arrow keys move through the menu.

## 2.0.1 — 13 Nov 2026
- Room Height is now an attribute of the room block (tag HEIGHT, e.g. "H = 2.70 m") next to the Greek and English names, Room# and area, instead of separate text. It follows the block when you move it in AutoCAD and can be edited with the other attributes.

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
