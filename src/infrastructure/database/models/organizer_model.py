from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.base import (
    Base,
    BasicNullString,
    BasicString,
    BoolFalse,
    DescriptionString,
)

if TYPE_CHECKING:
    from .event_model import Event
    from .user_model import User


class Organizer(Base):
    """Model for event organizers.

    Represents organizations or individuals who can create and manage events.
    """

    __tablename__ = "organizers"

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", use_alter=True, ondelete="CASCADE"), unique=True
    )

    # Relationships
    events: Mapped[list["Event"]] = relationship(
        "Event",
        secondary="event_organizers",
        lazy="selectin",
        back_populates="organizers",
    )
    user: Mapped["User"] = relationship(
        "User",
        lazy="joined",
        back_populates="organizer_profile",
        uselist=False,
    )

    # Boolean fields
    verified: Mapped[BoolFalse]

    # String fields
    website: Mapped[BasicNullString]
    contact: Mapped[BasicNullString]
    name: Mapped[BasicString]
    description: Mapped[DescriptionString]
    logo_url: Mapped[BasicNullString] = mapped_column(unique=True)

    # Numeric fields
    rating: Mapped[float] = mapped_column(
        Numeric(3, 2), CheckConstraint("rating >= 0 AND rating <= 5"), default=0
    )
