from django.shortcuts import render

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.account.serializers import PhoneValidationVerifyCodeRequestSerializer
from src.common.constants import HttpStatusCodes


class PhoneValidationVerifyCodeView(APIView):
    @swagger_auto_schema(
        operation_id="phone-validation-verify-code",
        operation_description="인증번호 검증",
        request_body=PhoneValidationVerifyCodeRequestSerializer(),
        responses={
            "200": openapi.Response("ok"),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = PhoneValidationVerifyCodeRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=HttpStatusCodes.C_400_BAD_REQUEST)

        return Response(status=HttpStatusCodes.C_200_OK)
