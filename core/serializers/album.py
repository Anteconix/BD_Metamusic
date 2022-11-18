from rest_framework.serializers import ModelSerializer, SlugRelatedField
from core.models import Album
from media.models import Image
from media.serializers import ImageSerializer
 
class AlbumSerializer(ModelSerializer):
   class Meta:
       model = Album
       fields = "__all__"
   foto_attachment_key = SlugRelatedField(
       source="foto",
       queryset=Image.objects.all(),
       slug_field="attachment_key",
       required=False,
       write_only=True,
   )
   foto = ImageSerializer(required=False, read_only=True)   
   capa_album_attachment_key = SlugRelatedField(
       source="capa_album",
       queryset=Image.objects.all(),
       slug_field="attachment_key",
       required=False,
       write_only=True,
   )
   capa_album = ImageSerializer(required=False, read_only=True)   