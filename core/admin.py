from django.contrib import admin

from core.models import Usuario, Artista, Album, Noticias, Banda_Grupo, Musica

admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Noticias)
admin.site.register(Banda_Grupo)
admin.site.register(Musica)