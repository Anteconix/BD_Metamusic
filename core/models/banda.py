from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from media.models import Image
from .artista import Artista

from media.models import Image

class Banda(models.Model):
    nome_banda = models.CharField(max_length=100)
    ano_criacao = models.CharField(max_length=4)
    integrantes = models.ManyToManyField(Artista, related_name="bandas")
    genero_banda = models.CharField(max_length=200, null=True, blank=True)
    desc_banda = models.TextField(max_length=2500)
    link_spotify = models.TextField(max_length=2500, null=True, blank=True)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )
    

    def __str__(self):
        return self.nome_banda

    capa_banda = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )