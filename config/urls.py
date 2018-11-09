from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ecojunk.junk.api.v1.resources import JunkPointMapResource
urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# API URLs
# Create a router and register our resources with it.
urlpatterns += [
    # V1 endpoints

    url(r"^api/v1/maps", JunkPointMapResource.as_view()),
    path("api/v1/", include("config.router", namespace="api_v1"))
]

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
