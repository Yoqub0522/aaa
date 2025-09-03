from django.db import models

from User.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    parents_phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=255)
    image = models.BigIntegerField()
