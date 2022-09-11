# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError, transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from jwt import InvalidTokenError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.account.exceptions import AlreadyExistUserError
from src.account.serializers import SignUpRequestSerializer, SignUpResponseSerializer
from src.account.services.sign_up_service import AccountSignUpService
from src.account.services.user_service import UserService
from src.common.constants import HttpStatusCodes
from src.validation.constants import SIGN_UP_PHONE_VALIDATION, USERS_ME_AUTHORIZATION
from src.validation.services.token_service import TokenService
from src.validation.services.token_validation_service import TokenValidationService


class SignUpView(APIView):
    @swagger_auto_schema(
        operation_id="sign-up",
        operation_description="회원가입",
        request_body=SignUpRequestSerializer(),
        responses={
            "200": openapi.Response("ok", schema=SignUpResponseSerializer()),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def post(self, request: Request) -> Response:
        serializer = SignUpRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST, data=serializer.errors
            )
        try:
            UserService.check_if_user_exists(
                serializer.validated_data["email"], serializer.validated_data["phone"]
            )
            TokenValidationService.verify_token(
                SIGN_UP_PHONE_VALIDATION,
                serializer.validated_data["token"],
                str(serializer.validated_data["phone"]),
            )
            with transaction.atomic():
                user = AccountSignUpService.sign_up(
                    email=serializer.validated_data["email"],
                    nickname=serializer.validated_data["nickname"],
                    password=serializer.validated_data["password"],
                    name=serializer.validated_data["name"],
                    phone=serializer.validated_data["phone"],
                )
            token = TokenService.generate_token(USERS_ME_AUTHORIZATION, user.id)
        except AlreadyExistUserError:
            return Response(
                status=HttpStatusCodes.C_406_NOT_ACCEPTABLE,
                data={"msg": "AlreadyExistUserError"},
            )
        except InvalidTokenError as e:
            return Response(
                status=HttpStatusCodes.C_400_BAD_REQUEST,
                data={"msg": str(e.args)},
            )
        except DatabaseError as e:
            return Response(
                status=HttpStatusCodes.C_404_NOT_FOUND,
                data={"msg": str(e.args)},
            )
        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=SignUpResponseSerializer({"user": user, "token": token}).data,
        )
