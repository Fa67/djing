# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djing.fields


class Migration(migrations.Migration):

    dependencies = [
        ('devapp', '0005_auto_20170502_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portstates',
            name='port',
        ),
        migrations.RemoveField(
            model_name='port',
            name='speed',
        ),
        migrations.AddField(
            model_name='device',
            name='mac_addr',
            field=djing.fields.MACAddressField(blank=True, integer=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='device',
            name='parent_dev',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='devapp.Device'),
        ),
        migrations.AddField(
            model_name='port',
            name='descr',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='devtype',
            field=models.CharField(choices=[('Dl', 'DLink switch'), ('Pn', 'PON OLT'), ('On', 'PON ONU')], default='Dl', max_length=2),
        ),
        migrations.DeleteModel(
            name='PortStates',
        ),
    ]
