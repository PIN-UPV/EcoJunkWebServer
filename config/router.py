from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ecojunk.companies.api.v1.resources import CompanyResource, ContractResource
from ecojunk.junk.api.v1.resources import (
    DealResource,
    JunkPointResource,
    JunkPointTypeResource,
)
from ecojunk.rewards.api.v1.resources import BadgeResource, MissionResource
from ecojunk.users.api.v1.views import (
    LoginAPIView,
    RegistrationAPIView,
    UserRetrieveUpdateAPIView,
)

app_name = "api_v1"

# ViewSet resources included using router
router = SimpleRouter()

router.register("junk_points", viewset=JunkPointResource, base_name="junk_points")
router.register(
    "junk_point_types", viewset=JunkPointTypeResource, base_name="request_restore_code"
)
router.register("deals", viewset=DealResource, base_name="deals")
router.register("missions", viewset=MissionResource)
router.register("badges", viewset=BadgeResource)
router.register("contracts", viewset=ContractResource)
router.register("companies", viewset=CompanyResource)

urlpatterns = [
    path("", include(router.urls)),
    path("users/register", RegistrationAPIView.as_view()),
    path("users/login", LoginAPIView.as_view()),
    path("users", UserRetrieveUpdateAPIView.as_view()),
]
