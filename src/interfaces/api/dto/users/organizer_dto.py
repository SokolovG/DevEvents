from litestar.dto import DTOConfig

from src.interfaces.api.dto.base_dto import BasePydanticDTO, UpdatePydanticDTO
from src.interfaces.api.schemas import OrganizerSchema, ReadOrganizerSchema


class ReadOrganizerDTO(BasePydanticDTO[ReadOrganizerSchema]):
    pass


class CreateOrganizerDTO(BasePydanticDTO[OrganizerSchema]):
    __config__ = DTOConfig(exclude={"id", "user_id", "verified", "created_at", "rating"})


class UpdateOrganizerDTO(UpdatePydanticDTO[OrganizerSchema]):
    __config__ = DTOConfig(
        exclude={"id", "user_id", "verified", "created_at", "rating"},
    )
