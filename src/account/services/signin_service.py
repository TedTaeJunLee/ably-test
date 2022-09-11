from django.core.exceptions import ObjectDoesNotExist
from src.account.exceptions import UserDoesNotExistError, WrongPasswordError
from src.account.models import User
from src.account.services.password_service import PasswordService
from src.account.services.user_service import UserService


class SignInService:
    @classmethod
    def sign_in(cls, login_input: str, password: str) -> User:
        try:
            user = UserService.get_by_login_input(login_input)
        except ObjectDoesNotExist as e:
            raise UserDoesNotExistError from e

        if not PasswordService.validate_password(password, user.password):
            raise WrongPasswordError

        return user
