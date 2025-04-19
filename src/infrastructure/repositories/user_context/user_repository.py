from sqlalchemy import select

from src.domain.user_context.entities.user import UserEntity
from src.domain.user_context.value_objects import UserId
from src.infrastructure.database.models import UserModel
from src.infrastructure.repositories.base import BasicRepository


class UserRepository(BasicRepository[UserModel]):
    """Repository for handling User model operations.

    Provides methods to query and persist user data, converting between domain entities and database models.

    Attributes:
        model_type: The type of the database model, set to UserModel.

    """

    model_type: type[UserModel] = UserModel

    async def get_by_username(self, username: str) -> UserEntity | None:
        """Retrieve a user by their username.

        Args:
            username: The username of the user to find.

        Returns:
            UserEntity | None: The user entity if found, otherwise None.

        """
        statement = select(UserModel).where(UserModel.username == username)
        user_model: UserModel = await self.session.scalar(statement)

        if not user_model:
            return None

        return self._to_entity(user_model)

    async def get_by_email(self, email: str) -> UserEntity | None:
        """Retrieve a user by their email address.

        Args:
            email: The email address of the user to find.

        Returns:
            UserEntity | None: The user entity if found, otherwise None.

        """
        statement = select(UserModel).where(UserModel.email == email)
        user_model: UserModel = await self.session.scalar(statement)

        if not user_model:
            return None

        return self._to_entity(user_model)

    async def get_by_phone(self, phone: str) -> UserEntity | None:
        """Retrieve a user by their phone number.

        Args:
            phone: The phone number of the user to find.

        Returns:
            UserEntity | None: The user entity if found, otherwise None.

        """
        statement = select(UserModel).where(UserModel.phone == phone)
        user_model = await self.session.scalar(statement)

        if not user_model:
            return None

        return self._to_entity(user_model)

    async def save(self, user_entity: UserEntity) -> UserEntity:
        """Save or update a user entity in the database.

        Args:
            user_entity: The user entity to save or update.

        Returns:
            UserEntity: The saved or updated user entity.

        """
        statement = select(UserModel).where(UserModel.id == user_entity.user_id.value)
        existing_user = await self.session.scalar(statement)

        if existing_user:
            existing_user.email = user_entity.email
            existing_user.password_hash = user_entity.password_hash
            existing_user.is_active = user_entity.is_active
        else:
            new_user = self.model_type(
                id=user_entity.user_id,
                email=user_entity.email,
                password_hash=user_entity.password_hash,
                is_active=user_entity.is_active,
            )
            self.session.add(new_user)

        await self.session.commit()
        return user_entity

    def _to_entity(self, model: UserModel) -> UserEntity:
        """Convert a UserModel to a UserEntity.

        Args:
            model: The database model to convert.

        Returns:
            UserEntity: The corresponding user entity.

        """
        return UserEntity(
            user_id=UserId(model.id), email=model.email, password_hash=model.hashed_password, is_active=model.is_active
        )

    def _to_model(self, entity: UserEntity) -> UserModel:
        """Convert a UserEntity to a UserModel.

        Args:
            entity: The user entity to convert.

        Returns:
            UserModel: The corresponding database model.

        """
        return UserModel(
            id=entity.user_id.value,
            email=entity.email,
            hashed_password=entity.password_hash,
            is_active=entity.is_active,
        )
