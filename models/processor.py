import pygame as pg
from models import control_unit, alu, record


class Processor:
    def __init__(self) -> None:
        self.ALU = alu.ALU()
        self.PC = record.Record()
        self.UC = control_unit.ControlUnit()
        self.MBR = record.Record()
        self.MAR = record.Record()
        self.IR = record.Record()

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, (255, 255, 255), (100, 100, 300, 300))
