# KiCAD Parts

This repository contains kicad parts for KiCAD V6+

They are designed to augment the standard KiCAD parts rather than replace so some parts in here will reference 3D models from the main KiCAD distribution as necessary.

To get started, clone this repository and set a new variable in KiCAD called `KICAD_BJS_KICAD_PARTS` which has the base directory of this repository as it's value.

## Scripting

Some of the parts are produced via scripts because otherwise it's too repetitive to make the parts in the UI. For example, connectors within the footprints are often scripted. The scripts are designed to be run via Python 3. See the separate documentation for each scripted part.

## Footprints

See the separate [documentation for the footprints](footprints/readme.md).
