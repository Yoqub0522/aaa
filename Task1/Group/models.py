from django.db import models

from Course.models import Course
from User.models import User


class Group(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE)