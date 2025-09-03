from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Group
from .serializers import GroupSerializer
from  User.permissions import RoleBasedPermission


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated,RoleBasedPermission]
