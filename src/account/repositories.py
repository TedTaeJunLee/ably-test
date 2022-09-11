from django.db.models import Q
from src.account.models import User
from src.common.repositories import BaseRepository


class UserRepository(BaseRepository):
    model_class = User

    @classmethod
    def get_by_email_and_phone(cls, email: str, phone: str) -> User:
        return cls.get_queryset().get(email=email, phone=phone)

    @classmethod
    def get_by_login_input(cls, login_input: str) -> User:
        return cls.get_queryset().get(
            Q(email=login_input) | Q(phone=login_input) | Q(nickname=login_input)
        )
