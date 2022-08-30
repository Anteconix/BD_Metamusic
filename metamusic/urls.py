from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import UsuarioViewSet, ArtistaViewSet, AlbumViewSet, NoticiasViewSet, Banda_GrupoViewSet, MusicaViewSet

router = DefaultRouter()
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Artista', ArtistaViewSet)
router.register(r'Album', AlbumViewSet)
router.register(r'Noticias', NoticiasViewSet)
router.register(r'Banda_Grupo', Banda_GrupoViewSet)
router.register(r'Musica', MusicaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]