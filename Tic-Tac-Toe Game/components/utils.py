# System imports
from collections.abc import Callable
# Third party imports
import pygame as pyg
# Local imports
from components.button import TextButton
from components.typing import ButtonColors


def create_text(
        text: str, font: pyg.font.Font, x_pos: int, y_pos: int,
        color: str = "#111111",
        backgroundColor: str | None = None
) -> tuple[pyg.Surface, pyg.Rect]:
    """Utility for creating a text box."""
    textColorArgs = [text, True, color]
    if backgroundColor is not None:
        textColorArgs.append(backgroundColor)
    textSurface = font.render(*textColorArgs)
    textRect = textSurface.get_rect()
    textRect.centerx = x_pos
    textRect.centery = y_pos

    return textSurface, textRect


def draw_tictactoe_board(screen: pyg.Surface, color: str) -> None:
    """Draws the Tic-Tac-Toe board"""
    pyg.draw.line(screen, color, (200, 50), (200, 350), 5)
    pyg.draw.line(screen, color, (300, 50), (300, 350), 5)
    pyg.draw.line(screen, color, (100, 150), (400, 150), 5)
    pyg.draw.line(screen, color, (100, 250), (400, 250), 5)


def setup_board_buttons(
        buttonColors: ButtonColors,
        place_piece: Callable
) -> list[TextButton]:
    """Create board's move buttons """
    buttons = []
    args = [0, 0, 0, 0, 0, buttonColors]
    args[0:5] = [150, 100, 100, 100, place_piece(0)]
    buttons.append(TextButton(*args))
    args[0:5] = [250, 100, 100, 100, place_piece(1)]
    buttons.append(TextButton(*args))
    args[0:5] = [350, 100, 100, 100, place_piece(2)]
    buttons.append(TextButton(*args))
    args[0:5] = [150, 200, 100, 100, place_piece(3)]
    buttons.append(TextButton(*args))
    args[0:5] = [250, 200, 100, 100, place_piece(4)]
    buttons.append(TextButton(*args))
    args[0:5] = [350, 200, 100, 100, place_piece(5)]
    buttons.append(TextButton(*args))
    args[0:5] = [150, 300, 100, 100, place_piece(6)]
    buttons.append(TextButton(*args))
    args[0:5] = [250, 300, 100, 100, place_piece(7)]
    buttons.append(TextButton(*args))
    args[0:5] = [350, 300, 100, 100, place_piece(8)]
    buttons.append(TextButton(*args))

    return buttons
