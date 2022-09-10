from django.db import models

# Create your models here.
from django.utils import timezone
from src.common.mixins import SoftDeleteMixin
from src.common.models import BaseModel


class PhoneValidationCode(SoftDeleteMixin, BaseModel):
    phone = models.CharField(max_length=30, verbose_name="개인 전화번호")
    code = models.CharField(max_length=6, verbose_name="인증번호")
    expire_at = models.DateTimeField(verbose_name="인증번호 만료일")
    is_used = models.BooleanField(default=False, verbose_name="사용 여부")
    use_at = models.DateTimeField(null=True, blank=True, verbose_name="인증번호 사용일")

    class Meta:
        db_table = "phone_validation_code"
        verbose_name = "핸드폰 번호 인증"
        verbose_name_plural = "핸드폰 번호 인증 목록"
        unique_together = (
            (
                "phone",
                "code",
            ),
        )

    def use(self):
        self.is_used = True
        self.use_at = timezone.now()
