from .serializers import RegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer
