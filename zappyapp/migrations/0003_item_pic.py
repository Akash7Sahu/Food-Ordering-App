# Generated by Django 2.2 on 2019-05-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zappyapp', '0002_auto_20190520_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pic',
            field=models.FileField(default=-1.0, upload_to='images/'),
            preserve_default=False,
        ),
    ]