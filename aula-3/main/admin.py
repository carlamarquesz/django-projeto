from django.contrib import admin

from .models import Aluno
#indicar para o meu admin a estrutura do banco criada.
admin.site.register(Aluno)