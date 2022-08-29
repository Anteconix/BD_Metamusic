import email
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
    numero_musicas = models.IntegerField(max_length=2)
    _data = models.TextField(db_column='data', blank=True)
    def set_data(self, data):
        self._data = base64.encodestring(data)
    def get_data(self):
        return base64.decodestring(self._data)
    data = property(get_data, set_data)