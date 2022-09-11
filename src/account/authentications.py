from typing import Optional, Tuple

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from src.account.models import User
from src.account.services.user_service import UserService
from src.validation.constants import HTTP_AUTHORIZATION


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request: Request) -> Optional[Tuple[User, None]]:
        authorization = request.META.get(HTTP_AUTHORIZATION)
        if not authorization:
            return None

        try:
            token = authorization.split()[1]
            return (
                UserService.get_user_by_token(token),
                None,
            )

        except ObjectDoesNotExist:
            return None

    def authenticate_header(self, request):
        return HTTP_AUTHORIZATION
