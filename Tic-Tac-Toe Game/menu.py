import pygame as pyg

from components import utils, colors
from components.button import TextButton
from gamestates import MenuState, MultiPlayerChoiceState


class Menu(object):
    def __init__(self):
        self.next = None
        self.done = False
        self.quit = False

        self.current = MenuState
        self.previous = None
        self.backgroundColor = colors.WHITE
        self.buttons = []

    def startup(self, data=None):
        self.next = None
        self.done = False
        buttonFont = pyg.font.SysFont("Arial", 30)
        # singlePlayerArgs = [
        #     250, 200, 200, 100, self.to_singleplayer, colors.DEFAULT_BUTTON,
        #     colors.BLACK, 'SinglePlayer', buttonFont
        # ]
        # self.buttons.append(TextButton(*singlePlayerArgs))
        multiPlayerArgs = [
            250, 325, 200, 100, self.to_multiplayer, colors.DEFAULT_BUTTON,
            colors.BLACK, 'MultiPlayer', buttonFont
        ]
        self.buttons.append(TextButton(*multiPlayerArgs))

    def cleanup(self):
        pass

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        titleText = "Tic-Tac-Toe"
        titleFont = pyg.font.SysFont("Arial", 75)
        surf, rect = utils.create_text(titleText, titleFont, 250, 75)
        screen.blit(surf, rect)
        for button in self.buttons:
            button.process(screen)

    # def to_singleplayer(self):
    #     self.next = SPC.state
    #     self.done = True
    #     pass

    def to_multiplayer(self):
        self.next = MultiPlayerChoiceState
        self.done = True
        pass
