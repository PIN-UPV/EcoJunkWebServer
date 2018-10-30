from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ecojunk.users.api.v1.views import (
    RegistrationAPIView,
    LoginAPIView,
    UserRetrieveUpdateAPIView,
)
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token,
    verify_jwt_token,
)

urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLs
# Create a router and register our resources with it.
urlpatterns += [
    # Token
    path("api/token-auth/", obtain_jwt_token),
    path("api/token-refresh/", refresh_jwt_token),
    path("api/token-verify/", verify_jwt_token),
    path("api/v1/users/register", RegistrationAPIView.as_view()),
    path("api/v1/users/login", LoginAPIView.as_view()),
    path("api/v1/users", UserRetrieveUpdateAPIView.as_view()),
    # V1 endpoints
    path("api/v1/", include("config.router", namespace="api_v1")),
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
