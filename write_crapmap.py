import struct


def write_crapmap(filename, image_data, color_table=None):
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
                    pixel_row.append(0xFF)
                elif color_table and pixel[:3] in color_table:
                    pixel_row.append(color_table.index(pixel[:3]))
                else:
                    pixel_row.append(0x01)  # Undefined color index
            f.write(bytes(pixel_row))

# We'll test this function once we have a sample image data and color table.
