from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.junk.api.v1.serializers import JunkPointSerializer, JunkPointTypeSerializer
from ecojunk.junk.models import JunkPoint, JunkPointType


class JunkPointResource(ModelViewSet):
    queryset = JunkPoint.objects.all()
    serializer_class = JunkPointSerializer
    permission_classes = [NoDeletes, NoUpdates]


class JunkPointTypeResource(ReadOnlyModelViewSet):
    queryset = JunkPointType.objects.all()
    serializer_class = JunkPointTypeSerializer
    permission_classes = [NoDeletes, NoUpdates]
