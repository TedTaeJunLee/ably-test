from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from src.common.repositories import BaseRepository
from src.validation.models import KeyValidation


class KeyValidationRepository(BaseRepository):
    model_class = KeyValidation

    @classmethod
    def get_active_by_key_type_and_kid(cls, key_type: str, kid: str) -> KeyValidation:
        now = timezone.now()
        return cls.get_queryset().get(expires_at__gte=now, key_type=key_type, kid=kid)

    @classmethod
    def get_active_last_by_key_type(cls, key_type: str) -> KeyValidation:
        now = timezone.now()

        if (
            key := cls.get_queryset()
            .filter(expires_at__gte=now, key_type=key_type)
            .order_by("expires_at")
            .last()
        ):
            return key

        raise ObjectDoesNotExist
