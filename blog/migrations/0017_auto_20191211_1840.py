# Generated by Django 2.2.4 on 2019-12-11 13:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191211_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 11, 13, 10, 50, 120303, tzinfo=utc)),
        ),
    ]
