# Generated by Django 2.1.1 on 2018-10-05 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181004_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
