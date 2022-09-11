from django.core.exceptions import ObjectDoesNotExist
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.account.exceptions import UserDoesNotExistError, WrongPasswordError
from src.account.serializers import SignInRequestSerializer, SignInResponseSerializer
from src.account.services.password_service import PasswordService
from src.account.services.signin_service import SignInService
from src.account.services.user_service import UserService
from src.common.constants import HttpStatusCodes
from src.validation.constants import USERS_ME_AUTHORIZATION
from src.validation.services.token_service import TokenService


class SignInView(APIView):
    @swagger_auto_schema(
        operation_id="sign-in",
        operation_description="로그인",
        request_body=SignInRequestSerializer(),
        responses={
            "200": openapi.Response("ok", schema=SignInResponseSerializer()),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = SignInRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST, data=serializer.errors
            )
        try:
            user = SignInService.sign_in(
                serializer.validated_data["login_input"],
                serializer.validated_data["password"],
            )
            token = TokenService.generate_token(USERS_ME_AUTHORIZATION, user.id)
        except UserDoesNotExistError:
            return Response(
                status=HttpStatusCodes.C_404_NOT_FOUND,
                data={"mgs": "사용자 정보를 찾을 수 없습니다."},
            )
        except WrongPasswordError:
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST,
                data={"mgs": "잘못된 비밀번호 입니다."},
            )

        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=SignInResponseSerializer({"user": user, "token": token}).data,
        )
