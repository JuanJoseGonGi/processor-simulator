import pygame as pg

import constants

from enum import Enum


class RecordStatus(Enum):
    IDLE = 0
    BUSY = 1


class Record:
    def __init__(
        self, x: float, y: float, width: float, height: float, parent_rect: pg.rect.Rect
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(
            self.x + parent_rect.x, self.y + parent_rect.y, self.width, self.height
        )

        self.data = 0
        self.name = ""
        self.color = constants.PURPLE
        self.font_color = constants.WHITE
        self.status = RecordStatus.IDLE

    def set_data(self, data: int) -> None:
        self.data = data
        self.status = RecordStatus.BUSY

    def reset(self) -> None:
        self.data = 0
        self.status = RecordStatus.IDLE

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, self.color, self.rect)

        text = pg.font.SysFont(constants.FONT, 12).render(
            self.name + ":" + str(self.data), True, self.font_color
        )
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
