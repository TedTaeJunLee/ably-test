from drf_yasg import openapi
from drf_yasg.openapi import IN_HEADER
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from src.account.authentications import UserAuthentication
from src.account.exceptions import UserDoesNotExistError
from src.account.serializers import UsersMeResponseSerializer
from src.account.services.user_service import UserService
from src.common.constants import HttpStatusCodes


class UsersMeView(APIView):
    authentication_classes = {UserAuthentication}
    permission_classes = {IsAuthenticated}

    @swagger_auto_schema(
        operation_id="users-me",
        operation_description="사용자 정보 조회",
        manual_parameters=[
            openapi.Parameter(
                in_=IN_HEADER,
                name="Authorization",
                type="JWT",
                description="Authentication을 위한 Bear token",
                example="Bearer {access_token}",
            )
        ],
        responses={
            "200": openapi.Response("ok", schema=UsersMeResponseSerializer()),
            "400": openapi.Response(
                "Bad Request",
            ),
        },
    )
    def get(self, request: Request) -> Response:
        try:
            user = UserService.get_user_by_id(request.user.id)
        except UserDoesNotExistError:
            return Response(
                status=HttpStatusCodes.C_404_NOT_FOUND,
                data={"msg": "사용자 정보를 찾을 수 없습니다."},
            )
        return Response(
            status=HttpStatusCodes.C_200_OK,
            data=UsersMeResponseSerializer({"user": user}).data,
        )
