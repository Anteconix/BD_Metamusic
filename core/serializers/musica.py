from rest_framework.serializers import ModelSerializer
from core.models import Musica

class MusicaSerializer(ModelSerializer):
    class Meta:
        model = Musica
        fields = "__all__"