from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
from django.urls import reverse
from portfolio.models import UnidadeCurricular, Projeto, Formacao, BlogPost, PontuacaoQuizz, Tecnologia


#
#  *** DISCLAIMER ***
#  Na construção de algumas das rotas, foi usado por referencia os projetos-template das "Tarefas" e "Flights",
#  fornecido pelos Docentes da Unidade Curricular. Como algumas funções se aproximavam bastante ao que
#  aqui era necessário, decidi usar as funções-base e aplicar ajustes. Portanto, será expectável encontrar semelhanças.
#  Forneço, então, os devidos Créditos aos Docentes, pelas funções-base que nos foram disponibilizadas.
#

def home_view(request):
    # Ajusta os cumprimentos apresentados ao user, conforme a hora em que este se esteja a ligar ao Site
    curr_time = datetime.datetime.now()

    if 6 <= curr_time.hour <= 12:
        greet = "bom dia"
    elif 13 <= curr_time.hour <= 19:
        greet = "boa tarde"
    else:
        greet = "boa noite"

    return render(request, 'portfolio/home.html', {
        'current_time': curr_time,
        'greetings': greet
    })


def educacao_view(request):
    # Obtem todas as formacoes armazenadas na base de dados;
    # Resultados ordenados descendente por ano de conclusao
    # Dica para a ordenacao decrescente com o '-':
    # https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending

    formacoes = Formacao.objects.all().order_by('-ano_conclusao')
    context = {'formacoes': formacoes}
    return render(request, 'portfolio/educacao.html', context)


# ROTAS SOBRE UNIDADES CURRICULARES
def licenciatura_view(request):
    form_fields = None

    if request.method == 'POST':
        # Submissao de formulario para inserir nova UnidadeCurricular
        if not request.user.is_authenticated:
            # Apenas como protecao adicional => caso um user não-autenticado
            # tenha conseguido submeter o formulario, encaminha-lo para o Login
            return HttpResponseRedirect(reverse('portfolio:login'))

        # Receber o form preenchido pelo user
        form = UnidadeCurricularForm(request.POST or None)
        if form.is_valid():
            # OK! Processar insercao da nova UnidadeCurricular e recarregar dados da página
            form.save()
        else:
            form_fields = form
    else:
        if request.user.is_authenticated:
            form_fields = UnidadeCurricularForm()  # Apresenta novo Form ao utilizador

    # Independentemente se foi um POST, carregar os dados da página
    ucs_a1s1 = UnidadeCurricular.objects.filter(ano=1, semestre=1)
    ucs_a1s2 = UnidadeCurricular.objects.filter(ano=1, semestre=2)
    ucs_a2s1 = UnidadeCurricular.objects.filter(ano=2, semestre=1)
    ucs_a2s2 = UnidadeCurricular.objects.filter(ano=2, semestre=2)
    ucs_a3s1 = UnidadeCurricular.objects.filter(ano=3, semestre=1)
    ucs_a3s2 = UnidadeCurricular.objects.filter(ano=3, semestre=2)
    context = {'a1s1': ucs_a1s1, 'a1s2': ucs_a1s2,
               'a2s1': ucs_a2s1, 'a2s2': ucs_a2s2,
               'a3s1': ucs_a3s1, 'a3s2': ucs_a3s2,
               'form': form_fields}

    return render(request, 'portfolio/licenciatura/licenciatura.html', context)


def ver_cadeira_view(request, cadeira_id):
    # Obter o objeto correspondente à cadeira selecionada,
    # para apresentar os seus detalhes. Preenche também o formulário com os seus detalhes
    # para permitir a sua edição por parte de utilizadores autenticados.
    # Permite tambem, em simultaneo, a gravação de dados no formulario, caso tenha sido um POST e o form esteja válido
    cadeira = UnidadeCurricular.objects.get(id=cadeira_id)
    cadeira_form = UnidadeCurricularForm(request.POST or None, instance=cadeira)

    if cadeira_form.is_valid():
        cadeira.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'cadeira': cadeira, 'form': cadeira_form}
    return render(request, 'portfolio/licenciatura/ver_cadeira.html', context)


def eliminar_cadeira_view(request, cadeira_id):
    cadeira = UnidadeCurricular.objects.get(id=cadeira_id)
    cadeira.delete()
    return HttpResponseRedirect(reverse('portfolio:licenciatura'))


# ROTAS SOBRE PROJETOS

# ***** OK! *****
def todos_projetos_view(request):
    """ Lista TODOS os projetos """
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos/projetos.html', context)


# ***** OK! *****
def projeto_view(request, projeto_id):
    """ Lista as informações de um Projeto em específico """
    context = {'projeto': Projeto.objects.get(pk=projeto_id)}
    return render(request, 'portfolio/projetos/ver_projeto.html', context)


# ***** OK! *****
@login_required
def projeto_novo_view(request):
    # No need... o Decorator trata disto automaticamente. ;)
    # if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse('portfolio:login'))

    form = ProjetoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:todos-projetos'))

    context = {'form': form}
    return render(request, 'portfolio/projetos/novo_projeto.html', context)


# ***** OK! *****
@login_required
def editar_projeto_view(request, projeto_id):
    # No need... o Decorator trata disto automaticamente. ;)
    # if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse('portfolio:login'))

    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:todos-projetos'))

    # Ou é um pedido GET (quando se abre a página), ou então o Form submetido não está válido.
    # (Re)Mostrar formulário de Editar
    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/projetos/editar_projeto.html', context)


