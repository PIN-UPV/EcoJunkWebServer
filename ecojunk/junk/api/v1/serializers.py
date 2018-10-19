from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from ecojunk.junk.models import Deal, JunkPoint, JunkPointType


class JunkPointTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JunkPointType
        fields = ("name", "description")


class JunkPointSerializer(serializers.ModelSerializer):

    location = GeometryField(help_text=_("Location as GeoJSON Point."))

    class Meta:
        model = JunkPoint
        fields = ("location", "type")


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ("customer", "rider", "junk_point")
        extra_kwargs = {"date": {"read_only": True}}

    def create(self, validated_data):
        """Override to handle nested groups."""
        pass
