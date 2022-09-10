from django.utils import timezone
from src.common.repositories import BaseRepository
from src.validation.models import PhoneValidationCode


class PhoneValidationCodeRepository(BaseRepository):
    model_class = PhoneValidationCode

    @classmethod
    def get_avail_by_phone_and_code_and_usage_type(
        cls, phone: str, code: str, usage_type: str
    ) -> PhoneValidationCode:
        return cls.get_queryset().get(
            phone=phone,
            code=code,
            expire_at__gte=timezone.now(),
            usage_type=usage_type,
            is_deleted=False,
        )

    @classmethod
    def soft_delete_unused_by_phone_and_usage_type(cls, phone: str, usage_type: str):
        return (
            cls.get_queryset()
            .filter(phone=phone, usage_type=usage_type, is_used=False)
            .update(is_deleted=True, deleted_at=timezone.now())
        )
