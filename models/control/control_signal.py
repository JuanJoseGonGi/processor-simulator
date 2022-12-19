from enum import Enum


class ControlSignal(Enum):
    NONE = "NONE"
    COPY_PC_TO_MAR = "COPY_PC_TO_MAR"
    COPY_MBR_TO_MAR = "COPY_MBR_TO_MAR"
    COPY_MBR_TO_IR = "COPY_MBR_TO_IR"
    COPY_IR_TO_MAR = "COPY_IR_TO_MAR"
    COPY_ALU_TO_MBR = "COPY_ALU_TO_MBR"
    READ_FROM_MEMORY = "READ_FROM_MEMORY"
    WRITE_TO_MEMORY = "WRITE_TO_MEMORY"
    INCREASE_PC = "INCREASE_PC"
    PUSH_MBR_TO_STACK = "PUSH_MBR_TO_STACK"
    POP_STACK_TO_MBR = "POP_STACK_TO_MBR"
    PUSH_ALU_TO_STACK = "PUSH_ALU_TO_STACK"
    POP_STACK_TO_ALU = "POP_STACK_TO_ALU"
    COPY_CODOP_TO_ALU = "COPY_CODOP_TO_ALU"
    EXECUTE_ALU = "EXECUTE_ALU"
    DONE = "DONE"
