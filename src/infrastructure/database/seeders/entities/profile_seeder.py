import random
from typing import override

from sqlalchemy import select

from src.infrastructure.database.models import Category, Profile
from src.infrastructure.database.models.enums import Gender
from src.infrastructure.database.seeders.base_seeder import BaseSeeder
from src.infrastructure.database.seeders.constants import NUM_TEST_DATA


class ProfileSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting profiles seeding...")
            await self.clear_table(Profile)

            query = select(Category)
            res = await self.session.execute(query)
            categories = res.scalars().all()
            category_names = [category.name for category in categories]

            for index in range(NUM_TEST_DATA):
                first_name = self.faker.first_name()
                random_category = random.choice(category_names)  # noqa
                profile = Profile(
                    user_id=index,
                    first_name=first_name,
                    last_name=self.faker.last_name(),
                    avatar_url=self.faker.image_url(),
                    interested_technologies=random_category,
                    location=self.faker.country(),
                    birth_date=self.faker.date_of_birth(),
                    gender=random.choice(list(Gender)),  # noqa
                )

                self.log(f"Created profile - {first_name}")
                self.session.add(profile)

            await self.session.commit()
            self.log("Profiles created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating profiles: {str(e)}", level="error")
            await self.session.rollback()
