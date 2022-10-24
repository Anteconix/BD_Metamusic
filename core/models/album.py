from django.db import models
from media.models import Image
from django.db import models
from .banda import Banda

class Album(models.Model):
    nome_album = models.CharField(max_length=100)
    numero_musicas = models.IntegerField()
    ano_lancamento = models.CharField(max_length=4)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="albuns")

    def __str__(self):
        return self.nome_album

    capa_album = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
)