# Let's generate a simple 5x5 image with the following specifications:
# - Two colors: Red (255, 0, 0) and Green (0, 255, 0)
# - A pattern:
#   R G R G R
#   G R G R G
#   R G R G R
#   G R G R G
#   R G R G R

from write_crapmap import write_crapmap


def generate_sample_crapmap(sample_filename):
    # Sample 5x5 image with a checkerboard pattern of red and green pixels
    color_table = [(255, 0, 0), (0, 255, 0)]
    image_data = []

    for i in range(5):
        row = []
        for j in range(5):
            if (i+j) % 2 == 0:
                row.append((255, 0, 0, 255))  # Red with full alpha
            else:
                row.append((0, 255, 0, 255))  # Green with full alpha
        image_data.append(row)

    # Write this data to a .crapmap file
    write_crapmap(sample_filename, image_data, color_table)


sample_filename = "data/sample1.crapmap"
generate_sample_crapmap(sample_filename)
