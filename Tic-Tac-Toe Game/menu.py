# Third party imports
import pygame as pyg
# Local imports
from components import utils, colors
from components.button import TextButton
from singleplayer import SinglePlayerChoice as SPC


class Menu(object):
    state = 'Main Menu'

    def __init__(self):
        self.current = self.state
        self.previous = None
        self.next = None
        self.done = False
        self.quit = False
        self.buttons = []
        self.backgroundColor = colors.WHITE

    def startup(self, data=None):
        # Title
        titleText = "Tic-Tac-Toe"
        titleFont = pyg.font.SysFont("Arial", 75)
        self.titleArgs = [titleText, titleFont, 250, 75]
        # Gamemode buttons
        buttonFont = pyg.font.SysFont("Arial", 30)
        singlePlayerArgs = [
            250, 200, 200, 100, self.to_singleplayer,
            colors.DEFAULT_BUTTON, 'SinglePlayer', buttonFont
        ]
        self.buttons.append(TextButton(*singlePlayerArgs))
        # args = [
        #     250, 325, 200, 100, self.to_multiplayer,
        #     colors.DEFAULT_BUTTON, 'MultiPlayer', buttonFont
        # ]
        # self.buttons.append(TextButton(*args))

    def cleanup(self):
        pass

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)

        surf, rect = utils.create_text(*self.titleArgs)
        screen.blit(surf, rect)

        for button in self.buttons:
            button.process(screen)

    def to_singleplayer(self):
        self.next = SPC.state
        self.done = True
        pass

    # def to_multiplayer(self):
    #     pass
