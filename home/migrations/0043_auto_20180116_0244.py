# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-16 02:44
from __future__ import unicode_literals

import ckeditor.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20180116_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationchannel',
            name='url',
            field=models.CharField(help_text='URL for the communication channel applicants will use to reach mentors and ask questions about this internship project. IRC URLs should be in the form irc://&lt;host&gt;[:port]/[channel]. Since many applicants have issues with IRC port blocking at their universities, IRC communication links will use <a href="https://kiwiirc.com/">Kiwi IRC</a> to direct applicants to a web-based IRC client. If this is a mailing list, the URL should be the mailing list subscription page.', max_length=200, validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'irc'])]),
        ),
        migrations.AlterField(
            model_name='project',
            name='community_benefits',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) How will this internship project benefit the FOSS community that is funding it?', max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='intern_benefits',
            field=ckeditor.fields.RichTextField(blank=True, help_text="(Optional) How will the intern benefit from working with your team on this project? Imagine you're pitching this internship to a promising candidate. What would you say to convince them to apply? For example, what technical and non-technical skills will they learn from working on this project? How will this help them further their career in open source?", max_length=800),
        ),
        migrations.AlterField(
            model_name='project',
            name='intern_tasks',
            field=ckeditor.fields.RichTextField(blank=True, help_text='(Optional) Description of possible internship tasks.', max_length=800),
        ),
    ]
