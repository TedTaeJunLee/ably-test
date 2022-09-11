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


class SignInRequestSerializer(BaseSerializer):
    login_input = serializers.CharField(label="로그인시 사용할 값 예) 이메일 or 폰번호 or 닉네임")
    password = serializers.CharField(label="로그인 비밀번호")


class SignInResponseSerializer(BaseSerializer):
    user = MinimalUserModelSerializer()
    token = serializers.CharField(label="토큰")


class UsersMeResponseSerializer(BaseSerializer):
    user = MinimalUserModelSerializer()


class PasswordResetRequestSerializer(BaseSerializer):
    token = serializers.CharField(label="핸드폰 인증 토큰")
    phone = PhoneNumberField(label="핸드폰 번호", region="KR")
    password = serializers.CharField(label="비밀번호")


class PasswordResetResponseSerializer(BaseSerializer):
    pass
