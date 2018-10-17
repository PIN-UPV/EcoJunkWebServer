from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer
from rest_framework_gis.fields import GeometryField

from ecojunk.junk.models import JunkPoint, JunkPointType


class JunkPointTypeSerializer(ModelSerializer):
    class Meta:
        model = JunkPointType
        fields = ("name", "description")


class JunkPointSerializer(ModelSerializer):

    location = GeometryField(help_text=_("Location as GeoJSON Point."))

    class Meta:
        model = JunkPoint
        fields = ("location", "type")
