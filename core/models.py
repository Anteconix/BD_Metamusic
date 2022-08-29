import email
from django.db import models

class Usuario(models.Model):
    email = models.CharField(max_length=100, notnull=True)
    dt_nasc_usuario = models.DateField(notnull=True)
    id_usuario = models.PrimaryKey( auto_created=True, primary_key=True)
    nome_usuario = models.CharField(max_length=100, notnull=True)
    senha = models.CharField(max_length=100, notnull=True)

class Artista(models.Model):
    