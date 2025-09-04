from rest_framework.viewsets import ModelViewSet
from .models import Student, StudentImage
from .serializers import StudentSerializer, StudentImageSerializer



class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentImageViewSet(ModelViewSet):
    queryset = StudentImage.objects.all()
    serializer_class = StudentImageSerializer

