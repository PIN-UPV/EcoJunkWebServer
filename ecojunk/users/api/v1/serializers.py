from rest_framework import serializers

from ecojunk.users.models import User, Permission


class PermissionSerializer(serializers.ModelSerializer):
    """Serializers to handle Permission model."""

    class Meta:
        model = Permission
        fields = ["id", "rol"]


class UserSerializer(serializers.ModelSerializer):
    """Handles serialization and deserialization of User objects."""

    permissions = PermissionSerializer(many=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "permissions", "password")
        extra_kwargs = {
            "token": {"read_only": True},
            "permissions": {"read_only": True},
        }

    def update(self, instance, validated_data):
        """Performs an update on a User."""
        password = validated_data.pop("password", None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["email", "password", "token"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

