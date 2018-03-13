# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-16 19:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskapp', '0008_auto_20161213_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='device',
        ),
        migrations.RemoveField(
            model_name='task',
            name='recipient',
        ),
        migrations.AddField(
            model_name='task',
            name='recipients',
            field=models.ManyToManyField(related_name='them_task', to=settings.AUTH_USER_MODEL),
        )
    ]