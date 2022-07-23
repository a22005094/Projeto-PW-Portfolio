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
    professores = models.ManyToManyField(Pessoa, related_name='cadeiras')  # TODO recheck relatedName
    link_pagina = models.TextField(blank=True, max_length=300)
    feita = models.BooleanField(default=False)

    # *** OUTROS CAMPOS ***
    # [projetos] ~> related_name para a lista de Projeto (s) associados
    # #### [nome_curto] ~> models.CharField(max_length=10) # util para carregar imagens => possivel atributo p/ imgs

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    """ TODO terminar classe e aplicar na pagina
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
                                on_delete=models.CASCADE)  # TODO
    participantes = models.ManyToManyField(Pessoa, related_name='projetos')  # TODO recheck relatedName
    link_github = models.TextField(blank=True, max_length=300)
    tecnologias = models.ManyToManyField(Tecnologia, related_name='projetos')  # TODO review. Classe ou texto??

    # competencias # TODO. Pertence à classe Competencia. Em principio também será uma N:M ...
    # [link_youtube] || (Campo omitido)

    def __str__(self):
        return self.titulo


class Tecnologia(models.Model):
    """
        Descreve uma tecnologia utilizada para suportar o desenvolvimento de 1+ Projeto (s).
        Contém relação N:M com a Classe Projeto (1 Projeto usa N tecnologias, e essa pode estar em M projetos)
    """
    nome = models.CharField(max_length=20)
    acronimo = models.CharField(max_length=5)
    ano = models.IntegerField()
    autor = models.CharField(max_length=50)
    # logotipo => TODO
    link_pagina = models.TextField(max_length=300)
    descricao_features = models.TextField(max_length=500)
    contexto_usado = models.CharField(max_length=150)

    # [projetos] ~> related_name para a lista de Projeto (s) associados

    def __str__(self):
        return self.nome


class Competencia(models.Model):
    """
        TODO :: Considerar que isto seja já diretamente uma ENUM dentro da Classe Projeto,
                se não tiver uso em mais nenhum sítio, que senão, na classe Projeto...!!
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

    def __str__(self):
        return self.descricao


# ######### PENDENTES #########
# TODO :: TODOS PARA BAIXO!
# ######### ######### #########

class TrabalhoFinalCurso(models.Model):
    """
        Classe para descrever projetos desenvolvidos por ex-colegas do nosso Curso,
        desenvolvidos como Projeto Final em âmbito da Unidade Curricular TFC.
    """
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=50)
    orientador = models.CharField(max_length=50)  # TODO :: Class ? Texto?
    resumo = models.CharField(max_length=150)
    # imagem => TODO
    descricao = models.TextField(max_length=500)
    link_github = models.TextField(max_length=300)
    link_youtube = models.TextField(max_length=300)

    def __str__(self):
        return self.titulo


class Blog(models.Model):
    autor = models.CharField(max_length=50)
    data_pub = models.DateTimeField()  # TODO ??
    texto = models.TextField(max_length=500)
    # TODO => restantes campos...
    # def __str__(self):
    #    return self.nome_curso


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=50)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.pontuacao


class Formacao(models.Model):
    # ?
    nome_curso = models.CharField(max_length=100)
    descricao_curso = models.TextField(max_length=500)
    ano_conclusao = models.IntegerField()

    def __str__(self):
        return self.nome_curso


class ArtigoMedium(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    # imagem => TODO
    link_artigo = models.TextField(max_length=300)

    def __str__(self):
        return self.titulo
