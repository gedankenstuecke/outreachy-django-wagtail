# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 06:33
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_auto_20180109_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Description of the project, excluding applicant skills.'),
        ),
    ]
