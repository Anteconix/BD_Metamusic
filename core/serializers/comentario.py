from xml.etree.ElementTree import Comment
from rest_framework.serializers import ModelSerializer
from core.models import Comentario

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"