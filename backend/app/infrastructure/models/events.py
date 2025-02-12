from decimal import Decimal

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    Table,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from backend.app.infrastructure.database.base import (
    Base,
    BasicNullInteger,
    BasicNullString,
    BasicString,
    BoolFalse,
    DescriptionString,
    IndexedString,
    IndexedUniqueString,
)
from backend.app.infrastructure.models.enums import (
    Currency,
    EventFormat,
    EventStatus,
)


class Location(Base):
    __tablename__ = 'locations'
    # String fields.
    name: Mapped[BasicString]
    address: Mapped[BasicString]
    city: Mapped[IndexedString]
    country: Mapped[IndexedString]
    # Relationships.
    events: Mapped["Event"] = relationship(
        'Event',
        back_populates='location',
        cascade='all, delete-orphan'
    )


class Category(Base):
    __tablename__ = 'categories'
    # String BasicString.
    name: Mapped[BasicString]
    slug: Mapped[IndexedUniqueString]
    description: Mapped[DescriptionString] = mapped_column(nullable=True)
    # Relationships.
    events = relationship('Event', back_populates='category')


class Event(Base):
    __tablename__ = 'events'
    name: Mapped[IndexedString]
    description: Mapped[DescriptionString]
    # Foreign Keys.
    organizer_id: Mapped[int] = mapped_column(
        ForeignKey('organizer.id', use_alter=True))
    location_id: Mapped[int] = mapped_column(
        ForeignKey('locations.id', use_alter=True),
        nullable=True
    )
    category_id: Mapped[int] = Column(
        ForeignKey('categories.id', use_alter=True),
    )
    # Relationships.
    organizer: Mapped["Organizer"] = relationship('Organizer', back_populates='authored_events')
    location: Mapped["Location"] = relationship('Location', back_populates='events')
    category: Mapped["Category"] = relationship('Category', back_populates='events')
    registered_profiles: Mapped[list["Profile"]] = relationship(
        "Profile",
        secondary='event_registrations',
        back_populates='registered_events'
    )
    # Enum fields
    format: Mapped[EventFormat] = mapped_column(
        default=EventFormat.OFFLINE,
    )
    status: Mapped[EventStatus] = mapped_column(
        default=EventStatus.PLANNED
    )
    currency: Mapped[Currency] = mapped_column(
        default=Currency.USD,
        nullable=True
    )
    # Boolean fields.
    is_published: Mapped[BoolFalse]
    is_online: Mapped[BoolFalse]
    is_verify: Mapped[BoolFalse]
    # Date fields.
    pub_date: Mapped[DateTime]
    event_start_date: Mapped[DateTime]
    event_end_date: Mapped[DateTime]
    registration_deadline: Mapped[DateTime] = mapped_column(nullable=True)
    # String fields.
    meeting_link: Mapped[BasicNullString]
    timezone: Mapped[BasicString] = mapped_column(default='UTC')
    # Numeric fields
    max_participants: Mapped[BasicNullInteger]
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=True)
    current_participants: Mapped[BasicNullInteger]


