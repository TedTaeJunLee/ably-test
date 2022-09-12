from django.db.models import Q
from src.account.models import User
from src.common.repositories import BaseRepository


class UserRepository(BaseRepository):
    model_class = User

    @classmethod
    def get_by_email_and_phone(cls, email: str = None, phone: str = None) -> User:
        queryset = cls.get_queryset().filter(is_deleted=False)
        if email:
            queryset = queryset.filter(email=email)
        if phone:
            queryset = queryset.filter(phone=phone)
        return queryset.last()

    @classmethod
    def get_by_login_input(cls, login_input: str) -> User:
        return cls.get_queryset().get(
            Q(email=login_input) | Q(phone=login_input) | Q(nickname=login_input)
        )
