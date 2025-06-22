import sys
import pygame
from pygame.locals import *

# Initialize game assets
# Initialize game window
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

DISPLAY = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAY.fill(WHITE)
pygame.display.set_caption("Tic Tac Toe")


def main():
    # Start game loop
    while True:

        # Check and process user input
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Includes controls for main menu and gameplay based on state
            # Includes option to quit playing by exiting the game loop.

            # Update game state based on game logic and user input
            # This should keep and update state information about the game like:
            # Current game state. Main Menu, Single Player, Multiplayer Mode, which players turn.
            # Checking for the victory condition

            # Draw / Render based off game state

            # Update Display
            pygame.display.update()

            # Control Framerate
            FramePerSec.tick(FPS)


main()
