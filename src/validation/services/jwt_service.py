from datetime import datetime
from typing import Dict

import jwt
from django.core.exceptions import ObjectDoesNotExist
from jwt import InvalidKeyError, InvalidTokenError
from src.common.utils import generate_random_str
from src.validation.constants import JWT_ALGORITHM_RSA
from src.validation.exceptions import JwtVerifyError
from src.validation.repositories.token_validation_repository import (
    KeyValidationRepository,
)
from src.validation.services.key_validation_service import KeyValidationService


class JwtService:
    def __init__(self, key_type: str, ttl: int = 60):
        self._key_type = key_type
        self._ttl = ttl

    def _create_payload(self, payload: Dict) -> Dict:
        payload.update({"exp": round(datetime.now().timestamp()) + self._ttl})
        return payload

    def generate(self, payload: Dict) -> str:
        key = KeyValidationService.get_key(self._key_type)
        return jwt.encode(
            self._create_payload(payload),
            key.private_key,
            JWT_ALGORITHM_RSA,
            {"kid": generate_random_str(5, True, True, True, False)},
        )

    def verify(self, encoded_jwt: str) -> Dict:
        try:
            kid = jwt.get_unverified_header(encoded_jwt).get("kid")
            key = KeyValidationRepository.get_active_by_key_type_and_kid(
                self._key_type, kid
            )
            return jwt.decode(encoded_jwt, key.private_key, JWT_ALGORITHM_RSA)
        except (InvalidTokenError, InvalidKeyError, ObjectDoesNotExist) as e:
            raise JwtVerifyError from e
