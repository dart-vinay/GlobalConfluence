from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Creates a new User in the system"""
    serializer_class = UserSerializer
