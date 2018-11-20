from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField

from ecojunk.junk.models import Deal, JunkPoint, JunkPointType
from ecojunk.users.api.v1.serializers import UserSerializer


class JunkPointTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JunkPointType
        fields = ("id", "name", "description")


class JunkPointSerializer(serializers.ModelSerializer):

    location = GeometryField(help_text=_("Location as GeoJSON Point"))

    class Meta:
        model = JunkPoint
        fields = ("id", "street_name", "description", "location", "types")

    def to_representation(self, instance):
        response = super().to_representation(instance)
        for index in range(len(response["types"])):
            response["types"][index] = JunkPointTypeSerializer(
                instance.types.all()[index]
            ).data
        return response


class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = ("id", "customer", "rider", "junk_point", "price", "date")
        extra_kwargs = {
            "customer": {"read_only": True},
            "rider": {"read_only": True},
            "date": {"read_only": True},
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["rider"] = UserSerializer(instance.customer).data
        response["customer"] = UserSerializer(instance.rider).data
        response["junk_point"] = JunkPointSerializer(instance.junk_point).data
        return response

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)
