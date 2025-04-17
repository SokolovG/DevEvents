from typing import Annotated

from pydantic import Field

from src.infrastructure.database.constants import (
    MAX_BASIC_LENGTH,
    MAX_DESCRIPTION_LENGTH,
    MIN_BASIC_LENGTH,
    PASSWORD_MIN_LENGTH,
)

BasicString = Annotated[
    str,
    Field(
        min_length=MIN_BASIC_LENGTH,
        max_length=MAX_BASIC_LENGTH,
        description="Standard text field with length validation",
    ),
]

DescriptionField = Annotated[
    str,
    Field(
        min_length=MIN_BASIC_LENGTH,
        max_length=MAX_DESCRIPTION_LENGTH,
        description="Extended text field for detailed content",
    ),
]

PasswordString = Annotated[
    str,
    Field(
        min_length=PASSWORD_MIN_LENGTH,
        max_length=MAX_BASIC_LENGTH,
        description="Password field with length validation",
    ),
]
