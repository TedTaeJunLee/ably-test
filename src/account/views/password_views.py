from django.db import DatabaseError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.account.serializers import PasswordResetRequestSerializer
from src.account.services.password_service import PasswordService
from src.common.constants import HttpStatusCodes
from src.validation.constants import PASSWORD_RESET_PHONE_VALIDATION
from src.validation.exceptions import InvalidTokenError
from src.validation.services.token_validation_service import TokenValidationService


class PasswordResetView(APIView):
    @swagger_auto_schema(
        operation_id="password-reset",
        operation_description="비밀번호 재설정",
        request_body=PasswordResetRequestSerializer(),
        responses={
            "200": openapi.Response("ok"),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = PasswordResetRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST, data=serializer.errors
            )

        try:
            TokenValidationService.verify_token(
                PASSWORD_RESET_PHONE_VALIDATION,
                serializer.validated_data["token"],
                str(serializer.validated_data["phone"]),
            )
            PasswordService.reset_password(
                str(serializer.validated_data["phone"]),
                serializer.validated_data["password"],
            )

        except InvalidTokenError as e:
                return Response(
                    status=HttpStatusCodes.C_400_BAD_REQUEST,
                    data={"mgs": f"InvalidTokenError"},
                )
        except DatabaseError as de:
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST,
                data={"mgs": str(de.args)},
            )

        return Response(status=HttpStatusCodes.C_200_OK)
