from django.db import models

class Artista(models.Model):
    nome_artista = models.CharField(max_length=100)
    dt_nasc = models.DateField()

    def __str__(self):
        return self.nome_artista