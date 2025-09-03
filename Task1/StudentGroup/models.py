from django.db import models

from Group.models import Group
from Student.models import Student


class StudentGroup(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
