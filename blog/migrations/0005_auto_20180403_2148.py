# Generated by Django 2.0.1 on 2018-04-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180403_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='src',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/', verbose_name='画像'),
        ),
    ]
