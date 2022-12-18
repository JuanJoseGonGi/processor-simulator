import pygame as pg

from models.processor import Processor
from models.memories.memory import Memory
from models.io_device import IODevice
from models.buses.system_bus import SystemBus


class Computer:
    def __init__(self) -> None:
        self.system_bus = SystemBus()

        self.processor = Processor(self.system_bus)
        self.main_memory = Memory(self.system_bus)
        self.io_devices = {
            "keyboard": IODevice(),
        }

    def update(self) -> None:
        self.processor.update()
        self.main_memory.update()

        for io_device in self.io_devices.values():
            io_device.update()

    def draw(self, screen: pg.surface.Surface) -> None:
        self.processor.draw(screen)
        self.main_memory.draw(screen)

        for io_device in self.io_devices.values():
            io_device.draw(screen)

        self.system_bus.draw(screen)
