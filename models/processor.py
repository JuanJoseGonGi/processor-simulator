import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control_unit import ControlUnit


class Processor:
    def __init__(self) -> None:
        self.x = 100
        self.y = 100
        self.width = 300
        self.height = 300
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.ALU = ALU()
        self.UC = ControlUnit()

        self.PC = Record()
        self.MBR = Record()
        self.MAR = Record()
        self.IR = Record()

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, (255, 255, 255), self.rect)
