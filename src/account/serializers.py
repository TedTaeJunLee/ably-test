from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from src.account.models import User
from src.common.serializers import BaseModelSerializer, BaseSerializer


class MinimalUserModelSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "masked_email",
            "masked_phone",
        ]


class SignUpRequestSerializer(BaseSerializer):
    email = serializers.EmailField(label="이메일")
    nickname = serializers.CharField(label="닉네임")
    password = serializers.CharField(label="비밀번호")
    name = serializers.CharField(label="사용자 이름")
    phone = PhoneNumberField(label="핸드폰 번호", region="KR")
    token = serializers.CharField(label="핸드폰 인증 토큰")


class SignUpResponseSerializer(BaseSerializer):
    user = MinimalUserModelSerializer()
    token = serializers.CharField(label="토큰")
