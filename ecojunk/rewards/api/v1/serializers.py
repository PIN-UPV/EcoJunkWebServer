from rest_framework.serializers import ModelSerializer

from ecojunk.rewards.models import Badge, Mission


class MissionSerializer(ModelSerializer):
    class Meta:
        model = Mission
        fields = ("name", "description", "difficulty", "badges")


class BadgeSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = ("name", "description")
