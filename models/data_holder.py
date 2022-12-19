from __future__ import annotations
from typing import Generic, TypeVar
from enum import Enum


T = TypeVar("T")


class DataHolderStatus(Enum):
    IDLE = 0
    BUSY = 1


class DataHolder(Generic[T]):
    def __init__(self, data: T | None):
        self.data = data
        self.initial_data = data
        self.status = DataHolderStatus.IDLE

    def get_data(self) -> T | None:
        return self.data

    def set_data(self, data: T | None) -> None:
        if data is not None:
            self.data = data
            self.status = DataHolderStatus.BUSY

            return

        self.data = None
        self.status = DataHolderStatus.IDLE
