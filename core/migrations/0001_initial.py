# Generated by Django 4.1.2 on 2022-11-29 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("media", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_album", models.CharField(max_length=100)),
                ("numero_musicas", models.IntegerField()),
                ("ano_lancamento", models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name="Artista",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_artista", models.CharField(max_length=100)),
                ("dt_nasc", models.DateField()),
                (
                    "foto_artista",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="media.image",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Noticia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo_noticia", models.CharField(max_length=255)),
                ("dt_noticia", models.DateField(auto_now_add=True)),
                ("conteudo_noticia", models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Musica",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo_musica", models.CharField(max_length=255)),
                ("tempo_musica", models.TimeField()),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="musicas",
                        to="core.album",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comentario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data_comentario", models.DateField(auto_now_add=True)),
                ("comentario", models.CharField(max_length=200)),
                (
                    "criado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comentarios",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Banda",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_banda", models.CharField(max_length=100)),
                ("ano_criacao", models.CharField(max_length=4)),
                (
                    "genero_banda",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("desc_banda", models.TextField(max_length=2500)),
                (
                    "link_spotify",
                    models.TextField(blank=True, max_length=2500, null=True),
                ),
                (
                    "capa_banda",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="media.image",
                    ),
                ),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="media.image",
                    ),
                ),
                (
                    "integrantes",
                    models.ManyToManyField(related_name="bandas", to="core.artista"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="album",
            name="banda",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="albuns",
                to="core.banda",
            ),
        ),
        migrations.AddField(
            model_name="album",
            name="capa_album",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="media.image",
            ),
        ),
    ]
