from django.db import models


class Artista(models.Model):
    nome_artista = models.CharField(max_length=100)
    dt_nasc = models.DateField()

    def __str__(self):
        return self.nome_artista


class Banda(models.Model):
    nome_banda = models.CharField(max_length=100)
    ano_criacao = models.CharField(max_length=4)
    integrantes = models.ManyToManyField(Artista, related_name="bandas")
    desc_banda = models.TextField(max_length=2500)

    def __str__(self):
        return self.nome_banda


class Album(models.Model):
    nome_album = models.CharField(max_length=100)
    numero_musicas = models.IntegerField()
    ano_lancamento = models.CharField(max_length=4)

    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name="albuns")

    def __str__(self):
        return self.nome_album


class Musica(models.Model):
    titulo_musica = models.CharField(max_length=255)
    tempo_musica = models.TimeField()

    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="musicas")

    def __str__(self):
        return self.titulo_musica


class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=255)
    dt_noticia = models.DateField(auto_now_add=True)
    conteudo_noticia = models.TextField(max_length=255)

    def __str__(self):
        return self.titulo_noticia
