# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20180408_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='img_tall',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]