from enum import Enum


class ControlSignal(Enum):
    NONE = 0
    COPY_PC_TO_MAR = 1
    COPY_MBR_TO_MAR = 2
    COPY_MBR_TO_IR = 3
    COPY_MBR_TO_ALU = 4
    COPY_ALU_TO_MBR = 5
    READ_FROM_MEMORY = 6
    WRITE_TO_MEMORY = 7
    DONE = 8


FETCH_STAGES = [
    ControlSignal.COPY_PC_TO_MAR,
    ControlSignal.READ_FROM_MEMORY,
    ControlSignal.COPY_MBR_TO_IR,
]
