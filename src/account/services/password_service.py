import bcrypt
from src.account.exceptions import WrongPasswordError


class PasswordService:
    @classmethod
    def make_hashed_password(cls, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @classmethod
    def validate_password(cls, password: str, expected_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"), expected_password.encode("utf-8")
        )
