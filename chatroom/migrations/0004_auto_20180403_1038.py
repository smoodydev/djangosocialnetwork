# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 10:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatroom', '0003_auto_20180403_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatechat',
            name='allowed',
        ),
        migrations.AddField(
            model_name='privatechat',
            name='allowed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='other', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
