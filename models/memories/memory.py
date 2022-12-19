import pygame as pg

import constants

from models.memories.memory_cell import MemoryCell
from models.memories.memory_mode import MemoryMode
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
        self.control = MemoryMode.IDLE

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

    def set_address(self) -> None:
        received_address = self.address_iface.get_data()
        if received_address is None:
            self.address = ""
            return

        self.address = received_address

    def get_data(self) -> Any:
        return self.data[self.address]

    def set_data(self) -> None:
        if self.address == "":
            raise Exception("Memory address not specified")

        if self.address not in self.data:
            raise Exception(f"Memory address {self.address} not found")

        received_data = self.data_iface.get_data()
        self.data[self.address].set_data(received_data)

        return

    def set_control(self) -> None:
        received_control = self.control_iface.get_data()
        if received_control is None:
            self.control = MemoryMode.IDLE
            return

        self.control = received_control

    def update(self):
        self.set_control()
        if self.control == MemoryMode.IDLE:
            return

        self.set_address()
        if self.address == "":
            return

        if self.control == MemoryMode.READ:
            self.data_iface.set_data(self.get_data())
            return

        if self.control == MemoryMode.WRITE:
            self.set_data()
            return

    def draw(self, screen: pg.surface.Surface):
        pg.draw.rect(screen, constants.PINK, self.rect)

        for cell in self.data.values():
            cell.draw(screen)
