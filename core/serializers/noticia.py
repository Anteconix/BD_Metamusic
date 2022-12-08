from rest_framework.serializers import ModelSerializer
from core.models import Noticia

class NoticiaSerializer(ModelSerializer):
    class Meta:
        model = Noticia
        fields = "__all__"
    
    foto_noticia_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto_noticia = ImageSerializer(required=False, read_only=True)   