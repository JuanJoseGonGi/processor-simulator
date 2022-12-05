import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control_unit import ControlUnit


class Processor:
    def __init__(self) -> None:
        self.ALU = ALU()
        self.UC = ControlUnit()

        self.PC = Record()
        self.MBR = Record()
        self.MAR = Record()
        self.IR = Record()

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, (255, 255, 255), (100, 100, 300, 300))
