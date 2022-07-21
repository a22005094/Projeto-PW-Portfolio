from django.shortcuts import render
import datetime

from portfolio.models import UnidadeCurricular


def home_view(request):
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


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def licenciatura_view(request):
    cadeiras_a1s1 = UnidadeCurricular.objects.filter(ano=1, semestre=1)
    cadeiras_a1s2 = UnidadeCurricular.objects.filter(ano=1, semestre=2)
    cadeiras_a2s1 = UnidadeCurricular.objects.filter(ano=2, semestre=1)
    cadeiras_a2s2 = UnidadeCurricular.objects.filter(ano=2, semestre=2)
    cadeiras_a3s1 = UnidadeCurricular.objects.filter(ano=3, semestre=1)
    cadeiras_a3s2 = UnidadeCurricular.objects.filter(ano=3, semestre=2)
    context = {'a1s1': cadeiras_a1s1, 'a1s2': cadeiras_a1s2,
               'a2s1': cadeiras_a2s1, 'a2s2': cadeiras_a2s2,
               'a3s1': cadeiras_a3s1, 'a3s2': cadeiras_a3s2}

    return render(request, 'portfolio/licenciatura.html', context)


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def contactos_view(request):
    return render(request, 'portfolio/contactos.html')
