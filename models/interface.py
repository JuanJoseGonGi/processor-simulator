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

    def set_data(
        self, data: T | None = None, source_data_holder: DataHolder[T] | None = None
    ) -> None:
        if data is not None:
            self.bus.set_data(data)
            return

        if source_data_holder is not None:
            data = source_data_holder.get_data()
            self.bus.set_data(data)

    def get_data(self) -> T | None:
        return self.bus.get_data()
