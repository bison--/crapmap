import pygame

from read_crapmap import read_crapmap


def visualize_crapmap(filename):
    # Initialize pygame
    pygame.init()

    # Set the FPS
    clock = pygame.time.Clock()

    # Read the image data from the .crapmap file
    image_data = read_crapmap(filename)

    # Get the dimensions of the image
    height = len(image_data)
    width = len(image_data[0]) if height > 0 else 0

    # Create a window of the size of the image
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('Crapmap Viewer')

    # Translate the image data to a pygame surface
    original_surface = pygame.Surface((width, height))
    for y, row in enumerate(image_data):
        for x, (r, g, b, a) in enumerate(row):
            original_surface.set_at((x, y), (r, g, b, a))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Scale the surface to fit the window size
        scaled_surface = pygame.transform.scale(original_surface, screen.get_size())

        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


# Call the function with the .crapmap file path
# visualize_crapmap('path_to_your_crapmap_file.crapmap')


if __name__ == '__main__':
    visualize_crapmap('data/sample.crapmap')
