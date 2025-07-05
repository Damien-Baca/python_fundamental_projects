from collections.abc import Callable

import pygame as pyg

from .typing import ButtonColors
from .colors import RED, BLACK
from .button import TextButton


class GameBoard(object):
    CHOICE_O = 'O'
    CHOICE_X = 'X'

    GameBoardColor = "#111111"
    boardButtonColors = ButtonColors({
        "normal": "#FFFFFF00",
        "hover": "#ffffff00",
        "pressed": "#FFFFFF00"
    })

    def __init__(self, startingTurn: str) -> None:
        self.turn = startingTurn
        self.boardButtons = []
        self.boardState = [''] * 9

    def startup(self) -> None:
        """Create Tic-Tac-Toe board place move buttons """
        self.boardButtons = []
        args = [0, 0, 0, 0, 0, self.boardButtonColors]
        args[0:5] = [150, 125, 100, 100, self.place_piece_init(0)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [250, 125, 100, 100, self.place_piece_init(1)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [350, 125, 100, 100, self.place_piece_init(2)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [150, 225, 100, 100, self.place_piece_init(3)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [250, 225, 100, 100, self.place_piece_init(4)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [350, 225, 100, 100, self.place_piece_init(5)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [150, 325, 100, 100, self.place_piece_init(6)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [250, 325, 100, 100, self.place_piece_init(7)]
        self.boardButtons.append(TextButton(*args))
        args[0:5] = [350, 325, 100, 100, self.place_piece_init(8)]
        self.boardButtons.append(TextButton(*args))

    def update(self):
        for i, move in enumerate(self.boardState):
            self.boardButtons[i].buttonText = move
            if move is self.CHOICE_O:
                self.boardButtons[i].textColor = RED
            else:
                self.boardButtons[i].textColor = BLACK

    def draw(self, screen: pyg.Surface) -> None:
        """Draws the Tic-Tac-Toe board"""
        pyg.draw.line(screen, self.GameBoardColor, (200, 75), (200, 375), 5)
        pyg.draw.line(screen, self.GameBoardColor, (300, 75), (300, 375), 5)
        pyg.draw.line(screen, self.GameBoardColor, (100, 175), (400, 175), 5)
        pyg.draw.line(screen, self.GameBoardColor, (100, 275), (400, 275), 5)

        for button in self.boardButtons:
            button.process(screen)

    def check_win(self):
        pass

    def place_piece_init(self, move: int):
        """
        Returns a function that makes a move on the board that depends
        on which players turn it is.
        """
        def place_piece():
            if not self.boardState[move]:
                self.boardState[move] = self.turn
                self.turn = self.CHOICE_X if self.turn is self.CHOICE_O else self.CHOICE_O
        return place_piece

    def get_current_turn(self) -> str:
        return self.turn
