# Generated by Django 3.0 on 2019-12-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0020_auto_20191222_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcases',
            name='input1',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='input2',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='input3',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='input4',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='input5',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='output1',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='output2',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='output3',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='output4',
            field=models.TextField(default='', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='testcases',
            name='output5',
            field=models.TextField(default='', max_length=1000000),
        ),
    ]
