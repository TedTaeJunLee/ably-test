# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.common.constants import HttpStatusCodes
from src.validation.serializers import (
    PhoneValidationSendCodeRequestSerializer,
    PhoneValidationSendCodeResponseSerializer,
)


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

        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=PhoneValidationSendCodeResponseSerializer({"code": "111111"}).data,
        )
