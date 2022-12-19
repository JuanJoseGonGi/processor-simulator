from models.control.control_signal import ControlSignal
from models.control.instructions_set import Codop

from typing import List
from enum import Enum


class InstructionCycle(Enum):
    FETCH = 0
    DECODE = 1
    EXECUTE = 2
    DONE = 3


INSTRUCTION_CYCLES = [
    InstructionCycle.FETCH,
    InstructionCycle.DECODE,
    InstructionCycle.EXECUTE,
    InstructionCycle.DONE,
]

FETCH_STAGES = [
    [ControlSignal.COPY_PC_TO_MAR],
    [ControlSignal.READ_FROM_MEMORY],
    [ControlSignal.COPY_MBR_TO_IR, ControlSignal.INCREASE_PC],
]


class Instruction:
    def __init__(self, codop: Codop, addr: str = "") -> None:
        self.codop = codop
        self.addr = addr
        self.cycle_index = 0
        self.stage_index = 0
        self.executor = None

    def fetch(self) -> List[ControlSignal]:
        return FETCH_STAGES[self.stage_index]

    def decode(self) -> List[ControlSignal]:
        return [ControlSignal.NONE]

    def execute(self) -> List[ControlSignal]:
        return [ControlSignal.NONE]

    def done(self) -> List[ControlSignal]:
        return [ControlSignal.DONE]

    def update(self) -> List[ControlSignal]:
        if self.cycle_index >= len(INSTRUCTION_CYCLES):
            raise Exception("Instruction cycle index out of range")

        cycle = INSTRUCTION_CYCLES[self.cycle_index]

        if cycle == InstructionCycle.FETCH:
            return self.fetch()
        elif cycle == InstructionCycle.DECODE:
            return self.decode()
        elif cycle == InstructionCycle.EXECUTE:
            return self.execute()
        elif cycle == InstructionCycle.DONE:
            return self.done()

        return [ControlSignal.NONE]

    def increase_stage(self) -> None:
        self.stage_index += 1
        if self.stage_index >= len(FETCH_STAGES):
            self.stage_index = 0
            self.cycle_index += 1
