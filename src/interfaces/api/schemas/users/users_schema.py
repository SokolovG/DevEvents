from datetime import datetime

from pydantic import EmailStr, ValidationInfo, field_validator

from src.interfaces.api.schemas.base_dto import BasePydanticModel
from src.interfaces.api.schemas.custom_types import BasicString, PasswordString


class UserSchema(BasePydanticModel):
    """Base Pydantic schema for User model.

    This class serves as a foundation for all User-related schemas.
    All derived schemas inherit these base fields:
    Used as a parent class for:
    - UserRead: For retrieving users data
    - UserCreate: For creating new users
    - UserUpdate: For updating existing users
    """

    username: BasicString
    email: EmailStr


class ReadUserSchema(UserSchema):
    """Schema for reading user data."""

    id: int
    created_at: datetime
    is_verified: bool
    is_active: bool


class CreateUserSchema(UserSchema):
    """Schema for creating new user.

    Extends UserBase with additional validation:
    - Passwords match validation

    Validation rules:
    1. The password must coincide
    """

    password: PasswordString
    password_confirm: PasswordString

    @field_validator("password_confirm")
    def passwords_match(self, value: str, info: ValidationInfo) -> str:
        """Validate that password and password_confirm match.

        Args:
            value: password_confirm
            info: данные
        Returns:
            password_confirm if validated

        """
        data = info.data
        if "password" in data and value != data["password"]:
            raise ValueError("Passwords do not match.")
        return value


class UpdateUserSchema(BasePydanticModel):
    """Schema for updating existing user.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Validation from base class still applies to provided fields

    """

    username: BasicString | None = None
    email: BasicString | None = None
    password: PasswordString | None = None
    password_confirm: PasswordString | None = None
