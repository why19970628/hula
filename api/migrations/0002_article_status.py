# Generated by Django 3.0.7 on 2020-06-18 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(1, '发布'), (2, '删除')], default=1, verbose_name='状态'),
        ),
    ]