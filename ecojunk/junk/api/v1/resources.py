from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny
from ecojunk.core.api.permissions import NoUpdates
from ecojunk.junk.api.v1.exceptions import DealAlreadyPicked, DealNotYours
from ecojunk.junk.api.v1.permissions import IsUserOwnerForDeletes
from ecojunk.junk.api.v1.serializers import (
    DealSerializer,
    JunkPointSerializer,
    JunkPointTypeSerializer,
)
from ecojunk.junk.models import Deal, JunkPoint, JunkPointType
from ecojunk.users.api.v1.permissions import (
    RiderPermissions,
    AuthenticatedReadPermission,
)


class JunkPointResource(ModelViewSet):
    queryset = JunkPoint.objects.all()
    serializer_class = JunkPointSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        lat = self.request.query_params.get("lat")
        lng = self.request.query_params.get("lng")

        if not lat or lng:
            return queryset

        point = Point(lng, lat)
        radius = self.request.query_params.get("km", 10)
        queryset = queryset.filter(location__distance_lt=(point, Distance(km=radius)))
        return queryset


class JunkPointTypeResource(ReadOnlyModelViewSet):
    queryset = JunkPointType.objects.all()
    serializer_class = JunkPointTypeSerializer
    permission_classes = [AllowAny]


# TODO: handle auth, limit queryset, etc..
class DealResource(ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = [
        RiderPermissions,
        IsUserOwnerForDeletes,
        NoUpdates,
        AuthenticatedReadPermission,
    ]

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)

    @action(detail=True, methods=["post"])
    def accept_deal(self, request, **kwargs):
        deal = self.get_object()
        if deal.rider:
            raise DealAlreadyPicked
        deal.rider = request.user
        deal.accepted_date = timezone.now()
        deal.state = deal.ACCEPTED
        deal.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def decline_deal(self, request, **kwargs):
        deal = self.get_object()
        if deal.rider and deal.rider != self.request.user:
            raise DealNotYours
        deal.rider = None
        deal.accepted_date = None
        deal.state = deal.PUBLISHED
        deal.save()
        return Response(status=status.HTTP_200_OK)
