from core.models import Usuario

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            "id",
            "username",
            "email",            
            "password",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            password=validated_data["password"],
        )
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
