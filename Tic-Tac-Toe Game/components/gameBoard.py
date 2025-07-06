import pygame as pyg

from .error import log_error
from .typing import ButtonColors
from .colors import RED, BLACK
from .button import TextButton


class GameBoard(object):
    O = "O"
    X = "X"
    TIE = "Tie"

    GameBoardColor = "#111111"
    boardButtonColors = ButtonColors({
        "normal": "#FFFFFF00",
        "hover": "#ffffff00",
        "pressed": "#FFFFFF00"
    })

    def __init__(self, startingTurn: str) -> None:
        self.turn = startingTurn
        self.boardButtons = []
        self.boardState = [""] * 9

    def init_board(self) -> None:
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

    def update_board(self):
        """Updates the Tic-Tac-Toe board."""
        for i, move in enumerate(self.boardState):
            self.boardButtons[i].buttonText = move
            if move == self.O:
                self.boardButtons[i].textColor = RED
            else:
                self.boardButtons[i].textColor = BLACK

    def draw_board(self, screen: pyg.Surface) -> None:
        """Draws the Tic-Tac-Toe board."""
        pyg.draw.line(screen, self.GameBoardColor, (200, 75), (200, 375), 5)
        pyg.draw.line(screen, self.GameBoardColor, (300, 75), (300, 375), 5)
        pyg.draw.line(screen, self.GameBoardColor, (100, 175), (400, 175), 5)
        pyg.draw.line(screen, self.GameBoardColor, (100, 275), (400, 275), 5)

        for button in self.boardButtons:
            button.process(screen)

    def check_win(self) -> str | None:
        """Checks to see if a player has won. If that's the case, returns winning piece."""
        checks = [
            self.check_trio([0, 1, 2]),
            self.check_trio([3, 4, 5]),
            self.check_trio([6, 7, 8]),
            self.check_trio([0, 3, 6]),
            self.check_trio([1, 4, 7]),
            self.check_trio([2, 5, 8]),
            self.check_trio([0, 4, 8]),
            self.check_trio([2, 4, 6])
        ]
        results = [result for result in checks if result is not None]
        if len(results) == 1:
            return results[0]
        if len(results) > 1:
            log_error("Error, invalid game results: multiple win conditions")
            exit()
        if self.boardState.count('') == 0:
            return self.TIE

    def check_trio(self, trioIndex: list[int]) -> str | None:
        trio = [self.boardState[i] for i in trioIndex]
        if trio.count(self.O) == 3:
            return self.O
        if trio.count(self.X) == 3:
            return self.X

    def place_piece_init(self, move: int):
        """
        Returns a function that makes a move on the board that depends
        on which players turn it is.
        """
        def place_piece():
            if not self.boardState[move]:
                self.boardState[move] = self.turn
                self.turn = self.X if self.turn == self.O else self.O
        return place_piece

    def get_current_turn(self) -> str:
        return self.turn
