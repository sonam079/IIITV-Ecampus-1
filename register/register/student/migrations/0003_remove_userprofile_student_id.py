# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20171118_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='student_id',
        ),
    ]