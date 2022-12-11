import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control_unit import ControlUnit

import constants

from typing import List


class Processor:
    def __init__(self) -> None:
        self.x = constants.PROCESSOR_X
        self.y = constants.PROCESSOR_Y
        self.width = constants.PROCESSOR_WIDTH
        self.height = constants.PROCESSOR_HEIGHT
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

        self.ALU = ALU(self.rect)
        self.UC = ControlUnit(self.rect)

        self.PC = Record(
            constants.PC_X,
            constants.PC_Y,
            constants.PC_WIDTH,
            constants.PC_HEIGHT,
            self.rect,
        )

        self.PC.name = "PC"

        self.MBR = Record(
            constants.MBR_X,
            constants.MBR_Y,
            constants.MBR_WIDTH,
            constants.MBR_HEIGHT,
            self.rect,
        )

        self.MBR.name = "MBR"

        self.MAR = Record(
            constants.MAR_X,
            constants.MAR_Y,
            constants.MAR_WIDTH,
            constants.MAR_HEIGHT,
            self.rect,
        )

        self.MAR.name = "MAR"

        self.IR = Record(
            constants.IR_X,
            constants.IR_Y,
            constants.IR_WIDTH,
            constants.IR_HEIGHT,
            self.rect,
        )

        self.IR.name = "IR"

        self.general_records: List[Record] = []

        for i in range(constants.GENERAL_RECORDS_LENGTH):
            x = float(constants.GENERAL_RECORDS_X)
            if i % 2 != 0:
                x = constants.GENERAL_RECORDS_X + constants.GENERAL_RECORDS_WIDTH

            y = (
                constants.GENERAL_RECORDS_Y
                + (i // 2) * constants.GENERAL_RECORDS_HEIGHT
            )

            record = Record(
                x,
                y,
                constants.GENERAL_RECORDS_WIDTH,
                constants.GENERAL_RECORDS_HEIGHT,
                self.rect,
            )

            record.name = f"R{i}"

            self.general_records.append(record)

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, constants.DARK_GREEN, self.rect)

        self.ALU.draw(screen)
        self.UC.draw(screen)

        self.PC.draw(screen)
        self.MBR.draw(screen)
        self.MAR.draw(screen)
        self.IR.draw(screen)

        for record in self.general_records:
            record.draw(screen)
