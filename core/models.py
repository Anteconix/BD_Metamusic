from pyexpat import model
from django.db import models


class Usuario(models.Model):
    email = models.CharField(max_length=100)
    dt_nasc_usuario = models.DateField()
    id_usuario = models.IntegerField(auto_created=True, primary_key=True)
    nome_usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)


class Artista(models.Model):
    nome_artista = models.CharField(max_length=100)
    id_artista = models.IntegerField(auto_created=True, primary_key=True)
    dt_nasc_artista = models.DateTimeField()
    biografia = models.TextField(max_length=2500)


class Album(models.Model):
    nome_album = models.CharField(max_length=100)
    id_album = models.IntegerField(auto_created=True, primary_key=True)
    numero_musicas = models.IntegerField()
    data = models.TextField(db_column='data', blank=True)


class Noticias(models.Model):
    titulo_noticias = models.CharField(max_length=255)
    conteudo_noticia = models.TextField(max_length=255)
    id_noticia = models.IntegerField(auto_created=True, primary_key=True)


class Banda_Grupo(models.Model):
    integrantes = models.CharField(max_length=255)
    id_banda = models.IntegerField(auto_created=True, primary_key=True)
    dt_criacao = models.DateField()
    desc_banda = models.TextField(max_length=2500)
    nome_banda = models.CharField(max_length=100)


class Musica(models.Model):
    titulo_musica = models.CharField(max_length=255)
    id_musica = models.IntegerField(auto_created=True, primary_key=True)
    tempo_musica = models.TimeField()
    artistas = models.ManyToManyField(Artista, related_name="musicas")
