# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 23:51
from __future__ import unicode_literals

from django.db import migrations, models

import mydefs


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpPoolItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', mydefs.MyGenericIPAddressField(max_length=8, protocol=b'IPv4')),
            ],
        ),
    ]
