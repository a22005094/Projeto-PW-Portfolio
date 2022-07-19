from django.shortcuts import render
import datetime


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


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')


def contactos_view(request):
    return render(request, 'portfolio/contactos.html')
