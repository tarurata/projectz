# Generated by Django 2.0.1 on 2018-04-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180404_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(blank=True, default='', null=True, verbose_name='サムネイル'),
        ),
    ]
