# Generated by Django 4.0.6 on 2022-07-26 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_rename_blog_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='dataHora',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
