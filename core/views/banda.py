from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Banda

from core.serializers import BandaSerializer

class BandaViewSet(ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer