from django.db import models

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=255)
    dt_noticia = models.DateField(auto_now_add=True)
    subtitulo = models.CharField(max_length=255)
    conteudo_noticia = models.TextField(max_length=255)

    def __str__(self):
        return self.titulo_noticia