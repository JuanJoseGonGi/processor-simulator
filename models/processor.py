import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control_unit import ControlUnit

import constants


class Processor:
    def __init__(self) -> None:
        self.x = constants.PROCESSOR_X
        self.y = constants.PROCESSOR_Y
        self.width = constants.PROCESSOR_WIDTH
        self.height = constants.PROCESSOR_HEIGHT
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.ALU = ALU()
        self.UC = ControlUnit()

        self.PC = Record()
        self.MBR = Record()
        self.MAR = Record()
        self.IR = Record()
        self.GeneralRecords = [
            Record() for _ in range(constants.GENERAL_RECORDS_LENGTH)
        ]

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, constants.DARK_GREEN, self.rect)

        self.ALU.draw(screen, self.rect)
        self.UC.draw(screen, self.rect)

        self.PC.draw(screen, self.rect)
        self.MBR.draw(screen, self.rect)
        self.MAR.draw(screen, self.rect)
        self.IR.draw(screen, self.rect)

        for record in self.GeneralRecords:
            record.draw(screen, self.rect)
