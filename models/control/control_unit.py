import pygame as pg

from models.record import Record
from models.alu import ALU
from models.instructions.instruction import Instruction
from models.control.control_signal import ControlSignal
from models.control.instructions_set import InstructionsSet
from models.interface import Interface
from models.memories.memory_mode import MemoryMode

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
        address_iface: Interface[str],
        data_iface: Interface[str],
        control_iface: Interface[MemoryMode],
        stack: List[Record],
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
        self.address_iface = address_iface
        self.data_iface = data_iface
        self.control_iface = control_iface
        self.stack = stack

        self.instructions_pipeline: List[Instruction] = []
        self.instructions_set = InstructionsSet()

    def add_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.append(instruction)

    def remove_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.remove(instruction)

    def increase_pc(self) -> None:
        pc_data = self.PC.get_data()
        if pc_data is None:
            raise Exception("PC data is None")

        if pc_data == "31":
            self.PC.set_data("00")
            return

        increased_pc_data = int(pc_data) + 1

        self.PC.set_data(f"{increased_pc_data:02d}")

    def send_control_signal(
        self, control_signal: ControlSignal, instruction: Instruction
    ) -> None:
        if control_signal == ControlSignal.COPY_PC_TO_MAR:
            self.MAR.set_data(self.PC.get_data())
            return

        if control_signal == ControlSignal.COPY_MBR_TO_MAR:
            self.MAR.set_data(self.MBR.get_data())
            return

        if control_signal == ControlSignal.COPY_MBR_TO_IR:
            self.IR.set_data(self.MBR.get_data())
            return

        if control_signal == ControlSignal.COPY_ALU_TO_MBR:
            self.MBR.set_data(self.ALU.output.get_data())
            return

        if control_signal == ControlSignal.READ_FROM_MEMORY:
            self.control_iface.set_data(MemoryMode.READ)
            self.address_iface.set_data(self.MAR.get_data())
            return

        if control_signal == ControlSignal.WRITE_TO_MEMORY:
            self.control_iface.set_data(MemoryMode.WRITE)
            self.address_iface.set_data(self.MAR.get_data())
            self.data_iface.set_data(self.MBR.get_data())
            return

        if control_signal == ControlSignal.INCREASE_PC:
            self.increase_pc()
            return

        if control_signal == ControlSignal.DONE:
            self.remove_instruction(instruction)
            return

    def send_control_signals(
        self, control_signals: List[ControlSignal], instruction: Instruction
    ) -> None:
        for signal in control_signals:
            self.send_control_signal(signal, instruction)

    def update(self) -> None:
        for instruction in self.instructions_pipeline:
            signals = instruction.update()
            self.send_control_signals(signals, instruction)
            instruction.increase_stage()

    def draw(self, screen: pg.surface.Surface) -> None:
        pg.draw.rect(screen, constants.GREEN, self.rect)

        text = pg.font.SysFont(constants.FONT, 20).render("CU", True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
