from src.common.exceptions.user_exceptions import (
    UserExistError,
    UserIsNotActiveError,
    UserNotFoundError,
    UserNoVerifyPasswordError,
)
from src.domain.user_context.entities.user import UserEntity
from src.infrastructure.repositories.user_context.user_repository import UserRepository


class AuthService:
    """Service for handling user authentication and registration.

    Provides methods to authenticate and register users, interacting with the user repository.

    Attributes:
        user_repository: Repository for user data operations.
        secret_key: Secret key used for authentication processes.

    """

    def __init__(self, user_repository: UserRepository, secret_key: str) -> None:
        """Initialize the AuthService.

        Args:
            user_repository: The repository to handle user data.
            secret_key: The secret key for authentication.

        """
        self.user_repository = user_repository
        self.secret_key = secret_key

    async def authenticate_user(self, email: str, password: str) -> UserEntity:
        """Authenticate a user by email and password.

        Args:
            email: The user's email address.
            password: The user's password.

        Returns:
            UserEntity: The authenticated user entity.

        Raises:
            UserNotFoundError: If no user is found with the provided email.
            UserIsNotActiveError: If the user account is not active.
            UserNoVerifyPasswordError: If the password does not match.

        """
        user = await self.user_repository.get_by_email(email)

        if not user:
            raise UserNotFoundError(email)

        if not user.is_active:
            raise UserIsNotActiveError(email)

        if not user.verify_password(password):
            raise UserNoVerifyPasswordError(password)

        return user

    async def register_user(self, email: str, password_hash: str) -> UserEntity:
        """Register a new user with the provided email and password hash.

        Args:
            email: The user's email address.
            password_hash: The hashed password for the user.

        Returns:
            UserEntity: The newly created and saved user entity.

        Raises:
            UserExistError: If a user with the provided email already exists.

        """
        existing_user = await self.user_repository.get_by_email(email)

        if existing_user:
            raise UserExistError(email)

        user_entity = UserEntity.create(email=email, password_hash=password_hash)

        return await self.user_repository.save(user_entity)
