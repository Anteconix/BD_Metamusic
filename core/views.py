from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Artista, Album, Noticia, Banda, Musica

from core.serializers import ArtistaSerializer, AlbumSerializer, NoticiaSerializer, BandaSerializer, MusicaSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class NoticiaViewSet(ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class BandaViewSet(ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer