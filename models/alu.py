import pygame as pg

import constants


class ALU:
    def __init__(self) -> None:
        self.x = 10
        self.y = 30
        self.width = 100
        self.height = 100
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen: pg.Surface, parent_rect: pg.Rect) -> None:
        rect = self.rect.copy()
        rect.x += parent_rect.x
        rect.y += parent_rect.y

        points = [
            (rect.x, rect.y),
            (rect.x + rect.width * 0.4, rect.y),
            (rect.x + rect.width * 0.5, rect.y + rect.height * 0.5),
            (rect.x + rect.width * 0.6, rect.y),
            (rect.x + rect.width, rect.y),
            (rect.x + rect.width * 0.6, rect.y + rect.height),
            (rect.x + rect.width * 0.4, rect.y + rect.height),
        ]

        pg.draw.polygon(screen, constants.PURPLE, points)
