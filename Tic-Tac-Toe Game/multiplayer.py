from sys import exit
from random import choice

import pygame as pyg

import components.colors as colors
from components.error import log_error
from components.button import TextButton
from components.utils import create_text
from components.gameBoard import GameBoard as GB
from gamestates import \
    VictoryState, MultiPlayerChoiceState, MultiPlayerState


class MultiPlayerChoice(object):
    def __init__(self):
        self.next = None
        self.done = False
        self.quit = False

        self.current = MultiPlayerChoiceState
        self.previous = None
        self.p1Piece = None
        self.backgroundColor = colors.WHITE
        self.buttons = []
        self.returnData = {}

    def startup(self, data={}):
        self.next = None
        self.done = False
        self.quit = False
        pieceFont = pyg.font.SysFont("Arial", 80)
        O_args = [175, 250, 75, 75, self.select_O, colors.DEFAULT_BUTTON,
                  colors.RED, GB.O, pieceFont]
        self.buttons.append(TextButton(*O_args))
        X_args = [325, 250, 75, 75, self.select_X, colors.DEFAULT_BUTTON,
                  colors.BLACK, GB.X, pieceFont]
        self.buttons.append(TextButton(*X_args))

    def cleanup(self):
        return self.returnData

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
        self.next = MultiPlayerState
        self.done = True

    def select_O(self):
        # self.p1Piece = GB.O
        self.returnData["p1Piece"] = GB.O
        self.to_multiplayer()

    def select_X(self):
        # self.p1Piece = GB.X
        self.returnData["p1Piece"] = GB.X
        self.to_multiplayer()


class Multiplayer(object):
    def __init__(self):
        self.next = None
        self.done = False
        self.quit = False
        self.p1Score = 0
        self.p2Score = 0
        self.startingTurn = choice([GB.O, GB.X])

        self.current = MultiPlayerState
        self.previous = None
        self.gameBoard = None
        self.backgroundColor = colors.WHITE
        self.returnData = {}
        self.titleText = "Player 1 - Take your turn."
        self.p1ScoreArgs = []
        self.p2ScoreArgs = []
        self.p1Piece = None
        self.p2Piece = None

    def startup(self, data={}):
        self.next = None
        self.done = False
        self.quit = False
        if "p1Piece" in data:
            self.p1Piece = data["p1Piece"]
        if "continue" not in data or not data["continue"]:
            self.p1Score = 0
            self.p2Score = 0
        if self.p1Piece not in [GB.O, GB.X]:
            log_error("Invalid play piece")
            exit()

        self.p2Piece = GB.O if self.p1Piece == GB.X else GB.X
        scoreFont = pyg.font.SysFont("Arial", 20)
        p1ScoreText = f"Player 1 ({self.p1Piece}): "
        p2ScoreText = f"Player 2 ({self.p2Piece}): "
        self.p1ScoreArgs = [p1ScoreText, scoreFont, 90, 475, "#111111"]
        self.p2ScoreArgs = [p2ScoreText, scoreFont, 410, 475, "#111111"]

        self.gameBoard = GB(self.startingTurn)
        self.gameBoard.init_board()
        self.startingTurn = GB.X if self.startingTurn is GB.O else GB.O

    def cleanup(self):
        return self.returnData

    def event_loop(self):
        pass

    def update(self, screen, dt):
        if self.gameBoard is None:
            log_error("Gameboard does not exist")
            exit()

        self.gameBoard.update_board()
        self.update_score()
        gameResult = self.gameBoard.check_win()
        if gameResult in [GB.O, GB.X, GB.TIE]:
            self.to_victory(gameResult)
        self.draw(screen)

    def draw(self, screen):
        screen.fill(self.backgroundColor)
        if self.gameBoard is None:
            log_error("Gameboard does not exist")
            exit()

        titleFont = pyg.font.SysFont("Arial", 30)
        surf, rect = create_text(self.titleText, titleFont, 250, 25)
        screen.blit(surf, rect)
        p1ScoreText = self.p1ScoreArgs[0] + str(self.p1Score)
        surf, rect = create_text(p1ScoreText, *self.p1ScoreArgs[1:])
        screen.blit(surf, rect)
        p2ScoreText = self.p2ScoreArgs[0] + str(self.p2Score)
        surf, rect = create_text(p2ScoreText, *self.p2ScoreArgs[1:])
        screen.blit(surf, rect)
        self.gameBoard.draw_board(screen)

    def update_score(self):
        if self.gameBoard is None:
            log_error("Gameboard does not exist")
            exit()

        isTurnFont = pyg.font.SysFont("Arial", 25)
        notTurnFont = pyg.font.SysFont("Arial", 20)
        currentTurn = self.gameBoard.get_current_turn()
        if currentTurn == self.p1Piece:
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

    def to_victory(self, result):
        if result == self.p1Piece:
            self.returnData['winnerText'] = "Player 1 has won!"
            self.p1Score += 1
        elif result == self.p2Piece:
            self.returnData['winnerText'] = "Player 2 has won!"
            self.p2Score += 1
        elif result == GB.TIE:
            self.returnData['winnerText'] = "Tie!"
        self.next = VictoryState
        self.done = True
