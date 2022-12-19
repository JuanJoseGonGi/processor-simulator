from models.buses.bus import Bus
import pygame as pg

from models.processor import Processor
from models.memories.memory import Memory
from models.io_device import IODevice
from models.buses.system_bus import SystemBus
import constants as cons
from typing import List, Tuple


class Computer:
    def __init__(self) -> None:
        self.system_bus = SystemBus()

        self.processor = Processor(self.system_bus)
        self.main_memory = Memory(self.system_bus)
        self.io_devices = {
            "keyboard": IODevice(),
        }

        #Components (UC, MAR, MBR) comunication to system bus
        
        self.transition_processor_to_address_bus = Bus(int(cons.TRANSITION_PROCESSOR_TO_ADDRESS_BUS_WIDTH), 
            [(cons.TRANSITION_PROCESSOR_TO_ADDRESS_BUS_X, cons.TRANSITION_PROCESSOR_TO_ADDRESS_BUS_Y), 
            (cons.TRANSITION_PROCESSOR_BUS_TO,cons.TRANSITION_PROCESSOR_TO_ADDRESS_BUS_Y)])

        self.transition_processor_to_data_bus = Bus(int(cons.TRANSITION_PROCESSOR_TO_DATA_BUS_WIDTH), 
            [(cons.TRANSITION_PROCESSOR_TO_DATA_BUS_X, cons.TRANSITION_PROCESSOR_TO_DATA_BUS_Y), 
            (cons.TRANSITION_PROCESSOR_BUS_DATA_TO, cons.TRANSITION_PROCESSOR_TO_DATA_BUS_Y)])

        self.transition_processor_to_control_bus = Bus(int(cons.TRANSITION_PROCESSOR_TO_CONTROL_BUS_WIDTH), 
            [(cons.TRANSITION_PROCESSOR_TO_CONTROL_BUS_X, cons.TRANSITION_PROCESSOR_TO_CONTROL_BUS_Y), 
            (cons.TRANSITION_PROCESSOR_BUS_CONTROL_TO, cons.TRANSITION_PROCESSOR_TO_CONTROL_BUS_Y)])


        #System bus comunication to memory

        self.transition_address_bus_to_memory = Bus(int(cons.TRANSITION_PROCESSOR_TO_CONTROL_BUS_WIDTH),
            [(cons.TRANSITION_ADDRESS_BUS_TO_MEMORY_X, cons.TRANSITION_ADDRESS_BUS_TO_MEMORY_Y),
            (cons.TRANSITION_ADDRESS_BUS_TO_MEMORY, cons.TRANSITION_ADDRESS_BUS_TO_MEMORY_Y)])

        self.transition_data_bus_to_memory = Bus(int(cons.TRANSITION_DATA_BUS_TO_MEMORY_WIDTH),
            [(cons.TRANSITION_DATA_BUS_TO_MEMORY_X, cons.TRANSITION_DATA_BUS_TO_MEMORY_Y),
            (cons.TRANSITION_DATA_BUS_TO_MEMORY, cons.TRANSITION_DATA_BUS_TO_MEMORY_Y)])

        self.transition_control_bus_to_memory = Bus(int(cons.TRANSITION_CONTROL_BUS_TO_MEMORY_WIDTH),
            [(cons.TRANSITION_CONTROL_BUS_TO_MEMORY_X, cons.TRANSITION_CONTROL_BUS_TO_MEMORY_Y),
            (cons.TRANSITION_CONTROL_BUS_TO_MEMORY, cons.TRANSITION_CONTROL_BUS_TO_MEMORY_Y)])    

        

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
        self.transition_processor_to_address_bus.draw(screen)
        self.transition_processor_to_data_bus.draw(screen)
        self.transition_processor_to_control_bus.draw(screen)
        self.transition_address_bus_to_memory.draw(screen)
        self.transition_data_bus_to_memory.draw(screen)
        self.transition_control_bus_to_memory.draw(screen)