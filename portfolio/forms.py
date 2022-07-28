from django.forms import ModelForm
from .models import UnidadeCurricular, Projeto, TrabalhoFinalCurso, BlogPost


class UnidadeCurricularForm(ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = '__all__'

        help_texts = {
            'nome': 'Máx. 50 caracteres',
            'ano': 'Insira o ano do curso (de 1 a 3)',
            'semestre': 'Qual semestre? (1 ou 2)',
            'ects': 'Minimo: 1 ECTS',
            'ano_letivo_freq': 'Exemplo: 2021/22',
            'topicos': 'Máx. 300 caracteres para os tópicos',
            'ranking': 'Ranking entre 1 a 5',
            'professores': 'Pode selecionar vários Professores (CTRL-Click)',
            'link_pagina': '(O link é opcional)',
            'feita': 'Marcar caixa se a Unidade Curricular foi concluída'
        }

        labels = {
            'topicos': 'Tópicos',
            'link_pagina': 'Link da UC',
            'feita': 'Concluída?'
        }


class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link_github': 'Link do Github',
            'competencias': 'Competências'
        }

        help_texts = {
            'titulo': 'Máx. 20 caracteres',
            'descricao': 'Máx. 500 caracteres',
            'ano': 'Ano de realização do projeto',
            'cadeira': 'De que UC foi âmbito?',
            'participantes': 'Pode selecionar vários participantes (CTRL-Click)',
            'link_github': '(O link é opcional)',
            'tecnologias': 'Pode selecionar várias tecnologias (CTRL-Click)',
            'competencias': 'Pode selecionar várias competências (CTRL-Click)',
        }


class TrabalhoFinalCursoForm(ModelForm):
    class Meta:
        model = TrabalhoFinalCurso
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'ano_realizado': 'Ano',
            'sumario': 'Sumário',
            'link_github': 'Link do Github',
            'link_youtube': 'Link do Youtube',
        }

        help_texts = {
            'titulo': 'Máx. 50 caracteres',
            'autores': 'Pode selecionar vários autores (CTRL-Click)',
            'orientadores': 'Pode selecionar vários orientadores (CTRL-Click)',
            'ano_realizado': 'Em que ano foi realizado?',
            'sumario': 'Máx. 150 caracteres',
            'resumo': 'Máx. 500 caracteres',
            'link_github': '(O link é opcional)',
            'link_youtube': '(O link é opcional)',
        }


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ['dataHora']  # retira do Form o campo da DataHora, pois vai ser insercao automatica (default value)
        labels = {
            'autor': 'Nome',
            'titulo': 'Título'
        }

        help_texts = {
            'autor': 'Indique o seu nome',
            'titulo': 'Título que dê contexto à mensagem'
        }
