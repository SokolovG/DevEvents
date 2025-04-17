from typing import TypeVar

from litestar.dto import DTOConfig
from litestar.plugins.pydantic.dto import PydanticDTO

T = TypeVar("T")


class BasePydanticDTO(PydanticDTO[T]):
    pass


class UpdatePydanticDTO(PydanticDTO[T]):
    config = DTOConfig(partial=True)
