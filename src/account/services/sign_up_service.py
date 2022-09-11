from src.account.models import User
from src.account.repositories import UserRepository
from src.account.services.password_service import PasswordService


class AccountSignUpService:
    @classmethod
    def sign_up(
        cls, email: str, nickname: str, password: str, name: str, phone: str
    ) -> User:
        return UserRepository.create(
            [
                User(
                    email=email,
                    nickname=nickname,
                    password=PasswordService.make_hashed_password(password),
                    name=name,
                    phone=phone,
                )
            ]
        )[0]
