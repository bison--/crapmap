import struct


def write_crapmap(filename, image_data, color_table=None):
    # Check if the number of colors (excluding transparency) is within the allowed range
    if color_table and len(color_table) > 255:  # Excluding 0x00 for transparency
        raise ValueError(
            "Number of colors exceeds the maximum supported by crapmap (maximum 255 excluding transparency).")

    with open(filename, 'wb') as f:
        # Write magic bytes and version
        f.write(b'CRAP')
        f.write(struct.pack('B', 0x01))

        # Get and write dimensions
        height = len(image_data)
        width = len(image_data[0]) if height > 0 else 0
        f.write(struct.pack('B', width))
        f.write(struct.pack('B', height))

        # Write color table if provided
        if color_table:
            f.write(struct.pack('B', len(color_table)))
            for color in color_table:
                f.write(struct.pack('BBB', *color))

        # Write pixel data
        for row in image_data:
            pixel_row = []
            for pixel in row:
                if pixel[3] == 0:  # Alpha is 0, so it's transparent
                    pixel_row.append(0x00)
                elif color_table and pixel[:3] in color_table:
                    pixel_index = color_table.index(pixel[:3]) + 1  # Adjust index to match .crapmap format
                    pixel_row.append(pixel_index)
                else:
                    pixel_row.append(0x01)  # Undefined color index
            f.write(bytes(pixel_row))
