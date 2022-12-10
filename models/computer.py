import pygame as pg
from models.processor import Processor


class Computer:
    def __init__(self) -> None:
        self.processor = Processor()

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        self.processor.draw(screen)
