import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Drawing with Transforms")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while True:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Game logic should go here

    # --- Drawing code should go here
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    # --- Draw a rectangle
    pygame.draw.rect(screen, GREEN, [300, 300, 100, 100])

    # --- Draw a triangle
    pygame.draw.polygon(screen, WHITE, [[300, 400], [400, 400], [350, 350]])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)
