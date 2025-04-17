from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import ProfileSchema, ReadProfileSchema


class ReadProfileDTO(BasePydanticDTO[ReadProfileSchema]):
    pass


class CreateProfileDTO(BasePydanticDTO[ProfileSchema]):
    pass


class UpdateProfileDTO(UpdatePydanticDTO[ProfileSchema]):
    pass
