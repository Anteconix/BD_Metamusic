from django.contrib.auth.models import User
from django.db import models


class Comentario(models.Model):
    criado_por = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comentarios",
    )
    data_comentario = models.DateField(auto_now_add=True)
    quem = models.ManyToManyField(User, related_name="comentarios")
    comentario = models.CharField(max_length=200)

    def __str__(self):
        return self.comentario
