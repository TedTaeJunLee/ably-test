import bcrypt
from src.account.repositories import UserRepository
from src.account.services.user_service import UserService


class PasswordService:
    @classmethod
    def make_hashed_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @classmethod
    def validate_password(cls, password: str, expected_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"), expected_password.encode("utf-8")
        )

    @classmethod
    def reset_password(cls, phone: str, new_password: str) -> None:
        user = UserService.get_user_by_phone(phone)
        user.password = PasswordService.make_hashed_password(new_password)
        UserRepository.save([user], update_fields=["password"])
