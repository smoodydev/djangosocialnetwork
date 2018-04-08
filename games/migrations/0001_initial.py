# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-03 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('blurb', models.TextField(blank=True, max_length=140)),
                ('bio', models.TextField(blank=True, max_length=800)),
                ('release_date', models.DateTimeField()),
                ('reviews_num', models.IntegerField()),
                ('reviews_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('blurb', models.TextField(blank=True, max_length=140)),
                ('bio', models.TextField(blank=True, max_length=800)),
                ('contact', models.CharField(blank=True, max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('validated', models.BooleanField(default=False)),
                ('publisheradmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Publisher'),
        ),
    ]