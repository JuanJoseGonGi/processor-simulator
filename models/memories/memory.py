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
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

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
        for i in range(32):
            address = f"{i:02d}"
            x = constants.MEMORY_CELL_X + (i // 8) * (
                constants.MEMORY_CELL_WIDTH + constants.MEMORY_CELL_GAP_X
            )
            y = constants.MEMORY_CELL_Y + (i % 8) * (
                constants.MEMORY_CELL_HEIGHT + constants.MEMORY_CELL_GAP_Y
            )
            self.data[address] = MemoryCell(x, y, address, self.rect)

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
        pg.draw.rect(screen, constants.GREEN, self.rect)

        for cell in self.data.values():
            cell.draw(screen)
