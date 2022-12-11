import pygame as pg

import constants


class ControlUnit:
    def __init__(self, parent_rect: pg.rect.Rect) -> None:
        self.x = constants.CONTROL_UNIT_X
        self.y = constants.CONTROL_UNIT_Y
        self.width = constants.CONTROL_UNIT_WIDTH
        self.height = constants.CONTROL_UNIT_HEIGHT
        self.rect = pg.Rect(
            self.x + parent_rect.x, self.y + parent_rect.y, self.width, self.height
        )

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, constants.GREEN, self.rect)

        text = pg.font.SysFont(constants.FONT, 20).render("CU", True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
