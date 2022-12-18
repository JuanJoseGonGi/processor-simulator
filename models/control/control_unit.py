import pygame as pg

from models.record import Record
from models.alu import ALU
from models.instructions.instruction import Instruction
from models.control.control_signal import ControlSignal

import constants

from typing import List


class ControlUnit:
    def __init__(
        self,
        parent_rect: pg.rect.Rect,
        PC: Record,
        MBR: Record,
        MAR: Record,
        IR: Record,
        ALU: ALU,
    ) -> None:
        self.x = constants.CONTROL_UNIT_X
        self.y = constants.CONTROL_UNIT_Y
        self.width = constants.CONTROL_UNIT_WIDTH
        self.height = constants.CONTROL_UNIT_HEIGHT
        self.rect = pg.Rect(
            self.x + parent_rect.x, self.y + parent_rect.y, self.width, self.height
        )

        self.PC = PC
        self.MBR = MBR
        self.MAR = MAR
        self.IR = IR
        self.ALU = ALU

        self.instructions_pipeline: List[Instruction] = []

    def add_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.append(instruction)

    def remove_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.remove(instruction)

    def send_control_signal(self, control_signal: ControlSignal) -> None:
        if control_signal == ControlSignal.COPY_PC_TO_MAR:
            self.MAR.set_data(self.PC.get_data())
        elif control_signal == ControlSignal.COPY_MBR_TO_IR:
            self.IR.set_data(self.MBR.get_data())
        elif control_signal == ControlSignal.COPY_MBR_TO_ALU:
            # TODO
            # self.ALU.set_data(self.MBR.get_data())
            pass
        elif control_signal == ControlSignal.COPY_ALU_TO_MBR:
            # TODO
            # self.MBR.set_data(self.ALU.get_data())
            pass
        elif control_signal == ControlSignal.COPY_MBR_TO_MAR:
            self.MAR.set_data(self.MBR.get_data())

    def send_control_signals(self, control_signals: List[ControlSignal]) -> None:
        for signal in control_signals:
            self.send_control_signal(signal)

    def update(self) -> None:
        for instruction in self.instructions_pipeline:
            instruction.update()

    def draw(self, screen: pg.surface.Surface) -> None:
        pg.draw.rect(screen, constants.GREEN, self.rect)

        text = pg.font.SysFont(constants.FONT, 20).render("CU", True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
