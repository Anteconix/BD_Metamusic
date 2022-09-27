from rest_framework.serializers import ModelSerializer

from core.models import Artista

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"