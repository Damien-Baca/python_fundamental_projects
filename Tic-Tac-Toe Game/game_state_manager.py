# System imports
from sys import exit
# Third party imports
import pygame as pyg
from pygame.locals import QUIT
# Local imports
from menu import Menu
from singleplayer import SinglePlayerChoice as SPC, SinglePlayer as SP


class GameStateManager:
    """Game state machine responsible for switching between menu and playable modes."""
    FPS = 60
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    INITIAL_STATE = Menu.state
    # INITIAL_STATE = SPC.state

    STATES = {
        Menu.state: Menu(),
        SP.state: SP(),
        SPC.state: SPC()
    }

    def __init__(self):
        pyg.init()
        self.done = False
        self.clock = pyg.time.Clock()
        self.screen = pyg.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        self.state = self.STATES[self.INITIAL_STATE]
        self.state.startup()

        pyg.display.set_caption("Tic Tac Toe")

    def update_gamestate(self):
        """Handle switching state."""
        data = self.state.cleanup()
        self.state = self.STATES[self.state.next]
        self.state.previous, self.state.current = self.state.current, self.state.next
        self.state.startup(data)
        pass

    def event_loop(self):
        """Handle pyg events and then state events."""
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.done = True
        self.state.event_loop()

    def update(self, dt):
        """Update game data."""
        if self.state.done:
            self.update_gamestate()
        if self.state.quit:
            self.done = True
        self.state.update(self.screen, dt)

    def game_loop(self):
        """Main game loop."""
        while not self.done:
            dt = self.clock.tick(self.FPS) / 1000.0  # frame time
            self.event_loop()
            self.update(dt)
            pyg.display.update()
