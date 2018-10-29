from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.rewards.api.v1.serializers import BadgeSerializer, MissionSerializer
from ecojunk.rewards.models import Badge, Mission
from rest_framework.permissions import IsAuthenticated


class MissionResource(ReadOnlyModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]


class BadgeResource(ReadOnlyModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]
