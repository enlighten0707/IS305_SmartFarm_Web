# Generated by Django 2.2.5 on 2021-06-19 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Monitor', '0004_auto_20210618_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='environment_monitor',
            name='hour_time',
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='day',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='hour',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='month',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='environment_monitor',
            name='year',
            field=models.FloatField(default=0),
        ),
    ]
