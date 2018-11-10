from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token,
                                      verify_jwt_token)
from ecojunk.companies.api.v1.resources import (CompanyResource,
                                                ContractResource)
from ecojunk.junk.api.v1.resources import (DealResource, JunkPointResource,
                                           JunkPointTypeResource, JunkPointMapResource)
from ecojunk.rewards.api.v1.resources import BadgeResource, MissionResource
from ecojunk.users.api.v1.resources import UserResource
from ecojunk.users.api.v1.views import RegistrationAPIView

app_name = "api_v1"

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
    path("users/refresh-token/", refresh_jwt_token),
    path("users/verify-token/", verify_jwt_token),
    path("users/register/", RegistrationAPIView.as_view()),
    path("users/login/", obtain_jwt_token),
    path("users/me/", UserResource.as_view()),
    path("maps", JunkPointMapResource.as_view()),
]
