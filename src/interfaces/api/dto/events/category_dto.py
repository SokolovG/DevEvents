from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import CategorySchema, ReadCategorySchema


class CreateCategoryDTO(BasePydanticDTO[CategorySchema]):
    pass


class UpdateCategoryDTO(UpdatePydanticDTO[CategorySchema]):
    pass


class ReadCategoryDTO(BasePydanticDTO[ReadCategorySchema]):
    pass
