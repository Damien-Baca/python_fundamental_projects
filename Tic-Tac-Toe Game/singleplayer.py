# System imports
from sys import exit
# Third party imports
import pygame as pyg
# Local imports
import components.error as error
import components.colors as colors
from components.button import TextButton
from components.typing import ButtonColors
from components.utils import \
    draw_tictactoe_board, setup_board_buttons, create_text

CHOICE_O = 'O'
CHOICE_X = 'X'


class SinglePlayerChoice(object):
    state = "Singleplayer Choice"

    def __init__(self):
        self.playPieceChoice = None
        self.current = self.state
        self.previous = None
        self.next = None
        self.done = False
        self.quit = False
        self.buttons = []
        self.backgroundColor = colors.WHITE

    def startup(self, data=None):
        # Title
        titleText = "Select you're play piece."
        titleFont = pyg.font.SysFont("Arial", 40)
        self.titleArgs = [titleText, titleFont, 250, 75]
        # Piece Selection Buttons
        pieceFont = pyg.font.SysFont("Arial", 80)
        O_args = [175, 250, 75, 75, self.select_O,
                  colors.DEFAULT_BUTTON, 'O', pieceFont]
        self.buttons.append(TextButton(*O_args))
        X_args = [325, 250, 75, 75, self.select_X,
                  colors.DEFAULT_BUTTON, 'X', pieceFont]
        self.buttons.append(TextButton(*X_args))

    def cleanup(self):
        return self.playPieceChoice

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)

        surf, rect = create_text(*self.titleArgs)
        screen.blit(surf, rect)

        for button in self.buttons:
            button.process(screen)

    def to_singleplayer(self):
        self.next = SinglePlayer.state
        self.done = True

    def select_O(self):
        self.playPieceChoice = CHOICE_O
        self.to_singleplayer()

    def select_X(self):
        self.playPieceChoice = CHOICE_X
        self.to_singleplayer()


class SinglePlayer(object):
    state = "Singleplayer"

    def __init__(self):
        self.playPieceChoice = None
        self.current = self.state
        self.previous = None
        self.next = None
        self.done = False
        self.quit = False
        self.buttons = []
        self.availableMoves = ['', '', '', '', '', '', '', '', '']
        self.backgroundColor = colors.WHITE
        self.buttonColors = ButtonColors({
            "normal": "#ff0000ff",
            "hover": "#eeff00ff",
            "pressed": "#00000000"
        })

    def startup(self, data=None):
        if data is not CHOICE_O and data is not CHOICE_X:
            error.log_error(f"Player piece choice is '{data}'. Exiting.")
            exit()
        self.playPieceChoice = data
        self.buttons += setup_board_buttons(
            self.buttonColors,
            self.place_piece
        )

    def cleanup(self):
        pass

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)

        draw_tictactoe_board(screen, colors.BLACK)
        for button in self.buttons:
            button.process(screen)

    def place_piece(self, move):
        pass
