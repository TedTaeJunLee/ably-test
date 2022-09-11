from src.account.models import User
from src.account.repositories import UserRepository


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
                    password=password,
                    name=name,
                    phone=phone,
                )
            ]
        )[0]
