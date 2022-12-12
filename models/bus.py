import pygame as pg

import constants

from typing import List, Tuple


class Bus:
    def __init__(self, points: List[Tuple[int, int]]):
        self.points = points

        self.data = 0
        self.used = False

    def set_data(self, data):
        self.data = data
        self.used = True

    def reset(self):
        self.data = 0
        self.used = False

    def update(self):
        pass

    def draw(self, screen):
        pg.draw.lines(screen, constants.BLACK, False, self.points, constants.BUS_WIDTH)
