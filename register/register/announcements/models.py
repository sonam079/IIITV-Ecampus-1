# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Announcement(models.Model):
    announcement = models.CharField(max_length=500, blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    announcementUser = models.ForeignKey(User, null=True)