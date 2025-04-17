from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database.base import Base
from src.infrastructure.database.models.enums import ParticipantStatus


class EventRegistration(Base):
    """Model representing registration of a profile for an event.

    This is a many-to-many relationship table between profiles and events,
    tracking the registration status of each participant.

    Attributes:
        profile_id: ID of the registered profile
        event_id: ID of the event
        status: Current status of the registration

    """

    __tablename__ = "event_registrations"

    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", use_alter=True, ondelete="CASCADE"),
        primary_key=True,
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", use_alter=True, ondelete="CASCADE"),
        primary_key=True,
    )
    status: Mapped[ParticipantStatus] = mapped_column(default=ParticipantStatus.REGISTERED)


class EventOrganizers(Base):
    """Model representing relationship between events and their organizer_model.py.

    This is a many-to-many relationship table between events and organizer_model.py.

    Attributes:
        organizer_id: ID of the organizer
        event_id: ID of the event

    """

    __tablename__ = "event_organizers"

    organizer_id: Mapped[int] = mapped_column(
        ForeignKey("organizers.id", use_alter=True, ondelete="CASCADE"),
        primary_key=True,
    )
    event_id: Mapped[int] = mapped_column(
        ForeignKey("events.id", use_alter=True, ondelete="CASCADE"),
        primary_key=True,
    )
