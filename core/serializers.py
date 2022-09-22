from rest_framework.serializers import ModelSerializer

from core.models import Artista, Album, Noticia, Banda, Musica

class Artistaserializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"

class albunserializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class NoticiaSerializer(ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"

class BandaSerializer(ModelSerializer):
    class Meta:
        model = Banda
        fields = "__all__"

class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"