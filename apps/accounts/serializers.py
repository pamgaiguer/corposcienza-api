from rest_framework import serializers
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class TokenPairSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

class Meta:
    model = CustomUser
    fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "full_name",
        "phone",
        "is_active",
        "is_staff",
    ]
