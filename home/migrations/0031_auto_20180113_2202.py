# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0030_auto_20180113_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='mentorapproval',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='participation',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='approval_status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('W', 'Withdrawn'), ('R', 'Rejected')], default='W', max_length=1),
        ),
    ]
