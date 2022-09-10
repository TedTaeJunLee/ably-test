from django.urls import path
from src.account.apps import AccountConfig
from src.account.views import PhoneValidationVerifyCodeView

app_name = AccountConfig.name

urlpatterns = []
