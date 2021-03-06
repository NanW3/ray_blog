# Generated by Django 2.1.2 on 2018-11-21 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20181121_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadNum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='articlepost',
            name='read_number',
        ),
        migrations.AddField(
            model_name='readnum',
            name='articlepost',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='article.ArticlePost'),
        ),
    ]
