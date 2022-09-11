from django.core.exceptions import ObjectDoesNotExist
from src.account.exceptions import AlreadyExistUserError
from src.account.models import User
from src.account.repositories import UserRepository


class UserService:
    @classmethod
    def get_user_by_email_and_phone(cls, email: str, phone: str) -> User:
        return UserRepository.get_by_email_and_phone(email, phone)

    @classmethod
    def check_if_user_exists(cls, email: str, phone: str) -> None:
        try:
            cls.get_user_by_email_and_phone(email, phone)
            raise AlreadyExistUserError
        except ObjectDoesNotExist:
            pass

    @classmethod
    def get_by_login_input(cls, login_input: str) -> User:
        return UserRepository.get_by_login_input(login_input)
