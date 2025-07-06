import pygame as pyg

from components.error import log_error
from components import colors, utils
from components.button import TextButton
from gamestates import \
    VictoryState, MenuState, MultiPlayerState, MultiPlayerChoiceState


class Victory(object):
    def __init__(self) -> None:
        self.next = None
        self.done = False
        self.quit = False

        self.current = VictoryState
        self.previous = None
        self.backgroundColor = colors.WHITE
        self.buttons = []
        self.returnData = {}
        self.winnerText = ""

    def startup(self, data={}):
        self.next = None
        self.done = False
        self.quit = False
        if "winnerText" not in data and "p1Piece" not in data:
            log_error("Invalid data supplied to victory state")
            quit()
        self.winnerText = data["winnerText"]
        buttonFont = pyg.font.SysFont("Arial", 30)
        continueArgs = [
            250, 200, 250, 100, self.continue_game, colors.DEFAULT_BUTTON,
            colors.BLACK, "Continue Game", buttonFont
        ]
        self.buttons.append(TextButton(*continueArgs))

        resetArgs = [
            250, 325, 250, 100, self.reset_game, colors.DEFAULT_BUTTON,
            colors.BLACK, "Restart Game", buttonFont
        ]
        self.buttons.append(TextButton(*resetArgs))

    def cleanup(self):
        return self.returnData

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        titleText = f"{self.winnerText}"
        titleFont = pyg.font.SysFont("Arial", 50)
        surf, rect = utils.create_text(titleText, titleFont, 250, 75)
        screen.blit(surf, rect)
        for button in self.buttons:
            button.process(screen)

    def continue_game(self):
        self.returnData["continue"] = True
        self.next = MultiPlayerState
        self.done = True
        pass

    def reset_game(self):
        self.next = MultiPlayerChoiceState
        self.done = True
        pass

    def to_main_menu(self):
        self.next = MenuState
        self.done = True
        pass
