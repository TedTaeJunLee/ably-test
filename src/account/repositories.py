from src.account.models import User
from src.common.repositories import BaseRepository


class UserRepository(BaseRepository):
    model_class = User

    @classmethod
    def get_by_email_and_phone(cls, email: str, phone: str) -> User:
        return cls.get_queryset().get(email=email, phone=phone)
