# Generated by Django 4.0.6 on 2022-07-26 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_blogpost_datahora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='dataHora',
        ),
    ]
