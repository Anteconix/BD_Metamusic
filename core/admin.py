from django.contrib import admin
from core.models import Artista, Album, Noticia, Banda, Musica, Usuario, Comentario
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models.comentario import Comentario

admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Noticia)
admin.site.register(Banda)
admin.site.register(Musica)
admin.site.register(Comentario)



class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "cpf", "telefone", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

admin.site.register(Usuario, UserAdmin)