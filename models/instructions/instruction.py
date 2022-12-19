from models.control.control_signal import ControlSignal
from models.control.instructions_set import Codop

from typing import List
from enum import Enum


class InstructionCycle(Enum):
    FETCH = 0
    DECODE = 1
    EXECUTE = 2
    DONE = 3


class Instruction:
    def __init__(self, codop: Codop, addr: str = "") -> None:
        self.codop = codop
        self.addr = addr
        self.executor: List[List[ControlSignal]] = []
        self.stage_index = 0

    def execute(self) -> List[ControlSignal]:
        return self.executor[self.stage_index]

    def done(self) -> List[ControlSignal]:
        return [ControlSignal.DONE]

    def update(self) -> List[ControlSignal]:
        return self.execute()

    def increase_stage(self) -> None:
        self.stage_index += 1
        if self.stage_index >= len(self.executor):
            self.done()
