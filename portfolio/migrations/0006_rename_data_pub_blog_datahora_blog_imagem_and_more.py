# Generated by Django 4.0.6 on 2022-07-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_formacao_ano_inicio_formacao_local'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='data_pub',
            new_name='dataHora',
        ),
        migrations.AddField(
            model_name='blog',
            name='imagem',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='titulo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
