from django.db import models

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=255)
    
    def __str__(self):
        return self.titulo_noticia
    dt_noticia = models.DateField(auto_now_add=True)
    subtitulo = models.CharField(max_length=255, null=True)
    texto = models.TextField(null=True)
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
