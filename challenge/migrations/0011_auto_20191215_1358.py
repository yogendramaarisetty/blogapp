# Generated by Django 2.2.7 on 2019-12-15 08:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0010_auto_20191215_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 8, 28, 34, 49307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 15, 8, 28, 34, 49307, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
