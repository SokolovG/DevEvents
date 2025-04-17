from datetime import datetime

from src.interfaces.api.schemas.base_dto import BasePydanticModel
from src.interfaces.api.schemas.custom_types import BasicString


class LocationSchema(BasePydanticModel):
    """Base Pydantic schema for Location model.

    This class serves as a foundation for all Location-related schemas.
    All derived schemas inherit these base fields:
    - name: Name of the location/venue
    - address: Street address
    - city: City name
    - country: Country name

    Used as a parent class for:
    - LocationRead: For retrieving location data
    - LocationCreate: For creating new locations
    - LocationUpdate: For updating existing locations
    """

    name: BasicString
    address: BasicString
    city: BasicString
    country: BasicString


class ReadLocationSchema(LocationSchema):
    """Schema for reading location data."""

    id: int
    created_at: datetime
