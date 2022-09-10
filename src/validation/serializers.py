from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from src.common.serializers import BaseSerializer
from src.validation.constants import PHONE_VALIDATION_USAGE_TYPE_CHOICES


class PhoneValidationSendCodeRequestSerializer(BaseSerializer):
    phone = PhoneNumberField(label="핸드폰 번호", region="KR")
    usage_type = serializers.ChoiceField(
        choices=PHONE_VALIDATION_USAGE_TYPE_CHOICES, label="사용 용도 유형"
    )


class PhoneValidationSendCodeResponseSerializer(BaseSerializer):
    code = serializers.CharField(label="전화번호 인증 코드")


class PhoneValidationVerifyCodeRequestSerializer(BaseSerializer):
    phone = PhoneNumberField(label="핸드폰 번호", region="KR")
    code = serializers.CharField(label="전화번호 인증 코드")
    usage_type = serializers.ChoiceField(
        choices=PHONE_VALIDATION_USAGE_TYPE_CHOICES, label="사용 용도 유형"
    )
