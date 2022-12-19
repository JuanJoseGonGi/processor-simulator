import pygame as pg

import constants

from models.data_holder import DataHolder
from models.memories.memory_cell import MemoryCell
from models.interface import Interface
from models.buses.system_bus import SystemBus

from typing import Any

class Memory:
    def __init__(self, system_bus: SystemBus):
        self.x = constants.MEMORY_X
        self.y = constants.MEMORY_Y
        self.width = constants.MEMORY_WIDTH
        self.height = constants.MEMORY_HEIGHT
        self.XhearBoard = constants.HEARBOARD_X
        self.yHearBoard = constants.HEARBOARD_Y
        self.widthHearBoard = constants.HEARDBOARD_WIDTH
        self.heightHearBoard = constants.HEARDBOARD_HEIGTH
        self.HearBoard = pg.Rect(self.XhearBoard , self.yHearBoard, self.widthHearBoard, self.heightHearBoard)
        self.HearBoard2 = pg.Rect(self.XhearBoard / 1.25, self.yHearBoard, self.widthHearBoard, self.heightHearBoard)
        self.rect = pg.Rect(self.x  / 1.25, self.y, self.width, self.height)
        self.rect2 = pg.Rect(self.x, self.y, self.width, self.height)

        self.address = ""
        self.control = ""

        self.address_iface = Interface(
            system_bus.address_bus,
        )
        self.data_iface = Interface(system_bus.data_bus)
        self.control_iface = Interface(
            system_bus.control_bus,
        )

        self.data: dict[str, MemoryCell] = {}        

        for i in range(16):
            address = f"{i:02d}"
            x = constants.MEMORY_CELL_X + (i // 8) * (
                constants.MEMORY_CELL_WIDTH + constants.MEMORY_CELL_GAP_X
            )
            y = constants.MEMORY_CELL_Y + (i % 8) * (
                constants.MEMORY_CELL_HEIGHT + constants.MEMORY_CELL_GAP_Y
            )
            self.data[address] = MemoryCell(x, y, address, self.rect)
    
        
        for i in range(16):
            address = f"{i+16:02d}"
            x = constants.MEMORY_CELL_X + (i // 8) * (
                constants.MEMORY_CELL_WIDTH + constants.MEMORY_CELL_GAP_X
            )
            y = constants.MEMORY_CELL_Y + (i % 8) * (
                constants.MEMORY_CELL_HEIGHT + constants.MEMORY_CELL_GAP_Y
            )
            self.data[address] = MemoryCell(x, y, address, self.rect2)

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str) -> None:
        self.address = address

    def reset_address(self) -> None:
        self.address = ""

    def get_data(self) -> Any:
        if self.address == "":
            raise Exception("Memory address not specified")

        if self.address not in self.data:
            raise Exception(f"Memory address {self.address} not found")

        return self.data[self.address]

    def set_data(
        self, data: Any = None, source_data_holder: DataHolder | None = None
    ) -> None:
        if self.address == "":
            raise Exception("Memory address not specified")

        if self.address not in self.data:
            raise Exception(f"Memory address {self.address} not found")

        if data is not None:
            self.data[self.address].set_data(data)
            return

        if source_data_holder is not None:
            self.data[self.address].set_data(source_data_holder=source_data_holder)

    def reset(self) -> None:
        for cell in self.data.values():
            cell.reset()

    def set_control(self, control: str) -> None:
        self.control = control

    def reset_control(self) -> None:
        self.control = ""

    def update(self):
        self.control_iface.get_data()

    def draw(self, screen: pg.surface.Surface): 

        pg.draw.rect(screen, constants.LIGTH_BLUE_2, self.rect)
        pg.draw.rect(screen, constants.LIGTH_BLUE, self.rect2)
        pg.draw.rect(screen, constants.LIGTH_BLUE, self.HearBoard)
        pg.draw.rect(screen, constants.LIGTH_BLUE_2, self.HearBoard2)

        text = pg.font.SysFont(constants.FONT, 20).render(
            "Program Memory", True, constants.BLACK    
        )

        rect = text.get_rect();
        rect.center = self.rect.center
        rect.top = self.rect.top - 20
        
        screen.blit(text, rect)

        text2 = pg.font.SysFont(constants.FONT, 20).render(
            "Data Memory", True, constants.BLACK
        )

        rect2 = text2.get_rect();
        rect2.center = self.rect2.center
        rect2.top = self.rect2.top - 20
        
        screen.blit(text2, rect2)

        for cell in self.data.values():
            cell.draw(screen)
