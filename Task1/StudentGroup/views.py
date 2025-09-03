from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import StudentGroup
from .serializers import StudentGroupSerializer


class StudentGroupViewSet(viewsets.ModelViewSet):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupSerializer
    permission_classes = [IsAuthenticated]
