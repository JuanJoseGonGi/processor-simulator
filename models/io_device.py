import pygame as pg

from models.bus import Bus

from typing import List


class IODevice:
    def __init__(self) -> None:
        pass

    def update(self, system_bus: List[Bus]) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pass
