import random
from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Event, EventRegistration, Profile
from src.infrastructure.database.seeders.base_seeder import BaseSeeder


class RelationshipSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting relationships seeding...")
            await self.clear_table(EventRegistration)

            profiles = (await self.session.execute(select(Profile))).scalars().all()

            events = (await self.session.execute(select(Event))).scalars().all()

            for profile in profiles:
                num_events = random.randint(1, 3)  # noqa
                selected_events = random.sample(events, num_events)
                profile.registered_events.extend(selected_events)

            await self.session.commit()
            self.log("Relationships created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating relationships: {str(e)}", level="error")
            await self.session.rollback()
