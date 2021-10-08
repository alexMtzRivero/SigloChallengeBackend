from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from sigloChallenge.user_profiles.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
