# Generated by Django 2.0.1 on 2018-04-04 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180404_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(blank=True, default='', verbose_name='サムネイル'),
        ),
    ]
