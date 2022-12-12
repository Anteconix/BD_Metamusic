from rest_framework.viewsets import ModelViewSet

from core.models import Banda
from core.serializers import BandaSerializer, BandaDetailSerializer

class BandaViewSet(ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BandaDetailSerializer
        return BandaSerializer