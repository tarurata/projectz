# Generated by Django 2.0.1 on 2018-04-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.TextField(blank=True, default='', null=True, verbose_name='サムネイル'),
        ),
    ]
