from datetime import datetime
from decimal import Decimal

from pydantic import HttpUrl, ValidationInfo, field_validator

from src.infrastructure.database.models.enums import Currency, EventFormat, EventStatus
from src.interfaces.api.schemas.base_dto import BasePydanticModel
from src.interfaces.api.schemas.custom_types import BasicString, DescriptionField


class EventSchema(BasePydanticModel):
    """Base Pydantic schema for the Event model.

    This class serves as a foundation for all Event-related schemas.
    All derived schemas inherit these base fields.

    Used as a parent class for:
    - EventRead: For retrieving events data
    - EventCreate: For creating new event
    - EventUpdate: For updating existing events
    """

    # Basic event information
    name: BasicString
    description: DescriptionField

    # Date and time fields
    event_start_date: datetime
    event_end_date: datetime
    registration_deadline: datetime
    timezone: BasicString

    # Event configuration
    format: EventFormat
    status: EventStatus
    meeting_link: HttpUrl | None = None

    # Participation details
    max_participants: int | None = None
    current_participants: int | None = 0

    # Financial information
    price: Decimal | None = None
    currency: Currency = Currency.USD

    @field_validator("event_end_date")
    def validate_end_date(self, end_date: datetime, info: ValidationInfo) -> datetime:
        """Validate that event end date is after start date.

        Args:
            end_date: The event's end date
            info: Validation context containing all fields

        Returns:
            datetime: Validated end date

        Raises:
            ValueError: If end date is not after start date

        """
        data = info.data
        start_date = data.get("event_start_date")
        if start_date and end_date <= start_date:
            raise ValueError("End date must be after start date.")
        return end_date

    @field_validator("registration_deadline")
    def deadline_before_start(self, deadline: datetime, info: ValidationInfo) -> datetime:
        """Validate that registration deadline is before event start.

        Args:
            deadline: The registration deadline
            info: Validation context containing all fields

        Returns:
            datetime: Validated deadline

        Raises:
            ValueError: If deadline is not before event start

        """
        data = info.data
        start_date = data.get("event_start_date")
        if start_date and deadline >= start_date:
            raise ValueError("Registration deadline must be before event start.")
        return deadline

    @field_validator("current_participants")
    def validate_number_of_participants(self, current: int, info: ValidationInfo) -> int:
        """Validate that current participants don't exceed maximum.

        Args:
            current: Number of current participants
            info: Validation context containing all fields

        Returns:
            int: Validated number of participants

        Raises:
            ValueError: If current participants exceed maximum

        """
        data = info.data
        max_number = data.get("max_participants")
        if max_number and current > max_number:
            raise ValueError("Current participants cannot exceed maximum.")
        return current

    @field_validator("price")
    def validate_price_currency(
        self, price: Decimal | None, info: ValidationInfo
    ) -> Decimal | None:
        """Validate price and currency relationship.

        Args:
            price: Event price
            info: Validation context containing all fields

        Returns:
            Optional[Decimal]: Validated price or None

        Raises:
            ValueError: If currency is missing when price is set

        """
        if price is None:
            return None

        currency = info.data.get("currency", Currency.USD)

        if not currency:
            raise ValueError("Currency must be specified when price is set")

        return price


class ReadEventSchema(EventSchema):
    """Schema for reading event data.

    Extends EventBase with additional fields needed for data retrieval.
    """

    # Identification fields
    id: int
    location_id: int | None
    category_id: int
    organizer_id: int

    # Status flags
    is_published: bool
    is_online: bool
    is_verify: bool

    # Publication information
    pub_date: datetime


class CreateEventSchema(EventSchema):
    """Schema for creating new events.

    Extends EventBase with fields required for event creation.
    """

    # Relationship fields
    location_id: int | None = None
    category_id: int | None = None
    organizer_id: int | None = None


class UpdateEventSchema(BasePydanticModel):
    """Schema for updating existing event.

    Notes:
        - All fields are optional to allow partial updates
        - Only changed fields need to be included in request
        - Validation from base class still applies to provided fields

    """

    # Basic information
    name: BasicString | None = None
    description: DescriptionField | None = None

    # Relationships
    organizer_id: int | None = None
    location_id: int | None = None
    category_id: int | None = None

    # Classification
    format: EventFormat | None = EventFormat.OFFLINE
    status: EventStatus | None = EventStatus.PLANNED
    currency: Currency | None = Currency.USD

    # Status flags
    is_published: bool | None = None
    is_online: bool | None = None
    is_verify: bool | None = None

    # Dates
    pub_date: datetime | None = None
    event_start_date: datetime | None = None
    event_end_date: datetime | None = None
    registration_deadline: datetime | None = None

    # Additional details
    meeting_link: HttpUrl | None = None
    timezone: BasicString | None = None
    max_participants: int | None = None
    price: Decimal | None = None
    current_participants: int | None = None
