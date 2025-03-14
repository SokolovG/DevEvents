from datetime import datetime
from typing import Optional

from backend.src.interfaces.api.schemas.base import BaseModel
from backend.src.interfaces.api.schemas.types import BasicString


class LocationBase(BaseModel):
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


class LocationRead(LocationBase):
    """Schema for reading location data."""

    id: int
    created_at: datetime


class LocationCreate(LocationBase):
    """Schema for creating new locations.

    Inherits all fields from LocationBase without modifications.
    """


class LocationUpdate(LocationBase):
    """Schema for updating existing locations.

    Notes:
    - All fields are optional to allow partial updates
    - Only changed fields need to be included in request
    - Inheritance ensures consistent validation rules
    """

    name: Optional[BasicString] = None
    address: Optional[BasicString] = None
    city: Optional[BasicString] = None
    country: Optional[BasicString] = None
