
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=18)
    texto   = models.TextField(max_length=200, blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, null=True)
    escolaridade = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome