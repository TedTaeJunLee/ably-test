from datetime import timedelta

from src.validation.constants import TOKEN_EXPIRE_DAYS, USERS_ME_AUTHORIZATION
from src.validation.exceptions import InvalidTokenError, JwtVerifyError
from src.validation.services.jwt_service import JwtService


class TokenService:
    @classmethod
    def generate_token(cls, key_type: str, user_id: int) -> str:
        payload = {"sub": user_id}
        return JwtService(
            key_type,
            int(timedelta(days=TOKEN_EXPIRE_DAYS).total_seconds()),
        ).generate(payload)

    @classmethod
    def get_token_payload(cls, key_type: str, token: str):
        try:
            return JwtService(key_type, 0).verify(token)

        except JwtVerifyError as e:
            raise InvalidTokenError from e
