from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.junk.api.v1.exceptions import DealAlreadyPicked, DealNotYours
from ecojunk.junk.api.v1.serializers import (
    DealSerializer,
    JunkPointSerializer,
    JunkPointTypeSerializer,
)
from ecojunk.junk.models import Deal, JunkPoint, JunkPointType
from ecojunk.users.api.v1.permissions import RiderPermissions
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from rest_framework.generics import ListAPIView


class JunkPointMapResource(ListAPIView):
    # queryset = JunkPoint.objects.filter(location__distance_lt=(point, Distance(km=radius)))
    model = JunkPoint
    serializer_class = JunkPointSerializer
    permission_classes = [NoDeletes, NoUpdates]

    def get_queryset(self):
        queryset = JunkPoint.objects.all()
        lat = self.request.query_params.get('lat', None)
        lng = self.request.query_params.get('lng', None)
        if lat is not None and lng is not None:
            lat = float(lat)
            lng = float(lng)
        else:
            return queryset
        # print("LAT: " + str(lat) + " LNG: " + str(lng))
        point = Point(lng, lat)
        radius = self.request.query_params.get('km', 10)
        queryset = queryset.filter(location__distance_lt=(point, Distance(km=radius)))
        return queryset

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
    permission_classes = [RiderPermissions, NoDeletes, NoUpdates]

    @action(detail=True, methods=["post"])
    def accept_deal(self, request, **kwargs):
        deal = self.get_object()
        if deal.rider:
            raise DealAlreadyPicked
        deal.rider = request.user
        deal.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def decline_deal(self, request, **kwargs):
        deal = self.get_object()
        if deal.rider and deal.rider != self.request.user:
            raise DealNotYours
        deal.rider = None
        deal.save()
        return Response(status=status.HTTP_200_OK)
