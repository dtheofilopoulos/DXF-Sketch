# Changelog

Important changes only; smaller ones are listed as general bug fixes.

## 1.2.1 — 14 Nov 2026
- Site survey as a PDF: plan, room schedule, each room with its services, needs, checklist, notes and photos, page-numbered on A4. Names in any language print correctly.
- Export fits its panel: the buttons wrap onto two columns, with no sideways scrolling.

## 1.2.0 — 14 Nov 2026
- Floors: a hospital has floors, each with its laboratories (the floor button next to Laboratory). The DXF puts each floor in a row of its own, named, one above the other.
- Wall elevations: any wall seen from inside the room, with doors, windows, pillars, furniture, equipment and services at their heights and a chain of dimensions; print or save it as PDF.
- Heights: services have a height above the floor (shown in 3D, elevations and the survey), windows a sill and height, and rooms an optional false ceiling.
- Equipment needs: PCs, printers, sinks, centrifuges, reverse osmosis and the named equipment know which outlets, network points, water and drains they need. Equipment and Services say what is still missing.
- Templates: save a room's furniture, equipment and services and drop them into another room in one tap.
- Open an existing DXF as a faint underlay to trace over (File menu or the laboratory menu). It is not exported.
- Compare with an earlier visit: room by room, what changed in area, walls, openings, services and furniture.
- Site checklist per room (measured, photographed, services counted, signed off), shown in the room list and the site survey. The site report is now called the site survey.
- General bug fixes.

## 1.1.0 — 14 Nov 2026
- Backups: with a GitHub token, every project is backed up as you work into a private Gist on your account (photos stay on the device). Projects shows when each was last backed up, and Settings can back up everything at once or restore a project from the backup.
- Storage in Settings: how much room your projects and photos take on this device, with a warning before it fills up.
- Plan to scale (Export): the plan at 1:50 on A4 or A3, or 1:100 if it will not fit, with a title block and scale bar, ready to print or save as PDF.
- Every release is now checked automatically first: the app opens on tablet, portrait and phone sizes, every step and 3D draw, and the DXF is checked for errors, layers, colours and the 0,0 origin.
- General bug fixes.

## 1.0.1 — 14 Nov 2026
- Tap a room's name on the plan to open its details; tap it again to close them and go back to what you were doing. A second tap on anything selected (a wall, door, pillar, outlet or piece of furniture) lets it go.
- Devices still on the old 3.x versions now update to this version by themselves.
- General bug fixes.

## 1.0.0 — 14 Nov 2026
First release.

- Laboratories and rooms: several laboratories per hospital, each with its rooms; rooms can sit next door to each other and share walls. Each room has a name (and one in another language), Room#, height, wall thickness and fill.
- Walls: sketch with Apple Pencil or a finger, start from a rectangle or an L, or walk the room wall by wall with the laser meter. Tap any length or angle to change it; rooms always stay closed.
- Openings, pillars and shafts: doors (single or double, with unequal leaves), windows and passages; pillars and shafts that snap to walls, corners and each other. The floor area leaves them out.
- Services: electrical outlets (1P, 1P UPS, 3P UPS), network outlets (RJ45), water, drain and air, on walls, pillars or shafts.
- Furniture and equipment as your own AutoCAD blocks: benches at any size, cabinets, drawers, chairs, PCs, sinks, printers, centrifuges, reverse osmosis and named equipment. Items on a bench line up with each other, and a selected item shows only the gaps to its neighbours.
- DXF for AutoCAD 2018, millimetres 1:1: your layers, hatched walls, dimensions in your STYLE[inch] style, the Area label, doors, windows, services in their own colours and furniture and equipment in colour 125, all starting from 0,0,0, with a north arrow.
- 3D view with low, cut-away or full-height walls.
- North from the compass along the first wall, or by hand; one tap squares the laboratory up and turns it landscape or portrait.
- Sharing: a short live link that always opens the latest version, sent by email to one person or to anyone, with a green dot for who has it open; or a frozen copy inside a link.
- Files and reports: New, Open, Save and Save as; project files; a printable site report, a plan picture and a room schedule (CSV); photos and notes per room.
- Works offline on any device once added to the Home Screen; light and dark themes; metric or feet and inches; undo and redo; updates from About.
