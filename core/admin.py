from django.contrib import admin
from core.models import Artista, Album, Noticia, Banda, Musica, Comentario
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.comentario import Comentario

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Noticia)
admin.site.register(Banda)
admin.site.register(Musica)
admin.site.register(Comentario)
