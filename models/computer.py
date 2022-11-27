import pygame as pg
from models import processor


class Computer:
    def __init__(self) -> None:
        self.processor = processor.Processor()

    def update(self) -> None:
        print("Executing")

    def draw(self, screen: pg.Surface) -> None:
        self.processor.draw(screen)
