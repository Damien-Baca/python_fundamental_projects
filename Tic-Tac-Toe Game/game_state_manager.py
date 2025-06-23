from sys import exit
import pygame
from pygame.locals import QUIT

from menu import Menu
from single_player import SinglePlayer
from multi_player import MultiPlayer

FPS = 60
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

INITIAL_STATE = 'menu'

MAIN_MENU_STATE = 'menu'
SINGLE_PLAYER_STATE = 'singlePlayer'
MULTI_PLAYER_STATE = 'multiplayer'
STATES = {
    MAIN_MENU_STATE: Menu(),
    SINGLE_PLAYER_STATE: SinglePlayer(),
    MULTI_PLAYER_STATE: MultiPlayer()
}


class GameStateManager:
    def __init__(self):
        pygame.init()
        self.done = False
        self.state = STATES[INITIAL_STATE]
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        pygame.display.set_caption("Tic Tac Toe")

    def update_gamestate(self):
        pass

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
        self.state.event_loop()

    def update(self, dt):
        if self.state.done:
            self.update_gamestate()
        if self.state.quit:
            self.done = True
        self.state.update(self.screen, dt)

    def game_loop(self):
        while not self.done:
            dt = self.clock.tick(FPS) / 1000.0  # frame time
            self.event_loop()
            self.update(dt)
            pygame.display.update()
