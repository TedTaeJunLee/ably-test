from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from django.db import models

# Create your models here.
from django.utils import timezone
from src.common.mixins import SoftDeleteMixin
from src.common.models import BaseModel
from src.validation.constants import (
    PHONE_VALIDATION_USAGE_TYPE_CHOICES,
    RSA_PRIVATE_KEY_BITS,
    TOKEN_VALIDATION_KEY_TYPE_CHOICES,
)


class PhoneValidationCode(SoftDeleteMixin, BaseModel):
    phone = models.CharField(max_length=30, verbose_name="개인 전화번호")
    code = models.CharField(max_length=6, verbose_name="인증번호")
    expire_at = models.DateTimeField(verbose_name="인증번호 만료일")
    is_used = models.BooleanField(default=False, verbose_name="사용 여부")
    use_at = models.DateTimeField(null=True, blank=True, verbose_name="인증번호 사용일")
    usage_type = models.CharField(
        choices=PHONE_VALIDATION_USAGE_TYPE_CHOICES,
        max_length=16,
        verbose_name="사용 용도 유형",
    )

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


class KeyValidation(BaseModel):
    kid = models.CharField(max_length=10, unique=True, verbose_name="kid")
    key_type = models.CharField(
        max_length=64, choices=TOKEN_VALIDATION_KEY_TYPE_CHOICES, verbose_name="키 유형"
    )
    public_key = models.TextField(verbose_name="비대칭키의 공개키")
    private_key = models.TextField(verbose_name="비대칭키의 비밀키")

    expires_at = models.DateTimeField(verbose_name="만료시간")

    class Meta:
        db_table = "key_validation"
        verbose_name = "키 검증"
        verbose_name_plural = "키 검증 리스트"

    def __str__(self) -> str:
        return str(self.kid)

    def _generate_rsa_key(self):
        if self.public_key and self.private_key:
            return

        generated_private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=RSA_PRIVATE_KEY_BITS,
            backend=default_backend(),
        )
        self._generate_asymmetric_key(generated_private_key)

    def _generate_asymmetric_key(self, generated_private_key):
        self.public_key = (
            generated_private_key.public_key()
            .public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            .decode()
        )

        self.private_key = generated_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode()

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self._generate_rsa_key()
        super().save(force_insert, force_update, using, update_fields)
