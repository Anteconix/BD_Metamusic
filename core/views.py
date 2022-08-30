from rest_framework.viewsets import ModelViewSet

from core.models import Usuario, Artista, Album, Noticias, Banda_Grupo, Musica
from core.serializers import UsuarioSerializer, ArtistaSerializer, AlbumSerializer, NoticiasSerializer, Banda_GrupoSerializer, MusicaSerializer

class UsuarioSerializer(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ArtistaSerializer(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumSerializer(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class NoticiasSerializer(ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer

class Banda_GrupoSerializer(ModelViewSet):
    queryset = Banda_Grupo.objects.all()
    serializer_class = Banda_GrupoSerializer

class MusicaSerializer(ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer