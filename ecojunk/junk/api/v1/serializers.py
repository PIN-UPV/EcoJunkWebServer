from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from ecojunk.junk.models import Deal, JunkPoint, JunkPointType


class JunkPointTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JunkPointType
        fields = ("id", "name", "description")


class JunkPointSerializer(serializers.ModelSerializer):

    location = GeometryField(help_text=_("Location as GeoJSON Point."))

    class Meta:
        model = JunkPoint
        fields = ("id", "street_name", "description", "location", "types")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        for i in range(0, len(response["types"])):
            response["types"][i] = JunkPointTypeSerializer(instance.types.all()[i]).data
        # response["type"] = JunkPointTypeSerializer(instance.type).data
        return response


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ("id", "customer", "rider", "junk_point", "price")
        extra_kwargs = {"date": {"read_only": True}}

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
