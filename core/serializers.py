from rest_framework.serializers import ModelSerializer

from core.models import Usuario, Artista, Album, Noticias, Banda_Grupo, Musica

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"

class albunserializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"

class NoticiasSerializer(ModelSerializer):
    class Meta:
        model = Noticias
        fields = "__all__"

class Banda_GrupoSerializer(ModelSerializer):
    class Meta:
        model = Banda_Grupo
        fields = "__all__"

class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"