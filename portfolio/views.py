from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# TODO views.py

def home_view(request):
    return render(request, 'portfolio/home.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentacao.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_view(request):
    return render(request, 'portfolio/formacao.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')
