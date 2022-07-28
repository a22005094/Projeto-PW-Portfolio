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
    path('educacao', views.educacao_view, name='educacao'),
    path('contactos', views.contactos_view, name='contactos'),
    path('about', views.about_view, name='sobre'),
    path('blog', views.blog_view, name='blog'),
    path('api', views.api_view, name='api'),
    path('prog-web', views.prog_web_view, name='prog-web'),

    # ROTAS SOBRE O QUIZ
    path('quiz', views.quiz_view, name='quiz'),  # Abre a página inicial (apenas indica os Top scores)
    path('novo-quiz', views.gravar_quiz_view, name='novo-quiz'),  # Mostra o Quiz e permite submeter as respostas
    path('resultados-quiz', views.resultados_quiz_view, name='resultados-quiz'),  # Mostra os resultados do Quiz

    # ROTAS CRUD - UNIDADES CURRICULARES
    # [NOTA1] a rota para Inserir cadeira não foi gerada, porque já é tratada no POST da 'portfolio:licenciatura'.
    # [NOTA2] a rota para Editar cadeira não foi gerada, porque já é tratada no POST da 'portfolio:ver-cadeira'.
    path('licenciatura', views.licenciatura_view, name='licenciatura'),  # lista cadeiras & permite adicionar cadeira
    path('cadeira/<int:cadeira_id>', views.ver_cadeira_view, name='ver-cadeira'),  # permite Ver, Editar & Remover
    # path('cadeiras/adicionar', views.cadeira_nova_view, name='nova-cadeira'), => nao usada
    # path('cadeiras/<int:cadeira_id>/edit', views.editar_cadeira_view, name='editar-cadeira'), => nao usada
    path('cadeira/<int:cadeira_id>/delete', views.eliminar_cadeira_view, name='eliminar-cadeira'),

    # ROTAS CRUD - PROJETOS
    path('projetos', views.todos_projetos_view, name='todos-projetos'),
    path('projetos/<int:projeto_id>', views.projeto_view, name='ver-projeto'),
    path('projetos/adicionar', views.projeto_novo_view, name='novo-projeto'),
    path('projetos/<int:projeto_id>/edit', views.editar_projeto_view, name='editar-projeto'),
    path('projetos/<int:projeto_id>/delete', views.eliminar_projeto_view, name='eliminar-projeto'),

    # ROTAS CRUD - TFCs
    path('tfcs', views.todos_tfcs_view, name='todos-tfcs'),  # permite Consultar lista TFCs + Inserir TFC
    path('tfcs/<int:tfc_id>', views.ver_tfc_view, name='ver-tfc'),  # permite consultar um TFC + Editar o TFC
    # esta rota abaixo permite Eliminar o TFC consultado @ portfolio:ver-tfc
    path('tfcs/<int:tfc_id>/delete', views.eliminar_tfc_view, name='eliminar-tfc'),

    # ROTAS PARA AUTENTICAÇÃO
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
