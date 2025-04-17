from sqlalchemy.orm import Mapped, relationship

from src.infrastructure.database.base import (
    Base,
    BasicString,
    DescriptionString,
    IndexedUniqueString,
)


class Category(Base):
    """Model for event categories.

    Represents different types/categories of events.
    """

    __tablename__ = "categories"

    # String fields
    name: Mapped[BasicString]
    slug: Mapped[IndexedUniqueString]
    description: Mapped[DescriptionString]

    # Relationships
    events = relationship("Event", back_populates="category")