# ***** OK! *****
@login_required
def eliminar_projeto_view(request, projeto_id):
    # No need... o Decorator trata disto automaticamente. ;)
    # if not request.user.is_authenticated:
    #    return HttpResponseRedirect(reverse('portfolio:login'))

    projeto = Projeto.objects.get(id=projeto_id)
    projeto.delete()
    return HttpResponseRedirect(reverse('portfolio:todos-projetos'))


# OUTRAS ROTAS

def contactos_view(request):
    return render(request, 'portfolio/contactos.html')


def about_view(request):
    tecnologias_usadas = Tecnologia.objects.filter(usada_projeto=True)
    context = {'tecnologias': tecnologias_usadas}
    return render(request, 'portfolio/sobre.html', context)


def blog_view(request):
    # Pedido POST :: processa a gravação de um novo Post (no pun intended) no Blog.
    form = BlogPostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    # Pedido GET (leitura de dados na página), OU gravação do Post teve erro:
    #  => carrega os Posts do blog, ordenados em descendente por DataHora.
    posts = BlogPost.objects.all().order_by('-dataHora')
    context = {'posts': posts, 'form': form}
    return render(request, 'portfolio/blog.html', context)


def prog_web_view(request):
    tec_frontend = Tecnologia.objects.filter(tipo_tecnologia='F')
    tec_backend = Tecnologia.objects.filter(tipo_tecnologia='B')
    tec_outras = Tecnologia.objects.filter(tipo_tecnologia='O')
    context = {'tecnologias_front': tec_frontend, 'tecnologias_back': tec_backend, 'tecnologias_outras': tec_outras}
    return render(request, 'portfolio/prog-web.html', context)


def quiz_view(request):
    # Carrega o formulário (GET) apenas com texto descritivo sobre o Quiz.
    # Adicionalmente, se ja existir um "podium" de classificacoes, envia esses dados
    top_3 = PontuacaoQuizz.objects.all().order_by('-pontuacao')[:3]
    context = {'topscores': top_3}
    return render(request, 'portfolio/quiz/quiz.html', context)


def gravar_quiz_view(request):
    if request.method == 'POST':
        participante = request.POST['nome-participante']
        pontos = 0
        total_pontuacao = 10  # O maximo que se conseguiria atingir neste Quiz

        # CALCULAR PONTUACAO (Min: 0 ; Max: 10 ; 2 pts por pergunta)
        # > Pergunta1 => Resposta certa: "C"
        if request.POST['pergunta1'] == 'C':
            pontos += 2

        # > Pergunta2 => Respostas certas: "B", "D" (1 pt por opcao certa)
        # Aqui desconta-se por respostas erradas, apenas para equilibrar contra as corretas
        # No final só se soma se o resultado foi positivo - impede-se que a pergunta desconte
        aux = 0
        if request.POST.get('p2_CheckA'):
            aux -= 1
        if request.POST.get('p2_CheckB'):
            aux += 1
        if request.POST.get('p2_CheckC'):
            aux -= 1
        if request.POST.get('p2_CheckD'):
            aux += 1
        if request.POST.get('p2_CheckE'):
            aux -= 1
        if aux > 0:
            pontos += aux

        # > Pergunta3 => Respostas certas: "D"
        if request.POST['pergunta3'] == 'D':
            pontos += 2
        # > Pergunta4 => Resposta certa: "C"
        if request.POST['pergunta4'] == 'C':
            pontos += 2
        # > Pergunta5 => Resposta certa: 27
        if int(request.POST['pergunta5']) == 27:
            pontos += 2
        # Gravar novo Score na BD
        nova_pontuacao = PontuacaoQuizz(nome=participante, pontuacao=pontos)
        nova_pontuacao.save()

        # Fornecer parametros pelas vars. de sessao, antes de abrir a nova página (serão lidos na página seguinte)
        request.session['pontos_quiz'] = pontos
        request.session['total_pontuacao_quiz'] = total_pontuacao
        return HttpResponseRedirect(reverse('portfolio:resultados-quiz'))

    return render(request, 'portfolio/quiz/quiz-responder.html')


def resultados_quiz_view(request):
    pontos_quiz = request.session['pontos_quiz']  # buscar da sessao o objeto da Nova pontuacao
    total_score_quiz = request.session['total_pontuacao_quiz']  # buscar da sessao o total de pontuacao do Quiz
    # Calcular percentagem de certas para mostrar na página dos resultados
    percentagem_certas = ((pontos_quiz * 100.0) / total_score_quiz)
    context = {'pontos_quiz': pontos_quiz, 'total_score_quiz': total_score_quiz,
               'percentagem_certas': percentagem_certas}
    return render(request, 'portfolio/quiz/quiz-resultados.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Tentar fazer autenticacao com os dados fornecidos
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            # Reabrir página com mensagem de erro. O Login falhou.
            return render(request, 'portfolio/autenticacao/login.html', {
                'msg_erro': 'ERRO: Credenciais inválidas!'
            })
    else:
        # Pressupõe-se que é um pedido GET.
        # Redireciona para o formulário de Login.
        return render(request, 'portfolio/autenticacao/login.html')


def logout_view(request):
    if request.method == 'POST':
        # O único POST feito na página do LOGOUT é quando se clica no botão para terminar sessão
        # Assume-se então, que o único POST feito foi para fazer Logout.
        logout(request)
        return HttpResponseRedirect(reverse('portfolio:home'))
    else:
        # Pressupõe-se que é um pedido GET.
        # Será para o lançamento da página inicial de onde se pode fazer Logout.
        return render(request, 'portfolio/autenticacao/logout.html')
