from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.utils import timezone
from src.common.exceptions import InvalidValidationCodeError
from src.common.utils import generate_random_str
from src.validation.constants import PHONE_VALIDATION_CODE_EXPIRE_MIN
from src.validation.models import PhoneValidationCode
from src.validation.repositories import PhoneValidationCodeRepository


class PhoneValidationService:
    @classmethod
    def send_code(cls, phone: str) -> str:
        phone_validation_code = None

        PhoneValidationCodeRepository.soft_delete_unused_by_phone(phone)

        while True:
            try:
                phone_validation_code = PhoneValidationCode(
                    phone=phone,
                    code=generate_random_str(6, False, False, True, False),
                    expire_at=timezone.now()
                    + timedelta(minutes=PHONE_VALIDATION_CODE_EXPIRE_MIN),
                )
                PhoneValidationCodeRepository.create([phone_validation_code])
                break

            except IntegrityError:
                continue

        return phone_validation_code.code

    @classmethod
    def verify_code(cls, phone: str, code: str):
        try:
            phone_validation_code = (
                PhoneValidationCodeRepository.get_avail_by_phone_and_code(phone, code)
            )
        except ObjectDoesNotExist as e:
            raise InvalidValidationCodeError from e

        if phone_validation_code.is_used:
            raise InvalidValidationCodeError

        if phone_validation_code.expire_at < timezone.now():
            raise InvalidValidationCodeError

        phone_validation_code.use()
        phone_validation_code.save()
