# Create your views here.
from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.common.constants import HttpStatusCodes
from src.common.exceptions import InvalidValidationCodeError
from src.validation.constants import SIGN_UP_PHONE_VALIDATION
from src.validation.serializers import (
    PhoneValidationSendCodeRequestSerializer,
    PhoneValidationSendCodeResponseSerializer,
    PhoneValidationVerifyCodeRequestSerializer,
    PhoneValidationVerifyCodeResponseSerializer,
)
from src.validation.services.phone_validation_service import PhoneValidationService
from src.validation.services.token_validation_service import TokenValidationService


class PhoneValidationSendCodeView(APIView):
    @swagger_auto_schema(
        operation_id="phone-validation-send-code",
        operation_description="인증번호 발송",
        request_body=PhoneValidationSendCodeRequestSerializer(),
        responses={
            "200": openapi.Response(
                "ok", schema=PhoneValidationSendCodeResponseSerializer()
            ),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = PhoneValidationSendCodeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST,
                data=serializer.errors,
            )
        code = PhoneValidationService.send_code(
            serializer.validated_data["phone"], serializer.validated_data["usage_type"]
        )

        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=PhoneValidationSendCodeResponseSerializer({"code": code}).data,
        )


class PhoneValidationVerifyCodeView(APIView):
    @swagger_auto_schema(
        operation_id="phone-validation-verify-code",
        operation_description="인증번호 검증",
        request_body=PhoneValidationVerifyCodeRequestSerializer(),
        responses={
            "200": openapi.Response(
                "ok", schema=PhoneValidationVerifyCodeResponseSerializer()
            ),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = PhoneValidationVerifyCodeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST, data=serializer.errors
            )
        with transaction.atomic():
            try:
                PhoneValidationService.verify_code(
                    serializer.validated_data["phone"],
                    serializer.validated_data["code"],
                    serializer.validated_data["usage_type"],
                )

            except InvalidValidationCodeError:
                return Response(
                    status=HttpStatusCodes.C_400_BAD_REQUEST,
                    data={"msg": "InvalidValidationCodeError"},
                )

            token = TokenValidationService.generate_token(
                SIGN_UP_PHONE_VALIDATION, str(serializer.validated_data["phone"])
            )

        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=PhoneValidationVerifyCodeResponseSerializer({"token": token}).data,
        )
