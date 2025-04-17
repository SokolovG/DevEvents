from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import (
    Base,
    BasicNullInteger,
    BasicNullString,
    BasicString,
    BoolFalse,
    DescriptionString,
    IndexedString,
)
from src.infrastructure.database.models.enums import Currency, EventFormat, EventStatus

if TYPE_CHECKING:
    from .category_model import Category
    from .location_model import Location
    from .organizer_model import Organizer
    from .profile_model import Profile


class Event(Base):
    """Model for events.

    Main event model containing all event-related information.
    """

    __tablename__ = "events"

    # Basic fields
    name: Mapped[IndexedString]
    description: Mapped[DescriptionString]

    # Foreign Keys
    organizer_id: Mapped[int] = mapped_column(ForeignKey("organizers.id", use_alter=True))
    location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id", use_alter=True), nullable=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", use_alter=True),
    )

    # Relationships
    organizers: Mapped[list["Organizer"]] = relationship(
        "Organizer",
        secondary="event_organizers",
        back_populates="events",
        lazy="select",
    )
    location: Mapped["Location"] = relationship("Location", back_populates="events")
    category: Mapped["Category"] = relationship("Category", back_populates="events")
    registered_profiles: Mapped[list["Profile"]] = relationship(
        "Profile", secondary="event_registrations", back_populates="registered_events"
    )

    # Enum fields
    format: Mapped[EventFormat] = mapped_column(
        default=EventFormat.OFFLINE,
    )
    status: Mapped[EventStatus] = mapped_column(default=EventStatus.PLANNED)
    currency: Mapped[Currency] = mapped_column(
        default=Currency.USD,
    )

    # Boolean fields
    is_published: Mapped[BoolFalse]
    is_online: Mapped[BoolFalse]
    is_verify: Mapped[BoolFalse]

    # Date fields
    pub_date: Mapped[datetime]
    event_start_date: Mapped[datetime]
    event_end_date: Mapped[datetime]
    registration_deadline: Mapped[datetime] = mapped_column(nullable=True)

    # String fields
    meeting_link: Mapped[BasicNullString]
    timezone: Mapped[BasicString] = mapped_column(default="UTC")

    # Numeric fields
    max_participants: Mapped[BasicNullInteger]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    current_participants: Mapped[BasicNullInteger]
