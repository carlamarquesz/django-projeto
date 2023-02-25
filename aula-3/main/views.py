from django.shortcuts import redirect, render, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib import messages

# faz os tratamentos dos dados
# importa a tabela Aluno


def alunoView(request):
    alunos = Aluno.objects.all().order_by(
        "nome"
    )  # variavel aluno recebe todos os objetos dentro de Aluno(nome,descricao...etc)
    return render(
        request, "main/list.html", {"alunos": alunos}
    )  # vai renderizar esses alunos em uma pagina html (list), convertendo em json (dicionario)


def alunoIdView(request, id):
    aluno = get_object_or_404(
        Aluno, pk=id
    )  # Vai ver se tem o Id na classe Alunos, se nao tiver retorna pagina 404
    return render(request, "main/aluno.html", {"aluno": aluno})


def exemplo(request):
    if request.method == "POST":
        name = request.POST.get("nome", None)
        email = request.POST.get("email", None)
        telefone = request.POST.get("telefone", None)
        print(name, email, telefone)
        # Aluno.objects.create(nome=name,email=email,telefone=telefone)
    return render(request, "main/indexx.html")


""" 
O código verifica se a requisição é uma solicitação POST ou não. 
Se for uma solicitação POST, o código cria um formulário de Aluno a partir dos dados enviados na requisição, 
verifica se o formulário é válido e, se for válido, cria um novo objeto Aluno com base nos dados do formulário 
e salva esse objeto no banco de dados. Em seguida, o código redireciona o usuário para a página inicial.
"""


def newAluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            messages.success(request, "Usuário cadastrado com sucesso!", "success-add")
            return redirect("/")
    else:
        form = AlunoForm()
    return render(request, "main/add_aluno.html", {"form": form})


def editAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    form = AlunoForm(instance=aluno)
    if request.method == "POST":
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            aluno.save()
            return redirect("/")
        else:
            return render(
                request, "main/edit_aluno.html", {"form": form, "aluno": aluno}
            )
    else:
        return render(request, "main/edit_aluno.html", {"form": form, "aluno": aluno})


def deleteAluno(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    messages.success(request, "Usuário removido com sucesso!", "success-remove")
    return redirect("/")
