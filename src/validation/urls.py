from django.urls import path
from src.validation.apps import ValidationConfig
from src.validation.views import (
    PhoneValidationSendCodeView,
    PhoneValidationVerifyCodeView,
)

app_name = ValidationConfig.name

urlpatterns = [
    path(
        "phone-validation/send-code/",
        PhoneValidationSendCodeView.as_view(),
        name="phone-validation-send-code",
    ),
    path(
        "phone-valiation/verify-code/",
        PhoneValidationVerifyCodeView.as_view(),
        name="phone-validation-verify-code",
    ),
]
