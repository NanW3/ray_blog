# Generated by Django 2.1.2 on 2018-11-21 21:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
