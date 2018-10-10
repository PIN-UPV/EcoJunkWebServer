from rest_framework import serializers

from ecojunk.junk.models import JunkPoint, JunkPointType


class JunkPoint(serializers.ModelSerializer):
    class Meta:
        model = JunkPoint
        fields = ("location",)
