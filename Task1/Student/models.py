from django.db import models

from User.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parents_phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.DateField

    def __str__(self):
       return self.user.username


class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="students/")

    def __str__(self):
        return f"{self.student.user.username}-rasmi"

