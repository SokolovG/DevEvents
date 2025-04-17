from typing import override

import bcrypt

from src.infrastructure.database.models import User
from src.infrastructure.database.seeders.base_seeder import BaseSeeder
from src.infrastructure.database.seeders.constants import NUM_TEST_DATA


class UserSeeder(BaseSeeder):
    @override
    async def run(self) -> None:
        try:
            self.log("Starting users seeding...")
            await self.clear_table(User)

            for _ in range(NUM_TEST_DATA):
                username = self.faker.user_name()
                password = self.faker.password()
                hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
                    "utf-8"
                )
                user = User(
                    username=username,
                    email=self.faker.email(),
                    hashed_password=hashed_password,
                )

                self.log(f"Created user - {username}")
                self.session.add(user)

            await self.session.commit()
            self.log("Users created successfully!", level="success")

        except Exception as e:
            self.log(f"Error creating users: {str(e)}", level="error")
            await self.session.rollback()
