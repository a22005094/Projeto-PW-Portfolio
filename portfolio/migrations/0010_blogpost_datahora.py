# Generated by Django 4.0.6 on 2022-07-26 23:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_remove_blogpost_datahora'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='dataHora',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]