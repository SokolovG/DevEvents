from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import LocationSchema, ReadLocationSchema


class CreateLocationDTO(BasePydanticDTO[LocationSchema]):
    pass


class UpdateLocationDTO(UpdatePydanticDTO[LocationSchema]):
    pass


class ReadLocationDTO(BasePydanticDTO[ReadLocationSchema]):
    pass
