from src.domain.services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        """Докстринг."""
