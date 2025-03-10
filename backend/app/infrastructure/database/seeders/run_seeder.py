import asyncio

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from backend.app.infrastructure.database.seeders.entities import (
    CategorySeeder,
    LocationSeeder,
    UserSeeder,
    ProfileSeeder,
    EventSeeder,
    RelationshipSeeder,
    OrganizerSeeder,
)
from backend.app.core.config.settings import settings


async def create_session() -> AsyncSession:
    """Create session for test data db."""
    engine = create_async_engine(settings.database_url, echo=False)

    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    return async_session()


async def run() -> None:
    """Run all seeders."""
    async with await create_session() as session:
        seeders = [
            CategorySeeder(session=session),
            LocationSeeder(session=session),
            UserSeeder(session=session),
            ProfileSeeder(session=session),
            EventSeeder(session=session),
            RelationshipSeeder(session=session),
            OrganizerSeeder(session=session),
        ]
        for seeder in seeders:
            await seeder.run()


if __name__ == "__main__":
    # To run - python -m backend.app.infrastructure.database.seeders.run_seeder
    asyncio.run(run())
