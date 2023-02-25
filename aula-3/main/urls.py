from django.urls import path
from . import views

urlpatterns = [
    path(
        "", views.alunoView, name="aluno-lista"
    ),  # Estou chamando minha funcao alunoview
    path("aluno/<int:id>", views.alunoIdView, name="aluno-view"),
    path("exemplo", views.exemplo, name="exemplo"),
    path("newaluno/", views.newAluno, name="new-aluno"),
]
