from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from core.models import Album
from core.serializers import AlbumSerializer

class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [AllowAny]