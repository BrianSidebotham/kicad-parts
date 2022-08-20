from KicadModTree import *
import os

def generate_footprint_name(nickname: str, orientation: str,manufacturer: str, pin_count: int, part_name: str):
    return f"{manufacturer}_{nickname}_{orientation}_{pin_count}_{part_name}"

def generate_part_name(connector_series: str, pin_count: int):
    prefix = "" if int(pin_count / 10) == 0 else f"{int(pin_count / 10)}-"
    suffix = f"-{pin_count - (10 * int(pin_count / 10))}"
    return f"{prefix}{connector_series}{suffix}"

output_directory="."
pin_counts = range(2, 24, 2)
manufacturer = "te-connectivity"
orientation = "vertical"
connector_series = "1586768"
connector_nickname = "val-u-lok"
pin_pitch_x = 4.2
pin_pitch_y = 5.5
drill_size = 1.4
pad_size = (2.5, 3.5)

# init kicad footprint
for pin_count in pin_counts:
    part_name = generate_part_name(connector_series, pin_count)
    footprint_name = generate_footprint_name(nickname=connector_nickname,
                                             manufacturer=manufacturer,
                                             orientation=orientation,
                                             part_name=part_name,
                                             pin_count=pin_count)

    kicad_mod = Footprint(footprint_name)
    kicad_mod.setDescription(f"{manufacturer} {connector_series} series {pin_count} pin connector")
    kicad_mod.setTags(manufacturer)

    # set general values
    kicad_mod.append(Text(type='reference', text='REF**', at=[0, -7], layer='F.SilkS'))
    kicad_mod.append(Text(type='value', text=part_name, at=[0, 2], layer='F.Fab'))

    # We use bounding boxes for the pins (without and pad/copper adjustment) and the physical body size
    pin_bounds = ( (((pin_count / 2) - 1) * pin_pitch_x ), pin_pitch_y)
    bodysize = ( (((pin_count / 2) - 1) * pin_pitch_x ) + 5.4, 9.75)

    # create silscreen bounding box and fab layer box
    kicad_mod.append(RectLine(start=[-bodysize[0] / 2, -bodysize[1] / 2],
                              end=[bodysize[0] / 2, bodysize[1] / 2],
                              layer='F.SilkS'))

    # create courtyard
    kicad_mod.append(RectLine(start=[-bodysize[0] / 2, -bodysize[1] / 2],
                              end=[bodysize[0] / 2, bodysize[1] / 2],
                              layer='F.CrtYd'))

    kicad_mod.append(RectLine(start=[-bodysize[0] / 2, -bodysize[1] / 2],
                              end=[bodysize[0] / 2, bodysize[1] / 2],
                              layer='F.Fab'))

    px = -pin_bounds[0] / 2
    py = -pin_pitch_y / 2

    # Create a position indicator for pin number 1 in this connector series
    kicad_mod.append(RectLine(start=[(-bodysize[0] / 2) - 0.5, py + 0.5],
                              end=[(-bodysize[0] / 2), py - 0.5],
                              layer='F.SilkS'))

    # Create a latch indicator for the mating part
    kicad_mod.append(RectLine(start=[-1.0, bodysize[1] / 2],
                              end=[1.0, (bodysize[1] / 2) + 1.0],
                              layer='F.SilkS'))

    # We will be numbering the pins in the two dimension like so:
    #
    # +--------------
    # | 1 | 3 | 5 ...
    # +--------------
    # | 2 | 4 | 6 ...
    # +--------------
    #
    for pin in range(int(pin_count / 2)):
        # create pads
        kicad_mod.append(Pad(number=(pin * 2) + 1, type=Pad.TYPE_THT, shape=Pad.SHAPE_ROUNDRECT,
                        at=[px, py], size=pad_size, drill=drill_size, layers=Pad.LAYERS_THT))

        kicad_mod.append(Pad(number=(pin * 2) + 2, type=Pad.TYPE_THT, shape=Pad.SHAPE_ROUNDRECT,
                        at=[px, py + pin_pitch_y], size=pad_size, drill=drill_size, layers=Pad.LAYERS_THT))

        # Move to the next pin column
        px += pin_pitch_x

    # add model
    kicad_mod.append(Model(filename=f"${{KICAD_BJS_KICAD_PARTS}}/footprints/te-connectivity_val-u-lok_vertical.3dshapes/{part_name}.stp",
                       at=[0, 0, (12.8/25.4)], scale=[1, 1, 1], rotate=[0, 0, 0]))

    # output kicad model
    file_handler = KicadFileHandler(kicad_mod)
    file_handler.writeFile(os.path.join(output_directory, f'{footprint_name}.kicad_mod'))
