# Generated by Django 2.0.1 on 2018-04-04 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180404_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.URLField(blank=True, null=True, verbose_name='サムネイル'),
        ),
    ]
