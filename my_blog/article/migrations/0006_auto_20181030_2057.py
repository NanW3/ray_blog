# Generated by Django 2.1.2 on 2018-10-30 20:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20181030_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 30, 20, 57, 51, 518477, tzinfo=utc)),
        ),
    ]
