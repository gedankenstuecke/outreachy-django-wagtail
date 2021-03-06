# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-09 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_project_long_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='communication_norms',
            field=models.CharField(blank=True, help_text='(Optional) After following the project communication channel link, are there any special instructions? E.g. Join this Zulip channel. ', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='communication_url',
            field=models.URLField(blank=True, help_text='(Optional) URL for your project`s communication channel. For IRC, use irc://<host>[:port]/[channel]. Since many applicants have issues with IRC port blocking at their universities, IRC communication links will use <a href="https://kiwiirc.com/">Kiwi IRC</a> to embed the IRC communications in the project page.'),
        ),
    ]
