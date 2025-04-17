from logging import Logger, getLogger

from litestar.di import Provide

from src.infrastructure.repositories.event import provide_event_repo


async def provide_event_logger() -> Logger:
    """Provide a logger instance for the events module.

    Returns:
        Logger: Configured logger instance for the events module.

    """
    return getLogger("src.events")


event_dependencies = {"repo": Provide(provide_event_repo), "logger": Provide(provide_event_logger)}
