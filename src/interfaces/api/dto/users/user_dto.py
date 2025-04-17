from litestar.dto import DTOConfig

from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import CreateUserSchema, ReadUserSchema, UpdateUserSchema


class CreateUserDTO(BasePydanticDTO[CreateUserSchema]):
    __config__ = DTOConfig(
        exclude={"id", "created_at", "is_verified", "is_active"},
    )


class UpdateUserDTO(UpdatePydanticDTO[UpdateUserSchema]):
    __config__ = DTOConfig(
        exclude={"id", "created_at", "is_verified", "is_active"},
    )


class ReadUserDTO(BasePydanticDTO[ReadUserSchema]):
    pass
