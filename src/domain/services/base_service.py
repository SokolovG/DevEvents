from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseService(Generic[T], ABC):
    @abstractmethod
    async def get_by_id(self, inst_id: int) -> T | None:
        """Докстринг."""

    @abstractmethod
    async def get_all(self) -> list[T]:
        """Докстринг."""

    @abstractmethod
    async def create(self, data: dict) -> T:
        """Докстринг."""

    @abstractmethod
    async def update(self, inst_id: int, data: dict) -> T | None:
        """Докстринг."""

    @abstractmethod
    async def delete(self, inst_id: int) -> bool:
        """Докстринг."""
