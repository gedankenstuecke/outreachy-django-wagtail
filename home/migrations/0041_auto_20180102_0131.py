# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20180102_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcommunity',
            name='proprietary_software_description',
            field=models.CharField(blank=True, help_text='(Optional) If your community relies or builds upon proprietary software, please provide description of what software is used.', max_length=3000),
        ),
        migrations.AlterField(
            model_name='newcommunity',
            name='unapproved_license_description',
            field=models.CharField(blank=True, help_text='(Optional) If your community uses a license that is not an OSI-approved license or a Creative Commons license, please provide links to the licenses or a description.', max_length=3000),
        ),
    ]
