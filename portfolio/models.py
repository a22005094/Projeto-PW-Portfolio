from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


# TODO registar modelos para estarem visiveis no BackOffice do Django
# TODO criar um superuser

class Pessoa(models.Model):
    """
        Define a classe Pessoa, usada para representar, por exemplo, os Docentes de uma UC.
        *NOTA*: O campo 'Link do LinkedIn' foi propositadamente desativado, por ter existido dificuldade
        em encontrar uma quantidade de links suficientes para justificar a inclusão deste campo no Modelo.
    """
    nome = models.CharField(max_length=50)
    link_lusofona = models.TextField(blank=True, max_length=300)

    # [link_linkedin] ~> (propositadamente inutilizado)
    # [cadeiras] ~> (related_name de ligação para a lista de UnidadesCurriculares lecionadas)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    """
        Classe que caracteriza as Unidades Curriculares listadas nas páginas
    """
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    semestre = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    ects = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    ano_letivo_freq = models.CharField(blank=True, max_length=7,
                                       validators=[RegexValidator(regex=r"\d\d\d\d\/\d\d")])  # exemplo: '2021/22'
    topicos = models.TextField(max_length=300)  # TODO review tipo de dados a usar aqui
    ranking = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    professores = models.ManyToManyField(Pessoa, related_name='cadeiras')  # TODO check funcionamento relatedName
    link_pagina = models.TextField(blank=True, max_length=300)
    feita = models.BooleanField(default=False)

    # *** OUTROS CAMPOS ***
    # [projetos] ~> (related_name que faz ligação para a lista de Projetos associados) # TODO check
    # nome_curto = models.CharField(max_length=10) # util para carregar imagens => possivel atributo p/ imagens

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    """ TODO
        Classe que caracteriza Projetos desenvolvidos no âmbito de Unidades Curriculares do Curso
    """
    unidade_curricular = models.ForeignKey(UnidadeCurricular, related_name='projetos', on_delete=models.CASCADE)

    def __str__(self):
        return "PROJETO"  # todo fix me!
