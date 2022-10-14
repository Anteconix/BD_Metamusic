from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from media.router import router as media_router
from core.views import ArtistaViewSet ,AlbumViewSet, NoticiaViewSet, BandaViewSet, MusicaViewSet, UsuarioViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r'Artista', ArtistaViewSet)
router.register(r'Album', AlbumViewSet)
router.register(r'Noticia', NoticiaViewSet)
router.register(r'Banda', BandaViewSet)
router.register(r'Musica', MusicaViewSet)
router.register(r'Usuario', UsuarioViewSet)
router.register(r'Comentario', ComentarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('', include(router.urls)),
    path("api/media/", include(media_router.urls)),

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
