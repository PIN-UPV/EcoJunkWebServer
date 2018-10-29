from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.junk.api.v1.serializers import (
    DealSerializer,
    JunkPointSerializer,
    JunkPointTypeSerializer,
)
from ecojunk.junk.models import Deal, JunkPoint, JunkPointType


class JunkPointResource(ModelViewSet):
    queryset = JunkPoint.objects.all()
    serializer_class = JunkPointSerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]


class JunkPointTypeResource(ReadOnlyModelViewSet):
    queryset = JunkPointType.objects.all()
    serializer_class = JunkPointTypeSerializer
    permission_classes = [IsAuthenticated, NoDeletes, NoUpdates]


# TODO: handle auth, limit queryset, etc..
class DealResource(ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [NoDeletes, NoUpdates]

    @action(detail=True, methods=["post"])
    def accept_deal(self, request, **kwargs):
        # TODO check user is rider and give the deal
        deal = self.get_object()
        return Response(status=status.HTTP_200_OK)
