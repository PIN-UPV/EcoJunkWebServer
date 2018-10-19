from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ecojunk.junk.api.v1.resources import (JunkPointResource,
                                           JunkPointTypeResource)
from ecojunk.rewards.api.v1.resources import (MissionResource,
                                               BadgeResource)
from ecojunk.companies.api.v1.resources import (CompanyResource,
                                               ContractResource)
from ecojunk.users.api.v1.resources import (UserResource)

app_name = "api_v1"

# ViewSet resources included using router
router = SimpleRouter()
router.register("junk_points", viewset=JunkPointResource)
router.register(
    "junk_point_types", viewset=JunkPointTypeResource, base_name="request_restore_code"
)
router.register("missions", viewset=MissionResource)
router.register("badges", viewset=BadgeResource)
router.register("contracts", viewset=ContractResource)
router.register("companies", viewset=CompanyResource)
router.register("users", viewset=UserResource)

urlpatterns = [path("", include(router.urls))]
