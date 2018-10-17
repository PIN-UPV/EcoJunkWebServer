from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ecojunk.junk.api.v1.resources import (JunkPointResource,
                                           JunkPointTypeResource)

app_name = "api_v1"

# ViewSet resources included using router
router = SimpleRouter()
router.register("junk_points", viewset=JunkPointResource)
router.register(
    "junk_point_types", viewset=JunkPointTypeResource, base_name="request_restore_code"
)

urlpatterns = [path("", include(router.urls))]
