from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import ArtistaViewSet ,AlbumViewSet, NoticiaViewSet, BandaViewSet, MusicaViewSet

router = DefaultRouter()
router.register(r'Artista', ArtistaViewSet)
router.register(r'Album', AlbumViewSet)
router.register(r'Noticia', NoticiaViewSet)
router.register(r'Banda', BandaViewSet)
router.register(r'Musica', MusicaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]