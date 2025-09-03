from rest_framework import serializers
from .models import Student, StudentImage

class StudentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentImage
        fields = ["id", "image"]

class StudentSerializer(serializers.ModelSerializer):
    images = StudentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ["id", "user", "parents_phone", "address", "birth_date", "images"]
