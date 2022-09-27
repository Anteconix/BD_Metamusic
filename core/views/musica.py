from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Musica

from core.serializers import MusicaSerializer

class MusicaViewSet(ModelViewSet):
    queryset = Musica.objects.all()
    serializer_class = MusicaSerializer