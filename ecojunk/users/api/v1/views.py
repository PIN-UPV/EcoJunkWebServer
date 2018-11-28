from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ecojunk.users.api.v1.serializers import RegistrationSerializer
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        # user = request.data
        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer = JSONWebTokenSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # print("First token : " + str(serializer.data))
        # payload = jwt_payload_handler(serializer.data)
        # print("Second token : " + str(jwt_encode_handler(payload)))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
