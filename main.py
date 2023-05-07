import pygame
from game import Game

pygame.init()

# Set up the game window
window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("2D Platformer")

# Create a game instance
game = Game(window)

# Run the game loop
game.run()

pygame.quit()
