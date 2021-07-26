from typing import final
from django.db import models
from django.db.models import fields
from django.db.models.enums import Choices

# Create your models here.
class Contact(models.Model):
    nome = models.CharField(null=False, max_length=30)
    apelido = models.CharField(null=False, max_length=30)
    telefone = models.CharField(null=False, max_length=12)
    email = models.EmailField(null=False, max_length=100)
    data_nascimento = models.DateTimeField(null=False)

    def __str__(self):
        return self.nome + ' | ' + self.ultimo_nome + ' | ' + self.email

class Comment(models.Model):
    nome_completo = models.CharField(null = False, max_length = 60)
    ultimo_comentario = models.TextField(null = True, default = '', max_length = 400)
    data_comentario = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.nome_completo + ' | ' + self.data_comentario.strftime('%a, %d %b %Y')