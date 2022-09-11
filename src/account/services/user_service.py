from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from src.account.exceptions import AlreadyExistUserError, UserDoesNotExistError
from src.account.models import User
from src.account.repositories import UserRepository
from src.validation.constants import USERS_ME_AUTHORIZATION
from src.validation.exceptions import InvalidTokenError
from src.validation.services.token_service import TokenService


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

    @classmethod
    def get_user_by_token(cls, authorization_token: str) -> Optional[User]:
        try:
            payload = TokenService.get_token_payload(
                USERS_ME_AUTHORIZATION, authorization_token
            )
        except (InvalidTokenError, IndexError):
            return None
        user = UserRepository.get_by_id(payload["sub"])
        return user

    @classmethod
    def get_user_by_id(cls, user_id: int) -> User:
        try:
            return UserRepository.get_by_id(user_id)
        except ObjectDoesNotExist:
            raise UserDoesNotExistError

    @classmethod
    def get_user_by_phone(cls, phone: str) -> User:
        try:
            return UserRepository.get_by_email_and_phone(phone=phone)
        except ObjectDoesNotExist:
            raise UserDoesNotExistError
