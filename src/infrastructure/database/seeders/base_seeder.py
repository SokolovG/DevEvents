import logging
import sys
from abc import ABC, abstractmethod

from colorama import Fore, Style, init
from faker import Faker
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

# Init for colorama
init()


class BaseSeeder(ABC):
    """Base class seeder, defines logging and faker."""

    def __init__(self, session: AsyncSession) -> None:
        """Initialize seeder with database session, faker instance and logger."""
        self.session = session
        self.faker = Faker("en-US")
        self.logger = self._setup_logger()

    @abstractmethod
    async def run(self) -> None:
        """Execute seeding process.Must be implemented by derived classes."""

    async def clear_table(self, model: type[DeclarativeBase]) -> None:
        """Докстринг."""
        await self.session.execute(delete(model))
        await self.session.commit()
        self.log(f"Cleared {model.__tablename__}")

    def _setup_logger(self) -> logging.Logger:
        """Create and configure logger instance for the seeder class."""
        logger = logging.getLogger(self.__class__.__name__)

        logger.setLevel(logging.INFO)

        if logger.handlers:
            logger.handlers.clear()

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            f"{Fore.GREEN}%(name)s{Style.RESET_ALL} - %(message)s",
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

        return logger

    def log(self, message: str, level: str | None = "info") -> None:
        """Log messages with specified level and colors."""
        if level == "info":
            message = f"{Fore.WHITE}{message}{Style.RESET_ALL}"
            self.logger.info(message)
        elif level == "error":
            message = f"{Fore.RED}{message}{Style.RESET_ALL}"
            self.logger.error(message)
        elif level == "warning":
            message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
            self.logger.warning(message)
        elif level == "success":
            message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
            self.logger.info(message)
