import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Pessoa(models.Model):
    """
        Define a classe Pessoa, usada para representar, por exemplo, os Docentes de uma UC.
        Contém relação N:M com as classes UnidadeCurricular e Projeto.

        *NOTA*: O campo 'Link do LinkedIn' foi propositadamente desativado, por ter existido dificuldade
        em encontrar uma quantidade de links suficientes para justificar a inclusão deste campo no Modelo.
    """
    nome = models.CharField(max_length=50)
    link_lusofona = models.TextField(blank=True, max_length=300)

    # [cadeiras] ~> related_name para a lista de UnidadesCurricular (es) que leciona (se referenciar um Docente)
    # [projetos] ~> related_name para a lista de Projeto (s) associados
    # [autor_tfc] ~> related_name para a lista de TFCs em que o objeto é Autor
    # [orientador_tfc] ~> related_name para a lista de TFCs em que o objeto é Orientador
    # [link_linkedin] || (Campo omitido)

    def __str__(self):
        return self.nome


class UnidadeCurricular(models.Model):
    """
        Classe que caracteriza as Unidades Curriculares listadas nas páginas.
        Permite, a partir desta, a criação de objetos Projeto que contêm esta cadeira como o âmbito (relação 1:N)
    """
    nome = models.CharField(max_length=50)
    ano = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
    semestre = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    ects = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(30)])
    ano_letivo_freq = models.CharField(blank=True, max_length=7,
                                       validators=[RegexValidator(regex=r"\d\d\d\d\/\d\d")])  # exemplo: '2021/22'
    topicos = models.TextField(max_length=300)
    ranking = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    professores = models.ManyToManyField(Pessoa, related_name='cadeiras')
    link_pagina = models.TextField(blank=True, max_length=300)
    feita = models.BooleanField(default=False)

    # *** OUTROS CAMPOS ***
    # [projetos] ~> related_name para a lista de Projeto (s) associados

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    """
        Descreve uma tecnologia utilizada para suportar o desenvolvimento de 1+ Projeto (s).
        Contém relação N:M com a Classe Projeto (1 Projeto usa N tecnologias, e essa pode estar em M projetos)
    """

    # Classe interna, para atribuir um tipo a cada tecnologia (FrontEnd / BackEnd / Outras)
    class TiposTecnologia(models.TextChoices):
        FRONT_END = 'F', 'Front-end'
        BACK_END = 'B', 'Back-end'
        OUTRAS = 'O', 'Outras'
        LINGUAGEM_PROG = 'P', 'Linguagem de Programação'

    nome = models.CharField(max_length=100)
    acronimo = models.CharField(max_length=10)
    ano = models.IntegerField()
    autor = models.CharField(max_length=50)
    link_pagina = models.TextField(max_length=300)
    descricao_features = models.TextField(max_length=500)
    contexto_usado = models.CharField(max_length=150, blank=True)

    # [projetos] ~> related_name para a lista de Projeto (s) associados
    # Campos custom na Classe #
    usada_projeto = models.BooleanField(default=False)  # Indica se foi usada neste Projeto (util @"Sobre a Pagina")
    tipo_tecnologia = models.CharField(
        max_length=1,
        choices=TiposTecnologia.choices,
        default=TiposTecnologia.OUTRAS
    )

    # logotipo |=> nao usado

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    """
        Classe para descrever Competencias. Usa um genero de Enum, com tipos de Competencias previamente definidos,
        para que, no momento da criacao de uma Competencia, se selecione um dos tipos pré-existentes.
    """

    class TiposCompetencia(models.TextChoices):
        TECNICA = 'TEC', 'Técnica'
        ORGANIZATIVA = 'ORG', 'Organizativa'
        SOCIAL = 'SOC', 'Social'

    descricao = models.CharField(max_length=100)
    tipo = models.CharField(
        max_length=3,
        choices=TiposCompetencia.choices,
        default=TiposCompetencia.TECNICA,
    )

    # [projetos] ~> related_name para a lista de Projeto (s) associados

    def __str__(self):
        return self.descricao


class Projeto(models.Model):
    """
        Classe que descreve Projetos desenvolvidos em âmbito de Unidades Curriculares deste Curso.
        Contém relação N:M com as classes Pessoa e Tecnologia, e 1:N com a classe UnidadeCurricular
        (esta classe é a dependente, contendo a "chave estrangeira").

        *NOTA*: O campo 'Link para Youtube' foi propositadamente omitido, por infelizmente não ter conseguido
        resgatar os links dos (poucos) projetos em que foi solicitada gravação de vídeo e publicação no Youtube... :(
    """
    titulo = models.CharField(max_length=20)
    descricao = models.TextField(max_length=500)
    # imagem => TODO
    ano = models.IntegerField()
    cadeira = models.ForeignKey(UnidadeCurricular, blank=True, related_name='projetos',
                                on_delete=models.CASCADE)
    participantes = models.ManyToManyField(Pessoa, related_name='projetos')
    link_github = models.TextField(blank=True, max_length=300)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')
    competencias = models.ManyToManyField(Competencia, related_name='projetos')

    # [link_youtube] || (Campo omitido)

    def __str__(self):
        return self.titulo


class Formacao(models.Model):
    """
        Classe para descrever as formacoes que realizei ao longo do meu percurso Académico
    """
    nome_curso = models.CharField(max_length=100)
    descricao_curso = models.TextField(max_length=500)
    ano_inicio = models.IntegerField()
    ano_conclusao = models.IntegerField()
    local = models.CharField(max_length=50)
    link_instituicao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome_curso


class BlogPost(models.Model):
    autor = models.CharField(max_length=50)
    dataHora = models.DateTimeField(default=datetime.datetime.now)
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=500)
    imagem = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

    def __str__(self):
        return f"{self.nome}: {self.pontuacao} pontos"


# TODO
class TrabalhoFinalCurso(models.Model):
    """
        Classe para descrever projetos desenvolvidos por ex-colegas do nosso Curso,
        desenvolvidos na componente de Projeto Final em âmbito da Unidade Curricular de TFC.
    """
    titulo = models.CharField(max_length=20)
    autores = models.ManyToManyField(Pessoa, related_name='autor_tfc')
    orientadores = models.ManyToManyField(Pessoa, related_name='orientador_tfc')
    ano_realizado = models.IntegerField()
    sumario = models.CharField(max_length=150)
    resumo = models.TextField(max_length=500)
    link_github = models.TextField(max_length=300, blank=True)
    link_youtube = models.TextField(max_length=300, blank=True)

    # imagem => TODO

    def __str__(self):
        return self.titulo


# TODO
class NoticiaMedium(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)  # RESUMIDO! 3 linhas
    link_artigo = models.TextField(max_length=300)

    def __str__(self):
        return self.titulo
