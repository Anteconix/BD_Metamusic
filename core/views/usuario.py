from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import Usuario
from core.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]