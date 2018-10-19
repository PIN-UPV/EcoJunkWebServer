from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.rewards.api.v1.serializers import MissionSerializer, BadgeSerializer
from ecojunk.rewards.models import Mission, Badge


class MissionResource(ReadOnlyModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [NoDeletes, NoUpdates]


class BadgeResource(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [NoDeletes, NoUpdates]
