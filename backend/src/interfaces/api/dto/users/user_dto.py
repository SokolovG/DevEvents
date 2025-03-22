from backend.src.interfaces.api.dto.base_dto import BasePydanticDTO
from backend.src.interfaces.api.schemas import UserCreate, UserRead, UserUpdate


class UserCreateDTO(BasePydanticDTO[UserCreate]):
    pass

class UserUpdateDTO(BasePydanticDTO[UserUpdate]):
    pass

class UserReadDTO(BasePydanticDTO[UserRead]):
    pass

