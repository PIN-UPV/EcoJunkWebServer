from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer

from ecojunk.rewards.models import Badge, Mission


class BadgeSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ("name", "description")


class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = ("name", "description", "dificulty", "badges")
