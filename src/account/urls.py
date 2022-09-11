from django.urls import path
from src.account.apps import AccountConfig
from src.account.views.signin_views import SignInView
from src.account.views.signup_views import SignUpView
from src.account.views.user_views import UsersMeView

app_name = AccountConfig.name


urlpatterns = [
    path(
        "sign-up/",
        SignUpView.as_view(),
        name="sign-up",
    ),
    path(
        "sign-in/",
        SignInView.as_view(),
        name="sign-in",
    ),
    path(
        "users/me/",
        UsersMeView.as_view(),
        name="users-me",
    ),
]
