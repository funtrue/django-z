from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from account.models import Profile
from account.serializers import UserSerializer, GroupSerializer, UserProfileSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    用户

    Args:
        viewsets (_type_): _description_
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    用户组

    Args:
        viewsets (_type_): _description_
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    用户拓展

    Args:
        viewsets (_type_): _description_
    """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
