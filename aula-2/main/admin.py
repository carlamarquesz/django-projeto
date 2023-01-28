from django.contrib import admin
#registrar no admnistrador do django nossa tabela Aluno
from .models import Aluno

admin.site.register(Aluno)