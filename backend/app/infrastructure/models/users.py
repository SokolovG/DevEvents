"""Models for user management including basic users, organizers.py and profiles."""
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from backend.app.infrastructure.database.base import (
    Base,
    BasicString,
    BoolFalse,
    BoolTrue,
    IndexedUniqueString,
)

if TYPE_CHECKING:
    from .profiles import Profile
    from .organizers import Organizer


class User(Base):
    """Base user model containing authentication and core user data.

    This model represents the basic user entity with authentication details
    and links to specialized profiles.
    """

    __tablename__ = 'users'

    # String fields
    username: Mapped[IndexedUniqueString]
    email: Mapped[IndexedUniqueString]
    hashed_password: Mapped[BasicString]

    # Boolean fields
    is_verified: Mapped[BoolFalse]
    is_active: Mapped[BoolTrue]

    # Relationships
    profile: Mapped["Profile"] = relationship(
        'Profile',
        back_populates='user',
        uselist=False,
        lazy='joined',
        cascade='all, delete-orphan'
    )
    organizer_profile: Mapped["Organizer"] = relationship(
        'Organizer',
        back_populates='user',
        uselist=False,
        lazy='joined',
        cascade='all, delete-orphan'
    )