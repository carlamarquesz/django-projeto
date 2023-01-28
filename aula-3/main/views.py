from django.shortcuts import render,get_object_or_404
from.models import Aluno
#faz os tratamentos dos dados
#importa a tabela Aluno

def alunoView(request):
    alunos = Aluno.objects.all() #variavel aluno recebe todos os objetos dentro de Aluno(nome,descricao...etc)
    return render(request, 'main/list.html', {'alunos':alunos}) #vai renderizar esses alunos em uma pagina html (list), convertendo em json (dicionario)

