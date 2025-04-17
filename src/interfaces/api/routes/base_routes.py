from litestar import Router

from src.interfaces.api.controllers.event_controller import EventController

event_router = Router(path="/api/v1", route_handlers=[EventController])
