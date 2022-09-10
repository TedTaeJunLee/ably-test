from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from src.common.serializers import BaseSerializer


class PhoneValidationSendCodeRequestSerializer(BaseSerializer):
    phone = PhoneNumberField(label="핸드폰 번호", region="KR")


class PhoneValidationSendCodeResponseSerializer(BaseSerializer):
    code = serializers.CharField(label="전화번호 인증 코드")
