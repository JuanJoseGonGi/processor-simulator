import pygame as pg

from models.processor import Processor
from models.memory import Memory
from models.io_device import IODevice
from models.bus import Bus


class Computer:
    def __init__(self) -> None:
        self.processor = Processor()
        self.main_memory = Memory()
        self.io_devices = {
            "keyboard": IODevice(),
        }

        self.system_bus = [Bus([]), Bus([]), Bus([])]

    def update(self) -> None:
        self.processor.update(self.system_bus)
        self.main_memory.update(self.system_bus)

        for io_device in self.io_devices.values():
            io_device.update(self.system_bus)

    def draw(self, screen: pg.Surface) -> None:
        self.processor.draw(screen)
        self.main_memory.draw(screen)

        for io_device in self.io_devices.values():
            io_device.draw(screen)
