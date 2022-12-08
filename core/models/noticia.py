from django.db import models

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=255)
    dt_noticia = models.DateField(auto_now_add=True)
    subtitulo = models.TextField(max_length=255)
    corpo1 = models.TextField(max_length=255)
    corpo2 = models.TextField(max_length=255)
    corpo3 = models.TextField(max_length=255)
    corpo4 = models.TextField(max_length=255)
    corpo5 = models.TextField(max_length=255)

    def __str__(self):
        return self.titulo_noticia