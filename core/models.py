import email
from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=100, notnull=True)
    dt_nasc_usuario = models.DateField(notnull=True)
    id_usuario = models.PrimaryKey(auto_created=True, primary_key=True)
    nome_usuario = models.CharField(max_length=100, notnull=True)
    senha = models.CharField(max_length=100, notnull=True)

class Artista(models.Model):
    nome_artista = models.CharField(max_length=100, notnull=True)
    id_artista = models.PrimaryKey(auto_created=True, primary_key=True)
    dt_nasc_artista = models.DateTimeField(notnull=True)
    biografia = models.TextField(max_length=2500)

class Album(models.Model):
    nome_album = models.CharField(max_length=100, notnull=True)
    id_album = models.PrimaryKey(auto_created=True, primary_key=True)
    numero_musicas = models.IntegerField(max_length=2, notnull=True)
    capa_album = models.BinaryField(binary=True,notnull=True)
    