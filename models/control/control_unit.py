import pygame as pg

from models.record import Record
from models.alu import ALU
from models.instructions.instruction import Instruction
from models.control.control_signal import ControlSignal
from models.control.instructions_set import InstructionsSet
from models.control.instructions_set import Codop
from models.interface import Interface
from models.memories.memory_mode import MemoryMode

import constants

from typing import List

FETCH = [
    [ControlSignal.COPY_PC_TO_MAR],
    [ControlSignal.READ_FROM_MEMORY],
    [ControlSignal.COPY_DATA_IFACE_TO_MBR],
    [ControlSignal.COPY_MBR_TO_IR, ControlSignal.INCREASE_PC],
]


class ControlUnit:
    def __init__(
        self,
        parent_rect: pg.rect.Rect,
        PC: Record,
        MBR: Record,
        MAR: Record,
        IR: Record,
        ALU: ALU,
        address_iface: Interface[str | None],
        data_iface: Interface[str | None],
        control_iface: Interface[MemoryMode | None],
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
        self.stack_pointer = 31

        self.instructions_pipeline: List[Instruction] = []
        self.instructions_set = InstructionsSet()

        self.fetch_stage = 0

    def add_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.append(instruction)

    def remove_instruction(self, instruction: Instruction) -> None:
        self.instructions_pipeline.remove(instruction)

    def increase_pc(self) -> None:
        pc_data = self.PC.get_data()
        if pc_data is None:
            raise Exception("PC data is None")

        if pc_data == "15":
            self.PC.set_data("00")
            return

        increased_pc_data = int(pc_data) + 1

        self.PC.set_data(f"{increased_pc_data:02d}")

    def stack_pop(self) -> str | None:
        if self.stack_pointer > 31:
            return None

        data = self.stack[self.stack_pointer].get_data()
        self.stack[self.stack_pointer].set_data(None)
        self.stack_pointer += 1

        return data

    def stack_push(self, data: str | None) -> None:
        if self.stack_pointer < 1:
            raise Exception("Stack overflow")

        self.stack_pointer -= 1
        self.stack[self.stack_pointer].set_data(self.MBR.get_data())

        return

    def send_control_signal(
        self, control_signal: ControlSignal, instruction: Instruction | None = None
    ) -> None:
        print(f"Sending control signal: {control_signal} on instruction: {instruction}")

        if control_signal == ControlSignal.COPY_PC_TO_MAR:
            self.MAR.set_data(self.PC.get_data())
            return

        if control_signal == ControlSignal.COPY_MBR_TO_MAR:
            self.MAR.set_data(self.MBR.get_data())
            return

        if control_signal == ControlSignal.COPY_MBR_TO_IR:
            self.IR.set_data(self.MBR.get_data())
            return

        if control_signal == ControlSignal.COPY_IR_TO_MAR:
            self.MAR.set_data(self.IR.get_data())
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

        if control_signal == ControlSignal.COPY_DATA_IFACE_TO_MBR:
            self.MBR.set_data(self.data_iface.get_data())
            return

        if control_signal == ControlSignal.INCREASE_PC:
            self.increase_pc()
            return

        if control_signal == ControlSignal.PUSH_MBR_TO_STACK:
            self.stack_push(self.MBR.get_data())
            return

        if control_signal == ControlSignal.POP_STACK_TO_MBR:
            self.MBR.set_data(self.stack_pop())
            return

        if control_signal == ControlSignal.PUSH_ALU_TO_STACK:
            self.stack_push(self.ALU.output.get_data())
            return

        if control_signal == ControlSignal.POP_STACK_TO_ALU:
            self.ALU.output.set_data(self.stack_pop())
            return

        if control_signal == ControlSignal.EXECUTE_ALU:
            self.ALU.execute()
            return

        if control_signal == ControlSignal.COPY_MBR_TO_PC_IF_TRUE:
            cond = bool(self.stack_pop())
            if not cond:
                return

            next_pc = self.stack_pop()
            if next_pc is None:
                raise Exception("Next PC is None")

            self.PC.set_data(next_pc)

            return

        if control_signal == ControlSignal.CLEAR_PIPELINE:
            self.instructions_pipeline = []
            self.fetch_stage = 0
            return

        if instruction is None:
            return

        if control_signal == ControlSignal.COPY_CODOP_TO_ALU:
            self.ALU.set_codop(instruction.codop)
            return

        if control_signal == ControlSignal.DONE:
            self.remove_instruction(instruction)
            return

    def send_control_signals(
        self,
        control_signals: List[ControlSignal],
        instruction: Instruction | None = None,
    ) -> None:
        for signal in control_signals:
            self.send_control_signal(signal, instruction)

    def fetch(self) -> None:
        if len(self.instructions_pipeline) >= 5:
            return

        if self.fetch_stage >= len(FETCH):
            self.fetch_stage = 0

        signals = FETCH[self.fetch_stage]
        self.send_control_signals(signals)

    def decode(self) -> None:
        if len(self.instructions_pipeline) >= 5:
            return

        if self.fetch_stage != 0:
            return

        ir_data = self.IR.get_data()
        if ir_data is None:
            return

        decoded_instruction = ir_data.split()
        if len(decoded_instruction) == 0:
            return

        if decoded_instruction[0] not in Codop:
            return

        codop = Codop[decoded_instruction[0]]

        if len(decoded_instruction) == 1:
            decoded_instruction.append("")

        instruction = Instruction(codop, decoded_instruction[1])
        self.instructions_pipeline.append(instruction)

    def update(self) -> None:
        for instruction in self.instructions_pipeline:
            signals = instruction.update()
            self.send_control_signals(signals, instruction)
            instruction.increase_stage()

        self.fetch()
        self.fetch_stage += 1

        self.decode()

    def draw(self, screen: pg.surface.Surface) -> None:
        pg.draw.rect(screen, constants.GREEN, self.rect)

        text = pg.font.SysFont(constants.FONT, 20).render("CU", True, constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        screen.blit(text, text_rect)
