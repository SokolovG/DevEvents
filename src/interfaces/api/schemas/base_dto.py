from pydantic import BaseModel as _BaseModel
from pydantic import ConfigDict


class BasePydanticModel(_BaseModel):
    """Base abstract model.

    Contains model config for all children models:
    - from_attributes=True for ORM
    - str_strip_whitespace for clean data
    - validate_assignment for runtime validation
    """

    model_config = ConfigDict(
        from_attributes=True,
        use_enum_values=True,
        str_strip_whitespace=True,
        validate_assignment=True,
    )
