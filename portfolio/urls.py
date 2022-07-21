"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('home', views.home_view, name='home'),
    path('apresentacao', views.apresentacao_view, name='apresentacao'),
    path('competencias', views.competencias_view, name='competencias'),
    path('formacao', views.formacao_view, name='formacao'),
    path('licenciatura', views.licenciatura_view, name='licenciatura'),
    path('projetos', views.projetos_view, name='projetos'),
    path('contactos', views.contactos_view, name='contactos'),
]
