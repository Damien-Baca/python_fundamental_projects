import pygame as pyg


def create_text(
        text: str, font: pyg.font.Font,
        x_pos: int, y_pos: int,
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
