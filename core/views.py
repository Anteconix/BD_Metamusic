from rest_framework.viewsets import ModelViewSet

from core.models import Usuario, Artista, Album, Noticias, Banda_Grupo, Musica

from core.serializers import UsuarioSerializer, ArtistaSerializer, AlbumSerializer, NoticiasSerializer, Banda_GrupoSerializer, MusicaSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class NoticiasViewSet(ModelViewSet):
    queryset = Noticias.objects.all()
    serializer_class = NoticiasSerializer

class Banda_GrupoViewSet(ModelViewSet):
    queryset = Banda_Grupo.objects.all()
    serializer_class = Banda_GrupoSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer