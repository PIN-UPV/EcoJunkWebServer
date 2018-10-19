from django.utils.translation import ugettext_lazy as _
from rest_framework.serializers import ModelSerializer

from ecojunk.users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "email", "permissions", "completed_missions", "is_staff", "is_active", "date_joined")
