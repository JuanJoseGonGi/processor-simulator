import pygame as pg

from models.alu import ALU
from models.record import Record
from models.control.control_unit import ControlUnit
from models.interface import Interface
from models.buses.system_bus import SystemBus

import constants

from typing import List


class Processor:
    def __init__(self, system_bus: SystemBus) -> None:
        self.x = constants.PROCESSOR_X
        self.y = constants.PROCESSOR_Y
        self.width = constants.PROCESSOR_WIDTH
        self.height = constants.PROCESSOR_HEIGHT
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

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

        self.address_iface = Interface(
            system_bus.address_bus,
        )
        self.data_iface = Interface(system_bus.data_bus)
        self.control_iface = Interface(
            system_bus.control_bus,
        )

        self.ALU = ALU(self.rect)
        self.UC = ControlUnit(self.rect, self.PC, self.MBR, self.MAR, self.IR, self.ALU)

    def update(self) -> None:
        self.UC.update()

    def draw(self, screen: pg.surface.Surface) -> None:
        pg.draw.rect(screen, constants.DARK_BLUE, self.rect)

        self.ALU.draw(screen)
        self.UC.draw(screen)

        self.PC.draw(screen)
        self.MBR.draw(screen)
        self.MAR.draw(screen)
        self.IR.draw(screen)

        for record in self.general_records:
            record.draw(screen)
