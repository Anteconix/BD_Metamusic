from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Editora

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"


class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"