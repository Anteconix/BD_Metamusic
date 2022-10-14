from django.db import models
from .usuario import Usuario

class Comentario(models.Model):
    comentario = models.CharField(max_length=200)
    usuario = Usuario
    data_comentario = models.DateField()

    def __str__(self):
        return self.nome_comentario