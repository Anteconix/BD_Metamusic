from rest_framework.serializers import ModelSerializer

from core.models import Banda

class BandaSerializer(ModelSerializer):
    class Meta:
        model = Banda
        fields = "__all__"