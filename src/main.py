import uvicorn
from litestar import Litestar
from litestar.config.cors import CORSConfig
from litestar.logging import LoggingConfig
from sqladmin import ModelView
from sqladmin_litestar_plugin import SQLAdminPlugin

from src.infrastructure.database.config import get_sqlalchemy_config, get_sqlalchemy_plugin
from src.infrastructure.database.models.event_model import Event
from src.interfaces.api.routes.base_routes import event_router
from src.interfaces.cli.commands import CLIPlugin

cors_config = CORSConfig(
    allow_origins=["http://localhost:5173"], allow_methods=["*"], allow_headers=["*"]
)


logging_config = LoggingConfig(
    root={"level": "INFO", "handlers": ["queue_listener"]},
    formatters={
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    loggers={
        "src.events": {"level": "DEBUG", "propagate": True},
        "src.users": {"level": "INFO", "propagate": True},
        "src.auth": {"level": "WARNING", "propagate": True},
    },
    log_exceptions="always",
)


class EventAdmin(ModelView, model=Event):  # type: ignore
    column_list = [Event.name, Event.price, Event.description]


sqlalchemy_plugin = get_sqlalchemy_plugin()
sqlalchemy_config = get_sqlalchemy_config()
admin = SQLAdminPlugin(engine=sqlalchemy_config.get_engine(), base_url="/admin", views=[EventAdmin])
app = Litestar(
    route_handlers=[event_router],
    plugins=[sqlalchemy_plugin, admin, CLIPlugin()],
    debug=True,
    cors_config=cors_config,
    logging_config=logging_config,
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
