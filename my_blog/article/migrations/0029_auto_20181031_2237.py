# Generated by Django 2.1.2 on 2018-10-31 22:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0028_auto_20181031_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 22, 37, 3, 221628, tzinfo=utc)),
        ),
    ]
