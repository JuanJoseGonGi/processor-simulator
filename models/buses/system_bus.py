import pygame as pg

from models.buses.bus import Bus
from models.control.control_unit import ControlSignal

import constants


class SystemBus:
    def __init__(self):
        self.address_bus = Bus[str](
            constants.SYSTEM_BUS_WIDTH,
            [
                (constants.SYSTEM_BUS_ADDRESS_X, constants.SYSTEM_BUS_Y),
                (
                    constants.SYSTEM_BUS_ADDRESS_X,
                    constants.SYSTEM_BUS_Y + constants.SYSTEM_BUS_HEIGHT,
                ),
            ],
        )

        self.data_bus = Bus[int | str](
            constants.SYSTEM_BUS_WIDTH,
            [
                (constants.SYSTEM_BUS_DATA_X, constants.SYSTEM_BUS_Y),
                (
                    constants.SYSTEM_BUS_DATA_X,
                    constants.SYSTEM_BUS_Y + constants.SYSTEM_BUS_HEIGHT,
                ),
            ],
        )

        self.control_bus = Bus[ControlSignal](
            constants.SYSTEM_BUS_WIDTH,
            [
                (constants.SYSTEM_BUS_CONTROL_X, constants.SYSTEM_BUS_Y),
                (
                    constants.SYSTEM_BUS_CONTROL_X,
                    constants.SYSTEM_BUS_Y + constants.SYSTEM_BUS_HEIGHT,
                ),
            ],
        )

    def draw(self, screen: pg.surface.Surface):
        self.address_bus.draw(screen)
        self.data_bus.draw(screen)
        self.control_bus.draw(screen)
