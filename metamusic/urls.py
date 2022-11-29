from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from core.views import (
    ArtistaViewSet,
    AlbumViewSet,
    NoticiaViewSet,
    BandaViewSet,
    MusicaViewSet,
    ComentarioViewSet,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from media.router import router as media_router

router = DefaultRouter()
router.register(r"Artista", ArtistaViewSet)
router.register(r"Album", AlbumViewSet)
router.register(r"Noticia", NoticiaViewSet)
router.register(r"Banda", BandaViewSet)
router.register(r"Musica", MusicaViewSet)
router.register(r"Comentario", ComentarioViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("api/media/", include(media_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
