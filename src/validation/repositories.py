from django.utils import timezone
from src.common.repositories import BaseRepository
from src.validation.models import PhoneValidationCode


class PhoneValidationCodeRepository(BaseRepository):
    model_class = PhoneValidationCode

    @classmethod
    def get_avail_by_phone_and_code(cls, phone: str, code: str) -> PhoneValidationCode:
        return cls.get_queryset().get(
            phone=phone, code=code, expire_at__gte=timezone.now(), is_deleted=False
        )

    @classmethod
    def soft_delete_unused_by_phone(cls, phone: str):
        return (
            cls.get_queryset()
            .filter(phone=phone, is_used=False)
            .update(is_deleted=True, deleted_at=timezone.now())
        )
