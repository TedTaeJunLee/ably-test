from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils import timezone
from src.common.utils import generate_random_str
from src.validation.models import KeyValidation
from src.validation.repositories.token_validation_repository import (
    KeyValidationRepository,
)


class KeyValidationService:
    @classmethod
    def get_key(cls, key_type: str) -> KeyValidation:
        try:
            return KeyValidationRepository.get_active_last_by_key_type(key_type)

        except ObjectDoesNotExist:
            return cls.generate_key(key_type)

    @classmethod
    def generate_key(cls, key_type: str) -> KeyValidation:
        while True:
            key = KeyValidation(
                kid=generate_random_str(5, True, True, True, False),
                key_type=key_type,
                expires_at=timezone.now() + timedelta(days=365),
            )

            try:
                key.save()

            except IntegrityError:
                continue

            return key
