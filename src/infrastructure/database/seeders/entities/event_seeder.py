from datetime import timedelta
from typing import override

from src.infrastructure.database.models.enums import Currency, EventFormat, EventStatus
from src.infrastructure.database.models.event_model import Event
from src.infrastructure.database.seeders.base_seeder import BaseSeeder
from src.infrastructure.database.seeders.constants import NUM_TEST_DATA


class EventSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting events seeding...")
            await self.clear_table(Event)

            for _ in range(NUM_TEST_DATA):
                event_name = f"{self.faker.bs().title()} {self.faker.company_suffix()} Conference"
                is_online = self.faker.boolean()
                pub_date = self.faker.date_between(start_date="-30d", end_date="now")
                event_start = self.faker.date_time_between(
                    start_date=pub_date, end_date=pub_date + timedelta(days=90)
                )
                event_end_date = self.faker.date_time_between(
                    start_date=event_start, end_date=event_start + timedelta(days=7)
                )
                registration_deadline = self.faker.date_time_between(
                    start_date=pub_date, end_date=event_start
                )
                current_participants = self.faker.random_int(min=1, max=250)
                price = (
                    self.faker.pydecimal(left_digits=4, right_digits=2, positive=True)
                    if self.faker.boolean()
                    else None
                )

                event = Event(
                    name=event_name,
                    description=self.faker.paragraph(nb_sentences=4),
                    # Foreign Keys
                    organizer_id=self.faker.random_int(min=1, max=10),
                    location_id=self.faker.random_int(min=1, max=10),
                    category_id=self.faker.random_int(min=1, max=10),
                    # Enum fields
                    format=self.faker.random_element(EventFormat),
                    status=self.faker.random_element(EventStatus),
                    currency=(
                        self.faker.random_element(Currency) if price is not None else Currency.USD
                    ),
                    # Boolean fields
                    is_published=self.faker.boolean(),
                    is_online=is_online,
                    is_verify=self.faker.boolean(),
                    # Date fields (уже есть)
                    pub_date=pub_date,
                    event_start_date=event_start,
                    event_end_date=event_end_date,
                    registration_deadline=registration_deadline,
                    # String fields
                    meeting_link=self.faker.url() if is_online else None,
                    timezone=self.faker.timezone(),
                    # Numeric fields
                    current_participants=current_participants,
                    max_participants=self.faker.random_int(min=current_participants, max=500),
                    price=price,
                )

                self.session.add(event)
                self.log(f"Created event - {event_name}")

            await self.session.commit()
            self.log("Events created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating events: {str(e)}", level="error")
            await self.session.rollback()
