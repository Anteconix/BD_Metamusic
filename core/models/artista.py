from django.db import models
from media.models import Image

class Artista(models.Model):
    nome_artista = models.CharField(max_length=100)
    dt_nasc = models.DateField()

    def __str__(self):
        return self.nome_artista
    foto_artista = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )       