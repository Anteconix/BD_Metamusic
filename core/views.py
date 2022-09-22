from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Artista, Album, Noticia, Banda, Musica

from core.serializers import Artistaserializer, albunserializer, NoticiaSerializer, BandaSerializer, MusicaSerializer

class ArtistaViewSet(ModelViewSet):
    queryset = Artista.objects.all()
    serializer_class = Artistaserializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = albunserializer

class NoticiaViewSet(ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer

class BandaViewSet(ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer