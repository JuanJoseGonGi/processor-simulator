from models.control.control_signal import ControlSignal

from enum import Enum
from typing import List, Dict


class Codop(Enum):
    ADD = "0000"
    SUB = "0001"
    MPY = "0010"
    DIV = "0011"
    PUSH = "0100"
    POP = "0101"
    ABS = "0110"
    AND = "0111"
    OR = "1000"
    NOT = "1001"
    COMPARE = "1010"
    INPUT = "1011"
    OUTPUT = "1100"
    CONDJUMP = "1101"
    RETURN = "1110"
    START_IO = "1111"


UNARY_OPERATION: List[List[ControlSignal]] = [
    [ControlSignal.POP_STACK_TO_ALU],
    [ControlSignal.COPY_CODOP_TO_ALU],
    [ControlSignal.EXECUTE_ALU],
    [ControlSignal.PUSH_ALU_TO_STACK],
]

BINARY_OPERATION: List[List[ControlSignal]] = [
    [ControlSignal.POP_STACK_TO_ALU]
] + UNARY_OPERATION

INSTRUCTION_SET: Dict[Codop, List[List[ControlSignal]]] = {
    Codop.ADD: BINARY_OPERATION,
    Codop.SUB: BINARY_OPERATION,
    Codop.MPY: BINARY_OPERATION,
    Codop.DIV: BINARY_OPERATION,
    Codop.PUSH: [
        [ControlSignal.COPY_IR_TO_MAR],
        [ControlSignal.READ_FROM_MEMORY],
        [ControlSignal.PUSH_MBR_TO_STACK],
    ],
    Codop.POP: [
        [
            ControlSignal.POP_STACK_TO_MBR,
            ControlSignal.COPY_IR_TO_MAR,
        ],
        [ControlSignal.WRITE_TO_MEMORY],
    ],
    Codop.ABS: UNARY_OPERATION,
    Codop.AND: BINARY_OPERATION,
    Codop.OR: BINARY_OPERATION,
    Codop.NOT: UNARY_OPERATION,
    Codop.COMPARE: BINARY_OPERATION,
    Codop.INPUT: [
        # TODO: Julian will implement this
    ],
    Codop.OUTPUT: [
        # TODO: Julian will implement this
    ],
    Codop.CONDJUMP: BINARY_OPERATION,
    Codop.RETURN: [
        # TODO: If we have time, we will implement this with the interrupts
    ],
}


class InstructionsSet:
    def __init__(self) -> None:
        self.instructions = INSTRUCTION_SET

    def get_instruction_executor(self, codop: Codop) -> List[List[ControlSignal]]:
        return self.instructions[codop]
