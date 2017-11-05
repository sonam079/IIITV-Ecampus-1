import os
from django.contrib.auth.models import User
from django.db import models
from register.course.models import CourseMaterial

# Create your models here.

class AssignmentMaterial(models.Model):
    course_no = models.ForeignKey(CourseMaterial.course_no)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    faculty = models.ManyToManyField(User)

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return os.path.basename(self.file.name)
