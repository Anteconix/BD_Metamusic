from xml.etree.ElementTree import Comment
from rest_framework.serializers import ModelSerializer

from core.models import Comentario
from core.serializers import CustomUserDetailNestedSerializer

class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


class ComentarioDetailSerializer(ModelSerializer):
    criado_por = CustomUserDetailNestedSerializer()

    class Meta:
        model = Comentario
        fields = "__all__"
        depth = 1
