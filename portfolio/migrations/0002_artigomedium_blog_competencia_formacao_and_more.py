# Generated by Django 4.0.6 on 2022-07-23 19:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoMedium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=500)),
                ('link_artigo', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=50)),
                ('data_pub', models.DateTimeField()),
                ('texto', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('TEC', 'Técnica'), ('ORG', 'Organizativa'), ('SOC', 'Social')], default='TEC', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=100)),
                ('descricao_curso', models.TextField(max_length=500)),
                ('ano_conclusao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PontuacaoQuizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('pontuacao', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('acronimo', models.CharField(max_length=5)),
                ('ano', models.IntegerField()),
                ('autor', models.CharField(max_length=50)),
                ('link_pagina', models.TextField(max_length=300)),
                ('descricao_features', models.TextField(max_length=500)),
                ('contexto_usado', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='TrabalhoFinalCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=50)),
                ('orientador', models.CharField(max_length=50)),
                ('resumo', models.CharField(max_length=150)),
                ('descricao', models.TextField(max_length=500)),
                ('link_github', models.TextField(max_length=300)),
                ('link_youtube', models.TextField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='unidade_curricular',
        ),
        migrations.AddField(
            model_name='projeto',
            name='ano',
            field=models.IntegerField(default=2020),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='cadeira',
            field=models.ForeignKey(blank=True, default=2020, on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='portfolio.unidadecurricular'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projeto',
            name='link_github',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='projeto',
            name='participantes',
            field=models.ManyToManyField(related_name='projetos', to='portfolio.pessoa'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='titulo',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='link_lusofona',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='projeto',
            name='tecnologias',
            field=models.ManyToManyField(related_name='projetos', to='portfolio.tecnologia'),
        ),
    ]
