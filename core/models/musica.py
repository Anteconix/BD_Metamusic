from django.db import models
from .album import Album

class Musica(models.Model):
    titulo_musica = models.CharField(max_length=255)
    tempo_musica = models.TimeField()

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="musicas")

    def __str__(self):
        return self.titulo_musica