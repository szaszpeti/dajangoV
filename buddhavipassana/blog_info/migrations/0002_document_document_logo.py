# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_logo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
