from sys import exit

import pygame as pyg

import components.colors as colors
from components.button import TextButton
from components.utils import create_text
from components.gameBoard import GameBoard as GB


class MultiPlayerChoice(object):
    state = "Multiplayer Choice"

    def __init__(self):
        self.current = self.state
        self.previous = None
        self.next = None
        self.done = False
        self.quit = False
        self.buttons = []
        self.p1Piece = None
        self.backgroundColor = colors.WHITE

    def startup(self, data=None):
        pieceFont = pyg.font.SysFont("Arial", 80)
        O_args = [175, 250, 75, 75, self.select_O, colors.DEFAULT_BUTTON,
                  colors.RED, GB.CHOICE_O, pieceFont]
        self.buttons.append(TextButton(*O_args))
        X_args = [325, 250, 75, 75, self.select_X, colors.DEFAULT_BUTTON,
                  colors.BLACK, GB.CHOICE_X, pieceFont]
        self.buttons.append(TextButton(*X_args))

    def cleanup(self):
        return self.p1Piece

    def event_loop(self):
        pass

    def update(self, screen, dt):
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        titleText = "Player 1, select you're play piece."
        titleFont = pyg.font.SysFont("Arial", 30)
        surf, rect = create_text(titleText, titleFont, 250, 75)
        screen.blit(surf, rect)
        for button in self.buttons:
            button.process(screen)

    def to_multiplayer(self):
        self.next = Multiplayer.state
        self.done = True

    def select_O(self):
        self.p1Piece = GB.CHOICE_O
        self.to_multiplayer()

    def select_X(self):
        self.p1Piece = GB.CHOICE_X
        self.to_multiplayer()


class Multiplayer(object):
    state = "Multiplayer"

    def __init__(self):
        self.current = self.state
        self.previous = None
        self.next = None
        self.done = False
        self.quit = False
        self.backgroundColor = colors.WHITE
        self.gameBoard = None
        self.titleText = "Player 1 - Take your turn."
        self.p1ScoreArgs = []
        self.p2ScoreArgs = []
        self.p1Piece = None
        self.p2Piece = None
        self.p1Score = 0
        self.p2Score = 0

    def startup(self, p1Piece: str):
        if p1Piece is not GB.CHOICE_O and p1Piece is not GB.CHOICE_X:
            exit()  # Error

        self.gameBoard = GB(p1Piece)
        self.gameBoard.startup()
        self.p1Piece = p1Piece
        self.p2Piece = GB.CHOICE_O if p1Piece is GB.CHOICE_X else GB.CHOICE_X
        scoreFont = pyg.font.SysFont("Arial", 20)
        p1ScoreText = f"Player 1 ({self.p1Piece}): "
        p2ScoreText = f"Player 2 ({self.p2Piece}): "
        self.p1ScoreArgs = [p1ScoreText, scoreFont, 90, 475, "#111111"]
        self.p2ScoreArgs = [p2ScoreText, scoreFont, 410, 475, "#111111"]

    def cleanup(self):
        pass

    def event_loop(self):
        pass

    def update(self, screen, dt):
        if self.gameBoard is None:
            exit()  # Error

        self.gameBoard.update()
        self.update_score()
        self.gameBoard.check_win()
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        if self.gameBoard is None:
            exit()  # Error

        titleFont = pyg.font.SysFont("Arial", 30)
        surf, rect = create_text(self.titleText, titleFont, 250, 25)
        screen.blit(surf, rect)
        p1ScoreText = self.p1ScoreArgs[0] + str(self.p1Score)
        surf, rect = create_text(p1ScoreText, *self.p1ScoreArgs[1:])
        screen.blit(surf, rect)
        p2ScoreText = self.p2ScoreArgs[0] + str(self.p2Score)
        surf, rect = create_text(p2ScoreText, *self.p2ScoreArgs[1:])
        screen.blit(surf, rect)
        self.gameBoard.draw(screen)

    def update_score(self):
        if self.gameBoard is None:
            exit()  # Error

        isTurnFont = pyg.font.SysFont("Arial", 25)
        notTurnFont = pyg.font.SysFont("Arial", 20)
        currentTurn = self.gameBoard.get_current_turn()
        if currentTurn is self.p1Piece:
            self.titleText = "Player 1 - Take your turn."
            self.p1ScoreArgs[1] = isTurnFont
            self.p1ScoreArgs[4] = colors.GREEN
            self.p2ScoreArgs[1] = notTurnFont
            self.p2ScoreArgs[4] = colors.BLACK
        else:
            self.titleText = "Player 2 - Take your turn."
            self.p1ScoreArgs[1] = notTurnFont
            self.p1ScoreArgs[4] = colors.BLACK
            self.p2ScoreArgs[1] = isTurnFont
            self.p2ScoreArgs[4] = colors.GREEN
