from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import Comentario
from core.serializers import ComentarioSerializer, ComentarioDetailSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ComentarioDetailSerializer
        return ComentarioSerializer
