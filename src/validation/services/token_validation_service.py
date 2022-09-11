from src.validation.exceptions import InvalidTokenError, JwtVerifyError
from src.validation.services.jwt_service import JwtService


class TokenValidationService:
    @classmethod
    def generate_token(cls, key_type: str, payload: str, ttl: int = 60 * 10) -> str:
        return JwtService(key_type, ttl).generate({"payload": payload})

    @classmethod
    def verify_token(cls, key_type: str, token: str, payload: str):
        try:
            token_payload = JwtService(key_type).verify(token)
        except JwtVerifyError as e:
            raise InvalidTokenError from e

        if token_payload["payload"] != payload:
            raise InvalidTokenError
