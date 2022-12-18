from models.control.control_signal import ControlSignal, FETCH_STAGES

from typing import List
from enum import Enum


class InstructionCycle(Enum):
    FETCH = 0
    DECODE = 1
    EXECUTE = 2


INSTRUCTION_CYCLES = [
    InstructionCycle.FETCH,
    InstructionCycle.DECODE,
    InstructionCycle.EXECUTE,
]


class Instruction:
    def __init__(self, codop: str, addr: str = "") -> None:
        self.codop = codop
        self.addr = addr
        self.cycle_index = 0
        self.stage_index = 0

    def fetch(self) -> List[ControlSignal]:
        return [FETCH_STAGES[self.stage_index]]

    def decode(self) -> List[ControlSignal]:
        return [ControlSignal.NONE]

    def execute(self) -> List[ControlSignal]:
        return [ControlSignal.NONE]

    def update(self) -> List[ControlSignal]:
        if self.cycle_index >= len(INSTRUCTION_CYCLES):
            return [ControlSignal.DONE]

        cycle = INSTRUCTION_CYCLES[self.cycle_index]

        if cycle == InstructionCycle.FETCH:
            return self.fetch()
        elif cycle == InstructionCycle.DECODE:
            return self.decode()
        elif cycle == InstructionCycle.EXECUTE:
            return self.execute()

        return [ControlSignal.NONE]

    def increase_stage(self) -> None:
        self.stage_index += 1
        if self.stage_index >= len(FETCH_STAGES):
            self.stage_index = 0
            self.cycle_index += 1
