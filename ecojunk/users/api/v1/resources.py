from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from ecojunk.core.api.permissions import NoDeletes, NoUpdates
from ecojunk.users.api.v1.serializers import UserSerializer
from ecojunk.users.models import User


class UserResource(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [NoDeletes, NoUpdates]
