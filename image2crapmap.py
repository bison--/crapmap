from PIL import Image
from write_crapmap import write_crapmap


def image_to_crapmap(image_path, output_path):
    # Open the image using PIL
    img = Image.open(image_path)
    width, height = img.size

    # Check if the image dimensions are within the allowed range (0x01 to 0xFF)
    if width > 255 or height > 255:
        raise ValueError("Image dimensions exceed the maximum supported by crapmap (255x255).")

    # Convert image to RGBA to ensure we handle images with and without alpha channels
    img = img.convert("RGBA")

    # Extract unique colors and check if they are within the allowed range
    unique_colors = list(set(img.getdata()))
    if len(unique_colors) > 256:  # 0x00 to 0xFF inclusive
        raise ValueError("Image has more colors than supported by crapmap (maximum 256 including transparency).")

    # Convert image data for crapmap
    # This format will be a list of rows, where each row is a list of RGBA tuples
    image_data = list(img.getdata())
    image_rows = [image_data[n:n+width] for n in range(0, len(image_data), width)]

    # Convert the unique colors to RGB (excluding the alpha)
    color_table = [color[:3] for color in unique_colors if color[3] != 0]  # Exclude fully transparent colors

    # Write to the crapmap format
    write_crapmap(output_path, image_rows, color_table)


if __name__ == "__main__":
    # This allows the script to be executed directly, but you can also use the function in other scripts
    input_image_path = input("Enter the path to the image: ").strip()
    output_crapmap_path = input("Enter the desired output path (with .crapmap extension): ").strip()

    try:
        image_to_crapmap(input_image_path, output_crapmap_path)
        print(f"Image converted successfully to {output_crapmap_path}")
    except ValueError as e:
        print(f"Error: {e}")
