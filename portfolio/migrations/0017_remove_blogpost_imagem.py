# Generated by Django 4.0.6 on 2022-07-28 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_alter_trabalhofinalcurso_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='imagem',
        ),
    ]