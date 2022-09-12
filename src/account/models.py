from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField
from src.common.mixins import BaseAbstractBaseUser, SoftDeleteMixin
from src.common.models import BaseModel
from src.common.utils import mask_email, mask_string


class User(SoftDeleteMixin, BaseAbstractBaseUser, BaseModel):
    email = models.EmailField(unique=True, verbose_name="이메일")
    nickname = models.CharField(unique=True, max_length=64, verbose_name="닉네임")
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    name = models.CharField(max_length=32, verbose_name="사용자 이름")
    phone = PhoneNumberField(unique=True, verbose_name="핸드폰 번호", region="KR")

    class Meta:
        db_table = "user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자 리스트"
        unique_together = ("email", "phone")

    @property
    def masked_phone(self) -> str:
        return mask_string(self.phone.as_national, length_to_show=5)

    @property
    def masked_email(self):
        return mask_email(self.email)
