import asyncio

from src.infrastructure.database.config import get_sqlalchemy_config
from src.infrastructure.database.seeders.entities import (
    CategorySeeder,
    EventSeeder,
    LocationSeeder,
    OrganizerSeeder,
    ProfileSeeder,
    RelationshipSeeder,
    UserSeeder,
)

sqlalchemy_config = get_sqlalchemy_config()


async def run() -> None:
    """Run all seeders."""
    session_maker = sqlalchemy_config.create_session_maker()
    async with session_maker() as session:
        seeders = [
            CategorySeeder(session=session),
            LocationSeeder(session=session),
            UserSeeder(session=session),
            ProfileSeeder(session=session),
            OrganizerSeeder(session=session),
            EventSeeder(session=session),
            RelationshipSeeder(session=session),
        ]
        for seeder in seeders:
            await seeder.run()


if __name__ == "__main__":
    asyncio.run(run())
