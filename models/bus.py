import pygame as pg

import constants

from typing import List, Tuple
from enum import Enum


class BusStatus(Enum):
    IDLE = 0
    BUSY = 1


class Bus:
    def __init__(self, width, points: List[Tuple[int, int]]):
        self.width = width
        self.points = points

        self.data = 0
        self.status = BusStatus.IDLE

    def set_data(self, data):
        self.data = data
        self.status = BusStatus.BUSY

    def reset(self):
        self.data = 0
        self.status = BusStatus.IDLE

    def update(self):
        pass

    def draw(self, screen):
        pg.draw.lines(screen, constants.WHITE, False, self.points, self.width)
