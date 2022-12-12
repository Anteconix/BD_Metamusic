from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Artista
from media.models import Image
from media.serializers import ImageSerializer

class ArtistaSerializer(ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"

    foto_artista_attachment_key = SlugRelatedField(
        source="foto_artista",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto_artista = ImageSerializer(required=False, read_only=True) 

