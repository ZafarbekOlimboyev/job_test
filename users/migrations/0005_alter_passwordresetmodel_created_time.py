# Generated by Django 5.0.6 on 2024-06-12 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_passwordresetmodel_created_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresetmodel',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 12, 14, 48, 13, 254041)),
        ),
    ]
