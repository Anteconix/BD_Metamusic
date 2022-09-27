from django.db import models
from .artista import Artista

class Banda(models.Model):
    nome_banda = models.CharField(max_length=100)
    ano_criacao = models.CharField(max_length=4)
    integrantes = models.ManyToManyField(Artista, related_name="bandas")
    desc_banda = models.TextField(max_length=2500)

    def __str__(self):
        return self.nome_banda