from django.db import models
#Aluno é a tabela usando sqlite
# make migrations preparar os campos da tabela(variaveis) , preparar a migração
# migrate insere as informaçoes no banco de dados
class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.IntegerField()
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.nome