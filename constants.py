import pygame as pg

# Colors
DARK_GREEN = (4, 138, 129)
GREEN = (6, 214, 160)
BLUE = (84, 198, 235)
PURPLE = (138, 137, 192)
PINK = (205, 162, 171)
WHITE = (255, 255, 255)
BLACK = (17, 17, 17)

# Fonts
FONT = "Consolas"

# Window
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1366

# Pygame events
COMPUTER_CLK = pg.USEREVENT
TOGGLE_EDITOR = pg.USEREVENT + 1

# Control bar
CONTROL_BAR_HEIGHT = WINDOW_HEIGHT * 0.07
CONTROL_BAR_X = 0
CONTROL_BAR_BUTTON_HEIGHT = (int)(CONTROL_BAR_HEIGHT * 0.6)
CONTROL_BAR_BUTTON_Y = (int)(CONTROL_BAR_HEIGHT * 0.2)

# Instructions text input
ITI_OFFSET_X = WINDOW_WIDTH * 0.01
ITI_OFFSET_Y = ITI_OFFSET_X
ITI_TEXT_AREA_HEIGHT = WINDOW_HEIGHT - (ITI_OFFSET_Y * 7)
ITI_TEXT_AREA_WIDTH = WINDOW_WIDTH - (ITI_OFFSET_X * 2)

# Memory
MEMORY_WIDTH = WINDOW_WIDTH * 0.4
MEMORY_HEIGHT = WINDOW_HEIGHT - CONTROL_BAR_HEIGHT - WINDOW_HEIGHT * 0.02
MEMORY_X = WINDOW_WIDTH - MEMORY_WIDTH - 10
MEMORY_Y = WINDOW_HEIGHT * 0.01

# Memory cell
MEMORY_CELL_GAP_Y = 10
MEMORY_CELL_GAP_X = 5
MEMORY_CELL_WIDTH = MEMORY_WIDTH / 4 - MEMORY_CELL_GAP_X
MEMORY_CELL_HEIGHT = MEMORY_HEIGHT / 8 - MEMORY_CELL_GAP_Y
MEMORY_CELL_X = MEMORY_CELL_GAP_X / 2
MEMORY_CELL_Y = MEMORY_CELL_GAP_Y / 2

# Processor
PROCESSOR_X = WINDOW_WIDTH * 0.01
PROCESSOR_Y = PROCESSOR_X
PROCESSOR_WIDTH = WINDOW_WIDTH * 0.4
PROCESSOR_HEIGHT = PROCESSOR_WIDTH

# ALU
ALU_X = 30
ALU_Y = 60
ALU_WIDTH = PROCESSOR_WIDTH * 0.5
ALU_HEIGHT = PROCESSOR_HEIGHT * 0.25
ALU_INPUT_WIDTH = ALU_WIDTH * 0.5
ALU_INPUT_HEIGHT = 20
ALU_INPUT_Y = -ALU_INPUT_HEIGHT - 10
ALU_OUTPUT_Y = ALU_HEIGHT + 10

# Control Unit
CONTROL_UNIT_WIDTH = PROCESSOR_WIDTH * 0.25
CONTROL_UNIT_HEIGHT = CONTROL_UNIT_WIDTH
CONTROL_UNIT_X: float = PROCESSOR_WIDTH - CONTROL_UNIT_WIDTH - ALU_X
CONTROL_UNIT_Y = ALU_Y + ALU_INPUT_Y

# PC
PC_X = CONTROL_UNIT_X
PC_WIDTH = CONTROL_UNIT_WIDTH
PC_HEIGHT = PROCESSOR_HEIGHT * 0.05
PC_Y = CONTROL_UNIT_Y + CONTROL_UNIT_HEIGHT + 10

# MBR
MBR_X = PC_X
MBR_WIDTH = PC_WIDTH
MBR_Y = PC_Y + PC_HEIGHT + 10
MBR_HEIGHT = PC_HEIGHT

# MAR
MAR_X = MBR_X
MAR_WIDTH = MBR_WIDTH
MAR_Y = MBR_Y + MBR_HEIGHT + 10
MAR_HEIGHT = MBR_HEIGHT

# IR
IR_X = MAR_X
IR_WIDTH = MAR_WIDTH
IR_Y = MAR_Y + MAR_HEIGHT + 10
IR_HEIGHT = MAR_HEIGHT

# General Records
GENERAL_RECORDS_LENGTH = 16
GENERAL_RECORDS_WIDTH = PC_WIDTH
GENERAL_RECORDS_HEIGHT = PC_HEIGHT
GENERAL_RECORDS_X = ALU_X
GENERAL_RECORDS_Y = (
    PROCESSOR_HEIGHT
    - GENERAL_RECORDS_HEIGHT * GENERAL_RECORDS_LENGTH / 2
    - PROCESSOR_HEIGHT * 0.03
)

# BUS
BUS_WIDTH = 2

# System Bus
SYSTEM_BUS_WIDTH = 20
SYSTEM_BUS_ADDRESS_X = (
    PROCESSOR_X + PROCESSOR_WIDTH + MEMORY_X
) / 2 - SYSTEM_BUS_WIDTH * 3 / 2
SYSTEM_BUS_DATA_X = SYSTEM_BUS_ADDRESS_X + SYSTEM_BUS_WIDTH + 10
SYSTEM_BUS_CONTROL_X = SYSTEM_BUS_DATA_X + SYSTEM_BUS_WIDTH + 10
SYSTEM_BUS_HEIGHT = PROCESSOR_HEIGHT
SYSTEM_BUS_Y = PROCESSOR_Y
