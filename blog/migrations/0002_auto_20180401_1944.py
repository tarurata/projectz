# Generated by Django 2.0.1 on 2018-04-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank='True', null='True', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(default='名前', max_length=30, verbose_name='お名前'),
        ),
    ]
