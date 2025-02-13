from __future__ import annotations

from typing import TYPE_CHECKING

from litestar.plugins.sqlalchemy import repository

from backend.app.infrastructure.models import Event

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class EventRepository(repository.SQLAlchemyAsyncRepository[Event]):
    """Repository for Event model."""
    model_type = Event


async def provide_event_repo(db_session: AsyncSession) -> EventRepository:
    """Provide Event repository instance.

    Args:
       db_session: Async database session
    Returns:
       EventRepository instance
    """
    return EventRepository(session=db_session)
