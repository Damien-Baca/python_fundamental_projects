# Third party imports
import pygame as pyg
# Local imports
from components import colors


LEFT_CLICK = 0
MIDDLE_CLICK = 0
RIGHT_CLICK = 0


class TextButton(object):
    alreadyClicked = False

    def __init__(self, x, y, width, height, onClickFunction, fillColors=colors.DEFAULT_BUTTON, buttonText=None, font=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onClickFunction = onClickFunction
        self.fillColors = fillColors
        self.buttonText = buttonText

        centerx = self.x - self.width / 2
        centery = self.y - self.height / 2
        buttonSize = (self.width, self.height)
        self.buttonSurface = pyg.Surface(buttonSize, pyg.SRCALPHA)
        self.buttonRect = pyg.Rect(centerx, centery, *buttonSize)

        if font is not None:
            self.buttonText = font.render(buttonText, True, (20, 20, 20))

    def process(self, screen: pyg.Surface) -> None:
        mouse_pos = pyg.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors["normal"])
        if self.buttonRect.collidepoint(mouse_pos):
            self.buttonSurface.fill(self.fillColors["hover"])
            mouse_btn_state = pyg.mouse.get_pressed()
            if mouse_btn_state[LEFT_CLICK]:
                if not TextButton.alreadyClicked:
                    self.buttonSurface.fill(self.fillColors["pressed"])
                    self.onClickFunction()
                    TextButton.alreadyClicked = True
            else:
                TextButton.alreadyClicked = False

        if self.buttonText is not None:
            buttonRectWidth = self.buttonRect.width
            buttonRectHeight = self.buttonRect.height
            buttonTextWidth = self.buttonText.get_rect().width
            buttonTextHeight = self.buttonText.get_rect().height
            self.buttonSurface.blit(self.buttonText, [
                buttonRectWidth/2 - buttonTextWidth/2,
                buttonRectHeight/2 - buttonTextHeight/2
            ])
        screen.blit(self.buttonSurface, self.buttonRect)


class ImageButton(object):
    pass
