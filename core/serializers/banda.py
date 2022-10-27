from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Banda
from media.models import Image
from media.serializers import ImageSerializer

class BandaSerializer(ModelSerializer):
    class Meta:
        model = Banda
        fields = "__all__"
    foto_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)    