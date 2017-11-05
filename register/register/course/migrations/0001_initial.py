# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 07:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=100, null=True)),
                ('faculty', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]