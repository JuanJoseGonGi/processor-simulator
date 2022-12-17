import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control_unit import ControlUnit
from models.bus import Bus
from models.instruction import Instruction

import constants

from typing import List
from enum import Enum


class ProcessorCycle(Enum):
    FETCH = 0
    DECODE = 1
    EXECUTE = 2


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

        half_general_records_length = constants.GENERAL_RECORDS_LENGTH // 2
        for i in range(constants.GENERAL_RECORDS_LENGTH):
            x = float(constants.GENERAL_RECORDS_X)
            if i >= half_general_records_length != 0:
                x = constants.GENERAL_RECORDS_X + constants.GENERAL_RECORDS_WIDTH

            y = (
                constants.GENERAL_RECORDS_Y
                + (i % half_general_records_length) * constants.GENERAL_RECORDS_HEIGHT
            )

            record = Record(
                x,
                y,
                constants.GENERAL_RECORDS_WIDTH,
                constants.GENERAL_RECORDS_HEIGHT,
                self.rect,
            )

            record.name = f"R{i:02d}"

            self.general_records.append(record)

        self.current_cycle = ProcessorCycle.FETCH
        self.current_instruction: Instruction | None = None

    def fetch(self) -> None:
        self.MAR.set_data(self.PC.data)
        self.PC.set_data(self.PC.data + 1)

    def decode(self) -> None:
        self.IR.set_data(self.MBR.data)
        self.current_instruction = Instruction(self.IR.data)

    def update(self, system_bus: List[Bus]) -> None:
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
