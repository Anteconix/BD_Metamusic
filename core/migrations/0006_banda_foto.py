# Generated by Django 4.1.2 on 2022-10-27 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
        ('core', '0005_alter_comentario_data_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='media.image'),
        ),
    ]
