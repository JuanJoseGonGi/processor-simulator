import pygame as pg

import constants

from models.bus import Bus

from typing import List


class Memory:
    def __init__(self):
        self.x = constants.MEMORY_X
        self.y = constants.MEMORY_Y
        self.width = constants.MEMORY_WIDTH
        self.height = constants.MEMORY_HEIGHT
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def update(self, system_bus: List[Bus]):
        pass

    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, constants.GREEN, self.rect)

        text = pg.font.SysFont(constants.FONT, 20).render("MM", True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
