from logging import Logger

from litestar import Controller, get

from src.infrastructure.dependencies.dependencies import event_dependencies
from src.infrastructure.repositories.event import EventRepository
from src.interfaces.api.dto import ReadEventDTO
from src.interfaces.api.schemas import ReadEventSchema


class EventController(Controller):
    """Basic event controller."""

    path = "/events"
    dependencies = event_dependencies

    @get(dto=ReadEventDTO)
    async def get_all_events(self, repo: EventRepository, logger: Logger) -> list[ReadEventSchema]:
        """Get all events."""
        logger.info("Get all events")
        events: list[ReadEventSchema] = await repo.list()
        return events

    @get("/{event_id:int}", dto=ReadEventDTO)
    async def get_event_by_pk(
        self, event_id: int, repo: EventRepository, logger: Logger
    ) -> ReadEventSchema:
        """Get event by_pk."""
        logger.info(f"Getting event with id {event_id}")
        event: ReadEventSchema = await repo.get_one_or_none(id=event_id)
        return event

    # register_for_event, search_events
