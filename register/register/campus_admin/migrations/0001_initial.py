# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-11-18 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('course', '0002_offeredin_acadyear'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('courseNo', models.CharField(default='', max_length=10, primary_key=True, serialize=False)),
                ('courseName', models.CharField(default='', max_length=100)),
                ('credits', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FeeReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiptId', models.CharField(blank=True, default='0', max_length=30)),
                ('status', models.CharField(blank=True, default='Not Paid', max_length=50)),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='course.OfferedIn')),
                ('semesterNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester+', to='course.OfferedIn')),
                ('studentId', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='student_id+', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='course.OfferedIn')),
                ('courseNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='course.course')),
                ('semesterNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester+', to='course.OfferedIn')),
            ],
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=4, null=True)),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='course.OfferedIn')),
                ('courseNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='course.course')),
                ('semesterNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester+', to='course.OfferedIn')),
                ('studentId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_id+', to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPI', models.FloatField(blank=True, default='', null=True)),
                ('acadYear', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='course.OfferedIn')),
                ('semesterNo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semester+', to='course.OfferedIn')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_id+', to='student.student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='registers',
            unique_together=set([('acadYear', 'semesterNo', 'courseNo', 'studentId')]),
        ),
        migrations.AlterUniqueTogether(
            name='offers',
            unique_together=set([('acadYear', 'semesterNo', 'courseNo')]),
        ),
        migrations.AlterUniqueTogether(
            name='feereceipt',
            unique_together=set([('acadYear', 'semesterNo', 'studentId')]),
        ),
    ]
