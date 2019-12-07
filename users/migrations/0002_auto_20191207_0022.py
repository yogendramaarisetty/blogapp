# Generated by Django 2.2.7 on 2019-12-06 18:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='rollnumber',
            field=models.CharField(default=datetime.datetime(2019, 12, 6, 18, 52, 17, 854494, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
