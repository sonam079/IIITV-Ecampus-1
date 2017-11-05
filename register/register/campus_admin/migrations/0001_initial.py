# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Registers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(blank=True, max_length=4, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SPI', models.FloatField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acadYear', models.CharField(default='', max_length=200)),
                ('semesterNo', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('studentId', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('studentName', models.CharField(default='', max_length=100)),
                ('batch', models.CharField(default='', max_length=20)),
                ('programName', models.CharField(default='', max_length=20, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='semester',
            unique_together=set([('acadYear', 'semesterNo')]),
        ),
        migrations.AddField(
            model_name='result',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='result',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='result',
            name='studentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentId+', to='campus_admin.Student'),
        ),
        migrations.AddField(
            model_name='registers',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='registers',
            name='courseNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='campus_admin.Courses'),
        ),
        migrations.AddField(
            model_name='registers',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='registers',
            name='studentId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registers_studentId', to='campus_admin.Student'),
        ),
        migrations.AddField(
            model_name='offers',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='offers',
            name='courseNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseNo+', to='campus_admin.Courses'),
        ),
        migrations.AddField(
            model_name='offers',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='feereceipt',
            name='acadYear',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acadYear+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='feereceipt',
            name='semesterNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterNo+', to='campus_admin.Semester'),
        ),
        migrations.AddField(
            model_name='feereceipt',
            name='studentId',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='feereceipt_studentId', to='campus_admin.Student'),
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
