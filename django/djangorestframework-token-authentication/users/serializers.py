from django.contrib.auth import get_user_model
from rest_framework import serializers
# from .models import CustomUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password']
