from models.data_holder import DataHolder
from models.buses.bus import Bus

from typing import TypeVar

T = TypeVar("T")


class Interface(DataHolder[T]):
    def __init__(
        self,
        bus: Bus[T],
    ):
        self.bus = bus

    def set_data(self, data: T | None) -> None:
        self.bus.set_data(data)
        return

    def get_data(self) -> T | None:
        return self.bus.get_data()
