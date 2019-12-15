# Generated by Django 2.2.7 on 2019-12-15 07:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0009_auto_20191215_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 7, 19, 56, 187503, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 7, 19, 56, 187503, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
