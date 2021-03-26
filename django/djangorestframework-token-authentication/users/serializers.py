from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
