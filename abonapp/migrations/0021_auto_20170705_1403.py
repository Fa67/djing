# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devapp', '0006_auto_20170705_1403'),
        ('abonapp', '0020_auto_20170517_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abon',
            name='opt82',
        ),
        migrations.DeleteModel(
            name='Opt82',
        ),
        migrations.AddField(
            model_name='abon',
            name='dev_port',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devapp.Port'),
        ),
        migrations.AddField(
            model_name='abon',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devapp.Device'),
        ),
        migrations.AddField(
            model_name='abon',
            name='is_dynamic_ip',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='AbonDevice',
        ),
    ]
