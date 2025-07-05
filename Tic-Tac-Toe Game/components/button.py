# System imports
from collections.abc import Callable
# Third party imports
import pygame as pyg
# Local imports
from components import colors


LEFT_CLICK = 0
MIDDLE_CLICK = 0
RIGHT_CLICK = 0


class TextButton(object):
    alreadyClicked = False

    def __init__(self, x, y, width, height, onClickFunction: Callable, buttonColors=colors.DEFAULT_BUTTON, textColor="#111111", buttonText=None, font=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = font
        self.onClickFunction = onClickFunction
        self.buttonColors = buttonColors
        self.textColor = textColor
        self.buttonText = buttonText
        centerx = self.x - self.width / 2
        centery = self.y - self.height / 2
        buttonSize = (self.width, self.height)
        self.buttonSurface = pyg.Surface(buttonSize, pyg.SRCALPHA)
        self.buttonRect = pyg.Rect(centerx, centery, *buttonSize)
        if font is None:
            self.font = pyg.font.SysFont("Arial", 80)

    def process(self, screen: pyg.Surface) -> None:
        if self.font:
            self.buttonTextRender = self.font.render(
                self.buttonText, True, self.textColor)

        mouse_pos = pyg.mouse.get_pos()
        self.buttonSurface.fill(self.buttonColors["normal"])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.buttonColors["hover"])
            mouse_btn_state = pyg.mouse.get_pressed()
            if mouse_btn_state[LEFT_CLICK]:
                if not TextButton.alreadyClicked:
                    self.buttonSurface.fill(self.buttonColors["pressed"])
                    self.onClickFunction()
                    TextButton.alreadyClicked = True
            else:
                TextButton.alreadyClicked = False

        if self.buttonTextRender is not None:
            buttonRectWidth = self.buttonRect.width
            buttonRectHeight = self.buttonRect.height
            buttonTextWidth = self.buttonTextRender.get_rect().width
            buttonTextHeight = self.buttonTextRender.get_rect().height
            self.buttonSurface.blit(self.buttonTextRender, [
                buttonRectWidth/2 - buttonTextWidth/2,
                buttonRectHeight/2 - buttonTextHeight/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)


class ImageButton(object):
    pass
