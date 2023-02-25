from django.db import models
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    nome = models.CharField(max_length=254)
    telefone = models.CharField(null=True, blank=True,max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    description = models.TextField()
    #assim que criar o aluno o created ele vai pegar data atual q foi criado devido o auto now,
    #padrao de projeto de filtro pra voltar sempre dos cadastro mais recentes
    created_at = models.DateTimeField(auto_now_add=True) #Implementado automaticamente
    #atualizar a data
    updated_at = models.DateTimeField(auto_now=True) #Implementado automaticamente
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)  #Tudo que for referente ao usuario ele vai ser deletado (Em cascata)
    
    def __str__(self):
        return self.nome
