from django.db import models
from .usuario import Usuario

class Comentario(models.Model):
    usuario = Usuario
    data_comentario = models.DateField()
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_comentario