# Generated by Django 2.1 on 2018-11-15 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tariff_app', '0002_auto_20180807_1548'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='periodicpay',
            options={'ordering': ('-id',), 'verbose_name': 'Periodic pay', 'verbose_name_plural': 'Periodic pays'},
        ),
    ]
