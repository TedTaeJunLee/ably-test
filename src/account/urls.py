from django.urls import path
from src.account.apps import AccountConfig
from src.account.views import SignUpView

app_name = AccountConfig.name

urlpatterns = [
    path(
        "sign-up/",
        SignUpView.as_view(),
        name="sign-up",
    ),
]
