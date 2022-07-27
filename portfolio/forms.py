from django.forms import ModelForm
from .models import UnidadeCurricular, Projeto, TrabalhoFinalCurso, BlogPost


class UnidadeCurricularForm(ModelForm):
    class Meta:
        model = UnidadeCurricular
        fields = '__all__'

        # ferramentas
        # widgets = {
        #    'titulo': forms.TextInput(attrs={
        #    'class': 'form-control',
        #    'placeholder': 'descrição da tarefa...'}),
        #
        #    'prioridade': forms.NumberInput(attrs={
        #    'class': 'form-control' ,
        #    'max': 3,
        #    'min': 1}),
        # }

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


# TODO finish
class TrabalhoFinalCursoForm(ModelForm):
    class Meta:
        model = TrabalhoFinalCurso
        fields = '__all__'

        help_texts = {
            # 'titulo': 'Máx. 20 caracteres',
            # 'descricao': 'Máx. 500 caracteres',
            # 'ano': 'Ano de realização do projeto',
            # 'cadeira': 'De que UC foi âmbito?',
            # 'participantes': 'Pode selecionar vários participantes (CTRL-Click)',
            # 'link_github': '(O link é opcional)',
            # 'tecnologias': 'Pode selecionar várias tecnologias (CTRL-Click)',
            # 'competencias': 'Pode selecionar várias competências (CTRL-Click)',
        }


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        exclude = ['dataHora']  # retira do Form o campo da DataHora, pois é insercao automatica
        labels = {
            'autor': 'Nome',
            'titulo': 'Título'
        }

        help_texts = {
            'autor': 'Indique o seu nome',
            'titulo': 'Título que dê contexto à mensagem'
        }
