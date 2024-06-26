from uno import run_game
import pygame
import random

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])
# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    # Draw a solid blue circle in the center
    pygame.draw.rect(screen, color, pygame.Rect(5, 20, 100, 300))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(395, 20, 100, 300))
    # Flip the display
    pygame.display.flip()
    clock.tick(2)

# Done! Time to quit.
pygame.quit()

