# Generated by Django 2.0.1 on 2018-04-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20180404_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='サムネイル'),
        ),
    ]
