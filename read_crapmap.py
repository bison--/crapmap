import struct


def read_crapmap(filename):
    with open(filename, 'rb') as f:
        # Read and check magic bytes
        magic = f.read(4)
        if magic != b'CRAP':
            raise ValueError(f"Invalid magic bytes: {magic}")

        # Read version
        version = f.read(1)[0]
        if version != 0x01:
            raise ValueError(f"Invalid version: {version}")

        # Read width and height
        width = f.read(1)[0]
        height = f.read(1)[0]

        # Read colors (if present)
        colors_byte = f.read(1)
        color_table = []

        if colors_byte:
            num_colors = colors_byte[0]
            for _ in range(num_colors):
                color = struct.unpack('BBB', f.read(3))
                color_table.append(color)

        # Read pixel data
        pixel_data = [list(struct.unpack('B' * width, f.read(width))) for _ in range(height)]

        # Convert pixel indices to RGB values
        image_data = []
        for row in pixel_data:
            image_row = []
            for pixel in row:
                if pixel == 0x00:  # Transparent
                    image_row.append((255, 255, 255, 0))
                elif 0 < pixel <= len(color_table):  # Adjust index to match Python's 0-based list indexing
                    image_row.append((*color_table[pixel - 1], 255))
                else:
                    image_row.append((0, 0, 0, 255))  # Undefined color (black for now)
            image_data.append(image_row)

    return image_data
