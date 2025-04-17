from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import CreateEventSchema, ReadEventSchema, UpdateEventSchema


class CreateEventDTO(BasePydanticDTO[CreateEventSchema]):
    pass


class UpdateEventDTO(UpdatePydanticDTO[UpdateEventSchema]):
    pass


class ReadEventDTO(BasePydanticDTO[ReadEventSchema]):
    pass
