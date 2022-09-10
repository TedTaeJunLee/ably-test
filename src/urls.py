"""account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from account import urls as account_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from validation import urls as verification_urls

urlpatterns = [
    path("api/accounts/", include(account_urls, namespace="accounts")),
    path("api/validations/", include(verification_urls, namespace="validation")),
    path("admin/", admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    schema_view = get_schema_view(
        openapi.Info(
            title="Ably-Test API",
            default_version="v1",
            description="Test description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="tejunlee007@ably-test.local"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    urls = [
        path(
            "api/swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "api/redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path("api/__debug__/", include(debug_toolbar.urls)),
    ]
    urlpatterns = (
        urls
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + urlpatterns
    )
tterns = (
    urls + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + urlpatterns
)
