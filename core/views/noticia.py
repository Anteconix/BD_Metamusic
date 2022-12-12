from rest_framework.viewsets import ModelViewSet

from core.models import Noticia
from core.serializers import NoticiaSerializer

class NoticiaViewSet(ModelViewSet):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializer
