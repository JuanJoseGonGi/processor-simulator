import pygame as pg

from models.processor import Processor
from models.memory import Memory
from models.io_device import IODevice


class Computer:
    def __init__(self) -> None:
        self.processor = Processor()
        self.main_memory = Memory()
        self.io_devices = {
            "keyboard": IODevice(),
        }

    def update(self) -> None:
        self.processor.update()
        self.main_memory.update()

        for io_device in self.io_devices.values():
            io_device.update()

    def draw(self, screen: pg.Surface) -> None:
        self.processor.draw(screen)
        self.main_memory.draw(screen)

        for io_device in self.io_devices.values():
            io_device.draw(screen)
