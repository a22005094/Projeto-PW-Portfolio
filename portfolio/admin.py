from django.contrib import admin
from .models import *

# Registar aqui todos os Modelos gerados,
# para serem geríveis @ BackOffice Django!

admin.site.register(Pessoa)
admin.site.register(UnidadeCurricular)
admin.site.register(Projeto)
admin.site.register(Tecnologia)
admin.site.register(Competencia)
admin.site.register(TrabalhoFinalCurso)
admin.site.register(BlogPost)
admin.site.register(PontuacaoQuizz)
admin.site.register(Formacao)
