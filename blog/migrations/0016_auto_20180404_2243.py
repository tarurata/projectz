# Generated by Django 2.0.1 on 2018-04-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20180404_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.TextField(blank=True, default='', max_length=255, null=True, verbose_name='サムネイル'),
        ),
    ]
